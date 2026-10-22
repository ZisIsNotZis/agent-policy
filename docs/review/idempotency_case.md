# Idempotency case: kill, reopen, `go`

The case the review contract's Idempotency check names: killed at a stable point, reopened, the person says `go`; the roadmap state is the same and no node is launched twice. This is the walk that shows it, and the contrast with the order the law had at `7b7dcc9`.

## Case

A manager walks its roadmap with two packages ready and one behind them. It is killed between taking and launching, reopened, and told `go`.

## Fixture

A roadmap whose nodes carry a status, with one precedence edge:

```
1_probe (ready)
2_measure (ready)
3_report (ready)
```

`1_probe -> 3_report`: `3_report` is taken only once `1_probe` is `done`. `ready` is a node nothing has happened to yet; the edge, not the status, is what makes `3_report` wait.

## Before: the marker was written after the launch

`take next` read "take every node whose dependencies are met, write down that it is taken": the walk is the taking, the marker is its last clause.

| step | artefact state | launches |
|---|---|---|
| `go` | `1_probe (ready)`, `2_measure (ready)`, `3_report (ready)` | 0 |
| take, launch `probe_a` | unchanged | 1 |
| take, launch `measure_b` | unchanged | 2 |
| killed here | no node marked | 2 |
| reopen, `go` | unchanged: both dependency-met, both `ready` | 2 |
| take again | unchanged | 4: `probe_a`, `probe_a2`, `measure_b`, `measure_b2` |

The state after the kill is the state before the take, so the second `go` repeats the first: two children on each package's paths, against `one writer per area`, and the spend twice.

## After: the marker is written and committed before the launch

`take next` writes `running` for every node it takes, commits, and launches only then. The marker names the child, so the state names its job and `recovery` has something to read.

| step | artefact state | launches |
|---|---|---|
| `go` | `1_probe (ready)`, `2_measure (ready)`, `3_report (ready)` | 0 |
| take both, write, commit | `1_probe (running: probe_a)`, `2_measure (running: measure_b)`, `3_report (ready)` | 0 |
| launch `probe_a` | committed above | 1 |
| launch `measure_b` | committed above | 2 |

Kill at any of those three points, reopen, read the document, `go`:

| kill point | state after `go` | launches after `go` |
|---|---|---|
| after the commit, before either launch | `1_probe (running: probe_a)`, `2_measure (running: measure_b)`, `3_report (ready)` | 0 |
| after `probe_a`, before `measure_b` | the same three lines | 0 |
| after both launches | the same three lines | 0 |

The state is the same at all three points, and no node becomes ready because the manager was reopened: `3_report` waits on `1_probe` being `done`, not on the reopen. The one thing the kill can still cost is a node marked `running` whose child never started; that is visible at the next roadmap read, where the marker names a child that has no report and whose declared wall-clock has passed, so `stuck` presumes it stuck and `stuck disposal` cancels or re-dispatches it. A visible stall, not a silent duplicate.

## The check that would catch a regression

- Criterion: after every kill, reopen and `go`, the status lines are byte-identical to the pre-kill ones, and no package has two children.
- Reproduction: `git show <pre-kill-commit>:docs/roadmap/<doc>.md | grep -n 'running'` against `grep -n 'running' docs/roadmap/<doc>.md` after `go`; the two outputs must be equal, and each `running` line names exactly one child.
- Failure shows as a changed status line, or as a second child named on the same package after `go`.
- `safe point` requires the statuses committed, so the pre-kill state is always a commit and this diff exists.

## Fix

`dispatch.take_next` writes and commits `running` with the child's name before it launches, and skips every node that is not `ready`; `docs_shape.roadmap_shape` gives a node its one status, its seven values, and the verdict that moves it to `done` or `failed`; `operations.safe_point` requires every status changed to be committed before control is handed back.

## What was not run

The kill is walked over the law's text, not executed: no harness here kills a manager at the dispatch boundary. Confidence is high that the new order closes the duplicate window and that the old order opens it; medium on whether the runtime re-enters `take next` on `go`, which the walk assumes.
