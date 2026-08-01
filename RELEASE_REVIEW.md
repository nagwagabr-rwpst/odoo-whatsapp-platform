# RELEASE_REVIEW.md

**Project:** RelayRuntime Landing Page  
**Release:** RC1 · RELEASE-010  
**Review Date:** 2026-07-31  
**Reviewers (roles):** Senior Product Designer · Senior UX Designer · Senior Frontend Architect · SaaS Marketing Expert  
**Source of Truth:** `docs/marketing/LANDING_PAGE_SPEC.md`  
**Scope:** Engineering / UX review only — no new sections, no message rewrites, no rebranding.

---

## Overall Score

| Category | Score (1–10) |
|---|---|
| **Visual Design** | **8.5** |
| **UX** | **8.5** |
| **Marketing** | **8.0** |
| **Responsiveness** | **8.5** |
| **Accessibility** | **9.0** |
| **SEO** | **8.5** |
| **Performance** | **8.0** |
| **Professionalism** | **8.5** |
| **Overall** | **8.4 / 10** |

RC1 is **launch-capable** for GitHub Pages and company website presentation after Critical/Major fixes applied in this review. Remaining gaps are mostly assets, demo authenticity, and store listing maturity — not page structure.

---

## Review Method

Evaluated the live implementation across 18 dimensions. Issues classified as Critical / Major / Minor / Nice to Have. All **Critical** and **Major** items were fixed in code before scoring.

---

## Findings (Pre-Fix) → Disposition

### Critical

| # | Issue | Disposition |
|---|---|---|
| C1 | Scroll-reveal set `opacity: 0` by default — **entire below-fold page invisible if JS fails** | **Fixed** — reveals gated behind `html.js`; content visible without JS |
| C2 | Hero used reveal animation — **LCP / first paint risk** | **Fixed** — hero content/visual no longer use reveal |
| C3 | Open Graph / Twitter / Schema image URLs were **relative** — social crawlers break | **Fixed** — absolute URLs on canonical host |
| C4 | Hero showed full composite `banner_1.jpg` (complete second landing) beside identical HTML copy — **double-hero / diluted hierarchy** | **Fixed** — crop via `object-fit`/`object-position` to product dashboard; lightbox still shows full asset |

### Major

| # | Issue | Disposition |
|---|---|---|
| M1 | Primary CTA “Watch Live Demo” linked to GitHub root — **misleading, no demo** | **Fixed** — anchors to `#experience` (real product screens) |
| M2 | No LCP preload for hero image | **Fixed** — `<link rel="preload" as="image">` + `fetchpriority="high"` |
| M3 | Tablet hero stayed 2-column too long — cramped | **Fixed** — stack at `≤900px` |
| M4 | Sticky header lacked scroll elevation — flat enterprise feel | **Fixed** — `.is-scrolled` shadow/state |
| M5 | Lightbox missing `aria-hidden` toggle | **Fixed** |
| M6 | Google Fonts requested unused italic axis | **Fixed** — removed italic from request |
| M7 | Provider “logo grid” felt empty (no fake logos allowed) | **Fixed** — monogram marks (not third-party logos) |
| M8 | Odoo Apps footer → generic `apps.odoo.com` | **Fixed** — search deep-link for RelayRuntime |
| M9 | Below-fold paint cost | **Fixed** — `content-visibility: auto` on sections |
| M10 | Images missing `sizes` hints | **Fixed** |

### Minor (not auto-fixed)

| # | Issue | Notes |
|---|---|---|
| m1 | Command Center screenshot appears twice (OCC + Experience) | Spec requires both; browser cache mitigates weight |
| m2 | Unused JPG logos still in `/assets` (~320KB disk, not network) | Harmless for Pages; clean up optional |
| m3 | Schema `offers.price: 0` may be wrong if Apps listing is paid | Update when pricing is final |
| m4 | No `sitemap.xml` / `robots.txt` | Add when GH Pages URL is final |
| m5 | FAQ all collapsed by default | Opening first item is a polish choice |
| m6 | No live interactive demo / `demo.gif` | Asset still missing per store docs |
| m7 | Exact Odoo Apps module URL unknown | Search link is interim |

### Nice to Have

| # | Idea |
|---|---|
| n1 | Official provider SVG/PNG logo pack (licensed) for true logo grid |
| n2 | Dedicated `/demo` or Loom/embed for true “Watch Live Demo” |
| n3 | Customer logos / partner strip (when available) |
| n4 | Dark/light logo variants as SVG wordmark |
| n5 | WebP/AVIF derivatives of screenshots for Lighthouse headroom |
| n6 | Active nav section highlighting on scroll |

---

## Dimension Notes

### 1. Visual hierarchy — 8.5
Strong dark hero → muted problem → solution → features cadence. Post-crop hero visual no longer competes as a second page. Eyebrows and H2 scale read correctly.

### 2. Typography — 8.5
Plus Jakarta Sans, clear weight ladder, comfortable body measure. Enterprise, not startup-playful.

