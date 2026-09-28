# LANDING_PAGE_SPEC.md

**Project:** RWPST RelayRuntime  
**Document Version:** 1.0  
**Status:** Approved for Implementation  
**Owner:** RWPST  
**Purpose:** Official specification for the RelayRuntime marketing landing page.

---

# 1. Vision

The RelayRuntime landing page is the primary marketing website for the product.

Its purpose is to clearly communicate that RelayRuntime is **not another WhatsApp connector**, but a complete **Enterprise Messaging Runtime** built for Odoo Community.

The landing page should inspire confidence, demonstrate enterprise readiness, and convert visitors into users.

---

# 2. Product Positioning

## Product Name

RelayRuntime

## Tagline

Enterprise Messaging Runtime for Odoo Community

## Positioning Statement

RelayRuntime brings WhatsApp campaigns to Odoo Community: bulk sending, campaign history, a delivery dashboard, and operator retry.

Live sending uses Green API. Mock Provider is included for demos. One active provider configuration is used per company.

---

# 3. Core Marketing Messages

The landing page must repeatedly reinforce these messages.

## Message 01

Built Around a Runtime, Not Just an Integration.

---

## Message 02

Provider Setup.

Green API sends live messages.

Mock Provider simulates sends for testing.

---

## Message 03

Enterprise Operational Command Center.

Review every campaign.

Track sent, failed, and skipped.

---

## Message 04

Ready for attended Green API campaigns on Odoo 19 Community.

---

## Message 05

Enterprise Messaging Starts Here.

---

# 4. Target Audience

Primary

• Odoo Partners

• ERP Consultants

• Solution Integrators

• SMEs

• Enterprise IT Teams

Secondary

• CTOs

• Operations Managers

• Technical Decision Makers

---

# 5. Design Philosophy

Inspired by

• Stripe

• Vercel

• Supabase

• Linear

Characteristics

• Premium

• Enterprise

• Clean

• Fast

• Modern

Avoid

• Heavy gradients

• Stock photos

• Cartoon illustrations

• Excessive animations

---

# 6. Branding

Primary Color

Deep Blue

Accent

Electric Blue

Background

White

Dark Hero Section

Typography

Modern Sans Serif

Large headlines

Comfortable spacing

Rounded buttons

Soft shadows

---

# 7. Information Architecture

Hero

↓

Problem

↓

Solution

↓

Key Features

↓

Operational Command Center

↓

Provider Abstraction

↓

Screenshots

↓

Providers

↓

Deployment

↓

FAQ

↓

CTA

↓

Footer

---

# 8. Hero Section

Goal

Immediately communicate what RelayRuntime is.

Asset

Use:

assets/banner_1.jpg

Headline

Enterprise Messaging Starts Here

Subheadline

RelayRuntime brings WhatsApp campaigns to Odoo Community: bulk sending, campaign history, a delivery dashboard, and operator retry. Live sending uses Green API. Mock Provider is included for demos.

Bullet List

✓ Bulk Messaging & Campaigns

✓ Delivery Dashboard & Retry

✓ Green API live sending

CTA Primary

Watch Live Demo

CTA Secondary

Documentation

---

# 9. Problem Section

Headline

Enterprise Messaging Is More Than Sending Messages

Description

Businesses quickly outgrow basic messaging integrations.

As messaging volume increases, organizations face delivery failures, provider limitations, missing observability, and operational complexity.

RelayRuntime solves these challenges by introducing an enterprise messaging runtime.

Cards

• Single Provider Dependency

• No Retry Engine

• No Campaign Record

• No Monitoring

• No Delivery Analytics

• Manual Operations

---

# 10. Solution Section

Headline

One Runtime for WhatsApp Campaigns.

Description

RelayRuntime sits between Odoo and the active WhatsApp provider, so operators run campaigns with a delivery log and a path to retry.

The runtime handles

• Bulk sending

• Campaign execution

• Operator retry

• Monitoring

• Analytics

• Provider abstraction

---

# 11. Key Features

Grid

2 Rows

3 Columns

Cards

Provider Setup

Campaign Execution

Operator Retry

Bulk Messaging

Delivery Dashboard

---

# 12. Operational Command Center

Headline

One Dashboard.
Complete Visibility.

Description

Manage every aspect of enterprise messaging from one operational dashboard.

