---
name: planning-and-decomposition
description: Use when turning a project Goal into workstreams, delegating to agents, planning milestones, coordinating dependencies, or revising a plan after new findings.
---

# Planning and Decomposition

## Purpose

Create enough structure for coordinated progress while preserving the ability to discover and change a better path.

## Plan from outcomes

Start with the intended result and its major capabilities, questions, or deliverables. Decompose only as far as needed to assign ownership, expose dependencies, estimate resources, and evaluate progress. Do not decompose every detail in advance.

A work package may produce software, research, an experiment, a design, a decision, a dataset, or a validated finding. Define the expected outcome rather than assuming all work is implementation.

## Build an adaptive plan

For each meaningful work item, identify as relevant:
- intended outcome and Goal connection;
- owner and decision rights;
- scope, exclusions, and constraints;
- deliverable or expected learning;
- acceptance/evaluation method;
- relevant context and authoritative references;
- interfaces, dependencies, and affected owners;
- resource envelope and review/checkpoint;
- reviewer and integration owner.

Keep near-term work concrete and distant work directional. Avoid false precision where uncertainty is high.

## Optional top-down decomposition method

Use this when the work has a structured hierarchy (for example, a new system, module, workflow, or policy). Do not force it onto exploratory discovery, where the right categories may not yet be known.

1. State the question or outcome for the current layer in one sentence.
2. Define the boundary: inputs, outputs, assumptions, and what is outside this layer.
3. Enumerate the major subitems, each with a distinct responsibility.
4. Check **coverage**: identify the relevant dimensions of the parent question and verify that each important case or responsibility belongs somewhere. Add or split items when a meaningful case is unowned.
5. Check **non-duplication**: if two items always lead to the same decision or own the same responsibility, consider merging them; keep them separate when they produce meaningfully different outcomes.
6. Repeat only until each leaf can be assigned, implemented, investigated, or evaluated independently enough for the project.
7. Reassemble the parts mentally and verify that they still cover the parent outcome without unnecessary duplication.

The goal is a complete-enough and non-overlapping decomposition for the current decision—not mathematical proof of exhaustive completeness. Revisit the decomposition when evidence contradicts its assumptions.

## Model dependencies as a changing graph

Track meaningful prerequisites and shared interfaces. A work item can be:
- ready;
- partially actionable;
- blocked by a named dependency;
- obsolete or superseded;
- complete but awaiting integration or acceptance.

Update dependencies when discoveries change the order or make work newly actionable. Continue unaffected work instead of waiting on an entire workstream. Do not assume parallel work is independent merely because it has separate owners.

## Delegate with judgment

Give the receiver enough context to understand the outcome and boundaries. State what decisions it can make independently and what requires coordination. Include a suggested approach only when it materially reduces risk or conveys a necessary constraint.

A time box or checkpoint should trigger reassessment, not automatic abandonment. At the checkpoint, compare progress and evidence with remaining cost and expected value. Continue, redirect, narrow, hand over a useful partial, or stop with a reason.

## Integrate deliberately

The Manager owns project-level integration; a Sub-Manager owns integration within its subtree. They may delegate mechanics but retain accountability. Plan integration checks early enough to discover incompatibilities before the final delivery.

## Keep planning lightweight

Maintain the current plan in the project's existing roadmap or planning source of truth. Do not create per-task documents or ticket machinery unless the project genuinely benefits from it. Record changes that affect owners, dependencies, scope, acceptance, or milestones; do not log every routine adjustment.

## Deliverable

A current, understandable plan that shows outcomes, owners, dependencies, decision rights, resource expectations, evaluation, and integration responsibility—at a level of detail appropriate to uncertainty.
