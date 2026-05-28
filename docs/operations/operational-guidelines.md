# Operational Guidelines

[← Documentation index](../README.md)

Safe practices for running RelayRuntime in production Odoo environments.

---

## Deployment baseline

| Setting | Recommendation |
|---------|----------------|
| Odoo workers | `workers >= 1` for production; understand lease behavior if `0` |
| `limit_time_real` | Set above worst-case bulk duration |
| Database backups | Before module upgrade or mass retry |
| Staging | Mock Provider mandatory for CI-like validation |
| Module path | `addons_path` includes `.../apps/odoo` only |

---

## Campaign operations

| Practice | Rationale |
|----------|-----------|
| Size batches to timeout budget | Single HTTP transaction |
| Avoid parallel bulk on same campaign | Lease rejects; race edge cases |
| Wait for terminal state before retry | Understand partial logs |
| Use retry wizard for failed subset | Preserves lineage + fingerprint |
| Document provider incidents | DB may not reflect provider truth |

---

## Credential and access

- Limit **WhatsApp Manager** to trusted admins.
- Rotate tokens after staff departure or leak suspicion.
- Do not share production DB dumps publicly.
- Redact tokens from support tickets.

---

## Upgrade and migration

- Follow [MIGRATION.md](../../MIGRATION.md) for `whatsapp_simple` → `relayruntime`.
- Never install both modules on one database.
- Run `-u relayruntime` on staging first.
- Verify XML ID customizations after upgrade.

---

## Recovery discipline

| Scenario | Guideline |
|----------|-----------|
| Stuck `running` | Check execution heartbeat; trigger reconcile via new begin or runbook |
| Partial batch | Read logs before retry |
| Suspected duplicates | Stop retries; compare provider IDs |
| Wrong content sent | No automated undo—business process |

---

## Performance

| Factor | Note |
|--------|------|
| Inter-recipient delay | Safety throttle—extends wall time |
| Attachments | Multiply provider calls |
| Daily limits | Mid-send stop possible |
| Long polling UI | Monitor may refresh; not execution authority |

---

## What not to do

- Add `cr.commit()` inside bulk loop (breaks recovery model).
- Bypass lease via custom scripts without execution records.
- Assume `progress_percent == 100` means all recipients sent.
- Enable production bulk on untested provider credentials.

---

## Incident severity (suggested)

| Level | Example |
|-------|---------|
| S1 | Mass duplicate sends to customers |
| S2 | Stuck campaigns blocking operations |
| S3 | UI counter drift with correct logs |
| S4 | Documentation / cosmetic |

---

## Related

- [failure-scenarios.md](failure-scenarios.md)
- [observability.md](observability.md)
- [RUNBOOK.md](RUNBOOK.md)
