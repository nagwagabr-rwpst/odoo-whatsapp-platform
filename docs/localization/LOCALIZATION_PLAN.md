# RelayRuntime Localization Plan (Phase 1)

**Module:** `relayruntime` (Odoo 19)  
**Version audited:** `19.0.6.0.0`  
**Languages target:** English (source) + Arabic (`ar`)  
**Status:** Documentation only — no code or `.po` changes in this phase.

---

## 1. Executive summary

RelayRuntime mixes **business-user UI** (campaigns, wizards, dashboards) with **runtime/observability surfaces** (executions, leases, idempotency, provider diagnostics). Phase 1 establishes a **dual-language policy**:

| Layer | Language policy |
|-------|-----------------|
| **User-facing UI** | Translatable via Odoo i18n (`_()`, field `string=`, XML `string=`) → Arabic for operators and sales teams |
| **Operational / runtime engineering** | Remain **English** in labels, logs, provider names, and diagnostic field names |
| **Hybrid** | Arabic (or translated) **label** + English **technical token** in help text or parentheses |

Blind translation of runtime terms would harm support, log correlation, and cross-team runbooks documented in English under `docs/operations/` and `docs/runtime/`.

---

## 2. Translation strategy

### 2.1 Odoo i18n mechanics (RelayRuntime)

- **Python:** `from odoo import _` and `from odoo.tools.translate import _` in services; wrap all user-visible exceptions and notifications.
- **Models:** `fields.*(string='...', help='...')` — Odoo exports these automatically.
- **Selection tuples:** Second element of `(value, 'Label')` is translatable when defined on the model; constants in `constants.py` and module-level lists need the same treatment in Phase 2.
- **XML:** `string=` on views, menus, buttons, filters, actions — exported by `odoo-bin ... -d DB --i18n-export=...`.
- **JS:** Only `campaign_monitor_kanban.js` exists; it has **no user-facing strings** (registry + reload interval only). Kanban template text is in **XML/QWeb**, not JS.
- **Manifest:** `name`, `summary`, `description` are translatable module metadata.

### 2.2 Dual-language rules

1. **Translate:** menus, wizard tabs, buttons, dashboards, campaign/delivery **status labels**, validation messages shown to end users, empty-state help, product catalog boilerplate sent to customers.
2. **Keep English:** `Execution UUID`, `Idempotency Key`, `API Message ID`, `Lease Token`, `Retry Fingerprint`, `Exception Type`, `Traceback Summary`, `API Response Body`, provider brand names (Green API, Meta Cloud, …), mock deterministic test numbers block, file log paths, constraint messages aimed at developers.
3. **Hybrid pattern (Phase 2):**  
   - Label: `مفتاح عدم التكرار`  
   - Help: `Idempotency Key — unique key per outbound message attempt (runtime).`

### 2.3 Locale and RTL

- Install Arabic (`ar`) on Odoo; set user preference or company language.
- Verify **RTL** on: bulk send wizard notebook, campaign monitor kanban, config form notebook, stat buttons.
- Campaign monitor uses inline English in kanban template (`processed`, `remaining`, `elapsed`) — must move to translatable QWeb or field formatters in Phase 2.

### 2.4 Outbound WhatsApp content

- **Catalog messages** (`build_catalog_message`) are **customer-facing** — translate template lines (`New Products Available:`, `Contact us for ordering.`) via `_()`.
- **User-typed message body** is not translated by the system.
- **Failure_reason / api_response** stored in logs: operational English (provider errors); optional future “user summary” field in Arabic.

### 2.5 Engineering logs

- `_logger.*` and `campaign_logger` / `attachment_logger` — **never translated** (English only, grep-friendly).

---

## 3. Terminology dictionary

Canonical English terms for productization. Arabic recommendations use **Modern Standard Arabic** suited to ERP operators; technical tokens stay Latin where noted.

