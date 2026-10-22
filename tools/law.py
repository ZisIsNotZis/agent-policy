"""Render the corpus into one view per kind of agent, and check it.

AGENTS.yaml is the source. A rule lists in `scope` every role that reads it. A role reads the
rules that name it; the root also reads manager rules, and the law worker reads root, manager and
policy rules. Nothing else is inherited.

A view is its role's `sop` first, then the rules that role reads: the ordered steps come before
the reference, and every step names a file or a command that `--check` resolves in this tree.

    python3 tools/law.py            regenerate one view per role
    python3 tools/law.py --check    fail if a scope is unknown, a role has no SOP, a step names a
                                    path that is gone, a node reaches no agent, a balance has no
                                    goal, or an end is not exactly zh+en; view drift is
                                    tools/build.py --check
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent
CORPUS = HERE / "AGENTS.yaml"
RENDER_DIR = HERE / "agents"

RULESETS = ("root", "manager", "worker", "researcher", "reviewer", "policy")
META = ("role_specs", "lexicon", "ceiling")
# A balance reads when → goal. band. pull, so its goal is a field of its own.
REQUIRED = {
    "balance": ("_when", "_goal", "_between", "_pull"),
    "act": ("_when", "_goal", "_how"),
    "principle": ("_when", "_goal"),
}
TITLES = {
    "laws": "Laws", "architecture": "Architecture", "speech": "Speech", "inbox": "Inbox",
    "records": "Records", "spend": "Spend", "scheduling": "Scheduling", "dispatch": "Dispatch",
    "review": "Review", "gates": "Gates", "degrees": "Degrees", "writing": "Writing",
    "change": "Change", "git": "Git", "operations": "Operations", "practice": "Practice",
    "roles": "Roles", "precedence": "Precedence", "intent": "Intent", "delivery": "Delivery",
    "docs_shape": "Document shape", "upkeep": "Upkeep", "resources": "Resources",
    "proof_process": "Proof process", "communication": "Communication", "principles": "Principles",
    "prices": "Prices",
}


def corpus() -> dict:
    return yaml.safe_load(CORPUS.read_text(encoding="utf-8"))


ROLE_SPECS = corpus()["role_specs"]
ROLES = tuple(ROLE_SPECS)


def banned_words() -> list[str]:
    return list(corpus()["lexicon"]["banned"])


def ceiling() -> int:
    return int(corpus()["ceiling"]["prohibitions"])


def prohibitions(text: str) -> int:
    return sum(1 for s in re.split(r"(?<=[.;:])\s+", text)
               if re.search(r"\b(must not|may not|never|cannot|refuses? to|is not sent)\b", s))


def resolve(key: str, nodes: dict) -> list[str]:
    """The rules `key` names as dependencies, once each; every one of them is a row of its own."""
    seen = {key}
    out = []
    for dep in nodes.get(key, {}).get("_depends", []):
        if dep in nodes and dep not in seen:
            seen.add(dep)
            out.append(dep)
    return out


def ruleset(role: str) -> str:
    """A role reads one rule set; a flavour that behaves like a worker says so in `role_specs`."""
    return ROLE_SPECS[role]["ruleset"]


def reads(role: str, scope: list) -> bool:
    """The root is a manager; the policy worker holds the law and its own dispatch."""
    rs = ruleset(role)
    if role == "policy_worker":
        return bool({"root", "manager", "policy"} & set(scope))
    return rs in scope or (rs == "root" and "manager" in scope)


def rule_text(node: dict, lang: str = "en") -> str:
    """A rule's text: the goal, then the how. A balance reads when → goal. band. pull."""
    if "_goal" not in node and node.get("_kind") != "balance":
        raise SystemExit(f"{node.get('_name', 'a rule')} has no _goal; _text is gone")
    if node.get("_kind") == "balance":
        goal = node.get("_goal")
        if not goal:
            raise SystemExit(f"a balance has no _goal: {node.get('_when', {}).get('en', '?')}")
        when = node.get("_when")
        band = node["_between"]
        g = (goal.get(lang) or goal["en"]).rstrip(". ")
        text = g[0].lower() + g[1:] + ". " + (band.get(lang) or band["en"]).rstrip()
        if not text.endswith((".", "?", "!")):
            text += "."
        pull = node.get("_pull")
        if pull:
            text += " " + (pull.get(lang) or pull["en"]).rstrip()
            if not text.endswith((".", "?", "!")):
                text += "."
        if when:
            w = (when.get(lang) or when["en"]).rstrip(". ")
            return w[0].lower() + w[1:] + " → " + text
        return text
    goal = node["_goal"].get(lang) or node["_goal"]["en"]
    how = node.get("_how")
    when = node.get("_when")
    head = ""
    if when:
        w = (when.get(lang) or when["en"]).rstrip(". ")
        head = w[0].lower() + w[1:] + " → "
    body = goal[0].lower() + goal[1:].rstrip(". ") + "."
    if how:
        body += " " + (how.get(lang) or how["en"])
    return head + body


