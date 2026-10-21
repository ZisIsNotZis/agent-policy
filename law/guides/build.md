# Build

## A slice

One behaviour a person could judge, from the caller's side, with its check. Then the next. Do not batch a design and its checks and its wiring into one act, because then no evidence separates the parts.

## Boundaries

An interface is everything a caller must know: types, invariants, order, configuration, error modes. Hide what is incidental; keep what the caller must not get wrong.

Introduce an abstraction when the variation is real and can be named. A direct form is the default, and a layer that removes only hypothetical complexity is a cost.

## Change shape

Separate a structural change from a behaviour change, or the diff cannot say which one broke it. If behaviour must change, say so before the edit.

You commit the area your contract named and nothing else. A commit that sweeps a sibling's half-written file is the unreviewable diff the one-writer rule exists to prevent, arriving by way of the rule that requires a commit.

## Refactor

Define the behaviour that stays, characterise it where it is missing, then move in steps small enough to reverse. Rerun the checks the move invalidated.
