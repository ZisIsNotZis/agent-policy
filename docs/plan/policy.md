# Policy

The product is the law in AGENTS.yaml, rendered to AGENTS.md and checked by `python3 render_policy.py`. This is the plan for that product.

## Status

- AGENTS.yaml is the only source and AGENTS.md is its generated view; `python3 render_policy.py --check` passes and runs on every commit through `.githooks/pre-commit`, enabled once per clone by `git config core.hooksPath .githooks`, and in CI for a contributor's pull request.
- The law lives here and the workspace consumes it at a pinned submodule, with its root `AGENTS.md` a symlink into that submodule, so the text has one home and is still physically at the level an agent reads.
- No document cites a ticket, an issue or a session.

## Amendment one, agreed

Rulings: a claim that no longer describes the world dies while retraction, a negative finding and evidence survive; `upkeep.archive` and the compatibility clause die; `roles.inversion` carries the end/means split, one round of argument, then execution with the dissent recorded, and urgency buys one line of explanation; the superseded catalogue work records are killed rather than annotated.

Nodes: `ssot.kill`, `upkeep.supersede`, `record.plan_tree`, `roles.inversion`, `discussion.corrected`, `self_improvement.intake`.
Edits: `discussion.divergence` also covers the terse or heated message; `outdated` loses the compatibility clause; `people` and `files` no longer assume this repository is the only scope; the naming rule loses its guidance-only mark once the lint refuses the shape.

## Work packages

- `1.structural-move` — done. `plain_name` sits beside `one_name`, and the render differs by that one line alone.
- `2.amendment` — the six nodes and the edits above. Acceptance: the check passes, and the kill rule is exercised by writing one banned token and watching the check refuse it.
- `3.names` — the lint over document text and file names, in this repository and in the workspace. Acceptance: zero hits, check passes, the workspace's catalogue scripts still reproduce their artefacts.
- `4.inheritance` — the renderer chains a scope's own source onto this one and refuses a duplicate key, so a scope can refine these rules without copying them.

## Open questions

None.
