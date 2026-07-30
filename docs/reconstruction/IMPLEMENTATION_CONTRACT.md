# MERGE-003 — Implementation Contract

**Status:** EFFECTIVE  
**ARB decision:** APPROVED WITH CONDITIONS (MERGE-002)  
**Effective when:** baseline tags exist and branch `reconstruct/unify-ui-on-runtime` is checked out.

## Frozen baselines

| Tag | Commit | Role |
|-----|--------|------|
| `lineage-a-2188035` | `2188035403fe49e36b1d3589f0738ad9216f736d` | UI source (import-only) |
| `lineage-b-63975c4` | `63975c48f53034a753314e31b13ce9239d096594` | Architectural foundation |
| `merge-base-6ec77be` | `6ec77bec8d39f2dcac1ae400867f58afb2dc1577` | Historian reference |

## Working branch

`reconstruct/unify-ui-on-runtime` — branched from `63975c4`.

## Target identity

| Field | Value |
|-------|-------|
| Technical module | `relayruntime` (nested package) |
| Display name | `RWPST RelayRuntime` |
| Version | `19.0.6.1.0` |

## Hard rules

1. Never `git merge` tip `2188035` into the reconstruction branch.
2. Never replace B-LOCK runtime files with Lineage A copies.
3. Never place a flat `__manifest__.py` at repository root.
4. Never drop idempotency, outbound intent, or execution lease semantics.
5. No ownership-matrix deviation without a new ARB review.

## Sequence

Follow MERGE-002 Steps 0–19 exactly. See [OWNERSHIP.md](OWNERSHIP.md) for path authority.

## SCSS scope

Import Lineage A asset registration including `web._assets_primary_variables` hooks.  
Emergency rollback (Asset Test failure): narrow to `web.assets_backend` only — allowed without ARB.

## Change control

**Requires ARB:** changing B-LOCK authority; adopting A campaign/log/bulk_service as base; runtime extraction during unify; background queue; tip-to-tip merge; skipping Steps 16 or 19.

**Allowed without ARB:** KPI query adaptation; XML ID / import retargeting; ACL additions; i18n regen; emergency SCSS narrow; bugfixes preserving ownership.
