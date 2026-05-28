# Failure Scenarios

[← Documentation index](../README.md)

Realistic operational failures for embedded RelayRuntime—not exhaustive, but actionable.

---

## Worker interruption

| Symptom | Cause | System behavior | Operator action |
|---------|-------|-----------------|-----------------|
| Campaign `running` forever | HTTP killed, OOM, deploy | Heartbeat stops; later reconcile → `reconciled` / `failed` | Inspect logs; retry failed only |
| Partial logs | Crash mid-loop | Transaction rollback **may** drop in-flight rows | Compare provider |
| No finish() | Worker death | Execution not terminal | Wait for stale or new begin |

**Not mitigated:** automatic resume from last index.

---

## Partial batch failure

| Symptom | Cause | Behavior |
|---------|-------|----------|
| `completed_with_errors` | Some recipients failed | Terminal with mixed logs |
| `stopped` | Daily limit mid-send | Partial progress |
| Skipped rows | Missing phone, idempotency | Counted in stats |

Use **Retry failed recipients** for subset—not full parent resend unless intended.

---

## Provider timeout

| Symptom | Risk |
|---------|------|
| HTTP timeout to Green API | Message may have been sent without DB `sent` |
| 5xx from provider | Log `failed`; retry may duplicate |
| Rate limit | Backoff via safety validator; may stop batch |

**Guidance:** check provider message list before retrying same partners.

---

## Duplicate send risk

| Scenario | Duplicate possible? |
|----------|---------------------|
| Same campaign, same partner, second loop iteration | No (idempotency skip) |
| Retry child campaign | **Yes** (new campaign id) |
| Reconcile + new bulk on parent | **Yes** if logs rolled back |
| Two operators, race before lease | Edge case—rare |
| Provider retries HTTP | Outside RelayRuntime |

---

## Attachment inconsistency

| Symptom | Cause |
|---------|-------|
| Text sent, image failed | Multi-segment send |
| Product image missing | Catalog / access issue |
| Wrong attachment order | Template vs product segments |

Logs record per-segment outcome where implemented; review full log chain per partner.

---

## Lease conflict

| Symptom | Meaning |
|---------|---------|
| UserError on begin | Active lease on campaign |
| Second browser tab send | Expected rejection |

Wait for terminal or stale reconcile before retrying full bulk.

---

## Database / upgrade failures

| Symptom | Action |
|---------|--------|
| Module upgrade mid-campaign | Avoid; quiesce sends first |
| Missing execution table | Upgrade not applied |
| XML ID broken views | Fix customizations per MIGRATION |

---

## Multi-worker (caution)

Embedded runtime assumes coordinated DB locking. Under multiple workers:

- Validate lease + `FOR UPDATE` behavior under load.
- Do not assume in-memory locks.

Distributed runtime not implemented—see [runtime-vision.md](../architecture/runtime-vision.md).

---

## Related

- [replay-recovery.md](../recovery/replay-recovery.md)
- [stale-execution-reconciliation.md](../recovery/stale-execution-reconciliation.md)
- [KNOWN_LIMITATIONS.md](../architecture/KNOWN_LIMITATIONS.md)
