# WhatsApp Simple (Odoo 19 Community)

Lightweight WhatsApp sales workflow: single and bulk sending, delivery tracking, product catalogs, and manual order creation.

## Features

- **Settings** — API URL, instance ID, token, safety limits
- **Single send** — Contacts and Sales Orders
- **Bulk send** — Multi-contact campaigns with attachments and products
- **Delivery logs** — Per-recipient state, failures, API IDs, duration
- **Dashboard** — Success rate and quick filters
- **Campaign Monitor** — Live kanban with auto-refresh during bulk sends
- **Observability** — Structured loggers + optional `logs/whatsapp.log` file
- **Product catalogs** — Auto message + optional product images
- **Sale orders** — Create draft SO from manual product selection (no chatbot/AI)

## Install

1. Copy `whatsapp_simple` into your Odoo addons path (e.g. `C:\Odoo19.0c`).
2. Update Apps list and install **WhatsApp Simple**.
3. Assign **WhatsApp User** or **WhatsApp Manager** groups.
4. Configure **WhatsApp → Settings** (Green API compatible).

## Bulk send from Contacts

1. Open **Contacts** list.
2. Select records.
3. Click **WhatsApp Bulk Send** in the list header (or Action menu).
4. Compose message, attach files, and/or select products.
5. Review statistics and logs when finished.

## Product workflow

1. Select products in the bulk wizard and enable **Use Product Images**.
2. Customers receive a numbered catalog and product images.
3. Record their selection in **Create Sale Order from Selection** (campaign or message log).
4. Confirm quantities and create a draft quotation.

## Campaign Monitor

Open **WhatsApp → Campaign Monitor** while a bulk send runs. Cards show progress %, current contact/product, and sent/failed/skipped counts. The view reloads every 5 seconds (no websocket).

## Dedicated log file (optional)

In **WhatsApp → Settings**, enable **Dedicated WhatsApp Log File** and set the path (default `C:\Odoo19.0c\logs\whatsapp.log`). Logs still appear in the main Odoo log.

See `docs/ARCHITECTURE.md` and `docs/PROVIDER_ARCHITECTURE.md` for service and provider adapter design.

## Provider types

**Green API** is production-ready. **Mock Provider** simulates sends without real messages (QA, demos, stress tests). Other providers are placeholders for future adapters.

### Mock Provider quick start

1. **WhatsApp → Settings** → Provider Type: **Mock Provider (Test Mode)**
2. Adjust simulation rates on the **Mock Simulation** tab (optional)
3. Run bulk campaigns, retries, and monitor — no real WhatsApp traffic
4. Use magic numbers like `201333333333` on a contact to force timeouts (see Settings help text)

## Upgrade

```bash
python odoo-bin -c odoo.conf -d YOUR_DB -u whatsapp_simple
```

## Version

See [CHANGELOG.md](CHANGELOG.md).
