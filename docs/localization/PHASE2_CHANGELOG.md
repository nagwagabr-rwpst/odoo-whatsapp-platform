# Phase 2 Changelog — Arabic UX Layer (Code Preparation)

**Module:** `relayruntime`  
**Phase:** 2 — Stabilize translatable UI strings (no `.po` generation)  
**Date:** 2026-06-01  
**Reference:** [LOCALIZATION_PLAN.md](./LOCALIZATION_PLAN.md)

---

## Summary

Phase 2 prepares RelayRuntime for Arabic translation by wrapping user-facing Python strings with `_()`, moving kanban QWeb literals to computed translatable fields, normalizing product terminology, and keeping runtime/engineering diagnostics in English. No replay logic, field renames, or `.po` files were changed.

---

## Files changed

### Python — providers & services

| File | Change |
|------|--------|
| `relayruntime/constants.py` | `_lt()` on provider **status** labels (Healthy / Degraded / Disconnected) |
| `relayruntime/services/providers/green_api_provider.py` | `_()` on Green API config validation errors |
| `relayruntime/services/providers/base_provider.py` | `_()` on invalid recipient phone error |
| `relayruntime/services/providers/mock_provider.py` | `_()` on mock config validation; field `string` for rate labels; connection-test flag errors |
| `relayruntime/services/providers/stub_provider.py` | `_()` on not-implemented provider config error |
| `relayruntime/services/providers/provider_registry.py` | `_()` on invalid provider type |
| `relayruntime/services/whatsapp_bulk_service.py` | `_()` on attachment summary lines; **Product Catalog** label |

### Python — models & wizards

| File | Change |
|------|--------|
| `relayruntime/views/models/whatsapp_bulk_campaign.py` | Kanban display computed fields; terminology; `_()` retry constraint |
| `relayruntime/views/models/whatsapp_config.py` | Test-mode alert computed fields; mock rate validation uses field `string` |
| `relayruntime/views/models/whatsapp_message_log.py` | `_()` on product selection action name |
| `relayruntime/views/models/whatsapp_delivery_dashboard.py` | Model description → **Delivery Dashboard** |
| `relayruntime/wizard/whatsapp_bulk_send_wizard.py` | **Current Recipient**; attachment `help` with `_()`; **Product Catalog** label |
| `relayruntime/wizard/whatsapp_bulk_send_wizard_views.xml` | Removed duplicate hardcoded attachment paragraph (help on field) |

### XML — views

| File | Change |
|------|--------|
| `relayruntime/views/whatsapp_campaign_monitor_views.xml` | Kanban uses computed labels; monitor group **Status** |
| `relayruntime/views/whatsapp_bulk_campaign_views.xml` | Kanban badges / success rate via computed fields |
| `relayruntime/views/whatsapp_config_views.xml` | Test-mode alert via computed fields |
| `relayruntime/views/whatsapp_message_log_views.xml` | **Message Logs** / **Message Log** view titles |
| `relayruntime/views/whatsapp_delivery_dashboard_views.xml` | Form title **Delivery Dashboard** |

---

## Strings normalized (terminology)

| Before | After | Scope |
|--------|-------|-------|
| Free Attachments | Attachments | Campaign `attachment_ids` label |
| Success / Failures (related totals) | Sent / Failed | Campaign `total_success`, `total_failures` |
| State / Processing State | Status | Campaign `state`, `processing_state` user labels |
| Current Contact | Current Recipient | Bulk send wizard live progress |
| WhatsApp Delivery Logs / Log | Message Logs / Message Log | Log list, form, search views |
| WhatsApp Delivery Dashboard | Delivery Dashboard | Dashboard form & model description |
| Products (catalog) | Product Catalog | Attachment summary in bulk service & wizard |
| Kanban: elapsed, processed, remaining, Sent, Failed, Skipped, Success: | Computed `_()` fields | Campaign monitor & bulk kanban |

### Canonical terms retained (per plan)

- **Recipient** — wizards, monitor kanban, send errors  
- **Contact** — `partner_id` on logs (Odoo standard)  
- **Campaign**, **Delivery**, **Message Log**, **Retry**, **Provider**, **Attachment**, **Product Catalog**  
- **Execution UUID**, **Idempotency Key**, **API Message ID**, provider brands — English, unchanged  

---

## Terminology decisions

