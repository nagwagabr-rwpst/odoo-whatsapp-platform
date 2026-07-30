# RelayRuntime — Official Product Vision

**Document type:** Constitutional Product Document  
**Status:** Authoritative  
**Audience:** Architecture, Engineering, QA, Release Management, Documentation, Roadmap Planning, Solution Partners  
**Validity:** Intended to remain stable across product generations  

This document defines **what RelayRuntime is**, **what it is not**, and **the boundaries that all future work must respect**.  
It is the product constitution. Implementation details, repository state, and temporary gaps do not override it.

---

# 1. Product Definition

## One sentence

**RelayRuntime is a replay-safe operational messaging execution runtime for Odoo Community that owns campaign execution authority, delivery outcomes, recovery, and provider-independent outbound messaging.**

## Professional definition

RelayRuntime is an enterprise software product that provides a controlled **execution plane** for outbound operational messaging inside (and eventually beside) Odoo Community Edition.

It is not a messaging UI skin, not a CRM, and not a marketing automation suite.  
It is the system that decides:

- when an execution attempt begins and ends
- who owns a running execution
- what happened to each recipient
- how retries relate to prior attempts
- how recovery proceeds after interruption
- how providers are invoked without leaking vendor semantics into business workflows

Odoo Community supplies ERP identity, partners, products, sales context, authorization, and UI surfaces.  
RelayRuntime supplies **execution correctness under failure** for outbound messaging campaigns and related operational sends.

The product is designed as a **platform-oriented runtime**, initially delivered as an Odoo application module, with a long-term architecture that separates ERP orchestration from runtime execution without changing the product identity.

---

# 2. Problem Statement

## The real-world problem

Organizations that run outbound messaging from an ERP (order notifications, catalog offers, operational broadcasts, customer follow-ups) face a reliability gap that ordinary “send WhatsApp” integrations do not solve:

| Failure mode | Business consequence |
|--------------|----------------------|
| Worker/process dies mid-campaign | Unknown progress; risk of duplicate sends or silent incomplete runs |
| Partial delivery | Operators cannot distinguish sent, failed, skipped, and unprocessed |
| Naive retry | Duplicate campaigns, duplicate messages, corrupted counters |
| Provider outages / rate limits | Uncontrolled stoppage without recoverable state |
| Stale “running” records | False operational status; conflicting recovery |
| Vendor lock-in to one API | Business workflows coupled to a single gateway |
| No execution lineage | Auditors and operators cannot explain what ran and why |

These are **operational runtime problems**, not marketing feature problems.

## Who experiences the problem

- **Operations and sales teams** who must send bulk or high-volume messages from Odoo and need trustworthy status
- **System administrators** who must keep messaging safe under upgrades, concurrency, and partial failure
- **Implementation consultants and solution partners** who must deliver messaging without building a custom reliability layer per customer
- **Business owners** who cannot accept silent duplicates, lost campaigns, or unverifiable delivery history

## Why Odoo Community is insufficient without RelayRuntime

Odoo Community provides partners, products, sales orders, mail infrastructure, and UI frameworks. It does **not** provide:

- a messaging **execution authority** with lease ownership and heartbeat semantics
- **replay-safe** bulk execution with recipient-level truth
- **retry lineage** as first-class product behavior
- **provider-independent** outbound messaging contracts
- operational campaign monitoring grounded in execution state rather than optimistic UI counters alone

Without RelayRuntime, messaging integrations become fragile scripts: they send, but they do not own execution correctness. RelayRuntime exists to close that gap.

---

# 3. Target Users

## 3.1 System Administrator

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | Install/upgrade the module, configure providers and limits, manage security groups, monitor logs, ensure multi-company isolation |
| **Goals** | Stable upgrades, safe credentials, predictable resource use, recoverable failures |
| **Interaction** | Settings, provider configuration, security, observability, operational runbooks |

