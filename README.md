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

[AGENTS.yaml](AGENTS.yaml) is the whole law: every rule carries a trigger, a goal and an action, in
Chinese and English side by side, plus the six role specs with their SOPs, the banned-word lexicon and the
ceiling. Nothing else in this repository is a source. The sizes are printed by `python3 tools/policy.py --check`
rather than kept here.

`python3 tools/policy.py` writes one file per role into [agents/](agents): the role's SOP — the steps it runs
in order, each naming its file or its command — then the rules that role reads, and nothing else. A role
file is generated and never edited, and `--check` fails when one has drifted.

| Role | What it is for | Kind |
|---|---|---|
| `root` | the one node whose parent is the person | manager |
| `manager` | holds a directory, a document and a roadmap, and dispatches | manager |
| `policy_worker` | holds the law, its views and this repository's roadmap, and dispatches the review of its own change | manager |
| `worker` | executes one work package and reports once | worker |
| `researcher` | answers one bounded question with max thinking and writes nothing | worker |
| `reviewer` | reads one artefact against its acceptance and returns a verdict | worker |

`root`, `manager` and `policy_worker` hold a directory, a document and a roadmap, and dispatch. `worker`,
`researcher` and `reviewer` execute one package and report once: the worker may launch the reviewer of its
own slice, and the researcher and reviewer launch nothing. A behaviour that is a matter of subject rather
than of interface — holding a GPU, searching the web, writing for the public — is not a role. It is a
contract that names the rules it needs.

## Read it

`agents/root.md` is the view a root reads, because a root launched directly by pi loads no role
file and that is the file it gets. Subagents never see it: each role file turns project context off.

## Install it

The law is one checkout, but a child launched from a project resolves agents from `~/.pi/agent/agents`. Link the five child role files there; the command is idempotent and writes nothing inside this repository.

```sh
sh tools/install-agents.sh          # install or refresh the links
sh tools/install-agents.sh --check  # fail if one is missing or points elsewhere
```

## Check it

```sh
python3 tools/policy.py         # check everything, then write agents/ and agents/zh/
python3 tools/policy.py --check # check everything and write nothing
sh tools/check.sh               # the same check, for a script
```

The check also counts prohibitions against the `ceiling` block in `AGENTS.yaml`, so a rule cannot quietly
become a ban; and it refuses a role with no SOP, or an SOP step naming a file that is gone.

## The rest of the repository

- `AGENTS.yaml` — the rules, the six role specs, the banned-word list and the ceiling. The only source.
- `tools/policy.py` — one pass: every check, then the render. `tools/law.py` renders one view and checks the corpus.
- `tools/build.py` — writes `agents/*.md` and the Chinese reading copy `agents/zh/*.md`.
- `tools/contract.py` — checks a contract's identity, its floor and the lines above it before dispatch; `--template` prints the skeleton.
- `tools/policy.py`, `tools/counts.py`, `tools/dupes.py` — the checks `policy.py` runs: the case list against the law, the section table against the corpus, a copied band against its twin.
- `tools/install-agents.sh` — links the five role files into `~/.pi/agent/agents`.
- `tools/check.sh` — one entry point.
- `docs/roadmap/policy.md` — the roadmap; `docs/product/policy.md` — the product commitment; `docs/review/contract.md` — the review criteria.

Proposals live in the owning document's open questions, with their author and source. History lives in git.
