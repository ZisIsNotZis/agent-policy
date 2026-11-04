---
name: safe-migration
description: Use for broad refactors, file or directory restructuring, schema or data migrations, API or contract changes, or any transformation where partial completion or regressions could be costly.
---

# Safe Migration

## Purpose

Change structure or data while preserving required behavior, traceability, and a reliable recovery path.

## Decide whether a migration is needed

Clarify the problem the migration solves, the desired end state, affected users and systems, compatibility requirements, and the cost of leaving the current state in place. Prefer incremental cleanup when a broad migration adds risk without corresponding value.

## Establish guarantees before changing

- Inventory affected files, data, interfaces, consumers, and dependencies.
- Define the target structure or contract.
- Map old locations or representations to new ones where traceability matters.
- Identify invariants and observable behavior that must remain true.
- Establish regression tests, validation queries, backups, or other recovery evidence appropriate to the migration.
- Agree on ownership, sequencing, integration, and rollback criteria.

## Execute incrementally

Prefer small, reversible stages. Keep old and new representations clearly distinguishable during transition. Migrate one coherent unit at a time, validate it, and remove obsolete material only after its replacement is verified. Avoid leaving ambiguous duplicate sources active.

For data migrations, consider idempotency, partial failure, consistency, ordering, backup/restore, and compatibility between old and new application versions. For code or document migrations, preserve references and update consumers systematically.

## Verify the end state

Confirm that:
- every in-scope item has a known disposition;
- required behavior and contracts remain valid;
- references and dependencies point to the intended new locations;
- regression and migration-specific checks pass;
- obsolete material is removed or explicitly retained for a reason;
- rollback or recovery instructions are usable where needed;
- documentation reflects the new authoritative state.

## Stop conditions

Pause or revise the migration if the mapping is incomplete, validation fails, an unexpected dependency appears, or the cost/risk exceeds the approved envelope. Preserve the current recoverable state and report evidence and options.

## Deliverable

A verified target state, a clear record of what changed, evidence that required behavior survived, and no unexplained half-migrated state.
