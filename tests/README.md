# Tests

Odoo module tests live in:

```
apps/odoo/relayruntime/tests/
```

Run:

```bash
odoo-bin -c odoo.conf -d TEST_DB --test-tags=relayruntime --stop-after-init
```

Future repository-level integration tests may be added here.