1. **Recipient vs Contact** — UI progress and kanban use *Recipient*; `res.partner` fields remain *Contact*.  
2. **Message Logs** — Single menu term; removed “Delivery Logs” from view `string` attributes.  
3. **Sent vs Success** — Counters labeled *Sent*; rate field remains *Success Rate %* (metric, not counter).  
4. **Status** — User-visible campaign `state` / `processing_state` labels; technical field names unchanged.  
5. **Product Catalog** — Replaces informal “Products (catalog)” in attachment summaries.  
6. **Provider status** — `Healthy` / `Degraded` / `Disconnected` use `_lt()` for export; provider **brand** names stay English.  

---

## Python `_()` additions (user-facing)

- Green API: API URL, Instance ID, Access Token required  
- Base provider: invalid recipient phone  
- Mock provider: simulation rates, latency, attachment failure rate, disconnect/auth flags  
- Stub provider: not implemented configuration message  
- Provider registry: invalid provider type  
- Bulk service: file/product attachment summary strings  
- Message log: `WhatsApp Product Selection` action  
- Campaign: retry fingerprint constraint message  

### Left in English (operational / engineering)

- SQL constraints: Execution UUID uniqueness, idempotency key duplicate  
- Mock simulated API `failure_reason` strings (logs)  
- Stub `ProviderNotImplementedError` for connection/send/media (internal API)  
- Base provider: templates, delivery status, media upload, webhooks not supported  
- Green API connection fallback `'Connection test failed'` (wrapped upstream in service)  
- Logger messages, mock deterministic phone help block, file log paths  
- `current_step` still stored with `_()` at write time (Phase 3: technical step codes)  

---

## XML / kanban refactor

Hardcoded QWeb in campaign kanban templates replaced with computed `Char` fields on `whatsapp.bulk.campaign`:

- `monitor_elapsed_suffix`, `monitor_progress_summary`, `monitor_success_rate_text`  
- `kanban_label_sent`, `kanban_label_failed`, `kanban_label_skipped`  
- `kanban_label_current_recipient`, `kanban_label_current_product`  

Config test-mode alert body uses `test_mode_alert_title` / `test_mode_alert_body` (Python `_()`). Ribbon `TEST MODE - NO REAL MESSAGES` remains view `title` (exports via standard view i18n).

---

## Translator comments added

| Location | Comment |
|----------|---------|
| `whatsapp_bulk_campaign._compute_kanban_display_labels` | Suffix after running duration on monitor kanban |
| Same | Success rate line; `%%` for literal percent |
| `whatsapp_bulk_service._attachment_label` | Product Catalog line in attachment summary |
| `whatsapp_config._compute_test_mode_display_labels` | Mock provider alert copy |

---

## Validation

| Check | Result |
|-------|--------|
| `py_compile` (all `relayruntime/**/*.py`) | Pass |
| XML well-formed (`*.xml`) | Pass (12 files) |
| Registry / JS | Not run (requires live Odoo instance); no JS user strings changed |
| `.po` generation | **Not performed** (Phase 3) |

---

## Unresolved translation risks (Phase 3+)

| Risk | Notes |
|------|-------|
| `current_step` stored translated at write | DB language lock-in; migrate to technical codes + display translation |
| Provider errors via `% exc` | Config boundary still embeds English `ProviderValidationError` text for unknown errors |
| Mock connection `raw_response['message']` | English operational payload; UI notification text is separately translated |
| RTL on kanban badges | Arabic label length may overflow mobile cards — QA with `ar` user |
| Config mock deterministic numbers block | Engineering reference; intentionally English |
| App menu “WhatsApp” vs “RelayRuntime” | Product decision deferred (Phase 1 §3.1) |
| `ngettext` for bulk notification counts | Bulk summary uses `_()`; plural rules not yet applied |
| Catalog message per-contact locale | No per-campaign locale field yet |
| Ribbon `TEST MODE - NO REAL MESSAGES` | View-arch export only (not Python `_()`) |

---

## Suggested commit groups (not committed)

1. **i18n: provider validation and constants** — `constants.py`, `services/providers/*`  
2. **i18n: models terminology and kanban display fields** — `whatsapp_bulk_campaign.py`, `whatsapp_config.py`, `whatsapp_message_log.py`, `whatsapp_delivery_dashboard.py`  
3. **i18n: bulk service and wizard** — `whatsapp_bulk_service.py`, `whatsapp_bulk_send_wizard.py`  
4. **i18n: views (kanban, logs, config, dashboard)** — `views/*.xml`, `wizard/*_views.xml`  
5. **docs: Phase 2 changelog** — `docs/localization/PHASE2_CHANGELOG.md`  

---

*Next step: Phase 3 — `odoo-bin --i18n-export` and `ar.po` professional review per LOCALIZATION_PLAN §9.*
