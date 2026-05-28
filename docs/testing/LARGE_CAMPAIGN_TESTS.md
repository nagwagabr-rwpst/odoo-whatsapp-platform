# Large Campaign Tests

[← Documentation index](../README.md) · [Testing Strategy](TESTING_STRATEGY.md)

Stress and scale tests for **synchronous** bulk sending. These validate operational limits, not unlimited scalability.

## Preconditions

| Setting | Value |
|---------|-------|
| Provider | `mock_provider` |
| `simulated_latency_ms` | Tune to realistic Green API latency |
| `daily_send_limit` | Above test size |
| `limit_time_real` | Document actual server value |

## Scenarios

### L1 — 100 recipients, text only

| Metric | Record |
|--------|--------|
| Wall time | |
| HTTP timeout occurred? | |
| Final campaign state | |
| Execution state | |
| Logs created | |

**Expected:** completes if within `limit_time_real`; execution heartbeats every 5 / 45s.

### L2 — 100 recipients, 2 attachments each

| Risk | Attachment decode memory + provider segments |
|------|---------------------------------------------|

Watch `limit_memory_soft` in Odoo logs.

### L3 — 500+ recipients (optional)

**Status:** likely to fail on default `limit_time_real=120` — document failure mode (`failed` / timeout / partial).

This is **expected** under current architecture — not a defect report unless marketing unlimited scale.

### L4 — Product images per recipient

Enable **Use Product Images** with catalog + N products.

Count provider calls ≈ recipients × (1 + products + free attachments).

## Observations to capture

| Signal | Tool |
|--------|------|
| Progress UI | Campaign Monitor kanban |
| DB growth | `whatsapp_message_log` row count |
| Lock duration | PostgreSQL `pg_stat_activity` |
| Worker CPU | OS monitor |

## Pass / fail criteria (pragmatic)

| Result | Classification |
|--------|----------------|
| Completes within timeout, consistent logs | Pass for defined size |
| `stopped` at daily limit with correct progress | Pass (boundary) |
| Timeout with reconciled/stuck state | Operational limit documented |
| OOM or worker crash | Fail — reduce batch size |

## Planned / future

When background queue exists, repeat L3/L4 against async job model — **not applicable today**.

## Further reading

- [Production Checklist](../deployment/PRODUCTION_CHECKLIST.md)
- [Known Limitations](../architecture/KNOWN_LIMITATIONS.md)
