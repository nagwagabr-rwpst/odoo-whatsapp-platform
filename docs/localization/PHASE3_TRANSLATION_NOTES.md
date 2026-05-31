# RelayRuntime Phase 3 — Arabic Translation Notes

**Module:** `relayruntime` (Odoo 19)  
**Version:** `19.0.6.0.0`  
**Date:** 2026-05-31  
**Assets:** `relayruntime/i18n/relayruntime.pot`, `relayruntime/i18n/ar.po`

---

## 1. Summary

Phase 3 delivers the first production-grade bilingual operational UX layer for RelayRuntime:

| Asset | Entries | Notes |
|-------|---------|-------|
| `relayruntime.pot` | 384 translatable strings | Generated via standard Odoo export |
| `ar.po` | 384 strings | 296 Arabic UX translations + 88 intentional English fallbacks |

**Export command (validated on Windows / Odoo 19):**

```bash
python odoo-bin \
  --addons-path=server/odoo/addons,whatsapp_simple \
  i18n export \
  -c server/odoo.conf \
  -d <database_with_relayruntime> \
  --languages pot \
  -- relayruntime
```

**Import command:**

```bash
python odoo-bin \
  --addons-path=server/odoo/addons,whatsapp_simple \
  i18n loadlang -c server/odoo.conf -d <database> -l ar

python odoo-bin \
  --addons-path=server/odoo/addons,whatsapp_simple \
  i18n import -c server/odoo.conf -d <database> -l ar -w -- relayruntime/i18n/ar.po
```

Regeneration helper: `scripts/build_relayruntime_ar_po.py` (copies `pot` → `ar.po` with terminology map).

---

## 2. Export integrity validation

| Check | Result |
|-------|--------|
| Odoo `i18n export` completes | ✅ `relayruntime/i18n/relayruntime.pot` created |
| Entry count pot ↔ ar.po | ✅ 384 = 384 |
| UTF-8 encoding | ✅ `charset=UTF-8` in headers; Arabic glyphs verified |
| `polib.pofile()` parse | ✅ No malformed entries |
| Odoo `i18n import -l ar -w` | ✅ `translations are loaded successfully` |
| PO plural forms (Arabic) | ✅ `nplurals=6` header set |

---

## 3. Intentionally untranslated terms (English fallback)

Per `LOCALIZATION_PLAN.md` §2.2 — operational/runtime vocabulary stays **English** in UI labels (empty `msgstr` → Odoo shows `msgid`).

### 3.1 Runtime diagnostics & identity

| English (shown) | Rationale |
|-----------------|-----------|
| Execution UUID | Log/runbook correlation |
| Idempotency Key | Deduplication contract |
| API Message ID | Provider correlation |
| Lease Token / Lease Expires | Worker lease semantics |
| Retry Fingerprint | Retry lineage |
| Exception Type / Traceback Summary | Engineering triage |
| API Response / API Response Body | Raw provider payload |
| Related Model / Related Record ID | ORM introspection |
| Outbound Intent At | Runtime intent timestamp |
| Reconciled | Internal execution state |
| Processing State / Processing Duration (s) | Engineering field names |
| Last Heartbeat / Last Recipient Index | Liveness diagnostics |
| Execution Token / Execution Lock Expires | Lock coordination |
| Parent Execution / Active Execution | Execution graph |
| Log Count / Executor / Retryable | Observability internals |

### 3.2 API & provider identifiers

| English (shown) | Rationale |
|-----------------|-----------|
| API URL / Access Token / API Version | Credential keys |
| Instance ID / Phone Number ID / Business Account ID | Provider API fields |
| Webhook Secret | Integration secret |
| Capabilities (JSON) / Provider Debug Info | Raw debug surfaces |
| Provider Name / Provider Version / Provider Implemented | Adapter metadata |
| Green API, Meta WhatsApp Cloud API, Evolution API, UltraMsg, Twilio WhatsApp, Gupshup, Custom Internal API, Mock Provider (Test Mode) | Brand names |

### 3.3 Engineering-only messages

| English (shown) | Rationale |
|-----------------|-----------|
| Execution UUID must be unique. | SQL constraint |
| Duplicate message log idempotency key. | SQL constraint |
| Deterministic test numbers block (config help) | QA reference |
| `campaign_id` / `whatsapp_campaign_id` leaked labels | Technical field names |
| `https://api.green-api.com` placeholder | API endpoint example |
| Mock simulation config-flag diagnostics | Developer toggles |

**Count:** 88 entries with empty `msgstr` (by design).

---

## 4. Hybrid operational UX (Arabic label + English token)

| UI label (Arabic) | English token preserved in value/help |
|-------------------|---------------------------------------|
| مزود | `green_api`, provider brand in selection |
| حالة المزود | `healthy`, `degraded`, `disconnected` keys |
| محاولة تنفيذ | `execution_uuid`, execution notebook |
| المراقبة (Observability) | Log paths, JSON debug |
| API URL مطلوب لـ Green API. | Green API brand in sentence |
| اختر Green API … Mock Provider … | HTML help with brand names |

Translator comments in `ar.po` mark hybrid entries (`# hybrid UX: …`) and runtime keep-English labels (`# runtime: keep English label per LOCALIZATION_PLAN`).

---

## 5. Arabic terminology decisions

Canonical choices from `LOCALIZATION_PLAN.md` §3 and §7, applied consistently in `ar.po`:

