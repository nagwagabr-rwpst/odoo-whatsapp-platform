# Environment Variables

[← Documentation index](../README.md)

## Overview

**WhatsApp Simple** stores operational settings in the **`whatsapp.config`** Odoo model, not in environment variables. There are **no module-specific `os.environ` keys** in the codebase.

Deployment configuration uses standard **Odoo server options** (config file or Odoo.sh platform settings).

## Odoo server options (relevant)

| Option | Typical impact on this module |
|--------|------------------------------|
| `addons_path` | Must include directory containing `whatsapp_simple` |
| `workers` | `0` = threaded; `>0` = prefork — affects concurrency |
| `limit_time_real` | Max seconds per HTTP request (bulk send) |
| `limit_time_cpu` | CPU time limit per request |
| `limit_memory_soft` / `limit_memory_hard` | Large campaigns + attachments |
| `db_*` | PostgreSQL connection |
| `proxy_mode` | If behind reverse proxy for HTTPS |
| `log_level` / `log_handler` | Visibility of `whatsapp_simple` loggers |

**Example from repository** `server/odoo.conf`:

```ini
limit_time_real = 120
workers = 0
http_port = 8029
```

## Module settings (database — implemented)

Configured per company in **WhatsApp → Settings** (`whatsapp.config`):

| Category | Examples |
|----------|----------|
| Provider | `provider_type`, API URL, tokens |
| Safety | `daily_send_limit`, min/max delay, cooldown thresholds |
| Mock | Simulation rates, latency |
| Logging | `file_log_enabled`, `file_log_path` |

Access: **WhatsApp Manager** required to write sensitive fields (e.g. `access_token`).

## Environment variable patterns (not implemented)

The following are **not** built into the module today:

| Pattern | Status |
|---------|--------|
| `WHATSAPP_API_TOKEN` env → config | Planned / custom deployment only |
| `os.environ` provider selection | Not implemented |
| Separate secrets manager integration | Not implemented |

Teams may implement external secret injection via standard Odoo `server_environment` or custom modules — outside this module's scope.

## Further reading

- [Local Setup](LOCAL_SETUP.md)
- [Production Checklist](PRODUCTION_CHECKLIST.md)