## 3.2 Operations Manager

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | Oversee campaign execution health, intervene on failures, authorize retries, interpret delivery outcomes |
| **Goals** | Know what ran, what failed, what is safe to retry; avoid duplicate operational risk |
| **Interaction** | Campaign monitor, delivery dashboard, execution status, retry workflows, failure diagnostics |

## 3.3 Sales User

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | Send messages to customers/prospects; run catalog or offer campaigns tied to partners and products |
| **Goals** | Complete sends with clear outcomes; continue sales work from Odoo without leaving ERP context |
| **Interaction** | Send wizards, partner/sale-order entry points, campaign creation, basic progress visibility |

## 3.4 Marketing User

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | Execute outbound broadcast-style campaigns for offers and product communication |
| **Goals** | Controlled campaign execution with delivery tracking—not a full marketing automation platform |
| **Interaction** | Bulk campaign flows, recipient selection, message/attachment/product content, monitoring |

> **Boundary note:** Marketing users may *use* RelayRuntime for execution. Campaign journey design, segmentation engines, and multi-channel automation belong outside RelayRuntime.

## 3.5 Customer Service / Support Agent

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | May trigger operational outbound notices; may need delivery history context |
| **Goals** | Reliable outbound notification and auditability of what was sent |
| **Interaction** | Limited send entry points and message logs; **not** an inbox or ticket console |

## 3.6 Developer / Technical Integrator

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | Extend providers, integrate ERP hooks, automate tests, respect runtime contracts |
| **Goals** | Stable APIs/contracts, provider adapters, upgrade-safe extension points |
| **Interaction** | Provider abstraction, service facades, runtime safety rules, documentation contracts |

## 3.7 Solution Partner

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | Package RelayRuntime into customer solutions; configure providers; train operators |
| **Goals** | A bounded, supportable product with clear scope and enterprise readiness criteria |
| **Interaction** | Full product surface within documented boundaries; no expectation of building CRM/helpdesk inside RelayRuntime |

## 3.8 Implementation Consultant

| Dimension | Definition |
|-----------|------------|
| **Responsibilities** | Map customer messaging processes to RelayRuntime capabilities; define security and operational procedure |
| **Goals** | Fit-for-purpose deployment without scope creep into adjacent enterprise systems |
| **Interaction** | Campaign design within product scope, settings, ACL, monitoring, recovery procedures |

---

# 4. Product Scope

Everything below **is** RelayRuntime. Each item belongs because it is required for a trustworthy messaging **execution runtime**.

## 4.1 Messaging Runtime

Owns the lifecycle of outbound execution: start, progress, terminal states, and authority under concurrency.  
**Why:** Without a runtime, messaging is a fire-and-forget script.

## 4.2 Campaign Execution

Runs bulk (and related) outbound campaigns as controlled execution attempts against defined recipients and payloads.  
**Why:** Campaigns are the primary business unit of operational messaging.

## 4.3 Execution Authority

A single authoritative record of what an attempt did (identity, ownership, counters, terminal outcome). Campaign UI aggregates are projections of that authority.  
**Why:** Ambiguous “source of truth” causes unsafe recovery.

## 4.4 State Management

Explicit campaign and execution states with defined transitions (draft, running, completed, completed with errors, stopped, failed, reconciled where applicable).  
**Why:** Operators and systems must share one state language.

## 4.5 Lease / Ownership Coordination

At most one active owner per execution scope; stale ownership must be detectable.  
**Why:** Concurrent overlapping runs corrupt delivery and counters.

## 4.6 Heartbeat & Liveness

Periodic proof that an execution is still alive.  
**Why:** Distinguishes active work from abandoned “running” zombies.

## 4.7 Replay Protection & Replay-Safe Recovery

Re-invoking execution paths must not corrupt aggregates or invent inconsistent history; recovery is controlled, not ad hoc.  
**Why:** Failures are normal; unsafe replay is the primary enterprise risk.

## 4.8 Idempotency (Recipient / Intent Level)

Outbound intents and recipient outcomes must resist duplicate harmful side effects within defined rules.  
**Why:** Retries and restarts are inevitable.

