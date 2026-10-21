"""Extract one role's view verbatim from AGENTS.yaml, for reading or for building a guide.

    python3 tools/extract.py manager > view.md

Nothing is rewritten here. The point is to have the material in one place, exact, so a guide can
be built from it instead of from somebody's memory of it.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent
VIEWS = {
    "root": ("root_only", "root_manager", "manager_worker", "every_role"),
    "manager": ("root_manager", "manager_worker", "every_role"),
    "worker": ("manager_worker", "worker_only", "every_role"),
}

TITLES = {
    "laws": "Laws", "architecture": "Architecture", "speech": "Speech", "inbox": "Inbox",
    "records": "Records", "spend": "Spend", "scheduling": "Scheduling", "dispatch": "Dispatch",
    "review": "Review", "gates": "Gates", "degrees": "Degrees", "writing": "Writing",
    "change": "Change", "git": "Git", "operations": "Operations", "practice": "Practice",
    "roles": "Roles", "precedence": "Precedence", "intent": "Intent", "delivery": "Delivery",
    "docs_shape": "Document shape", "upkeep": "Upkeep", "resources": "Resources",
    "proof_process": "Proof process", "communication": "Communication", "principles": "Principles",
}


def main() -> int:
    role = sys.argv[1] if len(sys.argv) > 1 else "manager"
    want = VIEWS[role]
    d = yaml.safe_load((HERE / "AGENTS.yaml").read_text(encoding="utf-8"))
    print(f"# {role} view\n")
    n = 0
    for sec, body in d.items():
        rows = [(k, v["_text"]) for k, v in body.items() if v["scope"] in want]
        if not rows:
            continue
        print(f"\n## {TITLES.get(sec, sec)} ({len(rows)})\n")
        for k, txt in rows:
            n += 1
            print(f"- **{k}** — {' '.join(txt.split())}")
    print(f"\n{n} rules", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
