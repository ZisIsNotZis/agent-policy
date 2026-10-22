# Policy product

What this repository is for, held to the standard the policy itself states.

## Commitment

One written law for agents working in a repository, published so its author and a stranger read the same text.

- **Audience:** others - a stranger adopting it, and a reviewer judging what this author's agents are held to.
- **Artefact:** a document set, with the checker that renders one agent view per role and refuses a view that drifted.
- **Openness:** open-read, with contributions as issues and pull requests.
- **Done criterion:** `python3 tools/policy.py --check` passes on the default branch; every generated view matches its source; a reader reaches the current law from any copy of it in one hop.

## Quality dimensions, each with the observation that would satisfy it

- **It runs.** A fresh clone runs `python3 tools/policy.py --check` and prints the pass line, with PyYAML as the only dependency.
- **It explains.** The README says in one screen what the law is for and who it is not for, before any detail.
- **It shows.** The render is the whole law, so the artefact is its own demonstration; the check's refusals are listed with what each one catches.
- **It ships.** The repository is the shipping form: a pinned commit is a version, and the render can be copied without the tooling.
- **It is legible.** A licence, a goal, non-goals and a public place to report a defect.

## Non-goals

- A product, a service, a package or an installation procedure beyond a pinned checkout.
- Universal advice. A rule here is derived from this author's failures, so a rule that does not fit a scope is refused by that scope rather than softened here.
- Personal material: the owner's memory file and any scope's refinements stay with that scope.
- Enforcement of anything that cannot be checked at the layer where it lands. Such a rule carries a guidance-only mark instead of pretending.
