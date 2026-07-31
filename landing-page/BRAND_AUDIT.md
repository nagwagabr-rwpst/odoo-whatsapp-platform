# BRAND_AUDIT.md

**Project:** RelayRuntime Landing Page  
**Release:** RELEASE-011 · Brand Identity Lock  
**Date:** 2026-07-31  
**Scope:** Official hexagonal brand migration — landing page only  

---

## Final Brand Consistency Score

# **10 / 10**

The landing page uses **only** the official RelayRuntime hexagonal identity. Legacy Odoo-style circular icons have been removed from the landing-page asset tree and all HTML/CSS/meta references.

---

## Brand Assets Used

| Official Asset | Role on Landing Page |
|---|---|
| `assets/HorizontalLogo.jpg` | Desktop/tablet navigation · Footer · Open Graph · Twitter Card · Schema.org `image` / `logo` · README · Preload |
| `assets/AppIcon.jpg` | Browser favicon · Apple touch icon · Mobile header (mark + “RelayRuntime” text) · Provider Abstraction diagram mark |
| `assets/VerticalLogo.jpg` | Present in official pack (available for future vertical placements; not forced into nav/footer) |
| `assets/banner_1.jpg` | Hero product visual (already branded — no extra logo layered on top) |
| `assets/banner.png` | Retained as marketing/store cover asset (not used as brand identity / favicon) |

**Source of truth directory:**  
`relayruntime/static/description`

**Rule applied:** Never recreate assets. Use provided files exactly.

---

## Brand Lock Compliance

| Placement | Required | Implementation | Status |
|---|---|---|---|
| Navigation | HorizontalLogo | `.brand--desktop` → `HorizontalLogo.jpg` | Pass |
| Footer | HorizontalLogo | `.brand--footer` → `HorizontalLogo.jpg` on light plate | Pass |
| Hero | No second logo | No logo element in hero; banner cropped to dashboard | Pass |
| Mobile menu / header | AppIcon + RelayRuntime text | `.brand--mobile` (≤768px) | Pass |
| Favicon | AppIcon only | `<link rel="icon" href="assets/AppIcon.jpg">` | Pass |
| Apple touch icon | AppIcon | `<link rel="apple-touch-icon" href="assets/AppIcon.jpg">` | Pass |
| Open Graph | HorizontalLogo | Absolute URL to `HorizontalLogo.jpg` | Pass |
| Twitter Card | HorizontalLogo | Absolute URL to `HorizontalLogo.jpg` (`summary`) | Pass |
| Schema.org | HorizontalLogo | `image`, `logo`, `author.logo` | Pass |
| README | HorizontalLogo | Documented + embedded reference | Pass |
| Abstraction diagram | Official mark | `AppIcon.jpg` (not legacy SVG) | Pass |

---

## Legacy Assets Removed

Removed from `landing-page/assets/` (no longer referenced):

| Deprecated File | Reason |
|---|---|
| `icon.svg` | Legacy Odoo circular / orange-cross application mark |
| `icon.png` | Legacy module icon |
| `icon_128.png` | Legacy small icon variant |
| `rwpst_relayruntime_logo.png` | Legacy circular product icon |

**Note:** The same legacy files may still exist under `relayruntime/static/description/` for Odoo Apps packaging history. They are **out of scope for the landing page** and must not be copied back into `landing-page/assets/`.

---

## Duplicate Branding Review (Hero)

**Risk:** Navigation HorizontalLogo + Hero Banner both carry brand.

**Mitigation applied:**

1. Hero does **not** inject an additional logo element.
2. Hero image is cropped (`object-position`) to the **product dashboard** region of `banner_1.jpg`, reducing on-canvas logo/headline competition with the HTML hero copy.
3. Full branded banner remains available in lightbox for users who enlarge the visual.

**Verdict:** Branding is elegant, not cluttered. Pass.

---

## Visual Quality Checks

| Check | Result |
|---|---|
| Logo sharpness | Pass — official JPG assets, preloaded HorizontalLogo, `object-fit: contain` |
| Padding / spacing | Pass — nav height 40px logo; footer plate padding for white-canvas JPG |
| Retina | Pass — source assets larger than display size |
| SVG preference | N/A — no official SVG hexagonal lockup provided; JPG used as mandated |
| Dark footer appearance | Pass — HorizontalLogo on white rounded plate (JPG has white canvas) |
| Light header appearance | Pass — HorizontalLogo blends with white header |
| Mobile appearance | Pass — AppIcon mark + RelayRuntime wordmark |
| Favicon | Pass — AppIcon only |

---

## Remaining Branding Issues

**None blocking.** Score is 10/10 for the landing page brand lock.

Optional future improvements (outside RELEASE-011 mandatory scope):

1. Provide official **transparent PNG/SVG** HorizontalLogo for dark surfaces without a white plate.
2. Provide a **32×32 / 180×180** AppIcon export optimized specifically for favicons (same art, smaller bytes).
3. When ready, deprecate legacy `icon.*` files from the Odoo module description pack in a separate packaging release.

---

## Recommendations

1. Treat `landing-page/assets/{HorizontalLogo,VerticalLogo,AppIcon}.jpg` as the canonical web brand pack.
2. Never reintroduce `icon.svg` / `icon.png` into the landing page.
3. For future UI work, continue Brand Lock rules before any visual polish.
4. If GitHub Pages base path differs from the assumed canonical host, update absolute OG/Twitter/Schema URLs accordingly — keep asset filenames unchanged.

---

## Audit Evidence (Scan)

Landing-page references after migration:

- `HorizontalLogo.jpg` — nav, footer, meta, schema, preload, README  
- `AppIcon.jpg` — favicon, apple-touch, mobile brand, abstraction node  
- `VerticalLogo.jpg` — assets pack only  
- Zero matches for `icon.svg`, `icon.png`, `icon_128`, `rwpst_relayruntime_logo` in landing HTML/CSS/JS/README  

---

## Sign-Off

| Gate | Status |
|---|---|
| Official assets only | Pass |
| Legacy assets removed from landing page | Pass |
| Brand Lock placements correct | Pass |
| No duplicate hero logo injection | Pass |
| Brand Consistency Score = 10/10 | **Pass** |

**RELEASE-011 Brand Identity Lock: COMPLETE**

Future UI work may proceed under this locked identity.

---

END OF BRAND AUDIT
