---
name: documentation-and-ssot
description: Use when creating or restructuring project documentation, deciding what should be recorded, maintaining shared agent memory, resolving conflicting sources, or designing a project-specific documentation structure.
---

# Documentation and SSOT

## Purpose

Preserve the smallest reliable body of information that lets people and agents understand current truth, make consistent decisions, continue work, and avoid repeating expensive mistakes.

## Choose documents for the project

Do not force every project into one template. Select documents according to the work:
- software/product work may need Goal, use cases, product decisions, architecture, and roadmap;
- research may need research questions, hypotheses, prior art, experimental design, evaluation methods, results, and limitations;
- creative work may need intent, references, constraints, iterations, review criteria, and selected direction;
- operational work may need service boundaries, runbooks, ownership, and incident knowledge.

Prefer a small number of clear, useful documents over a large taxonomy. Each document should have a distinct purpose and an obvious owner.

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

Use names and directory structure that make contents discoverable. Add an index only when names and layout are insufficient. Split documents when doing so improves navigation or ownership, not merely to satisfy a line-count rule. Keep current state prominent; move obsolete detail to history only when it has continuing value.

## Deliverable

A compact, navigable, internally consistent project memory with clear authoritative sources, useful rationale, and evidence links—without documentation overhead disproportionate to the project.
