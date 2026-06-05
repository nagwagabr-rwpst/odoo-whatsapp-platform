# RWPST Global Brand Layer — Implementation Report

**Module:** `relayruntime` (RWPST RelayRuntime)  
**Version:** 19.0.5.4.27  
**Date:** 2026-06-05

## Objective

Replace the default Odoo Community purple (`#71639e`) with the RWPST palette across the entire ERP chrome while preserving Odoo UX behavior and business logic.

## Brand Palette Applied

| Token | Hex | Usage |
|-------|-----|--------|
| Primary | `#2563EB` | Buttons, links, focus rings, action color |
| Deep Primary | `#1E3A8A` | Top navbar, search facet labels, mobile search header, sidebar top bar |
| Dark Navy | `#0F172A` | Body text, headings, breadcrumb current item |
| Accent / Alert | `#F97316` | Navbar notification badges, warning alerts |
| Success | `#25D366` | Success badges, semantic success (WhatsApp green) |

## Asset Architecture

```
web._assets_primary_variables
├── (before) _rwpst_brand_tokens.scss          ← canonical palette + interaction tokens
├── (before) rwpst_brand_primary_variables.scss ← $o-community-color, $o-brand-odoo, $o-brand-primary
├── primary_variables.scss                      ← Odoo core (Community defaults skipped)
├── (after)  rwpst_brand_derived_variables.scss ← action, buttons, links, list-group, theme colors
├── *.variables.scss                            ← Odoo component variables
└── (after)  rwpst_brand_component_variables.scss ← burger sidebar top bar

web.assets_backend
├── _rwpst_brand_tokens.scss
├── rwpst_variables.scss                        ← Command Center tile tokens
├── rwpst_mixins.scss
├── rwpst_theme.scss                            ← scoped Command Center enhancements
├── rwpst_dashboard.scss
├── rwpst_tiles.scss
└── rwpst_global_brand.scss                     ← global CSS layer (all apps)

web.assets_frontend
├── _rwpst_brand_tokens.scss
└── rwpst_global_brand.scss                     ← login / database manager
```

## Files

| File | Role |
|------|------|
| `_rwpst_brand_tokens.scss` | Canonical palette, hover/active/focus/tint tokens |
| `rwpst_brand_primary_variables.scss` | Pre-`primary_variables` Odoo core overrides |
| `rwpst_brand_derived_variables.scss` | Post-`primary_variables` derived tokens + button maps |
| `rwpst_brand_component_variables.scss` | Component variable overrides (burger sidebar) |
| `rwpst_global_brand.scss` | Global CSS layer for navbar, sidebar, forms, kanban, login, alerts |
| `rwpst_variables.scss` | Command Center tile accents (analytics tile de-purpled to `#1D4ED8`) |
| `__manifest__.py` | Asset bundle registrations |

**Unchanged (by design):** Python models, XML views, security, JS behavior, `rwpst_theme.scss` scoped dashboard rules.

## Odoo Variables Overridden

### Before `primary_variables.scss`

| Variable | New value |
|----------|-----------|
| `$o-community-color` | `$o-rwpst-blue` (`#2563EB`) |
| `$o-brand-odoo` | `$o-rwpst-blue-deep` (`#1E3A8A`) |
| `$o-brand-primary` | `$o-rwpst-blue` (`#2563EB`) |

### After `primary_variables.scss`

| Variable | New value |
|----------|-----------|
| `$o-action` | `$o-rwpst-blue` |
| `$o-success` | `$o-rwpst-success` (`#25D366`) |
| `$o-warning` | `$o-rwpst-accent` (`#F97316`) |
| `$o-info` | `$o-rwpst-blue` |
| `$o-main-text-color` | `$o-rwpst-navy` |
| `$o-main-link-color` | `$o-rwpst-blue-deep` |
| `$o-component-active-bg` | `rgba(#2563EB, 0.12)` |
| `$o-btns-bs-override` | Primary, secondary, light — RWPST hover/active |
| `$o-btns-bs-outline-override` | Primary, secondary outline — RWPST tints |

### Propagated automatically (via Odoo SCSS chain)

- `$primary` (Bootstrap) ← `$o-brand-primary`
- `$o-navbar-background` ← `$o-brand-odoo`
- `$link-color`, `$nav-pills-link-active-bg`, `$input-focus-border-color`, etc.

## Global CSS Layer Targets

- Top navbar (`.o_main_navbar`) — deep blue, white text, orange systray badges
- App menu & dropdown menus — RWPST blue active/hover tints
- Mobile / app sidebar (`.o_burger_menu`, `.o_app_menu_sidebar`)
- Breadcrumbs & control panel view switchers
- Search view focus ring & facet labels
- Primary / secondary / outline buttons
- Badges, nav pills, tabs, pagination, progress bars
- Form stat buttons, checkboxes, list selection highlights
- Kanban column hover & record focus
- Alerts (warning = orange accent)
- File upload progress & export dialog selection
- Settings mobile tabs
- App launcher background gradient
- Login page (`body.bg-100`, `.o_database_list`)

## Deployment

```powershell
C:\Odoo19.0c\python\python.exe C:\Odoo19.0c\server\odoo-bin -c C:\Odoo19.0c\server\odoo.conf -u relayruntime --stop-after-init
```

Restart the Odoo server, then hard-refresh the browser (`Ctrl+Shift+R`).

## Rollback

1. Remove the `web._assets_primary_variables` block and `rwpst_global_brand.scss` entries from `__manifest__.py`.
2. Upgrade: `-u relayruntime`
3. Hard-refresh browser.

Uninstalling `relayruntime` removes all branding assets and RelayRuntime functionality.
