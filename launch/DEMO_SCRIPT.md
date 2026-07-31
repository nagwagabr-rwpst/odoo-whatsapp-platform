# DEMO_SCRIPT.md

**Document ID:** RELEASE-013  
**Document Title:** RelayRuntime Launch Video — Official Production Script  
**Product:** RWPST RelayRuntime  
**Version:** 1.0  
**Status:** Approved — Official Launch Video Specification  
**Owner:** RWPST Release / Marketing Production  
**Audience:** Presenter, screen-capture operator, video editor, AI video generator, QA reviewer  
**Target runtime:** 90–120 seconds  
**Aspect ratio:** 16:9 (1920×1080 preferred; 1280×720 minimum)  
**Frame rate:** 30 fps  
**Audio:** Voice-over primary; UI click SFX optional and quiet  

---

## 1. Document Header

| Field | Value |
|-------|--------|
| Spec name | RelayRuntime Launch Demo Script |
| Release gate | RELEASE-013 — Launch Assets |
| Positioning | **Enterprise Messaging Runtime** (not a WhatsApp connector) |
| Platform shown | Odoo 19 Community + RelayRuntime application module |
| App menu root | **RWPST RelayRuntime** |
| Primary surfaces | Command Center → Runtime Configuration → Bulk Messaging → Live Monitor → Delivery Dashboard |
| Language | English (US), professional enterprise tone |
| Brand marks | RWPST RelayRuntime logo / AppIcon; deep blue + electric blue accents |
| Forbidden framing | “WhatsApp plugin,” “WhatsApp connector,” “chat tool,” “CRM,” “marketing automation suite” |
| Required framing | Runtime, execution authority, provider independence, observability, recovery, delivery truth |

This document is the single source of truth for producing the launch demo. If a shot conflicts with this script, the script wins unless Release revises this file.

---

## 2. Recording Rules

### 2.1 Environment

1. Use a clean Odoo backend session with RelayRuntime installed and active.
2. Sign in as a user with RelayRuntime manager access (configuration + campaigns + logs).
3. Company name in the top bar must look professional (e.g. “Acme Manufacturing” or “RWPST Demo”). Avoid “My Company,” “Test,” or developer DB names.
4. Browser: Chrome or Edge, latest stable. Zoom **100%**. Bookmarks bar hidden. Extensions that inject UI must be disabled.
5. Capture the Odoo backend only — no desktop wallpaper, OS notifications, or browser tabs chrome if a clean browser profile / kiosk-style capture is available. If browser chrome is visible, keep a single tab titled `RelayRuntime`.
6. Prefill demo data before recording (do not create data live unless the scene explicitly requires it):
   - Runtime configuration: **Configured**, provider status **Healthy**, Test Mode **off** for production look (or on only if a “safe demo” callout is approved — default is **off**).
   - At least one completed campaign with sent / failed / skipped counts.
   - One campaign in **running** state with live progress labels populated (or a paused-looking running card with non-zero counters if live send cannot be shown safely).
   - Delivery Dashboard counters non-zero: Sent, Failed, Skipped, Delivery Rate ≥ 90% preferred.
   - Message logs with readable partner names (no PII from real customers).
7. Hide or redact API tokens, secrets, and phone numbers beyond last 4 digits if any full numbers appear.
8. Prefer demo partner names: `Northwind Supplies`, `Blue Harbor Retail`, `Summit Parts Co.`

### 2.2 Capture settings

| Setting | Requirement |
|---------|-------------|
| Resolution | 1920×1080 |
| Codec | H.264 or ProRes proxy for edit; final export H.264 MP4 |
| Cursor | Visible; smooth pointer; no frantic movement |
| Scroll | Slow, deliberate; ease in/out |
| Click highlight | Optional soft ring (editor/plugin); never flashy |
| Transitions | Hard cut or 8–12 frame dissolve only |
| Music | Optional bed under −18 LUFS relative to VO; no lyrics |
| VO level | Consistent; target −14 to −16 LUFS integrated |
| Silence | No dead air longer than 0.8 s without intentional beat |

### 2.3 Performance and UX hygiene