## 4.9 Retry Logic & Retry Lineage

Retries are first-class: child campaigns/attempts with parent linkage and deduplicated retry identity—not silent mutation of history.  
**Why:** Auditable recovery requires lineage.

## 4.10 Provider Abstraction

Business and runtime layers invoke a provider-neutral contract; vendor APIs live behind adapters.  
**Why:** ERP workflows must outlive any single gateway.

## 4.11 Provider Management

Configuration, validation, credentials handling, capability declaration, and selection of active provider.  
**Why:** Runtime cannot execute without governed provider access.

## 4.12 Delivery Tracking

Per-recipient outcome records (sent / failed / skipped / in-progress) with failure context where available.  
**Why:** Recipient-level truth is the basis of monitoring and retry.

## 4.13 Message Logging

Structured operational logs for campaign lifecycle, API interactions (sanitized), and attachment handling.  
**Why:** Observability and post-incident diagnosis are product requirements.

## 4.14 Campaign Monitoring

Operational views of running and historical campaigns grounded in execution progress and outcomes.  
**Why:** Long-running messaging without monitoring is operationally blind.

## 4.15 Delivery / Operational Dashboards

Summaries of delivery outcomes for operators (counts, drill-downs to logs).  
**Why:** Managers need aggregate signal without reading raw tables.

## 4.16 Execution Safety Controls

Limits, delays, MIME/duplicate checks, empty-campaign guards, cooldown behavior, and related safety validators.  
**Why:** Unbounded sending creates provider bans, legal risk, and data damage.

## 4.17 Attachment & Media Coordination

Consistent handling of attachments/media for outbound sends within provider capabilities.  
**Why:** Partial attachment failure is a major source of inconsistent campaigns.

## 4.18 Product Catalog Messaging Support

Sending product-oriented content (text/images derived from Odoo products) as part of campaign payloads.  
**Why:** ERP-native commercial messaging is a core use case—not a separate commerce app.

## 4.19 ERP Integration Surfaces

Integration with Odoo partners, products, and sales context for entry points and business linkage.  
**Why:** RelayRuntime is ERP-first; messaging must attach to business records.

## 4.20 Settings & Configuration

Company-scoped settings for providers, limits, observability, and operational parameters.  
**Why:** Runtime behavior must be governable without code changes.

## 4.21 Security & Access Control

Roles, access rights, and record rules appropriate to messaging configuration and campaign data.  
**Why:** Credentials and customer contact channels are sensitive assets.

## 4.22 Observability

Operator-visible status, diagnostics, and logging sufficient to answer: what ran, when, for whom, with what outcome.  
**Why:** Runtime without observability cannot be operated enterprise-wide.

## 4.23 Upgrade Safety & Odoo Community Compatibility

Compatible with Odoo Community Edition upgrade practices; migrations preserve execution history semantics.  
**Why:** Enterprise customers upgrade; product identity must survive.

## 4.24 Extensibility via Provider & Integration Contracts

Documented extension points for providers and controlled ERP hooks—without absorbing adjacent products.  
**Why:** Partners need extension without forking the runtime core.

---

# 5. Product Boundaries

The following are **intentionally outside** RelayRuntime. Adjacent products may integrate with RelayRuntime; they must not be absorbed into it.

