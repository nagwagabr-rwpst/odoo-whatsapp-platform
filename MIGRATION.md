# Migration: whatsapp_simple → RelayRuntime

Operational migration guide for databases, addons paths, and XML identity. Treat this as a **controlled cutover**, not a rename-in-place.

---

## What changed

| Dimension | Before | After |
|-----------|--------|-------|
| Repository layout | Flat addon at repo root | `apps/odoo/relayruntime/` |
| Odoo module name | `whatsapp_simple` | `relayruntime` |
| Display name | WhatsApp Simple | RelayRuntime |
| Python imports | `odoo.addons.whatsapp_simple` | `odoo.addons.relayruntime` |
| XML / external ID prefix | `whatsapp_simple.*` | `relayruntime.*` |
| Model `_name` (e.g. `whatsapp.bulk.campaign`) | `whatsapp.*` | **Unchanged** |

PostgreSQL table names for `whatsapp.*` models are **unchanged**. Business logic semantics (lease, idempotency, execution) are **unchanged** at 19.0.6.0.0 restructure.

---

## New installations

1. Clone repository; add **`apps/odoo`** to `addons_path`.
2. Install: `-i relayruntime`.
3. Configure provider settings; validate with Mock Provider.
4. Document `addons_path` in your deployment runbook.

No `whatsapp_simple` module should be present.

---

## Existing production databases

**There is no supported automatic in-place module rename** in this repository.

### Risk summary

| Risk | Impact |
|------|--------|
| XML ID prefix change | Menu actions, security refs, automated upgrades may break |
| Duplicate module install | Two modules fighting over same business concepts |
| Lost `ir.model.data` linkage | Customizations referencing `whatsapp_simple.*` fail |
| Provider config | Must re-enter or migrate `whatsapp.config` rows manually |

### Recommended cutover (Option A)

1. **Freeze** outbound campaigns; wait for running jobs to finish or reconcile stale state ([runbook](docs/operations/RUNBOOK.md)).
2. **Export** campaign/log evidence if audit requires continuity of IDs in external systems.
3. **Staging rehearsal** — full cutover on copy of production DB.
4. **Maintenance window** on production.
5. **Uninstall** `whatsapp_simple` (do **not** run both modules).
6. **Install** `relayruntime`; reconfigure WhatsApp settings.
7. **Smoke test**: Mock bulk → retry failed → verify execution lease blocks overlap.
8. **Rollback plan**: restore DB backup if failure; do not partial-install.

### Advanced (Option B)

Custom migration of `ir.module.module` and `ir.model.data` XML IDs from `whatsapp_simple` to `relayruntime`.

- **Not shipped** in this repo.
- Requires tested SQL/ORM scripts and QA on staging.
- Engage only with DBA and Odoo partner support.

---

## Addons path change

```diff
-addons_path = ...,/path/to/whatsapp_simple
+addons_path = ...,/path/to/relayruntime/apps/odoo
```

Verify module discovery:

```bash
odoo-bin -c odoo.conf -d YOUR_DB --addons-path=... --stop-after-init
# Apps list should show RelayRuntime (relayruntime)
```

---

## XML ID and customization audit

Before cutover, search custom modules and studio exports for:

```
whatsapp_simple.
```

Update references to `relayruntime.` **only after** validating XML ID remap strategy.

Inherited views, server actions, and automated actions are common breakage points.

---

## Database migration warnings

| Topic | Guidance |
|-------|----------|
| Historical logs | Remain in `whatsapp_message_log` tables (model names unchanged) |
| Campaigns in `running` | Reconcile before uninstall; see [stale reconciliation](docs/recovery/stale-execution-reconciliation.md) |
| `ir.attachment` links | Campaign M2M may need validation after reinstall |
| Backups | Full DB + filestore backup before uninstall |

**Uninstalling `whatsapp_simple` may remove module-owned data** depending on Odoo uninstall policy and field `ondelete`—verify on staging.

---

## Rollback precautions

| If cutover fails | Action |
|------------------|--------|
| Before uninstall | Restore DB from pre-window backup |
| After uninstall | Restore backup; do not attempt to “reinstall whatsapp_simple” without restore if data was dropped |
| Partial relayruntime install | Remove module; restore backup; post-mortem on staging |

Keep backup until relayruntime has run successfully through at least one full business cycle.

---

## Version reference

Repository restructure: module **19.0.6.0.0** — see [CHANGELOG.md](CHANGELOG.md).

---

## Related documentation

- [Embedded runtime](docs/deployment/embedded-runtime.md)
- [Runtime boundaries](docs/architecture/runtime-boundaries.md)
- [Local setup](docs/deployment/LOCAL_SETUP.md)