| English (canonical) | Category | Arabic (UX label) | Notes |
|---------------------|----------|-------------------|-------|
| Campaign | User | حملة | Bulk send job |
| Bulk Campaign | User | حملة جماعية | Menu/action name |
| Execution | Hybrid | تنفيذ (Execution) | User sees progress; engineers say “execution attempt” |
| Execution Attempt | Hybrid | محاولة تنفيذ | Notebook tab |
| Execution UUID | Operational | Execution UUID | Do not translate label |
| Retry | User | إعادة المحاولة | Button / attempt kind |
| Retry Campaign | User | حملة إعادة محاولة | |
| Retry Fingerprint | Operational | Retry Fingerprint | |
| Delivery | User | تسليم | |
| Delivery State | User | حالة التسليم | |
| Message Log | User | سجل الرسائل | |
| Provider | Hybrid | مزود (Provider) | Type = English brand |
| Provider Status | User | حالة المزود | Values: Healthy / Degraded / Disconnected → translate |
| Attachment | User | مرفق | |
| Free Attachments | User | مرفقات مرفوعة | Distinct from product images |
| Product Catalog | User | كتالوج المنتجات | |
| Health | User | الصحة | Config group “Health” |
| Campaign Monitor | User | مراقبة الحملات | |
| Delivery Dashboard | User | لوحة التسليم | |
| Cooldown | User | فترة تهدئة | Anti-spam pause |
| Recipient | User | مستلم | |
| Contact | User | جهة اتصال | Odoo `res.partner` |
| Sent / Failed / Skipped | User | مُرسل / فشل / تم تخطيه | Status chips |
| Queued / Sending | User | في الانتظار / جاري الإرسال | |
| Completed with Errors | User | اكتمل مع أخطاء | |
| Reconciled | Operational | Reconciled | Internal execution state |
| Idempotency Key | Operational | Idempotency Key | |
| API Message ID | Operational | API Message ID | |
| Lease Token | Operational | Lease Token | |
| Observability | Hybrid | المراقبة (Observability) | Manager-only tab |
| Test Mode | User | وضع الاختبار | Mock provider |
| Settings | User | الإعدادات | |
| Sale Order | User | أمر بيع | Odoo standard |

### 3.1 Inconsistent terminology (fix in Phase 2)

| Issue | Locations | Recommendation |
|-------|-----------|----------------|
| **Contact** vs **Recipient** | Wizards use “Recipients”; models use `Current Recipient` / `Current Contact` | Standardize UI to **Recipient** (مستلم); keep `partner_id` string as **Contact** (جهة اتصال) per Odoo |
| **Message Logs** vs **Delivery Logs** | Menu “Message Logs”; view `WhatsApp Delivery Logs` | One term: **Message Logs** / سجل الرسائل |
| **Success** vs **Sent** | Fields `Success` / `Sent`, kanban “Sent” | Counters: **Sent**; rate: **Success Rate** |
| **Processing State** vs **State** | Campaign has both | User label: **Status**; engineering docs: `state` / `processing_state` |
| **Failures** vs **Failed** | `total_failures` / `failed_count` | Align labels to **Failed** |
| **Free Attachments** vs **Attachments** | Field vs group titles | Use **Attachments** in UI; “free” only in help |
| **WhatsApp** vs **RelayRuntime** | App menu still “WhatsApp”; module name RelayRuntime | Product decision: menu **WhatsApp** (channel) or **RelayRuntime** (product) |

---

## 4. Audit summary

### 4.1 Coverage statistics (approximate)

| Source | Translatable items | Wrapped / exportable | Gaps |
|--------|-------------------|----------------------|------|
| Python `_()` | ~55 user strings | Good in wizards, safety, config actions | ~15 provider/runtime strings without `_()` |
| Field `string` / `help` | ~120 | Auto-export | Some help is operational English only (OK) |
| Selection labels | ~35 values | On models + constants | `constants.py` provider list not using lazy translation |
| XML UI | ~150 strings | Exportable | Kanban inline English; config alert HTML |
| JS | 0 user strings | N/A | — |
| Security groups | ~8 | Exportable | — |
| Notifications | ~8 | `_()` in Python | — |

### 4.2 Classification matrix (by area)

#### A) User-facing → translate

- All **menus** (`whatsapp_menu.xml`, delivery dashboard menu).
- **Wizard** titles, tabs, buttons, placeholders, summary groups.
- **Actions** window names and empty-state help (campaign monitor, config).
- **Dashboard** counters, buttons (Sent/Failed/Skipped logs).
- **Campaign** form buttons: Retry, Open Monitor, Message Logs, Create Sale Order.
- **Filters:** Sent, Failed, Skipped, Running, With Errors, Today.
- **User errors:** phone required, select contacts, daily limit, attachment limits (shown in UI).
- **Notifications:** Message Sent, Bulk send finished, Connection Successful, Mock Provider Ready.
- **Product catalog** template lines in `whatsapp_product_service.py`.
- **Progress steps** shown in UI: Starting campaign, Sending to recipient, Finished, etc. (`_()` already).
- **Selection states** for campaign, delivery, wizard draft/done (user-visible badges).

