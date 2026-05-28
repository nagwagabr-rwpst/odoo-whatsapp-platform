---
name: Deployment Issue
about: Installation, upgrade, Odoo.sh, Docker, timeout, or infrastructure problems
title: "[Deploy]: "
labels: ["deployment", "triage"]
assignees: []
---

## Environment

| Field | Value |
|-------|-------|
| **Odoo version** | |
| **Module version** | |
| **Platform** | <!-- Local Windows / Linux / Odoo.sh / Docker / Other --> |
| **PostgreSQL version** | <!-- if known --> |

## Odoo configuration (relevant)

| Setting | Value |
|---------|-------|
| `workers` | |
| `limit_time_real` | |
| `limit_time_cpu` | |
| `limit_memory_soft` | |
| `addons_path` includes module | <!-- yes/no --> |

## Deployment steps performed

1. <!-- clone / copy module -->
2. <!-- install or -u whatsapp_simple -->
3. <!-- configure provider -->

## Problem description

<!-- What fails: install, upgrade, timeout on bulk, worker crash, etc. -->

## Traceback / error message

<details>
<summary>Full traceback (sanitize paths if needed)</summary>

```
(paste here)
```

</details>

## Module upgrade

- [ ] Fresh install
- [ ] Upgrade from version: 
- [ ] Migration / registry error

## Bulk send context (if timeout)

| Field | Value |
|-------|-------|
| Recipients count | |
| Attachments per recipient | |
| Approx. duration before failure | |

## Logs

<details>
<summary>Odoo log excerpt</summary>

```
```

</details>

## Checklist

- [ ] I followed [Local Setup](docs/deployment/LOCAL_SETUP.md) or [Odoo.sh Deployment](docs/deployment/ODOO_SH_DEPLOYMENT.md)
- [ ] I reviewed [Production Checklist](docs/deployment/PRODUCTION_CHECKLIST.md)
- [ ] No secrets in this issue
