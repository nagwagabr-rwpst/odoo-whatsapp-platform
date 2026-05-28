# Testing Strategy

[← Documentation index](../README.md)

## Goals

Verify **implemented** behavior of WhatsApp Simple without assuming future queue or webhook capabilities.

| Priority | Area |
|----------|------|
| P0 | Bulk send completes; logs match outcomes |
| P0 | Idempotency and retry deduplication |
| P0 | Execution lease blocks concurrent same-campaign runs |
| P1 | Stale reconciliation |
| P1 | Provider adapter errors surfaced on logs |
| P2 | Large campaign timeout and memory behavior |

## Test layers (current repository)

| Layer | Location | Status |
|-------|----------|--------|
| Automated unit/integration | `tests/` | **Partial** — wizard action + product tests |
| Mock provider | `services/providers/mock_provider.py` | **Implemented** |
| Manual QA | Campaign monitor + logs | **Required** for execution/lease |
| Load/stress | Not in CI | **Manual** |

Run automated tests:

```bash
python odoo-bin -c odoo.conf -d TEST_DB --test-tags=whatsapp_simple --stop-after-init
```

## Test environment

| Setting | Recommendation |
|---------|----------------|
| Provider | `mock_provider` |
| `daily_send_limit` | High (e.g. 10000) for bulk tests |
| `workers` | Match target deployment or `0` for local |
| Database | Dedicated test DB; never production |

## Coverage gaps (honest)

| Area | Automated coverage |
|------|-------------------|
| Execution lease / heartbeat | **Not in `tests/` yet** |
| Idempotency constraint | **Not in `tests/` yet** |
| Retry fingerprint | **Not in `tests/` yet** |
| Green API HTTP | Manual / external sandbox |
| Concurrency | Manual |
| Crash simulation | Manual |

## Related test documents

- [Runtime Failure Tests](RUNTIME_FAILURE_TESTS.md)
- [Concurrency Tests](CONCURRENCY_TESTS.md)
- [Large Campaign Tests](LARGE_CAMPAIGN_TESTS.md)

## Planned / future

- CI job on Odoo 19 with `whatsapp_simple` tag
- Transactional tests for `begin_campaign_execution` / reconcile
- Property tests for fingerprint stability

## Further reading

- [Local Setup](../deployment/LOCAL_SETUP.md)
- [Runtime Safety Rules](../development/RUNTIME_SAFETY_RULES.md)
