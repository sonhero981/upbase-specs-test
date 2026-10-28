#!/usr/bin/env python3
"""Cài khung upbase-specs: sinh .claude/ từ engine/ và workspace.yaml.

Chạy lại bao nhiêu lần cũng an toàn. Không cài phần mềm hệ thống, chỉ in lệnh cài khi thiếu.

    python scripts/setup.py            cài
    python scripts/setup.py --check    chỉ kiểm, không ghi (doctor.py gọi vào đây)
"""
from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OK, WARN, FAIL, SKIP = "[ok]", "[!]", "[X]", "[-]"
report: list[tuple[str, str, str]] = []


def say(level: str, what: str, detail: str = "") -> None:
    report.append((level, what, detail))


def load_workspace() -> dict:
    """Đọc workspace.yaml. Dùng pyyaml nếu có, không thì parser tối giản đủ cho file này."""
    path = ROOT / "workspace.yaml"
    text = io.open(path, encoding="utf-8").read()
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text)
    except ImportError:
        return _mini_yaml(text)


def _scalar(v: str) -> str:
    v = v.strip()
    if v[:1] in ('"', "'") and v[-1:] == v[:1] and len(v) >= 2:
        return v[1:-1]
    return v


def _mini_yaml(text: str) -> dict:
    """Parser tối giản, đủ cho workspace.yaml: map lồng nhau và list of map.

    Không hỗ trợ list of scalar, multiline hay anchor — workspace.yaml không dùng.
    """
    root: dict = {}
    # (indent, container): container là dict đang nhận key ở mức indent đó
    stack: list[tuple[int, dict]] = [(-1, root)]
    # key của list đang mở, để biết gắn mục "- " vào đâu
    open_list: tuple[int, list] | None = None

    for raw in text.splitlines():
        line = raw.split("#", 1)[0] if raw.lstrip().startswith("#") else _strip_comment(raw)
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        body = line.strip()

        if body.startswith("- "):
            if open_list is None or indent < open_list[0]:
                continue
            item: dict = {}
            open_list[1].append(item)
            key, _, val = body[2:].partition(":")
            item[key.strip()] = _scalar(val)
            # các key tiếp theo của mục này nằm sâu hơn dấu "-"
            stack = [s for s in stack if s[0] < indent] + [(indent + 1, item)]
            continue

        while len(stack) > 1 and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        key, sep, val = body.partition(":")
        if not sep:
            continue
        key, val = key.strip(), val.strip()
        if val:
            parent[key] = _scalar(val)
        else:
            # chưa biết là map hay list; quyết khi gặp dòng con đầu tiên
            child: dict = {}
            lst: list = []
            parent[key] = child
            stack.append((indent, child))
            open_list = (indent, lst)
            _list_slots[id(parent), key] = (parent, key, lst, child)
    # key nào đã nhận mục "- " thì thay dict rỗng bằng list
    for parent, key, lst, child in _list_slots.values():
        if lst and parent.get(key) is child:
            parent[key] = lst
    _list_slots.clear()
    return root


_list_slots: dict = {}


def _strip_comment(line: str) -> str:
    """Bỏ comment cuối dòng, giữ nguyên dấu # nằm trong chuỗi nháy."""
    out, quote = [], ""
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = ""
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


# ---------------------------------------------------------------- kiểm công cụ
def check_tools(ws: dict) -> None:
    say(OK, f"Python {sys.version.split()[0]}")

    want = (ws.get("tools") or {}).get("openspec", "")
    exe = shutil.which("openspec")
    if not exe:
        say(FAIL, "chưa cài OpenSpec CLI", f"npm install -g @fission-ai/openspec@{want}")
    else:
        try:
            got = subprocess.run([exe, "--version"], capture_output=True, text=True, timeout=30).stdout.strip()
        except Exception as exc:
            got = f"không chạy được ({exc})"
        if want and want not in got:
            say(WARN, f"OpenSpec trên máy là {got}, khung yêu cầu {want}",
                f"npm install -g @fission-ai/openspec@{want}")
        else:
            say(OK, f"OpenSpec {got}")

    try:
        import yaml  # noqa: F401
        say(OK, "pyyaml")
    except ImportError:
        say(WARN, "chưa cài pyyaml", "pip install pyyaml  (tech-tools.py cần)")


def check_repos(ws: dict) -> list[dict]:
    repos = ws.get("repos") or []
    found = []
    for r in repos:
        p = (ROOT / r["path"]).resolve()
        if p.is_dir():
            say(OK, f"repo {r['id']}", str(p))
            found.append(r)
        else:
            say(WARN, f"repo {r['id']} chưa có ở {r['path']}", "clone về hoặc sửa workspace.yaml")
    return repos


