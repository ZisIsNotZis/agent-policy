---
name: repository-hygiene
description: Use when creating or reorganizing a code repository, reviewing project structure and naming, cleaning generated artifacts, improving discoverability, or preparing a repository for handoff.
---

# Repository Hygiene

## Purpose

Keep the repository understandable, reproducible, and free of avoidable clutter. Apply conventions appropriate to the project's language, tooling, and scale.

## Structure and naming

- Organize by meaningful responsibility or domain, not arbitrary file counts.
- Use names that make a file or directory's purpose apparent.
- Avoid duplicate sources, ambiguous names, unexplained abbreviations, and unnecessary nesting.
- Add an index or directory README only when the structure and names do not adequately explain the contents.
- Keep generated output separate from maintained source where practical.

## Source of truth

Each important behavior, configuration, or fact should have an identifiable authoritative location. Avoid maintaining parallel copies that can drift. Link to canonical material instead of duplicating it.

## Generated and temporary files

Review `.gitignore` and repository contents for editor backups, OS metadata, caches, build output, local environments, temporary files, credentials, and other generated artifacts. Commit generated artifacts only when they are intentionally part of the deliverable and their provenance/rebuild path is clear.

Do not remove files merely because they look generated: first establish whether they are required for distribution, reproducibility, or the project's workflow.

## Reproducibility and handoff

Check that a new contributor or agent can identify the entry points, supported toolchain, setup steps, tests, build commands, and important project docs. Verify links and commands that are part of the handoff when practical.

## Deliverable

A repository whose structure communicates its organization, whose authoritative sources are clear, and whose tracked contents are intentional and reproducible.
