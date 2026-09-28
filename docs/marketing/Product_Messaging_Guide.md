# RelayRuntime — Official Product Messaging Guide

**Status:** Authoritative commercial source of truth  
**Audience:** Marketing, Sales, Partners, Documentation, Product, Support, Content creators  
**Applies to:** Odoo Apps · Website · LinkedIn · YouTube · Documentation · Blog · GitHub · Presentations · Demo · Sales material  
**Positioning:** Enterprise Messaging Runtime for Odoo Community  

This guide is the single source of truth for RelayRuntime commercial messaging.  
Every public asset must follow it. If an asset conflicts with this guide, revise the asset.

---

## 1. Product position

### What RelayRuntime is

**RelayRuntime is an Enterprise Messaging Runtime for Odoo Community.**

It is the operational layer between Odoo and the active WhatsApp provider. It owns campaign execution, delivery logs, operator retry, and provider setup. Live sending uses Green API. Mock Provider covers demos and tests.

### What RelayRuntime is not

Do **not** position RelayRuntime as:

- another WhatsApp connector
- another messaging module
- another chatbot
- a chat inbox
- a CRM
- a marketing automation suite
- a thin “send WhatsApp” plugin

### Category statement

| Preferred category | Forbidden category |
|--------------------|--------------------|
| Enterprise Messaging Runtime | WhatsApp connector |
| Enterprise Messaging Platform | Simple WhatsApp module |
| Operational messaging runtime | Basic sender / chatbot |

---

## 2. Core message

**Official product message (≤ 25 words):**

> RelayRuntime brings WhatsApp campaigns to Odoo Community: bulk sending, a delivery dashboard, operator retry, and Green API live sending.

**Word count:** 22

---

## 3. One-line pitch

**Official one-liner (≤ 20 words):**

> Enterprise Messaging Runtime for Odoo Community—campaigns, a delivery dashboard, and Green API live sending.

**Word count:** 14

---

## 4. 30-second pitch

**Audience:** Business owner · Odoo Partner · ERP Consultant

> Most WhatsApp tools for Odoo only send messages. Teams then lose the campaign record and cannot recover failed contacts cleanly. RelayRuntime is an Enterprise Messaging Runtime for Odoo Community. It runs bulk sending and campaign history with operator retry and a Delivery Dashboard. Live sending uses Green API. Mock Provider is included for demos. You keep Odoo as the system of record.

---

## 5. 2-minute product pitch

### Problem

Businesses using Odoo Community need WhatsApp for sales updates, support messages, operational notifications, and campaigns. Basic integrations send a message—and stop there. As volume rises, failures appear: incomplete campaigns, unclear delivery status, fragile retries, and workflows locked to one provider API.

### Traditional approach

A traditional connector wires Odoo forms to a send button. It may work for a few sends. It does not keep campaign history, a delivery log, operator retry, or a Delivery Dashboard.

### RelayRuntime approach

RelayRuntime introduces an Enterprise Messaging Runtime between Odoo and the active provider. Campaigns, operator retry, and delivery monitoring stay in the runtime. Teams run bulk sending from the Command Center. Live sending uses Green API. Mock Provider simulates sends for testing.

### Business value

- A delivery log for sent, failed, and skipped contacts
- Operator retry after a finished campaign
- One active provider per company, with Green API for live sending and Mock Provider for tests
- Clear operational visibility for sales, support, and operations
- WhatsApp campaigns on Odoo Community

---

## 6. Taglines (10)

1. Runtime-grade WhatsApp for Odoo Community  
2. Execution you can trust. Delivery you can prove.  
3. From send button to messaging operations  
4. Green API live sending. One operational runtime.  
5. Campaigns with control. Deliveries with truth.  
6. Built for operators, not inbox chat  
7. WhatsApp campaigns with a delivery log  
8. The messaging layer Odoo Community was missing  
9. Campaigns. Retry. Dashboard. Command Center.  
10. Enterprise messaging. Community foundation.

---

## 7. Value proposition

**Official value proposition (outcomes, not features):**

RelayRuntime helps Odoo Community organizations run attended WhatsApp campaigns—so teams can send in bulk, review sent, failed, and skipped results, and retry failed contacts from the campaign. Live sending uses Green API.

---

## 8. Differentiators

Explain difference with concepts—not competitor attacks.

### Runtime

RelayRuntime owns execution. It is not a UI wrapper over a vendor API. It decides how campaigns run, how progress is recorded, and how recovery proceeds after interruption.

### Provider abstraction

The active provider is an adapter. Green API sends live messages. Mock Provider simulates sends. Meta Cloud API, Evolution API, UltraMsg, Twilio, Gupshup, and Custom are registered and are not available for live sending in this release. One active configuration is used per company.

### Operational reliability

Campaign execution, operator retry, and the Delivery Dashboard reduce silent failure and ambiguous status. Operators see sent, failed, and skipped results from the provider HTTP response.

### Scalability of operations

Bulk messaging and campaign history are first-class workflows for attended Green API campaigns on Odoo 19 Community.

### Enterprise workflow

Command Center, Delivery Dashboard, Provider Management, and campaign lineage support daily operator work—aligned with ERP context in Odoo Community.

---

## 9. Buyer personas — messaging

### Odoo Partner

**Lead with:** Implementation leverage and differentiation.  
**Say:** “Deliver enterprise messaging capability on Community without building a custom reliability layer per customer.”  
**Avoid:** Hobbyist or ‘plugin’ language.

### Business Owner

**Lead with:** Risk reduction and control.  
**Say:** “Know what was sent, failed, or skipped, and retry failed contacts from the campaign.”  
**Avoid:** Feature dumps and jargon without outcomes.

