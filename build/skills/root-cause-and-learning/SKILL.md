---
name: root-cause-and-learning
description: Reconstruct failures, identify the responsible causal layer, correct the outcome and safeguard, and consume temporary staging entries.
---

# Root-cause analysis and learning

Use this procedure when an error, failed check, unexpected result, user correction, repeated misunderstanding, premature escalation, Goal drift, or infrastructure incompatibility reveals that the current outcome or operating method may be wrong.

## 1. Reconstruct before correcting

1. State the intended outcome and the relevant acceptance condition in plain language.
2. Reconstruct what actually happened from available evidence. Separate observed facts from inference and unknowns.
3. Identify the earliest point at which the result diverged from the intended outcome.
4. Identify the safeguard that should have prevented or detected the divergence, and why it did not.
5. Consider the full causal chain: Goal interpretation, direction, scope, assignment, method, implementation, verification, role boundary, escalation, reporting, and runtime support. Do not assume the last visible failure is the root cause.
6. If the evidence is insufficient, define the smallest investigation that can distinguish the plausible causes. Do not present a hypothesis as a finding.

## 2. Correct the right layer

Choose the narrowest layer that actually owns the cause:

- **Current artifact or execution:** repair the immediate defect.
- **Goal/design/plan:** correct a false assumption, proxy objective, missing constraint, or obsolete direction.
- **Assignment or handoff:** clarify intended outcome, boundary, context, authority, acceptance, or reporting level.
- **Verification:** add or repair the check that should have detected the problem.
- **Role instruction or reusable skill:** correct a recurring behavioral ambiguity or missing procedure.
- **Evaluation/regression scenario:** encode the corrected invariant and the former failure mode.
- **Runtime/integration contract:** expose a missing capability or enforce a required lifecycle behavior.
- **LAW:** change only when the lesson is a durable cross-tree invariant, not merely a local preference or one incident.

Do not add a rule just because an incident occurred. First ask whether the behavior can be prevented by better structure, clearer ownership, a check, or a design correction. Avoid both symptom-only patches and overgeneralized rules.

## 3. Verify learning, not just the patch

1. Verify the immediate correction against the original Goal and acceptance condition.
2. Run the new or corrected safeguard against the failure mode that previously escaped detection.
3. Where practical, test a nearby case to ensure the correction did not merely overfit one example.
4. Confirm the behavior changed at the layer that caused the failure.
5. Report the causal lesson and durable change to the responsible parent in the parent's outcome language. Keep technical traces with the Worker/evidence record.

A change is not learned until the safeguard is shown to work. An apology, acknowledgment, note, or test that merely reproduces the old failure is not learning.

## 4. Use `0_STAGING.md` only for genuinely deferred work

Create or update the scope's `0_STAGING.md` only if the item cannot responsibly be completed now. Do not stage routine work that can be resolved in place. Each entry must be newcomer-readable and contain:

- **Situation:** what happened, stated without unexplained local shorthand.
- **Expected behavior:** what should have happened and why.
- **Significance:** the consequence or recurrence risk.
- **Cause:** current causal explanation, with uncertainty clearly marked.
- **Responsible layer and owner:** one accountable person/agent role, not a vague team.
- **Next action:** a concrete verb-led action and intended permanent destination.
- **Verification:** what evidence will demonstrate the correction works.
- **Due point:** a specific date/time or named event, no later than the next milestone review.
- **Evidence:** links to exact logs, artifacts, tests, or source context; these support the explanation but do not replace it.

Translate local terms into general concepts so a newcomer can understand the issue without knowing the incident's internal vocabulary. Keep exact names, paths, IDs, measurements, and logs only in linked evidence when they are needed to locate or reproduce the incident.

## 5. Process and consume every entry

Review `0_STAGING.md` when resuming work, before each milestone review, and before handoff/context loss. For each entry:

1. Confirm the owner and due point are still valid.
2. Reconstruct enough context to act; do not rely on the entry's diagnosis as unquestionable truth.
3. Implement the correction, encode the durable safeguard, update the authoritative record, or reject the item with an evidence-based reason.
4. Verify the chosen disposition and the safeguard where applicable.
5. Record the permanent destination or rejection rationale in its proper home.
6. Notify affected owners in their appropriate outcome language.
7. Delete the processed entry from `0_STAGING.md`.

One deferral is permitted only for a named dependency that makes processing impossible. The owner explains it, obtains the Manager's agreement, and sets a new due date within the following seven calendar days. If still not processable then, escalate to the principal for an explicit disposition: provide authority/resources, transfer ownership, or reject/discard with a reason. Never roll dates forward automatically or leave an item indefinitely. Critical safety, security, data-loss, Goal-fidelity, role-boundary, and infrastructure-invariant issues are handled immediately and must not wait for staging review.

`0_STAGING.md` is empty or absent when there is no deferred work. Preserve useful history in evidence, version history, or the authoritative rule—not in a permanently growing staging file.