1. Do not open the Odoo Apps menu, debug assets, or developer mode UI.
2. Do not show error toasters unless Scene 05 intentionally demonstrates recovery (default: no errors).
3. Mouse must never hover unrelated systray icons (activities, messaging, user menu) except where scripted.
4. Keyboard shortcuts are allowed only when scripted; prefer mouse for clarity.
5. If a load spinner appears > 1.5 s, cut around it or re-record with warm caches.

### 2.4 Language and on-screen copy rules

1. On-screen lower-thirds must say **Enterprise Messaging Runtime**, never **WhatsApp Connector**.
2. WhatsApp may appear only as a **channel / provider badge** or provider adapter label — never as the product category.
3. Prefer product vocabulary: runtime, queue, execution, delivery, provider adapter, Command Center, Live Monitor, replay-safe, observability.

---

## 3. Demo Objective

Demonstrate in under two minutes that RelayRuntime is a production **Enterprise Messaging Runtime** for Odoo Community: an operational execution plane with provider abstraction, campaign execution control, live monitoring, and delivery analytics — not a thin messaging connector.

Viewer takeaway (one sentence):

> RelayRuntime owns outbound messaging execution, observability, and delivery truth inside Odoo — with providers as replaceable adapters.

Primary CTA implied by the ending card: install / evaluate RelayRuntime for Odoo Community.

---

## 4. Scene Timeline (Master)

| Scene | Title | Duration | Cumulative | Screen |
|-------|--------|----------|------------|--------|
| 00 | Cold open / brand lockup | 0:00–0:08 (8s) | 0:08 | Brand slate (or landing hero still) |
| 01 | Command Center | 0:08–0:28 (20s) | 0:28 | App → Command Center |
| 02 | Provider-independent runtime config | 0:28–0:42 (14s) | 0:42 | Configuration → Runtime Configuration form |
| 03 | Launch operational bulk execution | 0:42–1:02 (20s) | 1:02 | Bulk Messaging wizard |
| 04 | Live Monitor — execution truth | 1:02–1:18 (16s) | 1:18 | Operations → Live Monitor (kanban) |
| 05 | Delivery Dashboard — outcomes | 1:18–1:38 (20s) | 1:38 | Analytics → Delivery Dashboard |
| 06 | Close / positioning lock | 1:38–1:50 (12s) | 1:50 | Brand end card |
| — | **Editable pad** | +0–10s | **≤ 2:00** | Hold end card or extend Scene 01/04 slightly |

**Nominal cut length:** ~110 seconds.  
**Hard minimum:** 90 seconds.  
**Hard maximum:** 120 seconds.

---

## 5. Scene Specs

### Scene 00 — Cold Open / Brand Lockup

**Duration:** 8 seconds (0:00–0:08)

**Screen to open:**  
Full-frame brand slate (preferred) or a frozen still of the landing hero with product name dominant. Do **not** start inside a random Odoo list view.

**Exact UI actions:**  
None (static or subtle logo fade). If using the live app, freeze on Command Center with logo visible but do not move the mouse yet.

**Camera movement:**  
Static. Optional 2% slow push-in on the logo (Ken Burns), ending before Scene 01 cut.

**Mouse movement:**  
Hidden or off-screen.

**On-screen text:**

| Time | Placement | Copy |
|------|-----------|------|
| 0:00–0:08 | Center / lower third | `RWPST RelayRuntime` |
| 0:02–0:08 | Under title | `Enterprise Messaging Runtime for Odoo Community` |

**Voice-over:**

> RelayRuntime. The enterprise messaging runtime for Odoo Community.

**Transition notes:**  
Hard cut or 10-frame dissolve into Scene 01 as the Odoo app shell appears.

---

### Scene 01 — Command Center

**Duration:** 20 seconds (0:08–0:28)

**Screen to open:**  
Odoo main backend → left app switcher / home menu → open **RWPST RelayRuntime** → land on **Command Center** (`whatsapp.app.dashboard` form).

**Pre-roll state (before camera rolls on this scene):**  
Command Center already loaded. Alerts strip shows healthy state preferred: “All runtime checks passed — no active alerts.” KPI row populated. Workspace tiles visible without scrolling if possible.

**Exact UI actions:**

