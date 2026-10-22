"""The one tool: validate the rule file against its schema, then render the views.

    python3 tools/schema.py            validate, render, write agents/<role>.md
    python3 tools/schema.py --depth N  the same, with N levels of references pulled in

There is no check-only mode and no second command. Validation happens once, on one parse; a
failure stops the pass before anything is written. The schema is read, never checked.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "AGENTS.yaml"
SCHEMA = ROOT / "AGENTS.schema.yaml"
ROLES = ROOT / "roles.yaml"
BANNED = ROOT / "banned.yaml"
OUT = ROOT / "agents"
NAME = re.compile(r"^[a-z][a-z0-9_]*$")


class Strict(yaml.SafeLoader):
    """A loader that refuses a duplicate key instead of silently keeping the last one."""


def _mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise SystemExit(f"duplicate key {key!r}")
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


Strict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load(path: Path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=Strict)


def text_of(node: dict) -> str:
    parts = []
    for field in ("_when", "_know", "_goal"):
        if node.get(field):
            parts.append(str(node[field]))
    for choice in node.get("_choices") or []:
        parts += [str(choice.get("move", "")), str(choice.get("gain", "")), str(choice.get("cost", ""))]
    return "\n".join(parts)


def check_fields(where: str, node: dict, spec: dict, ids: set, roles: set, schema: dict) -> list[str]:
    fails = []
    required = spec["required"]
    optional = spec.get("optional", [])
    for field in required:
        if field not in node:
            fails.append(f"{where}: no {field}")
    for field in node:
        if field not in required and field not in optional:
            fails.append(f"{where}: extra field {field}")
    for field, value in node.items():
        if field not in spec["fields"]:
            continue
        kind = spec["fields"][field]["type"]
        if kind == "number":
            if not isinstance(value, int):
                fails.append(f"{where}.{field}: not a number")
        elif kind == "text":
            if not isinstance(value, str):
                fails.append(f"{where}.{field}: not text")
            elif not value.strip() and not spec["fields"][field].get("empty"):
                fails.append(f"{where}.{field}: empty")
        elif kind == "keys":
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                fails.append(f"{where}.{field}: not a list of keys")
            else:
                for item in value:
                    if item not in ids:
                        fails.append(f"{where}.{field}: {item!r} names no rule")
        elif kind == "roles":
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                fails.append(f"{where}.{field}: not a list of roles")
            else:
                for item in value:
                    if item not in roles:
                        fails.append(f"{where}.{field}: unknown role {item!r}")
        elif kind == "list":
            if not isinstance(value, list):
                fails.append(f"{where}.{field}: not a list")
                continue
            if len(value) < spec["fields"][field].get("min", 1):
                fails.append(f"{where}.{field}: {len(value)} items, needs {spec['fields'][field]['min']}")
            for index, item in enumerate(value):
                inner = schema[spec["fields"][field]["of"]]
                if not isinstance(item, dict):
                    fails.append(f"{where}.{field}[{index}]: not a map")
                    continue
                fails += check_fields(f"{where}.{field}[{index}]", item, inner, ids, roles, schema)
    return fails


def validate(corpus: dict, schema: dict, roles: dict, banned: list[str]) -> list[str]:
    fails = []
    ids = set(corpus)
    for key, node in corpus.items():
        if not NAME.match(key):
            fails.append(f"{key}: the key is not a leading word")
        if not isinstance(node, dict):
            fails.append(f"{key}: not a map")
            continue
        fails += check_fields(key, node, schema["rule"], ids, set(roles), schema)
        for term in banned:
            if re.search(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])", text_of(node), re.I):
                fails.append(f"{key}: uses the banned term {term!r}")
    return fails


def reads(role: str, scope: list) -> bool:
    """A role reads what names it; the root also reads manager, the law roles also read root+manager."""
    if role in scope:
        return True
    if role == "root_manager" and "manager" in scope:
        return True
    if role in ("policy_writer", "policy_reviewer") and ({"root", "manager"} & set(scope)):
        return True
    return False


def choice_line(choice: dict) -> str:
    return f"{choice['move']} — {choice['gain']}；代价：{choice['cost']}"


def render(role: str, corpus: dict, roles: dict, depth: int) -> str:
    included = {key for key, node in corpus.items() if reads(role, node.get("_scope") or [])}
    frontier = set(included)
    for _ in range(depth):
        nxt = set()
        for key in frontier:
            for dep in corpus[key].get("_depends_on") or []:
                if dep not in included:
                    nxt.add(dep)
        included |= nxt
        frontier = nxt

    steps = sorted(
        (key for key in corpus
         if key in included and isinstance(corpus[key].get("_order"), int)
         and role in (corpus[key].get("_scope") or [])),
        key=lambda key: corpus[key]["_order"],
    )
    body = [key for key in corpus if key in included and "_order" not in corpus[key]]

    out = [f"# 法，{role} 读到的样子\n", (roles[role].get("description") or "") + "\n"]
    if steps:
        out.append("\n## 步骤\n")
        for index, key in enumerate(steps, 1):
            node = corpus[key]
            out.append(f"{index}. **{key}.** {choice_line(node['_choices'][0])}\n")
    for key in body:
        node = corpus[key]
        deps = [dep for dep in node.get("_depends_on") or [] if dep in included]
        refs = " " + " ".join("@" + dep for dep in deps) if deps else ""
        out.append(f"\n**{key}.** {node['_when']} → {node['_goal']}{refs}\n")
        for choice in node["_choices"]:
            out.append(f"  - {choice_line(choice)}\n")
    return "".join(out)


def frontmatter(role: str, spec: dict) -> str:
    if role == "root_manager":
        return ""
    desc = str(spec.get("description") or "").replace('"', "'")
    return "\n".join([
        "---", f"name: {role}", f'description: "{desc}"',
        f"tools: {spec['tools']}", f"thinking: {spec['thinking']}",
        "model: inherit", "systemPromptMode: replace",
        "inheritProjectContext: false", "inheritGlobalContext: false",
        "inheritSkills: false", "---", "",
    ])


def main() -> int:
    depth = int(sys.argv[sys.argv.index("--depth") + 1]) if "--depth" in sys.argv else 0
    schema = load(SCHEMA)
    roles = load(ROLES)
    banned = (load(BANNED) or {}).get("banned") or []
    corpus = load(CORPUS)
    fails = validate(corpus, schema, roles, banned)
    if fails:
        print("\n".join(f"FAIL {f}" for f in fails))
        return 1
    for role, spec in roles.items():
        text = frontmatter(role, spec) + render(role, corpus, roles, depth)
        path = OUT / f"{role}.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text(text, encoding="utf-8")
    link = ROOT / "AGENTS.md"
    if link.is_symlink() or link.exists():
        link.unlink()
    link.symlink_to(Path("agents") / "root_manager.md")
    print(f"ok: {len(corpus)} rules, {len(roles)} views, depth {depth}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
