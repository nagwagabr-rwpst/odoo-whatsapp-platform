# RelayRuntime Phase 3 — Lazy Translation Boundary Fix

**Module:** `relayruntime` (Odoo 19)  
**Date:** 2026-05-31  
**Trigger:** `no translation language detected, skipping translation` during registry load after Phase 2/3 localization.

---

## 1. Problem

Phase 2 wrapped some **class-definition-time** strings with `_()`. At import/registry init there is no `env.lang`, so Odoo logs:

```text
no translation language detected, skipping translation
```

This is noisy during registry loading, module import, CLI bootstrap, and test startup. It does not break functionality but indicates incorrect translation boundary placement.

---

## 2. Audit results (Phase 2/3 `_()` at import time)

Full-module grep identified **exactly two** import-time `_()` usages introduced during localization prep:

| File | Line | Context | Phase |
|------|------|---------|-------|
| `views/models/whatsapp_bulk_campaign.py` | 262 | `models.Constraint(..., _('...'))` | Phase 2 |
| `wizard/whatsapp_bulk_send_wizard.py` | 31 | `fields.Many2many(..., help=_('...'))` | Phase 2 |

All other `_()` calls in `relayruntime` are inside **methods** (actions, computes at request time, services, wizards on button click, `UserError`/`ValidationError` raises) and correctly remain `_()`.

### Not import-time (keep `_()`)

Examples verified as runtime-only:

- `_compute_kanban_display_labels` — `_()` runs when compute executes with `env`
- `_compute_test_mode_display_labels` — same
- `action_*`, `create`, `write`, bulk service steps, provider validation raises
- Wizard `action_send`, notification dicts, safety utils checks

### Already correct (plain `str` at definition)

- `CAMPAIGN_STATE_SELECTION`, `DELIVERY_STATE_SELECTION`, `EXECUTION_STATE_SELECTION` — plain tuples on models
- `PROVIDER_STATUS_SELECTION`, `PROVIDER_SELECTION_LABELS` in `constants.py` — plain `str` (required for Odoo 19 selection reflection)
- Other `models.Constraint` messages in `whatsapp_message_log.py`, `whatsapp_bulk_execution.py`
- Other field `help=` strings across config/campaign models

---

## 3. Fix applied

Replaced import-time `_()` with **plain English `str` literals** (Odoo core pattern):

```python
# Constraint — whatsapp_bulk_campaign.py
_whatsapp_retry_fingerprint_unique = models.Constraint(
    'unique(parent_campaign_id, retry_fingerprint)',
    'A retry campaign for the same parent and recipient set already exists.',
)

# Field help — whatsapp_bulk_send_wizard.py
help=(
    'Select multiple files. Each file is sent in order with a short delay. '
    'Product catalog images stay on the Products tab and are never mixed with these uploads.'
),
```

**No PO file changes.** Strings unchanged; still exported in `relayruntime.pot` / translated via `ar.po`.

---

## 4. Why not `_lt()` for these two cases?

`_lt()` was evaluated per task spec but **breaks Odoo 19 registry init** for field metadata:

| Attempt | Result |
|---------|--------|
| `_()` at class body | Warning: `no translation language detected, skipping translation` |
| `_lt()` on `help=` | `NotImplementedError` in `LazyGettext.__eq__` during `ir.model.fields._reflect_fields` tuple comparison |
| `_lt()` on `Constraint` message | Same class of reflection issues; message not stored as `str` in `ir.model.constraint` |

Odoo 19 requires **`str`** for:

- `fields.*(help=...)` when reflected to `ir.model.fields`
- `Selection` list labels (`isinstance(label, str)` in `ir.model.fields.selection._reflect_selections`)
- `models.Constraint(..., message=...)` when persisted (non-`str` → stored as `None`)

**Approved lazy pattern for metadata:** plain literal at class definition; translation deferred to i18n load / UI render via standard export (`field help`, `constraint message` entries in `.pot`).

`_lt()` remains appropriate for **module-level constants** that are not compared during reflection (e.g. access error templates in `ir_model.py`) — not for field help or SQL constraint messages in addons.

---

## 5. Runtime vs import-time rules

| Use | Function | When |
|-----|----------|------|
| Field `string`, `help`, selection labels, constraint messages | Plain `str` | Class definition — export via `i18n export` |
| Module constants not tied to `fields.Selection` lists | `_lt()` optional | If not compared as non-str during reflection |
| `UserError`, `ValidationError`, notifications | `_()` | Inside methods with `env` / request context |
| Action `name`, dynamic `current_step`, computed display labels | `_()` | Inside methods when recordset/env available |
| Customer outbound catalog text | `_()` | At send time in service with caller context |
| **Runtime execution labels** (attachment summaries, log metadata built without UI) | Plain `str` (English) | Bulk/cron/worker paths — see §5.1 |
| Logger / traceback / provider raw errors | English literal | Never translate |

