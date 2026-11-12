"""tech-tools.py - sensor cho phần Tech (AWS AI-DLC layout + plugin tech-workflow).

  check <intent-dir> [--stage=<slug>] [--unit=<unit-name>] [--bolt=<Bnn>] [--write]
      Không --stage: kiểm toàn chuỗi US -> Unit -> Bolt -> TC (dùng ở 2.9 trở đi).
      --stage=reverse-engineering  codekb mỗi repo đủ 9 file AWS, có "## Scope of Analysis"
      --stage=domain-design        components.md có khối yaml parse được, decisions.md có ADR
      --stage=units-generation     DAG yaml `units:` parse được, không vòng; mỗi US đợt này đúng một Unit
      --stage=contract-design      mọi khối yaml trong contract-summary.md parse được; có "Approved by" khi Agreed
      --stage=test-cases           mỗi US có TC (Happy + Negative/Edge), mọi BR của US đợt này có TC
      --stage=functional-design    cần --unit; đủ file; traceability.json: AC OK trỏ BR có trong rules.md
      --stage=code-generation      cần --bolt; mỗi Unit của Bolt có code-generation-plan.md; change Bolt đã mở
      --write  ghi kết quả chuỗi vào bolt-plan.md giữa <!-- trace:start --> / <!-- trace:end -->
  trace <intent-dir> ...  = check (tên cũ)
Mã thoát 1 khi có lỗi.
"""
import json
import re
import sys
from pathlib import Path

import yaml

sys.stdout.reconfigure(encoding="utf-8")

AWS_CODEKB = ["business-overview", "architecture", "code-structure", "api-documentation", "component-inventory",
              "technology-stack", "dependencies", "code-quality-assessment", "reverse-engineering-timestamp"]


def read(p):
    p = Path(p)
    return p.read_text(encoding="utf-8") if p.exists() else ""


def rows(text, heading=None):
    """Dòng bảng markdown; có heading thì chỉ lấy bảng đầu tiên sau heading đó."""
    out, inside = [], heading is None
    for line in text.splitlines():
        if heading and line.startswith("#") and heading.lower() in line.lower():
            inside = True
            continue
        if heading and inside and line.startswith("#") and out:
            break
        if inside and line.startswith("|"):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
            if not set("".join(cells)) <= set("-: "):
                out.append(cells)
    return out


def ids(text, prefix):
    return re.findall(r"\b%s\d+\b" % prefix, text or "")


def yaml_blocks(text):
    return re.findall(r"```ya?ml\n(.*?)```", text, flags=re.S)


def unit_id(name):
    m = re.match(r"u(\d+)", name or "", flags=re.I)
    return "U%s" % m.group(1) if m else name


class Intent:
    def __init__(self, path):
        self.dir = Path(path).resolve()
        # Gốc store là thư mục tổ tiên có `openspec/`. Không đếm cứng số cấp: bố cục `intents/<slug>` (nay)
        # và `.claude/intents/<slug>` (cũ) sâu khác nhau.
        self.store = next((p for p in self.dir.parents if (p / "openspec").is_dir()), self.dir.parents[1])
        self.slug = self.dir.name
        self.problems = []

    def p(self, rel):
        return self.dir / rel

    def scope_us(self):
        state = read(self.p("tech-state.md"))
        m = re.search(r"^\| Phạm vi đợt này \| (.*?) \|$", state, flags=re.M)
        if m and ids(m.group(1), "US"):
            return ids(m.group(1), "US")
        stories = read(self.p("inception/user-stories/stories.md"))
        us = [r[0] for r in rows(stories, "Danh sách") if r and re.match(r"US\d+$", r[0])
              and (len(r) < 7 or "không" not in r[6].lower())]
        if us:
            return us
        prd = read(self.p("inception/prd/prd.md"))
        return [m.group(1) for m in re.finditer(r"^## (US\d+):(.*)$", prd, flags=re.M) if "chưa làm" not in m.group(2).lower()]

    def dag(self):
        text = read(self.p("inception/units-generation/unit-of-work-dependency.md"))
        for block in yaml_blocks(text):
            try:
                data = yaml.safe_load(block)
            except yaml.YAMLError as e:
                self.problems.append("DAG: yaml lỗi (%s)" % str(e).splitlines()[0])
                return None
            if isinstance(data, dict) and "units" in data:
                units = data["units"]
                if isinstance(units, list):
                    units = {u.get("name"): u for u in units if isinstance(u, dict)}
                return {k: (v or {}) for k, v in units.items()}
        return None

    def story_map(self):
        text = read(self.p("inception/units-generation/unit-of-work-story-map.md"))
        m = {}
        for r in rows(text):
            us = ids(r[0], "US")
            units = [unit_id(x) for c in r[1:] for x in re.findall(r"\bu\d+[\w-]*|\bU\d+\b", c, flags=re.I)]
            for u in us:
                for x in units:
                    if x not in m.setdefault(u, []):
                        m[u].append(x)
        return m

    def bolts(self):
        """Bảng tóm tắt đầu tiên có header | Bolt | Units | … trong bolt-plan.md."""
        text = read(self.p("inception/delivery-planning/bolt-plan.md"))
        out, table = {}, []
        for line in text.splitlines() + [""]:
            if line.startswith("|"):
                table.append([c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))])
                continue
            if table:
                head = [h.lower() for h in table[0]]
                if head and head[0] == "bolt" and "units" in head:
                    col = head.index("units")
                    for r in table[2:]:
                        m = re.match(r"(B\d+)", r[0])
                        if m and len(r) > col:
                            out[m.group(1)] = [unit_id(x) for x in re.findall(r"\bU\d+\b|\bu\d+[\w-]*", r[col], flags=re.I)]
                    return out
                table = []
        return out

    def changes(self):
        return [p.name for p in (self.store / "openspec/changes").glob("*") if p.is_dir()]


