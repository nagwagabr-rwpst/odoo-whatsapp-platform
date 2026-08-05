# RELEASE-020 — Odoo Apps SEO & Discoverability Report

**Date:** 2026-08-05  
**Module:** `relayruntime` (technical name unchanged)  
**Commercial title:** RelayRuntime – Enterprise WhatsApp Messaging for Odoo Community  
**Version / license:** `19.0.6.1.0` / LGPL-3 (unchanged)

---

## 1. Current keyword coverage (before)

| Keyword / intent | Manifest name | Manifest summary | Marketplace description | Landing hero | Banner |
|------------------|---------------|------------------|-------------------------|--------------|--------|
| WhatsApp | Weak (legacy note only) | Missing | Sparse | Meta keywords only | Missing |
| WhatsApp Messaging | Missing | Missing | Sparse | Missing | Missing |
| Messaging | Weak (“messaging runtime”) | Weak | Weak | Weak | Weak |
| Bulk Message / Bulk Messaging | Missing | Missing | Weak (“Bulk send”) | Feature card only | Missing |
| Campaign / Campaigns | Weak | Missing | Weak | Later sections | Missing |
| Odoo Community | Weak | Missing | Present | Present | “Community Edition” |

**Problem:** Discoverability relied on brand/runtime language (“Enterprise Messaging Runtime”) instead of buyer search terms used on Odoo Apps (WhatsApp, Bulk Messaging, Campaign).

---

## 2. New keyword coverage (after)

| Keyword / intent | Manifest name | Manifest summary | Marketplace description (first section) | Landing hero | Banner |
|------------------|---------------|------------------|------------------------------------------|--------------|--------|
| WhatsApp | ✔ | ✔ | ✔ | ✔ | ✔ |
| WhatsApp Messaging | ✔ | ✔ | ✔ | ✔ | ✔ |
| Messaging | ✔ | ✔ | ✔ | ✔ | ✔ |
| Bulk Messaging | ✔ | ✔ | ✔ | ✔ | ✔ |
| Campaign / Campaigns | ✔ | ✔ | ✔ | ✔ | ✔ |
| Campaign Management | — | — | ✔ | ✔ | ✔ |
| Delivery Dashboard | — | ✔ (delivery tracking) | ✔ | ✔ | ✔ |
| Message Queue | — | — | ✔ | ✔ | ✔ |
| Retry | — | — | ✔ | ✔ | — |
| Templates / Notifications | — | — | ✔ | — | — |
| Multi Provider | — | ✔ | ✔ | ✔ | ✔ |
| Meta Cloud API | — | — | ✔ | meta/description | ✔ |
| Evolution API | — | — | ✔ | meta/description | ✔ |
| Green API | — | — | ✔ | meta/description | ✔ |
| Odoo Community | ✔ | ✔ | ✔ | ✔ | ✔ |
| Enterprise WhatsApp Messaging | ✔ | ✔ | ✔ | ✔ | ✔ |

Natural phrasing used; no comma-separated keyword stuffing blocks.

---

## 3. Files modified

| File | Change |
|------|--------|
| `relayruntime/__manifest__.py` | Commercial `name`, SEO `summary`, marketplace `description` feature set |
| `relayruntime/static/description/index.html` | Overview, features, providers, screenshot captions, CTAs |
| `relayruntime/static/description/banner_1.png` | First store visual rewritten for WhatsApp / Campaigns / Bulk / Delivery / Runtime |
| `relayruntime/static/description/screenshots/README.md` | Caption / first-visual guidance |
| `landing-page/index.html` | Title, meta, OG/Twitter, JSON-LD, hero copy, demo lead, hero alt |
| `landing-page/assets/banner_1.png` | Synced with marketplace banner |
| `launch/DEMO_SCRIPT.md` | Opening + closing on-screen titles |
| `launch/SHOT_LIST.md` | Opening on-screen text |
| `docs/releases/RELEASE-020_SEO_REPORT.md` | This report |

**Unchanged by design:** technical module name (`relayruntime`), version `19.0.6.1.0`, license `LGPL-3`, demo video re-record (`all_end.mp4`).

---

## 4. Expected search improvements

| Buyer search | Expected effect |
|--------------|-----------------|
| WhatsApp | Title + summary + first description paragraph now index the term for Apps listing text |
| WhatsApp Messaging | Commercial title and hero/banner phrase match primary product category |
| Messaging | Reinforced via “Enterprise WhatsApp Messaging” and platform summary |
| Bulk Message / Bulk Messaging | Explicit in summary, feature bullets, hero, banner badges |
| Campaign | Explicit in summary, Campaign Management copy, screenshots captions, banner |
| Adjacent Ops terms (Delivery Dashboard, Queue, Retry, Templates, Multi Provider, Meta/Evolution/Green) | Strengthens long-tail Apps page relevance once crawlers/reindex pick up listing HTML |

**Caveat:** Odoo Apps search ranking is opaque and may lag until the listing is re-published / reindexed. Text SEO cannot alone guarantee top rank against established competitors.

---

## 5. Remaining manual actions

1. **Demo video title cards:** Update opening + closing burned-in titles in `landing-page/all_end.mp4` (and any Apps upload copy) to **Enterprise WhatsApp Messaging for Odoo Community** without re-recording scenes. Source of truth updated in `launch/DEMO_SCRIPT.md`.
2. **Odoo Apps republish:** Upload/update the Apps listing so new `name` / `summary` / `description` / `banner_1.png` / screenshots captions go live.
3. **Optional UI recapture:** Product UI subtitle still reads “Operational Messaging Runtime for Odoo” inside PNGs; captions/banner now carry SEO load. Recapture only if Apps reviewers require in-image copy alignment.
