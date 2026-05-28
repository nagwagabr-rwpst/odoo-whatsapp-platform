## Summary

<!-- What does this PR change and why? -->

Fixes #<!-- issue -->

## Change type

- [ ] Bug fix
- [ ] Documentation
- [ ] CI / repository hygiene
- [ ] Runtime / business logic *(requires explicit reviewer approval — see checklist below)*

> **Repository-only PRs** should not change `models/`, `services/`, or `wizard/` behavior unless explicitly intended.

## Architecture impact

<!-- Describe changes to execution authority, campaign projection, providers, or data model -->

| Area | Impact |
|------|--------|
| Execution attempt authority | None / describe |
| Campaign projection | None / describe |
| Provider layer | None / describe |
| New persistent models | None / describe |

## Transaction boundary impact

- [ ] No new `cr.commit()` in bulk send loops
- [ ] No hidden transaction boundaries introduced
- [ ] Outbound intent / flush semantics unchanged OR documented in `/docs`

## Retry impact

- [ ] Retry fingerprint / lineage unchanged OR migration documented
- [ ] Idempotency key semantics unchanged OR migration documented
- [ ] No new duplicate-send paths introduced

## Runtime safety validation

- [ ] I read [Runtime Safety Rules](docs/development/RUNTIME_SAFETY_RULES.md)
- [ ] Lease / heartbeat / reconcile paths considered
- [ ] Exception paths still call `execution.finish()` where applicable *(if code touched)*

## Testing performed

- [ ] `python scripts/ci_validate.py` (local)
- [ ] CI workflow passes
- [ ] Odoo tests: `<!-- command or N/A for docs-only -->`
- [ ] Manual: Mock provider bulk / retry *(if runtime touched)*

## Documentation

- [ ] `/docs` updated for behavior changes
- [ ] `CHANGELOG.md` entry under `[Unreleased]` or version section
- [ ] `__manifest__.py` version bumped *(if releasing)*

## Screenshots / logs

<!-- If UI changed -->

## Release notes snippet

<!-- One line for GitHub Release description -->
