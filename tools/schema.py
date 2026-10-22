"""The one tool: validate a rule file against AGENTS.schema.yaml.

    python3 tools/schema.py [file]        default AGENTS.yaml

The schema is read, never checked. Every failure names the rule and the field, and the file is
not a place to extend the vocabulary: a field the schema does not name is a failure.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "AGENTS.schema.yaml"
DEFAULT = ROOT / "AGENTS.yaml"
NAME = re.compile(r"^[a-z][a-z0-9_]*$")


class Strict(yaml.SafeLoader):
    """A loader that refuses a duplicate key instead of silently keeping the last one."""


def _mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise SystemExit(f"duplicate key {key!r} in the file")
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


Strict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load(path: Path) -> dict:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=Strict)


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
        if kind == "text":
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


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    schema = load(SCHEMA)
    data = load(path)
    if not isinstance(data, dict):
        print("FAIL the file is not a map")
        return 1
    fails = []
    for key, node in data.items():
        where = key
        if not NAME.match(key):
            fails.append(f"{where}: the key is not a leading word")
        if not isinstance(node, dict):
            fails.append(f"{where}: not a map")
            continue
        fails += check_fields(where, node, schema["rule"], set(data), set(schema["roles"]), schema)
    if fails:
        print("\n".join(f"FAIL {f}" for f in fails))
        return 1
    print(f"ok: {len(data)} rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