1. Hold still 1.0 s on app header: logo, title **RWPST RelayRuntime**, subtitle **Operational Messaging Runtime for Odoo**, channel badge, Configured / Healthy badges.
2. Slowly pan/scroll the viewport downward just enough to reveal **Runtime KPIs** (Provider, Active Campaigns, Delivery Rate, Queue).
3. Pause 1.5 s on KPI row.
4. Continue slight scroll to reveal **Workspaces** tile grid.
5. Move mouse deliberately across tiles left-to-right: Command Center → Campaigns → Bulk Messaging → (optional) Live Monitor — **do not click** yet.
6. Hover **Live Monitor** tile briefly (show “live” KPI if running count > 0), then return mouse to neutral center-left.

**Camera movement:**  
Medium shot of full browser content area. Soft vertical follow-scroll with the content (no handheld shake). Keep app header in frame for the first 6 seconds.

**Mouse movement:**  
Enter from lower-right at action step 5; smooth arc; hover dwell 0.4–0.6 s per tile; no clicks.

**On-screen text:**

| Time | Placement | Copy |
|------|-----------|------|
| 0:08–0:16 | Lower third | `Operational Command Center` |
| 0:16–0:28 | Lower third | `Observe every queue. Track every delivery.` |

**Voice-over:**

> This is the Command Center — the operational hub for runtime health, alerts, and messaging workspaces. Not a chat inbox. An execution control surface.

**Transition notes:**  
Cut on mouse leaving the tile row. Next scene opens Runtime Configuration already focused (or click **Runtime & Settings** tile if a continuous take is preferred; if clicking, allocate 1 s of the Scene 01 budget to the click + load).

**Preferred navigation for continuous take:**  
Click workspace tile **Runtime & Settings** at 0:26; cut to Scene 02 as the configuration form settles.

---

### Scene 02 — Provider-Independent Runtime Configuration

**Duration:** 14 seconds (0:28–0:42)

**Screen to open:**  
**Configuration → Runtime Configuration** — open an existing config form (`whatsapp.config` form). Header buttons **Test Connection** / **Provider Self-Test** visible. Provider statusbar shows **healthy**.

**Exact UI actions:**

1. Frame the **Provider** group: `provider_type` radio options visible (show that a provider is selected; do not dwell on secrets).
2. Mouse moves to Provider radio group — hover only; do **not** change provider mid-take unless pre-approved alternate take.
3. Pan attention to **Health** group: last successful connection, latency, status.
4. Optional: click **Test Connection** once; wait for success notification; if notification is noisy, omit click and only show healthy statusbar.
5. Do not open Credentials page long enough to reveal tokens. If notebook opens on Credentials, immediately switch to a non-secret page or cut.

**Camera movement:**  
Slight push toward Provider + Health groups. Keep form title and statusbar visible.

**Mouse movement:**  
Top-left of sheet → Provider group → Health metrics → (optional) Test Connection button → rest.

**On-screen text:**

| Time | Placement | Copy |
|------|-----------|------|
| 0:28–0:42 | Lower third | `Provider adapters. Replace providers — not workflows.` |

**Voice-over:**

> Providers are adapters. Swap the gateway without rewriting your operational workflows. The runtime stays in charge of execution.

**Transition notes:**  
Hard cut to Bulk Messaging wizard pre-opened on **Recipients** tab (fastest). Alternate continuous path: Apps menu already on RelayRuntime → **Operations → Bulk Messaging**.

---

### Scene 03 — Launch Operational Bulk Execution

**Duration:** 20 seconds (0:42–1:02)

**Screen to open:**  
**Operations → Bulk Messaging** — wizard form **Send WhatsApp (Bulk)** with tabs: Recipients, Message, Products, Attachments.

**Prep:**  
Recipients already selected (8–25 demo partners). Message tab contains a short operational message (order update / catalog notice — not spammy promo copy). Products optional but strong if one product line is previewable.

**Exact UI actions:**

1. Start on **Recipients** tab; show recipient count / list briefly (2 s).
2. Click **Message** tab; pause so message body is readable (3 s).
3. Optional: click **Products** tab; show Product Preview (2 s).
4. Click **Attachments** only if an attachment is prepared; otherwise skip.
5. Move mouse to primary footer button **Send**.
6. Click **Send**.
7. Show **Live Progress** group appearing (`processing_state == running`) with progress fields updating **or** cut within 2 s to a prepared running campaign if live send is unsafe in the recording environment.
8. Do not wait for full campaign completion in this scene.

