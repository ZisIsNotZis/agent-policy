"""Render the corpus into one view per kind of agent, and check it.

AGENTS.yaml is the source. Every node declares one of four blocks; a role reads a union of them:

    root    = root_only  + root_manager + manager_worker
    manager = root_manager + manager_worker
    worker  = manager_worker + worker_only

There is no fifth block. A manager is an agent whose parent is a manager, and the root is a
manager whose parent is the person, so every manager rule reaches the root by construction and
every shared rule reaches both remaining kinds.

    python3 tools/law.py            regenerate the three views
    python3 tools/law.py --check    fail if a view is stale, a scope is unknown, or a node reaches
                                    no agent at all
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent
LAW = HERE / "law"
CORPUS = HERE / "AGENTS.yaml"
RENDER_ROOT = HERE / "AGENTS.md"
RENDER_DIR = HERE / "agents"

BLOCKS = ("root_only", "root_manager", "manager_worker", "worker_only", "every_role")
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


def corpus() -> dict:
    return yaml.safe_load(CORPUS.read_text(encoding="utf-8"))


def read(name: str) -> str:
    return (LAW / name).read_text(encoding="utf-8") if (LAW / name).exists() else ""


def banned_words() -> list[str]:
    table = read("lexicon.md")
    if "# Lexicon" in table:
        table = table.split("# Lexicon", 1)[1]
    return [w.strip() for line in table.splitlines() for w in line.split("|")[3:4]
            for w in [x.strip() for x in w.split(",")] if w and not w.startswith("---")]


def ceiling() -> int:
    for line in read("ceiling").splitlines():
        if line.startswith("prohibitions"):
            return int(line.split()[1])
    raise SystemExit("law/ceiling needs a `prohibitions N` line")


def prohibitions(text: str) -> int:
    return sum(1 for s in re.split(r"(?<=[.;:])\s+", text)
               if re.search(r"\b(must not|may not|never|cannot|refuses? to|is not sent)\b", s))


def render(role: str) -> str:
    want = VIEWS[role]
    out = [f"# Law, as {role} reads it\n"]
    for name, body in corpus().items():
        rows = [(k, v) for k, v in body.items() if v.get("scope") in want]
        if not rows:
            continue
        out.append(f"\n## {TITLES.get(name, name)}\n")
        for key, node in rows:
            out.append(f"**{key.replace('_', ' ')}.** {node['_text'].strip()}\n")
    return "\n".join(out)


def main() -> int:
    args = sys.argv[1:]
    check = "--check" in args
    failures: list[str] = []
    text = ""
    for name, body in corpus().items():
        for key, node in body.items():
            scope = node.get("scope")
            if scope not in BLOCKS:
                failures.append(f"{name}.{key} has scope {scope!r}")
            if scope != "every_role" and not any(scope in v for v in VIEWS.values()):
                failures.append(f"{name}.{key} reaches no agent")
            text += node["_text"] + "\n"

    banned = [w for w in banned_words() if w and re.search(rf"\b{re.escape(w)}\b", text, re.I)]
    for w in banned:
        failures.append(f"banned word {w!r}")

    views = {"root": render("root"), "manager": render("manager"), "worker": render("worker")}
    targets = {"root": RENDER_ROOT, "manager": RENDER_DIR / "manager.md",
               "worker": RENDER_DIR / "worker.md"}
    if check:
        for role, path in targets.items():
            if not path.exists() or path.read_text(encoding="utf-8") != views[role]:
                failures.append(f"{path.relative_to(HERE)} is stale")
    else:
        for role, path in targets.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(views[role], encoding="utf-8")

    n = prohibitions(views["root"])
    if n > ceiling():
        failures.append(f"the root view states {n} prohibitions against a ceiling of {ceiling()}")

    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    print(f"ok: {len(views)} views, {len(corpus())} sections, "
          f"{sum(len(b) for b in corpus().values())} nodes, {n} prohibitions, "
          f"{len(banned_words())} banned words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
