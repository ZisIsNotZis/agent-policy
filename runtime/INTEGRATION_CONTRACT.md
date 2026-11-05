# Runtime Integration Contract

This document translates LAW requirements into harness/runtime capabilities. It is an implementation checklist, not a claim that any particular runtime already provides them.

## 1. Root Manager singleton and PANIC

The runtime should expose a Manager registry keyed by canonicalized absolute CWD (and scope identity where needed).

- `find_root_manager(cwd)` returns the existing root Manager and its process/assignment state.
- `start_root_manager(cwd, assignment)` atomically prevents duplicate root Managers for the same CWD.
- Startup acknowledgement confirms both process start and receipt of the root-scope assignment.
- Health/status inspection distinguishes starting, running, unreachable, exited, and failed.
- Communicator may enter normal routing only after verified establishment.
- If no Manager can be established, Communicator enters PANIC; it must not silently continue as Manager.

A process that merely exists but has not received its role/scope assignment is not an established Manager.

## 2. Child Manager scope uniqueness

Before launch, validate:

- Child Manager receives a distinct, runtime-supported working directory; it need not be beneath the parent CWD.
- The child managed scope is explicitly defined and non-overlapping; CWD is not treated as the ownership boundary.
- No other active Manager has overlapping exclusive operational ownership.
- Parent/child relationship and assignment are durably recorded.

Reject same-CWD Child Manager launches. Do not confuse a Worker process in a child directory with a Child Manager.

## 3. Worker work-package and write scope

Every Worker launch should carry a structured assignment containing role, CWD, package ID, write scope, exclusions, shared resources, deliverable, acceptance conditions, and parent identity.

CWD alone is not a write lock. The runtime/project workflow should support one or more of:

- isolated worktrees/branches/copies;
- file/resource ownership locks;
- serialized access to shared mutable resources;
- explicit coordination before merging conflicting changes.

The Git index, generated indexes, lockfiles, shared configuration, and shared libraries are mutable shared resources when multiple agents can touch them.

## 4. Actual platform constraints and execution duration

The runtime must expose and enforce genuine platform, authorization, contractual, or explicitly configured limits that apply to a process. Do not introduce arbitrary hierarchy-depth, fan-out, concurrency, or retry ceilings as a policy default. The organization may grow to whatever recursive depth and parallelism the Goal and available harness capabilities justify.

The current Pi `pi-subagents` extension itself imposes a finite nested-depth guard (documented default: two levels). This is a harness limitation, not a LAW rule. Configure a high finite `PI_SUBAGENT_MAX_DEPTH` and avoid stricter per-agent depth settings; if the required tree exceeds that value, the runtime must be extended. See `PI_SUBAGENTS_CONFIGURATION.md`.

For Pi deployments, configure a finite execution timeout long enough for legitimate delegated work; do not leave a short default that routinely kills Managers while their children continue, and do not assume an unlimited timeout is safe. The current extension supports `timeoutMs` in milliseconds; see `PI_SUBAGENTS_CONFIGURATION.md`.

When a real platform limit is encountered, report the exact limit and affected operation, adapt the method, and continue unaffected work. A limit is not permission to abandon the Goal or to invent a broader restriction than the platform actually imposes.

## 5. Asynchronous process and event contract

Required operations:

1. Launch independently and return a durable process/run ID promptly.
2. Inspect process state without blocking.
3. Retrieve stdout/stderr or equivalent output by ID.
4. Cancel/terminate where supported.
5. Emit completion/failure events that wake or schedule the responsible agent.
6. Persist process state and output independently of the event delivery path.
7. Recover in-flight runs after an agent/runtime restart and avoid accidental duplicate launches.

Completion events may be duplicated, delayed, or lost. The receiver must be able to query authoritative process state and output. Event acknowledgement/retry semantics should prevent silent loss where the platform supports it.

## 6. Published status interface

The root Manager publishes a concise user-facing summary in the root scope's `STATE.md` or a designated equivalent status endpoint. The Communicator receives read-only access to that publication, not general project filesystem access.

The publication should include last-updated time, current outcome status, material progress, blockers/risks, user-input requests, and next meaningful action. Internal logs and raw agent chatter remain outside the user-facing summary unless material.

## 7. Compiler and CI integration

Run the production role-view compiler in CI and validate:

- role tags and inheritance;
- correct role identity at the start of each view;
- no source-only preamble leakage;
- no empty headings or dangling cross-references;
- role-exclusive content does not leak;
- token/word counts are reported and configurable thresholds warn or fail according to deployment policy;
- required templates and skill references exist.

The included `tools/lint_policy.py` is a reference checker only. The production compiler remains authoritative for generated prompt output.


## v9 organizational assumptions

A tree is explicitly started at the Communicator CWD with an explicit Goal and scope. The user avoids overlapping tree roots. The runtime does not need to discover/adopt/re-parent trees or search parent directories for goals. The root Manager shares the Communicator CWD; descendant CWD placement is independent of managed-scope ownership. A runtime may later implement machine-generated portfolio rollups from the fixed STATE summary fields, but the policy does not assume that mechanism exists.
