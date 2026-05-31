# Odoo App Store Assets

Place final marketing assets in this directory before Odoo Apps submission.

## Required files

| File | Dimensions | Format | Notes |
|------|------------|--------|-------|
| `icon.png` | 256×256 (min 128×128) | PNG | Module icon in Apps list |
| `banner.png` | 560×280 recommended | PNG | Store banner |
| `index.html` | — | HTML | Store description (included) |
| `screenshots/*.png` | 1280×720 or 1024×768 | PNG | 3–6 screenshots |

## Optional

| File | Purpose |
|------|---------|
| `demo.gif` | Short screen recording of bulk send + monitor |

## Placeholder

`icon.svg` is a **temporary vector placeholder**. Export to `icon.png` before submission.

```bash
# Example with Inkscape (if installed)
inkscape icon.svg -w 256 -h 256 -o icon.png
```

## Content guidelines

- Use **Mock Provider** screenshots for public marketing when possible.
- Include **limitations** slide or section (no exactly-once guarantee).
- Do not claim: distributed HA, background queue, inbound webhooks (unless shipped).
- Align version text with `__manifest__.py`.

## Suggested screenshots

1. WhatsApp Settings (provider + safety)
2. Bulk send wizard
3. Campaign monitor during run
4. Campaign form with Executions tab
5. Message logs / delivery dashboard
6. Retry campaign lineage (parent → child)
