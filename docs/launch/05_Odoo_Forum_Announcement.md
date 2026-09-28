# 05 — Odoo Forum Announcement

**Channel:** Odoo Community Forum  
**Tone:** Natural · Technical · Community · No sales hype  
**Source of truth:** `docs/marketing/Product_Messaging_Guide.md`  

---

## Suggested title

RelayRuntime — Enterprise Messaging Runtime for Odoo Community (feedback welcome)

---

## Post body

Hello,

Sharing a project we have been building for Odoo Community: **RelayRuntime**.

### Context

Many Community projects need WhatsApp for operational messages — order updates, bulk notices, campaign sends, and customer communication. Thin “send WhatsApp” modules often work for small tests, then become difficult when you need:

- clearer sent, failed, and skipped outcomes  
- a way to retry failed or skipped contacts from the campaign  
- a campaign record after the send finishes  

### What RelayRuntime is

RelayRuntime is positioned as an **Enterprise Messaging Runtime** for Odoo Community.

It sits between Odoo and messaging providers and focuses on:

- Bulk messaging and campaign history  
- Operator retry for failed and skipped recipients  
- Delivery Dashboard totals for sent, failed, and skipped  
- Live sending through Green API, plus Mock Provider for testing  

Meta Cloud API, Evolution API, UltraMsg, Twilio, Gupshup, and Custom are registered adapters and are not available for live sending in this release.

The goal is operational reliability and visibility — not a chat inbox or chatbot.

### Links

- Website / demo: https://relayruntime.rwpst.com  
- Demo section: https://relayruntime.rwpst.com/#demo  
- Repository: https://github.com/nagwagabr-rwpst/odoo-whatsapp-platform  

### Looking for discussion

Especially interested in feedback from:

- Community implementers  
- Odoo Partners delivering messaging projects  
- Operators who need campaign history and a clear sent, failed, and skipped record  

Happy to answer technical questions about scope, limitations, and roadmap priorities.

Thanks.
