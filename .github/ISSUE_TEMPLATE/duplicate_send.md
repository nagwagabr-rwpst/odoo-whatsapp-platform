---
name: Duplicate Send
about: Report the same recipient receiving duplicate WhatsApp messages
title: "[Duplicate]: "
labels: ["duplicate-send", "integrity", "triage"]
assignees: []
---

## Environment

| Field | Value |
|-------|-------|
| **Odoo version** | |
| **Module version** | |
| **Provider** | <!-- green_api / mock_provider --> |
| **Deployment** | |

## Recipient

| Field | Value |
|-------|-------|
| **Partner ID** | |
| **Phone number** (normalized) | |
| **Company** | |

## Send instances

<!-- List each delivery with timestamp -->

| # | Approx. time (UTC) | Campaign ID | Execution ID | Log ID | Provider message ID |
|---|-------------------|-------------|--------------|--------|---------------------|
| 1 | | | | | |
| 2 | | | | | |

## Execution attempt context

| Field | Value |
|-------|-------|
| First execution UUID | |
| Second execution UUID | |
| Same campaign? | <!-- yes / no (retry child) --> |
| Idempotency key (if visible on log) | `campaign:{id}:partner:{id}` |

## Retry lineage

<!-- Was this after Retry Failed Recipients? New retry campaign? -->

- [ ] Same campaign re-run attempt
- [ ] Retry child campaign (`parent_campaign_id` set)
- [ ] Manual second bulk to same contacts
- [ ] Provider/dashboard shows duplicate without matching Odoo logs
- [ ] Unknown

**Parent / child campaign IDs:**

```
```

## Timestamps

| Event | Time |
|-------|------|
| First log `outbound_intent_at` | |
| First log terminal state | |
| Second send | |
| Worker restart / timeout (if any) | |

## Provider evidence

<!-- Green API / provider dashboard screenshots or message IDs — redact secrets -->

<details>
<summary>Provider response / dashboard</summary>

```
```

</details>

## Hypothesis (optional)

- [ ] Retry campaign (new campaign id — expected resend path)
- [ ] HTTP rollback after provider success
- [ ] Concurrent execution race
- [ ] Provider transport retry
- [ ] Reconciliation + manual retry
- [ ] Other

## Checklist

- [ ] I verified idempotency keys on message logs for the campaign(s)
- [ ] I read [Retry and Replay](docs/runtime/RETRY_AND_REPLAY.md) and [Known Limitations](docs/architecture/KNOWN_LIMITATIONS.md)
- [ ] No API tokens included in this report
