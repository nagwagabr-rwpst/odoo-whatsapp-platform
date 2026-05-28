# WhatsApp Simple — Architecture (legacy)

> **Superseded:** Use the canonical documentation index at [`docs/README.md`](README.md) and [`docs/architecture/SYSTEM_OVERVIEW.md`](architecture/SYSTEM_OVERVIEW.md).  
> This file is retained for backward compatibility. Some sections below are **outdated** (e.g. mid-loop `cr.commit()` — removed in 19.0.5.4+).

---

# WhatsApp Simple — Architecture

Odoo 19 Community module for WhatsApp outbound messaging via a provider-agnostic service layer (Green API adapter today).

## Layer overview

```
UI (wizards, views, menus)
    ↓
Models (campaign, log, config)
    ↓
Services (bulk, product, safety, WhatsAppService facade)
    ↓
Provider adapters (Green API, Meta Cloud, …)
    ↓
External WhatsApp REST APIs
```

See **`docs/PROVIDER_ARCHITECTURE.md`** for provider onboarding and adapter details.

| Layer | Responsibility |
|--------|----------------|
| **Models** | Persistence, access rules, actions (retry, monitor) |
| **Wizards** | User input validation, campaign creation |
| **Services** | Business logic, sequential sending, no ORM in loops where avoidable |
| **Logger** | `campaign_logger`, `api_logger`, `attachment_logger` + optional file |

## Campaign lifecycle

```
draft → running → completed | completed_with_errors | stopped | failed
```

| State | Meaning |
|--------|---------|
| `draft` | Created, not yet executing |
| `running` | Bulk sender active; progress fields updated with `cr.commit()` |
| `completed` | All recipients processed without failures |
| `completed_with_errors` | Finished; one or more failed/skipped |
| `stopped` | Interrupted (e.g. daily limit) |
| `failed` | Fatal error aborted the run |

**Live fields** (updated during `running`): `current_recipient_id`, `current_recipient_number`, `current_product_id`, `progress_percentage`, `processed_count`, `remaining_count`, `current_step`, `last_activity_at`.

**Timing**: `execution_started_at` / `execution_finished_at` (plus legacy `started_at` / `finished_at`).

## Bulk send flow

1. Wizard validates payload (message / attachments / products).
2. `whatsapp.bulk.campaign` record created with `partner_ids`, products, settings.
3. `WhatsAppBulkSender.send_to_partners()`:
   - Configures logging (`configure_whatsapp_logging`).
   - Validates safety (duplicates, MIME, limits, empty campaign).
   - Batch-reads partners and phone numbers once.
   - Caches attachment bytes per `ir.attachment` id.
   - For each recipient (sequential, randomized delay):
     - Updates campaign progress + commit.
     - Creates `whatsapp.message.log` (`sending` → `sent` / `failed` / `skipped`).
     - Sends text and/or attachments / product images.
     - Applies cooldown when configured.
4. Campaign `_mark_finished()` with final state.

No background queue, websocket, or multiprocessing — by design for Community stability (50–500 contacts).

## Logging flow

| Logger | Purpose |
|--------|---------|
| `odoo.addons.whatsapp_simple.campaign` | Campaign/recipient/cooldown lifecycle |
| `odoo.addons.whatsapp_simple.api` | HTTP requests/responses (sanitized payloads) |
| `odoo.addons.whatsapp_simple.attachment` | File uploads |

All loggers **propagate** to Odoo’s default log (`odoo.log`).

**Optional file** (Settings → Observability): rotating UTF-8 file at `file_log_path` (default `C:\Odoo19.0c\logs\whatsapp.log`). Does not replace root handlers.

## Failure tracking

Each `whatsapp.message.log` for a failed/skipped recipient may store:

- `exception_type`, `traceback_summary`
- `failure_reason`, `api_response_body`
- `failed_at`, `retryable`

## Retry flow

1. User opens completed campaign → **Retry Failed Recipients**.
2. New child campaign (`parent_campaign_id`) is created.
3. Partners from logs with `delivery_state` in `failed`, `skipped` are collected.
4. `WhatsAppBulkSender` runs the same message/product settings.
5. Original campaign history is preserved; retries appear in `retry_campaign_ids`.

## Provider abstraction

- **`WhatsAppService`**: Facade — resolves adapter via `ProviderRegistry`.
- **`GreenAPIProvider`**: Only Green API HTTP paths live here.
- **`WhatsAppSafetyValidator`**: Delays, limits, MIME, duplicates.
- **`WhatsAppProductService`**: Catalog text and product image attachments.
- **`WhatsAppBulkSender`**: Orchestration.

## Campaign Monitor UI

- Menu: **WhatsApp → Campaign Monitor**
- Kanban view `js_class="whatsapp_campaign_monitor_kanban"` reloads every 5s via standard OWL `model.root.load()` (no websocket).

## Future queue architecture (not implemented)

Planned extension points:

- Replace synchronous loop in `WhatsAppBulkSender` with job records + cron/worker.
- Push progress via bus/longpolling optional.
- Keep campaign/log models as source of truth; worker only calls existing service methods.

Current `cr.commit()` progress updates are compatible with a future queue (same fields).
