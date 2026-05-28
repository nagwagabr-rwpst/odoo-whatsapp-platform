# Deployment Evolution

[← Documentation index](../README.md)

How RelayRuntime deployments are expected to mature—from single Odoo instance to optional standalone runtime service.

---

## Roadmap overview

| Phase | Topology | Status |
|-------|----------|--------|
| **Embedded** | Odoo app + PostgreSQL; bulk in HTTP worker | **Current** |
| **Scaled embedded** | Odoo multi-worker + tuned timeouts | Supported with validation |
| **Worker isolation** | Dedicated job workers / cron consumers | Planned |
| **Queue-backed** | Outbound queue + Odoo enqueue | Planned |
| **Runtime service** | Separate process/cluster | Planned |
| **Managed cloud** | Hosted runtime plane | Aspirational |

Each phase adds operational surface area; do not skip observability and recovery discipline.

---

## Phase comparison

| Aspect | Embedded | Runtime service (future) |
|--------|----------|---------------------------|
| Process | Odoo worker | Runtime + Odoo |
| Bulk trigger | HTTP wizard | API / queue |
| Failure domain | Request timeout | Consumer retry policies |
| Observability | Odoo logs | Logs + metrics API |
| Exactly-once | Not claimed | Still not claimed without ledger |

---

## Migration between phases

| Transition | Requirement |
|------------|-------------|
| Embedded → workers | Load test leases; set `limit_time_real` |
| Workers → queue | Dual-write or freeze campaigns during cutover |
| Queue → service | Freeze idempotency contract; version API |

No automated migrator exists today.

---

## Environment tiers

| Tier | Provider | Purpose |
|------|----------|---------|
| Dev | Mock | Fast iteration |
| Staging | Mock or sandbox API | Upgrade validation |
| Production | Live API | Customer traffic |

Never point staging DB at production provider tokens.

---

## Related

- [embedded-runtime.md](embedded-runtime.md)
- [future-runtime-service.md](future-runtime-service.md)
- [runtime-vision.md](../architecture/runtime-vision.md)
- [INSTALLATION.md](INSTALLATION.md)
