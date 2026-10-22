# Balance migration

Goal: every rule that presents a live choice is a balance: two live options, each with a cost in the seven units and a payer, the band where the role acts, and the pull that says which way to yield. A rule with one live option is a procedure and keeps its `how`.

## The test

1. Name two options an agent could actually take at this moment.
2. Each option has a cost it would pay, in one of the seven units.
3. The band says where the line sits, and the pull says which way to yield at it.

A rule with no second live option stays an act; a second label for the same option is not an option. The keyword test in an earlier draft (`if`, `only`, `when`, `prefer`) counted 114 candidates; it over-counts, because a clause that says *how* is not a choice. The balance test decided each one.

## State

The table is derived from the corpus and `python3 tools/counts.py` refuses a row that drifts; the corpus also holds the principles, which are neither acts nor balances.

| section | acts | balances |
|---|---:|---:|
| laws | 0 | 17 |
| architecture | 14 | 0 |
| speech | 14 | 8 |
| inbox | 9 | 0 |
| records | 17 | 0 |
| spend | 15 | 3 |
| scheduling | 16 | 3 |
| dispatch | 15 | 3 |
| review | 17 | 2 |
| gates | 5 | 2 |
| degrees | 8 | 3 |
| writing | 8 | 1 |
| change | 13 | 2 |
| git | 15 | 1 |
| operations | 6 | 0 |
| practice | 11 | 12 |
| roles | 3 | 0 |
| precedence | 7 | 0 |
| intent | 16 | 7 |
| delivery | 10 | 1 |
| docs_shape | 16 | 3 |
| upkeep | 7 | 1 |
| resources | 15 | 0 |
| proof_process | 12 | 0 |
| communication | 14 | 3 |
| principles | 6 | 0 |
| prices | 8 | 0 |
| total | 297 | 72 |

## Accept

The balance test in `docs/review/contract.md`; `sh tools/check.sh`; one fresh review; the case coverage from `docs/review/cases.md`.

## Paths

`AGENTS.yaml`; one writer, the policy_worker.

## Spend

`machine_time`, local; `person_attention` at the review.

## Stop

The result gate.

## Owner

The policy_worker writes the law and regenerates the views; a subagent reviews and only reviews.
