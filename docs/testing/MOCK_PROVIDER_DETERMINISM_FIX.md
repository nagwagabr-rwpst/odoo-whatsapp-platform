# Mock Provider Determinism Fix

[← Documentation index](../README.md) · [Testing Strategy](TESTING_STRATEGY.md)

## Root cause

`MockProvider._get_rate_map()` and `whatsapp.config._onchange_provider_type()` used falsy `or` fallbacks:

```python
float(self.config.simulate_failure_rate or 5.0)
```

In Python, `0.0` is falsy. Any explicitly configured **0%** simulation rate was treated as “missing” and replaced with the default (e.g. failure `5.0`, timeout `3.0`).

That broke the contract for:

- CI tests that set `simulate_failure_rate=0.0` (and siblings) for deterministic success
- operators who want **true 0%** failure/timeout/rate-limit simulation on Mock Provider

## Why `0.0 or default` is dangerous

| Expression | Intended meaning | Actual result |
|------------|------------------|---------------|
| `0.0 or 5.0` | 0% failure rate | `5.0` (default) |
| `None or 5.0` | unset → default | `5.0` (correct) |
| `False or 5.0` | unset in onchange | `5.0` (correct) |

The bug is **silent**: no validation error, no log — mock sends randomly fail in CI while configs look correct in the database.

## Fix

Use explicit unset detection (`None` / `False` only), not falsy `or`:

- `relayruntime/services/providers/mock_provider.py` — `_coalesce_simulation_rate()` in `_get_rate_map()`, attachment rate, and `_pick_random_outcome()`
- `relayruntime/views/models/whatsapp_config.py` — `_default_if_unset_float()` in `_onchange_provider_type()`

Configured `0.0` is preserved. Unset fields still receive model/UI defaults (`85 / 5 / 3 / 2` for outcome weights, etc.).

### Deterministic success fast-path

When failure, timeout, and rate-limit weights are all exactly `0`, `_pick_random_outcome()` returns `'success'` without calling `random.uniform()`. This keeps bulk/CI runs stable when only success weight is non-zero (e.g. `simulate_success_rate=100` and all error rates `0`).

Magic test numbers (`201000000000`, etc.) are unchanged and still force specific outcomes.

## Deterministic testing guarantees

With Mock Provider configured as:

```python
{
    'simulate_success_rate': 100.0,
    'simulate_failure_rate': 0.0,
    'simulate_timeout_rate': 0.0,
    'simulate_rate_limit_rate': 0.0,
    'simulate_attachment_failure_rate': 0.0,
    'simulated_latency_ms': 0.0,
}
```

(non-magic recipient numbers)

- Outcome selection does not inject random failures from configured rates
- Repeated test runs should not flake on provider simulation alone
- Orchestration, replay, bulk leases, and provider interfaces are unchanged

## Operator simulation semantics

| Setting | Meaning |
|---------|---------|
| `0` on a rate field | **0% weight** for that outcome in random selection (not “use default”) |
| Empty / unset in UI onchange | Provider-type switch fills documented defaults once |
| `100` success + `0` on all error rates | Effectively always success for normal numbers (fast-path) |
| Magic numbers | Deterministic errors regardless of rates |

To simulate realistic failure mix, set non-zero weights that sum with success; defaults remain `85 / 5 / 3 / 2` when fields are never set.

## Validation

```bash
python -m py_compile relayruntime/services/providers/mock_provider.py
python -m py_compile relayruntime/views/models/whatsapp_config.py
```

Odoo module tests (when DB available):

```bash
python odoo-bin -c odoo.conf -d TEST_DB --test-tags=relayruntime --stop-after-init
```

Re-run the same tag twice; mock-configured suites should not gain new random failures from rate coercion.
