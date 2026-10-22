# Review contract

One reviewer per role. Read the role's view (`agents/<role>.md`), the law (`AGENTS.yaml`), the case metric (`/home/z/vibe/docs/method/review.md`), and the writing lens (`/home/z/.agents/skills/writing-for-agents/SKILL.md`). Do not read another role's view: a reviewer that knows what the others were told invents the answer instead of finding it missing.

## The case metric

One row per case, in the order the role meets it: the moment, the axis (`authority`/`proceed`), the verdict (`stated`/`delegated`/`ambiguous`/`silent`), the sentence that settles it or the missing one, and the wrong action the role would most likely take when it is missing.
An authority case may not be `ambiguous` or `silent`. A proceed case may be `delegated`, but an implicit delegation scores as `silent`.

## The nine content checks

1. **Redundancy**: the same meaning twice, inside the view or against the law.
2. **Conflict**: two rules that cannot both hold.
3. **Stale**: a reference to something that no longer exists.
4. **Completeness**: a real case the role meets is not covered. Target 99%; only a case that is both nearly impossible and cheap may be left.
5. **Necessity / no-op**: a line the model already obeys by default; use the writing-for-agents no-op test.
6. **Logical self-consistency**: parent and child relations hold; a rule's how reaches its goal.
7. **Omission**: a class of rules that should exist and is absent.
8. **SMART**: not specific, not actionable; an adjective instead of an action.
9. **Self-consistency**: the view obeys the law it states (SSOT, no diary, naming, etc.).

## The SOP test

For every case, the view says what the role does next, in order, with a completion criterion. A goal without a how is not an SOP.

## The balance test

For every decision rule: two ends, each with a cost and a payer; the band; the pull that says which way to yield. If it cannot be written as a balance, the design is the defect.

## The writing lens

Leading words, no-op, context load, relevance, progressive disclosure. The law's `writing` section is the short form; the skill is the long form.

## System checks

- **Idempotency**: kill at a stable point, reopen, say `go`; the roadmap state is the same, and no node becomes ready because the session restarted.
- **Timeout**: every discussed block has an absolute deadline; only the no-discussion (empty) case waits forever.
- **Efficiency**: the declared wall-clock against the actual; exploration outside the contract; the context read.
- **Expectation**: every rule names its goal (the expectation) and its how; a balance carries the goal; information the role must collect outside the contract is named there or reported as a contract defect.

## For a law change

Before a change lands, name the existing rule it amends or the search that found none. A change that does neither is refused.

## Evidence

One report per role: the case rows, findings with location, criterion and reproduction, blocking versus non-blocking, and the count of authority cases `ambiguous` or `silent`. A finding without a reproduction is not a finding.
