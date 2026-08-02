# RELEASE-016 — Final Demo Integration Report

**Status:** Complete  
**Date:** 2026-08-02  
**Official demo asset:** `landing-page/all_end.mp4` (unchanged)

---

## Summary

The official RelayRuntime product demo (`all_end.mp4`) is embedded in the landing page and the Odoo Apps description. The file was not renamed, moved, recompressed, or duplicated.

---

## 1. Landing Page

| Item | Detail |
|------|--------|
| File | `landing-page/index.html` |
| Section title | **Watch RelayRuntime in Action** |
| Anchor | `#demo` |
| Placement | Immediately after **Key Features** (`#features`), before **Operational Command Center** |
| Video source | `all_end.mp4` (same directory — relative path) |
| Poster | `assets/banner_1.png` (existing brand hero visual) |
| Markup | Responsive HTML5 `<video>` with `controls`, `preload="metadata"`, `loading="lazy"`, `playsinline` |
| Frame | Existing `browser-frame` chrome for visual consistency |
| Styles | Minimal `.demo-video` / `.demo-video__player` rules in `css/style.css` (16:9, full width, max-width 960px) |
| Nav | Added **Demo** link → `#demo` (no branding or layout redesign) |

### Behavior

- Desktop / mobile: video is `width: 100%` inside the existing container + section spacing scale.
- Metadata-only preload limits initial bandwidth; lazy loading applies where supported.
- Branding, screenshots, and README were not modified.

---

## 2. Odoo Apps Description

| Item | Detail |
|------|--------|
| File | `relayruntime/static/description/index.html` |
| Section title | **Product Demonstration** |
| Placement | After **Features**, before **Limitations** |
| Video source | `../../../landing-page/all_end.mp4` |
| Poster | `../../../landing-page/assets/banner_1.png` |
| Duplication | None — references the same official file |

### Path resolution

From `relayruntime/static/description/` the relative path resolves to:

`landing-page/all_end.mp4`

Verified on disk: path exists and points to the single canonical MP4.

**Note:** On Odoo Apps Store hosting, only `static/description` assets are typically packaged with the module listing. The relative link is correct for the monorepo / local docs context and GitHub Pages deployments that serve `landing-page` as the site root (`…/all_end.mp4`). No second copy was created for Apps packaging.

---

## 3. Asset Integrity

| Check | Result |
|-------|--------|
| Filename | `all_end.mp4` (unchanged) |
| Location | `landing-page/all_end.mp4` (unchanged) |
| Size | 34,353,508 bytes (~32.8 MB) |
| MP4 copies in tree | **1** (no duplicates) |
| Recompression | Not performed |
| Branding assets | Untouched |
| Screenshots | Untouched |
| README | Untouched |

---

## 4. Verification Checklist

| Check | Status |
|-------|--------|
| Video file present at canonical path | Pass |
| Landing embed `src="all_end.mp4"` | Pass |
| Description embed resolves to same file | Pass |
| Controls enabled | Pass |
| `preload="metadata"` | Pass |
| Lazy loading attribute present | Pass |
| Poster image available and referenced | Pass |
| Section order: Features → Demo → Command Center | Pass |
| Responsive CSS (full-width 16:9 player) | Pass |
| No duplicated video assets | Pass |
| No rename / move / recompress | Pass |

---

## 5. Files Touched

1. `landing-page/index.html` — demo section + nav link  
2. `landing-page/css/style.css` — demo video spacing / responsive player  
3. `relayruntime/static/description/index.html` — Product Demonstration section  
4. `landing-page/RELEASE_MEDIA_REPORT.md` — this report  

**Unchanged:** `landing-page/all_end.mp4`, logos, screenshots, README, brand colors.
