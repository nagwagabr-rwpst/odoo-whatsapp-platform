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

It is the operational layer between Odoo and the active WhatsApp provider. It owns campaign execution, delivery logs, and operator retry. Live sending uses Green API. Mock Provider covers demos and tests.

RelayRuntime is not another WhatsApp connector, chatbot, or simple sender.

### Why it exists

Odoo Community teams need WhatsApp for sales updates, support communication, and campaigns. Thin connectors can send a message and then leave no campaign record when contacts fail.

RelayRuntime exists to close that gap for attended Green API campaigns.

### Highlights

- Bulk messaging, attachments, and product catalogs  
- Campaign history and operator retry for failed or skipped recipients  
- Delivery Dashboard totals for sent, failed, and skipped  
- Live sending through Green API, with Mock Provider for demos  
- Operator Command Center for KPIs, alerts, and workspaces  
- Built for Odoo 19 Community  

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
