# Operations

## Nothing long inside a turn

A turn is a channel a person can interrupt, so nothing that takes minutes runs inside it. It runs detached, behind a named log and an identifier, and its completion comes back as a message.

A timeout is not a guard against being stuck. It kills the process it started and not the processes that process started, and it does not survive a process that ignores it.

No node blocks waiting for a child. A child returns immediately and its result arrives when it arrives.

Waiting is never written as a sleep. A command that begins with `sleep` is the one case the promotion floor does not rescue, and it is the most common way a node blocks itself.

The client's own budget belongs here too: an unbounded retry count and a disabled idle timeout turn one stalled connection into a permanent block, whatever the command was doing.

## Resources

A contract declares what its package will consume: cores, memory, accelerators, and the wall-clock it expects. A node that does not know says so, starts, and asks up the moment it learns.

Allocation is hereditary. The root grants a budget to a container, and the container grants from that budget to its children, so the common case costs no message. Only an exhausted grant travels up.

A child that has written nothing for longer than its declared wall-clock is presumed stuck. That is noticed when the node next reads its own roadmap, never by watching it.

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
