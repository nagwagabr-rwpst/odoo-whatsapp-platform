# Runtime Failure Tests

[← Documentation index](../README.md) · [Testing Strategy](TESTING_STRATEGY.md)

Manual and semi-automated scenarios for **failure and recovery** behavior. Use **Mock Provider** unless explicitly testing Green API.

## Crash simulation

| # | Steps | Expected (implemented) | Known gap |
|---|-------|------------------------|-----------|
| 1 | Start bulk (50+ recipients), kill Odoo process mid-run | Request txn lost; may have partial provider sends; campaign/execution may stay `running` until reconcile | Provider may have sent without committed log |
| 2 | After kill, open wizard and start **different** campaign | Reconcile on entry may mark stale execution `reconciled` | — |
| 3 | Kill immediately after notification "finished" | Should be consistent committed state | — |

**Tooling:** stop Windows service / `taskkill` / container SIGKILL — environment-specific.

## Retry simulation

| # | Steps | Expected |
|---|-------|----------|
| 1 | Bulk with Mock failure rate > 0 | Some `failed` logs |
| 2 | **Retry Failed Recipients** | New child campaign; `attempt_kind=retry`; sends only failed/skipped partners |
| 3 | Double-click retry quickly | Same retry campaign opened (fingerprint dedup) |
| 4 | Change message on parent, retry again | New fingerprint → **new** retry campaign allowed |

## Stale execution recovery

| # | Steps | Expected |
|---|-------|----------|
| 1 | Set campaign `running`, set `execution.heartbeat_at` to 31+ minutes ago (shell/SQL) | — |
| 2 | Trigger any bulk send (reconcile runs) | Execution → `reconciled`; campaign → `failed` if active match |
| 3 | Start send on previously stuck campaign | New execution if lease clear |

**SQL example (test DB only):**

```sql
UPDATE whatsapp_bulk_execution
SET heartbeat_at = NOW() - INTERVAL '35 minutes'
WHERE state = 'running';
```

## Duplicate-send testing

| # | Steps | Expected |
|---|-------|----------|
| 1 | Complete bulk for partner A | Log with idempotency key exists |
| 2 | Attempt second bulk on **same** campaign for partner A | Skipped (warning in log) |
| 3 | Retry campaign including partner A | **May send again** (new campaign id) |
| 4 | Mock magic timeout numbers (Settings help) | Failed logs; retry path works |

## Worker restart testing

| # | Steps | Expected |
|---|-------|----------|
| 1 | Start bulk, restart Odoo worker mid-run | Same as crash simulation |
| 2 | `workers > 0`: two users same campaign | Second should get UserError (active lease) if first still running |

## ValidationError / daily limit

| # | Steps | Expected |
|---|-------|----------|
| 1 | Set low `daily_send_limit` | Pre-send block |
| 2 | Set limit to N, send N successfully, continue bulk | Mid-loop stop; `stopped`; progress < 100% |

## Outbound intent

| # | Steps | Expected |
|---|-------|----------|
| 1 | Enable SQL logging or breakpoint after `commit_outbound_intent` | `delivery_state=sending`, `outbound_intent_at` set before provider call in same txn |
| 2 | Rollback forced after provider (test harness) | No log row after rollback; duplicate risk on rerun |

## Record evidence

For each test record:

- Campaign id, execution id, execution_uuid
- Log ids and `delivery_state`
- Server log excerpts (`campaign_logger`)

## Further reading

- [Outbound Intents](../runtime/OUTBOUND_INTENTS.md)
- [Runbook](../operations/RUNBOOK.md)
