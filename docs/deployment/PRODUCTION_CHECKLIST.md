# Production Checklist

[← Documentation index](../README.md)

Use before enabling real WhatsApp traffic in production.

## Workers and process model

| Item | Dev (repo sample) | Production guidance |
|------|-------------------|---------------------|
| `workers` | `0` in sample `odoo.conf` | **Use `workers > 0`** for prefork |
| HTTP blocking | Bulk holds worker | Size campaigns to fit timeouts |
| Longpolling worker | Separate | Unaffected by bulk |

**Status:** multi-worker lease behavior is **partially implemented** — test concurrent operations on your target topology.

## Cron guidance

| Item | Status |
|------|--------|
| Module-owned bulk cron | **Not implemented** |
| Stale reconciliation | Runs on **next** user-triggered send/retry |
| Recommended ops cron | **Optional custom** scheduled action to call `_reconcile_stale_executions` — **not shipped** |

**Operational note:** without periodic reconciliation, stale `running` campaigns persist until someone triggers a send or manual intervention.

## Timeout considerations

| Setting | Risk |
|---------|------|
| `limit_time_real` too low | Bulk aborted mid-run; partial logs |
| Provider HTTP timeout | Adds to wall time per segment |
| `time.sleep` delays | Linear increase with recipients |

**Rule of thumb:** estimate `(recipients × (delay + segments × provider_latency))` and compare to `limit_time_real`.

## Scaling caveats

| Approach | Supported today |
|----------|-----------------|
| Larger single bulk | Partial — timeout/lock risk |
| Parallel bulks by users | Yes — separate campaigns |
| Same campaign parallel | Blocked by lease (**implemented**) |
| Horizontal async workers | **Not implemented** |

## Memory considerations

| Factor | Effect |
|--------|--------|
| Attachment byte cache in sender | Per-run dict keyed by attachment id |
| Partner batch read | Loads all recipients upfront |
| ORM identity map | Grows with logs created in one transaction |

Operational policy: cap recipients per campaign; avoid multi-megabyte attachments when possible.

## Security checklist

- [ ] Only trusted users in **WhatsApp Manager** for tokens
- [ ] Review `bypass_search_access` on attachment fields — users can attach files visible to send flow
- [ ] Multi-company rules enabled (default module rules)
- [ ] Mock provider disabled on production DB

## Data integrity checklist

- [ ] Understand idempotency is **per campaign**
- [ ] Retry creates **new** campaigns for failed sets
- [ ] Reconcile stale runs after incidents ([Runbook](../operations/RUNBOOK.md))
- [ ] Daily limit uses `status='sent'` — align expectations with `delivery_state` if customizing reports

## Monitoring checklist

- [ ] Odoo server log monitoring for `Campaign` / `Execution` log lines
- [ ] Optional dedicated `whatsapp.log` file rotation
- [ ] Campaign Monitor for operators during sends
- [ ] PostgreSQL disk space for log growth

## Provider checklist (Green API)

- [ ] Valid instance and token
- [ ] Test connection from Settings
- [ ] Rate limits understood (module adds its own delays)
- [ ] Incident plan for provider outage (messages fail; logs show `failed`)

## Post-deploy upgrade

```bash
odoo-bin -u relayruntime -d PROD_DB
```

Verify `whatsapp.bulk.execution` table exists after 19.0.5.5.0+ upgrade.

## Further reading

- [Known Limitations](../architecture/KNOWN_LIMITATIONS.md)
- [Monitoring Guide](../operations/MONITORING_GUIDE.md)
- [Odoo.sh Deployment](ODOO_SH_DEPLOYMENT.md)
