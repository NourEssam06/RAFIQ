---
title: RAFIQ Application Experience
status: final
updated: 2026-11-21
sources:
  - PRD.md
  - TRD.md
  - DESIGN.md
---

# RAFIQ Application Experience

## Foundation

This is RAFIQ’s application-flow specification. The approved [PRD](PRD.md) governs scope, operating limits, and release gates. The [TRD](TRD.md) governs technical behavior and calculations. This document governs navigation, interaction, and state presentation. The existing [DESIGN.md](DESIGN.md) owns visual direction. The written contracts take precedence over mockups and reference captures.

RAFIQ is an English-language desktop browser application for adult drivers using controlled stationary sessions or an approved supervised vehicle test. The qualification baseline is Chrome on Windows 11 with a built-in camera. There are three browser surfaces: public account access, the private driver application, and separate invitation-only administration. A supervisor uses only delegated controls on the driver's device. Emergency contacts receive messages in their inbox or WhatsApp. Compatible agents connect through MCP. Clerk supplies identity screens and verified account-linking behavior. Navigation names, screen grouping, and example copy below are UX decisions derived from the approved requirements.

Use the existing `{colors.canvas}`, `{colors.ink}`, `{typography.body}`, and `{spacing.md}` as shared references. Use `{components.top-nav}`, `{components.nav-pill}`, and `{components.input}` where their visual roles apply. DESIGN.md describes a GSAP marketing reference and leaves RAFIQ-specific warning, chart, focus, and dense workspace treatments open. Keep state meanings independent of accent colors and enforce the accessibility requirements below when those treatments are specified.

## Information Architecture

The driver navigation follows the order **Dashboard · Sessions · Clips · Analysis · Reports · Settings**, with **Start session** as a distinct action. Analysis opens **What-If** and links to **Experiment Studio** and **Benchmark**. Account actions live in Settings. Open temporary chat from **Settings → Connections** when a provider is connected, consented, and eligible. During a session, the session workspace takes priority over normal navigation.

| Surface | Entry and exit | What the surface delivers |
|---|---|---|
| Public entry and account access | Public entry → Create account or Sign in. Email verification and recovery return to sign-in or the verified destination. | Adult eligibility, email/password registration, verification and recovery. Show Google and Apple only where independently qualified. Link an existing identity through verified account linking, including a different Apple relay address. |
| Controlled-use onboarding | First verified sign-in → review and accept conditions → intended eligible destination or Dashboard. | Explain stationary setup and the supervised-use boundary. Before opening private content, complete verification and check current account access. |
| Dashboard | Signed-in default → latest completed Session Detail with ready analytics. **Personal Overview** is one click away. | Explain a newer syncing session without replacing ready results. Offer a link when the newer session becomes ready. Show pending or unavailable reasons if there is no ready result. Offer Start session for first use. |
| Start session and readiness | Start session → readiness → Monitoring. Cancel returns to origin. | Session conditions, built-in camera preview, usable view, local asset readiness, account/network eligibility, recording choice, and supervised session options when eligible. |
| Monitoring and end status | Start or manual resume → Monitoring. End → session status or ready Session Detail. | Observation state, warning and interruption controls, recording and sync status, and Emergency Mode where eligible. Keep ended session status reachable from Sessions. |
| Sessions and Session Detail | Dashboard, Sessions history, authorized link or ended session → select session. | History status, detail KPIs, zoomable timeline, incidents, original detection evidence, warnings and emergency outcomes, available clip links, and session deletion. |
| Personal Overview | Dashboard or Session Detail → Personal Overview → select sessions or incident evidence. | Period and behavior filters, trends, comparison of two to four sessions, behavior ranking and overlap, elapsed-monitoring bands and findings. |
| Clips and clip replay | Clips search/filter, or Session Detail incident → replay → Back to incident or filtered results. | Owner-only video, event context, available/pending/unavailable status, expiry, and clip deletion. |
| What-If | Analysis or eligible Session Detail → select source → configure → compare → reopen saved result. | Owner-only threshold simulation over eligible measurement series with versioned baseline comparison. |
| Experiment Studio | Analysis → Experiment Studio → dataset, conditions and method → run, review, reopen, or export an eligible aggregate. | Approved versioned synthetic fixtures or predefined studies, descriptive and eligible exploratory inference, and disclosure-checked results. |
| Benchmark | Analysis → Benchmark, or benchmark reference from a report → approved results. | Aggregate held-out detection evidence, definitions, coverage, limitations and versions. |
| Reports | Reports → open report/status → review validated snapshot → PDF or Word. | Agent-authored session or trend reports, evidence, limitations, eligibility and export feedback. MCP help explains how to request a report or new version. |
| Settings | Settings → Profile, Monitoring, Emergency contacts, Privacy or Connections. | Profile and history link, supported camera, optional warning audio and visual presentation, clip preferences, contact order, fixed alert preview, sharing consent, retention and deletion. Connections has MCP and optional chat provider controls. |
| Restricted account | Sign-in or authorization change → account status. | Published RAFIQ support contact, hosted access restriction, and fresh sign-in entry after reinstatement. |
| Admin entry | Separate internal entry or bound invite → verified identity → TOTP enrollment/challenge → permitted view. | Invite acceptance, authenticator setup and recovery, or denied/expired access. Public account creation grants driver access. |
| Service Health and Release Readiness | Default admin view with metrics permission. Release Readiness inside Service Health. | Operational aggregates, freshness, channel delivery counts, and read-only gate evidence. |
| Adoption | Admin navigation → Adoption with metrics permission. | Privacy-checked funnel, usage cards, trends and range controls. |
| Account Support | Admin navigation → Account Support with support permission. | Exact account lookup and allowed verification, recovery, suspension and reinstatement actions. |
| Staff Access and Audit | Owner navigation → Staff Access or Audit. | Invitations, permissions, Owner changes, MFA recovery, and read-only audit history. |

