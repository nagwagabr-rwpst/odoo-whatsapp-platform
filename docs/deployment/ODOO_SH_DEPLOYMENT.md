# Odoo.sh Deployment

[← Documentation index](../README.md) · [Local Setup](LOCAL_SETUP.md)

Guidance for hosting **WhatsApp Simple** on [Odoo.sh](https://www.odoo.sh/). This module has **no Odoo.sh-specific code**; deployment follows standard Odoo.sh practices with operational caveats from synchronous bulk sending.

## Add module to project

1. Push `relayruntime` to your GitHub repository branch tracked by Odoo.sh.
2. Ensure the module path is at the **repository root** or configured addons root Odoo.sh expects.
3. Wait for build; install/upgrade on staging first.

```bash
# Typical staging upgrade (Odoo.sh shell or local against remote DB)
odoo-bin -u relayruntime -d <staging-db>
```

## Branch workflow

| Branch | Use |
|--------|-----|
| Staging | Full bulk + Mock provider regression |
| Production | Green API credentials; conservative limits |

## Odoo.sh configuration considerations

| Topic | Recommendation |
|-------|----------------|
| **Workers** | Use multi-worker production (not `workers=0`) |
| **Request timeout** | Increase `limit_time_real` if large bulks are required — understand tradeoffs |
| **Longpolling** | Unaffected; bulk send is HTTP POST on wizard |
| **Cron** | Module does not register bulk-send crons; default Odoo crons only |
| **Secrets** | Store API tokens in `whatsapp.config` (Manager ACL); consider env-based config only via custom bridge (**not implemented** in module) |

## Staging validation checklist

- [ ] Install/upgrade `relayruntime` without traceback
- [ ] Mock provider bulk send (10–50 recipients)
- [ ] Retry failed recipients
- [ ] Confirm execution rows and leases in campaign form
- [ ] Green API test connection on staging instance (optional)
- [ ] Review server logs for `campaign_logger` / `api_logger` volume

## Production promotion

1. Merge to production branch after staging sign-off.
2. Upgrade module on production database during low-traffic window.
3. Reconcile any stale `running` campaigns before heavy use (see [Runbook](../operations/RUNBOOK.md)).

## Scaling caveats on Odoo.sh

**Implemented behavior:** bulk send blocks one HTTP worker for the full campaign duration.

| Risk | Mitigation |
|------|------------|
| HTTP timeout | Smaller batches; increase limit cautiously |
| Worker starvation | Avoid concurrent large bulks by operations policy |
| Memory | Limit recipients per campaign operationally |

**Planned / future:** background queue — not available on Odoo.sh or self-hosted without new development.

## Further reading

- [Production Checklist](PRODUCTION_CHECKLIST.md)
- [Known Limitations](../architecture/KNOWN_LIMITATIONS.md)
