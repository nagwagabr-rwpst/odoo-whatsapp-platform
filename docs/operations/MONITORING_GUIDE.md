# Monitoring Guide

[← Documentation index](../README.md)

## What to monitor (implemented)

| Signal | Source | Notes |
|--------|--------|-------|
| Campaign state | `whatsapp.bulk.campaign` | `running` should be transient |
| Execution heartbeat | `whatsapp.bulk.execution.heartbeat_at` | Stale > 30 min → reconcile on next op |
| Delivery outcomes | `whatsapp.message.log.delivery_state` | Authoritative per recipient |
| Provider errors | Log `failure_reason`, `api_response_body` | |
| Server log | Python loggers | `campaign_logger`, `api_logger`, `attachment_logger` |
| Optional file | `whatsapp.log` | If enabled in Settings |

**Not implemented:** Prometheus metrics, webhook health endpoints, APM instrumentation.

## UI monitoring

### Campaign Monitor

**Menu:** WhatsApp → Campaign Monitor

- Kanban cards: sent / failed / skipped, progress %
- Auto-reload: **5 seconds** (`campaign_monitor_kanban.js`)
- **Not** real-time push

### Campaign form

- **Executions** tab: lease, heartbeat, executor, terminal state
- **Message Logs** tab: per-recipient detail

### Delivery Dashboard

Snapshot on open — does not auto-refresh.

## Loggers

Defined in `services/logger.py`:

| Logger | Typical content |
|--------|-----------------|
| `campaign_logger` | Campaign/execution lifecycle, skips |
| `api_logger` | Provider request/response summary |
| `attachment_logger` | Multi-attachment sequencing |

Enable DEBUG for verbose delay/API payload logs.

## Alerts (recommended — external)

Configure outside the module:

| Alert | Condition |
|-------|-----------|
| Stuck running | Campaign `running` > N minutes (query DB) |
| High failure rate | `failed_count / total_count` threshold on recent campaigns |
| Daily limit approached | Count sent logs vs limit |
| Odoo worker restarts | OS / platform during bulk hours |

**Planned / future:** built-in scheduled stale check — not shipped.

## Sample SQL monitors (read-only)

**Running campaigns older than 30 minutes:**

```sql
SELECT c.id, c.name, c.last_activity_at, e.id AS execution_id, e.heartbeat_at
FROM whatsapp_bulk_campaign c
LEFT JOIN whatsapp_bulk_execution e ON e.id = c.active_execution_id
WHERE c.state = 'running'
  AND c.last_activity_at < NOW() - INTERVAL '30 minutes';
```

**Today's send volume (legacy status field):**

```sql
SELECT COUNT(*) FROM whatsapp_message_log
WHERE status = 'sent' AND sent_date::date = CURRENT_DATE;
```

## Health checks

| Check | Method |
|-------|--------|
| Provider config | Settings → Test Connection |
| Module version | Apps → WhatsApp Simple → version `19.0.5.5.0` |
| Registry | `scripts/run_registry_check.py` (dev) |

## Further reading

- [Runbook](RUNBOOK.md)
- [Production Checklist](../deployment/PRODUCTION_CHECKLIST.md)