If Staff cannot open Service Health, land on the first permitted admin view. With zero permitted views, explain access and provide sign-out. A protected direct link may resume following sign-in only after current authorization succeeds. Missing and inaccessible private links share a neutral unavailable response with a link back to the relevant authorized list. Browser Back restores the originating filters, range and selected row during normal review. Explicit **End session** controls the normal exit from live monitoring. For in-app navigation that would leave live monitoring, offer **Stay in session** and **End session** while stationary. Tab close, reload or crash follows interruption recovery.

## Voice and Tone

Use short status labels followed by the observed reason or next action. In a warning, name the behavior, the visible cue, and duration. In the history and reports, distinguish detector confidence, statistical uncertainty, and provider delivery evidence. State elapsed times, time zone, units, and denominators where the driver interprets results.

| Moment | Example copy |
|---|---|
| Usable feed | “Monitoring active. No qualifying behavior observed.” |
| Combined warning | “Drowsiness and phone use observed.” Follow with each cue and its duration. |
| Camera interruption | “Monitoring paused. Your face is obscured. Restore the camera view, then select Resume monitoring.” |
| Offline monitoring | “Monitoring continues on this device. Session records are waiting to sync.” |
| Alert acceptance | “Email accepted by provider. Delivery is awaiting confirmation.” |
| Analytics without exposure | “Unavailable. The camera could not observe this behavior in the selected sessions.” |
| Suppressed aggregate | “Hidden to protect participant privacy.” |

Describe observations of visible behavior and the limits of the evidence. Show the fixed recipient message from PRD §8.5 in Emergency contacts. Reserve **Delivered** for confirmed provider delivery and **Unconfirmed** for an attempt that closes without definitive evidence.

## Component Patterns

| Pattern | Behavior | Visual reference |
|---|---|---|
| Navigation and current selection | Name the active page and current subsection. Use genuine links for destinations, buttons for actions, and a distinct start action. Hide restricted admin entries and recheck on entry. | `{components.top-nav}`, `{components.nav-pill}` |
| Form fields and settings | Use persistent labels, field-level error text and a summary for failed submissions. Preserve editable input after recoverable failure. Separate Save, Disconnect, Revoke, and Delete. Show save success only after confirmation. Show which monitoring preferences will take effect in a subsequent session. Consent withdrawal and access revocation take effect immediately under their respective policies. Live behavior, severity and timing rules are fixed by the release policy. | `{components.input}`, `{typography.body}` |
| Live status and warning | Keep session, observation, recording, sync and emergency states separately labeled. Combine simultaneous qualifying behaviors in one warning and show each cue/duration. Keep the stronger warning identifiable by visible wording and emphasis. | `{colors.canvas}`, `{colors.ink}` for base surfaces. Warning treatment must meet the Accessibility Floor. |
| Session, incident and clip rows | Expose one clear detail link and individually named actions. Show timestamps, state and expiry where applicable. The incident row selects the matching timeline position and opens the details. | `{typography.body}`, `{spacing.md}` |
| Timelines, charts, KPI cards and tables | Name scope and units. Expose exact values, sample size or denominator, missing values and release/policy version when relevant. Provide a keyboard-operable data view and direct selection for interactive marks. | `{colors.canvas}`, `{colors.ink}`, `{typography.body}` for the baseline. |
| Confirmation and re-verification | Open one dialog for a destructive or privileged action. Identify the target, scope and effects. Return focus to the opener or the nearest surviving row. Keep time-critical alert cancellation direct. | Existing button and input roles in DESIGN.md. |
| Progress and access feedback | Distinguish loading, saving, queued, syncing, processing, and ready. Place retry or recovery by the affected item. Announce state changes without repeating every progress update. | `{typography.body}`, `{spacing.md}` |

## State Patterns