| Domain | Why it is outside |
|--------|-------------------|
| **CRM** | CRM owns pipeline, activities, lead scoring, and relationship management. RelayRuntime owns outbound execution, not relationship strategy. |
| **Helpdesk / Ticketing** | Ticket lifecycle, SLAs, and agent assignment are support-platform concerns. |
| **Customer Support Inbox** | Inbound conversation triage is an inbox product, not an execution runtime. |
| **Conversation CRM / Contact Center** | Omnichannel agent desktops and live conversation routing exceed messaging execution scope. |
| **Chatbot Builder** | Dialog design, NLU, and bot flows are AI/conversation products. |
| **AI Agent Framework** | Autonomous agents, tool-calling, and LLM orchestration are separate platforms. |
| **Marketing Automation** | Journeys, drip sequences, A/B experimentation platforms, and multi-channel orchestration are MA products. RelayRuntime may *execute* a send requested by such systems; it does not *be* them. |
| **Social Media Platform** | Publishing, scheduling, and social analytics are not operational messaging runtime. |
| **Billing / Subscription System** | Monetization of messaging credits or SaaS billing is a commercial platform concern (except local operational limits). |
| **Website Builder** | Site content and e-commerce storefronts belong to website products. |
| **Document Management** | DMS is not required for execution authority; attachments are transport payload, not a DMS suite. |
| **Full Inbound Messaging Platform** | Receiving, threading, and customer reply management as a primary product is out of scope (provider webhooks may exist later as integration, not as inbox product). |
| **Exactly-Once Distributed Messaging Guarantees** | Without provider + ledger support, claiming distributed exactly-once is dishonest; RelayRuntime targets replay-safe operational recovery instead. |
| **Global Multi-Region Active-Active Consensus** | Distributed systems consensus is not part of the core product identity. |

**Boundary rule:** If a feature does not improve **execution correctness, delivery truth, provider independence, ERP-linked outbound orchestration, or operational recoverability**, it is presumed out of scope until this constitution is amended.

---

# 6. Core Product Principles

These principles are non-negotiable. Features that violate them are defects, not roadmap items.

## 6.1 Provider Independence

Runtime and business workflows must not hard-depend on a single vendor’s API shapes. Adapters translate; the product contract remains stable.

## 6.2 ERP-First

Odoo business objects (partners, products, sales context, company, ACL) are the natural home of orchestration. Messaging serves ERP processes; ERP is not bolted onto a chat app.

## 6.3 Execution Safety

No send path may bypass safety controls that protect against empty runs, unsafe duplicates, unbounded volume, or invalid payloads within product rules.

## 6.4 Replay Protection

Recovery and re-entry must be designed so re-invocation does not silently corrupt state. Replay-safe is a product promise; “hope it works” is not.

## 6.5 Idempotency

Where the product records outbound intent or recipient outcome, repeated attempts follow explicit idempotent rules. Side effects are bounded and explainable.

## 6.6 Execution Authority

When UI aggregates and execution records disagree, **execution attempt + recipient logs** define what happened for that run.

## 6.7 Observability

Operators must be able to determine execution identity, timing, ownership, and outcomes without reading source code.

## 6.8 Honest Limits

The product must not claim distributed exactly-once, infinite scale, or provider guarantees it cannot enforce. Documented limits are part of product integrity.

## 6.9 Upgrade Safety

Schema and behavior changes must preserve historical campaign/execution meaning or provide explicit migration semantics.

## 6.10 Odoo Community Compatibility

The primary delivery vehicle remains compatible with Odoo Community Edition. Enterprise Edition features must not become silent hard requirements for core product identity.

## 6.11 Modularity

Orchestration (ERP/UI/ACL) and execution (runtime authority/recovery) must remain conceptually separable even when co-deployed.

## 6.12 Extensibility

Partners extend via contracts (providers, documented hooks), not by forking core execution semantics.

## 6.13 Maintainability

Complexity that does not serve execution correctness or operability is rejected. Prefer clear state machines over clever shortcuts.

## 6.14 Failure-First Design

Interruptions, partial completion, provider instability, and stale ownership are **normal operating conditions**. The product is designed around them.

## 6.15 Lineage Over Mutation

Retries and recoveries create traceable lineage; they do not rewrite history to look successful.

---

# 7. Product Architecture Layers

Logical architecture (responsibilities only—not implementation).

```
Presentation Layer
        ↓
Business / Orchestration Layer
        ↓
Runtime Layer
        ↓
Provider Layer
        ↓
Infrastructure Layer
```

## 7.1 Presentation Layer

**Responsibility:** Expose human-facing operations—menus, wizards, monitors, dashboards, settings forms—so users can define campaigns, start sends, observe progress, and trigger controlled recovery.

Does **not** own execution truth.

