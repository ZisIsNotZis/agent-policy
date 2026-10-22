"""One tool: check AGENTS.yaml against its schema, then write the views.

    python3 tools/policy.py            check, then write agents/<role>.md and agents/zh/<role>.md
    python3 tools/policy.py --check    check and write nothing
    python3 tools/policy.py --render ROLE [--lang zh] [--depth N]

A view is the rules whose scope names the role, plus, at depth N, the rules they refer to.
A reference that is not drawn is not shown. A rule that no view draws is allowed.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "AGENTS.yaml"
OUT = ROOT / "agents"








ROOT = Path(__file__).resolve().parent.parent


# What each name the law lists decides. A name the law gains and this map lacks is refused loudly.
WHAT = {
    "kind": "the kind of contract, `worker contract` or `manager contract`",
    "name": "the package's name",
    "roadmap": "whose roadmap the result would change",
    "goal": "what the package is for",
    "scope": "what is inside it, and what is excluded",
    "accept": "the observation that decides done, with the command that produces it",
    "paths": "the exact paths that may be written, or `none` and what is done instead",
    "spend": "one class plus the wall-clock that ends the run, or `unknown` and when it becomes known",
    "stop": "the condition that ends the package before the clock does",
    "caps": "attempts, review rounds and no-progress rounds, as `budget caps` says",
    "tools": "the tools it gets and their limits, as `subagent scope` says",
    "model": "the model and the thinking level, named, as `model cost` says",
    "holds": "what it holds, as `worker` says: a manager's directory and name, or nothing",
    "rev": "the revision the review is bound to",
    "change": "the diff or artefact the review reads",
    "ran": "the mechanical checks and the commands that produced them",
    "judge": "the checks left to judgement",
    "blocking": "the criterion that makes a finding block",
    "budget": "the rounds and the wall-clock the review may spend",
    "escalate": "where an unanswerable question goes",
    "repair": "who repairs what the review finds",
}

CLASSES = {"time", "idle-compute", "metered-compute", "exclusive", "unrecoverable", "unknown"}
OLD_NAMES = {
    "boundary": "goal",
    "area": "paths",
    "acceptance": "accept",
    "report target": "roadmap",
    "wall-clock": "spend",
}
MAX_BYTES = 16384
HEADING = re.compile(r"^\s*[-*#>\s]*(?P<key>[A-Za-z][A-Za-z \-]*?)\s*:\s*(?P<value>.*)$")
COMMAND = re.compile(r"`[^`]+`|\b(python3?|sh|bash|npm|make|cargo|pytest|go test)\b")
DURATION = re.compile(r"\b\d+(?:\.\d+)?\s*(?:s|sec|min|h|hour|day)s?\b", re.I)
NOTHING = re.compile(r"\bnone\b|\bnothing\b", re.I)
READ_ONLY = re.compile(r"read|judge|review|write nothing", re.I)
MANAGER = re.compile(r"\bmanager\b", re.I)
REVIEW = re.compile(r"\breview\b", re.I)


def law_names() -> dict[str, dict]:
    """The names a contract carries, read from the law so this file cannot drift from it."""
    try:
        corpus = yaml.safe_load(CORPUS.read_text(encoding="utf-8"))
        flat = {k: v for body in corpus.values() if isinstance(body, dict) for k, v in body.items()}
        return {
            "identity": list(flat["contract_identity"]["_fields"]),
            "floor": list(flat["contract_fields"]["_fields"]),
            "above": dict(flat["contract_fields"]["_above"]),
            "review": list(flat["reviewer_contract"]["_fields"]),
        }
    except (OSError, KeyError, TypeError, AttributeError, yaml.YAMLError) as exc:
        raise SystemExit(f"FAIL the law is unreadable at {CORPUS}: {exc}")


def describe(name: str) -> str:
    if name not in WHAT:
        raise SystemExit(
            f"FAIL the law names `{name}:` and tools/contract.py has no line saying what it decides")
    return WHAT[name]


def fields(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for line in text.splitlines():
        m = HEADING.match(line)
        if not m:
            continue
        key = " ".join(m.group("key").lower().split())
        found.setdefault(key, m.group("value").strip())
    return found


def missing(key: str, line: str | None) -> str | None:
    if line is None:
        return f"no `{key}:` line — the contract must say {describe(key)}"
    if not line:
        return f"`{key}:` is empty — a blank field is not a declaration"
    return None


def check(text: str) -> list[str]:
    found = fields(text)
    names = law_names()
    failures: list[str] = []

    for key in names["identity"] + names["floor"]:
        bad = missing(key, found.get(key))
        if bad:
            failures.append(bad)

    for key, rule in names["above"].items():
        bad = missing(key, found.get(key))
        if bad:
            failures.append(
                f"{bad} — the six are the floor, and `{rule.replace('_', ' ')}` puts this line above it")

    for old, new in OLD_NAMES.items():
        if old in found:
            failures.append(f"`{old}:` is the old name; the law says `{new}:`")

    kind = found.get("kind", "")
    if REVIEW.search(kind):
        for key in names["review"]:
            if not found.get(key):
                failures.append(
                    f"no `{key}:` line — a review contract carries the nine of `reviewer contract`, "
                    f"and this one says {describe(key)}")

    accept = found.get("accept", "")
    if accept and not COMMAND.search(accept):
        failures.append("`accept:` names no command — say how the observation is produced, in backticks")

    spend = found.get("spend", "")
    if spend:
        named = {w.strip(" `,;.()").lower() for w in spend.split()} & CLASSES
        if not named:
            failures.append(
                f"`spend:` names no class — one of {', '.join(sorted(CLASSES))}, "
                "and `unknown` with the moment it becomes known")
        elif "unknown" in named and len(spend.split()) < 4:
            failures.append("`spend: unknown` must say when it becomes known")
        elif not DURATION.search(spend):
            failures.append("`spend:` names no wall-clock — add how long it may hold the node")

    stop = found.get("stop", "")
    if stop:
        if NOTHING.search(stop) and len(stop.split()) < 4:
            failures.append("`stop:` says nothing ends it — name the condition that ends the package")
        elif DURATION.search(stop) and len(DURATION.sub(" ", stop).split()) < 3:
            failures.append(
                "`stop:` restates the wall-clock — name the condition that ends the package before "
                "the clock does, or the run returns nothing when it is killed")

    holds = found.get("holds", "")
    if holds and MANAGER.search(kind) and NOTHING.search(holds):
        failures.append("`holds:` says nothing and the kind is a manager contract — a manager holds a directory and a name")

    paths = found.get("paths", "")
    if paths and NOTHING.search(paths) and not READ_ONLY.search(paths):
        failures.append("`paths:` says nothing may be written, so say what the package does instead")

    size = len(text.encode("utf-8"))
    if size > MAX_BYTES:
        failures.append(f"{size} bytes — the dispatch transport refuses a payload above {MAX_BYTES}")
    return failures


def template() -> str:
    names = law_names()
    lines = [f"{key}: <{describe(key)}>" for key in names["identity"]]
    lines.append("")
    lines += [f"{key}: <{describe(key)}>" for key in names["floor"]]
    lines.append("")
    lines += [f"{key}: <{describe(key)}>  # above the floor: `{rule.replace('_', ' ')}`"
              for key, rule in names["above"].items()]
    lines.append("")
    lines.append("# a review contract also carries " + ", ".join(
        k for k in names["review"] if k not in names["floor"]))
    return "\n".join(lines) + "\n"


def without(text: str, keys) -> str:
    prefixes = tuple(f"{key}:" for key in keys)
    return "\n".join(line for line in text.splitlines() if not line.startswith(prefixes))


def self_test() -> list[str]:
    good = """kind: worker contract