| Scope | Loading or in progress | Empty or unavailable | Error and recovery |
|---|---|---|---|
| Public access and onboarding | Keep entered email while awaiting verification or recovery. Show a clear continuation after provider redirects. | Verification needed, link expired, identity provider unqualified, or signup pending release. | Retry verification/recovery through Clerk. Social cancellation returns to sign-in. A linked identity returns to the existing history. Restricted accounts get the account status surface. |
| Readiness | Show camera permission prompt, feed check, asset preparation, and current eligibility separately. | Missing built-in camera, unsupported setup, unusable view, offline new start, or consent decision pending. | Explain browser permission recovery or camera correction, then Recheck. Keep monitoring inactive until checks pass. Declining clips completes the consent decision. |
| Monitoring | Display Active or Paused, plus current observation, capture and sync status. Camera loss overrides stale warnings. | Usable observation with no qualifying behaviors, or unavailable observations with the specific reason. | Manual resume after a usable view. Distinguish deliberate pause from observation loss. When hosted service is unreachable, keep local warnings while supported. |
| Ended session, Dashboard, Sessions | Show pending uploads and required sync/analytics separately. Keep a ready older session available. | No sessions, no eligible results for filters, or unavailable data. Offer Start session or Clear filters as applicable. | Retry eligible records after reconnect. Keep expired, deleted and permanently ineligible records out of retry. Refresh authorized results when available. |
| Session Detail and Personal Overview | Keep the selected scope visible during calculation. Label the scope of any still-visible previous results. | Zero detections with usable observation, no usable observations, no matching sessions, or unavailable comparison. | Explain low coverage, incompatible versions, insufficient exposure or expired inputs at the affected result. Preserve eligible descriptive figures. |
| Clips and playback | Show capture, queued, uploading, available, or loading playback as applicable. | Explain no matching clips, recording disabled, category excluded, expired, deleted, or clip unavailable from storage limits. | Retry current, eligible playback or upload. Stop playback and clear the resource when it loses eligibility. An optional clip never blocks session analytics. |
| What-If and Experiment Studio | Show selected source, method and versions while a job is queued or processing. | No eligible session/fixture, inadequate inputs, withheld inference, or a disclosure-suppressed group. | Retry a transient failure with the same inputs. Flag invalid or expired inputs and route back to source selection. Keep saved and new runs distinct. |
| Benchmark | Show an aggregate loading state with the version context. | Benchmarks awaiting approval or a metric unavailable for a class/version. | Retry retrieval of the approved aggregate; explain evidence limitations in the result. |
| Reports and exports | Show authorized job status where visible to the driver. Use Queued, Processing and Ready to review for report progress and a separate export progress state. | No reports, a submitted draft needs revision, publication blocked, expired, or withdrawn. | Direct draft correction and regeneration to the MCP agent. For an expired download link, repeat the export from the authorized report if it is still eligible. |
| Settings, Connections and Chat | Keep provider connection, consent, authorization and in-flight message status separate. | No contacts, no MCP grants, unqualified provider, disconnected provider, or a new temporary chat. | Explain invalid or opted-out contact channels, failed saves, expired provider connections, unavailable service, or exhausted allowances. Offer Reconnect, Retry or another qualified provider as applicable. |
| Admin entry, Staff Access and Audit | Show invitation validation, enrollment, challenge, saving and re-verification where applicable. | Expired invite, no matching audit records, no active grant or no permitted views. | Handle invalid/reused or rate-limited codes, recovery, last-Owner protection and permission changes. Close privileged surfaces immediately if their permission is revoked. |
| Admin Health and Adoption | Show date range and signal freshness while loading. Preserve valid sections when another source is unavailable. | Distinguish fresh zero from missing/stale telemetry and privacy-suppressed or incomplete Adoption data. | Retry unavailable data independently and retain the requested range. Show Unknown for stale signals and Unavailable for a fresh confirmed outage. |
| Account Support | Require an exact lookup and show action progress independently of lookup. | No match, no permission, or no applicable action for the account state. | Show rate limits, fresh verification requirements and action outcome. Keep entered reason selection across recoverable failure and recheck eligibility before committing. |

## Interaction Primitives

- Navigate between pages with links and a meaningful page title. Move focus to the new page heading or main region after page navigation. In-page changes preserve the originating context and focus unless the user opens a dialog or explicitly jumps to a result.
- Apply date and behavior choices together so scope changes are clear. Show active filters and a Clear filters action. Preserve position and selection on Back. Use explicit previous/next controls on long lists.
- Give timeline users Zoom in, Zoom out, Reset zoom, and a means to move the visible range without dragging. Show range boundaries and let selection jump to an event. Incident details include a link back to the selected occurrence. Clip playback starts on request, with labeled controls and keyboard seek.
- For local changes with hosted consequences, show the distinction between the local action and hosted confirmation. Keep an action in progress until its outcome is known. A transient retry preserves the original operation and selection.
- Confirm clip, session and account deletion with the affected data and separate impact on reports/downloads. Keep **Acknowledge warning**, **Cancel contact alert**, **Pause monitoring**, **Resume monitoring**, and **End session** separately named. The emergency countdown cancellation takes effect on activation without an extra prompt.
- Motion presentations follow the approved supervised procedure. Keep the driver passive, suppress the stationary preview and navigation during motion, and expose only the authorized supervisor controls under that procedure.

## Accessibility Floor

- Verify the end-to-end keyboard and screen-reader path for signup and verification, readiness and permission recovery, start, pause and manual resume, ending and sync, session analytics, timeline/clip review, deletion, and report review/export. Check emergency and supervisor controls in the approved stationary or simulated test setup. Check scoped admin and access management workflows with the same keyboard/focus behavior.
- Use landmarks, hierarchical headings, associated form labels, predictable tab order, visible focus on every control, and a skip link. Dialogs have an accessible name, contain focus, support Escape when dismissal is safe, and restore focus. Provide accessible field errors and identify disabled control prerequisites in nearby readable text.
- Announce meaningful transitions such as pause, warning escalation, countdown entry, cancellation, and delivery outcome once per transition. Keep the timer readable on demand. Avoid an announcement at every tick or prediction and preserve focus during live updates. Label warning controls distinctly and keep them keyboard-reachable.
- Pair warning severity and state with plain text and a visible non-color cue. Keep the warning distinguishable with sound disabled, color distinctions absent, or reduced motion enabled. Visual presentation settings retain readable warning text and the non-color cue. Verify contrast and focus visibility against the actual treatments inside DESIGN.md’s palette. Decorative brand motion yields to reduced-motion preferences and must not interrupt monitoring or review.
- Support browser text zoom and reflow without hiding controls or state text. Give charts, timelines, overlaps, and bins text equivalents with units, ranges and accessible data tables or ordered event lists. Support direct keyboard access to exact values. Explain blanks, gaps, and suppressed results in words. Give replay controls names, state and time position. Incident metadata provides a text description of what the recording represents.

