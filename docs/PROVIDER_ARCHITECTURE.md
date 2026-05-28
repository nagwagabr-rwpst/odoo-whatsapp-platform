# Provider Architecture

> **Note:** Adapter design in this document remains accurate. For execution attempts, transactions, and runtime flow, see [`docs/architecture/`](architecture/SYSTEM_OVERVIEW.md) and [`docs/runtime/`](runtime/EXECUTION_FLOW.md).

---

# Provider Architecture

`whatsapp_simple` uses a **provider adapter** pattern so campaigns, bulk sending, logs, and monitoring stay provider-independent.

## Directory layout

```
services/
  providers/
    base_provider.py       # Abstract contract
    provider_registry.py # Factory & capability lookup
    green_api_provider.py  # Production adapter
    meta_cloud_provider.py # Placeholder
    evolution_provider.py
    ultramsg_provider.py
    stub_provider.py       # Twilio, Gupshup, Custom stubs
  exceptions/
    provider_errors.py     # Standardized errors
  webhook/
    webhook_router.py      # Future incoming message routing
  whatsapp_service.py      # Facade (business code uses this only)
```

## Lifecycle

1. **Configure** `whatsapp.config` with `provider_type` and credentials.
2. **Validate** on save via `provider.validate_configuration()`.
3. **Resolve** adapter: `ProviderRegistry.get_provider(config)`.
4. **Send** through `WhatsAppService` → `provider.send_text_message()` / `send_media_message()`.
5. **Normalize** responses to `WhatsAppProviderResponse` → `to_dict()` for legacy callers.

## Adapter flow

```
Wizard / BulkSender / Campaign
        ↓
   WhatsAppService (facade)
        ↓
   ProviderRegistry.get_provider(config)
        ↓
   GreenAPIProvider | MetaCloudProvider | …
        ↓
   HTTP / provider API
        ↓
   WhatsAppProviderResponse
```

## Response normalization

`WhatsAppProviderResponse` fields:

| Field | Purpose |
|--------|---------|
| `success` | Operation ok |
| `provider_message_id` | Provider-side message id |
| `delivery_state` | sent / failed |
| `raw_response` | Original JSON |
| `error_message` | Human-readable error |
| `retryable` | Safe to retry |
| `status_code` | HTTP status |
| `provider_request_id` | Correlation id in logs |

## Capability system

Each adapter declares `WhatsAppProviderCapabilities`:

- `supports_media`
- `supports_templates`
- `supports_delivery_tracking`
- `supports_webhooks`
- `supports_bulk`
- `supports_catalogs`

Stored on config as `provider_capabilities_json`. UI and services can call `service.supports_feature('supports_media')`.

## Exception mapping

| Exception | Typical cause |
|-----------|----------------|
| `ProviderConnectionError` | Timeout, network |
| `ProviderAuthenticationError` | 401 / 403 |
| `ProviderRateLimitError` | 429 |
| `ProviderValidationError` | Bad config / phone |
| `ProviderTemporaryFailure` | 5xx |

Providers map HTTP/errors in `parse_error()` / `map_exception()`.

## Onboarding a new provider

1. Subclass `BaseWhatsAppProvider` (or copy `GreenAPIProvider`).
2. Set `provider_type`, `is_implemented = True`, `capabilities`.
3. Implement `validate_configuration`, `test_connection`, `send_text_message`, `send_media_message`.
4. Register in `PROVIDER_REGISTRY` in `provider_registry.py`.
5. Add selection label to `PROVIDER_SELECTION_LABELS`.
6. Add config view visibility rules for provider-specific fields.
7. (Optional) Add `BaseWhatsAppWebhookHandler` and register in `WhatsAppWebhookRouter`.

## Multi-provider future

Prepared on `whatsapp.config`:

- `company_id` — one active config per company
- `fallback_config_id` — reserved for failover (not wired)
- Per-company provider via separate config records

No Celery/Redis/queues — compatible with Odoo 19 Community workers and current sequential bulk sender.

## Logging

| Logger | File (optional) |
|--------|------------------|
| `provider_api` | `logs/provider_api.log` |
| `campaign` | `logs/whatsapp.log` |
| `failures` | `logs/failures.log` |

Every provider request logs `provider_type` and `request_id`.

## Mock Provider (`mock_provider`)

Fully implemented internal testing adapter — **no HTTP, no real messages**.

Configure weighted random outcomes on `whatsapp.config` (Mock Simulation tab). Logs use `[MOCK]` prefix.

| Number (normalized) | Forced outcome |
|---------------------|----------------|
| `201000000000` | Invalid number |
| `201111111111` | Auth failure (401) |
| `201222222222` | Disconnect (503) |
| `201333333333` | Timeout (408) |
| `201444444444` | Rate limit (429) |
| `201555555555` | Malformed response |
| `201666666666` | Attachment failure |

Ideal for QA, demos, 1000+ recipient stress tests, retry/monitor/analytics validation.

## Webhooks (skeleton only)

`WhatsAppWebhookRouter.route()` dispatches to registered handlers when controllers are added. Signature verification hooks live on `BaseWhatsAppWebhookHandler`.

Incoming messaging is **not** implemented in this version.