name: self-test
roadmap: agent-policy

goal: prove the check refuses what the law refuses
scope: this tool; no other directory
accept: `python3 tools/contract.py --self-test` exits 0
paths: none; reads only
spend: idle-compute, 5 min wall-clock
stop: the self-test exits, or the 5 min clock ends it

caps: 1 attempt, 1 review round, 0 no-progress rounds
tools: `read`, `bash`; writes nothing outside this repository
model: the site default, thinking low
holds: nothing; it writes no directory, document or roadmap
"""
    names = law_names()
    failures: list[str] = []
    if check(good):
        failures.append(f"a full contract was refused: {check(good)}")
    for key in names["identity"] + names["floor"] + list(names["above"]):
        if not any(f.startswith(f"no `{key}:`") for f in check(without(good, [key]))):
            failures.append(f"a contract without `{key}:` passed")
    six_only = without(good, names["above"])
    if not any("floor" in f for f in check(six_only)):
        failures.append("a contract carrying the six and nothing above them passed")
    for old in OLD_NAMES:
        if not any(old in f for f in check(good.replace("paths:", f"{old}:", 1))):
            failures.append(f"the old name `{old}:` passed")
    if not check(good.replace("`python3 tools/contract.py --self-test` exits 0", "it works")):
        failures.append("`accept:` with no command passed")
    if not check(good.replace("spend: idle-compute, 5 min wall-clock", "spend: idle-compute")):
        failures.append("`spend:` with no wall-clock passed")
    if not any("clock" in f for f in check(without(good, ["spend"]))):
        failures.append("a contract with no `spend:` line did not name the clock")
    if not check(good.replace("stop: the self-test exits, or the 5 min clock ends it", "stop: none")):
        failures.append("`stop: none` passed")
    if not check(good.replace("stop: the self-test exits, or the 5 min clock ends it", "stop: 30 min")):
        failures.append("`stop:` restating the wall-clock passed")
    manager = good.replace("kind: worker contract", "kind: manager contract").replace(
        "holds: nothing; it writes no directory, document or roadmap", "holds: nothing")
    if not check(manager):
        failures.append("a manager contract holding nothing passed")
    if not any("reviewer contract" in f for f in check(good.replace("kind: worker contract", "kind: review contract"))):
        failures.append("a review contract without the nine passed")
    if not check(template()):
        failures.append("the generated template passed")
    return failures


def contract_main() -> int:
    args = sys.argv[1:]
    if "--template" in args:
        print(template(), end="")
        return 0
    if "--self-test" in args:
        failures = self_test()
        if failures:
            print("\n".join(f"FAIL {f}" for f in failures))
            return 1
        names = law_names()
        print(f"ok: {len(names['identity'])} identity lines, {len(names['floor'])} floor lines, "
              f"{len(names['above'])} above the floor, {len(names['review'])} in a review contract, "
              f"old names, command, wall-clock, stop, byte limit")
        return 0
    if "--check" not in args:
        print(__doc__.strip())
        return 2
    arg = args[args.index("--check") + 1] if args.index("--check") + 1 < len(args) else "-"
    text = sys.stdin.read() if arg == "-" else Path(arg).read_text(encoding="utf-8")
    failures = check(text)
    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    print(f"ok: identity, floor, above the floor, {len(text.encode('utf-8'))} bytes")
    return 0






ROOT = Path(__file__).resolve().parent


ROOT = ROOT.parent
CASES = ROOT / "docs/review/cases.md"
AXES = {"authority", "proceed"}


def resolves(name: str, rules: dict, corpus: dict) -> bool:
    if name in rules:
        return True
    parts = name.split(".")
    if len(parts) == 3 and parts[0] == "role_specs":
        return parts[1] in corpus["role_specs"] and parts[2] in corpus["role_specs"][parts[1]]
    return False
VERDICTS = {"stated", "delegated", "ambiguous", "silent"}


def cases_main() -> int:
    data = corpus()
    rules = {}
    for body in data.values():
        if isinstance(body, dict):
            for name, rule in body.items():
                if isinstance(rule, dict) and rule.get("_kind") in {"act", "balance", "principle"}:
                    rules[name] = rule

    rows = []
    role = None
    for line in CASES.read_text(encoding="utf-8").split("\n"):
        head = re.match(r"^## ([a-z_]+)$", line)
        if head:
            role = head.group(1)
            continue
        if not line.startswith("| ") or role is None or "`" not in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 4:
            continue
        moment, axis, verdict, cite = cells
        if axis not in AXES:
            print(f"FAIL axis {axis!r} in {role}: {moment}")
            return 1
        if verdict not in VERDICTS:
            print(f"FAIL verdict {verdict!r} in {role}: {moment}")
            return 1
        for name in re.findall(r"`([a-z_][a-z0-9_.]*)`", cite):
            if not resolves(name, rules, data):
                print(f"FAIL {role} cites {name}, which names nothing")
                return 1
            if name in rules and not reads(role, rules[name]["scope"]):
                print(f"FAIL {role} cites {name}, which its view does not read")
                return 1
        rows.append((role, verdict))

    counted = {}
    for role, verdict in rows:
        box = counted.setdefault(role, dict.fromkeys(VERDICTS, 0))
        box[verdict] += 1

    table = {}
    for line in CASES.read_text(encoding="utf-8").split("\n"):
        cells = [cell.strip().strip("*") for cell in line.strip("|").split("|")]
        if len(cells) == 6 and re.fullmatch(r"[a-z_]+|total", cells[0]):
            try:
                nums = [int(cell) for cell in cells[1:]]
            except ValueError:
                continue
            if sum(nums[1:]) != nums[0]:
                print(f"FAIL row {cells[0]} sums to {sum(nums[1:])}, not {nums[0]}")
                return 1
            key = cells[0]
            table[key] = dict(zip(("cases", "stated", "delegated", "ambiguous", "silent"), nums))

    for role, box in counted.items():
        want = table.get(role)
        got = (sum(box.values()), box["stated"], box["delegated"], box["ambiguous"], box["silent"])
        if want is None:
            print(f"FAIL {role} has {got[0]} rows and no table row")
            return 1
        if tuple(want[k] for k in ("cases", "stated", "delegated", "ambiguous", "silent")) != got:
            print(f"FAIL {role} table {want} does not match its rows {got}")
            return 1

    total = table.get("total")
    got = (
        len(rows),
        sum(1 for _, v in rows if v == "stated"),
        sum(1 for _, v in rows if v == "delegated"),
        sum(1 for _, v in rows if v == "ambiguous"),
        sum(1 for _, v in rows if v == "silent"),
    )
    if total is None or tuple(total[k] for k in ("cases", "stated", "delegated", "ambiguous", "silent")) != got:
        print(f"FAIL total {total} does not match the rows {got}")
        return 1

    print(f"ok: {len(rows)} cases, every citation readable, score table equals its rows")
    return 0






ROOT = Path(__file__).resolve().parent


DOC = ROOT.parent / "docs/roadmap/balance_migration.md"


def counts_main() -> int:
    data = corpus()
    sections = [name for name, body in data.items()
                if isinstance(body, dict) and name not in {"role_specs", "lexicon", "ceiling"}]
    want = {}
    for name in sections:
        body = data[name]
        want[name] = (
            sum(1 for r in body.values() if isinstance(r, dict) and r.get("_kind") == "act"),
            sum(1 for r in body.values() if isinstance(r, dict) and r.get("_kind") == "balance"),
        )

    rows = {}
    total = None
    for line in DOC.read_text(encoding="utf-8").split("\n"):
        cells = [c.strip().strip("*") for c in line.strip("|").split("|")]
        if len(cells) != 3:
            continue
        try:
            pair = (int(cells[1]), int(cells[2]))
        except ValueError:
            continue
        if cells[0] == "total":
            total = pair
        elif cells[0] in want:
            rows[cells[0]] = pair

    for name, pair in want.items():
        if rows.get(name) != pair:
            print(f"FAIL {name}: table {rows.get(name)} does not match corpus {pair}")
            return 1
    if len(rows) != len(want):
        print(f"FAIL the table names {len(rows)} sections, the corpus {len(want)}")
        return 1
    sums = (sum(a for a, _ in want.values()), sum(b for _, b in want.values()))
    if total != sums:
        print(f"FAIL total {total} does not match {sums}")
        return 1
    print(f"ok: {len(want)} sections, {sums[0]} acts, {sums[1]} balances")
    return 0






ROOT = Path(__file__).resolve().parent


THRESHOLD = 0.8


def words(text: str) -> set[str]:
    text = re.sub(r"`|\*", "", text.lower())
    return {w for w in re.findall(r"[a-z][a-z_]+", text) if len(w) > 2}


def dupes_main() -> int:
    rules = []
    for name, body in corpus().items():
        if not isinstance(body, dict) or name in {"role_specs", "lexicon", "ceiling"}:
            continue
        for key, node in body.items():
            if not isinstance(node, dict) or node.get("_kind") not in {"act", "balance"}:
                continue
            band = node.get("_between") or node.get("_how") or {}
            text = band.get("en") or ""
            if not text:
                continue
            rules.append((key, words(text), set(node.get("scope") or [])))

    fails = []
    for i, (name, bag, scope) in enumerate(rules):
        for other, obag, oscope in rules[i + 1:]:
            if not scope & oscope:
                continue
            union = bag | obag
            if not union:
                continue
            if len(bag & obag) / len(union) >= THRESHOLD:
                fails.append((name, other))

    if fails:
        for a, b in fails:
            print(f"FAIL {a} and {b} say the same thing to the same roles")
        return 1
    print(f"ok: {len(rules)} rules, no band is copied verbatim")
    return 0










ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "AGENTS.yaml"
RENDER_DIR = ROOT / "agents"

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


class Strict(yaml.SafeLoader):
    """A loader that refuses a duplicate key instead of silently keeping the last one."""


def _mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise SystemExit(f"duplicate key {key!r} in AGENTS.yaml")
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


Strict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def corpus() -> dict:
    return yaml.load(CORPUS.read_text(encoding="utf-8"), Loader=Strict)


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
    lines = ["---", f"name: {role}", f"description: {json.dumps(spec['description'], ensure_ascii=False)}",
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


ZH_TITLES = {
    "laws": "法则", "architecture": "架构", "speech": "说话", "inbox": "收件", "records": "记录",
    "spend": "花费", "scheduling": "调度", "dispatch": "派发", "review": "审查", "gates": "闸门",
    "degrees": "能动度", "writing": "写作", "change": "变更", "git": "Git", "operations": "操作",
    "practice": "实践", "roles": "角色", "precedence": "优先级", "intent": "意图", "delivery": "交付",
    "docs_shape": "文档形状", "upkeep": "维护", "resources": "资源", "proof_process": "证明过程",
    "communication": "沟通", "principles": "原则", "prices": "价格",
}


def render(role: str, lang: str = "en", depth: int = 0) -> str:
    """The rules whose scope names the role, plus `depth` levels of the rules they refer to."""
    flat = {k: v for b in sections().values() for k, v in b.items()}
    included = {k for k, v in flat.items() if reads(role, v.get("scope", ["manager", "worker"]))}
    frontier = set(included)
    for _ in range(depth):
        nxt = set()
        for key in frontier:
            for dep in flat[key].get("_depends", []):
                if dep in flat and dep not in included:
                    nxt.add(dep)
        included |= nxt
        frontier = nxt
    plan = [(name, [(k, v) for k, v in body.items() if k in included])
            for name, body in sections().items()]
    plan = [(name, rows) for name, rows in plan if rows]
    # Every rule this view draws is a row, so a dependency's text is already drawn: `drawn` holds
    # each row key and its position, and the dependency line points at it instead of repeating it.
    drawn: dict[str, int] = {}
    for _, rows in plan:
        for key, _ in rows:
            drawn[key] = len(drawn)
    if lang == "zh":
        out = [f"# 法，{role} 读到的样子\n\n{ROLE_SPECS[role]['description']}\n"]
        out.append("## SOP（英文；步骤只写一次）\n")
    else:
        out = [f"# Law, as {role} reads it\n\n{ROLE_SPECS[role]['description']}\n"]
        out.append("## SOP\n")
    for n, step in enumerate(sop(role), 1):
        out.append(f"{n}. {step}")
    for name, rows in plan:
        title = ZH_TITLES.get(name, name) if lang == "zh" else TITLES.get(name, name)
        out.append(f"\n## {title}\n")
        for key, node in rows:
            refs = " ".join("@" + dep for dep in resolve(key, flat) if dep in drawn)
            line = f"**{key.replace('_', ' ')}.** {rule_text(node, lang).strip()}"
            out.append(f"{line} {refs}\n" if refs else f"{line}\n")
    return "\n".join(out)


def dependency_failures(flat_all: dict) -> list[str]:
    """A dependency must exist in the corpus. Whether a view draws it is the renderer's business."""
    out: list[str] = []
    for key, node in flat_all.items():
        for dep in node.get("_depends", []):
            if dep not in flat_all:
                out.append(f"{key} depends on {dep}, which does not exist")
    return out