#### B) Operational / runtime → keep English

- Field labels: `Execution UUID`, `Idempotency Key`, `API Message ID`, `Lease Token`, `Lease Expires`, `Last Heartbeat`, `Execution Token`, `Execution Lock Expires`, `Exception Type`, `Traceback Summary`, `API Response`, `API Response Body`, `Related Model`, `Related Record ID`, `Outbound Intent At`, `Provider Debug Info`, `Capabilities (JSON)`.
- **Provider type** display names: Green API, Meta WhatsApp Cloud API, Evolution API, etc.
- **Mock simulation** deterministic phone numbers help block (engineering reference).
- **Provider registry / stub** errors raised as `ProviderValidationError` without `_()` (often bubble to ValidationError with English `str(exc)`).
- **SQL constraint** messages on execution UUID and retry fingerprint (developer-facing).
- **Log file path** default `C:\Odoo19.0c\logs\whatsapp.log`.
- **Internal states:** `reconciled` (execution), legacy `processing_state` mapping.
- **Logger messages** throughout services.

#### C) Mixed / hybrid → translate label only

| UI label (translate) | Keep in help / value (English) |
|----------------------|--------------------------------|
| تنفيذ / Execution Attempt | `whatsapp.bulk.execution`, `execution_uuid` |
| حالة المزود | `healthy`, `degraded`, `disconnected` keys |
| مزود | `green_api`, `mock_provider`, … |
| المراقبة | Observability tab — file log, debug JSON |
| محاولة تنفيذ | `initial` / `retry` attempt_kind keys |
| إعادة المحاولة | Retry lineage docs link in help |

---

## 5. Detailed string inventory

### 5.1 Menus and actions

| English | File | Class | Arabic (proposed) |
|---------|------|-------|-------------------|
| WhatsApp | `whatsapp_menu.xml` | A | واتساب |
| Settings | menu | A | الإعدادات |
| Message Logs | menu | A | سجل الرسائل |
| Campaign Monitor | menu | A | مراقبة الحملات |
| Bulk Campaigns | menu | A | الحملات الجماعية |
| Delivery Dashboard | `whatsapp_delivery_dashboard_views.xml` | A | لوحة التسليم |
| Configure your WhatsApp provider | config action help | A | قم بإعداد مزود واتساب |
| No active campaigns | campaign monitor help | A | لا توجد حملات نشطة |

### 5.2 Buttons

| English | Arabic (proposed) |
|---------|-------------------|
| Send | إرسال |
| Cancel | إلغاء |
| Close | إغلاق |
| View Logs | عرض السجلات |
| Test Connection | اختبار الاتصال |
| Provider Self-Test | اختبار ذاتي للمزود |
| Retry Failed Recipients | إعادة المحاولة للمستلمين الفاشلين |
| Open Monitor | فتح المراقبة |
| Create Sale Order from Selection | إنشاء أمر بيع من الاختيار |
| Send WhatsApp | إرسال واتساب |
| WhatsApp Bulk Send | إرسال واتساب جماعي |
| Sent Logs / Failed Logs / Skipped Logs / All Logs | سجلات المرسلة / الفاشلة / المتخطاة / الكل |

### 5.3 Wizard tabs and groups

| English | Arabic (proposed) |
|---------|-------------------|
| Send WhatsApp (Bulk) | إرسال واتساب (جماعي) |
| Recipients | المستلمون |
| Message | الرسالة |
| Products | المنتجات |
| Attachments | المرفقات |
| Product Preview | معاينة المنتجات |
| Live Progress | التقدم المباشر |
| Campaign Summary | ملخص الحملة |
| Selected Products | المنتجات المختارة |

### 5.4 Status and selection values

**Campaign `state`:** Draft → مسودة; Running → قيد التشغيل; Completed → مكتمل; Completed with Errors → مكتمل مع أخطاء; Stopped → متوقف; Failed → فشل.

**Delivery `delivery_state`:** Queued → في الانتظار; Sending → جاري الإرسال; Sent → مُرسل; Delivered → تم التسليم; Failed → فشل; Skipped → تم تخطيه.

**Execution `state`:** (+ Reconciled → **English** label “Reconciled” for operators with technical role).

**Provider status:** Healthy → سليم; Degraded → متدهور; Disconnected → غير متصل.

**Attempt kind:** Initial → أولي; Retry → إعادة محاولة.