Asset

Use screenshot

Command Center

Features

Runtime KPIs

Campaigns

Bulk Messaging

Live Monitor

Logs

Runtime Settings

---

# 13. Provider Abstraction

Headline

Campaigns Stay in RelayRuntime

Diagram

Business Logic

↓

RelayRuntime

↓

Green API

Mock Provider

Description

One active provider per company. Additional adapters are registered and are not available for live sending in this release.

---

# 14. Product Experience

Headline

Built For Daily Operations

Screenshots

Command Center

Runtime Settings

Bulk Messaging

Delivery Dashboard

Each screenshot contains

Title

One sentence description

---

# 15. Providers

Live sending

Green API

Test mode

Mock Provider

Registered adapters — not available for live sending

Meta Cloud API

Evolution API

UltraMsg

Twilio

Gupshup

Custom

Caption

One active provider per company. Green API sends live messages. Mock Provider simulates sends for testing.

---

# 16. Deployment

Headline

Deploy In Minutes

Cards

Odoo Addon — installs as an Odoo 19 Community addon on your existing Odoo host

Odoo Community Ready

Odoo 19 Ready

Attended Campaigns — attended campaign execution, delivery totals, and operator retry for Green API

VPS Ready

---

# 17. FAQ

Questions

What is RelayRuntime?

Does it support Odoo Community?

Can I change providers later?

Does it support Meta Cloud API?

Can I use multiple providers?

How does campaign execution work?

How are failed messages retried?

What is it ready for?

Required answers

Meta Cloud API, Evolution API, UltraMsg, Twilio, Gupshup, and Custom are registered adapters and are not available for live sending.

One active provider per company. Simultaneous live multi-provider sending is not available.

Campaign execution runs in the operator's request. This release does not include a background queue.

Retry Failed Recipients sends immediately from a finished campaign. Retry does not run in the background.

Ready for attended Green API campaigns on Odoo 19 Community.

---

# 18. Final CTA

Headline

Ready To Modernize Your Messaging Infrastructure?

Buttons

Watch Live Demo

Read Documentation

---

# 19. Footer

Links

Documentation

GitHub

Odoo Apps

Release Notes

Contact

License

---

# 20. Asset Mapping

Hero

banner_1.jpg

Logo

HorizontalLogo

VerticalLogo

AppIcon

Screenshots

01_command_center

02_settings

03_bulk_wizard

06_delivery_dashboard

Marketing Assets

MASTER ASSETS

ODOO APPS STORE ASSETS

---

# 21. Animation Rules

Hero

Fade Up

Cards

Fade In

Screenshots

Scale + Fade

CTA

Hover Glow

Scrolling

Smooth

Duration

250–350ms

---

# 22. Responsive Rules

Desktop

4-column layouts

Tablet

2-column layouts

Mobile

Single column

Buttons

Full width

Images

Lazy loaded

---

# 23. SEO

Title

RelayRuntime | Enterprise Messaging Runtime for Odoo Community

Meta Description

RelayRuntime brings WhatsApp campaigns to Odoo Community: bulk sending, campaign history, a delivery dashboard, and operator retry. Live sending uses Green API. Mock Provider is included for demos.

Keywords

Odoo WhatsApp

Enterprise Messaging

WhatsApp Integration

Provider Abstraction

Campaign Execution

Operator Retry

RelayRuntime

---

# 24. Performance Requirements

Lighthouse

Performance >95

Accessibility >95

SEO >95

Best Practices >95

---

# 25. Cursor Implementation Rules

Cursor must:

• Follow section order exactly.

• Do not invent additional sections.

• Use only approved assets.

• Do not replace screenshots with mockups.

• Preserve branding colors.

• Build semantic HTML.

• Use responsive CSS.

• Keep JavaScript minimal.

---

# 26. Acceptance Criteria

The landing page is considered complete when:

✓ Responsive on Desktop, Tablet, Mobile.

✓ Lighthouse Performance >95.

✓ Uses real RelayRuntime screenshots.

✓ Communicates Enterprise Messaging Runtime positioning.

✓ Highlights Provider Abstraction.

✓ Highlights Operational Command Center.

✓ Includes all CTAs.

✓ Ready for GitHub Pages deployment.

---

END OF SPECIFICATION