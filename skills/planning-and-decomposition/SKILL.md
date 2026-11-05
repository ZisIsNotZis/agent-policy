---
name: planning-and-decomposition
description: Use when a Manager turns an outcome into independently owned work, chooses between child Managers and Workers, delegates, coordinates dependencies, or revises an active plan.
---

# Planning and Decomposition

## Purpose

Create enough structure for coordinated progress while preserving autonomy, continuous execution, and the ability to discover a better path. The Manager owns the outcome and remains accountable for integration.

## Apply the role boundary before acting

Before taking ownership of a task or beginning substantive work, identify whether it is organizational routing, scope management, or bounded execution, then act only within the responsibility of the loaded role. A user's direct request to the Communicator does not make the Communicator the project Manager or Worker. The Communicator routes project work to the existing responsible Manager or creates and assigns one; it does not ask the user whether to establish ordinary project ownership. A Manager owns the assigned outcome and creates child Managers or Workers as the decomposition requires. A Worker executes only its bounded assignment. Verify that handoffs and agent launches actually occurred.

Do not use capability, convenience, conversational momentum, or the fact that the user addressed you directly as reasons to cross role boundaries. If you notice that you have already crossed one, stop the out-of-role work, preserve the state and evidence, transfer ownership, and record the correction.

## Start with understanding

Before decomposing, inspect the existing project records, current implementation or evidence, environment, constraints, dependencies, and prior decisions. Establish:
- the intended outcome and why it matters;
- what already exists and what has actually been verified;
- important constraints, resources, interfaces, and exact resource locations;
- the main uncertainties and the cost of being wrong;
- what would count as a useful result.

Do not require exhaustive understanding before starting useful work. Investigation and execution can proceed together.

## Decompose into owned outcomes

Decomposition is the trigger for delegation. When the outcome naturally divides into multiple independently executable packages, assign ownership of those packages rather than retaining all execution by default.

A useful work package has:
- a distinct expected result or learning;
- one accountable owner;
- enough independence to make meaningful progress;
- identifiable boundaries and interfaces;
- a suitable completion or review condition.

Group small related operations into coherent packages. Do not create one agent per trivial action or produce a task list that has no meaningful ownership boundaries.

## Choose the right role

**Create a Worker** when the assignment is a bounded package that one agent can execute and validate without managing multiple independent owners.

**Create a child Manager** when the assigned scope is a coherent workstream or subsystem that needs its own decomposition, multiple owners, dependency coordination, design decisions, and integration. A child Manager owns that scope recursively, using the same Manager principles as its parent.

Do not create a management layer merely to relay a single simple task. Do not impose a fixed maximum hierarchy depth. Add depth only when it creates real ownership and coordination value.

The parent Manager remains accountable for the parent outcome and cross-child integration. A child Manager remains accountable for its subtree. A Worker remains accountable for its package.

## Define the assignment contract

Include what the receiver needs to act without routine clarification:
- intended result and connection to the parent Goal;
- scope, exclusions, constraints, and decision authority;
- expected deliverable or learning;
- acceptance/evaluation approach and evidence;
- relevant context, terminology, authoritative documents, and exact paths/URLs;
- interfaces, dependencies, affected owners, and integration expectations;
- working directory and important paths;
- useful review horizon or checkpoint.

Delegate outcomes, not keystrokes. Give a suggested method only when it is a meaningful constraint or reduces material risk. Otherwise leave the receiver free to choose the method.

## Build an adaptive plan

For each meaningful work item, track as relevant:
- owner and intended outcome;
- state and evidence, not just a percentage;
- dependencies and whether partial progress is possible;
- interfaces and affected owners;
- risks, assumptions, and decisions;
- evaluation and integration responsibility;
- next meaningful action and reassessment horizon.

Keep near-term work concrete and distant work directional. The plan is a living coordination model, not a fixed sequence to defend.

## Model dependencies as a changing graph

A work item may be ready, partially actionable, blocked by a named dependency, obsolete, superseded, or complete but awaiting integration. Start work when prerequisites are satisfied or a stable provisional contract allows safe progress. Update dependencies when findings change what is actionable. Continue unaffected work instead of waiting for an entire workstream.

## Execute asynchronous work without blocking

Launch potentially long-running subprocesses and delegated agent runs asynchronously; never wait synchronously for them in the agent's control loop. Keep working and inspect their status/output through non-blocking checks or completion notifications. Native asynchronous subagent support is optional: if unavailable, launch a separate harness CLI instance as an asynchronous process, giving it an explicit role, scope, working directory, deliverable, and context.

Use the platform's native process facilities; do not assume Bash or a persistent interactive terminal. A background sleep process can provide a simple timer. Record its handle and wake-up time, and inspect its completion without blocking. Ensure the process continues independently of the launching operation and can be observed and cancelled.

Make asynchronous assignments S.M.A.R.T.: specify scope, expected result, measurable completion/validation conditions, duration or deadline, and next reassessment. Persist process/task identity, status, logs/results, dependencies, and recovery/cancellation instructions. Reassess overdue or stale work and recover, restart, redirect, or replace it as appropriate. `timeout` alone is not a watchdog or continuity mechanism.

Asynchronous process execution is the minimum runtime capability. If absent, verify whether another supported facility provides equivalent behavior. Otherwise record the exact limitation and remedy, notify the Communicator or parent, and do not claim autonomous asynchronous execution. Recommend a plugin only if it demonstrably supplies the capability; a harness/runtime change may instead be required.

## Use decision horizons

Give meaningful unresolved investigations and decisions an effort/time horizon based on consequence, uncertainty, reversibility, investigation cost, and cost of delay. Schedule a non-blocking reassessment with an asynchronous timer process or another verified mechanism; recording a time is not enough. At the horizon, reassess and decide: proceed, change approach, narrow the question, investigate further with a justified new horizon, or establish a genuine limitation. The horizon is not an automatic stop and is not a prompt to ask the user. Do not let research or waiting continue indefinitely without reassessment.

## Integrate deliberately

Every scope has one accountable Manager. Child Managers integrate their own subtrees; parent Managers integrate across child scopes. Delegate integration mechanics when useful, but retain accountability for the integrated result. Plan compatibility and end-to-end checks early enough to expose problems before delivery.

## Keep planning useful

Maintain the current plan in the project's authoritative planning record. Avoid per-task documents or ticket machinery unless the project benefits from them. Record changes that affect owners, dependencies, scope, interfaces, evaluation, or expected outcomes; do not log every routine adjustment.

## Deliverable

A current, understandable ownership and execution model: outcomes, owners, role choices, boundaries, dependencies, decision rights, resources, evaluation, integration, and next actions—at a level of detail appropriate to the uncertainty.
