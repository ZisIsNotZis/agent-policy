# agent-policy

Standing law for AI agents working in a repository: who is a node, who speaks to whom, what a report
carries, where a fact lives, and who may decide.

**For** someone who wants an agent held to something checkable, and for reading what this author's agents
actually work under.
**Not for** a product, a framework or a promise. It is one author's law, written for one human working with
agents. It refuses most of what a coding agent does by default: it kills deprecated material instead of
annotating it, it treats a person's words as evidence about the end rather than a specification of the
means, and it sends a failure to the layer that should have prevented it.

## One source, one shape

The law is four files and one tool:

- [AGENTS.yaml](AGENTS.yaml) — every rule. A flat map keyed by a leading word; each rule carries its
  situation, the facts to know, its choices with their gain and cost, and its goal. No kinds, no sections,
  no second shape.
- [AGENTS.schema.yaml](AGENTS.schema.yaml) — the one schema. Required, optional, types, no extra field.
- [roles.yaml](roles.yaml) — the harness fields a role file needs, and nothing else.
- [banned.yaml](banned.yaml) — the forbidden terms.
- [tools/schema.py](tools/schema.py) — the one tool: validate against the schema, then render and write
  every view. The only flag is `--depth N`, the levels of `_depends_on` pulled into a view.

A view in [agents/](agents) is generated and never edited. It is the role's steps first, then the rules that
role reads, each with its choices priced.

| Role | What it is for | Kind |
|---|---|---|
| `root_manager` | the manager whose parent is the person; pi reads its view through `AGENTS.md` | manager |
| `manager` | holds a directory, a document and a roadmap, and dispatches | manager |
| `worker` | executes one work package and reports once | worker |
| `researcher` | answers one bounded question and writes nothing | worker |
| `reviewer` | reads one artefact against its acceptance and returns a verdict | worker |
| `policy_writer` | holds the law, its views and this repository's roadmap, and writes the change | manager |
| `policy_reviewer` | reads one law change and returns a verdict; it repairs nothing | worker |

A worker launches nothing; a manager dispatches the reviewer of a returned package.

## Read it

`AGENTS.md` is the view the root manager reads: a symlink to `agents/root_manager.md`, because pi reads
`AGENTS.md` for the project context. Subagents never see it: each role file turns project context off.

## Install it

The law is one checkout, but a child launched from a project resolves agents from `~/.pi/agent/agents`. Link
the six child role files there; the command is idempotent and writes nothing inside this repository.

```sh
sh tools/install-agents.sh          # install or refresh the links
sh tools/install-agents.sh --check  # fail if one is missing or points elsewhere
```

## Check it

```sh
python3 tools/schema.py            # validate, then write agents/*.md
python3 tools/schema.py --depth 1  # the same, pulling one level of references into each view
sh tools/check.sh                  # the same command, for a script
```

There is no check-only mode. A failure stops the pass before anything is written, and every failure names
the rule and the field. The tool also refuses a `_depends_on` or `_why` that names no rule, an unknown role,
and a banned term.

## The rest of the repository

- `tools/install-agents.sh` — links the six child role files into `~/.pi/agent/agents`.
- `tools/check.sh` — one entry point.
- `docs/roadmap/policy.md` — the roadmap and its current facts.
- `docs/review/contract.md` — the criteria a policy reviewer applies.

History lives in git. A proposal is a fact with an author and a source; it lives in the owning document's
open questions, not in a diary.
