<div align="center">

<img src="relayruntime/static/description/HorizontalLogo.png" alt="RWPST RelayRuntime" width="280"/>

<br/><br/>

<img src="relayruntime/static/description/banner_1.png" alt="RelayRuntime — Enterprise Messaging Runtime for Odoo Community" width="920"/>

# RelayRuntime

### Enterprise Messaging Runtime for Odoo Community

Built around a runtime — not just an integration.

<br/>

[![Odoo](https://img.shields.io/badge/Odoo-19-714B67?style=flat-square&logo=odoo&logoColor=white)](https://www.odoo.com)
[![Edition](https://img.shields.io/badge/Edition-Community-0F172A?style=flat-square)](https://www.odoo.com)
[![License](https://img.shields.io/badge/License-LGPL--3-1E3A8A?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Odoo%2019%20Community-2563EB?style=flat-square)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![Version](https://img.shields.io/badge/Version-19.0.6.1.0-475569?style=flat-square)](CHANGELOG.md)

<br/>

[Landing Page](landing-page/) · [Documentation](docs/README.md) · [Release Notes](CHANGELOG.md) · [Odoo Apps](https://apps.odoo.com/apps/modules/browse?search=RelayRuntime)

</div>

---

## Overview

RelayRuntime is an **Enterprise Messaging Runtime** for Odoo Community.

It places a messaging layer between Odoo and the active WhatsApp provider — with campaign execution, operator retry, a Delivery Dashboard, and an Operational Command Center.

Live sending uses Green API. Mock Provider covers demos and tests. One active provider configuration is used per company.

Enterprise messaging starts here.

---

## Why RelayRuntime

| Traditional Connector | RelayRuntime |
|---|---|
| Single send button | Campaign history and a delivery log |
| Fire-and-forget sends | Operator retry for failed and skipped recipients |
| No outcome record | Delivery Dashboard (sent, failed, skipped) |
| Basic message logs | Operational Command Center |
| One-off connector setup | Green API live sending and Mock Provider for tests |
| Ad-hoc sending | Attended campaign execution on Odoo 19 Community |

```text
Enterprise Messaging Runtime
            │
            ▼
 Operational Command Center
            │
            ▼
    Provider Abstraction
            │
            ▼
   Messaging Providers
```

---

## Key Features

| | |
|---|---|
| **Operational Command Center** | Manage KPIs, campaigns, logs, and runtime health from one dashboard. |
| **Provider Setup** | One active provider per company. Green API sends live messages. Mock Provider simulates sends. |
| **Campaign Execution** | Each campaign runs in the operator's request, recipient by recipient, with a delivery log for every contact. |
| **Operator Retry** | From a finished campaign, retry failed and skipped contacts in a linked campaign that sends immediately. |
| **Delivery Dashboard** | Totals for sent, failed, and skipped, based on the provider HTTP response. |
| **Live Monitor** | Review campaign state and message logs from the campaign monitor. |
| **Runtime Settings** | Configure providers and runtime behavior in one place. |
| **Analytics** | Track delivery performance and runtime KPIs. |
| **Attachment Support** | Coordinate outbound messaging with attachments and catalogs. |
| **Enterprise Architecture** | Separate ERP workflows, runtime control, and provider adapters. |

---

## Screenshots

### Command Center

![RelayRuntime Operational Command Center](relayruntime/static/description/screenshots/01_command_center.png)

### Runtime Settings

![RelayRuntime Runtime Settings](relayruntime/static/description/screenshots/02_settings.png)

### Bulk Messaging

![RelayRuntime Bulk Messaging wizard](relayruntime/static/description/screenshots/03_bulk_wizard.png)

### Delivery Dashboard

![RelayRuntime Delivery Dashboard](relayruntime/static/description/screenshots/06_delivery_dashboard.png)

---

## Architecture

```text
                 Business Logic
                       │
                       ▼
                 RelayRuntime
                       │
                       ▼
              Active provider
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Green API       Mock Provider
          Live sending    Simulated sends
```

Registered adapters — Meta Cloud API, Evolution API, UltraMsg, Twilio, Gupshup, and Custom — are not available for live sending in this release.

Campaigns, logs, and retry stay in RelayRuntime.

---

## Installation

```bash
git clone https://github.com/nagwagabr-rwpst/odoo-whatsapp-platform.git
```

1. Add the repository path to Odoo `addons_path`.
2. Restart Odoo.
3. Update the Apps list.
4. Install **RWPST RelayRuntime**.

Installable module: `relayruntime/`

---

## Quick Start

1. Open **RelayRuntime** after installation.
2. Configure a provider under **Runtime Settings**.
3. Validate with Mock Provider, then connect Green API for live delivery.
4. Launch a bulk campaign from the Command Center.
5. Track results in the Delivery Dashboard and Live Monitor.

---

## Providers

| Provider | Status |
|---|---|
| Green API | Live |
| Mock Provider | Simulated |
| Meta Cloud API | Registered, not sendable |
| Evolution API | Registered, not sendable |
| UltraMsg | Registered, not sendable |
| Twilio | Registered, not sendable |
| Gupshup | Registered, not sendable |
| Custom | Registered, not sendable |

One active provider configuration per company.

---

## Project Structure

```text
odoo-whatsapp-platform/
├── landing-page/     Public product website
├── branding/         Official brand kit (SVG / PNG)
├── docs/             Architecture, runtime, operations
├── relayruntime/     Installable Odoo 19 module
├── runtime/          Runtime foundation (extraction path)
├── scripts/          Release and maintenance tooling
├── tests/            Verification suites
├── CHANGELOG.md
├── LICENSE
└── README.md
```

---

## Roadmap

### Version 1 — Enterprise Runtime

- Enterprise Messaging Runtime for Odoo Community
- Provider abstraction layer
- Operational Command Center
- Campaign execution and operator retry
- Delivery Dashboard and campaign operations

### Version 2 — Platform Expansion

- Developer SDK
- REST API surface
- Expanded technical documentation
- Deeper runtime-service extraction

---

## Documentation

| Resource | Link |
|---|---|
| Landing Page | [landing-page/](landing-page/) |
| Documentation | [docs/README.md](docs/README.md) |
| Release Notes | [CHANGELOG.md](CHANGELOG.md) |
| Migration Guide | [MIGRATION.md](MIGRATION.md) |
| Support | [SUPPORT.md](SUPPORT.md) |
| Security | [SECURITY.md](SECURITY.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Odoo Apps | [Browse RelayRuntime](https://apps.odoo.com/apps/modules/browse?search=RelayRuntime) |

---

## License

RelayRuntime is released under the **LGPL-3.0** license.

See [LICENSE](LICENSE).

---

**Enterprise Messaging Starts Here**

RelayRuntime · RWPST · Odoo 19 Community
