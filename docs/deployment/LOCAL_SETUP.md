# Local Setup

[← Documentation index](../README.md)

## Prerequisites

| Component | Notes |
|-----------|-------|
| Odoo 19 Community | Module version must be `19.0.x` |
| PostgreSQL | Standard Odoo database |
| Python | Matches Odoo 19 requirements for your distribution |
| RelayRuntime `apps/odoo` on addons path | See [apps/odoo/README.md](../../apps/odoo/README.md) |

**Repository example** (`server/odoo.conf`):

```ini
addons_path = c:\odoo19.0c\server\odoo\addons,C:\Odoo19.0c\relayruntime\apps\odoo
workers = 0
http_port = 8029
limit_time_real = 120
```

`workers = 0` is threaded dev mode — see [Production Checklist](PRODUCTION_CHECKLIST.md) before production.

## Install module

1. Add `apps/odoo` from this repository to `addons_path`.
2. Restart Odoo.
3. Apps → Update Apps List.
4. Install **WhatsApp Simple**.
5. Assign **WhatsApp User** or **WhatsApp Manager** to users.

## Configure provider

### Mock Provider (recommended for local QA)

1. **WhatsApp → Settings**
2. Provider Type: **Mock Provider (Test Mode)**
3. Adjust simulation rates on **Mock Simulation** tab (optional)
4. No real messages are sent

### Green API (real traffic)

1. Obtain Green API instance id and token.
2. Provider Type: **Green API**
3. Enter API URL, instance, token fields.
4. Use **Test Connection** action.

Other provider types appear in the UI but raise **not implemented** at send time unless `is_implemented=True` on the adapter.

## Optional file logging

**WhatsApp → Settings:**

- Enable **Dedicated WhatsApp Log File**
- Path default example: `C:\Odoo19.0c\logs\whatsapp.log`

Logs also go to the main Odoo server log via Python logging.

## Upgrade after pull

```bash
python odoo-bin -c odoo.conf -d YOUR_DB -u relayruntime --stop-after-init
```

Or upgrade from Apps UI when developer mode is enabled.

## Verify installation

| Check | Expected |
|-------|----------|
| Contacts list → **WhatsApp Bulk Send** action | Opens wizard |
| **WhatsApp → Campaign Monitor** | Kanban loads |
| Bulk send with Mock | Campaign + execution rows created |
| Campaign form → **Executions** tab | Lists `whatsapp.bulk.execution` |

## Further reading

- [Environment Variables](ENVIRONMENT_VARIABLES.md)
- [Production Checklist](PRODUCTION_CHECKLIST.md)
- [Testing Strategy](../testing/TESTING_STRATEGY.md)
