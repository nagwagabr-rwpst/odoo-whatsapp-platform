# Support

## Standard / Core (this repository)

**WhatsApp Simple** open-source module support covers:

| In scope | Out of scope |
|----------|--------------|
| Defects in shipped module code (see [CHANGELOG](CHANGELOG.md)) | Custom Odoo development not in this repo |
| Documentation in `/docs` | Third-party provider outages or account issues |
| Installation and upgrade on supported Odoo 19 Community | Hosted Odoo administration unless contracted separately |
| Guidance on Mock Provider testing | Guaranteed message delivery or exactly-once semantics |
| Integrity behavior as documented in [Known Limitations](docs/architecture/KNOWN_LIMITATIONS.md) | Unlimited bulk scale without timeout planning |

### How to get help

1. Read [docs/README.md](docs/README.md) and [Troubleshooting](docs/operations/TROUBLESHOOTING.md).
2. Search [GitHub Issues](https://github.com/YOUR_ORG/whatsapp_simple/issues) (update URL before release).
3. Open an issue using the appropriate template (bug, deployment, runtime, duplicate send).
4. For security issues, see [SECURITY.md](SECURITY.md) — **no public issues**.

### Unsupported customizations

The following are **not** covered under Standard/Core support unless you maintain them:

- Forked changes to `WhatsAppBulkSender`, execution model, or idempotency keys
- Custom providers not merged upstream
- Direct `cr.commit()` in bulk paths
- Bypassing lease or reconciliation logic
- Heavy XML/JS overrides without upgrade path

### Deployment responsibility

| You operate | You are responsible for |
|-------------|-------------------------|
| Odoo server / Odoo.sh / Docker | Workers, timeouts, HTTPS, backups |
| PostgreSQL | Capacity, backups, restore drills |
| WhatsApp provider account | Billing, rate limits, compliance, opt-in |
| Campaign content | Consent, spam regulations, message legality |

The module provides **runtime coordination** (execution attempts, leases, idempotency within a campaign). It does not replace operational monitoring or provider SLAs.

## Enterprise / runtime consulting (future direction)

**Not included** in the open-source module today:

- Background job queue and worker pool for bulk sending
- Multi-node distributed execution locks
- Event-sourced delivery ledger
- 24/7 managed operations
- Custom SLA on duplicate-send rates

Organizations needing these capabilities should plan a **separate engagement** or fork with explicit operational ownership. Feature requests may be tagged **Enterprise runtime** in GitHub — see [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md).

## Version and upgrade policy

- Track [VERSIONING](docs/releases/VERSIONING.md).
- Production should run a tagged release, not an unlabeled `develop` commit.
- Before upgrading, read `CHANGELOG.md` and run `-u whatsapp_simple` on staging.

## Community

- Contributions: [CONTRIBUTING](docs/development/CONTRIBUTING.md)
- Pull requests: follow [Runtime Safety Rules](docs/development/RUNTIME_SAFETY_RULES.md)