### 5.5 Notifications (already use `_()`)

| English | Arabic (proposed) |
|---------|-------------------|
| Message Sent | تم إرسال الرسالة |
| WhatsApp message was sent successfully. | تم إرسال رسالة واتساب بنجاح. |
| Bulk send finished: … | اكتمل الإرسال الجماعي: … |
| Connection Successful | الاتصال ناجح |
| Mock Provider Ready | مزود الاختبار جاهز |
| TEST MODE — no real WhatsApp messages… | وضع الاختبار — لن تُرسل رسائل حقيقية… |

### 5.6 Kanban template strings (NOT exportable today — Phase 2 fix)

Hardcoded in `whatsapp_campaign_monitor_views.xml` and `whatsapp_bulk_campaign_views.xml`:

- `elapsed`, `processed`, `remaining`, `Success:`, badge prefixes `Sent`, `Failed`, `Skipped`
- Icon `title="Current recipient"` / `Current product`

**Action:** Replace with `_()`-backed fields, `t-translation="off"` only for numbers, or use Odoo 19 translatable QWeb attributes.

---

## 6. Gaps and defects

### 6.1 Missing `_()` wrappers (operational — intentional or fix)

| String | File |
|--------|------|
| `ProviderValidationError('API URL is required...')` | `green_api_provider.py`, `base_provider.py`, `mock_provider.py` |
| `ProviderValidationError('Invalid provider type: %s')` | `provider_registry.py` |
| Stub provider messages | `stub_provider.py` |
| `'WhatsApp Product Selection'` action name | `whatsapp_message_log.py` (no `_`) |
| Constraint: `Execution UUID must be unique.` | `whatsapp_bulk_execution.py` |
| Constraint: `Duplicate message log idempotency key.` | `whatsapp_message_log.py` |

**Policy:** User-facing provider errors shown in UI should use `_()`; pure engineering validation may stay English but should pass through `ValidationError(_('...') % exc)` at config boundary (already done in `_check_provider_configuration`).

### 6.2 Hardcoded English in XML (non-exportable patterns)

- Kanban inline text (see §5.6).
- Config mock alert: `Mock Provider active.`, `No real WhatsApp messages are sent.`
- Ribbon: `TEST MODE - NO REAL MESSAGES`, `Archived`
- Bulk wizard `<p class="text-muted">` attachment instructions (long paragraph).

### 6.3 Duplicated labels

- “Message Logs” — menu, buttons, notebook tab, action returns (consistent ✓).
- “Send WhatsApp” — partner button, sale order, action binding (consistent ✓).
- “Create Sale Order from Selection” — log form + campaign form (duplicate string — reuse same translation entry).

### 6.4 `constants.py` provider list

`PROVIDER_SELECTION_LABELS` and `PROVIDER_STATUS_SELECTION` are imported into models — labels export **if** defined as module-level translatable in Phase 2 (`_lt` or move to model with `selection` method).

### 6.5 ValidationError field name leak

`whatsapp_config._check_mock_simulation_rates` uses `%(field)s` with **technical** `field_name` (e.g. `simulate_success_rate`) — operational; Phase 2 should map to human field label before translate.

---

## 7. Recommended Arabic UX wording (reference)

Use consistently across UI:

- **حملة** — campaign (not “حملة إعلانية” unless marketing context).
- **إرسال جماعي** — bulk send (wizard title alternative).
- **سجل الرسائل** — message logs (not “سجل التسليم” in menus).
- **إعادة المحاولة** — retry (verb/noun for button).
- **فترة تهدئة** — cooldown (prefer over “تبريد”).
- **مزود** — provider (with English brand following: «مزود Green API»).
- **وضع الاختبار** — test mode.
- **اكتمل مع أخطاء** — completed with errors (clearer than literal “مكتمل مع الأخطاء”).

**Customer catalog (outbound):**

- `New Products Available:` → `منتجات جديدة متوفرة:`
- `Contact us for ordering.` → `تواصلوا معنا للطلب.`

---

## 8. Localization risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Translating runtime field labels | Broken log/runbook alignment | Hybrid labels; English help |
| Arabic RTL on progress kanban | Layout overlap | Phase 2 UI QA with `ar` user |
| Long Arabic strings in buttons | Overflow on mobile kanban | Short labels; tooltips |
| Provider error `str(exc)` in English | Arabic users see mixed language | Map known errors to `_()` catalog |
| `current_step` stored translated | DB language lock-in | Store technical step codes + translate at display (Phase 3) |
| Catalog message language vs contact locale | Wrong language to end customer | Future: per-campaign locale field |
| Export missing kanban strings | Incomplete `ar.po` | Fix XML before export |
| `%` and plural in notifications | Arabic plural rules | Use `ngettext` where counts vary (Phase 2) |

