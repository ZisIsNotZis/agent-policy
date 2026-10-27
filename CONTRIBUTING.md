# Contributing

## Scope

This repository is one hand-written `LAW.md` plus the scripts that render it into role views. A change is in scope when the law gives a manager or a worker a better answer than it gives today, or when a script around it fails to keep a view true to the law.

Out of scope: folding a project's own rules into the law, adding a tracker or a state machine on top of it, and anything that turns the views into a second hand-written source.

## Read first

Read `LAW.md` whole before editing it. It is short, and a section's meaning depends on the sections beside it — the habits at the end qualify the rules above.

## Edit the law, not a view

`agents/` and `manager.md` are generated and carry a header saying so. Edit `LAW.md`; the renderer writes the views. A pull request that changes a generated file by hand fails the check below, which is the point.

## Checks

```sh
python3 tools/render.py      # render the views
sh tools/check.sh            # fail if a view on disk differs from the law
```

`check.sh` is the whole check: it renders in memory and compares. Run it before opening a pull request. The pre-commit hook does it again when a commit stages `LAW.md`, `banned.txt`, `tools/render.py`, `agents/` or `manager.md`; enable the hook once per clone with `git config core.hooksPath .githooks`.

## What a change carries

- **The case.** The situation that the current law answers badly, with the evidence that it does.
- **One home.** A fact lives where its question is answered; if the change restates a fact that already has a home, move it instead of copying it.
- **Wording.** The law's own terms, and none of the terms in `banned.txt`.
- **A small diff.** One rule or one script fix per commit, in the imperative: `law: name the release pass`, `tools: fail on a missing link`.

## Issues

Open an issue with the case and the evidence — a session that went wrong, a dispatch that lost the Goal, a rule that contradicted another. A rule that only reads well is not yet a change; what settles it is the situation it fixes.

## License

Contributions are under the MIT license in [LICENSE](LICENSE).
