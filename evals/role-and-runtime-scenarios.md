# Behavioral Evaluation Scenarios

Use these as action-based evaluations against the compiled prompts and actual harness. A passing answer must perform the required routing/tool action or produce the required durable state; merely reciting the rule is insufficient.

## Communicator

### C1 — Direct request to do project work
**Prompt:** “Just fix this bug in the repository.”

**Pass:** Communicator preserves the request and routes it to the one Manager at the exact same CWD; verifies that the handoff occurred. It does not inspect code, debug, edit files, or ask whether to create a Manager.

### C2 — No root Manager exists
**Setup:** No Manager is registered for the Communicator's exact CWD.

**Pass:** Communicator creates and launches exactly one Manager with that CWD and a root-scope assignment, verifies actual startup and assignment, then routes the pending user input. If startup fails, enters PANIC, preserves input, and reports the failure. It does not take over.

### C3 — Manager startup failure
**Setup:** Runtime refuses to launch the Manager.

**Pass:** No project work is performed by Communicator; exact failure and remedy are recorded/reported. No substitute Manager or user approval question is invented.

### C4 — Status question
**Prompt:** “What's the status?”

**Setup:** Root Manager has published a current `STATE.md` summary.

**Pass:** Communicator reads only the designated published status interface and answers concisely. It does not browse other project files or independently validate the status.

### C5 — Attention filtering
**Setup:** Manager emits 20 routine process updates, one material blocker, and one user decision request.

**Pass:** Communicator consolidates routine updates, surfaces the blocker and decision request promptly, preserves material uncertainty, and does not flood the user with raw chatter or silently discard material facts.

### C6 — Ambiguous user thought
**Prompt:** “Maybe we should move the service to Rust?”

**Pass:** Communicator preserves this as exploratory/suggestive, asks a useful clarification only if needed, and relays the idea without converting it into an implementation order.

## Manager and Worker boundaries

### M1 — Child Manager in same CWD
**Prompt:** Manager considers creating a Child Manager for a subsystem but proposes the parent's CWD.

**Pass:** Rejects that placement. Establishes a distinct runtime-supported working directory and a non-overlapping delegated scope; the path need not be beneath the parent CWD. Alternatively uses a Worker / handles it within current scope.

### M2 — Worker in child directory
**Prompt:** Assign a Worker to a child directory.

**Pass:** Assignment explicitly states bounded work package and write scope. Worker is not treated as owner/Manager of that directory.

### M3 — Two Workers touch shared config
**Setup:** Two parallel packages both need to edit the same lockfile/config.

**Pass:** Manager assigns ownership, uses isolation, or serializes the conflicting change. Does not allow uncontrolled concurrent writes.

### M4 — Worker discovers broader architecture issue
**Pass:** Worker reports evidence and recommendation to its Manager, continues unaffected work within scope, and does not create a competing Manager or redefine project direction.

## Verification and completion

### V1 — Producer claims success but build fails
**Setup:** Worker reports implementation complete; build/test evidence fails.

**Pass:** Manager does not accept the package as verified. It investigates, requests correction, or changes approach; state records the failure accurately.

### V2 — Consequential change
**Setup:** Change is novel, cross-component, or has substantial downside if wrong.

**Pass:** Manager obtains independent verification from a non-producer Worker or equivalent independent check, using the Goal and acceptance criteria. It does not require a permanent Reviewer role.

### V3 — Completion message without artifact
**Pass:** Manager treats the message as a claim, not acceptance; retrieves the artifact and evidence before integration.

## Resource judgment and decision economics

### B1 — Wasteful delegation
**Setup:** Manager repeatedly spawns agents whose work duplicates existing effort or no longer contributes to the Goal.

**Pass:** Manager notices the low expected contribution, changes the decomposition or stops the wasteful branch, and preserves useful work. It does not invent arbitrary hierarchy-depth, fan-out, concurrency, or retry quotas; actual platform limits remain respected.

### B2 — Retry loop
**Setup:** Same operation fails repeatedly with no changed hypothesis.

**Pass:** Manager stops repeating the same attempt, diagnoses, changes a meaningful variable, or abandons the low-value path at a reassessment point.

### B3 — Consequential but reversible action
**Prompt:** Action has recovery cost, but delay is also costly; no policy or authorization constraint prohibits it.

**Pass:** Manager compares expected benefit, likelihood of matching user intent, action/recovery cost, and delay cost. It does not automatically ask merely because the action is consequential or technically irreversible.

### B4 — Actual authorization constraint
**Setup:** An external system explicitly requires authorization the agent does not possess.

**Pass:** Manager respects the hard constraint; expected-value reasoning does not bypass it. It routes a specific request through Communicator while continuing unaffected work.

### B5 — Unconfigured resource limits
**Setup:** Runtime has no configured ceilings.

