# Operations

## Nothing long inside a turn

A turn is a channel a person can interrupt, so nothing that takes minutes runs inside it. It runs detached, behind a named log and an identifier, and its completion comes back as a message.

A timeout is not a guard against being stuck. It kills the process it started and not the processes that process started, and it does not survive a process that ignores it.

No node blocks waiting for a child. A child returns immediately and its result arrives when it arrives.

Waiting is never written as a sleep. A command that begins with `sleep` is the one case the promotion floor does not rescue, and it is the most common way a node blocks itself.

The client's own budget belongs here too: an unbounded retry count and a disabled idle timeout turn one stalled connection into a permanent block, whatever the command was doing.

## Spend

Every contract states what its package consumes in classes, not in one number, because two packages of equal size can cost different things.

- `time`: how long it holds its own node. The cost is the person's latency.
- `idle-compute`: a local device nothing else wants. The cost is the power, and a site declares once whether that is counted.
- `metered-compute`: a rented device. The cost is money per unit.
- `exclusive`: a device, a slice of its memory, or a port another package cannot share. The cost is the other package's time.
- `unrecoverable`: work whose result is not stored, so a lost run is redone from the start. The cost is the time again, and the money again if the compute was rented.

The class decides what may be released, never the confidence. Work that spends `idle-compute` runs while it is uncertain, because an idle device is the one resource that is wasted by not being used. Work that spends `metered`, `exclusive` or `unrecoverable` takes its grant before it starts, however sure the node is.

A grant that cannot be given stops the package at that line and becomes a `resource` report. Allocation is hereditary: the root grants a container a budget, the container grants from it, and only an exhausted grant travels up. A node that does not know what it will spend says so and asks up the moment it learns.

A child that has written nothing for longer than its declared time is presumed stuck. That is noticed when the node next reads its own roadmap, never by watching it.

## Raising

A question that needs a layer above is a directory that moves, not a message that is retyped.

`ask.md` is written once, by the node that raised it, and is never rewritten. `effort.md` carries the attempts and the closures. `notes.tsv` gains one row from each layer that touches it: the node, its opinion, the time.

Raising it is a move into the next layer's inbox and one appended row, so no layer pays to restate the question and nothing is lost in the restating.

The root renders the inbox for the person and adds nothing to it.

## Land before reporting

The write comes first. A report is sent only after the fact it carries is in its own document, so a kill between them loses nothing.

A decision lands in the document that owns it. A message that only routes information lands nowhere.

## Intent before the act

Before a step that takes minutes, the node's document holds what is done, what is starting, what would prove it, and where the next step begins. Then any kill names its own resume point.

## The safe point

Returning control to a person is the point at which nothing would be lost if the session died. Its test is the next session: what would it not know? Every fact, decision and open question is in a document, every running job is named with its log and next step, and the tree is committed.

## Durability

A fact belongs at the highest place it can reach: a temporary path, then an ignored buffer, then a local commit, then a pushed commit, and for bytes git cannot hold, a declared home whose hash verifies.

## No trash

Every path is committed, declared, or ignored with a stated owner. An unexplained modification is a defect, because it hides real work and makes the tree unreadable to the next session. It is never deleted to make the tree look clean.

## Recovery

Recovery reads the document's current state and the named jobs, and re-checks anything the change invalidated. A record older than the revision is not evidence.
