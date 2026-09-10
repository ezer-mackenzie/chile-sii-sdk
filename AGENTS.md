# AGENTS

## Project operating rules

This repository follows a structured, open-source SDK workflow. All contributors and AI agents must respect these rules:

1. Follow the roadmap in `temp/ROADMAP.md`.
2. Use semantic versioning tags in the form `v{major}.{minor}.{patch}`.
3. Use Conventional Commits in English:
   - feat
   - fix
   - chore
   - refactor
   - docs
   - test
   - ci
   - build
4. Keep all product-facing documentation in English first.
5. Add Spanish documentation support where relevant using MkDocs/i18n patterns.
6. Favor maintainable architecture: clear modules, typed contracts, and explicit errors.
7. Maintain sync and async compatibility strategy in design decisions.
8. Do not skip tests for public behavior changes.

## Working conventions

- Prefer small, reviewable commits.
- Keep the public API stable within the same minor version.
- Document breaking changes in `CHANGELOG.md`.
- Read the roadmap before implementing new features.
- Keep examples practical and aligned with real SII workflows.

## Ref implementation guidance

When working on this repository, treat the repo as a production-facing SDK and be conservative with protocol details. The project should be built incrementally, with v0.1.0 establishing the foundation:

- package metadata
- version contract
- environment configuration
- synchronous client interface
- errors and validation primitives
- documentation scaffolding

The project must be guided by the roadmap and by the AGENTS instructions, not by ad hoc shortcuts.