def check_dag(it):
    dag = it.dag()
    if dag is None:
        it.problems.append("DAG: thiếu khối ```yaml units: trong unit-of-work-dependency.md")
        return {}
    names = set(dag)
    for n, v in dag.items():
        for d in v.get("depends_on") or []:
            if d not in names:
                it.problems.append("DAG: %s phụ thuộc %s không tồn tại" % (n, d))
    seen, stack = set(), set()

    def visit(n):
        if n in stack:
            it.problems.append("DAG: có vòng qua %s" % n)
            return
        if n in seen:
            return
        stack.add(n)
        for d in dag.get(n, {}).get("depends_on") or []:
            if d in names:
                visit(d)
        stack.discard(n)
        seen.add(n)
    for n in dag:
        visit(n)
    return dag


def check_units(it):
    dag = check_dag(it)
    smap = it.story_map()
    for us in it.scope_us():
        u = smap.get(us, [])
        if not u:
            it.problems.append("GAP: %s chưa có Unit" % us)
        elif len(u) > 1:
            it.problems.append("DUP-US: %s nằm ở %s" % (us, ", ".join(u)))
    return dag


def check_tc(it):
    text = read(it.p("inception/test-cases/test-cases.md"))
    if not text:
        it.problems.append("TC: chưa có inception/test-cases/test-cases.md")
        return 0
    tc = [r for r in rows(text) if r and re.match(r"TC-\d+$", r[0])]
    kinds = {}
    for r in tc:
        for us in ids(r[1] if len(r) > 1 else "", "US"):
            kinds.setdefault(us, set()).add((r[6] if len(r) > 6 else "").strip().lower())
    scope = it.scope_us()
    for us in scope:
        k = kinds.get(us, set())
        if not k:
            it.problems.append("TC-GAP: %s chưa có test case" % us)
        elif "happy" not in k or not (k & {"negative", "edge"}):
            it.problems.append("TC-GAP: %s thiếu Happy hoặc Negative/Edge" % us)
    prd = read(it.p("inception/prd/prd.md"))
    norm = lambda s: s.replace("-", "")
    nums = {u[2:] for u in scope}
    br_prd = {norm(b) for b in re.findall(r"\bBR-?\d+\.\d+[a-z]?\b", prd) if re.match(r"BR-?(\d+)\.", b).group(1) in nums}
    br_tc = {norm(b) for b in re.findall(r"\bBR-?\d+\.\d+[a-z]?\b", text)}
    for a, b, c, d in re.findall(r"\bBR-?(\d+)\.(\d+)\s*[–-]\s*(?:BR-?)?(\d+)\.(\d+)\b", text):
        if a == c:
            br_tc |= {"BR%s.%d" % (a, i) for i in range(int(b), int(d) + 1)}
    for b in sorted(br_prd - br_tc, key=lambda x: [int(n) for n in re.findall(r"\d+", x)]):
        it.problems.append("TC-GAP: %s chưa có test case" % b)
    return len(tc)


