# Contributing

## Development workflow

1. Create a feature branch from `main`.
2. Keep changes focused and aligned with the roadmap.
3. Use conventional commit messages.
4. Add or update tests when changing behavior.
5. Update documentation when adding features or breaking changes.
6. Open a pull request with a clear summary and release context.

## Commit message convention

The project uses Conventional Commits.

Examples:

- `feat(auth): add seed and token retrieval client`
- `fix(xml): correct namespace on DTE serialization`
- `refactor(client): unify sync and async transport contracts`
- `docs(mkdocs): configure bilingual English/Spanish docs`
- `chore(deps): update cryptography and httpx`

## Versioning

The project follows semantic versioning with tags in the format `v{major}.{minor}.{patch}`.

Examples:

- `v0.1.0`
- `v0.2.0`
- `v1.0.0`

## Pull request checks

Before merging, ensure:

- tests pass
- docs are updated when needed
- new public APIs are documented
- security-sensitive code is reviewed carefully
