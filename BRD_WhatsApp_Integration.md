# PRD — WhatsApp Simple Integration for Odoo 19 Community

## Project Overview

Build a lightweight WhatsApp integration module for Odoo 19 Community that allows users to send WhatsApp messages directly from Odoo business documents.

The first version focuses only on outgoing messages.

---

# Goals

* Send WhatsApp messages from Odoo
* Keep implementation simple
* Support manual sending only
* Provide basic message tracking
* Ensure clean modular architecture

---

# In Scope

## WhatsApp Configuration

Admin users can configure:

* API URL
* Access Token
* Instance ID
* Active/Inactive Status

---

## Supported Models

### Contacts

Allow sending WhatsApp messages from:

* res.partner

### Sales Orders

Allow sending WhatsApp messages from:

* sale.order

---

## Send WhatsApp Wizard

The system should open a popup wizard containing:

* Recipient Number
* Message Body
* Optional Attachment

Actions:

* Send
* Cancel

---

## WhatsApp API Integration

The module should:

* Send text messages
* Send media attachments
* Handle API responses
* Handle API errors

---

## Message Logs

Store:

* Recipient
* Message
* Status
* API Response
* Related Document
* User
* Sent Date

---

## Security

Create groups:

* WhatsApp User
* WhatsApp Manager

Managers can:

* Access settings
* View all logs

Users can:

* Send messages
* View their own logs

---

# Technical Requirements

* Odoo 19 Community
* Python
* REST API
* PostgreSQL

---

# Architecture

## Module Structure

whatsapp_simple/

* models/
* wizard/
* services/
* security/
* views/
* data/

---

## Service Layer

Create reusable service methods:

* send_text_message()
* send_attachment()
* prepare_payload()
* process_response()

---

## Logging

Use:

* _logger.info()
* _logger.error()

Enable debug mode support.

---

# Out of Scope (Future Phases)

The following are NOT included in this version:

* Incoming messages
* Webhooks
* Live chat
* Campaigns
* Automation
* AI replies
* Chatbot
* Multi-agent inbox
* Message templates
* Scheduling

---

# UI Requirements

Add:

* "Send WhatsApp" button on Contact form
* "Send WhatsApp" button on Sales Order form

---

# Expected Result

Users can:

1. Open a Sales Order or Contact
2. Click "Send WhatsApp"
3. Enter message
4. Send message successfully
5. Track sent message in logs
