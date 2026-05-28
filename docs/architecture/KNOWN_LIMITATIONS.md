# Known Limitations

[← Documentation index](../README.md) · [System Overview](SYSTEM_OVERVIEW.md)

This document lists **honest, current** constraints. Do not assume capabilities not listed under "Implemented" elsewhere.

## Provider-side non-atomicity

| Limitation | Impact |
|------------|--------|
| WhatsApp send is external HTTP | Cannot roll back a delivered message if Odoo transaction fails |
| Multi-segment per recipient (text + N attachments) | Partial provider success may occur before log marked `failed` |
| No outbound idempotency token | Provider or network retries may duplicate delivery |
| Transport timeouts (Green API: 15–60s configurable paths) | Long blocking; worker tied up |

**Mitigation (partial):** `commit_outbound_intent()` + `queued`/`sending` log states before API calls.

**Not mitigated:** request-level rollback after provider acceptance.

## Long-running transaction limitations

| Limitation | Impact |
|------------|--------|
| Entire bulk run in one HTTP transaction | Large campaigns hold DB locks longer |
| `limit_time_real` (e.g. 120s in sample `odoo.conf`) | Request may be killed server-side |
| No checkpoint commits | Crash loses in-flight DB work for that request |
| ORM cache growth | Memory pressure on very large recipient lists |

**Observed dev config:** `workers = 0` (threaded mode) in repository `server/odoo.conf` — not a production multi-worker layout.

## Duplicate-send edge cases

| Scenario | Still possible? |
|----------|-----------------|
| Same partner twice in same campaign | **No** (idempotency key) |
| Retry campaign for same failed partner | **Yes** (new campaign id) |
| Same retry fingerprint double-click race | **Rare** (unique constraint + savepoint; not serializable isolation) |
| Provider success + HTTP rollback | **Yes** |
| Manual re-send after reconciled stale run | **Yes** if logs incomplete |
| Concurrent users on same campaign | **Reduced** by lease; not impossible under race |

## Retry limitations

| Limitation | Detail |
|------------|--------|
| Fingerprint sensitivity | Editing message/products/attachments changes fingerprint → new retry tree |
| No log-to-retry link | Cannot see which parent log spawned which retry row directly |
| Parent logs unchanged | Retry does not mutate failed parent entries |
| Failed + skipped only | Successful sends are not retried by built-in action |

## Concurrency limitations

| Mechanism | Coverage |
|-----------|----------|
| `FOR UPDATE` on campaign | Same DB connection serialization at start |
| Execution lease | Blocks second live run on same campaign |
| Idempotency unique key | Per campaign/partner |

**Gaps (partially implemented):**

- No `FOR UPDATE NOWAIT` — second starter may block until lock released
- No partial unique index enforcing one `running` execution per campaign at DB level
- Multi-worker Odoo: two workers could theoretically interleave without strict distributed lock
- Users can still create overlapping retry **campaigns** with different fingerprints

## Scalability boundaries

| Area | Current bound |
|------|----------------|
| Execution model | Synchronous sequential loop |
| Parallelism | None per campaign |
| Background processing | **Not implemented** |
| Rate control | Configurable delays + cooldown sleeps (`time.sleep`) in-process |
| Daily limit | Counts logs with `status='sent'` (legacy field), not `delivery_state` |

**Practical guidance:** treat hundreds of recipients per request as high risk for timeouts; thousands require architectural change (planned queue).

## Architectural tradeoffs

| Decision | Benefit | Cost |
|----------|---------|------|
| Single transaction per bulk | No fragmented partial DB state | Long lock duration; rollback scope |
| Campaign as UI aggregate | Simple monitor/kanban | Counters can drift from logs mid-run |
| Execution attempt layer | Lease + lineage without full rewrite | Extra writes; not full event sourcing |
| Provider adapter pattern | Vendor swap | Most adapters are stubs |
| Synchronous sleeps | Simple rate limiting | Blocks HTTP worker |

## Observability gaps

| Item | Status |
|------|--------|
| `delivered` state on logs | Field exists; outbound rarely sets it |
| `sent_at` on log create | Set at creation, not provider ACK time |
| Webhook delivery updates | **Not implemented** (no HTTP routes) |
| Real-time monitor | 5-second kanban reload, not websocket |

## Planned / future (explicitly not implemented)

- Background job queue and cron-driven sending
- Event-sourced append-only delivery events
- Recipient-level attempt table
- Provider outbound idempotency
- Log-derived counters
- Attachment ownership lifecycle and cleanup
- Inbound webhook controllers
- Multi-worker execution lease with DB uniqueness constraint

## Further reading

- [Transaction Model](TRANSACTION_MODEL.md)
- [Retry and Replay](../runtime/RETRY_AND_REPLAY.md)
- [Production Checklist](../deployment/PRODUCTION_CHECKLIST.md)