**Camera movement:**  
Static framed on wizard dialog/form. Tight enough to read tab labels and Send button.

**Mouse movement:**  
Tab clicks are crisp (no double-clicks). Approach **Send** with a 0.5 s hover, then single click.

**On-screen text:**

| Time | Placement | Copy |
|------|-----------|------|
| 0:42–0:52 | Lower third | `Replay-safe campaign execution` |
| 0:52–1:02 | Lower third | `Runtime-owned outbound sending` |

**Voice-over:**

> Launch bulk operational messaging from Odoo. RelayRuntime owns the execution — recipient-level progress, safe handling under failure, and a clear path to recovery.

**Transition notes:**  
As Live Progress appears, dissolve (10 frames) into Live Monitor kanban. If Send is not clicked live, still speak the VO as if execution is runtime-owned; show Monitor with a running card.

---

### Scene 04 — Live Monitor — Execution Truth

**Duration:** 16 seconds (1:02–1:18)

**Screen to open:**  
**Operations → Live Monitor** — kanban view (`whatsapp_campaign_monitor_kanban`). At least one card in **running** (preferred) plus one **completed** or **completed_with_errors** for contrast.

**Exact UI actions:**

1. Hold wide on kanban board 1.5 s.
2. Move mouse to a **running** campaign card.
3. Hover so progress / current recipient / sent-failed-skipped labels are visible.
4. Do not open the form unless needed; prefer staying on kanban for “live ops” feel.
5. Optional: toggle search filter **Running** on, then off — only if it helps clarity and fits timing.
6. Brief hover on a completed card counters (sent / failed / skipped).

**Camera movement:**  
Slow push-in on the running card during hover (max 5% scale). Keep surrounding cards partially visible to sell “operations floor,” not a single-record form.

**Mouse movement:**  
Enter from left; settle on running card; micro-move within card bounds to guide the eye to counters; exit toward top menu for next scene.

**On-screen text:**

| Time | Placement | Copy |
|------|-----------|------|
| 1:02–1:18 | Lower third | `Live execution monitoring` |

**Voice-over:**

> Live Monitor shows execution truth as campaigns run — state, progress, and delivery counters operators can trust.

**Transition notes:**  
Click top-level **Analytics → Delivery Dashboard** at 1:16, or hard cut to Delivery Dashboard already open.

---

### Scene 05 — Delivery Dashboard — Outcomes

**Duration:** 20 seconds (1:18–1:38)

**Screen to open:**  
**Analytics → Delivery Dashboard** form with **Counters** and **Performance** groups populated.

**Exact UI actions:**

1. Hold on dashboard title and counter groups 3 s (Sent / Failed / Skipped / rates as available).
2. Mouse hover across counter fields left-to-right.
3. Click **Sent Logs** (primary) — wait for message log list to open.
4. Scroll the log list slowly (1.5–2 s) to show per-recipient outcomes.
5. Optional: return via breadcrumb/back and click **Failed Logs** once for contrast (only if time remains; skip if under 4 s left in scene budget).
6. End parked on a log list or back on the dashboard counters — clean, no modal left open.

**Camera movement:**  
Static on dashboard; after opening logs, slight downward scroll follow.

**Mouse movement:**  
Predictable left-to-right on counters; deliberate click on **Sent Logs**; steady scroll wheel or scrollbar drag.

**On-screen text:**

| Time | Placement | Copy |
|------|-----------|------|
| 1:18–1:28 | Lower third | `Delivery analytics & message truth` |
| 1:28–1:38 | Lower third | `Production-ready observability` |

**Voice-over:**

> Delivery Dashboard and message logs close the loop — sent, failed, skipped — so operations can measure outcomes, not guess them.

**Transition notes:**  
Fade to black (12–15 frames) into Scene 06 end card. No abrupt audio cut; VO should finish before full black.

---

### Scene 06 — Close / Positioning Lock

**Duration:** 12 seconds (1:38–1:50) + optional hold to 2:00

**Screen to open:**  
End card: deep blue background, RelayRuntime horizontal or app logo, tagline, optional URL / Apps Store reference.

