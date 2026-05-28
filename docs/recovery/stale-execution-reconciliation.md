# Stale Execution Reconciliation

[← Documentation index](../README.md)

How RelayRuntime detects and releases **orphaned running executions** when workers die or HTTP requests abort without calling `finish()`.

---

## Problem

Bulk send runs inside a single HTTP request. If the worker is killed, proxy times out, or process crashes:

- Execution may remain `running`
- Campaign may remain `running`
- Heartbeat stops updating

Without reconciliation, operators cannot start a new lease-backed run.

---

## Detection (implemented)

Constants ([`constants.py`](../../apps/odoo/relayruntime/constants.py)):

| Constant | Value | Role |
|----------|-------|------|
| `LEASE_EXTENSION_SECONDS` | 900 (15 min) | Lease renewal window |
| `STALE_HEARTBEAT_SECONDS` | 1800 (30 min) | No heartbeat → stale |

Stale condition (conceptual):

```
execution.state == 'running'
AND now - execution.heartbeat_at > STALE_HEARTBEAT_SECONDS
```

---

## Reconciliation action

Triggered from `_reconcile_stale_executions` before new `begin_campaign_execution`:

| Step | Effect |
|------|--------|
| Mark execution | `reconciled` |
| Project campaign | `failed` if campaign still `running` |
| Log | Warning with execution id |

**Does not:** auto-resume recipients, delete partial logs, or call provider cancel APIs.

---

## Operator implications

| After reconcile | Meaning |
|-----------------|---------|
| Execution `reconciled` | Run abandoned—not successfully finished |
| Campaign `failed` | May have partial logs—inspect before retry |
| New bulk allowed | Fresh execution + lease |

Always verify `whatsapp.message.log` before retry—some recipients may have been sent before crash.

---

## Multi-worker caution

Reconciliation runs in the worker handling the **next** begin call. Under `workers > 1`, two begins on same campaign should still hit `FOR UPDATE` and lease assert; validate in your deployment if customizing.

**Not implemented:** dedicated cron reconcile job.

---

## Debugging checklist

1. Open Executions tab on campaign.
2. Note `heartbeat_at`, `lease_expires_at`, `state`.
3. Check server log around last activity timestamp.
4. Compare logs to provider for partial sends.
5. Document incident; use retry only on confirmed failed/skipped.

---

## Related

- [HEARTBEAT_AND_LEASES.md](../runtime/HEARTBEAT_AND_LEASES.md)
- [failure-scenarios.md](../operations/failure-scenarios.md)
- [replay-recovery.md](replay-recovery.md)