## Responsive & Platform

Design and qualify monitoring from a supported laptop desktop viewport. When space narrows or zoom increases, stack setup, status and review sections in reading order, and keep essential controls visible. Wide tables may scroll in a labeled region with a keyboard-accessible data view. The live workspace preserves state and controls when the layout reflows. For devices or browsers outside the approved monitoring setup, explain the supported setup and keep Start disabled. Mobile monitoring is outside the approved experience.

## Session and Emergency Mode Transitions

### Readiness, monitoring, and recovery

| From → to | Trigger and visible result |
|---|---|
| Readiness → Active | While stationary, accept controlled use if needed, confirm session context, qualify the built-in camera and view, prepare offline assets, verify current account eligibility online, and resolve recording consent. Show the setup preview. In a supervised session, explicitly authorize the designated supervisor while stationary; display delegated access and make revocation available to the driver while stationary. |
| Active → Active | In a stationary session, show the live feed, enabled qualifying behaviors or a usable view without qualifying behavior. Drowsiness, distraction, active phone use, eating and drinking follow the versioned policy. Reaching appears only after separate qualification. Escalate a persistent qualifying warning under the approved rule; use optional audio and preserve original observations after acknowledgment. Short tolerated gaps retain the incident, sustained observed recovery closes it, and cooldown governs repeat warnings. |
| Active → Deliberately paused | Driver while stationary, or the authorized supervisor, selects Pause monitoring. Preserve observations and identify the deliberate pause in the timeline. A deliberate pause is outside elapsed monitoring exposure. |
| Active → Observation-loss paused | Detect poor light, obstruction, low confidence, camera loss or another unusable feed. Replace the stale warning with the pause reason, stop producing warnings or escalation, and clear emergency dwell and countdown. Record the interval as elapsed monitoring time without usable observation. |
| Paused → Active | Show camera readiness when restored. The stationary driver manually resumes with a usable view. Start fresh behavior and emergency qualification. Supervisor authorization covers pause, warning acknowledgment and countdown cancellation. |
| Active or paused → Ended | The stationary driver ends the session. Stop the live camera, capture and unsent emergency actions. Show summary availability and sync separately. Release supervisor access. |
| Active → Active offline → Syncing | A configured session continues running on-device in the open monitoring tab. Show why records or clips are pending, sync each eligible item once after reconnect, and keep an interrupted or failed transfer distinct from a lost or unavailable item. The supported baseline is 30 minutes of continuous offline monitoring after readiness. |
| Tab closed, reloaded or crashed → Interrupted → Ended | Live observation ends and committed data remains locked if identity cannot be verified. Same-driver eligible online sign-in recovers pending data and finalizes at the last durably recorded observation. A new session goes through readiness. On sign-out, stop private processing and clear visible/decrypted data across open tabs. Other accounts see none of the pending data. |

Recording is video-only, with a separate opt-in, eligible behavior categories, a visible capture state, and **Stop recording**. A saved opt-in is visible during readiness. The camera feed stays on-device and setup requests camera permission only. Declining recording leaves camera monitoring available. Settings show the default three seconds before/after, independent 0–5 second ranges, and limits of 30 seconds and 20 MB per clip. Label a truncated clip as the available first segment. With no consent or a nonmatching category, no clip is expected. Revocation stops capture and discards unsent clips, including transfers still pending. The queue limit is 100 MB or 20 clips. At a queue or storage limit, mark affected new clips unavailable while monitoring and local warnings continue.

### Emergency Mode and delivery evidence

Emergency Mode is active only in an eligible supervised session with qualified delivery under the approved procedure. Settings support up to two contacts in explicit driver-selected order with email, WhatsApp, or both. Use labeled move controls to reorder. Show saved, qualified, opted-out, and unavailable channel states. WhatsApp eligibility depends on off-app opt-in and must be rechecked after number changes. Confirm contact edits or removals before treating them as saved and prevent stale sends to the old destination. Show a separate location sharing choice and the fixed alert preview.

