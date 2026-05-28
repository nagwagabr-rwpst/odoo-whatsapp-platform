# Troubleshooting

[← Documentation index](../README.md) · [Runbook](RUNBOOK.md)

## Symptom index

| Symptom | Likely cause | Doc |
|---------|--------------|-----|
| "Daily WhatsApp send limit reached" | `daily_send_limit` exceeded | [Settings / safety](#daily-limit) |
| "Campaign already has an active execution" | Concurrent or stale lease | [Runbook](RUNBOOK.md) |
| "Provider not implemented" | Non-Green/Mock provider selected | [Providers](#provider-errors) |
| Bulk wizard hangs then fails | `limit_time_real` exceeded | [Timeouts](#http-timeouts) |
| Progress stuck at 0% | Not started or monitor snapshot | [Monitor](#campaign-monitor) |
| Retry opens existing campaign | Fingerprint dedup (expected) | [Retry](../runtime/RETRY_AND_REPLAY.md) |
| Customer got duplicate message | Rollback/retry/provider | [Duplicates](#duplicate-messages) |
| No messages but logs say sent (Mock) | Mock provider — expected | [Mock](#mock-provider) |

## Provider errors

### "Provider not implemented"

**Cause:** `provider_type` is a stub adapter (`meta_cloud`, `evolution`, etc.).

**Fix:** Set **Green API** or **Mock Provider** in Settings.

### Green API connection failures

| Check | Action |
|-------|--------|
| Token / instance | Re-enter credentials |
| API URL | Default Green API base URL |
| Network | Firewall egress to Green API |
| Log `api_logger` | Response body on log `api_response_body` |

## Daily limit

**Implemented behavior:** counts logs where legacy `status='sent'` today — not `delivery_state` alone.

| Issue | Detail |
|-------|--------|
| Limit seems wrong | Failed sends do not count; skipped do not count |
| Mid-campaign stop | `ValidationError` → campaign `stopped`, partial progress |

**Partial gap:** `delivery_state='sent'` with `status` mismatch rare — investigate computed `status` field.

## HTTP timeouts

**Symptoms:** Worker kills request; partial logs; execution may reconcile as stale.

**Mitigations:**

- Reduce recipients per campaign
- Increase `limit_time_real` (understand worker blocking)
- Reduce attachments / product images
- Lower Mock latency for tests only

## Campaign monitor

**Implemented:** kanban reload every 5 seconds — not live websocket.

| Issue | Explanation |
|-------|-------------|
| Stale numbers | Wait for reload or reopen |
| Shows running after done | Browser cache / reconcile needed |

## Duplicate messages

| Cause | Detection |
|-------|-----------|
| Retry child campaign | New campaign id — intentional resend |
| HTTP rollback after provider success | No log row; provider dashboard shows send |
| Idempotency skip failed | Same campaign should not double-send |

No automated dedupe at provider layer.

## Mock provider

- Messages are simulated — `[MOCK]` in logs
- TEST MODE ribbon in UI
- Magic numbers in Settings force failures/timeouts

## Database / upgrade

| Symptom | Fix |
|---------|-----|
| Missing `whatsapp_bulk_execution` table | Upgrade module `-u relayruntime` |
| Unique violation idempotency | Expected race recovery — if persists, duplicate key data |

## Logs to collect for support

1. Campaign id, execution id, `execution_uuid`
2. `whatsapp.message.log` export for campaign
3. Odoo server log slice (time window)
4. Optional `whatsapp.log` file
5. Provider type and sanitized config (no tokens in tickets)

## Further reading

- [Monitoring Guide](MONITORING_GUIDE.md)
- [Known Limitations](../architecture/KNOWN_LIMITATIONS.md)
