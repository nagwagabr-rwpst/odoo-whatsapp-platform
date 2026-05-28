# Security Policy

RelayRuntime security spans **credential protection**, **execution integrity**, and **honest limits** of provider-side consistency. This is not a cryptographic messaging protocol.

---

## Supported versions

| Module version | Support |
|----------------|---------|
| 19.0.6.x | Yes |
| 19.0.5.x | Best effort |
| &lt; 19.0.5.4 | No |

Apply fixes via patch release on the `19.0.x` Odoo module series:

```bash
odoo-bin -u relayruntime -d YOUR_DATABASE
```

---

## Reporting a vulnerability

**Do not** open public GitHub issues for security vulnerabilities.

1. Email maintainers privately (see repository contact or `SECURITY` contact configured for your fork).
2. Include: Odoo version, `relayruntime` module version, deployment topology, reproduction, impact on confidentiality / integrity / availability.
3. Allow reasonable coordinated disclosure time.

Reports should distinguish **authorization bugs** from **operational duplicate-send risk** (often architectural, not CVE-class).

---

## Scope

### In scope

- ACL / record rule bypass on campaigns, logs, or config
- Exposure of `access_token` or webhook secrets via UI, logs, or exports
- Unauthorized send paths bypassing wizard or lease gates
- Integrity flaws allowing execution lease forgery via unauthenticated API

### Out of scope

- Compromised Odoo admin accounts
- Provider platform vulnerabilities (Green API, Meta, etc.)
- Social engineering of operators
- Absence of exactly-once delivery (documented limitation)
- Duplicate sends caused by HTTP rollback after provider success (operational risk)

---

## Operational integrity

### Execution correctness

| Control | Purpose |
|---------|---------|
| Execution lease | Reduce concurrent bulk runs on same campaign |
| Campaign idempotency key | Prevent duplicate recipient processing within same campaign |
| Retry fingerprint | Prevent duplicate retry campaign trees |
| Stale reconciliation | Reduce indefinite `running` ownership |

None of these provide **global** deduplication across retries, providers, or databases.

### Replay risks

| Scenario | Risk |
|----------|------|
| HTTP rollback after provider accept | Resend on manual retry without log row |
| Retry child campaign | New campaign id—may resend same partner by design |
| Provider transport retry | Outside RelayRuntime control |

Operators must use provider dashboards when DB and provider truth diverge.

### Duplicate execution risks

Concurrent operators, double-click retry, or race before lease insert may still produce duplicates at the edges. Multi-worker deployments require explicit validation.

---

## Credential handling

| Asset | Storage | Access |
|-------|---------|--------|
| Provider tokens | `whatsapp.config` DB fields | WhatsApp Manager write |
| Webhook secret field | DB | Manager; **no HTTP webhook shipped** |
| Optional log file | Filesystem path in settings | OS permissions |

**Never** commit tokens, `.env` files, or production dumps to the repository.

Issue reproduction must use **Mock Provider** when possible.

---

## Unsupported deployment modes

| Mode | Concern |
|------|---------|
| Public database manager | Full compromise |
| Shared Manager role with untrusted users | Token theft, arbitrary sends |
| `workers=0` under high parallel load | Race and timeout behavior |
| TLS termination misconfiguration | Session compromise |
| Secrets in VCS or backups without encryption | Credential leak |

---

## Provider consistency (non-guarantee)

RelayRuntime **does not** provide exactly-once delivery.

| Fact | Implication |
|------|-------------|
| Provider APIs are external to PostgreSQL | No atomic transaction with delivery |
| Single HTTP transaction per bulk | Rollback drops DB evidence of sends |
| No outbound idempotency tokens | Provider may duplicate independently |

See [docs/architecture/KNOWN_LIMITATIONS.md](docs/architecture/KNOWN_LIMITATIONS.md).

---

## Secure configuration

- Restrict **WhatsApp Manager** to administrators.
- Rotate tokens after suspected exposure.
- Cap campaign size vs `limit_time_real`.
- Protect backups and filestore.
- Stage with Mock Provider; production with Green API only after validation.

---

## Related documentation

- [Transaction model](docs/architecture/TRANSACTION_MODEL.md)
- [Runtime safety rules](docs/development/RUNTIME_SAFETY_RULES.md)
- [Failure scenarios](docs/operations/failure-scenarios.md)
- [Runbook](docs/operations/RUNBOOK.md)
