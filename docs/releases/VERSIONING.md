# Versioning

[← Documentation index](../README.md)

## Scheme

**Format:** `19.0.MAJOR.MINOR.PATCH` (Odoo module series)

**Current:** `19.0.5.5.0` (see `__manifest__.py`)

| Segment | Meaning (project convention) |
|---------|------------------------------|
| `19.0` | Odoo platform major |
| `5` | Feature / architecture generation (provider layer, stabilization, execution attempts) |
| `5` | Minor functional release within generation |
| `0` | Patch |

## Milestone reference (historical)

| Version | Theme |
|---------|-------|
| 19.0.3.x | Campaign monitor, observability, retry campaigns |
| 19.0.4.x | Provider adapter architecture |
| 19.0.5.0.x | Mock provider |
| 19.0.5.4.x | Transactional integrity stabilization (idempotency, no mid-loop commits) |
| 19.0.5.5.0 | Execution attempts, lease, heartbeat, outbound intent |

## Compatibility

| Dependency | Requirement |
|------------|-------------|
| Odoo | 19 Community (tested target) |
| Python | Per Odoo 19 |
| PostgreSQL | Per Odoo 19 |

## API stability

| Surface | Stability |
|---------|-----------|
| XML IDs / menus | Treat as stable within major module generation |
| Python services public methods | Unstable — internal module use |
| `whatsapp.config` fields | Stable; new fields additive |
| SQL constraints | Breaking if removed — migration required |

## Further reading

- [CHANGELOG.md](../../CHANGELOG.md)
- [Release Process](RELEASE_PROCESS.md)