---

## 9. Rollout plan

### Phase 1 (current) — Architecture & audit

- [x] Audit strings and classify A/B/C.
- [x] Terminology dictionary and Arabic UX proposals.
- [x] This document.

### Phase 2 — Code preparation (no `.po` yet)

1. Add `i18n/` folder placeholder in module manifest comment only when ready.
2. Fix non-exportable kanban/help strings (move to translatable patterns).
3. Wrap remaining user-visible `UserError`/`ValidationError` paths; keep operational errors English.
4. Introduce `selection` methods or `_()` on `constants.py` labels for provider **status** (not provider brand names).
5. Add hybrid `help=` text for operational fields (English technical description).
6. Resolve terminology inconsistencies (Contact/Recipient, Delivery Logs naming).
7. Map `simulate_*` validation to field `string` for Arabic errors.

### Phase 3 — Translation assets

1. `odoo-bin -c ... -d DB --i18n-export=relayruntime.pot --modules=relayruntime`
2. Create `i18n/ar.po`; professional review for ERP Arabic.
3. Load: `--i18n-import=... --language=ar`
4. Install `l10n` Arabic if needed for Odoo core RTL.

### Phase 4 — QA & productization

1. RTL screenshot matrix: config, bulk wizard, monitor, logs, dashboard.
2. Regression: observability grep on English log lines unchanged.
3. Operator acceptance: Arabic sales user + English DevOps on same DB.
4. Document in `docs/README.md` link to this plan.

### Phase 5 — Runtime extraction alignment

When `runtime/` is extracted, keep **operational vocabulary in English** in API contracts; localize only Odoo `relayruntime` addon UI.

---

## 10. File reference index

| Area | Primary files |
|------|----------------|
| Menus | `relayruntime/views/whatsapp_menu.xml` |
| Config UI | `relayruntime/views/whatsapp_config_views.xml`, `views/models/whatsapp_config.py` |
| Campaigns | `views/whatsapp_bulk_campaign_views.xml`, `views/models/whatsapp_bulk_campaign.py` |
| Executions | `views/models/whatsapp_bulk_execution.py` |
| Logs | `views/whatsapp_message_log_views.xml`, `views/models/whatsapp_message_log.py` |
| Monitor | `views/whatsapp_campaign_monitor_views.xml`, `static/src/js/campaign_monitor_kanban.js` |
| Dashboard | `views/whatsapp_delivery_dashboard_views.xml`, `views/models/whatsapp_delivery_dashboard.py` |
| Wizards | `wizard/*.py`, `wizard/*_views.xml` |
| Services | `services/whatsapp_*.py`, `services/providers/*` |
| Constants | `constants.py` |
| Security | `security/whatsapp_security.xml` |

---

## 11. Appendix: Python strings using `_()` (inventory)

<details>
<summary>User-facing Python strings (already wrapped)</summary>

- Campaign progress: Starting campaign, Recovered after interrupted execution, Finished, Sending to recipient, Preparing recipient, Sending message, Sending attachment/product image steps.
- Campaign actions: Message Logs, Sales Orders, Create Sale Order from Selection, Retry Campaign, retry errors.
- Bulk service: (attachments only), Text/Catalog/File/Product API error labels, No valid phone number.
- Wizards: phone/message validation, bulk summary notification, Message Logs action names.
- Safety: daily limit, empty campaign, duplicate phones, attachment validation suite.
- Config: connection test notifications, validation messages, get_active_config error.
- Partners/SO: Send WhatsApp, bulk send, phone field errors.
- Product service: catalog headers/footer, select products error.
- Provider registry: unknown/not implemented UserErrors (user-facing).

</details>

<details>
<summary>Python strings WITHOUT `_()` (review in Phase 2)</summary>

- `whatsapp_message_log.action_open_product_selection` → `'WhatsApp Product Selection'`
- Provider layer: `green_api_provider`, `base_provider`, `mock_provider`, `stub_provider`, `provider_registry.validate_provider_type`
- Model constraints (English technical messages)

</details>

---

*Document generated for RelayRuntime Phase 1 localization architecture. Next step: Phase 2 code preparation per §9.*