| Stage | Driver and supervisor experience |
|---|---|
| Unavailable or standing by | Explain an ineligible session, absence of authorized operator, or absence of eligible channels before use. Ordinary warnings remain available. Sustained qualifying drowsiness alone advances an eligible session. |
| Countdown | Show an explicit **Contact alert countdown** with the remaining time and **Cancel contact alert**. Acknowledge warning leaves the countdown intact. Cancellation, observed recovery, camera pause or session end stops unsent attempts. Manual resume after a camera pause starts fresh qualification and a full cancellation window. The PRD defines controlled-test starting values of 10 seconds of continuous qualifying drowsiness, a separate 15-second cancellation window, and a 120-second attempt deadline from countdown entry. |
| Attempt and fallback | Attempt each eligible channel for the current contact at most once, with fresh authenticated online confirmation from the active tab for every attempt. Skip contacts without eligible channels. Confirmed delivery on either channel closes fallback. Move to the next contact only after all eligible channels for the current contact have been attempted and report terminal failures. Pending or ambiguous results do not justify advancing. |
| Withheld or closed | Show why an unsent attempt was withheld when known, including offline, canceled, recovered, paused, ended, stale contact eligibility, or expired. Keep that outcome distinct from an ambiguous attempted send. Reconnect does not resend or resume stale alerts. A later bounce may update channel evidence without reopening a closed sequence. |
| Channel outcome | Show **Pending**, **Accepted**, **Delivered**, **Failed**, and **Unconfirmed** for each attempted eligible channel. Accepted means processing by the provider. Delivered requires positive delivery evidence. At the deadline, unresolved attempted channels are Unconfirmed. Keep channel outcomes separately discoverable from the session timeline. |
| Recipient | Deliver the fixed message and an authorized usable map location directly to email or WhatsApp. Otherwise include “Location unavailable.” The recipient can read the message and open the map without signing in to RAFIQ. |

## Review, Analysis, and Data Lifecycle

### Session Detail and Personal Overview

| View | Interaction and interpretation |
|---|---|
| Session Detail KPIs | Show monitored time, incident count and incidents/hour, total time and percentage with detected behavior, observation coverage, and warning count. Provide descriptive statistics and sample sizes as applicable. |
| Session timeline and incident detail | Use elapsed time since session start. Give each detected behavior its own row and show deliberate pauses and observation loss in an observation row. Distinguish usable time without detections. Mark warnings and Emergency Mode events. Selecting an incident jumps to its timestamp and displays end time, duration, constituent behaviors, overlap, confidence and available measurements and clip. An Emergency Mode marker opens recorded per-channel outcomes. Timeline zoom changes the timeline range only. Keep original detection details if the driver disagrees with a result. |
| Session breakdown and durations | Toggle horizontal bars between count and duration with exact values. Up to 30 matching detections, show individual durations by behavior. Above 30 use fixed bins of 0–<2, 2–<5, 5–<10, 10–<30 and ≥30 seconds. Show the sample size. |
| Personal Overview KPIs and filters | Show five cards for completed sessions and monitored hours, incident count and incidents/hour, time and share with detected behavior, coverage, and warning count and warnings/hour. Default to the last 30 days. Offer last 7 days, all available history, custom dates, sessions and behavior filters. Include only completed sessions whose analytics are ready and display separate pending and unavailable counts. |
| Trends and session comparison | Switch between incidents/hour, warnings/hour and share of time with detected behavior. Through 30 days use daily points; use local Monday-starting weeks for longer ranges. Group a whole session by its start date in the displayed time zone. Show monitored time and coverage per point, and gaps for unusable data. Compare KPI values and behavior breakdowns for two to four selected sessions with exposure and coverage alongside rates. |
| Ranking, overlap and time bands | Rank by detection count, duration or share of behavior-observable sessions. In the overlap matrix, show incident count with actual overlap and the number of sessions where both classes could be observed together. Show incident rate, monitored minutes, coverage, and contributing sessions in 0–<5, 5–<15, 15–<30, 30–<60, and 60+ monitored-minute bands. Assign incidents by start. |
| Findings | Compare with the immediately preceding window of equal length under matching scope and time zone. Require an eligible completed session, at least 15 monitored minutes, at least 90% coverage and comparable versions in both windows. Show the available values and the reason when a comparison is withheld. Report absolute change when the baseline is zero. |

Use pooled monitored hours for rates and total monitored exposure for percentage of time with detections. Count a combined incident or warning once and use the union of overlapping behavior time for the overall total. Preserve individual behavior durations and applicable coverage in the breakdown. Behavior filters match any selected behavior while preserving the selected sessions' exposure and overall coverage. Flag coverage below 90% using unrounded figures. Distinguish unavailable exposure or observability from a confirmed zero. Label relevant catalog, model and policy version changes. Use validated results with their units, denominator, sample and input revision.

### What-If, Experiment Studio, and Benchmark

- **What-If.** Show only owner-authorized retained sessions with a compatible measurement series, observation flags, timestamps, policy and sufficient values. Select eligible inputs, change supported simulation thresholds, review the baseline and run. Compare the saved versioned result with the recorded baseline and label differences as simulated. Show missed detections, false alarms or accuracy only when reference labels support them. Keep clips and precise location out of the simulation and keep saved runs separate from source sessions, live policy and Emergency Mode.
- **Experiment Studio.** Select a versioned synthetic paired or independent-group fixture or an approved predefined study, select conditions and approved method, and run or rerun saved inputs. Present eligible descriptive outputs and, where prerequisites pass, exploratory inference. Show the study design, conditions, observation unit, inputs, sample size, method, data/analysis versions, estimates, uncertainty, and sample limitations alongside any result. For paired comparisons show the mean within-participant difference in incidents per hour, the two-sided paired permutation test and 95% paired bootstrap interval with at least 10 complete pairs. For independent groups show the proportion of participants with at least one incident, the two-sided Fisher’s exact test and 95% Wilson intervals with at least 10 participants per arm. Include the 0.05 significance level and reproducibility settings, such as the bootstrap seed and draw count, in method details. Withhold inference with a reason when prerequisites fail. Show and export only approved aggregates meeting the 10-participant minimum in each visible group and suppress complementary results that would disclose a hidden group. The surface uses predefined inputs without new participant collection or access to private driver records.
- **Benchmark.** Present approved aggregate held-out performance with dataset, catalog and policy versions, class-level precision, recall, F1, accuracy and confusion counts or matrices, overall and class coverage, false warnings per monitored hour, and warning delay. Include labeled sample/exposure context and explain how class-unusable intervals were excluded from scoring. Approved benchmark findings are available as references for general reports; evaluation inputs and the benchmark runner are internal.

