# agent-policy

Standing rules for AI agents working in a repository: what counts as a fact, where it lives, who may decide, and how a mistake becomes a rule instead of a patch.

**For** someone who wants their agent held to something, and for reading what this author's agents actually work under.
**Not for** a product, a framework or a promise. It is one author's law, written for one human working with agents, and it refuses most of what a coding agent does by default: it kills deprecated material instead of annotating it, it treats his words as evidence about the end rather than a specification of the means, and it sends a failure back to the layer that should have prevented it.

## Read it

[AGENTS.md](AGENTS.md) is the whole law, rendered from [AGENTS.yaml](AGENTS.yaml). Any copy of it, wherever you found it, names this repository in its banner, so a reader who lands on a stray copy can find the current one.

Two files are not published here because they belong to a scope rather than to the law: the owner's `PEOPLE.md`, and any scope's own `AGENTS.yaml` that refines these rules.

## Check it

```sh
python3 render_policy.py --check
```

It prints `checks passed; AGENTS.md matches AGENTS.yaml.` and takes about 0.3 s, measured on the author's machine with Python 3.12 and PyYAML. It refuses a duplicate key, two nodes with the same text, an `@ref` that names no node, a manually wrapped line, and a render that no longer matches its source, and it regenerates the view with `python3 render_policy.py`.

Run it on every commit instead of remembering to:

```sh
git config core.hooksPath .githooks
```

## Status and limits

- Status and work in flight live in [docs/plan/policy.md](docs/plan/policy.md); the commitment is [docs/product/policy.md](docs/product/policy.md).
- The renderer reads one source. A repository that wants to refine these rules and keep them in one rendered file cannot yet; the chaining that would allow it is planned, not shipped.
- The rules were written from this author's failures. Where a rule is advice rather than a check it says so in its own line, and those are the ones to distrust.

## Report a problem

Open an issue at [ZisIsNotZis/agent-policy/issues](https://github.com/ZisIsNotZis/agent-policy/issues). A defect report is most useful with the rule's name, the situation it fired in, and what the agent did instead; a rule that fails in a concrete situation is the only kind of evidence that changes this file.

## Licence

MIT. Take the rules, change them, ship them.