def law_main() -> int:
    flat_all = {k: v for b in sections().values() for k, v in b.items()}
    args = sys.argv[1:]
    if "--render" in args:
        lang = args[args.index("--lang") + 1] if "--lang" in args else "en"
        depth = int(args[args.index("--depth") + 1]) if "--depth" in args else 0
        print(render(args[args.index("--render") + 1], lang, depth), end="")
        return 0
    check = "--check" in args
    failures: list[str] = schema_failures()
    text = ""
    seen_keys: dict[str, str] = {}
    for name, body in sections().items():
        for key, node in body.items():
            if not isinstance(node, dict) or "_when" not in node and "_kind" not in node:
                continue
            if key in seen_keys:
                failures.append(f"{key} is a key in both {seen_keys[key]} and {name}")
            else:
                seen_keys[key] = name
            if key == name:
                failures.append(f"{name}.{key} repeats its section name")
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
                    extra = set(end) - {"name", "cost", "who_pays"}
                    if extra:
                        failures.append(f"{name}.{key} has an end with stray keys {sorted(extra)}")
                    for fld in ("name", "cost", "who_pays"):
                        if fld not in end:
                            failures.append(f"{name}.{key} has an end with no {fld}")
                    for fld in ("name", "cost"):
                        value = end.get(fld)
                        if not isinstance(value, dict) or set(value) != {"zh", "en"}:
                            failures.append(f"{name}.{key} has an end whose {fld} is not exactly zh+en")
                    cost_map = end.get("cost")
                    if isinstance(cost_map, dict) and set(cost_map) == {"zh", "en"}:
                        cost = cost_map.get("en") or ""
                        if not re.match(r"(person_attention|person_time|machine_time|money|exclusive|irreversible|trust)\b", cost):
                            failures.append(f"{name}.{key} has an end whose cost names no unit")
                    if end.get("who_pays") not in {"self", "parent", "person", "third_party"}:
                        failures.append(f"{name}.{key} has an end paid by {end.get('who_pays')!r}")
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
                    if "." in token.split("/")[-1] and not (ROOT / token).exists():
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