## 7.2 Business / Orchestration Layer

**Responsibility:** Define messaging work in ERP terms: recipients, message content, products/attachments, campaign records, authorization, company scope, and linkage to Odoo business objects.

Owns **what should be sent** and **who may send**.  
Does **not** own lease algorithms or provider transport loops as long-term authority.

## 7.3 Runtime Layer

**Responsibility:** Own execution attempts: identity, lease/ownership, heartbeat/liveness, recipient processing coordination, terminalization, retry attempt semantics, reconciliation of stale runs, and projection of progress back to orchestration.

Owns **what actually ran** and **how recovery is safe**.

## 7.4 Provider Layer

**Responsibility:** Translate normalized send/media/config operations into vendor-specific APIs and normalize responses (success, ids, retryability, errors).

Owns **how a specific gateway is called**.  
Must not own campaign state machines.

## 7.5 Infrastructure Layer

**Responsibility:** Persistence, transactions, logging sinks, process/hosting environment, and deployment topology (embedded worker today; isolated workers / runtime service later).

Owns **where the runtime runs**, not business meaning.

### Authority flow

Presentation → requests orchestration → orchestration requests runtime → runtime invokes provider → infrastructure persists outcomes.  
**Runtime authority overrides optimistic presentation state.**

---

# 8. Product Capabilities Matrix

Every capability appears in **exactly one** category.

| Capability | Category |
|------------|----------|
| Messaging execution runtime | **Mandatory** |
| Campaign definition & execution | **Mandatory** |
| Execution authority records | **Mandatory** |
| Recipient-level delivery tracking / message logs | **Mandatory** |
| Explicit execution & campaign state model | **Mandatory** |
| Lease / ownership coordination | **Mandatory** |
| Heartbeat / liveness | **Mandatory** |
| Replay-safe recovery semantics | **Mandatory** |
| Idempotent outbound intent handling | **Mandatory** |
| Retry with lineage | **Mandatory** |
| Provider abstraction contract | **Mandatory** |
| At least one production provider adapter | **Mandatory** |
| Provider configuration & credential governance | **Mandatory** |
| Execution safety controls (limits, validation) | **Mandatory** |
| Campaign monitoring | **Mandatory** |
| Operational delivery summary / dashboard | **Mandatory** |
| ERP integration (partners / products / sales linkage) | **Mandatory** |
| Security groups & access control | **Mandatory** |
| Multi-company isolation for messaging data | **Mandatory** |
| Observability via status + structured logging | **Mandatory** |
| Odoo Community install/upgrade path | **Mandatory** |
| Attachment/media outbound support | **Mandatory** |
| Product-oriented message content support | **Mandatory** |
| Single-message send entry points from ERP records | **Mandatory** |
| Mock/test provider for safe verification | **Mandatory** |
| Additional production provider adapters | **Optional** |
| Optional file-based operational logging | **Optional** |
| Localization / bilingual operational UX | **Optional** |
| Sale-order creation helpers from product selection flows | **Optional** |
| Advanced analytics / BI exports | **Optional** |
| Webhook ingress for provider status events | **Future Roadmap** |
| Isolated worker / non-HTTP execution plane | **Future Roadmap** |
| Durable outbound queue separation | **Future Roadmap** |
| Standalone runtime service API (Odoo as client) | **Future Roadmap** |
| Deeper inbound status reconciliation | **Future Roadmap** |
| Multi-tenant hosted cloud runtime | **Future Roadmap** |
| CRM | **Out of Scope** |
| Helpdesk / ticketing | **Out of Scope** |
| Support inbox / contact center | **Out of Scope** |
| Chatbot builder | **Out of Scope** |
| AI agent framework | **Out of Scope** |
| Marketing automation journeys | **Out of Scope** |
| Social media management | **Out of Scope** |
| Billing/subscription platform | **Out of Scope** |
| Website builder / CMS | **Out of Scope** |
| Document management suite | **Out of Scope** |
| Distributed exactly-once guarantee product | **Out of Scope** |