def frontmatter(role: str) -> str:
    """A role file is what the harness loads: it needs the block, and it must not inherit the project."""
    spec = ROLE_SPECS[role]
    lines = ["---", f"name: {role}", f"description: {spec['description']}",
             f"tools: {spec['tools']}", f"thinking: {spec['thinking']}",
             "model: inherit", "systemPromptMode: replace",
             "inheritProjectContext: false", "inheritGlobalContext: false",
             "inheritSkills: false", "---", ""]
    return "\n".join(lines)


def sections():
    """Every section that holds rules; the role specs, lexicon and ceiling are metadata."""
    return {k: v for k, v in corpus().items() if k not in META}


def sop(role: str) -> list[str]:
    """A role's procedure: the steps in the order it runs them, before the rules it reads."""
    return ROLE_SPECS[role].get("sop") or []


def render(role: str) -> str:
    """Each rule is drawn once, as its own row; a dependency is named, and the row it names is its text."""
    flat = {k: v for b in sections().values() for k, v in b.items()}
    plan = [(name, [(k, v) for k, v in body.items()
                    if reads(role, v.get("scope", ["manager", "worker"]))])
            for name, body in sections().items()]
    plan = [(name, rows) for name, rows in plan if rows]
    # Every rule this view draws is a row, so a dependency's text is already drawn: `drawn` holds
    # each row key and its position, and the dependency line points at it instead of repeating it.
    drawn: dict[str, int] = {}
    for _, rows in plan:
        for key, _ in rows:
            drawn[key] = len(drawn)
    out = [f"# Law, as {role} reads it\n\n{ROLE_SPECS[role]['description']}\n"]
    out.append("## SOP\n")
    for n, step in enumerate(sop(role), 1):
        out.append(f"{n}. {step}")
    for name, rows in plan:
        out.append(f"\n## {TITLES.get(name, name)}\n")
        for key, node in rows:
            out.append(f"**{key.replace('_', ' ')}.** {rule_text(node).strip()}\n")
            for dep in resolve(key, flat):
                if dep not in drawn:
                    raise SystemExit(f"{key} depends on {dep}, which {role} does not read")
                where = "above" if drawn[dep] < drawn[key] else "below"
                out.append(f"  depends on **{dep.replace('_', ' ')}** (drawn {where})\n")
    return "\n".join(out)


def dependency_failures(flat_all: dict) -> list[str]:
    """A dependency exists, and every role that reads the rule naming it also reads the dependency.

    render() relies on this: it points at the dependency's row, so a view can only be drawn when
    the dependency is a row of that view.
    """
    out: list[str] = []
    for key, node in flat_all.items():
        for dep in node.get("_depends", []):
            if dep not in flat_all:
                out.append(f"{key} depends on {dep}, which does not exist")
            else:
                for role in ROLES:
                    if reads(role, node.get("scope", [])) and not reads(role, flat_all[dep].get("scope", [])):
                        out.append(f"{key} depends on {dep}, which {role} may not read")
    return out


