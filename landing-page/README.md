# RelayRuntime Landing Page

Official marketing website for **RelayRuntime** — Enterprise Messaging Runtime for Odoo Community.

This page follows `docs/marketing/LANDING_PAGE_SPEC.md` as the single source of truth.

## Official Brand Identity (RC2)

The hexagonal RelayRuntime identity is the **only** official brand.

**Source of truth:** repository `branding/`

| Asset | Use |
|---|---|
| `HorizontalLogo.svg` / `.png` | Navigation · Footer · Open Graph · Twitter · Schema · README |
| `AppIcon.svg` / `.png` | Favicon (SVG + PNG fallback) · Apple touch · Mobile header · Abstraction diagram |
| `VerticalLogo.svg` / `.png` | Official pack (available for vertical placements) |

Sync: `branding/` → `landing-page/assets/` and `relayruntime/static/description/`.

**JPG logos are not used.** Screenshots/hero media may remain JPG/PNG.

Legacy files (`icon.svg`, `icon_128.png`, `rwpst_relayruntime_logo.*`, `*.jpg` logos) are forbidden.

## Structure

```
landing-page/
├── index.html
├── css/
│   ├── style.css
│   └── responsive.css
├── js/
│   └── main.js
├── assets/
│   ├── HorizontalLogo.svg
│   ├── HorizontalLogo.png
│   ├── VerticalLogo.svg
│   ├── VerticalLogo.png
│   ├── AppIcon.svg
│   ├── AppIcon.png
│   ├── banner_1.jpg
│   ├── banner.png
│   └── screenshots/
│       ├── 01_command_center.png
│       ├── 02_settings.png
│       ├── 03_bulk_wizard.png
│       └── 06_delivery_dashboard.png
├── BRAND_AUDIT.md
├── RELEASE_REVIEW.md
├── FINAL_RC2_REPORT.md
└── README.md
```

## Sections

1. Hero  
2. Problem  
3. Solution  
4. Key Features  
5. Operational Command Center  
6. Provider Abstraction  
7. Product Experience  
8. Supported Providers  
9. Deployment  
10. FAQ  
11. Final CTA  
12. Footer  

## Tech stack

- Pure HTML5 / CSS3 / Vanilla JavaScript
- No Bootstrap, Tailwind, jQuery, or React
- Google Fonts: Plus Jakarta Sans

## Local preview

```bash
python -m http.server 8080 --directory landing-page
```

Visit `http://localhost:8080`.

## Brand rules

- Navigation / Footer → `HorizontalLogo.svg`
- Mobile header → `AppIcon.svg` + “RelayRuntime” text
- Favicon → `AppIcon.svg` (fallback `AppIcon.png`)
- Social / Schema → `HorizontalLogo.png` (crawler-friendly)
- Hero banner already includes branding — do not add a second logo in the hero
