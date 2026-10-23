# Delivered from root_manager — one more class, found while delivering the first five

## 6. One tree's commit hook runs another tree's check against that tree's uncommitted work

- **Rule in play:** the workspace's pre-commit hook runs the policy tool inside `agent-policy/` and refuses when the law's views are uncommitted. That check is right for a change to the law. It is wrong for a change to a note, a pin, or a mail file.
- **Executable as written:** no. While the policy writer is mid-edit — which is exactly when a delivery is being made — the law repository is legitimately dirty, the hook fails, and **every commit in the workspace is blocked**, including the ones that carry the delivery. Measured 2026-10-23: two attempts, both refused with a YAML error from a half-written `AGENTS.yaml`.
- **Why it happened:** the hook's condition is "the law's views must match the law", which is a local check inside the law repository. The hook recomputes it from a tree another writer owns, and a recomputation over somebody else's half-finished edit reports their state as this commit's defect.
- **What root_manager makes of it:** this is the second time today that a check failed closed over a condition it does not own — the first was the hook naming two tools the law repository had already merged into one. Both cost more than the defect they guard.
- **Suggestion:** the hook checks what this commit changed. A commit that touches no file under `agent-policy/` runs no law check; a commit that moves the law's pin checks the law at that commit, not at the working tree. And a check that depends on another writer's tree says whose tree it is reading when it fails.

Related: the delivery of notes and the editing of law share one directory, so root_manager's commits and the policy writer's commits collide by construction. Where a note lands is a receiving side; which branch it lands on is a scheduling question nobody has answered.
