# Contributing

[← Documentation index](../README.md)

## Scope

Contributions should preserve **runtime safety** properties documented in [Runtime Safety Rules](RUNTIME_SAFETY_RULES.md). This module handles irreversible external side effects (WhatsApp sends).

## Before you start

1. Read [System Overview](../architecture/SYSTEM_OVERVIEW.md) and [Known Limitations](../architecture/KNOWN_LIMITATIONS.md).
2. Use **Mock Provider** for development and tests.
3. Do not document planned features as implemented.

## Development setup

See [Local Setup](../deployment/LOCAL_SETUP.md).

## Code style

- Match existing Odoo patterns in `models/`, `services/`, `wizard/`
- Keep provider-specific HTTP in `services/providers/`
- Use `campaign_logger` / `api_logger` instead of ad-hoc `print`
- Translations: `_()` for user-facing strings

## Pull request expectations

| Requirement | Detail |
|-------------|--------|
| Changelog | Entry in `CHANGELOG.md` |
| Version | Bump `__manifest__.py` if releasing |
| Tests | Add or extend `tests/` for behavior changes |
| Docs | Update `/docs` when runtime behavior changes |
| Safety review | No `cr.commit()` in bulk loops without explicit design doc |

## Areas requiring extra review

| Area | Risk |
|------|------|
| `whatsapp_bulk_service.py` | Duplicate send, transaction boundaries |
| `whatsapp_bulk_execution.py` | Lease / concurrency |
| `whatsapp_message_log.create_log` | Idempotency |
| Provider adapters | External I/O |
| Security / ACL | Token exposure |

## What we are not accepting without design discussion

- Mid-loop commits restoring partial durability
- New background queue without full docs and ops runbook
- Marketing claims in docs that exceed implementation

## Further reading

- [Codebase Structure](CODEBASE_STRUCTURE.md)
- [ORM Guidelines](ORM_GUIDELINES.md)
