# Release Process

[← Documentation index](../README.md) · [Versioning](VERSIONING.md)

## Overview

Releases are **module-level** (Odoo addon), not separate from the Odoo server distribution in this repository layout.

## Pre-release checklist

- [ ] Bump `version` in `__manifest__.py`
- [ ] Add [`CHANGELOG.md`](../../CHANGELOG.md) entry
- [ ] Run tests: `--test-tags=relayruntime`
- [ ] Upgrade test database: `-u relayruntime`
- [ ] Verify migration hooks if schema changed (`hooks.py`)
- [ ] Update `/docs` if runtime behavior changed
- [ ] Scan for accidental `cr.commit()` in bulk paths ([Runtime Safety Rules](../development/RUNTIME_SAFETY_RULES.md))

## Branching (repository practice)

This module may live in its own git repo (see `.git` under `relayruntime`) or monorepo root — follow your team's convention.

Suggested tags:

```
release/v19.0.5.5.0-stable
```

## Staging deployment

1. Deploy to staging Odoo / Odoo.sh staging branch.
2. `-u relayruntime`
3. Execute [Runtime Failure Tests](../testing/RUNTIME_FAILURE_TESTS.md) subset.
4. Sign-off from operations on [Production Checklist](../deployment/PRODUCTION_CHECKLIST.md).

## Production deployment

1. Maintenance window for `-u` if model changes.
2. Upgrade module.
3. Reconcile stale executions if upgrading from pre-execution versions ([Runbook](../operations/RUNBOOK.md)).
4. Smoke test: Mock or single-recipient Green API send.

## Rollback

| Scenario | Action |
|----------|--------|
| Code rollback | Deploy previous git tag; restart Odoo |
| Schema already migrated | Odoo does not auto-downgrade — restore DB backup or forward-fix |
| Data issues | Use runbook; do not delete execution rows without analysis |

**There is no built-in module downgrade script.**

## Communication

Include in release notes:

- Implementation status of major features (not roadmap as done)
- Known limitations link: `docs/architecture/KNOWN_LIMITATIONS.md`

## Further reading

- [Changelog Strategy](CHANGELOG_STRATEGY.md)
