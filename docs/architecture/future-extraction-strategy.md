# Future Extraction Strategy

[← Documentation index](../README.md) · [Runtime boundaries](runtime-boundaries.md)

How RelayRuntime code may leave the Odoo addon **without** breaking operational semantics or pretending extraction is complete.

---

## Extraction goal

Move **pure execution logic** into `runtime/*` packages callable from Odoo (or later from a standalone service) while keeping:

- stable idempotency key format
- lease / heartbeat / stale rules
- retry fingerprint semantics
- execution attempt as authority

---

## Candidate modules

| Current location | Extraction target | Risk |
|------------------|-------------------|------|
| Lease + stale reconcile | `runtime/execution/lease.py` | Medium — needs clock + config injection |
| Heartbeat policy | `runtime/execution/heartbeat.py` | Low |
| Idempotency key builder | `runtime/execution/idempotency.py` | **High** — DB unique constraint tied to format |
| Retry fingerprint | `runtime/retry/fingerprint.py` | Medium — SQL unique on campaign |
| Bulk recipient loop | `runtime/execution/runner.py` | High — Odoo ORM today |
| Provider adapter interface | `runtime/providers/base.py` | Medium |

**Do not extract** views, security XML, or ERP field definitions.

---

## Extraction phases (recommended)

### Phase A — Pure functions

Extract stateless helpers with unit tests **outside** Odoo:

- fingerprint computation
- idempotency key string
- stale threshold evaluation (inputs: timestamps, constants)

Odoo addon imports from `runtime.*`.

### Phase B — Execution DTOs

Define dataclasses / typed dicts:

- `ExecutionContext`, `RecipientResult`, `FinishStats`

Odoo models map to/from DTOs at boundary.

### Phase C — Runner without ORM

`BulkRunner.run(context, provider_port, store_port)` where `store_port` is implemented by Odoo in-process.

### Phase D — Optional service

HTTP API accepts enqueue; worker runs Phase C; Odoo polls or subscribes.

Each phase ships **independently** with regression tests on Mock Provider.

---

## Contracts to freeze before Phase C

Document and version:

```
idempotency_key = f"campaign:{campaign_id}:partner:{partner_id}"
retry_fingerprint = SHA1(parent_id + sorted(log_ids) + ...)
lease_duration_seconds = 900
stale_heartbeat_seconds = 1800
```

Breaking changes require migration scripts and CHANGELOG major note.

---

## What stays in Odoo indefinitely (likely)

| Asset | Reason |
|-------|--------|
| Campaign / wizard UI | ERP UX |
| `res.partner` linkage | Domain model |
| Security groups | Odoo ACL model |
| `whatsapp.config` | Tenant settings UI |

---

## Anti-patterns during extraction

- Importing `odoo` from `runtime/*`
- Duplicating lease logic in wizard and service
- Silent change to log `_name` or idempotency key
- “Temporary” second execution path without lease

---

## Validation checklist (per extraction PR)

- [ ] Mock Provider bulk still passes
- [ ] Lease rejection on concurrent begin still works
- [ ] Retry fingerprint dedup unchanged
- [ ] Stale reconcile behavior unchanged
- [ ] No new mid-loop commits

---

## Related

- [runtime-vision.md](runtime-vision.md)
- [embedded-runtime.md](../deployment/embedded-runtime.md)
- [future-runtime-service.md](../deployment/future-runtime-service.md)
- Legacy note: [future-runtime-extraction.md](../deployment/future-runtime-extraction.md) (shorter placeholder—prefer this doc)
