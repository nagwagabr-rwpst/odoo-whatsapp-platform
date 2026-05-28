# Execution package (planned)

**Status:** Placeholder — logic currently in `apps/odoo/relayruntime/models/whatsapp_bulk_execution.py` and `services/whatsapp_bulk_service.py`.

**Future home for:**

- `begin_execution` / `finish` orchestration (framework-agnostic)
- Lease and heartbeat policy engine
- Execution state machine

**Boundary:** No Odoo `env` imports in extracted core.
