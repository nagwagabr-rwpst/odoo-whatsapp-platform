# Support

RelayRuntime Standard/Core support covers **documented runtime behavior** on Odoo 19 Community. It does not include guaranteed delivery SLAs, managed operations, or custom ERP development unless separately contracted.

---

## What is supported

| In scope | Out of scope |
|----------|--------------|
| Defects in shipped `relayruntime` code per [CHANGELOG](CHANGELOG.md) | Third-party provider outages |
| Documentation in `/docs` | Exactly-once / zero-duplicate messaging guarantees |
| Install/upgrade with [MIGRATION](MIGRATION.md) guidance | Unlimited bulk scale without timeout planning |
| Integrity behavior per [Known Limitations](docs/architecture/KNOWN_LIMITATIONS.md) | Distributed HA runtime (not implemented) |
| Mock Provider reproduction guidance | Custom forks that bypass lease/idempotency |

---

## How to report issues

1. Read [docs/README.md](docs/README.md) and [Troubleshooting](docs/operations/TROUBLESHOOTING.md).
2. Search existing GitHub issues.
3. Open an issue using the correct template:

| Template | Use when |
|----------|----------|
| Bug Report | Incorrect behavior vs documentation |
| Runtime Corruption | Stuck campaigns, stale execution, counter drift |
| Duplicate Send | Same recipient received multiple messages |
| Deployment Issue | Install, upgrade, timeout, workers |

4. Security: [SECURITY.md](SECURITY.md) only—no public issues.

---

## Operational bug reports

For runtime incidents, include **execution identity**:

| Field | Where to find |
|-------|----------------|
| Campaign ID | Campaign form |
| Execution attempt ID | Executions tab |
| `execution_uuid` | Execution record |
| Module version | Apps → RelayRuntime |
| Provider type | WhatsApp Settings |
| Approximate UTC time | Incident window |

State whether concurrent users or retries were involved.

---

## Reproduction expectations

| Requirement | Detail |
|-------------|--------|
| Environment | Odoo version, module version, `workers`, `limit_time_real` |
| Provider | Prefer **Mock Provider** for public reports |
| Steps | Minimal path to reproduce |
| Expected vs actual | Reference doc section if possible |
| Logs | Sanitized Odoo log excerpt—**no tokens** |

Intermittent duplicate sends require provider message IDs and log IDs if available.

---

## Logs and telemetry requirements

| Source | Contents |
|--------|----------|
| Odoo server log | `campaign_logger`, `api_logger` lines for incident window |
| Message logs | `whatsapp.message.log` for affected campaign |
| Execution row | `state`, `heartbeat_at`, `lease_expires_at` |
| Optional file log | `whatsapp.log` if enabled in settings |

**Not available today:** centralized metrics, trace IDs, or automated incident bundles.

---

## Recovery-state debugging

When reporting stuck or reconciled executions, capture:

```
Campaign state:
Execution state:
heartbeat_at:
lease_expires_at:
last_activity_at (campaign):
```

Indicate whether `_reconcile_stale_executions` ran (e.g. new bulk send started).

See [stale execution reconciliation](docs/recovery/stale-execution-reconciliation.md).

---

## Unsupported customizations

Support does not cover forks that:

- Reintroduce mid-loop `cr.commit()`
- Bypass `begin_campaign_execution` or lease checks
- Change idempotency key format without migration
- Disable reconciliation hooks

---

## Deployment responsibility

| You operate | You own |
|-------------|---------|
| Odoo / Odoo.sh / containers | Uptime, workers, timeouts |
| PostgreSQL | Backups, capacity |
| WhatsApp provider account | Compliance, billing, rate limits |
| Message content | Consent and applicable law |

---

## Enterprise runtime (future)

Background workers, distributed leases, event-sourced delivery ledger, and managed SLAs are **not** included in this repository today. Track [runtime vision](docs/architecture/runtime-vision.md) for direction.

---

## Community contribution

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [VERSIONING](docs/releases/VERSIONING.md)
