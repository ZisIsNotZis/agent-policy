# agent-policy

Standing law for AI agents working in a repository: who is a node, who speaks to whom, what a report
carries, where a fact lives, and who may decide.

**For** someone who wants an agent held to something checkable, and for reading what this author's agents
actually work under.
**Not for** a product, a framework or a promise. It is one author's law, written for one human working with
agents. It refuses most of what a coding agent does by default: it kills deprecated material instead of
annotating it, it treats a person's words as evidence about the end rather than a specification of the
means, and it sends a failure to the layer that should have prevented it.

## One source, six projections

[AGENTS.yaml](AGENTS.yaml) is the whole law: 396 rules, each with a trigger, a goal and an action, in
Chinese and English side by side, plus the role specs, the banned-word lexicon and the ceiling. Nothing
else in this repository is a source.

`python3 tools/build.py` writes one file per role into [agents/](agents): the rules that role reads, and
nothing else. A role file is generated and never edited, and `--check` fails when one has drifted.

| Role | What it is for | Rules |
|---|---|---|
| `root` | the one node whose parent is the person | 339 |
| `manager` | holds a directory, a document and a roadmap, and dispatches | 288 |
| `worker` | executes one work package and reports once | 211 |
| `researcher` | answers one bounded question with max thinking and writes nothing | 151 |
| `reviewer` | reads one artefact against its acceptance and returns a verdict | 158 |
| `policy_worker` | changes this law and runs the checks | 187 |

The first two hold a directory and dispatch. The last four are flavours of a worker: they differ in what
they read, what they produce and how hard they are allowed to think, and none of them dispatches. A
behaviour that is a matter of subject rather than of interface — holding a GPU, searching the web, writing
for the public — is not a role. It is a contract that names the rules it needs.

## Read it

[AGENTS.md](AGENTS.md) is a symlink to `agents/root.md`, because a root launched directly by pi loads no role
file and that is the file it gets. Subagents never see it: each role file turns project context off.

## Install it

The law is one checkout, but a child launched from a project resolves agents from `~/.pi/agent/agents`. Link the five dispatchable role files there; the command is idempotent and writes nothing inside this repository.

```sh
sh tools/install-agents.sh          # install or refresh the links
sh tools/install-agents.sh --check  # fail if one is missing or points elsewhere
```

## Check it

```sh
python3 tools/law.py --check    # the corpus: shape, scope, dependencies, banned words, shields
python3 tools/build.py --check  # the six role files against the corpus
python3 tools/contract.py --self-test  # the field names read from the law, the command, the wall-clock, the byte limit
sh tools/check.sh               # all three
```

The check also counts prohibitions against the `ceiling` block in `AGENTS.yaml`, so a rule cannot quietly
become a ban.

## The rest of the repository

- `AGENTS.yaml` — the rules, the six role specs, the banned-word list and the ceiling. The only source.
- `tools/law.py` — renders one role's view out of the corpus, and checks it.
- `tools/build.py` — writes `agents/*.md`.
- `tools/contract.py` — checks a contract's identity, its floor and the lines above it before dispatch; `--template` prints the skeleton.
- `tools/install-agents.sh` — links the five role files into `~/.pi/agent/agents`.
- `tools/check.sh` — one entry point.
- `docs/roadmap/policy.md` — the roadmap; `docs/product/policy.md` — the product commitment; `docs/review/contract.md` — the review criteria.

Proposals live in the owning document's open questions, with their author and source. History lives in git.
