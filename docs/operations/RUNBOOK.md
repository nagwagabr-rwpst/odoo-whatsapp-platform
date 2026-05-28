# Operations Runbook

[← Documentation index](../README.md)

Procedures for operators supporting **WhatsApp Simple** in production.

## Stuck campaigns (`state=running`)

### Symptoms

- Campaign Monitor shows running indefinitely
- No progress on `processed_count`
- Users cannot retry (active lease message)

### Diagnosis

1. Open campaign form → **Executions** tab.
2. Check active execution:
   - `state`, `heartbeat_at`, `lease_expires_at`, `executor_uid`
3. Check server logs for `campaign_logger` / worker timeout.

### Recovery

| Situation | Action |
|-----------|--------|
| No real process running; heartbeat old | Trigger **any** bulk send on another campaign OR upgrade/restart after reconcile — or run reconcile via Odoo shell (below) |
| Execution heartbeat > 30 min stale | `_reconcile_stale_executions()` marks `reconciled` |
| Campaign still `running` without live lease | `_reconcile_stale_running_campaigns()` fallback |

**Odoo shell (staging/prod — use with care):**

```python
env['whatsapp.bulk.execution']._reconcile_stale_executions()
env['whatsapp.bulk.campaign']._reconcile_stale_running_campaigns()
```

4. Verify campaign `state` is `failed` or terminal.
5. Use **Retry Failed Recipients** if appropriate.

## Zombie executions

**Definition:** `whatsapp.bulk.execution` with `state=running` but no live worker.

**Recovery:** Same as stale reconciliation above.

**Do not** manually set `running` → `completed` without reviewing logs — counters may be wrong.

## Stale leases

| Field | Meaning |
|-------|---------|
| `lease_expires_at` in past | Lease expired; new run may start |
| `lease_expires_at` in future but stuck | Process died without finish — reconcile |

Clearing lease manually:

```python
execution.write({'lease_expires_at': False, 'lease_token': False, 'state': 'reconciled', 'finished_at': fields.Datetime.now()})
```

Only after confirming no active worker.

## Retry recovery

| Problem | Action |
|---------|--------|
| Duplicate retry campaigns | Identify `retry_fingerprint` on children; use canonical child |
| Wrong recipients retried | Parent logs unchanged — create new manual bulk if needed |
| Retry blocked (running) | Reconcile parent first |

## Rollback recovery (provider sent, DB unclear)

**There is no automatic provider rollback.**

1. Search provider dashboard / Green API history by phone and time.
2. Compare with `whatsapp.message.log` for campaign.
3. If provider shows sent but no log: **manual business decision** — do not auto bulk-retry without risk of duplicate.

Document incident; see [Known Limitations](../architecture/KNOWN_LIMITATIONS.md).

## `sending` logs stuck

| Step | Action |
|------|--------|
| 1 | Find logs `delivery_state=sending` for campaign |
| 2 | Check `outbound_intent_at` — intent was flushed in txn that may not have committed |
| 3 | If campaign completed and partner has no terminal log | Consider manual log correction **or** retry campaign (may skip if idempotency key exists) |

**Planned / future:** automated repair job — not implemented.

## Preventive operations

- Run reconciliation before large sends after incidents
- Cap campaign size per [Production Checklist](../deployment/PRODUCTION_CHECKLIST.md)
- Use Mock on non-prod only

## Further reading

- [Troubleshooting](TROUBLESHOOTING.md)
- [Monitoring Guide](MONITORING_GUIDE.md)
