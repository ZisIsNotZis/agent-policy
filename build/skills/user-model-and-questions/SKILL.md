---
name: user-model-and-questions
description: Use this skill when recording user evidence, interpreting preferences, deciding whether to ask the user, or preparing a decision packet. LAW remains authoritative.
---

# Ownership

- The Communicator maintains raw user-evidence records: faithful/verbatim statement, timestamp/context, classification (directive, correction, preference, suggestion, question, or other), and the scope in which it was expressed.
- The root Manager maintains the one authoritative derived `USER_MODEL.md` for the tree.
- Descendant Managers consume that model. They may add scoped local overrides/context, but never create a competing global model.
- Keep user-expressed facts separate from agent predictions. Predictions are inferences, never statements by the user.

# Evidence and scope

For each preference or tendency, record: proposition, expressed/inferred status, source evidence, context/scope, confidence, date, contradictory evidence, and last calibration. A preference expressed in one project is local to that project unless the user explicitly generalizes it or evidence supports a cautious broader inference. Test generalization at the first materially divergent context.

Explicit current user instructions outrank inferred preferences. Preserve exceptions instead of explaining them away. When a prediction differs from the user's actual answer or behavior, record the miss, revise the model at the narrowest justified scope, and reduce confidence where appropriate. Treat old evidence as potentially stale; revisit it when consequential.

# Whether to ask

Before asking: (1) define the decision; (2) search expressed evidence; (3) consult the authoritative model; (4) assess uncertainty, stakes, reuse across current/future decisions, and attention cost; (5) decide whether clarification is worth its cost. Do not ask trivia merely because uncertainty exists. Continue unaffected work. Deduplicate equivalent questions across child scopes.

# Decision packet

Send the Communicator a packet with:

- decision needed and why it matters;
- viable options and consequences;
- recommended default and rationale;
- prediction (if any), confidence, and evidence;
- stakes and reversibility;
- answer scope (this task, project, tree-wide, or explicitly global) and expected reuse;
- expiry and default action on timeout;
- what work continues while awaiting an answer.

The Manager determines the information needed and packet substance. The Communicator determines wording, batching, order, timing, and interaction format. It may use runtime-observed interaction facts (such as response latency or repeatedly ignored prompts) to improve delivery, but must not independently assess project state or silently discard a material question.

Prefer a concrete predicted choice that is easy to correct: “I'd choose B because X; is that right?” Do not force-choice when options are misleading or the user's own framing is essential.
