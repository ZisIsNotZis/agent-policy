---
name: documentation-and-ssot
description: Use when creating or restructuring project documentation, deciding what should be recorded, maintaining shared agent memory, resolving conflicting sources, or designing a project-specific documentation structure.
---

# Documentation and SSOT

## Purpose

Preserve the smallest reliable body of information that lets people and agents understand current truth, make consistent decisions, continue work, and avoid repeating expensive mistakes.

## Standard scope records

Use the supplied templates as the default minimum record set, adapting optional fields to the project without changing their purposes:
- `GOAL.md`: intended outcome, constraints, scope, deliverables, acceptance conditions.
- `PLAN.md`: approach, owners, work packages, dependencies, decisions, actual operating constraints, reassessment points.
- `STATE.md`: current observed state, evidence, work status, blockers, pending user input, next actions, and a concise user-facing summary.
- `HANDOFF.md`: assignment, owner, CWD, explicit write scope, interfaces, deliverable, acceptance conditions, evidence, and remaining work.

Each Manager maintains these records in its managed scope. The root Manager publishes a concise status in `STATE.md` for the Communicator to read. The Communicator may read that published status only; it does not browse other project records or independently investigate status.

## Choose additional documents for the project

Do not force every project into one template. Select documents according to the work:
- software/product work may need Goal, use cases, product decisions, architecture, and roadmap;
- research may need research questions, hypotheses, prior art, experimental design, evaluation methods, results, and limitations;
- creative work may need intent, references, constraints, iterations, review criteria, and selected direction;
- operational work may need service boundaries, runbooks, ownership, and incident knowledge.

Prefer a small number of clear, useful documents over a large taxonomy. Each document should have a distinct purpose and an obvious owner.

## Mirror the ownership hierarchy

Documentation ownership follows the Manager hierarchy. Each Manager maintains authoritative records for its assigned scope. Parent records contain the parent Goal, constraints, cross-workstream decisions, shared resources, ownership, overall state, and links to child records. Child Manager records contain their assigned outcome, local design, decisions, experiments, findings, exact resource locations, progress, and next actions. Worker records preserve only the package-specific context and evidence needed for execution and handoff.

Do not copy whole child records into parent documents. Summarize what the parent needs and link to the authoritative child source. Propagate discoveries upward when they affect parent scope, and propagate parent decisions downward when they affect child assignments.

## Establish SSOT

For every important class of information, identify one authoritative home. Other documents should link to it or provide clearly labeled summaries, not competing copies.

A practical SSOT check:
1. Can an agent quickly find the current decision or fact?
2. Is it clear which source is authoritative?
3. Are dependent summaries or references consistent?
4. Is there an owner who will update it when the state changes?
5. Can stale or superseded information be recognized?

SSOT does not mean one giant file. It means one authoritative source per important fact or decision.

## What to record

Preserve information when losing it could cause a future agent to repeat work, make a wrong decision, misunderstand an assignment, or ask for information already established. Exact paths, URLs, share locations, access methods, and environment details are often essential execution context; do not replace them with vague descriptions such as "the shared folder".


Prioritize information that affects future decisions, handoffs, reproducibility, or repeated work:
- current Goal, constraints, and priorities;
- important decisions and their rationale;
- interfaces, contracts, and ownership;
- assumptions and unresolved questions that matter;
- evidence, experiment outcomes, and limitations;
- rejected approaches likely to be reconsidered, with why they were rejected;
- current status and next meaningful action.

Do not preserve every thought, transient observation, routine action, or raw execution log. Store detailed evidence in the appropriate system and link to it.

## Mark epistemic status

Where confusion could change a decision, distinguish observed/verified facts, inferences, assumptions, hypotheses, attempted actions, rejected approaches, and unresolved issues. Do not present an inference as a confirmed user statement or an attempted test as a successful verification.

## Resolve discrepancies

Documentation is shared memory, not infallible truth. When docs, code, tests, runtime behavior, or new evidence disagree:
1. identify the exact discrepancy;
2. determine which source is stale, incomplete, or incorrect;
3. consult the Goal and relevant evidence;
4. update the authoritative record and actual system consistently;
5. preserve historical rationale when it remains useful.

Do not blindly prefer documentation over implementation or implementation over documentation.

## Keep it maintainable

Keep an obvious authoritative project entry point. Ensure each relevant scope has enough documentation for a new agent to orient itself without reconstructing the entire conversation. Before substantial work, inspect existing records and source locations; before handoff or context loss, reconcile important new facts, decisions, and actual state.


Use names and directory structure that make contents discoverable. Add an index only when names and layout are insufficient. Split documents when doing so improves navigation or ownership, not merely to satisfy a line-count rule. Keep current state prominent; move obsolete detail to history only when it has continuing value.

## Deliverable

A compact, navigable, internally consistent project memory with clear authoritative sources, useful rationale, and evidence links—without documentation overhead disproportionate to the project.
