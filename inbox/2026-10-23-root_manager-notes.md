# Delivered from root_manager — five error classes, 2026-10-23

This lands here because this is the policy writer's side. The earlier copy at `notes/2026-10-23-root.md` in the workspace is root_manager's own record; this file is the delivery.

Each class carries the five things that were asked for: which rule was in play, whether it could be executed as written, why it was not, what root_manager makes of it, and what it suggests changing. Where the suggestion is a rule, it is a suggestion — the writer decides.

---

## 1. A question reached the person in a project's internal handles

- **Rule in play:** `asking.self_contained`, `to_human.name_concretely`, `person_record.vocabulary`.
- **Executable as written:** yes. The person's vocabulary was on hand; nothing in the rule was ambiguous.
- **Why it still happened:** a question travels up in the form the project wrote it, and carrying is copying. Nothing between "the project filed a question" and "the person reads it" asks whether each noun can be pointed at. The rule binds the *author* of a question, and at that moment root_manager is the author.
- **What root_manager makes of it:** the rule is right and the missing thing is a step, not a sentence. The person's correction cost one round trip; the same shape will recur every time a gate is carried.
- **Suggestion:** the carrying of a question up is itself an act with a check — every noun in the question is either in the person's own words or is a thing they can point at, and a question that fails is sent back to the project rather than up. Where it already exists, this is `to_human.reviewing.open` one layer too narrow.

## 2. root_manager performed the policy writer's craft

- **Rule in play:** `rdi_agent.feedback_path` ("Root only hands it to Policy Worker or Policy Reviewer"), and the authority split in `reasoning.authority`.
- **Executable as written:** yes — and it was executed, eventually, after the person said so. The rule was not what failed.
- **Why it still happened:** the law file was open in root_manager's context because root_manager had been reading it to answer a question, and `edit` on an open file is one call where a delivery is two. The rule says who decides; it does not say what root_manager's hands may touch.
- **What root_manager makes of it:** the failure is not judgement but reach. A role that may read a submodule will eventually write it, and the law's own hand-off sentence is too far from the moment of the edit to fire.
- **Suggestion:** name the surface rather than the intention — root_manager's tools do not include writing inside the policy repository at all, and the delivery of a note is a file placed on the writer's side. A law that only forbids the act will be re-broken by whoever has root_manager's tool list.

## 3. A law's reason was asserted from mechanism instead of read from the record

- **Rule in play:** the policy writer's review contract on `_know` — "actual project details; an impression, not an investigation; no 大道理", and the requirement that a reason carry what was chosen, why now, the price, and the observation that would make it wrong.
- **Executable as written:** the contract was — but it binds the writer, and root_manager was writing. The reviewer caught both false sentences; the loop held.
- **Why it still happened:** the incident's numbers were three files away and the sentence was one line long, so the line was written from how billing should work rather than from the 42 rows that show how it did.
- **What root_manager makes of it:** this one is the cheapest to prevent and the most expensive to leave, because a rule whose reason is false teaches a reader to obey for a false reason. That it was caught twice by review is the contract working, not a substitute for the fix.
- **Suggestion:** a `_know` carries the read that produced it — the command or the file:line — and the review contract checks that the read exists and says what the sentence says. A reason nobody can re-run is a slogan with numbers in it.

## 4. A stale environment fact was sent as current

- **Rule in play:** `the_world_changes.truth.machine_fact`, added the same evening from this incident.
- **Executable as written:** it did not exist at the time of the incident; it exists now and covers it.
- **Why it still happened:** three reads of the host for a claim about a port, and no read of the port.
- **What root_manager makes of it:** covered. The only open question is whether a second project repeated the same error (a service reported stopped, read from a process table, while it was serving) and whether that reached the record anywhere.
- **Suggestion:** none for the rule; a check on whether the projects still holding a service claim have re-read it is work, not law.

## 5. root_manager spent its context doing instead of dispatching

- **Rule in play:** the portfolio's own sentence — "the root learns a project by asking it, not by reading it" — and `resources_are_limited.economy` on where effort is placed.
- **Executable as written:** the rule exists and names the right thing; it sets no bound, so it cannot be broken, only bypassed.
- **Why it still happened:** reading felt faster than dispatching, and nothing measured the cost. The person measured it: a fifth of the context in an hour, then unable to hold the whole tree.
- **What root_manager makes of it:** a rule that says "ask, don't read" with no threshold will lose to convenience every time. The cost is not only tokens: a root_manager that has read a project argues with its own summary instead of the project's answer.
- **Suggestion:** a bound with a number — root_manager reads a project's filed message and its one-line state, and anything deeper is a question to the project; a read beyond that is itself the error to be noted.

---

## Two defects in the law found while delivering this

1. **The role's name is inconsistent.** Prose in `rdi_agent` and elsewhere says "Root", while `roles.yaml` names the role `root_manager`. A name that exists in two forms is one name a reader will resolve wrongly, and this file was written wrongly because of it — the first copy says "root" throughout.
2. **There is no place for a note to arrive.** `rdi_agent` says "sends it up one level" and "Root only hands it to Policy Worker", but nothing in this repository receives: there was no inbox here until this file created one. A hand-off with no receiving side is a rule that can only be obeyed by editing the law, which is exactly defect 2 above.
