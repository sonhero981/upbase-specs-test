#!/usr/bin/env python3
"""Tiện ích kiểm tra cho luồng v2 (theo AWS AI-DLC). Không sửa artifact.

Dùng:
  po-tools.py trace   <intent-dir> [--write]
      Dựng bảng truy vết FR, US, BR từ requirements.md, stories.md và prd.md (nếu có).
      In bảng. Mã thoát 1 khi có GAP hoặc ORPHAN. --write ghi
      inception/prd/traceability.md và verification/phase-check-inception.md.
  po-tools.py archive <intent-dir> <stage-slug> <artifact> [--label <nhãn>]
      Chép artifact vào archive/<slug>/<tên>-v<version>-<YYYYMMDD>.md,
      hoặc -<nhãn>-<YYYYMMDD>.md khi có --label. Từ chối ghi đè.
  po-tools.py status  [intents-root]
      Bảng trạng thái mọi intent và tám kiểm tra lệch giữa state.md và đĩa.
      Mặc định intents-root là .claude/intents cạnh script.
Chỉ dùng thư viện chuẩn, chạy được với Python 3.9.
"""
import datetime
import re
import shutil
import sys
from pathlib import Path

STAGE_DIRS = {
    "intent-capture": "ideation/intent-capture",
    "market-research": "ideation/market-research",
    "scope-definition": "ideation/scope-definition",
    "approval-handoff": "ideation/approval-handoff",
    "requirements-analysis": "inception/requirements-analysis",
    "impact-analysis": "inception/impact-analysis",
    "solution-options": "inception/solution-options",
    "user-stories": "inception/user-stories",
    "hld-brief": "inception/hld-brief",
    "prd-generation": "inception/prd",
}
MAIN_ARTIFACT = {
    "intent-capture": "intent-statement.md",
    "market-research": "competitive-analysis.md",
    "scope-definition": "scope-document.md",
    "approval-handoff": "initiative-brief.md",
    "requirements-analysis": "requirements.md",
    "impact-analysis": "impact-matrix.md",
    "solution-options": "solution-options.md",
    "user-stories": "stories.md",
    "hld-brief": "hld-brief.md",
    "prd-generation": "prd.md",
}
QUESTIONS_FILE = {"prd-generation": "field-intake-questions.md"}
VERSION_ROWS = {
    "initiative-brief": "ideation/approval-handoff/initiative-brief.md",
    "hld-brief": "inception/hld-brief/hld-brief.md",
    "prd": "inception/prd/prd.md",
}
FR_RE = re.compile(r"\bN?FR\d+(?:\.\d+)?\b")
ID_FR = re.compile(r"N?FR\d+(?:\.\d+)?")
ID_US = re.compile(r"US\d+")


