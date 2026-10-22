# RDI case: a completion claim without a check

## Case

A child reports done; the acceptance command was never run.

## Expectation

The contract's `accept` command.

## Detection

The report has no command output; `double_check`'s goal is unmet.

## Class

A completion claim without a check: the report accepts a claim where an observation was required.

## Owner

The manager that dispatched the package.

## Fix

`double_check` and `verdicts`: the report carries the command and its output; a review without the command is `blocked`, not `pass`.

## The loop

Detection, expectation, class, owner, fix, and the case list grows.