### Retention, privacy, and export

In Clips, search the private library and filter by behavior, date and session. Available replay shows the behavior, source session and relevant timing. Show retention in Settings → Privacy and expiry at point of use: queued clips 24 hours after capture, hosted clips seven days after capture, session and incident metadata 90 days after end, precise location 24 hours after capture, and hosted reports 30 days after creation or earlier when a required source expires. Explain that deletion or expiry removes access immediately and retained copies are purged within 30 days. Clip deletion leaves independent session metadata. Session or source deletion/expiry removes affected access and withdraws dependent hosted reports. Keep downloads under the driver's control. Private monitoring data is excluded from secondary evaluation or training unless separately approved.

### MCP connection, reports, and optional chat

- **MCP.** Settings → Connections → MCP gives the single HTTPS endpoint and generic compatible-client setup instructions. The driver signs in during authorization, sees the requesting client and independently approves **Read driving data** and **Author reports**. List the client's active grants with independent revoke controls. On expired or revoked authorization, show the affected client or permission and use fresh authorization where the driver chooses to reconnect. The read grant exposes only authorized own session summary and approved analytics and event metadata. Report authoring additionally permits that agent to start a job, retrieve job-approved inputs/template and check status, then submit a draft. Clips and links, raw media and measurements, contacts, precise location and finished report contents stay outside agent access. The connection exposes read and report-authoring scopes only.
- **Reports.** In the external authorized agent, the driver requests a session or trend report or asks for a new version. In RAFIQ, open the report when ready and review the checked figures, methods, sources, limitations, and approved aggregate benchmark summary when applicable. Invalid evidence blocks publication. Revoking the authoring permission or losing eligible source data during processing also blocks release. Each successful export uses the validated reviewed snapshot. An authorized export link expires after five minutes and still requires current eligibility. Show withdrawal after source expiry or deletion, and direct regeneration from eligible sources to the external agent. The browser's report actions are review and export.
- **Chat.** Each independently qualified subscription provider has its own connection and first-use consent. Explain which messages and relevant PRD §8.8 fields will be sent and the provider's data handling before the first send. Show connected, consent required, unavailable, expired, and allowance-exhausted states. The driver can ask questions and follow-ups about their own sessions and trends in an open temporary conversation. Revoke sharing or disconnect in Settings. Clear the conversation on close, sign-out, sharing revocation or disconnect and suppress responses from invalidated requests. Optional chat is independent of public signup and offers questions about driving data.

## Admin Workflows

| View | Scope, interactions, and state |
|---|---|
| Service Health | Default to the last 24 hours; offer 1 hour, 7 days and 30 days. Show key service status, uptime, API error rate and p95 latency, sync/report queues with backlog age, storage usage and quotas, backup status and lag, deletion and purge progress, and counts of pending, accepted, delivered, failed and unconfirmed attempts separately for email and WhatsApp. Show last update, applicable units and denominator for each signal. Use **Healthy**, **Degraded**, **Unavailable**, and **Unknown**. Mark a channel awaiting qualification separately from its runtime health. |
| Release Readiness | Show **Passed**, **Failed**, or **Pending** per gate, last verification, and an approved evidence link when available. Identify public launch, each emergency channel, and each optional chat provider separately. Release approval and activation follow the release process outside the dashboard. |
| Adoption | Default to the last 30 days; offer last 7 days, all history and custom dates. Show signups, verified accounts, first completed sessions, active drivers, and completed sessions, with a signup → verification → first completed session funnel. The first three cards follow the signup cohort and ordered milestones reached within seven days. Show denominators and in-progress cohorts. Plot active drivers and completed sessions. An active driver completed at least one session and is counted once per requested range and once per trend bucket. Count completed sessions by recorded end after durable completion sync. Use the displayed time zone, with daily points through 30 days and local Monday-starting weeks for longer ranges. Show incomplete inputs separately from disclosure suppression. Apply the 10-driver threshold to inferable differences, totals, funnel steps, related views and overlapping ranges. After expiry/deletion, show eligible fixed anonymous historical buckets. Mark an exact range total unavailable when it requires expired detail or would join anonymous buckets. |
| Account Support | Look up an exact registered email or account ID. Return only ID, registered email, verification status, account status and signup date. Provide eligible verification/recovery actions to the registered email, with rate-limited outcomes and without revealing credentials or message payloads. Suspension and reinstatement require both support and suspension permission, recent verification, and selection of an approved reason code. Show confirmed outcome after the change. Account deletion is a driver workflow. |
| Staff Access | An Owner creates a single-use, expiring invitation bound to a verified identity. Require authenticator enrollment before admission. Manage metrics, support and suspension permissions independently, with fresh verification for invitations and access changes. An Owner can appoint another MFA-protected Owner and can reset another admin’s enrollment after fresh verification. Reject removal of the last active Owner and remove revoked access immediately. |
| Admin MFA recovery | Allow recovery with verified sign-in and one unused recovery code, or an eligible Owner reset. Invalidate affected admin access as required before re-enrollment. Loss of the last Owner’s authenticator and recovery codes goes through audited deployment recovery. |
| Audit | Owner-only and read-only. Filter the last 90 days by staff member, action, outcome and date. Show actor, target where applicable, timestamp and outcome, including failed lookups and actions. Keep submitted unmatched email values, access codes and private driving data out of audit output. |