def read(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except (FileNotFoundError, NotADirectoryError):
        return None


def frontmatter(text):
    fm = {}
    if not text:
        return fm
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    for ln in lines[1:]:
        if ln.strip() == "---":
            break
        if ":" in ln:
            k, v = ln.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def section(text, heading):
    """Phần văn bản dưới heading (khớp đầu dòng, không phân biệt cấp) tới heading kế."""
    if text is None:
        return ""
    m = re.search(r"^#+\s*" + re.escape(heading) + r"\b.*$", text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = re.search(r"^#+\s", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def table_rows(text):
    rows = []
    for ln in (text or "").splitlines():
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) or c == "" for c in cells):
            continue
        rows.append(cells)
    return rows


def us_key(us):
    return int(us[2:])


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


# ---------------------------------------------------------------- trace
def trace(intent, write=False):
    intent = Path(intent)
    req = read(intent / "inception/requirements-analysis/requirements.md")
    sto = read(intent / "inception/user-stories/stories.md")
    prd = read(intent / "inception/prd/prd.md")
    if req is None or sto is None:
        print("Thiếu requirements.md hoặc stories.md trong", intent)
        return 2

    frs = []
    for cells in table_rows(req):
        if cells and ID_FR.fullmatch(cells[0]) and cells[0] not in frs:
            frs.append(cells[0])

    us_fr, us_round = {}, {}
    for cells in table_rows(section(sto, "Danh sách") or sto):
        if cells and ID_US.fullmatch(cells[0]):
            us = cells[0]
            us_fr[us] = set(FR_RE.findall(" ".join(cells[1:])))
            last = cells[-1].lower()
            us_round[us] = not ("không" in last or "chưa" in last)

    explicit = {}
    for cells in table_rows(section(sto, "FR sang US")):
        if len(cells) >= 3 and ID_FR.fullmatch(cells[0]):
            explicit[cells[0]] = (cells[1], cells[2])

    gaps, orphans = [], []
    fr_rows = []
    for fr in frs:
        uss = sorted([u for u, s in us_fr.items() if fr in s], key=us_key)
        st = explicit.get(fr, ("", ""))[1]
        if uss:
            status = "OK"
        elif st.lower().startswith(("deferred", "n/a")):
            status = st
        else:
            status = "GAP"
            gaps.append("%s chưa có US" % fr)
        fr_rows.append((fr, ", ".join(uss) or explicit.get(fr, ("—", ""))[0] or "—", status))

    us_rows = []
    for us in sorted(us_fr, key=us_key):
        if us_fr[us]:
            us_rows.append((us, ", ".join(sorted(us_fr[us])), "OK"))
        else:
            us_rows.append((us, "—", "ORPHAN"))
            orphans.append("%s không truy về FR nào" % us)
        for fr in sorted(us_fr[us]):
            if fr not in frs:
                us_rows.append((us, fr, "ORPHAN"))
                orphans.append("%s trỏ tới %s không có trong requirements.md" % (us, fr))

    br_rows, prd_note = [], "chưa có prd.md, bỏ kiểm US sang PRD và BR"
    if prd is not None:
        prd_us = re.findall(r"^##\s+(US\d+)\b", prd, re.M)
        for us in sorted(us_fr, key=us_key):
            if us_round.get(us) and us not in prd_us:
                gaps.append("%s làm đợt này nhưng chưa có trong prd.md" % us)
        for us in prd_us:
            if us not in us_fr:
                orphans.append("%s có trong prd.md nhưng không có trong stories.md" % us)
        brs = sorted(set(re.findall(r"\bBR-?(\d+)\.(\d+)\b", prd)), key=lambda t: (int(t[0]), int(t[1])))
        for a, b in brs:
            us = "US%s" % a
            ok = us in prd_us
            br_rows.append(("BR%s.%s" % (a, b), us, "OK" if ok else "ORPHAN"))
            if not ok:
                orphans.append("BR%s.%s thuộc %s không có trong prd.md" % (a, b, us))
        prd_note = "%d US trong prd.md, %d BR" % (len(prd_us), len(brs))

    today = datetime.date.today().isoformat()
    result = "Đạt" if not gaps and not orphans else "Không đạt"
    body = [
        "# Traceability: %s" % intent.name,
        "",
        "Kiểm ngày %s bằng po-tools.py. Trạng thái: OK có đích · GAP chưa có · ORPHAN không truy về đâu · Deferred, N/A ghi ở stories.md." % today,
        "",
        "## FR sang US",
        md_table(["FR", "US", "Trạng thái"], fr_rows),
        "",
        "## US sang FR",
        md_table(["US", "FR", "Trạng thái"], us_rows),
        "",
        "## BR sang US",
        md_table(["BR", "US", "Trạng thái"], br_rows) if br_rows else "_%s_" % prd_note,
        "",
        "## Kết luận",
        "%s. GAP: %d. ORPHAN: %d." % (result, len(gaps), len(orphans)),
    ]
    for p in gaps:
        body.append("- GAP: " + p)
    for p in orphans:
        body.append("- ORPHAN: " + p)
    text = "\n".join(body) + "\n"
    print(text)

    if write:
        out = intent / "inception/prd/traceability.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("---\nintent: %s\nartifact: traceability\nchecked: %s\n---\n" % (intent.name, today) + text, encoding="utf-8")
        pc = intent / "verification/phase-check-inception.md"
        pc.parent.mkdir(parents=True, exist_ok=True)
        pc_rows = [
            ("1", "Mọi FR có US, hoặc Deferred, N/A có lý do", "Đạt" if not [g for g in gaps if "chưa có US" in g] else "Không đạt"),
            ("2", "Mọi US truy về FR có thật", "Đạt" if not [o for o in orphans if "FR" in o] else "Không đạt"),
            ("3", "Mọi US làm đợt này có trong PRD", "Đạt" if prd is not None and not [g for g in gaps if "prd.md" in g] else ("Chưa kiểm" if prd is None else "Không đạt")),
            ("4", "Mọi BR thuộc một US có trong PRD", "Đạt" if prd is not None and not [o for o in orphans if o.startswith("BR")] else ("Chưa kiểm" if prd is None else "Không đạt")),
        ]
        pc.write_text(
            "---\nintent: %s\nphase: inception\ndate: %s\nresult: %s\n---\n# Phase check: INCEPTION · %s\n\nSinh bởi po-tools.py trace. Điều kiện ngữ nghĩa (OQ chặn đã đóng, HLD Brief đủ chữ ký) AI kiểm thêm theo template phase-check.md.\n\n%s\n\n## Kết luận\n%s. GAP: %d. ORPHAN: %d. Chi tiết trong inception/prd/traceability.md.\n"
            % (intent.name, today, result, intent.name, md_table(["#", "Điều kiện", "Kết quả"], pc_rows), result, len(gaps), len(orphans)),
            encoding="utf-8",
        )
        print("Đã ghi:", out, "và", pc)
    return 0 if result == "Đạt" else 1


# -------------------------------------------------------------- archive
def archive(intent, slug, artifact, label=None):
    intent = Path(intent)
    src = Path(artifact)
    if not src.is_absolute() and not src.exists():
        src = intent / artifact
    if not src.exists():
        print("Không thấy artifact:", src)
        return 2
    fm = frontmatter(read(src))
    tag = label or ("v" + fm.get("version", "0"))
    today = datetime.date.today().strftime("%Y%m%d")
    dst_dir = intent / "archive" / slug
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / ("%s-%s-%s.md" % (src.stem, tag, today))
    if dst.exists():
        print("Đã có, không ghi đè:", dst, "— dùng --label để đặt tên khác")
        return 2
    shutil.copy2(src, dst)
    print("Đã chụp:", dst)
    return 0


# --------------------------------------------------------------- status
def status(root):
    root = Path(root)
    if not root.exists():
        print("Không thấy thư mục", root)
        return 2
    intents = sorted(p for p in root.iterdir() if p.is_dir() and (p / "state.md").exists())
    today = datetime.date.today()
    rows, findings = [], []
    for it in intents:
        st = read(it / "state.md")
        fm = frontmatter(st)
        stages = re.findall(r"^- \[(.)\] (\S+) (\S+)(.*)$", st, re.M)
        cur = {}
        for c in table_rows(section(st, "Current")):
            if len(c) >= 2:
                cur[c[0]] = c[1]
        vers = {}
        for c in table_rows(section(st, "Versions")):
            if len(c) >= 5 and c[0] != "Artifact":
                vers[c[0]] = c
        word = {"-": "đang làm", "?": "chờ duyệt", "R": "đang sửa", " ": "chưa bắt đầu"}
        active = next(((n, s, m) for m, n, s, _ in stages if m in "-?R"), None)
        if active is None:
            active = next(((n, s, m) for m, n, s, _ in stages if m == " "), None)
        if active is None:
            stage_txt, state_txt = "—", "xong"
        else:
            stage_txt, state_txt = "%s %s" % (active[0], active[1]), word.get(active[2], active[2])
        if fm.get("status", "").lower() in ("archived", "rejected", "parked"):
            state_txt = fm["status"]
        lark = " · ".join("%s %s" % (k, v[4]) for k, v in vers.items() if v[4] and v[4] not in ("—", "-"))
        rows.append((it.name, fm.get("profile", "?"), stage_txt, state_txt, cur.get("Next action", ""), cur.get("Blocking questions open", ""), cur.get("Open CR", ""), lark or "—"))

        dec = read(it / "decisions.md") or ""
        dec_stages = [c[2] for c in table_rows(dec) if len(c) > 2 and re.fullmatch(r"DEC\d+", c[0])]
        for m, n, slug, rest in stages:
            d = it / STAGE_DIRS.get(slug, "inception/" + slug)
            main = d / MAIN_ARTIFACT.get(slug, "")
            legacy = re.search(r"v1:\s*([^\s·,]+)", rest)
            if legacy:
                # artifact kế thừa từ luồng v1: kiểm file được trỏ tới, không đòi archive theo slug
                if not (it / legacy.group(1)).exists():
                    findings.append((it.name, "1. %s %s trỏ v1: %s nhưng file không có" % (n, slug, legacy.group(1)), "Sửa đường dẫn trong state.md"))
                main = None
            if m == "x" and main is not None:
                if not main.exists():
                    findings.append((it.name, "1. %s %s đã [x] nhưng thiếu %s" % (n, slug, main.relative_to(it)), "Kiểm lại state hoặc artifact"))
                arch = it / "archive" / slug
                if not arch.exists() or not any(arch.glob("*.md")):
                    findings.append((it.name, "1. %s %s đã [x] nhưng archive/%s/ trống" % (n, slug, slug), "Chụp bản duyệt: po-tools.py archive"))
            if m == "x" and not any((ds.split() or [""])[0] == n or slug in ds for ds in dec_stages):
                findings.append((it.name, "4. %s %s đã [x] nhưng decisions.md không có DEC của stage" % (n, slug), "Ghi DEC nguyên văn lời duyệt"))
            if m == " " and main is not None and main.exists():
                findings.append((it.name, "2. %s có trên đĩa nhưng %s %s còn [ ]" % (main.relative_to(it), n, slug), "Cập nhật state.md"))
            if m in "?xR":
                q = read(d / QUESTIONS_FILE.get(slug, slug + "-questions.md"))
                if q:
                    for block in re.split(r"^## ", q, flags=re.M)[1:]:
                        if re.search(r"^Chặn:\s*có", block, re.M | re.I):
                            ans = re.search(r"^\[Answer\]:(.*)$", block, re.M)
                            if ans and not ans.group(1).strip():
                                qid = block.split(".")[0].strip()
                                findings.append((it.name, "5. %s %s: %s chặn chưa trả lời nhưng stage đã [%s]" % (n, slug, qid, m), "Trả lời hoặc hạ cờ chặn"))
            if m in "?-":
                age = (today - datetime.date.fromtimestamp((it / "state.md").stat().st_mtime)).days
                if age > 7:
                    findings.append((it.name, "6. %s %s ở [%s] đã %d ngày không đổi" % (n, slug, m, age), "Nhắc PO, hoặc park"))
        for name, rel in VERSION_ROWS.items():
            row = vers.get(name)
            f = it / rel
            if row and f.exists():
                v_state = row[1].lstrip("v")
                v_file = frontmatter(read(f)).get("version", "")
                if v_state and v_file and v_state != v_file:
                    findings.append((it.name, "3. %s: state ghi v%s, file ghi v%s" % (name, v_state, v_file), "Đồng bộ state.md"))
                mv = re.search(r"v(\d+\.\d+)", row[4])
                if mv and v_file and mv.group(1) != v_file:
                    findings.append((it.name, "7. %s: Lark đang v%s, file đang v%s" % (name, mv.group(1), v_file), "Publish lại, hoặc ghi chú vì sao chưa"))
        im = read(it / "intent.md") or ""
        for c in table_rows(section(im, "Related intents")):
            ref = c[0].strip("`").strip()
            if not ref or ref.startswith("<") or ref.lower().startswith("intent"):
                continue
            if not (root / ref).exists():
                findings.append((it.name, "8. Related intents trỏ tới '%s' không tồn tại" % ref, "Sửa intent.md"))

    print("## Intent, luồng v2\n")
    if rows:
        print(md_table(["Intent", "Profile", "Stage", "Trạng thái", "Việc kế tiếp", "Câu chặn", "CR mở", "Lark"], rows))
    else:
        print("_Chưa có intent nào trong %s_" % root)
    print("\n## Kiểm tra lệch\n")
    if findings:
        print(md_table(["Intent", "Lệch", "Gợi ý xử lý"], findings))
    else:
        print("state khớp với đĩa")
    return 1 if findings else 0


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, args = argv[1], argv[2:]
    if cmd == "trace" and args:
        return trace(args[0], write="--write" in args)
    if cmd == "archive" and len(args) >= 3:
        label = args[args.index("--label") + 1] if "--label" in args and args.index("--label") + 1 < len(args) else None
        return archive(args[0], args[1], args[2], label)
    if cmd == "status":
        default_root = Path(__file__).resolve().parent.parent / "intents"
        return status(args[0] if args else default_root)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
