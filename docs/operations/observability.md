# Observability

[← Documentation index](../README.md)

What operators can see today in RelayRuntime embedded deployments—and what is **not** yet available.

---

## Observability goals

| Goal | Mechanism today |
|------|-----------------|
| Know if a run is active | Campaign state + Executions tab |
| Know per-recipient outcome | `whatsapp.message.log` |
| Know run ownership | `whatsapp.bulk.execution` lease + heartbeat |
| Diagnose failures | Odoo logs + optional file log |
| Audit lineage | Parent/child campaign + execution links |

---

## Logging

| Logger / channel | Content |
|------------------|---------|
| `campaign_logger` | Bulk lifecycle, lease, reconcile |
| `api_logger` | Provider HTTP (sanitize tokens in reports) |
| Optional `whatsapp.log` | File path from settings |

**Configuration:** standard Odoo `log_level`; no separate RelayRuntime log agent.

### Useful log patterns

- `begin_campaign_execution`
- `heartbeat`
- `reconcile_stale`
- `finish` / terminal stats
- Provider errors with status codes

---

## Execution visibility (UI)

| Surface | Data |
|---------|------|
| Campaign form | Aggregated counters, progress %, state |
| Executions tab | Per-attempt state, UUID, timestamps |
| Message logs | Per partner status, error text |
| Monitor views | Kanban/list by campaign state |

Progress is **projected** from execution—may lag seconds during large batches.

---

## Telemetry gaps (honest)

| Not implemented | Impact |
|-----------------|--------|
| Prometheus / OpenTelemetry | No metrics scrape |
| Distributed trace IDs | Cannot correlate across workers |
| Centralized log shipping | Use your Odoo/platform tooling |
| Real-time webhook to SIEM | N/A |
| Provider delivery receipts unified | Provider-dependent |

Future runtime service may expose metrics API—see [future-runtime-service.md](../deployment/future-runtime-service.md).

---

## Failure diagnostics workflow

1. Record `campaign_id`, `execution_id`, module version, UTC window.
2. Export or screenshot message logs for affected partners.
3. Pull Odoo server log slice (no tokens).
4. If duplicate suspected, compare idempotency keys and retry tree.
5. Staging: reproduce with Mock Provider.

See [SUPPORT.md](../../SUPPORT.md).

---

## Heartbeat as liveness signal

| Field | Use |
|-------|-----|
| `heartbeat_at` | Last loop progress |
| `lease_expires_at` | Expected lease validity |
| `last_recipient_index` | Debug only—not resume authority |

Stale heartbeat triggers [reconciliation](../recovery/stale-execution-reconciliation.md).

---

## Related

- [operational-guidelines.md](operational-guidelines.md)
- [failure-scenarios.md](failure-scenarios.md)
- [RUNBOOK.md](RUNBOOK.md)
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
