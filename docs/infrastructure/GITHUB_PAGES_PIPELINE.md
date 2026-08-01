# GitHub Pages Deployment Pipeline (RWPST Standard)

[← Documentation index](../README.md)

Reusable pipeline for publishing **product websites** from RWPST repositories to GitHub Pages — without publishing the repository root, without a maintained `gh-pages` branch, and without duplicating site files.

This document is the operational standard for:

| Product | Repository (example) | Custom domain (example) |
|---------|----------------------|-------------------------|
| RelayRuntime | `odoo-whatsapp-platform` | `relayruntime.rwpst.com` |
| AI Agents | *(future)* | `*.rwpst.com` |
| AI Academy | *(future)* | `*.rwpst.com` |
| Motion | *(future)* | `*.rwpst.com` |
| Future products | any RWPST product repo | product subdomain under `rwpst.com` |

**Workflow file:** [`.github/workflows/deploy-pages.yml`](../../.github/workflows/deploy-pages.yml)

---

## Problem this solves

GitHub Pages can be pointed at the **repository root**. For product repos that also contain Odoo modules, docs, and tooling, that publishes `README.md` and the whole tree as the “website.”

RWPST product sites live in a dedicated folder:

```text
landing-page/     # current RelayRuntime convention
site/             # preferred future convention
```

The pipeline publishes **only that folder’s contents** as the Pages site root. The repository layout stays unchanged.

---

## Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│  Product repository (e.g. odoo-whatsapp-platform)           │
│                                                             │
│  19.0  (or product release branch)                          │
│    ├── landing-page/   ← website source (unchanged in repo) │
│    ├── relayruntime/   ← product code (never published)     │
│    ├── docs/           ← engineering docs (never published) │
│    └── README.md       ← never served as Pages homepage     │
└──────────────────────────────┬──────────────────────────────┘
                               │ push
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions — Deploy GitHub Pages                       │
│                                                             │
│  1. Checkout branch                                         │
│  2. Copy SITE_SOURCE → _site/ (exclude *.md)                │
│  3. Write .nojekyll (+ optional CNAME)                      │
│  4. upload-pages-artifact → deploy-pages                    │
└──────────────────────────────┬──────────────────────────────┘
                               │ artifact only
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  GitHub Pages (Actions source)                              │
│                                                             │
│  Site root = published artifact                             │
│    index.html, css/, js/, assets/, CNAME, .nojekyll         │
│                                                             │
│  Custom domain → relayruntime.rwpst.com (HTTPS via GitHub)  │
└─────────────────────────────────────────────────────────────┘
```

### Design principles

| Principle | Implementation |
|-----------|----------------|
| Do not move site files | Source stays in `landing-page/` (or `site/`) |
| Do not duplicate site files | Artifact is assembled at deploy time |
| Do not maintain `gh-pages` | Official `actions/deploy-pages` publishes the artifact |
| Publish website only | Artifact excludes repository root and markdown docs |
| Reusable | Three knobs at top of the workflow (`SITE_SOURCE`, `CUSTOM_DOMAIN`, trigger branch) |

---

## Deployment flow

1. Developer (or release process) pushes to branch **`19.0`** (or runs **workflow_dispatch**).
2. Workflow **Deploy GitHub Pages** starts.
3. **Build** job:
   - Validates `SITE_SOURCE` exists and contains `index.html`.
   - Copies that folder into `_site/` (excludes `*.md` so internal READMEs/audits are not public files).
   - Adds `.nojekyll` (disables Jekyll processing).
   - Writes `CNAME` when `CUSTOM_DOMAIN` is set.
   - Uploads `_site/` as a Pages artifact.
4. **Deploy** job deploys the artifact to the `github-pages` environment.
5. GitHub serves the artifact at the Pages URL and, when DNS + CNAME are correct, at the custom domain.

### What is published vs not

| Included | Excluded |
|----------|----------|
| `index.html`, `css/`, `js/`, `assets/` | Repository root (`README.md`, module code, CI scripts) |
| Generated `CNAME`, `.nojekyll` | Markdown under the site folder (`*.md`) |
| | Any path outside `SITE_SOURCE` |

Success check: opening the custom domain (or Pages URL) shows the product website. The repository README is **not** the homepage.

---

## One-time repository setup

Required once per repository (Settings UI — not in git):

1. Open **Settings → Pages**.
2. Under **Build and deployment → Source**, select **GitHub Actions** (not “Deploy from a branch”).
3. After the first successful workflow run, confirm the deployment appears under **Settings → Pages** and the **Environments → github-pages** deployment history.
4. Under **Custom domain**, set the product hostname (e.g. `relayruntime.rwpst.com`) and enable **Enforce HTTPS** once the certificate is ready (usually minutes after DNS validates).

If Source is still “Deploy from a branch” pointed at `/` (root), GitHub will keep serving the README. Switch to **GitHub Actions**.

---

## Custom domain

### This repository

| Item | Value |
|------|--------|
| Custom domain | `relayruntime.rwpst.com` |
| Written by pipeline | `_site/CNAME` on every deploy (`CUSTOM_DOMAIN` env in the workflow) |
| Apex / www | Not used for this product site (subdomain only) |

Keeping `CNAME` in the **artifact** (not necessarily in the git tree) means every deploy re-asserts the domain binding. You can still set the same hostname in **Settings → Pages**; they should match.

### Changing the domain later

1. Update DNS (see below).
2. Set `CUSTOM_DOMAIN` in `.github/workflows/deploy-pages.yml`.
3. Update **Settings → Pages → Custom domain**.
4. Re-run the workflow (push or **workflow_dispatch**).
5. Wait for HTTPS to re-provision, then enable **Enforce HTTPS**.

---

## HTTPS

GitHub Pages provisions a TLS certificate for verified custom domains.

| Step | Expectation |
|------|-------------|
| DNS points correctly | `CNAME` / alias resolves to GitHub Pages |
| Domain listed in Pages settings / artifact `CNAME` | GitHub can issue the cert |
| First enable | Certificate provisioning may take a few minutes |
| Enforce HTTPS | Enable in Settings after the padlock works |

Do **not** terminate TLS elsewhere for this hostname if GitHub Pages is the origin — browsers should hit GitHub’s certificate for `*.rwpst.com` product subdomains served by Pages.

---

## DNS

Point the product subdomain at GitHub Pages for the repository owner.

### Typical record (subdomain)

| Type | Name | Value | Notes |
|------|------|--------|------|
| `CNAME` | `relayruntime` (host: `relayruntime.rwpst.com`) | `<owner>.github.io` | For this repo owner: `nagwagabr-rwpst.github.io` |

### Checklist

- [ ] `CNAME` (or equivalent ALIAS at DNS provider) targets the correct `*.github.io` host — **not** a random IP unless using GitHub’s documented A records for apex domains.
- [ ] No conflicting `A`/`AAAA` records on the same hostname.
- [ ] TTL lowered briefly during cutover if migrating from another host.
- [ ] After DNS propagates, **Settings → Pages** shows the domain as verified.
- [ ] `https://relayruntime.rwpst.com/` loads `index.html` from the Actions deployment.