| English | Arabic (UX) | Notes |
|---------|-------------|-------|
| Campaign | حملة | Not «حملة إعلانية» |
| Bulk Campaign(s) | حملة جماعية / الحملات الجماعية | Menu + model |
| Message Logs | سجل الرسائل | Single term everywhere |
| Delivery Dashboard | لوحة التسليم | |
| Campaign Monitor | مراقبة الحملات | |
| Recipient | مستلم | Wizard/tab standard |
| Contact | جهة اتصال | Odoo `partner_id` |
| Sent / Failed / Skipped | مُرسل / فشل / تم تخطيه | Counters & filters |
| Queued / Sending | في الانتظار / جاري الإرسال | |
| Completed with Errors | اكتمل مع أخطاء | |
| Retry | إعادة محاولة | Button + attempt kind |
| Cooldown | فترة تهدئة | Prefer over «تبريد» |
| Provider Status values | سليم / متدهور / غير متصل | Healthy / Degraded / Disconnected |
| Test Mode | وضع الاختبار | Ribbon + alerts |
| Settings | الإعدادات | |
| Sale Order | أمر بيع | Odoo standard |
| Success Rate | معدل النجاح | Distinct from Sent counter |
| Product Catalog | كتالوج المنتجات | Outbound catalog line |

**Customer-facing catalog (outbound WhatsApp):**

- `New Products Available:` → `منتجات جديدة متوفرة:`
- `Contact us for ordering.` → `تواصلوا معنا للطلب.`

---

## 6. RTL rendering concerns

| Surface | Risk | Mitigation / Phase 4 action |
|---------|------|------------------------------|
| Campaign monitor kanban | Badge + progress line direction | Kanban uses computed Arabic labels; numbers stay LTR via Odoo field widgets — **QA with `ar` user** |
| Bulk wizard notebook tabs | Tab order RTL | Standard Odoo RTL; verify on mobile |
| Config form notebook | Long Arabic help text wrap | Test Observability + Mock Simulation tabs |
| Stat buttons (Sent/Failed/Skipped) | Label overflow | Short Arabic labels chosen; tooltips if needed |
| Mixed Arabic + `%` / numbers in notifications | Bi-directional punctuation | Placeholders preserved (`%(sent)s`); verify «اكتمل الإرسال الجماعي» notification |
| HTML help (Green API / Mock Provider) | `<strong>` blocks in RTL | Render test in Settings empty-state help |
| Progress summary middle dot (`·`) | Neutral separator | Kept between Arabic fragments; monitor in RTL |

Odoo core RTL (`lang=ar`) required — install Arabic language pack if not present.

---

## 7. Pre-export fix (i18n-only, not runtime logic)

**File:** `relayruntime/constants.py`

Phase 2 used `_lt()` for `PROVIDER_STATUS_SELECTION`. Odoo 19 model reflection requires **plain `str`** selection labels (`ValidationError: non-str value/label in selection`). Labels were reverted to English strings; they remain exportable and translatable via `ar.po` selection entries (Healthy → سليم, etc.).

This change affects **i18n compatibility only** — no execution, lease, or provider behavior change.

---

## 8. Future localization risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| `current_step` stored translated at runtime | DB language lock-in if user language changes | Phase 4: store step codes + translate at display |
| Provider `str(exc)` in English inside Arabic UI | Mixed-language error toasts | Map known provider errors to `_()` catalog |
| Arabic plural in bulk summary | `%(...)s cooldown(s)` grammar | Consider `ngettext` in Phase 4 |
| Per-contact catalog locale | Wrong language to end customer | Future campaign locale field |
| Long Arabic button labels on mobile | Kanban/wizard overflow | Short labels + tooltips |
| Re-export after new strings | Drift from terminology map | Re-run export + `build_relayruntime_ar_po.py` + manual review |
| Operational field accidentally translated | Broken DevOps runbook alignment | Keep `KEEP_ENGLISH` set updated in build script |
| RTL regression on new views | Layout overlap | Phase 4 screenshot matrix |

---

## 9. Files touched in Phase 3

| Path | Purpose |
|------|---------|
| `relayruntime/i18n/relayruntime.pot` | Translation template (Odoo export) |
| `relayruntime/i18n/ar.po` | Arabic production translations |
| `relayruntime/constants.py` | Selection label str fix for Odoo 19 export |
| `scripts/build_relayruntime_ar_po.py` | Regenerate `ar.po` from `pot` + terminology map |
| `docs/localization/PHASE3_TRANSLATION_NOTES.md` | This document |

**Not modified:** runtime services, models logic, field names, views structure.

---

## 10. Phase 4 checklist (operator QA)

1. Set user language to Arabic (`ar`); verify WhatsApp app menu RTL.
2. Walk: Settings → Bulk Send wizard → Campaign Monitor → Message Logs → Delivery Dashboard.
3. Confirm **Execution UUID**, **Idempotency Key**, provider brands remain English.
4. Confirm menus/buttons show Arabic (إرسال، سجل الرسائل، مراقبة الحملات).
5. Trigger mock test-mode ribbon — verify «وضع الاختبار — لا رسائل حقيقية».
6. Re-run export after any new UI strings; diff `pot` and update `ar.po`.

---

*Phase 3 complete. See `LOCALIZATION_PLAN.md` for full architecture; `PHASE2_CHANGELOG.md` for string export preparation.*
