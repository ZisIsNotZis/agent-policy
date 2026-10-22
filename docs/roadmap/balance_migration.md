# Balance migration

Goal: every remaining decision act is a balance: two ends, each with a cost in the seven units and a payer, the band, and the pull. A procedure stays a `how`, with the balance that chooses it named.

Scope: the 351 acts that remain in `AGENTS.yaml`; the `laws` section (15) is already balanced; of the 351, 114 are decision candidates and 237 are procedures.

## Method

- A **decision** is an act whose `_how` names a condition or a trade-off: `if`, `unless`, `when`, `before`, `after`, `prefer`, `only`, `may`, `cannot`, `cost`, `worth`, `instead`, `rather`, `choose`, `else`, `until`. The section worker verifies each against the balance test.
- A **procedure** is an act that names one sequence, not a choice. Keep the act; name the balance that chooses it. A procedure with no choosing balance is an incomplete design.
- Each balance: two ends, each with a cost and a payer; the band is the old `_goal` plus `_how`; the pull is the tie-breaker, not a restatement of the band or the end cost.
- The `laws` section is the model: `atomic`, `no_op`, `falsifiable`, `top_down`, `absent`, `controlled`, `invalidate`, `specific_wins`, `rule_over_state`, `own_inference`, `untrusted_input`, `derived`, `inferable`, `fail_loud`, `levels_in_order`.

## Accept

The balance test in `docs/review/contract.md`; `sh tools/check.sh`; a fresh review; the case coverage from `baseline_score`.

## Paths

`AGENTS.yaml`; one writer per worktree.

## Spend

`machine_time`, local; `person_attention` at the review.

## Stop

The result gate.

## Owner

The root dispatches one package per section in a worktree; the policy_worker integrates; the fresh review is the root's.

## Sections

| section | acts | decisions | status |
|---|---:|---:|---|
| practice | 23 | 12 | pending |
| intent | 22 | 9 | pending |
| speech | 21 | 11 | pending |
| scheduling | 20 | 6 | pending |
| records | 19 | 1 | pending |
| review | 19 | 8 | pending |
| docs_shape | 19 | 8 | pending |
| spend | 17 | 6 | pending |
| dispatch | 17 | 5 | pending |
| resources | 16 | 4 | pending |
| architecture | 15 | 6 | pending |
| change | 15 | 6 | pending |
| git | 15 | 1 | pending |
| communication | 15 | 6 | pending |
| proof_process | 12 | 4 | pending |
| delivery | 11 | 2 | pending |
| inbox | 10 | 2 | pending |
| degrees | 10 | 3 | pending |
| writing | 10 | 4 | pending |
| upkeep | 8 | 2 | pending |
| prices | 8 | 1 | pending |
| operations | 7 | 3 | pending |
| precedence | 7 | 1 | pending |
| principles | 6 | 2 | pending |
| gates | 5 | 1 | pending |
| roles | 4 | 0 | pending |
| **total** | **351** | **114** | |
