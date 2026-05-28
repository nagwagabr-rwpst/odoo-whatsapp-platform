# Odoo addons path

Add **this directory** to Odoo `addons_path`:

```ini
addons_path = /path/to/odoo/addons,/path/to/relayruntime/apps/odoo
```

The installable module is:

```
relayruntime/   →  apps/odoo/relayruntime/
```

Do **not** point `addons_path` at the repository root.
