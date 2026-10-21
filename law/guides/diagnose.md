# Diagnose

## Reproduce first

Capture the exact wrong output, the inputs and the versions. Then remove one element at a time while the wrong output stays. Stop when further removal would remove fidelity or cost more than it discriminates.

An intermittent failure gets a rate, a seed and a count of attempts. It does not need to be deterministic to be diagnosed.

## One discriminating probe

Rank the plausible causes and state, for each, the observation that would kill it. Run the probe that separates the top two. A plausible narrative with no separating observation is still a guess.

## Unavailable

If it will not reproduce within the budget, record what was tried, what access was missing, and a bounded diagnosis marked provisional. Do not call it verified. Ask only for the access that changes the answer.

## Closure

This section applies when the contract is to fix. A package that is only to name the cause stops at the cause, reports it, and leaves the edit to whoever owns the fix.

Fix the cause, not the symptom. Keep a check that fails on the original input. Rerun the original scenario unreduced, because a nearby green check is not the original scenario. Remove the instrumentation, or state why it stays.
