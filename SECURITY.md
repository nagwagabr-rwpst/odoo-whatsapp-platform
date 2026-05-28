# Security Policy

## Supported versions

| Module version | Supported |
|----------------|-----------|
| 19.0.5.5.x (current) | Yes |
| 19.0.5.4.x | Best effort |
| &lt; 19.0.5.4 | No |

Security fixes are delivered via patch releases on the `19.0.x` Odoo module series. Upgrade with:

```bash
odoo-bin -u whatsapp_simple -d YOUR_DATABASE
```

## Reporting a vulnerability

**Please do not** open public GitHub issues for security vulnerabilities.

1. Email the maintainers with a private report (info.rwpst@gmail.com).

2. Include: Odoo version, module version, deployment type, reproduction steps, impact assessment.
3. Allow reasonable time for triage and patch before disclosure.

We will acknowledge receipt and communicate fix timelines when applicable.

## Scope

**In scope**

- Authentication and authorization flaws in this module (ACL, record rules, wizard access)
- Sensitive data exposure via module UI or logs (tokens, secrets)
- Integrity issues that allow unauthorized message send or campaign manipulation

**Out of scope**

- Compromised Odoo administrator accounts
- Misconfigured `whatsapp.config` credentials left in database backups
- Vulnerabilities in third-party WhatsApp providers (Green API, Meta, etc.)
- Generic Odoo core issues (report to Odoo security separately)

## Operational security boundaries

### Unsupported deployment modes

The following are **unsupported** for security or integrity guarantees:

| Mode | Risk |
|------|------|
| Exposing Odoo database manager to the internet without hardening | Full system compromise |
| Sharing **WhatsApp Manager** credentials with untrusted users | Token theft, arbitrary sends |
| Running production with `workers=0` under high concurrency | Race and timeout behavior |
| Disabling Odoo HTTPS / `proxy_mode` misconfiguration | Session hijack |
| Storing API tokens in version control | Credential leak |

### Provider consistency (not a crypto guarantee)

This module **does not** provide exactly-once delivery to WhatsApp recipients.

| Fact | Implication |
|------|-------------|
| Provider APIs are external to PostgreSQL | No atomic commit with message delivery |
| HTTP rollback may occur after provider success | Duplicate send possible on retry |
| Idempotency is campaign-scoped in Odoo | Retry campaigns may resend the same partner |
| No provider outbound idempotency tokens | Network/provider retries are outside module control |

See [Known Limitations](docs/architecture/KNOWN_LIMITATIONS.md).

### Data handling

- API tokens are stored in `whatsapp.config` database fields (Manager-only write).
- Optional dedicated log file may contain message metadata — protect filesystem permissions.
- Issue reports must **not** include live tokens; use Mock Provider for reproduction when possible.

## Secure configuration recommendations

- Assign **WhatsApp Manager** only to trusted administrators.
- Use **Mock Provider** on staging; rotate Green API tokens if exposed.
- Restrict database backups and filestore access.
- Set `limit_time_real` and campaign sizes appropriate to your SLA (see [Production Checklist](docs/deployment/PRODUCTION_CHECKLIST.md)).

## Security-related documentation

- [Transaction Model](docs/architecture/TRANSACTION_MODEL.md)
- [Runtime Safety Rules](docs/development/RUNTIME_SAFETY_RULES.md)
- [Runbook](docs/operations/RUNBOOK.md)