### Verification commands

```bash
# Should resolve toward GitHub Pages
dig +short relayruntime.rwpst.com CNAME
# or
nslookup relayruntime.rwpst.com

# Should return 200 and HTML (not GitHub blob/README chrome as the document)
curl -sI https://relayruntime.rwpst.com/ | head
```

---

## How to reuse in another RWPST repository

Copy one file, change three values, enable Pages once.

### 1. Copy the workflow

```text
.github/workflows/deploy-pages.yml
```

### 2. Edit product knobs (top of the workflow)

```yaml
on:
  push:
    branches:
      - 'main'          # ← product release / docs branch for that repo

env:
  SITE_SOURCE: site                 # ← preferred folder name going forward
  CUSTOM_DOMAIN: agents.rwpst.com   # ← or "" for default github.io URL
  EXCLUDE_GLOBS: '*.md'
```

### 3. Put the website in that folder

```text
site/
  index.html
  css/
  js/
  assets/
```

(or keep `landing-page/` and set `SITE_SOURCE: landing-page`)

### 4. Enable Pages

**Settings → Pages → Source = GitHub Actions**, set custom domain + Enforce HTTPS.

### 5. Push

A push to the configured branch publishes automatically.

Optional: also copy this document into `docs/infrastructure/GITHUB_PAGES_PIPELINE.md` and adjust the product/domain table.

---

## How to change the published folder

No file moves required beyond choosing the source path.

1. Open `.github/workflows/deploy-pages.yml`.
2. Set:

```yaml
env:
  SITE_SOURCE: site    # was: landing-page
```

3. Ensure `site/index.html` exists.
4. Push to the trigger branch (or run **workflow_dispatch**).

Repository structure elsewhere is untouched. Do **not** point Pages at “branch / root” or “branch / docs” in the UI — the Actions artifact defines the published root.

### Temporary dual support

If a repo is migrating `landing-page/` → `site/`, change `SITE_SOURCE` only after the new folder contains a complete site. The workflow publishes exactly one folder per deploy.

---

## Future maintenance

| Topic | Guidance |
|-------|----------|
| Site content updates | Edit files under `SITE_SOURCE`; push to the trigger branch |
| Pipeline upgrades | Prefer updating `actions/checkout`, `upload-pages-artifact`, and `deploy-pages` major versions in lockstep across RWPST repos |
| Branch rename | Update `on.push.branches` when the product’s published branch changes |
| Domain rename | Update DNS + `CUSTOM_DOMAIN` + Pages settings together |
| Markdown in site folder | Kept out of the artifact via `EXCLUDE_GLOBS`; adjust only if you intentionally want public `.md` URLs |
| Jekyll | `.nojekyll` is always written — leave it |
| Manual `gh-pages` branch | Do not create or push one; delete any legacy branch after Actions is the sole source |
| Broken deploy | Re-run failed workflow from the Actions tab; check `github-pages` environment protection rules if deploys are blocked |
| Org policy | New RWPST product repos should include this workflow before first public URL announcement |

### Explicit non-goals

This pipeline does **not**:

- Redesign or rebuild HTML/CSS/JS
- Move or symlink product/module files
- Publish Odoo addons or engineering documentation
- Replace Odoo.sh / application hosting

It only publishes the static product website folder to GitHub Pages.

---

## Success criteria (RelayRuntime)

After a push to **`19.0`** with Pages Source = **GitHub Actions**:

| Check | Expected |
|-------|----------|
| Workflow | **Deploy GitHub Pages** completes green |
| Homepage | `https://relayruntime.rwpst.com/` serves `landing-page/index.html` content |
| Isolation | Repository `README.md` is not the Pages homepage |
| Scope | Only website assets (plus `CNAME` / `.nojekyll`) are in the artifact |
| Reuse | Same workflow pattern works in other RWPST repos with knob changes only |

---

## Related

- Website source (this repo): [`landing-page/`](../../landing-page/)
- Marketing spec: [`docs/marketing/LANDING_PAGE_SPEC.md`](../marketing/LANDING_PAGE_SPEC.md)
- Workflow: [`.github/workflows/deploy-pages.yml`](../../.github/workflows/deploy-pages.yml)
