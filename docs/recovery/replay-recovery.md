# Replay and Recovery

[← Documentation index](../README.md)

Operational recovery for RelayRuntime bulk runs. **Replay-safe** means re-invoking paths should not corrupt aggregates; it does **not** guarantee zero duplicate messages at the provider.

---

## Replay-safe philosophy

| Concept | RelayRuntime interpretation |
|---------|------------------------------|
| Idempotent skip | Same campaign + partner → log exists → skip send |
| New execution | Each bulk begin creates new `whatsapp.bulk.execution` |
| Retry campaign | New campaign id → **new** idempotency namespace |
| Provider truth | May differ from DB after HTTP rollback |

Operators must treat **message logs + execution state** as primary internal truth; provider dashboard as external truth when they diverge.

---

## When to replay vs retry

| Situation | Action |
|-----------|--------|
| Transient provider errors on subset | **Retry failed** → child campaign |
| Campaign stuck `running`, stale execution | Reconcile (automatic on next begin) or runbook |
| Wrong message content sent | **Do not** auto-retry—manual comms + new campaign |
| HTTP timeout after provider accept | Investigate provider; avoid blind retry |

---

## Automatic reconciliation (implemented)

Before `begin_campaign_execution`:

1. Find executions for campaign in `running` with stale heartbeat (30+ min).
2. Mark execution `reconciled`.
3. Project campaign to `failed` if still `running`.

This is **not** a full replay—it releases ownership so operators can act.

Detail: [stale-execution-reconciliation.md](stale-execution-reconciliation.md)

---

## Manual recovery procedures

See [RUNBOOK](../operations/RUNBOOK.md):

- Verify execution tab state
- Compare `whatsapp.message.log` to provider
- Use Mock Provider in staging to reproduce
- Cancel campaign only when business rules allow

**Not implemented:** one-click “resume from last_recipient_index”.

---

## Recovery constraints

| Constraint | Reason |
|------------|--------|
| No mid-loop commit | Single transaction—rollback loses in-flight logs |
| Lease required for new run | Prevents parallel corrupting loops |
| Retry fingerprint unique | Prevents duplicate retry trees |
| Child campaign new id | Idempotency keys include campaign id |

---

## Consistency protection

| Mechanism | Protects against |
|-----------|------------------|
| `FOR UPDATE` on campaign | Counter races during projection |
| Execution authority | Stale UI progress |
| Unique idempotency key | Double-send same recipient same campaign |
| `commit_outbound_intent` | Partial visibility before provider (best-effort) |

Gaps: cross-campaign retry may resend same partner; provider duplicates outside DB.

---

## Related

- [retry-lineage.md](retry-lineage.md)
- [failure-scenarios.md](../operations/failure-scenarios.md)
- [TRANSACTION_MODEL.md](../architecture/TRANSACTION_MODEL.md)