Admin metrics are aggregates. Only Account Support shows the explicitly permitted driver account fields. Driving sessions, observations, recordings, reports, contacts, locations, impersonation and emergency dispatch controls are outside the admin surface.

On suspension, immediately deny hosted access and invalidate existing authorization. Show the restricted status and published support contact. Block new starts and lock hosted sync. A configured session already offline retains local warnings within its existing limits. On reconnect, keep uploads locked and continue normal retention enforcement. Reinstatement requires a fresh online sign-in before eligible queued records can sync, plus fresh consent to reconnect MCP. Old sessions, download links and MCP grants stay invalid.

## Key Flows

### J1. UJ-1 — First controlled session

1. Nour signs up publicly, verifies email, signs in and accepts controlled-use conditions. Qualified social sign-in and Clerk recovery offer alternate entry paths to the same verified workspace.
2. While stationary, Nour opens Start session, grants camera access, checks the view and completes the recording choice. **Start monitoring** becomes available when readiness passes, including if Nour declines recording.
3. Nour sees active observation and an explainable warning in a controlled fixture. When the view becomes unusable, RAFIQ pauses. Nour adjusts the view and selects **Resume monitoring**.
4. **Climax** — Nour ends the session and opens the ready summary to see the recorded incidents and observation coverage.

Recovery: camera denial returns to readiness guidance and Recheck. A pending summary opens session status and links to Session Detail once required data is ready.

### J2. Private recovery, clips, and deletion

1. Nour opts into selected clip categories, checks context bounds and begins a stationary session. RAFIQ records an eligible incident clip and labels it queued when the connection drops. Local observation and warnings continue in the open tab.
2. If the tab closes, Nour signs in online again with the same eligible account. RAFIQ ends the interrupted session at the last durable observation and syncs eligible records once.
3. Nour opens the incident from Session Detail or uses the Clips filters, opens available video and sees its capture timing and expiry.
4. **Climax** — Nour deletes the clip, sees playback access removed, and can still review independent incident metadata. Nour can delete a whole session from Session Detail or start account deletion from Privacy.

Recovery: if consent was revoked or the clip expired during transfer, replay stays unavailable after reconnect. On sign-out or account switch the old queue stays locked.

### J3. Supervised warning and contact alert

1. While stationary, Nour manages contact order, eligible channels, the alert preview and location consent. Nour starts an eligible supervised session and authorizes Sam to use the delegated controls.
2. In the approved supervised test, sustained qualifying drowsiness enters countdown. Sam can acknowledge the regular warning separately and cancel the pending contact alert with its own control.
3. If current eligibility holds and the countdown completes, RAFIQ attempts eligible channels for the current contact. Contact Leila sees the message directly and opens the permitted map location when included.
4. **Climax** — Nour ends the session while stationary, then opens the Emergency Mode timeline entry and distinguishes provider acceptance from confirmed delivery.

Recovery: cancellation or camera pause stops unsent attempts. Delivery on one channel stops fallback. An ambiguous attempt becomes Unconfirmed by the deadline. Reconnect cannot repeat the attempt or start stale fallback.

### J4. Understand a session and compare periods

1. Nour opens Dashboard during sync of a newer session, sees its status and reviews the latest ready Session Detail. Nour can open the newer session when it becomes ready.
2. Nour zooms the timeline, selects an overlapping incident and inspects its detections and associated warning. Nour checks duration and coverage alongside the count.
3. Nour opens Personal Overview in one action, changes the date and behavior filters, switches a trend measure, checks overlap and time bands, and selects three sessions for comparison.
4. **Climax** — Nour can explain a rate change using the visible exposure, coverage and comparable policy versions, or can see the reason the change finding is unavailable.

Recovery: missing media leaves analytics available. Low coverage, incompatible versions, and an empty or unobservable scope are labeled at the affected output.

### J5. Run a simulation, test a study, and interpret detection evidence

1. Nour selects a compatible personal session in What-If, adjusts a supported simulated threshold, and opens the saved baseline comparison.
2. Nour opens Experiment Studio, selects approved fixture conditions and a method, then runs and reopens the result from the same inputs. Where eligible, Nour exports the permitted aggregate.
3. Nour visits Benchmark to read the approved aggregate results and coverage context for a behavior of interest.
4. **Climax** — Nour can distinguish personal simulated changes, exploratory study inference, and held-out RAFIQ performance by their labels, sources and versions.

Recovery: unsupported accuracy claims remain absent when reference labels are missing. Ineligible samples retain descriptive results where permitted, and disclosure-suppressed groups stay hidden in views and exports.

### J6. Author through MCP and review a report

1. Nour opens MCP settings, follows the compatible-client setup, signs in and grants the agent report authoring. Nour independently decides whether to grant read access.
2. From the external client, Nour asks for a trend or session report. The agent starts a job, uses the approved evidence, and submits its draft. RAFIQ validates it and makes an eligible report ready for review.
3. **Climax** — Nour opens the checked report and exports it as PDF or Word with matching figures. A request for a new version goes back through the agent.

