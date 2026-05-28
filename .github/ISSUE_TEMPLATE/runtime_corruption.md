---
name: Runtime Corruption / Stale State
about: Report stuck campaigns, stale executions, or DB/runtime truth mismatch
title: "[Runtime]: "
labels: ["runtime", "integrity", "triage"]
assignees: []
---

## Environment

| Field | Value |
|-------|-------|
| **Odoo version** | |
| **Module version** | |
| **Provider** | |
| **Deployment** | <!-- Local / Odoo.sh / Docker --> |
| **Workers** | |
| **`limit_time_real`** | <!-- if known --> |

## Symptom

<!-- e.g. campaign stuck running, counters wrong, sending logs orphaned -->

- [ ] Campaign `state=running` indefinitely
- [ ] Execution `state=running` / `reconciled` unexpected
- [ ] Progress counters disagree with message logs
- [ ] `sending` logs never terminalized
- [ ] Other: 

## Identifiers

| Field | Value |
|-------|-------|
| **Campaign ID** | |
| **Campaign name** | |
| **Execution attempt ID** | |
| **Execution UUID** | |
| **Active execution on campaign** | <!-- yes/no/unknown --> |
| **Parent campaign ID** (if retry) | |
| **Parent execution ID** | |

## Retry lineage

<!-- Describe retry chain: parent → child campaigns, fingerprints if known -->

```
(paste lineage or list campaign IDs)
```

## Duplicate-send evidence

<!-- If customers received duplicates, note here or file Duplicate Send template too -->

| Recipient | Times sent | Log IDs | Provider message IDs |
|-----------|------------|---------|----------------------|
| | | | |

## Stale execution evidence

| Field | Value |
|-------|-------|
| `heartbeat_at` | |
| `lease_expires_at` | |
| `last_activity_at` (campaign) | |
| Last server activity time | |

## Transaction behavior

<!-- What happened around the incident: timeout, worker restart, double-click, concurrent users -->

- [ ] HTTP timeout / worker killed
- [ ] Odoo service restart mid-run
- [ ] Concurrent bulk/retry on same campaign
- [ ] Rollback or error after partial send
- [ ] Reconciliation run (wizard/retry/shell)

## Reconciliation results

<!-- If you ran reconcile or opened a new send, what changed? -->

```python
# Optional: shell commands used
# env['whatsapp.bulk.execution']._reconcile_stale_executions()
```

**Before / after states:**

| Object | Before | After |
|--------|--------|-------|
| Campaign | | |
| Execution | | |

## Logs

<details>
<summary>Sanitized log excerpt</summary>

```
(no tokens)
```

</details>

## References

- [Runbook](docs/operations/RUNBOOK.md)
- [Heartbeat and Leases](docs/runtime/HEARTBEAT_AND_LEASES.md)
- [Transaction Model](docs/architecture/TRANSACTION_MODEL.md)
