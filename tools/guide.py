"""Render a role's guide from procedure data and rules. Nothing is authored here but the data.

    python3 tools/guide.py manager --lang zh
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent


def pick(value, lang):
    return value[lang] if isinstance(value, dict) and lang in value else value


def main() -> int:
    args = sys.argv[1:]
    role = args[0] if args and not args[0].startswith("-") else "manager"
    lang = args[args.index("--lang") + 1] if "--lang" in args else "en"
    corpus = yaml.safe_load((HERE / "AGENTS.yaml").read_text(encoding="utf-8"))
    proc = yaml.safe_load((HERE / "law" / "procedure.yaml").read_text(encoding="utf-8"))
    flat = {k: v for b in corpus.values() for k, v in b.items()}
    blocks = proc.get("blocks", {})
    p = proc["procedure"][role]

    head = {"en": ("Which state you are in", "Ask in this order; the first that holds is what you are doing:",
                   "After each state you return to the table.", "Done when:"),
            "zh": ("你现在在哪个状态", "按顺序问，第一个成立的就是你正在做的：",
                   "每节做完回到这张表。", "判据：")}[lang]
    print(f"# {role}\n")
    print(f"## {head[0]}\n")
    print(head[1] + "\n")
    for i, row in enumerate(p["_test"], 1):
        print(f"{i}. {pick(row['_see'], lang)} → **{pick(p['_states'][row['_state']]['_name'], lang)}**")
    print(f"\n{head[2]}\n")

    drawn = {k for row in p["_test"] for k in p["_states"][row["_state"]]["_steps"]}
    for row in p["_test"]:
        st = p["_states"][row["_state"]]
        print(f"## {pick(st['_name'], lang)}\n")
        for n, key in enumerate(st["_steps"], 1):
            node = flat[key]
            text = pick(node["_goal"], lang) if "_goal" in node else node["_text"]
            # a secondary axis rides along as @name, and only when it is printed in this same file
            extra = [d for d in node.get("_depends", []) if d in drawn]
            tail = (" " + " ".join("@" + d for d in extra)) if extra else ""
            print(f"{n}. {key}: {text}{tail}")
            if "_how" in node:
                print(f"   → {pick(node['_how'], lang)}")
        if st.get("_artefact") in blocks:
            print(f"\n```\n{pick(blocks[st['_artefact']]['_text'], lang).rstrip()}\n```\n")
        c = st["_criterion"]
        print(f"**{head[3]}** {pick(c['_see'], lang)}（`{c['_by']}` → {c['_expect']}）\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
