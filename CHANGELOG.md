# Changelog

All notable changes to the `relayruntime` module are documented in this file.

## [19.0.5.0.0] - 2026-05-19

### Added — Mock Provider (internal testing)

- **`mock_provider`** — full simulated adapter (not a stub): success, failure, timeout, rate limit, attachment failures
- Configurable weighted rates: success, failure, timeout, rate limit, attachment failure
- **`simulated_latency_ms`** for performance / stress testing without external API
- Deterministic magic test numbers (documented in Settings → Mock Simulation)
- UI: **TEST MODE - NO REAL MESSAGES** ribbon and warning banner
- Logs prefixed with `[MOCK]` for simulated outcomes

### Use cases

- QA, demos, automated tests, bulk campaign stress tests (1000+ recipients), retry/monitor/analytics validation

## [19.0.4.0.0] - 2026-05-19

### Added — Provider-agnostic architecture

> Odoo 19.0 requires module versions in the `19.0.x` series (`19.1.x` is rejected at load time).
> This release is the provider-architecture milestone (requested as 19.1.0.0.0 semantically).

- **Provider adapter layer** under `services/providers/`:
  - `BaseWhatsAppProvider` abstract contract
  - `ProviderRegistry` factory
  - `GreenAPIProvider` (full implementation — existing behavior preserved)
  - Placeholder adapters: Meta Cloud, Evolution, UltraMsg, Twilio, Gupshup, Custom
- **Normalized** `WhatsAppProviderResponse` and standardized exception hierarchy
- **Config refactor**: `provider_type`, capabilities JSON, health monitoring, provider-specific credential fields
- **Webhook skeleton**: `services/webhook/` router and base handler (no controllers yet)
- **Provider-aware logging**: `provider_api`, `failures` loggers + optional `provider_api.log` / `failures.log`
- **Documentation**: `docs/PROVIDER_ARCHITECTURE.md`

### Changed

- `WhatsAppService` is now a facade over `ProviderRegistry` — no Green API code outside `green_api_provider.py`
- Settings UI: provider selector, capabilities tab, health status, dynamic credential fields
- Business services (bulk, single send, retry, monitor) unchanged in behavior; call facade only

## [19.0.3.0.0] - 2026-05-19

### Added — Stabilization and observability

- **Campaign execution states**: `draft`, `running`, `completed`, `completed_with_errors`, `stopped`, `failed`
- **Live progress fields**: `current_recipient_id`, `current_recipient_number`, `current_product_id`, `progress_percentage`, `processed_count`, `remaining_count`, `current_step`, `last_activity_at`, `execution_started_at`, `execution_finished_at`
- **Campaign Monitor** menu with auto-refreshing kanban (5s, no websocket)
- **Dedicated loggers**: `services/logger.py` (`campaign_logger`, `api_logger`, `attachment_logger`)
- **Optional rotating log file** via Settings (`file_log_enabled`, `file_log_path`)
- **Enhanced failure tracking** on message logs: `exception_type`, `traceback_summary`, `api_response_body`, `failed_at`, `retryable`
- **Retry Failed Recipients** action (linked child campaigns, preserves history)
- **Bulk safety**: empty campaign, duplicate phones, MIME validation, product image checks
- **Performance**: batch partner reads, attachment byte cache, reduced decode in loops
- **Internal docs**: `docs/ARCHITECTURE.md`

### Changed

- Bulk sender uses structured logging for all lifecycle events
- Campaign records store `partner_ids` for retry context
- User group may create/write campaigns during bulk send

## [19.0.2.0.0] - 2026-05-18

### Added — Sales workflow and delivery tracking

- **Historical delivery tracking** on `whatsapp.message.log`:
  - `delivery_state` (queued, sending, sent, delivered, failed, skipped)
  - `recipient_number`, `message_preview`, `attachment_count`, `sent_at`
  - `failure_reason`, `api_message_id`, `processing_duration`
  - Graph and pivot views; enhanced search filters and grouping
- **Delivery Dashboard** with sent / failed / skipped counters and success rate
- **Contacts list header button** “WhatsApp Bulk Send” (plus existing Action menu)
- **Product-based bulk sending**:
  - Select `product.template` records in bulk wizard
  - Auto-generated catalog message (name, price, reference, optional description)
  - “Use Product Images” sends catalog text then each product image with caption
- **Product selection wizard** to manually record customer choices and **create draft sale orders**
- **Campaign analytics**: `started_at`, `finished_at`, `duration_seconds`, `success_rate`, kanban/graph/pivot views
- **Live progress** on campaign and bulk wizard (`progress_percent`, current contact/product)
- New service: `whatsapp_product_service.py`

### Changed

- `sale.order` extended with `whatsapp_campaign_id` and `whatsapp_log_id`
- Bulk sender refactored for product sends, detailed logs, and progress commits
- Module depends on `product`
- Legacy `status` field kept (computed from `delivery_state`) for compatibility

## [19.0.1.2.0] - 2026-05-18

### Added — Safety and anti-spam

- Configurable random delays, cooldowns, daily limits, attachment limits
- `whatsapp_safety_utils.py` and `whatsapp_phone_utils.py` (Egyptian number normalization)

## [19.0.1.1.0] - 2026-05-18

### Added — Bulk messaging

- Bulk send wizard, campaigns, sequential sender, message logs

## [19.0.1.0.0] - 2026-05-18

### Added — Initial release

- WhatsApp configuration, single send, Green API service layer
