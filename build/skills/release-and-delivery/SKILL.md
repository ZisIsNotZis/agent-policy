---
name: release-and-delivery
description: Use when preparing a user-facing milestone, packaging or publishing a product, updating README or release notes, or checking whether a deliverable is accessible and usable by its intended audience.
---

# Release and Delivery

## Purpose

Make the delivered result usable, understandable, and honestly represented. Apply only the parts relevant to the project's distribution model.

## Confirm release readiness

Check that:
- the delivered result matches the current Goal and agreed acceptance/evaluation criteria;
- required integration and verification are complete;
- known material defects and limitations are fixed or clearly disclosed;
- the artifact, service, or result can be accessed by its intended users;
- setup, usage, dependencies, and support expectations are understandable where relevant;
- the release does not include secrets, temporary files, unintended data, or unlicensed material;
- rollback, recovery, or a safe follow-up path exists when the risk warrants it.

## README and user-facing documentation

A README should help its intended audience quickly understand what the project is, who it serves, why it matters, what it can do, how to access or use it, and where to find deeper documentation. Include installation, configuration, examples, limitations, and contribution/development instructions when relevant.

Keep claims aligned with the actual implementation and tested state. Do not market planned features as available. Prefer a clear entry point and links to detailed docs over duplicating the whole documentation set.

## Distribution and reachability

For distributed software or services, verify that critical dependencies, endpoints, package registries, download channels, and hosting are reachable by the intended audience and regions. Identify regional restrictions and provide a supported alternative where feasible. Do not assume global reachability from a successful local test.

## Localization and accessibility

Localize when the target audience and product requirements call for it. Use a consistent language strategy and review meaning, terminology, layout, and usability—not only literal translation. Check accessibility requirements relevant to the audience and medium.

## Release communication

Communicate what is new, what is usable now, material changes, known limitations, and any action required from users. Keep internal process detail out unless it helps the recipient.

## Deliverable

A usable, verified, clearly documented release or milestone, with honest disclosure of remaining risks and limitations.
