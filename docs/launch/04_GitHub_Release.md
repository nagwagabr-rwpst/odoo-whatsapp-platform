# 04 — GitHub Release

**Suggested tag:** align with commercial launch tag used on GitHub Releases  
**Branch / line:** 19.0  
**Module:** `relayruntime`  
**Source of truth:** `docs/marketing/Product_Messaging_Guide.md`  

---

## Release title

RelayRuntime — Enterprise Messaging Runtime for Odoo Community (Commercial Launch)

---

## Release notes body

### What is RelayRuntime

RelayRuntime is an Enterprise Messaging Runtime for Odoo Community.

It is the operational execution layer between Odoo and messaging providers. It owns campaign execution, delivery outcomes, recovery, queue behavior, retries, and provider-independent outbound messaging.

RelayRuntime is not another WhatsApp connector, chatbot, or simple sender.

### Why it exists

Odoo Community teams need WhatsApp for sales updates, support communication, ERP notifications, and campaigns. Thin connectors can send a message — then fail under real operations: unclear delivery status, fragile retries, and workflows locked to one provider.

RelayRuntime exists to close that gap with a production-oriented messaging runtime.

### Highlights

- Bulk Messaging and Campaign Management  
- Message Queue visibility and Retry for failed or skipped recipients  
- Delivery Dashboard and Delivery Tracking  
- Multi-Provider WhatsApp adapters (Meta Cloud API, Evolution API, Green API)  
- Operator Command Center for KPIs, alerts, and workspaces  
- Built for Odoo Community  

### Commercial links

- Website: https://relayruntime.rwpst.com  
- Live Demo: https://relayruntime.rwpst.com/#demo  
- Product messaging guide: `docs/marketing/Product_Messaging_Guide.md`  
- Launch kit: `docs/launch/`  

### Notes

- Live delivery requires an external provider account.  
- Mock Provider is included for safe testing.  
- Review module limitations in the Apps description / documentation before production rollout.  

### License

LGPL-3