**Exact UI actions:**  
None.

**Camera movement:**  
Static. Optional logo fade-in 0–8 frames.

**Mouse movement:**  
Hidden.

**On-screen text:**

| Time | Placement | Copy |
|------|-----------|------|
| 1:38–end | Center stack | `RWPST RelayRuntime` |
| | | `Enterprise Messaging Runtime` |
| | | `for Odoo Community` |
| Optional | Footer | `Built around a runtime — not just an integration.` |

**Voice-over:**

> RelayRuntime. Enterprise messaging starts here.

**Transition notes:**  
Hold end card in silence 0.5–1.0 s after VO. Optional music swell then taper. Do not fade VO under music.

---

## 6. Full Voice-Over Script (Contiguous)

Read in one pass for ADR / VO talent. Timing marks are approximate; prefer natural pacing within scene windows.

```text
[0:00]  RelayRuntime. The enterprise messaging runtime for Odoo Community.

[0:08]  This is the Command Center — the operational hub for runtime health,
        alerts, and messaging workspaces. Not a chat inbox. An execution
        control surface.

[0:28]  Providers are adapters. Swap the gateway without rewriting your
        operational workflows. The runtime stays in charge of execution.

[0:42]  Launch bulk operational messaging from Odoo. RelayRuntime owns the
        execution — recipient-level progress, safe handling under failure,
        and a clear path to recovery.

[1:02]  Live Monitor shows execution truth as campaigns run — state,
        progress, and delivery counters operators can trust.

[1:18]  Delivery Dashboard and message logs close the loop — sent, failed,
        skipped — so operations can measure outcomes, not guess them.

[1:38]  RelayRuntime. Enterprise messaging starts here.
```

**VO style notes:**  
Calm, confident, mid-tempo. No hype adjectives (“amazing,” “revolutionary”). Emphasize *runtime*, *execution*, *providers as adapters*, *truth*.

**Word count:** ~145 words → ~55–65 seconds of speech; remaining time is visual breathing room and end card.

---

## 7. On-Screen Text Board (Editor Checklist)

| # | Timecode | Copy | Max lines |
|---|----------|------|-----------|
| T0 | 0:00 | RWPST RelayRuntime / Enterprise Messaging Runtime for Odoo Community | 2 |
| T1 | 0:08 | Operational Command Center | 1 |
| T2 | 0:16 | Observe every queue. Track every delivery. | 2 |
| T3 | 0:28 | Provider adapters. Replace providers — not workflows. | 2 |
| T4 | 0:42 | Replay-safe campaign execution | 1 |
| T5 | 0:52 | Runtime-owned outbound sending | 1 |
| T6 | 1:02 | Live execution monitoring | 1 |
| T7 | 1:18 | Delivery analytics & message truth | 1 |
| T8 | 1:28 | Production-ready observability | 1 |
| T9 | 1:38 | Enterprise Messaging Runtime for Odoo Community | 2 |

Typography: modern sans, high contrast, safe margins 5% from edges. No emoji. No WhatsApp-green full-screen washes.

---

## 8. Transition Notes (Global)

1. **Scene 00 → 01:** Dissolve 8–10 frames or hard cut on first frame of Command Center.
2. **Scene 01 → 02:** Hard cut preferred; continuous click through **Runtime & Settings** allowed.
3. **Scene 02 → 03:** Hard cut to prepared wizard (avoid long menu hunting on camera).
4. **Scene 03 → 04:** Short dissolve as execution motif; match cut on progress UI → kanban running card.
5. **Scene 04 → 05:** Hard cut or menu navigation if continuous.
6. **Scene 05 → 06:** Fade through black; do not smash cut on a busy list scroll.
7. Never use wipe, light-leak, or glitch transitions.
8. Keep audio beds continuous across hard cuts; duck −2 dB under denser VO phrases if needed.

---

## 9. Recording Checklist

### Before record