Recovery: invalid evidence returns a revision status to the agent. Source deletion or expiry withdraws the affected report, and revocation during generation stops publication. A still-eligible report can issue a fresh export after link expiry.

### J7. Ask a temporary chat question

1. Nour opens Settings → Connections, links a qualified subscription and reviews and accepts the provider’s sharing disclosure.
2. Nour asks about trends, checks the scope of the answer and asks a follow-up. Provider availability and quota states offer an applicable recovery.
3. **Climax** — Nour closes the chat or revokes sharing and sees the conversation clear. Any response from an invalidated request is withheld.

Recovery: an expired connection offers Reconnect. An unqualified provider cannot be selected and the rest of the driver workflow remains available.

### J8. Operate RAFIQ and support an account

1. Owner Rana signs in with MFA, checks Service Health and release evidence, and reviews Adoption. A small cohort is labeled suppressed while eligible aggregates remain visible.
2. Rana invites Staff member Omar and grants support and suspension permissions. After invite acceptance and TOTP enrollment, Omar lands on Account Support and looks up Nour’s exact registered email. An eligible identity message goes to the account’s registered email.
3. With fresh verification and an approved reason, Omar suspends the account. Nour sees restricted status on reconnect while a configured offline session retains local warnings within its existing limits. Omar subsequently reinstates the account through the same verification and reason flow.
4. **Climax** — Rana sees the lookup and state changes in Audit. Nour signs in afresh and can sync still-eligible queued records, with separate fresh consent for any MCP reconnection.

Recovery: expired invitations, invalid or reused TOTP, revoked staff access, last-Owner protection and unavailable telemetry each show their specific state. Owner reset, a valid recovery code, or audited deployment recovery applies as appropriate.

## Requirement Coverage

| Approved requirement | Surface and journey |
|---|---|
| FR-01 · Public account access and recovery | Public entry, verification, recovery and onboarding · J1 |
| FR-02 · Driver data isolation | Private app, playback/export, Connections and account boundaries · J2, J6, J7, J8 |
| FR-03 · Profile and settings | Profile, Monitoring, Emergency contacts and Privacy · J1–J3 |
| FR-04 · Session readiness and lifecycle | Readiness, Monitoring and ended session · J1–J3 |
| FR-05 · Observe and show driver state | Monitoring · J1, J3 |
| FR-06 · Handle unreliable observation | Monitoring pause and timeline · J1, J3, J4 |
| FR-07 · Warn and explain | Monitoring, incident details and timeline · J1, J3, J4 |
| FR-08 · Continue a configured session offline | Monitoring, session status and queue recovery · J2, J8 |
| FR-09 · Control entry and cancellation | Supervised readiness and Emergency Mode countdown · J3 |
| FR-10 · Send an emergency message and location to registered contacts | Emergency contacts, delivery states, recipient channels and timeline · J3 |
| FR-11 · Preserve session observations | Sessions, timeline, incidents and summary · J1, J2, J4 |
| FR-12 · Record consented, bounded clips | Readiness, Monitoring, Clips and Privacy · J1, J2 |
| FR-13 · Review, expire, and delete data | Clips, Sessions, Privacy and Reports · J2, J6 |
| FR-14 · Analyze personal driving sessions | Dashboard, Session Detail and Personal Overview · J4 |
| FR-15 · Show reproducible statistical results | Experiment Studio methods and result evidence · J5 |
| FR-16 · Run what-if simulations | What-If · J5 |
| FR-17 · Run controlled experiments | Experiment Studio · J5 |
| FR-18 · Measure and publish detection performance | Benchmark and report summaries · J5, J6 |
| FR-19 · Author reports through MCP and review them in RAFIQ | External agent and Reports · J6 |
| FR-20 · Retrieve authorized data and author reports through MCP | Connections, MCP authorization and revocation · J6, J8 |
| FR-21 · Ask about driving data in RAFIQ | Connections and optional chat · J7 |
| FR-22 · Monitor RAFIQ and support driver accounts | Admin entry, Health, Readiness, Adoption, Support, Staff Access, MFA recovery and Audit · J8 |
| NFR-01–06 · Setup, capacity, recovery, accessibility, privacy and operating conditions | Foundation, Responsive & Platform, State Patterns, Accessibility Floor and session transitions · J1–J8 |
| SM-01–05 · Public journey and release evidence | J1 covers unassisted completion; Benchmark represents approved aggregate evidence and Service Health surfaces gate outcomes. |

## Qualification and Visual Handoff

- Apply the campus demonstration milestone to the normal stationary journey: show a warning, camera pause and session summary, with benchmark and gate evidence as specified in the PRD and TRD.
- Public signup, each social connection, each live alert channel and each optional chat provider reflect their own qualification status. The supervised motion presentation follows the institution-approved procedure. Use controlled stationary or simulator fixtures to verify time-sensitive interactions before qualifying them in motion.
- **UX decisions for handoff.** Navigation labels, page groupings, warning presentation behavior and sample copy are specified here. For configurable warning visibility, use a default presentation and an enhanced visibility option that makes the warning text and non-color cue more prominent. Specific warning and focus treatments and chart visuals require RAFIQ-specific design work within the existing visual reference. TRD §1.1 points to the Pen.dev design for chart handoff. Experiment Studio aggregate export format is unspecified by the PRD and TRD.
