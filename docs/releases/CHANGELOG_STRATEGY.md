# Changelog Strategy

[← Documentation index](../README.md)

## Location

Primary changelog: [`CHANGELOG.md`](../../CHANGELOG.md) at module root.

## Format

Follow [Keep a Changelog](https://keepachangelog.com/) principles adapted for Odoo modules:

```markdown
## [19.0.5.5.0] - YYYY-MM-DD

### Added
### Changed
### Fixed
### Security
```

## Version coupling

Module version in `__manifest__.py` **must** match the changelog entry header for releases.

Odoo 19 requires versions in the **`19.0.x`** series (not `19.1.x`).

## What to document

| Include | Exclude |
|---------|---------|
| User-visible behavior | Internal refactors with no runtime effect |
| Schema migrations / new models | Comment-only changes |
| Breaking ACL or config changes | Typo fixes in dev docs |
| Known limitation changes | Speculative future features |

## Integrity and stabilization releases

Group related fixes under clear headings:

- **Transactional integrity** — commits, idempotency, execution attempts
- **Provider** — adapter changes
- **UI** — wizards, monitor

Cross-link to `/docs` when behavior is non-obvious.

## Unreleased section

Optional `## [Unreleased]` at top during active development; move to versioned section on tag.

## Further reading

- [Versioning](VERSIONING.md)
- [Release Process](RELEASE_PROCESS.md)