### 3. White space — 8.5
Section padding (~6.5rem desktop) matches Stripe/Linear-class SaaS. Cards not cramped.

### 4. Alignment — 8.5
Consistent container, grid gutters, browser-frame chrome. Provider flex wrap centers cleanly with 7 items.

### 5. Consistency — 8.5
Radius, blue system, card elevation, and button language are coherent. Problem cards use a restrained danger tint vs feature blue.

### 6. Hero impact — 8.5
After crop + no-reveal + preload: clear message, visible CTAs, product UI as proof. Full banner remains available in lightbox.

### 7. CTA visibility — 9.0
Primary solid / secondary ghost contrast well on dark surfaces. Nav “Get Started” and final CTA reinforce conversion.

### 8. Marketing clarity — 8.0
Runtime positioning is repeated correctly (not “another WhatsApp connector”). Demo CTA now honest. Still missing true live demo asset for peak conversion.

### 9. Product positioning — 9.0
Spec messages preserved: Enterprise Messaging Runtime, Provider Abstraction, Operational Command Center, Production Ready, Queue/Retry/Analytics.

### 10. Enterprise feeling — 8.5
Navy/deep/electric blue, restrained motion, operational screenshots. Feels like infrastructure software, not a consumer chatbot landing.

### 11. Screenshot presentation — 8.5
Browser frames + lightbox + lazy-load. Real product shots only. Zero-data Mock Provider UI is honest but less “wow” than populated dashboards (asset limitation).

### 12–14. Responsive — 8.5
Desktop two-column hero; tablet 2-up grids; mobile single column + full-width buttons + drawer nav. Hero stacks by 900px.

### 15. Animation quality — 8.5
250–350ms fade/scale, staggered cards, reduced-motion respected, JS-failure safe.

### 16. Accessibility — 9.0
Skip link, focus-visible, FAQ accordion semantics, lightbox focus trap, new-tab announcements, 44px targets, contrast-conscious secondary text.

### 17. SEO — 8.5
Title, description, keywords, canonical, OG/Twitter absolute images, Schema.org SoftwareApplication, single H1, semantic sections.

### 18. Performance — 8.0
Lean HTML/CSS/JS, lazy screenshots, preload LCP, `content-visibility`, font subset trimmed. Hero JPG ~241KB remains the main LCP cost; WebP would push toward 95+ Lighthouse Performance more reliably.

---

## Fixes Applied in RC1 Review Pass

1. JS-gated reveal system (`document.documentElement.classList.add("js")`)
2. Hero removed from reveal path; LCP preload added
3. Absolute social/schema image URLs
4. Hero banner cropped to dashboard product region
5. “Watch Live Demo” → `#experience`
6. Header scroll elevation
7. Lightbox `aria-hidden` management
8. Provider monogram marks
9. Odoo Apps search deep-link
10. `content-visibility`, `sizes`, font request trim
11. Earlier hero stack breakpoint (900px)

---

## Launch Readiness

### Would this landing page be good enough for:

| Channel | Verdict | Why |
|---|---|---|
| **Odoo Apps** | **Almost — not store-complete alone** | Page is strong marketing collateral. Apps listing still needs module ZIP, `static/description/index.html`, populated screenshots, and ideally `demo.gif`. Landing page ≠ Apps submission package. |
| **GitHub** | **Yes** | Suitable as GitHub Pages / project website. Clear positioning, docs/GitHub links, professional presentation. |
| **Company Website** | **Yes (with caveats)** | Good enough as the product homepage for RWPST/RelayRuntime. Caveats: wire true demo URL when ready; replace Apps search link with exact module URL when published; optional WebP assets. |
| **Product Launch** | **Yes for soft/public web launch** | Ready for announce + GH Pages. For a high-stakes paid launch event, add a real demo (video/live) and preferably populated production screenshots — those are the only material gaps left. |

### What is still missing (not page-structure)

1. **True Live Demo** — video, Loom, or interactive environment behind “Watch Live Demo”
2. **Official Odoo Apps listing URL** — once published
3. **Populated screenshots / demo.gif** — Mock Provider empty-state KPIs under-sell enterprise scale
4. **Optional performance pack** — WebP/AVIF for banner + screenshots to lock Lighthouse Performance >95
5. **Licensed provider logos** — if marketing wants a true logo wall later

---

## RC1 Sign-Off

| Gate | Status |
|---|---|
| Spec section order preserved | Pass |
| Marketing messages unchanged | Pass |
| Branding preserved | Pass |
| Critical issues resolved | Pass |
| Major issues resolved | Pass |
| Ready for GitHub Pages | Pass |
| Ready as company product page | Pass (soft launch) |
| Ready as sole Odoo Apps package | Fail — needs Apps assets/listing workflow |

**Recommendation:** Ship RC1 to GitHub Pages as the official product website. Track remaining items as RELEASE-011 (Demo + Apps listing + image optimization).

---

END OF RELEASE REVIEW