- [ ] RelayRuntime app opens to Command Center without errors
- [ ] Subtitle reads **Operational Messaging Runtime for Odoo** (or current approved UI string)
- [ ] Provider status **healthy**; config **configured**
- [ ] No Test Mode ribbon unless approved for this take
- [ ] Secrets redacted; no real customer PII
- [ ] Demo partners and campaigns seeded
- [ ] One running campaign available for Live Monitor
- [ ] Delivery Dashboard counters non-zero
- [ ] Browser zoom 100%; notifications disabled
- [ ] Mic level check; room tone 5 s captured
- [ ] Screen recorder set to 1080p30; disk space verified
- [ ] Script printed or second-monitor cue sheet ready

### During record

- [ ] Slate clap or verbal marker: “RelayRuntime DEMO take __”
- [ ] Record 2–3 clean takes of Scenes 01–05 minimum
- [ ] One safety take with Bulk **Send** omitted (cut to pre-running campaign)
- [ ] Cursor never rests on unrelated Odoo systray icons
- [ ] No accidental Esc that closes wizards mid-sentence

### After record

- [ ] Verify audio not clipped
- [ ] Spot-check that no secret fields were exposed
- [ ] Export proxy for editor + archive master
- [ ] Log take numbers against scene IDs in the edit notes

---

## 10. Deliverables

| Deliverable | Spec |
|-------------|------|
| Master video | MP4 H.264, 1920×1080, 30 fps, 90–120 s |
| Social cut (optional) | Same narrative, 60 s trim using Scenes 00, 01, 04, 06 |
| Vertical crop (optional) | 9:16 center-weighted; recreate lower-thirds for safe area |
| VO stem | WAV 48 kHz mono/stereo, dry |
| Music bed (if used) | Licensed; WAV + documentation of license |
| Lower-thirds pack | PNG/SVG or Motion titles matching Section 7 |
| Thumbnail | 1280×720 still: Command Center or end card with legible product name |
| Edit project | Premiere / DaVinci / CapCut project or AI generator project file + this script referenced |
| Shot log | Take list mapped to scene IDs 00–06 |

Store finished assets under `launch/` (or release artifact storage linked from this folder) as:

```text
launch/
  DEMO_SCRIPT.md          ← this specification
  exports/                ← optional output folder for masters
  thumbnails/             ← optional
```

---

## 11. Success Criteria

The launch video **passes** RELEASE-013 only if all of the following are true:

1. **Duration** is between **90 and 120 seconds** inclusive.
2. The product is framed as an **Enterprise Messaging Runtime**, not a WhatsApp connector, in VO and on-screen text.
3. **Command Center**, **Runtime Configuration (provider adapter)**, **Bulk execution**, **Live Monitor**, and **Delivery Dashboard / logs** each appear on screen for a readable beat (≥ 3 s of identifiable UI).
4. A non-expert viewer can answer: *What is RelayRuntime?* → “A messaging runtime for Odoo that runs and observes outbound campaigns with provider independence.”
5. No secrets, raw API tokens, or real customer PII are visible.
6. UI actions in the final cut match this script’s intent (minor path differences allowed; positioning differences are not).
7. Audio is intelligible on laptop speakers; lower-thirds remain readable on a 13" display.
8. End card states **Enterprise Messaging Runtime** (or the approved tagline) without category confusion.

**Fail conditions (automatic):**  
Calling the product a connector/plugin in VO or titles; demo is only a single WhatsApp chat send with no runtime surfaces; runtime under 90 s or over 120 s without Release waiver; credentials visible on screen.

---

## 12. Alternate Takes (Approved)

| Take ID | When to use | Difference |
|---------|-------------|------------|
| A — Primary | Default launch | Live or simulated Send → Live Monitor |
| B — Safety | Cannot send live | Skip Send click; cut from filled wizard to running Monitor card |
| C — Config emphasis | Partner/technical audience | Extend Scene 02 to 18 s; shorten Scene 03 to 16 s (keep total ≤ 120 s) |

Do not invent additional scenes without updating this document.

---

## 13. Credits & Ownership

| Role | Responsibility |
|------|----------------|
| Release Owner | Approves positioning and final cut against this spec |
| Presenter / Operator | Executes UI actions per scene |
| Editor / AI Generator | Assembles picture, titles, VO sync strictly from this script |
| QA | Runs Section 9 checklist + Section 11 success criteria |

**Document control:** Any change to timing, VO, or positioning requires a version bump of this file and a new Release acknowledgment.

---

*End of official production script — RELEASE-013.*
