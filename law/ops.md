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

Where a site's price follows the clock, metered spend waits for the cheap window while the work is throughput-bound, and ignores the window while the work is waiting-bound, because an idle rented device costs more than the discount it waited for.

Waiting for the cheap window is worth it only while the wait is shorter than the work it discounts, so a two-hour job does not wait six hours to halve its price.

An allowance already bought expires whatever happens to it, so it is spent at any hour and on work whose failure is cheap. Waiting to save money on an allowance already paid saves nothing.

A reservation is written before the work starts and released when it ends, so the holdings at the node that holds the budget are the truth about who has the device. A probe of the device confirms a holding and never decides one, because a reservation is not a process.

Work whose continuation is still in question may not hold an exclusive resource. It runs on idle compute, or it settles the question first, because holding what another package cannot share is a commitment the work has not yet earned.

Displacing a holder is allowed when the waiter's loss is larger than the holder's loss at being stopped. A package is stoppable at its last write unless the contract says otherwise, so the loss of stopping it is the work done since that write, and only a package that cannot be stopped says so.

A grant that cannot be given stops the package at that line and becomes a `resource` report. Allocation is hereditary: the root grants a container a budget, the container grants from it, and only an exhausted grant travels up. A node that does not know what it will spend says so and asks up the moment it learns.

A child that has written nothing for longer than its declared time is presumed stuck. That is noticed when the node next reads its own roadmap, never by watching it.

## Messages

A message is written where the node it is about lives, so nothing about a node is ever filed above it. An answer is written back to the same place with a different target, which is why an answer reaches every layer that added a row without a special route.

## One writer

Two nodes writing one area produce a diff nobody can review and a state neither of them owns. One live writer per area.

The parent allocates the area when it dispatches, because it is the only node that starts a writer there and it already knows what it started. There is no lock to take and no table to keep: a second writer cannot appear without the parent creating it.

## Land before reporting

The write comes first. A report is sent only after the fact it carries is in its own document, so a kill between them loses nothing.

## Intent before the act

Before a step that takes minutes, the node's document holds what is done, what is starting, what would prove it, and where the next step begins. Then any kill names its own resume point.

## The safe point

Returning control to a person is the point at which nothing would be lost if the session died. Its test is the next session: what would it not know? Every fact, decision and open question is in a document, every running job is named with its log and next step, and the tree is committed.

## Durability

A fact belongs at the highest place it can reach: a temporary path, an ignored buffer, a local commit, a pushed commit, and for bytes git cannot hold, a declared home whose hash verifies.

## No trash

Every path is committed, declared, or ignored with a stated owner. An unexplained modification is a defect, because it hides real work and makes the tree unreadable to the next session. It is never deleted to make the tree look clean.