---

# 9. Release Definition

These definitions are **RelayRuntime-specific**. A build does not advance by renaming alone.

## 9.1 Prototype

- Demonstrates send paths and basic campaign UI
- Execution authority, lineage, and recovery semantics may be incomplete or illustrative
- Not suitable for real customer messaging
- Purpose: validate product shape and contracts

## 9.2 Alpha

- Core runtime loop exists with campaign + recipient logs
- Provider abstraction present with at least one adapter (including mock)
- Safety controls partially enforced
- Recovery/replay rules documented but may have known hazardous gaps
- Internal testing only; explicit “do not use on production customer lists”

## 9.3 Beta

- Execution authority, lease/heartbeat, and retry lineage are real product behaviors
- Monitoring and delivery visibility usable by operators
- Failure modes catalogued; major corruption paths addressed
- Suitable for controlled pilot customers with operational supervision
- Remaining gaps are listed, accepted, and time-bounded

## 9.4 Release Candidate (RC)

- Mandatory capabilities from Section 8 are complete for the embedded runtime stage
- Upgrade path validated on staging
- Security model reviewed for credentials and campaign data
- Provider production adapter validated under realistic load bands the product claims to support
- Documentation covers operations, recovery, and honest limits
- No known data-corrupting defects in execution/replay/retry paths

## 9.5 Production Ready

RelayRuntime may be called **Production Ready** only when all are true:

1. Mandatory capability set is complete and verified
2. Replay-safe recovery and retry lineage behave as specified under failure tests
3. Execution authority is unambiguous under concurrency and stale-run scenarios
4. Operators can answer what ran / failed / is retryable without engineering intervention
5. Upgrade and multi-company behavior are verified
6. Identity surfaces (product name, module, menus, docs) are consistent
7. Known limitations are published and do not include silent corruption risks
8. Support/runbook procedures exist for common failure scenarios

## 9.6 Enterprise Ready

Production Ready **plus**:

1. Proven operational procedure for stale reconciliation and partial completion
2. Clear capacity guidance (supported campaign size/concurrency bands)
3. Provider onboarding guide for partners adding adapters without breaking contracts
4. Observability sufficient for audited environments (traceability of attempts and outcomes)
5. Architecture readiness for the next deployment stage (isolated workers or queue separation) without rewriting product semantics
6. Solution-partner packaging: boundaries, non-goals, and integration patterns are explicit

**Enterprise Ready is not “more features.”** It is operational trust at scale within the product’s honest limits.

---

# 10. Roadmap Boundaries

Do not mix these horizons in planning language.

## 10.1 Immediate Product

The product that must be complete for Production Ready at the **embedded runtime** stage:

- Replay-safe campaign execution with execution authority
- Lease/heartbeat and stale-run handling
- Recipient delivery truth and campaign monitoring
- Retry lineage
- Provider abstraction + production provider path + mock provider
- ERP send entry points (partners / sales context)
- Safety controls and settings/security
- Consistent product identity across user-facing surfaces
- Operational documentation (runbook, failure scenarios, limits)

## 10.2 Near-term Roadmap

- Additional production provider adapters under the same contract
- Webhook-based delivery/status ingress (integration, not inbox product)
- Stronger operational dashboards for multi-campaign fleets
- Isolated workers / non-blocking execution plane preserving Stage-1 semantics
- Improved localization and partner implementation kits
- Deeper attachment/media resilience and provider capability gating in UX

## 10.3 Long-term Vision

- Durable outbound queue separation (orchestration enqueues; runtime consumes)
- Standalone runtime service (API/RPC) with Odoo as orchestration client
- Multi-tenant hosted cloud execution plane
- Broader channel abstraction **only if** it preserves runtime principles (not a pivot into MA/CRM)
- Ecosystem of certified provider adapters and partner extensions

Long-term vision **extends the runtime**; it does not redefine RelayRuntime as a CRM, helpdesk, or AI platform.

---

# 11. Non-Goals

Features that should **never** become part of RelayRuntime (unless this constitution is formally revised):

