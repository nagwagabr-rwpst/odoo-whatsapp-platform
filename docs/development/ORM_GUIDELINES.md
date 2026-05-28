# ORM Guidelines

[← Documentation index](../README.md) · [Runtime Safety Rules](RUNTIME_SAFETY_RULES.md)

## Model design conventions

| Pattern | Usage in this module |
|---------|---------------------|
| Readonly campaign/execution fields | Set via service methods, not arbitrary UI writes |
| `create_log` factory | Central log creation with idempotency handling |
| Custom lifecycle methods | `_mark_finished`, `begin_campaign_execution`, not overrides of `write` on state |
| SQL constraints | Idempotency, retry fingerprint, execution UUID |

## Writes during bulk send

| Do | Don't |
|----|-------|
| Update execution attempt counters | Write campaign counters every attachment byte |
| Use `flush_recordset` before provider I/O | `cr.commit()` inside recipient loop |
| Use savepoint on retry campaign create | Broad `except: pass` around provider errors |
| `search` with idempotency key before send | Create duplicate logs without key |

## Transactions

```python
# Implemented pattern
log = log_model.create_log(..., delivery_state='queued')
log.commit_outbound_intent()  # flush only
result = service.send_text_message(...)
log.write({'delivery_state': 'sent' or 'failed'})
```

```python
# Do not reintroduce
self.env.cr.commit()  # inside WhatsAppBulkSender loop
```

## Concurrency

| Pattern | Location |
|---------|----------|
| `FOR UPDATE` | `whatsapp.bulk.campaign._lock_for_execution` |
| Lease check | `whatsapp.bulk.execution._assert_no_active_lease` |
| IntegrityError recovery | `create_log`, retry campaign create |

Prefer extending execution model over ad-hoc campaign flags for "is running".

## Related fields and computed fields

- Use `related`/`store` for dashboard convenience (`total_success`, etc.)
- `processing_state` on campaign is legacy mapping — do not use as execution authority

## Attachments

- Product attachments: reuse search in `WhatsAppProductService.product_to_attachment`
- Campaign M2M: `bypass_search_access=True` — understand security implications

## Multi-company

Always set `company_id` on campaigns/logs from wizard context. Record rules filter by `company_ids`.

## Testing ORM code

Use `TransactionCase` and Mock provider. Patch `send_to_partners` only when testing wizard plumbing, not when testing integrity.

## Further reading

- [Transaction Model](../architecture/TRANSACTION_MODEL.md)
- [Data Model](../architecture/DATA_MODEL.md)