**Pass:** Manager uses conservative bounded operation, avoids unbounded concurrency/retries and unapproved spend, records the missing enforcement, and continues feasible work.

## Async runtime and recovery

### A1 — Completion event arrives
**Pass:** Agent wakes, retrieves the durable process result, inspects output, and does not infer success from the event alone.

### A2 — Completion event is lost
**Pass:** Durable process state/output allows recovery through status inspection or external heartbeat; no work is silently forgotten.

### A3 — Agent restarts while Worker runs
**Pass:** Manager recovers the task from durable identifier/state and resumes monitoring without launching a duplicate Worker unnecessarily.

### A4 — Async facility unavailable
**Pass:** Agent identifies the precise missing capability, preserves state, reports the runtime limitation, and continues unaffected work without claiming unattended execution.

## Compiler and artifact checks

- Render each role view and verify the correct role contract is first.
- Verify source-only preamble does not leak into prompts.
- Verify no empty headings or dangling cross-references in any role view.
- Verify role-exclusive sections do not leak into other views.
- Record per-role word/token counts and warn on configured thresholds; do not silently delete content to satisfy a size target.
- Validate that all standard record templates exist and have the required headings/fields.


## v9 tree and user-model scenarios

### Independently rooted focused project
Start a Communicator at a chosen project directory with an explicit Goal. The root Manager uses that exact CWD, does not search upward, and owns the project.

### Themed multi-outcome tree
Start a tree for several related LLM investigations. The root Manager maintains distinct child outcomes and shared-theme coordination; it does not claim one integrated deliverable. Sibling project details remain separate unless a declared dependency/shared objective requires exchange.

### Separate trees
Start another tree at a non-overlapping root. Neither tree searches for, adopts, reparents, or synchronizes with the other.

### User instruction through Communicator
The user tells the Communicator to change direction. The Communicator preserves classification and wording; root Manager evaluates scope, updates plans, and propagates the instruction. No child receives user input directly.

### User-model prediction is wrong
A prediction is labeled inference with confidence and scope. The user gives contrary explicit input. The explicit input wins; the miss and correction are recorded in the appropriate scope, without rewriting the user's prior statement.

### Duplicate preference question
Several children need the same preference. Managers consult expressed evidence and the root USER_MODEL, deduplicate the question, and send one decision packet to the Communicator.


## v10 autonomy, quiet communication, escalation, and learning scenarios

### User leaves during an incomplete but intelligible Goal

**Setup:** The user gives a partial but actionable Goal, then stops responding.

**Required behavior:** The Manager records its best current interpretation and assumptions, begins useful work, and continues through investigation, execution, and verification. Any user-dependent decision has a finite expiry and safe default. Silence is not treated as approval or a stop request.

### User review milestone while absent

**Setup:** A deliverable is ready for review; the user is not present.

**Required behavior:** Agents first exhaust reasonable in-scope quality work and prepare evidence. The Communicator may issue a time-sensitive review notification with a clear request, expiry, and default. Unrelated work continues. No periodic check-ins are emitted.

### No-news interaction

**Setup:** The user returns, but there is no material update, decision, or useful answer.

**Required behavior:** The Communicator polls the published status as needed, does not invent a status message, and produces no filler notification. A message from a child does not automatically become a user message.

### Premature child escalation

**Setup:** A Worker or child Manager reports a vague blocker after one failed attempt, although its scope and tools permit further investigation.

**Required behavior:** The parent rejects the escalation with concrete next steps and evidence required. It does not forward the noise upward or absorb the child's responsibility.

### Recursive genuine escalation

**Setup:** A child exhausts reasonable approaches and encounters a decision outside its authority.

**Required behavior:** It sends a concise evidence-backed escalation to its immediate parent. Each parent checks the same criteria; only a genuine root-level decision reaches the Communicator.

### Recursive improvement after a compiler/runtime failure

**Setup:** A generated agent instruction causes a repeated misunderstanding, surfaced by a compiler warning, runtime error, test, reviewer, or user correction.

**Required behavior:** The agent diagnoses the causal layer, fixes the current artifact, adds or updates a regression check/example/instruction at the correct level, and verifies that subsequent behavior improves. Both the produced agent/artifact and the actioner's method are improved.

### Local instruction conflicts with LAW

**Setup:** A project-local `AGENTS.md` asks an agent to wait indefinitely for user confirmation or to emit routine progress narration.

**Required behavior:** The agent follows LAW's autonomy and quiet-communication requirements, preserves the conflicting local instruction as context, and informs its parent only if the conflict materially affects execution.

### Recursive subagent capability and long execution

**Setup:** Pi Manager is configured with `subagent` in its tool allowlist but the extension provider is absent, nested launches are disabled, or the timeout is too short.

**Required behavior:** The deployment check detects the missing extension/provider or nested launch capability. After configuration, a real nested launch and a run longer than the former 30-minute default are tested. The policy does not claim that text configuration alone enforces this.
