# Reconstruction Ownership Matrix

**Contract:** MERGE-003  
**Foundation:** Lineage B `63975c4`  
**UI source:** Lineage A `2188035`  
**Branch:** `reconstruct/unify-ui-on-runtime`

## B-LOCK (preserve — no A overwrite)

| Path / feature | Notes |
|----------------|-------|
| `relayruntime/views/models/whatsapp_bulk_execution.py` | Lease, heartbeat, UUID |
| Campaign execution FKs / lock fields in `whatsapp_bulk_campaign.py` | `active_execution_id`, tokens |
| Idempotency + outbound intent in `whatsapp_message_log.py` | Unique key, `commit_outbound_intent` |
| `relayruntime/services/whatsapp_bulk_service.py` | Runtime send path |
| `relayruntime/services/providers/*` (B versions) | Absolute imports, i18n |
| `relayruntime/constants.py` lease/heartbeat constants | `EXECUTION_*` |
| `runtime/**` stubs | No implementation during unify |

## A-IMPORT (copy into nested package; adapt)

| Source (A) | Destination (B package) |
|------------|-------------------------|
| `models/whatsapp_app_dashboard.py` | `relayruntime/views/models/whatsapp_app_dashboard.py` |
| `views/whatsapp_app_dashboard_views.xml` | `relayruntime/views/whatsapp_app_dashboard_views.xml` |
| `views/whatsapp_menu.xml` | `relayruntime/views/whatsapp_menu.xml` |
| Dashboard ACL rows | Merge into `relayruntime/security/ir.model.access.csv` |
| `static/brand/*`, `static/logo/*`, brand SCSS, icons | `relayruntime/static/...` |
| Wizard menu actions `action_whatsapp_send_message`, `action_whatsapp_new_bulk_send` | Prepend to existing B wizard XML (keep B form arches) |

## UNION / REDESIGN

| Artifact | Rule |
|----------|------|
| `ir.model.access.csv` | Keep execution* + add app.dashboard* |
| `__manifest__.py` | B version line → `19.0.6.1.0`; A brand/assets/data |

## MANUAL (UX-only diffs)

Wizard form chrome, campaign/delivery/monitor polish — must not remove B fields or runtime labels.

## REGEN

`relayruntime/i18n/*.po|*.pot` after UI import (A has no i18n).

## Layout contract

All installable addon code lives under `relayruntime/`. Repository root remains packaging/docs/runtime stubs only. Flat A layout is forbidden on this branch.