| Non-goal | Why |
|----------|-----|
| Becoming a CRM | Destroys focus; duplicates Odoo CRM and partner CRMs |
| Becoming a helpdesk/inbox | Different product category; different UX and data model |
| Building chatbots or AI agents | Unbounded scope; unrelated failure modes |
| Full marketing automation suite | Journeys/segmentation are MA; runtime should execute, not orchestrate journeys |
| Social network management | Different domain and compliance model |
| Replacing Odoo mail/discuss as general messaging | Wrong layer; ERP collaboration ≠ provider messaging runtime |
| Guaranteeing provider-level exactly-once globally | Dishonest without ledger+provider support; erodes trust |
| Absorbing billing platforms | Commercial metering platforms are separate products |
| Becoming a website/CMS | Unrelated surface area |
| Competing as a contact-center suite | Violates modularity and ERP-first positioning |
| Silent scope expansion via “just one more adjacent module” | Protects maintainability and enterprise clarity |

**Scope creep test:**  
*Does this feature strengthen execution correctness, delivery truth, recovery, provider independence, or ERP-linked outbound orchestration?*  
If no → reject.

---

# 12. Product Identity

All public and technical naming must converge on one identity. Legacy aliases may exist only as migration footnotes, never as competing brands.

| Surface | Official value |
|---------|----------------|
| **Official Product Name** | RelayRuntime |
| **Technical Module Name** | `relayruntime` |
| **Menu Name** | RelayRuntime |
| **Brand Name** | RelayRuntime |
| **Repository Name** | `relayruntime` |
| **GitHub Repository** | `relayruntime` (org prefix as applicable, e.g. `ORG/relayruntime`) |
| **App Store / Apps Page Name** | RelayRuntime |
| **Documentation Name** | RelayRuntime Documentation |
| **Short technical descriptor** | Replay-safe operational messaging execution runtime for Odoo Community |

### Identity rules

1. User-visible menus, apps page, icons, docs titles, and release notes use **RelayRuntime**.
2. Technical code/module technical name remains **`relayruntime`** (lowercase, no spaces).
3. Provider names (e.g. WhatsApp, Green API) describe **channels/adapters**, not the product brand.
4. Legacy names (e.g. historical “WhatsApp Simple”) are migration history only—not current product identity.
5. No parallel brand for the same codebase (one product, one name, one module).

---

# 13. Executive Summary

## What is RelayRuntime?

RelayRuntime is a **replay-safe operational messaging execution runtime** for Odoo Community. It owns campaign execution authority, recipient delivery truth, recovery under failure, retry lineage, and provider-independent outbound messaging—delivered initially as an Odoo application with a platform runtime trajectory.

## What is it NOT?

It is **not** a CRM, helpdesk, chatbot platform, marketing automation suite, social media product, billing system, website builder, contact center, or AI agent framework.  
It is **not** a guarantee of distributed exactly-once delivery.  
It is **not** “just a WhatsApp button.”

## Who should use it?

Organizations and partners who need **trustworthy outbound messaging from Odoo**—operations, sales, and administrators who require recoverable campaigns, auditable outcomes, and provider flexibility—without building a custom reliability layer.

## Why does it exist?

Because ERP messaging integrations fail in the real world: partial runs, retries, stale ownership, provider instability, and missing delivery truth. Odoo Community alone does not provide an execution runtime for these conditions. RelayRuntime does.

## When will we officially call it Production Ready?

When the **Mandatory** capability set is complete and verified; replay/retry/lease behaviors are safe under failure tests; operators can explain outcomes without engineering rescue; upgrades and security hold; product identity is consistent; and published limitations contain no silent corruption risks—as defined in Section 9.5.

---

## Governance

- This document supersedes informal product descriptions and marketing shorthand.
- Architecture decisions, roadmap items, QA exit criteria, and documentation must cite alignment with this vision.
- Amendments require explicit product-architecture decision (versioned change to this document)—not silent feature accretion.

**End of Product Vision**
`)