def main() -> int:
    flat_all = {k: v for b in sections().values() for k, v in b.items()}
    args = sys.argv[1:]
    if "--render" in args:
        print(render(args[args.index("--render") + 1]), end="")
        return 0
    check = "--check" in args
    failures: list[str] = []
    text = ""
    for name, body in sections().items():
        for key, node in body.items():
            if not isinstance(node, dict) or "_when" not in node and "_kind" not in node:
                continue
            scope = node.get("scope")
            if not isinstance(scope, list) or not scope:
                failures.append(f"{name}.{key} has no scope list")
            else:
                unknown = [r for r in scope if r not in RULESETS]
                if unknown:
                    failures.append(f"{name}.{key} names unknown roles {unknown}")
            kind = node.get("_kind", "act")
            missing = [fld for fld in REQUIRED.get(kind, ("_when", "_goal")) if fld not in node]
            for fld in missing:
                failures.append(f"{name}.{key} is a {kind} with no {fld}")
            if not missing:
                text += rule_text(node) + "\n"
            if kind == "balance":
                ends = node.get("_ends") or []
                if len(ends) != 2:
                    failures.append(f"{name}.{key} has {len(ends)} ends, not two")
                for end in ends:
                    if not isinstance(end, dict):
                        failures.append(f"{name}.{key} has an end that is not a map")
                        continue
                    extra = set(end) - {"_name", "_cost", "_who_pays"}
                    if extra:
                        failures.append(f"{name}.{key} has an end with stray keys {sorted(extra)}")
                    for fld in ("_name", "_cost", "_who_pays"):
                        if fld not in end:
                            failures.append(f"{name}.{key} has an end with no {fld}")
                    for fld in ("_name", "_cost"):
                        value = end.get(fld)
                        if not isinstance(value, dict) or set(value) != {"zh", "en"}:
                            failures.append(f"{name}.{key} has an end whose {fld} is not exactly zh+en")
                    cost_map = end.get("_cost")
                    if isinstance(cost_map, dict) and set(cost_map) == {"zh", "en"}:
                        cost = cost_map.get("en") or ""
                        if not re.match(r"(person_attention|person_time|machine_time|money|exclusive|irreversible|trust)\b", cost):
                            failures.append(f"{name}.{key} has an end whose cost names no unit")
                    if end.get("_who_pays") not in {"self", "parent", "person", "third_party"}:
                        failures.append(f"{name}.{key} has an end paid by {end.get('_who_pays')!r}")
            for fld in ("_when", "_goal", "_how", "_between", "_pull"):
                if isinstance(node.get(fld), dict) and "zh" not in node[fld]:
                    failures.append(f"{name}.{key} {fld} has no zh")

    banned = [w for w in banned_words() if w and re.search(rf"\b{re.escape(w)}\b", text, re.I)]
    for w in banned:
        failures.append(f"banned word {w!r}")

    # A view points at a dependency instead of repeating it, so a broken dependency stops the render.
    dep_failures = dependency_failures(flat_all)
    if dep_failures:
        print("\n".join(f"FAIL {f}" for f in dep_failures))
    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1

    views = {r: render(r) for r in ROLES}
    targets = {r: RENDER_DIR / f"{r}.md" for r in ROLES}


    for role in ROLE_SPECS:
        for needed in ("systemPromptMode: replace", "inheritProjectContext: false",
                       "inheritGlobalContext: false"):
            if needed not in frontmatter(role):
                failures.append(f"role {role} would not be shielded: {needed} missing")
        steps = ROLE_SPECS[role].get("sop")
        if not isinstance(steps, list) or not steps or not all(isinstance(s, str) and s.strip() for s in steps):
            failures.append(f"role {role} has no sop list")
            continue
        for step in steps:
            for ref in re.findall(r"`([^`]+)`", step):
                for token in ref.split():
                    if "." in token.split("/")[-1] and not (HERE / token).exists():
                        failures.append(f"role {role} sop names {token}, which does not exist")

    n = prohibitions(views["root"])
    if n > ceiling():
        failures.append(f"the root view states {n} prohibitions against a ceiling of {ceiling()}")

    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    counts = ", ".join(f"{r} {sum(1 for line in views[r].splitlines() if line.startswith('**'))}"
                       for r in ROLES)
    print(f"ok: {len(views)} views ({counts}), {len(sections())} sections, "
          f"{sum(len(b) for b in sections().values())} nodes, {n} prohibitions, "
          f"{len(banned_words())} banned words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
