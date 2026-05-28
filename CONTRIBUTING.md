# Contributing to RelayRuntime

RelayRuntime is an **operational messaging execution runtime**. Contributors should think in terms of execution correctness, recovery, and extraction boundaries—not feature widgets.

---

## Who this is for

| Contributor type | Expected focus |
|------------------|----------------|
| **Runtime engineer** | Execution lifecycle, lease, idempotency, transaction boundaries |
| **Operational systems** | Observability, runbooks, failure scenarios, deployment constraints |
| **Odoo integrator** | ERP models, views, ACL—without collapsing runtime into UI code |

---

## Before you start

1. Read [docs/architecture/runtime-boundaries.md](docs/architecture/runtime-boundaries.md).
2. Read [docs/development/RUNTIME_SAFETY_RULES.md](docs/development/RUNTIME_SAFETY_RULES.md).
3. Run `python scripts/ci_validate.py`.
4. Use **Mock Provider** for execution-path testing.

---

## Runtime vocabulary

| Term | Meaning |
|------|---------|
| **Campaign** | Business aggregate (`whatsapp.bulk.campaign`)—configuration, UI, retry tree |
| **Execution attempt** | Runtime authority (`whatsapp.bulk.execution`)—one HTTP bulk run |
| **Lease** | Exclusive ownership window for an execution (`lease_token`, `lease_expires_at`) |
| **Heartbeat** | Liveness signal (`heartbeat_at`) for stale detection |
| **Projection** | Campaign fields mirrored from execution for UI |
| **Recipient truth** | `whatsapp.message.log` per partner within a campaign |
| **Replay** | Recovery after failure—reconcile, retry, manual operator action |
| **Idempotency key** | `campaign:{id}:partner:{id}`—campaign-scoped dedupe |

---

## Code organization rules

| Code belongs in | When |
|-----------------|------|
| `apps/odoo/relayruntime/models/` | Odoo persistence tied to ERP |
| `apps/odoo/relayruntime/wizard/` | User entrypoints |
| `apps/odoo/relayruntime/views/` | UI only |
| `apps/odoo/relayruntime/services/` | Orchestration today—mark extraction candidates |
| `runtime/*` | Framework-agnostic logic **when extracted**—no Odoo imports |

Do not add business logic to XML or JavaScript that should live in execution services.

---

## Runtime boundary discipline

- **Do not** call `cr.commit()` inside bulk recipient loops.
- **Do not** set `campaign.state = running` without `begin_campaign_execution`.
- **Do not** weaken idempotency or retry fingerprint constraints without migration docs.
- **Do not** re-raise exceptions after provider success without documented compensation.
- **Do** add `# Runtime boundary candidate` / `# TODO: Future extraction` only where meaningful.

Extraction-ready code: pure functions (fingerprint input, lease duration math) may move to `runtime/` with tests that do not require Odoo.

---

## Recovery-aware development

When changing send paths, answer:

1. What happens if the HTTP request rolls back after provider success?
2. What happens if two users start bulk on the same campaign?
3. What happens if the worker dies mid-recipient?
4. Does progress still reflect partial completion honestly?

Add or update docs in `docs/recovery/` when behavior changes.

---

## Failure-first thinking

Prefer explicit terminal states and operator-visible failures over silent retries.

| Avoid | Prefer |
|-------|--------|
| Swallowing provider errors | Terminal log + campaign/execution finish |
| Forced 100% progress | Derived progress from processed counts |
| Hidden second send paths | Single orchestration entry (`WhatsAppBulkSender`) |

See [docs/operations/failure-scenarios.md](docs/operations/failure-scenarios.md).

---

## Observability expectations

- Use `campaign_logger`, `api_logger`, `attachment_logger`—not ad-hoc `print`.
- New execution states must appear on **Executions** tab or logs.
- If adding metrics, target `runtime/observability/` design—do not hard-code vendor agents in models.

---

## Testing expectations

| Level | Requirement |
|-------|-------------|
| CI | `python scripts/ci_validate.py` passes |
| Style | Flake8 critical rules on `apps/odoo/relayruntime` |
| Odoo | `--test-tags=relayruntime` when touching runtime paths |
| Manual | Mock bulk, retry, duplicate-click retry, stale reconcile scenario |

Document manual steps in PR if automated coverage does not exist.

---

## Pull requests

Use [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).

Required for runtime-affecting PRs:

- Architecture impact statement
- Transaction boundary impact
- Retry/replay impact
- `CHANGELOG.md` entry under `[Unreleased]` or version section
- Doc updates in `docs/` when behavior changes

---

## Extraction-aware development

If your change grows execution logic:

1. Can it live in `runtime/` with an Odoo adapter?
2. Does it introduce Odoo imports into `runtime/`? (Reject.)
3. Is it documented in [future-extraction-strategy.md](docs/architecture/future-extraction-strategy.md)?

---

## Related

- [SUPPORT.md](SUPPORT.md)
- [SECURITY.md](SECURITY.md)
- [docs/development/CONTRIBUTING.md](docs/development/CONTRIBUTING.md) — supplemental Odoo module notes
