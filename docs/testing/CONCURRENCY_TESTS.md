# Concurrency Tests

[← Documentation index](../README.md) · [Testing Strategy](TESTING_STRATEGY.md)

Tests for **overlapping operations** on campaigns and retries. Run on a configuration that matches production (`workers > 0` recommended for worker tests).

## Same campaign — concurrent execution start

| # | Procedure | Expected (implemented) |
|---|-----------|------------------------|
| 1 | User A starts bulk on campaign X (hold tab open mid-run via Mock latency) | Execution running, lease valid |
| 2 | User B triggers send on **same** campaign (custom code or retry path if applicable) | `UserError`: active execution |
| 3 | Wait until finish | Lease cleared; new run allowed |

**Partial gap:** two simultaneous HTTP requests starting **at the same instant** may race before lease row exists — verify on your DB isolation level.

## Same campaign — FOR UPDATE behavior

| # | Procedure | Expected |
|---|-----------|----------|
| 1 | Long-running bulk holds lock from `begin_campaign_execution` | Second starter blocks at `FOR UPDATE` until first completes |

Observe PostgreSQL `pg_locks` in staging if diagnosing waits.

## Retry concurrency

| # | Procedure | Expected |
|---|-----------|----------|
| 1 | Two users click **Retry Failed Recipients** simultaneously | One child campaign created; second opens existing (fingerprint) |
| 2 | Different recipient sets on parent (if manually edited logs — advanced) | Different fingerprints → two retry campaigns possible |

## Idempotency race

| # | Procedure | Expected |
|---|-----------|----------|
| 1 | Theoretical parallel duplicate `create_log` same idempotency key | One succeeds; other hits `IntegrityError` and recovers to existing row in `create_log` |

Not covered by automated test today — optional stress script.

## Multi-worker Odoo

| # | Procedure | Expected |
|---|-----------|----------|
| 1 | `workers=2`, two bulks on **different** campaigns | Both proceed independently |
| 2 | Same campaign from two workers | Lease + lock should block one — **verify manually** (partially implemented) |

Document results; treat failures as architectural limits ([Known Limitations](../architecture/KNOWN_LIMITATIONS.md)).

## Stale lease vs live run

| # | Procedure | Expected |
|---|-----------|----------|
| 1 | Active bulk with heartbeats | Reconcile must **not** mark reconciled |
| 2 | Stuck bulk without heartbeat 30+ min | Reconcile marks `reconciled` |

## False-positive check

| # | Procedure | Risk |
|---|-----------|------|
| 1 | Mock `simulated_latency_ms` very high, few recipients, long gaps | May appear stale if heartbeats insufficient — use ≥45s gap test |

## Further reading

- [Heartbeat and Leases](../runtime/HEARTBEAT_AND_LEASES.md)
- [Runtime Failure Tests](RUNTIME_FAILURE_TESTS.md)