NODE_SCHEMA = {
    "act": ({"_kind", "_when", "_goal", "_how", "scope"}, {"_depends", "_fields", "_above"}),
    "balance": ({"_kind", "_when", "_goal", "_ends", "_between", "_pull", "scope"}, {"_depends", "_fields", "_above"}),
    "principle": ({"_kind", "_when", "_goal"}, {"scope", "_depends"}),
}
ROLE_KEYS = {"ruleset", "description", "sop", "tools", "thinking"}
PAYERS = {"self", "parent", "person", "third_party"}
UNITS = {"person_attention", "person_time", "machine_time", "money", "exclusive", "irreversible", "trust"}


def schema_failures() -> list[str]:
    """Required, optional and nothing else; only the first level carries the underscore."""
    out: list[str] = []
    for role, spec in ROLE_SPECS.items():
        if not isinstance(spec, dict):
            out.append(f"role_specs.{role} is not a map")
            continue
        miss = ROLE_KEYS - set(spec)
        extra = set(spec) - ROLE_KEYS
        if miss:
            out.append(f"role_specs.{role} has no {sorted(miss)}")
        if extra:
            out.append(f"role_specs.{role} has extra keys {sorted(extra)}")
    for name, body in sections().items():
        for key, node in body.items():
            where = f"{name}.{key}"
            if not isinstance(node, dict):
                out.append(f"{where} is not a map")
                continue
            kind = node.get("_kind")
            if kind not in NODE_SCHEMA:
                out.append(f"{where} has no _kind")
                continue
            required, optional = NODE_SCHEMA[kind]
            miss = required - set(node)
            extra = set(node) - required - optional
            if miss:
                out.append(f"{where} is a {kind} with no {sorted(miss)}")
            if extra:
                out.append(f"{where} has extra keys {sorted(extra)}")
            for field in ("_when", "_goal", "_how", "_between", "_pull"):
                if field in node and (not isinstance(node[field], dict) or set(node[field]) != {"zh", "en"}):
                    out.append(f"{where}.{field} is not exactly zh+en")
            if kind == "balance":
                ends = node.get("_ends")
                if not isinstance(ends, list) or len(ends) != 2:
                    out.append(f"{where} has no two ends")
                    continue
                for end in ends:
                    if not isinstance(end, dict) or set(end) != {"name", "cost", "who_pays"}:
                        out.append(f"{where} has an end that is not name+cost+who_pays")
                        continue
                    for field in ("name", "cost"):
                        if not isinstance(end[field], dict) or set(end[field]) != {"zh", "en"}:
                            out.append(f"{where} has an end whose {field} is not exactly zh+en")
                    cost = (end.get("cost") or {}).get("en") or ""
                    if cost.split(":")[0] not in UNITS:
                        out.append(f"{where} has an end whose cost names no unit")
                    if end.get("who_pays") not in PAYERS:
                        out.append(f"{where} has an end paid by {end.get('who_pays')!r}")
    return out