def check_codekb(it):
    root = it.store / "engine/tech/knowledge/codekb"
    repos = [d for d in root.iterdir() if d.is_dir()] if root.exists() else []
    for d in repos:
        have = {f.stem for f in d.glob("*.md")}
        if not have & set(AWS_CODEKB):
            continue  # repo chỉ có file vùng theo layout cũ
        for a in AWS_CODEKB:
            if a not in have:
                it.problems.append("CODEKB: %s thiếu %s.md" % (d.name, a))
        if "## Scope of Analysis" not in read(d / "reverse-engineering-timestamp.md"):
            it.problems.append("CODEKB: %s thiếu '## Scope of Analysis'" % d.name)


def check_yaml_file(it, rel, need=None):
    text = read(it.p(rel))
    if not text:
        it.problems.append("FILE: chưa có %s" % rel)
        return text
    blocks = yaml_blocks(text)
    if need and not blocks:
        it.problems.append("YAML: %s thiếu khối ```yaml (%s)" % (rel, need))
    for i, b in enumerate(blocks, 1):
        try:
            yaml.safe_load(b)
        except yaml.YAMLError as e:
            it.problems.append("YAML: %s khối %d lỗi (%s)" % (rel, i, str(e).splitlines()[0]))
    return text


def check_functional(it, unit):
    if not unit:
        it.problems.append("ARG: --stage=functional-design cần --unit=<unit-name>")
        return
    base = "construction/%s/functional-design/" % unit
    for f in ["entities.md", "rules.md", "functional-spec.md"]:
        if not it.p(base + f).exists():
            it.problems.append("FILE: chưa có %s" % (base + f))
    rules = read(it.p(base + "rules.md"))
    br = set(re.findall(r"\bBR\d+\.\d+[a-z]?\b", rules))
    tj = it.p(base + "traceability.json")
    if not tj.exists():
        it.problems.append("FILE: chưa có %straceability.json" % base)
        return
    try:
        data = json.loads(read(tj))
    except json.JSONDecodeError as e:
        it.problems.append("JSON: traceability.json lỗi (%s)" % e)
        return
    for c in data.get("coverage", []):
        if c.get("status") == "GAP":
            it.problems.append("TRACE: %s chưa có BR" % c.get("id"))
        elif c.get("status") == "OK":
            for t in re.findall(r"BR\d+\.\d+[a-z]?", str(c.get("target", ""))):
                if t not in br:
                    it.problems.append("TRACE: %s trỏ %s không có trong rules.md" % (c.get("id"), t))
    targeted = {t for c in data.get("coverage", []) for t in re.findall(r"BR\d+\.\d+[a-z]?", str(c.get("target", "")))}
    explained = {r.get("id") for r in data.get("reverse", [])}
    for b in sorted(br - targeted - explained):
        it.problems.append("ORPHAN: %s không truy về AC nào" % b)


def check_codegen(it, bolt, dag):
    if not bolt:
        it.problems.append("ARG: --stage=code-generation cần --bolt=<Bnn>")
        return
    units = it.bolts().get(bolt, [])
    names = {unit_id(n): n for n in (dag or {})}
    for u in units:
        name = names.get(u, u)
        if not it.p("construction/%s/code-generation/code-generation-plan.md" % name).exists():
            it.problems.append("FILE: %s chưa có code-generation-plan.md" % name)
    if not any(c.startswith("%s-%s" % (it.slug, bolt.lower())) for c in it.changes()):
        it.problems.append("BOLT: chưa mở change %s-%s-… ở openspec/changes" % (it.slug, bolt.lower()))


