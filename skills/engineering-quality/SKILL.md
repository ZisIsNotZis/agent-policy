---
name: engineering-quality
description: Use for software implementation, code review, testing strategy, debugging, reliability work, or engineering changes where correctness and maintainability must be demonstrated.
---

# Engineering Quality

## Purpose

Deliver software that satisfies the intended behavior and remains understandable, testable, and reliable within the project's constraints. This playbook applies to engineering work; do not force it onto non-code tasks.

## Before changing code

- Understand the user-visible behavior or system property being changed.
- Read the relevant implementation, tests, interfaces, and project instructions.
- Identify compatibility, security, performance, data, and operational risks that matter.
- Prefer the smallest coherent change that solves the actual problem; do not preserve a flawed design merely to minimize diff size.
- Check whether the defect is local or caused by a shared contract or architecture.

## Implement with quality

- Keep one authoritative implementation of each behavior where practical.
- Respect existing abstractions unless evidence justifies changing them.
- Make interfaces and failure behavior explicit.
- Validate inputs and outputs at meaningful boundaries.
- Handle errors with actionable messages and avoid silently swallowing failures.
- Avoid unnecessary dependencies, hidden state, duplicated logic, and speculative complexity.
- Keep comments focused on non-obvious intent, invariants, and trade-offs—not paraphrases of code.

## Verify proportionately

Choose checks based on risk and change type. Common layers include:
1. formatting, linting, static analysis, and type checks;
2. focused unit tests;
3. integration and API tests;
4. end-to-end or acceptance tests;
5. performance, security, accessibility, or compatibility checks where relevant;
6. manual or expert review for behavior that automation cannot judge.

Run the cheapest useful check early, then broader checks as appropriate. Do not claim tests passed unless they were actually run; report skipped checks and reasons. A green test suite does not prove the product solves the right problem.

## Review

Review the diff against the intended outcome, acceptance criteria, interfaces, and likely failure modes. Look for regressions, unhandled edge cases, unsafe assumptions, unnecessary scope, and tests that do not actually discriminate between correct and incorrect behavior.

Use an independent reviewer when impact, novelty, uncertainty, or cross-component risk warrants it. Ask the reviewer to find material problems, not simply approve the implementation.

## Debugging

Reproduce or characterize the failure where possible. Form a causal hypothesis, gather evidence, and change a meaningful variable when testing a fix. Distinguish transient environment failures from incorrect assumptions, implementation defects, and contract mismatches. After a repeated or systemic failure, reconsider the design or method rather than blindly retrying.

## Change management

Make coherent, reviewable commits or snapshots. Keep changes recoverable. For shared contracts, migrations, or cross-workstream changes, coordinate with affected owners and plan integration checks.

## Completion report

State what changed, the behavior achieved, checks run and their results, known limitations, and what remains unverified. Distinguish implemented, tested, verified, and accepted.