def views(depth: int = 0) -> dict[str, str]:
    texts = {}
    for role in ROLES:
        texts[f"{role}.md"] = (frontmatter(role) if role != "root" else "") + render(role, "en", depth)
        texts[f"zh/{role}.md"] = render(role, "zh", depth)
    return texts


def view_drift(depth: int = 0) -> list[str]:
    bad = []
    for rel, text in views(depth).items():
        path = OUT / rel
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            bad.append(rel)
    return bad


def write_views(depth: int = 0) -> None:
    for rel, text in views(depth).items():
        path = OUT / rel
        path.parent.mkdir(exist_ok=True)
        path.write_text(text, encoding="utf-8")


def main() -> int:
    args = sys.argv[1:]
    depth = int(args[args.index("--depth") + 1]) if "--depth" in args else 0
    if "--contract" in args or "--template" in args:
        sys.argv = [sys.argv[0]] + ["--check" if a == "--contract" else a for a in args]
        return contract_main()
    if "--render" in args:
        return law_main()
    if law_main():
        return 1
    failures = self_test()
    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    print("ok: contract self-test")
    for fn in (cases_main, counts_main, dupes_main):
        if fn():
            return 1
    if "--check" in args:
        bad = view_drift(depth)
        if bad:
            print("FAIL stale: " + ", ".join(bad))
            return 1
        print(f"ok: {len(ROLES)} role files, {len(ROLES)} Chinese views")
        return 0
    write_views(depth)
    print(f"ok: wrote {len(ROLES)} role files and {len(ROLES)} Chinese views")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
