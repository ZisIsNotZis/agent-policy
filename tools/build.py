"""Build one self-contained file per role: the procedure, then the rules that role reads.

    python3 tools/build.py            write one file per role into agents/, and its Chinese
                                     counterpart into agents/zh/
    python3 tools/build.py --check    fail if a file no longer matches its source
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / "agents"
import yaml
SPECS = yaml.safe_load((HERE / "AGENTS.yaml").read_text(encoding="utf-8"))["role_specs"]
ROLES = tuple(SPECS)
TITLES = {r: "# " + r.replace("_", " ").title() for r in ROLES}


def fm(role):
    spec = SPECS[role]
    return "\n".join(["---", f"name: {role}", f"description: {json.dumps(spec['description'], ensure_ascii=False)}",
                      f"tools: {spec['tools']}", f"thinking: {spec['thinking']}",
                      "model: inherit", "systemPromptMode: replace",
                      "inheritProjectContext: false", "inheritGlobalContext: false",
                      "inheritSkills: false", "---", ""])


def build(role, lang="en"):
    law = subprocess.run([sys.executable, str(HERE / "tools" / "law.py"), "--render", role, "--lang", lang],
                         capture_output=True, text=True, check=True).stdout
    head = fm(role) if (role != "root" and lang == "en") else ""
    return head + law


def main():
    check = "--check" in sys.argv
    bad = []
    for role in ROLES:
      for lang in ("en", "zh"):
        path = OUT / (f"{role}.md" if lang == "en" else f"zh/{role}.md")
        text = build(role, lang)
        head = text.split("---")[1] if text.startswith("---") else ""
        if head:
            meta = yaml.safe_load(head) or {}
            if meta.get("name") != role:
                bad.append(f"{role}: frontmatter name is {meta.get('name')!r}")
            for key in ("description", "tools", "thinking", "systemPromptMode"):
                if not meta.get(key):
                    bad.append(f"{role}: frontmatter has no {key}")
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                bad.append(f"{role}.{lang}")
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(text, encoding="utf-8")
    if bad:
        print("FAIL stale: " + ", ".join(bad))
        return 1
    print(f"ok: {len(ROLES)} role files, {len(ROLES)} Chinese views")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