**Rule of thumb:** If the string is evaluated when Python **defines the class** (field args, constraint args), use plain `str`. If evaluated when a **method runs** during a request or cron job, use `_()` **only when** an active language context exists (interactive UI). Operational execution metadata stays English.

### 5.1 Runtime execution labels policy

**Operational runtime execution labels MUST remain deterministic English strings.**

This applies to values persisted or compared during bulk send, registry bootstrap, and tests **without** a guaranteed `env.lang` — for example `WhatsAppBulkSender._attachment_label()` in `whatsapp_bulk_service.py`.

| Label | Example | Why English only |
|-------|---------|------------------|
| Free attachments | `Files (%(count)s): %(names)s` | Written to `whatsapp.message.log.attachment_info`; must match across retries, idempotency, and log search |
| Product images | `Product images: %s` | Same; built during campaign loop, often before UI language is set |
| Product catalog | `Product Catalog: %s` | Same; distinguishes catalog vs image mode in execution audit trail |

**Why attachment summaries intentionally remain English**

1. **No language at call site** — `_attachment_label()` runs from bulk orchestration during test startup, `--stop-after-init`, and cron-style execution where Odoo logs `no translation language detected, skipping translation` if `_()` is used.
2. **Stable audit semantics** — `attachment_info` is operational metadata (what was sent), not end-user copy; English keeps logs, exports, and support tooling consistent.
3. **UI vs runtime split** — Wizard attachment summaries (`whatsapp_bulk_send_wizard.py`) may still use `_()` when the user is in an interactive form; the bulk **service** path is execution-boundary only.

Do **not** wrap these service-layer summary strings in `_()` during localization normalization.

---

## 6. Validation

| Check | Result |
|-------|--------|
| `py_compile` all `relayruntime/**/*.py` | Pass |
| `-u relayruntime --stop-after-init` | Pass |
| Translation bootstrap warnings | **None** (`NO_TRANSLATION_WARNINGS`) |
| Registry load | Pass (no `NotImplementedError`) |
| PO / terminology | Unchanged |
| Module tests (`--test-tags=/relayruntime`) | 5/6 pass (1 pre-existing failure unrelated to this fix) |

Re-verify after changes:

```bash
python odoo-bin --addons-path=...,whatsapp_simple \
  -c odoo.conf -d YOUR_DB -u relayruntime --stop-after-init --log-level=warn 2>&1 \
  | rg "no translation language|skipping translation"
```

Expected: no matches.

---

## 7. Files changed

| File | Change |
|------|--------|
| `relayruntime/views/models/whatsapp_bulk_campaign.py` | Constraint message: `_()` → plain `str` |
| `relayruntime/wizard/whatsapp_bulk_send_wizard.py` | Field `help`: `_()` → plain `str` |
| `relayruntime/services/whatsapp_bulk_service.py` | `_attachment_label()`: `_()` → plain English literals (runtime execution labels) |
| `docs/localization/PHASE3_LAZY_TRANSLATION_FIX.md` | This document |

**Not modified:** wizards (attachment summary `_()` kept for UI), menus, dashboard translations, `i18n/*.po`, `i18n/*.pot`.

---

## 8. Future localization guidelines

1. **Never** use `_()` in field definitions, constraint definitions, or module-level selection tuples assigned to `fields.Selection(selection=[...])`.
2. Prefer **plain English literals** for `string=`, `help=`, and `models.Constraint` messages; rely on `odoo-bin i18n export` + `ar.po`.
3. Use `_()` only inside callables that run with an Odoo environment **and** interactive language context (model methods, wizard actions). Exception: do **not** use `_()` for bulk-service execution metadata (`_attachment_label`, log fields built without UI).
4. Do **not** use `_lt()` on field `help` or constraint messages until Odoo reflection accepts `LazyGettext` (currently Odoo 19.0 does not).
5. For `constants.py` selection labels shown in UI: keep plain `str`; translate via selection entries in `.po`.
6. After adding translatable strings, re-export `.pot` and merge into `ar.po` — do not wrap metadata in `_()` to “help” export.
7. CI guard (recommended): grep for `help=_\(|Constraint\([^)]*_\(` in `relayruntime/` on PRs.

---

## 9. Related docs

- [LOCALIZATION_PLAN.md](./LOCALIZATION_PLAN.md) — dual-language policy
- [PHASE3_TRANSLATION_NOTES.md](./PHASE3_TRANSLATION_NOTES.md) — Arabic layer delivery
- [PHASE2_CHANGELOG.md](./PHASE2_CHANGELOG.md) — string export preparation

---

*Lazy translation boundary stabilized for bilingual registry loading.*