# ---------------------------------------------------------------- sinh .claude
def deploy_claude(ws: dict, write: bool) -> None:
    claude = ROOT / ".claude"
    commands = claude / "commands"
    agents = claude / "agents"

    sources = [
        (ROOT / "engine" / "commands", commands, "*.md"),
        (ROOT / "engine" / "tech" / "commands", commands, "*.md"),
        (ROOT / "engine" / "agents", agents, "*.md"),
        (ROOT / "engine" / "tech" / "agents", agents, "*.md"),
    ]
    n = 0
    for src, dst, pat in sources:
        if not src.is_dir():
            continue
        if write:
            dst.mkdir(parents=True, exist_ok=True)
        for f in sorted(src.glob(pat)):
            if write:
                shutil.copy2(f, dst / f.name)
            n += 1
    # thư mục con của commands (opsx/)
    opsx = ROOT / "engine" / "tech" / "commands" / "opsx"
    if opsx.is_dir():
        if write:
            (commands / "opsx").mkdir(parents=True, exist_ok=True)
        for f in sorted(opsx.glob("*.md")):
            if write:
                shutil.copy2(f, commands / "opsx" / f.name)
            n += 1
    say(OK if write else SKIP, f"{n} command và agent {'đã sinh vào' if write else 'sẽ sinh vào'} .claude/")

    # settings.json sinh từ scripts/settings.base.json + repos trong workspace.yaml
    base_path = ROOT / "scripts" / "settings.base.json"
    if not base_path.is_file():
        say(FAIL, "thiếu scripts/settings.base.json", "lấy lại từ git; không sinh được settings.json")
        return
    py = python_cmd()
    raw = io.open(base_path, encoding="utf-8").read().replace("{{PYTHON}}", py)
    settings = json.loads(raw)
    settings.pop("_comment", None)
    settings.setdefault("permissions", {})["additionalDirectories"] = [
        r["path"].rstrip("/") + "/" for r in (ws.get("repos") or [])
    ]
    n_hooks = sum(len(v) for v in (settings.get("hooks") or {}).values())
    if write:
        claude.mkdir(parents=True, exist_ok=True)
        io.open(settings_path_of(claude), "w", encoding="utf-8", newline="\n").write(
            json.dumps(settings, indent=2, ensure_ascii=False) + "\n")
    dirs = settings["permissions"]["additionalDirectories"]
    say(OK if write else SKIP,
        f"settings.json: {len(dirs)} repo, {n_hooks} hook, lệnh python `{py}`")


def settings_path_of(claude):
    return claude / "settings.json"


def python_cmd() -> str:
    """Lệnh python mà hook sẽ gọi. Windows thường chỉ có `python`; alias Microsoft Store
    tên `python3` tồn tại trên PATH nhưng chạy là lỗi, nên phải thử chạy thật."""
    for cand in ("python3", "python"):
        exe = shutil.which(cand)
        if not exe:
            continue
        try:
            r = subprocess.run([exe, "-c", "print(1)"], capture_output=True, text=True, timeout=30)
            if r.returncode == 0 and r.stdout.strip() == "1":
                return cand
        except Exception:
            continue
    return "python"


CODEKB_FILES = [
    "architecture.md", "business-overview.md", "code-structure.md", "component-inventory.md",
    "dependencies.md", "technology-stack.md", "api-documentation.md",
    "code-quality-assessment.md", "reverse-engineering-timestamp.md",
]


def deploy_codekb(ws: dict, write: bool) -> None:
    base = ROOT / "domain" / "codekb"
    for r in ws.get("repos") or []:
        d = base / r["id"]
        if d.is_dir() and any(d.glob("*.md")):
            say(OK, f"codekb {r['id']}", f"{len(list(d.glob('*.md')))} file")
            continue
        if write:
            d.mkdir(parents=True, exist_ok=True)
            for name in CODEKB_FILES:
                f = d / name
                if not f.exists():
                    io.open(f, "w", encoding="utf-8", newline="\n").write(
                        f"# {name[:-3]} — {r['id']}\n\n"
                        f"Chưa quét. Chạy stage 2.1 Reverse Engineering cho repo `{r['id']}`:\n"
                        f"`/tech <intent-slug> nhảy tới reverse-engineering`\n")
        say(WARN, f"codekb {r['id']} còn rỗng", "chạy 2.1 Reverse Engineering cho repo này")


def main() -> int:
    check_only = "--check" in sys.argv
    write = not check_only
    ws = load_workspace()
    prod = ws.get("product") or {}
    print(f"\nupbase-specs — sản phẩm: {prod.get('name', '?')}\n")

    check_tools(ws)
    check_repos(ws)
    deploy_claude(ws, write)
    deploy_codekb(ws, write)

    width = max(len(w) for _, w, _ in report) + 2
    for level, what, detail in report:
        print(f"  {level:4} {what:<{width}} {detail}")

    bad = sum(1 for l, _, _ in report if l == FAIL)
    warn = sum(1 for l, _, _ in report if l == WARN)
    print()
    if bad:
        print(f"{bad} mục chặn, {warn} cảnh báo. Sửa theo cột bên phải rồi chạy lại.")
        return 1
    if write:
        print(f"Xong{f', {warn} cảnh báo' if warn else ''}. Mở Claude Code tại thư mục gốc repo này.")
    else:
        print(f"Kiểm xong{f', {warn} cảnh báo' if warn else ''}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