### Operations Manager

**Lead with:** Visibility and recovery.  
**Say:** “Campaign history, Delivery Dashboard totals, operator retry, and message logs in one operator surface.”  
**Avoid:** Marketing fluff.

### Marketing Team

**Lead with:** Controlled campaigns, not spam tools.  
**Say:** “Run bulk campaigns with attachments, product catalogs, and sent, failed, and skipped totals.”  
**Avoid:** Promising CRM or full marketing automation.

### Customer Support

**Lead with:** Clear customer communication.  
**Say:** “Send operational updates and review sent, failed, and skipped results. The dashboard does not show WhatsApp delivered or read receipts.”  
**Avoid:** Positioning as a live chat / chatbot product.

---

## 10. Messaging pyramid

```text
TOP     Mission
         │  Bring enterprise messaging reliability to Odoo Community.
         ▼
        Value
         │  Operational confidence: measurable, recoverable, provider-independent messaging.
         ▼
        Capabilities
         │  Runtime execution · Provider abstraction · Campaign operations · Delivery visibility
         ▼
BOTTOM  Features
           Bulk Messaging · Campaign History · Operator Retry · Delivery Dashboard
           Green API · Mock Provider · Command Center · Message Logs
```

**Rule:** Always sell from the top down. Features support value; they do not replace it.

---

## 11. Official vocabulary

Always prefer these terms:

| Use | Meaning |
|-----|---------|
| Enterprise Messaging Runtime | Product category |
| Enterprise Messaging Platform | Acceptable commercial category synonym |
| Bulk Messaging | High-volume / multi-recipient outbound |
| Campaign Management | Create, run, monitor, recover campaigns |
| Provider Management | Configure and observe adapters |
| Delivery Dashboard | Operational delivery outcomes view |
| Delivery Tracking | Sent / failed / skipped visibility |
| Reliable Messaging | Outcome-focused reliability language |
| Operational Visibility | Operator truth and monitoring |
| Green API | Live sending |
| Mock Provider | Simulated sends for demos and tests |
| Registered adapter | Listed provider that cannot send in this release |
| Campaign Execution | Recipient-by-recipient send inside the operator's request, with a delivery log |
| Operator Retry | Retry Failed Recipients on a finished campaign; sends immediately |
| Odoo Community / Community Edition | Target platform |
| Delivery Dashboard | Sent, failed, and skipped totals from the provider HTTP response |
| Command Center | Operator hub |
| WhatsApp Integration | Acceptable SEO/commercial phrase when tied to runtime |

---

## 12. Words to avoid

| Avoid | Why |
|-------|-----|
| Simple WhatsApp module | Weak, commodity positioning |
| Just another connector | Contradicts category |
| Basic sender | Undervalues runtime |
| Cheap / cheapest | Damages enterprise trust |
| Easy WhatsApp | Vague and non-enterprise |
| Clone | Implies derivative / low quality |
| Chatbot / chat tool | Wrong product category |
| WhatsApp plugin | Trivializes architecture |
| Marketing automation suite | Overclaim / wrong category |
| CRM | Overclaim / wrong category |
| Guaranteed delivery / exactly-once | Technically inaccurate |
| Production Ready / production volume / Queue Engine | Overstates attended Green API campaigns |
| Scheduled Messages / Message Templates | Not in this release |
| Docker Ready | No Docker package is shipped |
| Live Meta Cloud API, Evolution API, UltraMsg, Twilio, Gupshup, or Custom | Registered adapters; not sendable in this release |

---

## 13. Elevator pitches

### 15 seconds

> RelayRuntime is the Enterprise Messaging Runtime for Odoo Community—WhatsApp campaigns, a delivery dashboard, and Green API live sending.

### 30 seconds

> If your Odoo WhatsApp tool only sends messages, you lose the campaign record. RelayRuntime is an Enterprise Messaging Runtime: bulk sending, campaign history, operator retry, and a Delivery Dashboard—with Green API live sending for Odoo Community.

### 60 seconds

> Growing companies on Odoo Community need WhatsApp for sales, support, and operations. Traditional connectors send messages but leave no campaign history when contacts fail. RelayRuntime is an Enterprise Messaging Runtime. It sits between Odoo and the active provider, runs attended campaigns, and gives operators a Delivery Dashboard plus retry from the finished campaign. Live sending uses Green API. Mock Provider covers demos.

---

## 14. Mission

Bring attended WhatsApp campaigns to Odoo Community—so outbound sends are measurable, recoverable from the campaign, and sent through Green API.

---

## 15. Vision

RelayRuntime becomes the standard Enterprise Messaging Runtime for Odoo Community: the trusted execution layer that powers operational WhatsApp messaging across partners, industries, and providers—while Odoo remains the system of business record.

---

## 16. Consistency rule

Before publishing any asset, confirm:

1. Category = **Enterprise Messaging Runtime** (not connector/chatbot)  
2. Platform = **Odoo Community**  
3. Value before features  
4. Official vocabulary used; forbidden words removed  
5. Claims stay within product truth: Green API live sending, Mock Provider for tests, attended campaign execution, operator retry, and sent/failed/skipped totals. No background queue, scheduled messages, message templates, webhooks, Docker package, or live sending from registered adapters.

---

## Related documents

- `Brand_Voice_Guide.md` — tone, style, writing rules  
- `Messaging_Examples.md` — headlines, LinkedIn, YouTube, ready-to-use copy  
- `LANDING_PAGE_SPEC.md` — website structure specification  
- `../product/PRODUCT_VISION.md` — product constitution (engineering authority)