def chain(it, write):
    dag = check_units(it)
    bolts = it.bolts()
    bolt_of = {}
    for b, us in bolts.items():
        for u in us:
            bolt_of.setdefault(u, []).append(b)
    for u in [unit_id(n) for n in (dag or {})]:
        if u not in bolt_of:
            it.problems.append("GAP: %s chưa có Bolt" % u)
        elif len(bolt_of[u]) > 1:
            it.problems.append("DUP: %s nằm ở %s" % (u, ", ".join(bolt_of[u])))
    tc = check_tc(it)
    changes = it.changes()
    lines = ["| Bolt | Unit | Change ở store |", "|---|---|---|"]
    for b, us in bolts.items():
        ch = next((c for c in changes if c.startswith("%s-%s" % (it.slug, b.lower()))), "chưa mở")
        lines.append("| %s | %s | %s |" % (b, ", ".join(us), ch))
    report = "\n".join(lines)
    print(report)
    if write:
        p = it.p("inception/delivery-planning/bolt-plan.md")
        plan = read(p)
        body = report + "\n\n" + summary(it, len(dag or {}), len(bolts), tc)
        if "<!-- trace:start -->" in plan:
            plan = re.sub(r"(<!-- trace:start -->\n)(.*?)(<!-- trace:end -->)", lambda m: m.group(1) + body + "\n" + m.group(3), plan, flags=re.S)
        else:
            plan = plan.rstrip("\n") + "\n\n## Traceability\n<!-- trace:start -->\n" + body + "\n<!-- trace:end -->\n"
        p.write_text(plan, encoding="utf-8")
    return len(dag or {}), len(bolts), tc


def summary(it, units, bolts, tc, stage="all", note=""):
    status = "Đạt" if not it.problems else "Không đạt"
    if stage == "all":
        head = "%s. US đợt này: %d · Unit: %d · Bolt: %d · TC: %d · lỗi: %d." % (
            status, len(it.scope_us()), units, bolts, tc, len(it.problems))
    else:
        head = "%s. stage %s%s · lỗi: %d." % (status, stage, note, len(it.problems))
    return "\n".join([head] + ["- " + p for p in it.problems])


def main(argv):
    if len(argv) < 3 or argv[1] not in ("check", "trace"):
        print(__doc__)
        return 2
    opt = {a.split("=", 1)[0][2:]: a.split("=", 1)[1] for a in argv[3:] if a.startswith("--") and "=" in a}
    it = Intent(argv[2])
    stage = opt.get("stage", "all")
    units = bolts = tc = 0
    if stage == "all":
        units, bolts, tc = chain(it, "--write" in argv)
    elif stage == "reverse-engineering":
        check_codekb(it)
    elif stage == "domain-design":
        check_yaml_file(it, "inception/domain-design/components.md", need="component catalogue")
        if "ADR-" not in read(it.p("inception/domain-design/decisions.md")):
            it.problems.append("FILE: decisions.md chưa có ADR")
    elif stage in ("units-generation", "hld"):
        units = len(check_units(it) or {})
    elif stage == "contract-design":
        text = check_yaml_file(it, "inception/contract-design/contract-summary.md", need="OpenAPI/AsyncAPI")
        if re.search(r"\bAgreed\b", text) and "Approved by" not in text:
            it.problems.append("CONTRACT: có contract Agreed nhưng thiếu dòng Approved by")
        dag = it.dag() or {}
        edges = {(unit_id(n), unit_id(d)) for n, v in dag.items() for d in (v.get("depends_on") or [])}
        covered = set()
        for r in rows(text, "Phủ cạnh DAG"):
            m = re.match(r"\s*(U\d+)\s*(?:→|->)\s*(U\d+)", r[0])
            if m and len(r) > 1 and r[1].strip(" -—"):
                covered.add((m.group(1), m.group(2)))
        if edges and not covered:
            it.problems.append("CONTRACT: thiếu bảng '### Phủ cạnh DAG' (| Cạnh (A phụ thuộc B) | Contract | Ghi chú |)")
        for a, b in sorted(edges - covered):
            if covered:
                it.problems.append("CONTRACT: cạnh %s → %s chưa có contract (hoặc lý do) trong bảng Phủ cạnh DAG" % (a, b))
    elif stage in ("test-cases", "tc"):
        tc = check_tc(it)
    elif stage == "functional-design":
        check_functional(it, opt.get("unit"))
    elif stage == "code-generation":
        check_codegen(it, opt.get("bolt"), it.dag())
        opt["note"] = " · %s = %s" % (opt.get("bolt"), ", ".join(it.bolts().get(opt.get("bolt"), [])) or "không có Unit")
    else:
        print("Stage không hỗ trợ:", stage)
        return 2
    print(summary(it, units, bolts, tc, stage, opt.get("note", "") or (" · Unit %s" % opt["unit"] if opt.get("unit") else "")))
    return 1 if it.problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
