# RELEASE-019 — Final Verification

**Date:** 2026-08-02  
**Branch:** `19.0`  
**Module:** `relayruntime`  
**Module version:** `19.0.6.1.0`  
**Status:** PASS — marketplace package ready for Odoo Apps publication

Verification only. Branding, screenshots, landing page, README, and module version were not modified.

---

## 1. Website verification

| URL | Check | Result |
|-----|-------|--------|
| https://relayruntime.rwpst.com | HTTP 200, `text/html` | PASS |
| https://relayruntime.rwpst.com/#demo | Page loads; `id="demo"` section present | PASS |
| https://relayruntime.rwpst.com/all_end.mp4 | HTTP 200, `video/mp4` (~34 MB) | PASS |

Landing page layout and branding were not modified in this release.

---

## 2. Demo verification

| Check | Result |
|-------|--------|
| `#demo` anchor exists on live site | PASS |
| Demo video `all_end.mp4` served and playable path resolves | PASS |
| Marketplace CTA “Watch Product Demo” → `https://relayruntime.rwpst.com/#demo` | PASS |

---

## 3. Marketplace verification

**File:** `relayruntime/static/description/index.html`

| Check | Result |
|-------|--------|
| Final commercial Apps description | PASS |
| Version callout `19.0.6.1.0` | PASS |
| Overview / enterprise capabilities / features | PASS |
| Supported providers (Green API + Mock Provider) | PASS |
| Screenshots section present (unchanged assets) | PASS |
| No GitHub / Repository / README / SECURITY / MIGRATION / Issue tracker links | PASS |

**Manifest:** `relayruntime/__manifest__.py`

| Field | Expected | Actual | Result |
|-------|----------|--------|--------|
| `website` | `https://relayruntime.rwpst.com` | `https://relayruntime.rwpst.com` | PASS |
| `version` | unchanged `19.0.6.1.0` | `19.0.6.1.0` | PASS |
| GitHub URLs | none | none | PASS |
| Repository URLs | none | none | PASS |
| Customer-facing MIGRATION / README refs | none | none | PASS |

---

## 4. Commercial links verification

| Surface | Label | Target | Result |
|---------|-------|--------|--------|
| Apps description | Watch Product Demo | https://relayruntime.rwpst.com/#demo | PASS |
| Apps description | Visit Official Website | https://relayruntime.rwpst.com | PASS |
| Manifest | `website` | https://relayruntime.rwpst.com | PASS |

---

## 5. Final commercial audit

Scoped to **Odoo Apps / marketplace customer surfaces**:

- `relayruntime/static/description/index.html`
- `relayruntime/__manifest__.py` customer metadata (`website`, `description`, URLs)

| Forbidden public reference | Marketplace surfaces | Result |
|----------------------------|----------------------|--------|
| GitHub | none | PASS |
| Repository | none in customer fields | PASS |
| README | none | PASS |
| SECURITY | none as docs/links (ACL data paths only) | PASS |
| MIGRATION | none | PASS |
| Issue tracker | none | PASS |

**Note (out of modification scope):** the currently deployed product website HTML still contains legacy GitHub / github.io footer and Open Graph URLs. Per RELEASE-019 rules the landing page was not modified. Marketplace package surfaces are clean.

---

## 6. Final release checklist

- [x] Commercial Apps description verified (`static/description/index.html`)
- [x] Watch Product Demo link verified
- [x] Official Website link verified
- [x] `__manifest__.py` website = `https://relayruntime.rwpst.com`
- [x] Module version unchanged (`19.0.6.1.0`)
- [x] No GitHub / Repository URLs in marketplace metadata
- [x] Live site, `#demo`, and `all_end.mp4` verified online
- [x] Commercial audit of marketplace surfaces: PASS
- [x] Branding / screenshots / landing page / README / version left untouched
- [x] Repository prepared for Odoo Apps publication (marketplace package)

**Verdict:** READY for Odoo Apps marketplace synchronization.
