---
title: RAFIQ Product Requirements Document
status: final
created: 2026-11-20
updated: 2026-11-20
approved_by: Ali Sameh
---

# RAFIQ Product Requirements Document

## 1. Product intent

RAFIQ is a desktop-browser SaaS application for individual drivers in controlled sessions and supervised vehicle testing. It uses the device’s built-in camera to identify visible cues for drowsiness, distraction, phone use, eating, drinking, and additional behaviors that pass the checks in §8.3. The driver receives timely warnings and can review what RAFIQ observed after the session.

RAFIQ’s differentiator is reproducible analysis of the observations behind those warnings. A driver can review a timeline, compare sessions, test how different thresholds would change recorded results, and review a report backed by verifiable measures. Drivers already using monitoring tools are the initial audience. The design and engineering team will use this PRD to define the experience, requirements, and release evidence.

The project plans a free, English-language public release. Adult drivers can register, sign in, and use the released features through public self-service after release approval. Ali Sameh owns release sign-off. Section 8 specifies operating limits and evidence required before activation. The campus demonstration on 15 December 2026 is a separate project milestone. The original feature brief (`RAFIQ.md`) supplied product context. The MVP boundary below captures the disposition of its features, and interview decisions set the scope in this PRD.

## 2. MVP boundary

| Source features | Disposition |
|---|---|
| 1–10 and 12 | MVP. On-device monitoring, a versioned behavior catalog, concurrent detections, warnings with explanations, escalation within local warnings, and pause for unreliable observation. |
| 11 | Emergency Mode for eligible supervised sessions. Enable email and WhatsApp independently after the applicable operating and delivery checks pass. |
| 13–16 | Deferred. Risk score, personal calibration, behavior fingerprint, and behavior chains. |
| 17–18 and 20–24 | MVP. Session observations, descriptive and approved inferential statistics, personal dashboard, timeline, what-if simulation, and Experiment Studio. |
| 19 | Required release evidence. Publish approved aggregate benchmark results and include a summary in general reports. Running evaluations and exporting dedicated benchmark reports are outside the driver-facing scope. |
| 25–31 and 33 | MVP. Private driver accounts, profiles and settings, sessions, consented clips, private replay, and privacy controls. |
| 32 and 34 | MVP. MCP for authorized reads and agent-authored reports. Drivers review and export finished reports in PDF or Word. |

In-app chat is optional. Each provider becomes available when its subscription connection and privacy checks pass. Public signup can open regardless of provider availability.

The first public release includes an internal admin dashboard for service health, product adoption, and limited driver account support (FR-22).

Billing, organization workspaces, fleet dashboards, cross-driver browsing of driving data, routine unsupervised use, mobile monitoring, dedicated vehicle hardware, vehicle control, medical diagnosis, certified unconsciousness detection, accident prediction guarantees, public emergency dispatch, guaranteed GPS, manual detection correction, standalone reliability and camera stress-test modes, separate demo and research modes, raw personal data export, and MCP sharing or control actions are outside MVP scope.

### Rollout sequence

1. **Pre-launch validation.** Test self-service signup, the core session workflow, analytics, the What-If simulator, Experiment Studio, reports, MCP, and the admin dashboard. Qualify the deployed MCP endpoint with a client-neutral reference client before activation.
2. **Public signup.** Open English-language self-service registration and released features to adult drivers after the public release gates pass. Test participants can come from the public. Enable each emergency delivery channel and chat provider after its own checks pass.

## 3. Users and core journey

**Driver.** A public RAFIQ user who wants to know whether monitoring is active, understand why RAFIQ issued a warning, and review their own observations and clips. The driver's personal dashboard and driving records are private. Authorized support staff can see only the account fields listed in FR-22.

**Owner and Staff.** Invite-only roles for the RAFIQ team. The Owner manages staff access and can review the admin audit history. Staff use only the features the Owner assigns. Both roles use the admin dashboard under FR-22.

**Supervisor.** A person present during supervised vehicle testing whom the driver authorizes while stationary to use the warning acknowledgment, emergency countdown cancellation, and pause controls on the driver’s device. The driver starts sessions and uses controls while stationary. The supervisor has no separate RAFIQ sign-in or account access. If authorized interaction is unavailable, workflows that require interaction during motion are unavailable for that test session. See §8.2.

**Emergency contact.** A person the driver registers with an email address, a WhatsApp number, or both. A contact receives the alert and available, permitted location directly in their messaging app or inbox. Receiving an alert requires no RAFIQ account, confirmation link, or check-in. WhatsApp requires the contact’s opt-in under its provider rules.

### UJ-1. First controlled session

Nour, an illustrative first-time driver, creates a public account and signs in on a desktop browser. Nour checks the built-in camera, reviews recording consent, and starts a controlled monitoring session. The app shows that monitoring is active. If a behavior qualifies for a warning, Nour can see the behavior, the observed cue, and its duration. If observation is unreliable, the session pauses and Nour can resume manually after restoring a usable view. Nour ends the session and opens the summary to see recorded incidents and observation coverage. See SM-01 for the usability check.

## 4. Product terms

| Term | Meaning |
|---|---|
| Session | A driver-started monitoring run with active, paused, and ended states. |
| Behavior detection | A model observation associated with a behavior in the supported catalog. A detection has a time span, confidence, and supporting observations when available. |
| Incident | A session record that groups overlapping behavior detections while retaining individual behavior labels and times. |
| Warning | Visual feedback, with optional audio, for qualifying behavior detections. Acknowledging a warning does not erase the underlying observation. |
| Observation coverage | Usable observation time divided by elapsed monitoring time as defined in §8.3. |
| Incident clip | Consented, video-only recording linked to an incident, with bounded configurable context around the event. |
| Emergency Mode | The controlled escalation state that can send an alert to driver-registered contacts by email and WhatsApp in eligible supervised sessions. |
| Accepted alert | A delivery provider accepted the alert for processing. The interface shows acceptance and delivery separately for each channel. |
| Confirmed delivery | Positive delivery evidence from a provider. Delivery on either channel stops progression to a later contact. Reading or replying is a separate action. |
| Benchmark | A repeatable run against a held-out, controlled RAFIQ dataset. Labeled frames are the primary matching unit for per-behavior precision and recall. |

## 5. Functional requirements

### 5.1 Accounts, privacy, and readiness

**FR-01. Public account access and recovery.** Adult drivers can create an account through public self-service, verify their email, sign in, recover access, and use released features. Access uses the public account and the operating conditions for each feature.

- **AC-01.** Verify signup, email verification, sign-in, recovery, and use of the core workflow with a new public account that has no university affiliation, invitation, or enrollment record. Deny private data access to unverified or unauthenticated visitors.

**FR-02. Driver data isolation.** The driver can access only their own profile, sessions, data, reports, settings, and recordings. Access restrictions apply throughout the browser and all connected product surfaces, including in-app chat, MCP, and file retrieval.

- **AC-02.** A second driver cannot access another driver’s resources through direct links, changed identifiers, or assistant requests. Expired or revoked authorizations deny access even to resources previously available under that authorization.

**FR-03. Profile and settings.** The driver can view monitoring history and manage emergency contacts, the supported camera, optional warning audio, recording categories and context, and privacy settings. Emergency settings show the alert message and available contact channels. The product supplies the live behavior, severity, and timing rules.

- **AC-03.** The driver can save supported preferences and apply them in a subsequent session. Verify that a driver can register, edit, and remove contact channels without requiring a recipient account or RAFIQ confirmation. Recheck WhatsApp eligibility when its number changes and block pending sends to removed destinations. Simulation and settings changes cannot alter live thresholds.

**FR-04. Session readiness and lifecycle.** A signed-in driver starts a session after camera readiness and consent checks. The app shows the current session state, supports pausing and ending, and requires manual resume after an interruption. The driver can review an ended session. A camera preview is available during stationary setup.

- **AC-04.** A supported camera and completed readiness checks enable start whether the driver grants or declines recording. Camera denial provides a recovery path and leaves monitoring inactive. After disruption, a usable camera and manual action are required to resume. Ending the session closes the monitoring run and makes its summary available when the required data syncs. During supervised testing, verify that the pre-authorized supervisor can use only the approved warning and interruption controls. Workflows requiring interaction during motion are unavailable when there is no authorized operator.

### 5.2 On-device monitoring and warnings

**FR-05. Observe and show driver state.** Once set up, RAFIQ processes live camera input on the device. In a controlled stationary session, the driver can see a live camera feed and the current observation state. The observation state shows the supported behaviors currently qualifying, a usable observation without a qualifying behavior, or unavailable observation. The supervised-use procedure governs presentation during motion. Fixed release rules use the following observable boundaries.

| Behavior | Positive label |
|---|---|
| Drowsiness | Visible cues such as sustained eye closure and unusually long or slow blinks. Evaluate repeated yawning as a supporting cue. An ordinary blink or isolated yawn is a negative example for a drowsiness alert. |
| Distraction | Sustained off-task gaze or head direction. Include brief mirror checks as negative examples. |
| Phone use | Observable interaction with a phone, such as handling it to text or taking a call. An unused phone in view and an empty hand near the ear are negative examples. |
| Eating | Observable food consumption, supported by hand-to-mouth movement in the context of food or an eating utensil. Include talking and unrelated hand-to-face gestures as negative examples. |
| Drinking | Observable sipping or drinking, supported by hand-to-mouth movement with a cup, bottle, or another visible drink container. Include holding a cup without sipping as a negative example. |

V1 uses pretrained face and hand tracking and object detection with RAFIQ's calibrated behavior rules. The camera provides evidence of each action over time. The [technical design](TRD.md#21-pretrained-browser-vision) records the selected components.

**Candidate for a new behavior.** Evaluate reaching for an object away from the driving position, such as reaching toward a passenger seat or footwell. Enable it as a standalone class once it passes §8.3.

- **AC-05.** A stationary session shows the live feed and distinguishes concurrent behaviors, usable observation without a qualifying behavior, and unavailable observation. Test positive, negative, overlapping, and unusable examples for each class. When only a class's cues are obscured, mark that class unavailable and continue evaluating observable classes. Add a new class through the benchmark and release checks in §8.3.

**FR-06. Handle unreliable observation.** RAFIQ shows when low confidence, poor light, obstruction, or camera loss makes monitoring unreliable and pauses the session. It identifies affected intervals in the session record.

- **AC-06.** With an unusable feed, monitoring displays a plain-language pause state that takes precedence over any stale warning. The affected interval produces no new warning or escalation. Restoring the feed permits manual resume. The session summary reflects the affected interval in observation coverage.

**FR-07. Warn and explain.** RAFIQ issues a combined visual warning for overlapping qualifying behaviors and plays audio if enabled. The warning states the behaviors, the observable cues, and how long they were observed. Each behavior has a fixed policy for severity, qualifying duration, escalation, short detection gaps, sustained recovery, and cooldown. Validate these policies on calibration data and freeze them before release scoring. The product preserves the original detection when a result is disputed.

- **AC-07.** Two overlapping qualifying behaviors produce one warning naming both. A persistent behavior crossing the approved severity threshold produces a visibly stronger warning. Policy fixtures verify recurrence after acknowledgment, cooldown, short gaps, and sustained recovery. A short approved gap stays within one incident. Sustained recovery ends that incident. Audio can be switched off while visual warning remains available.

**FR-08. Continue a configured session offline.** After setup, on-device monitoring and local warnings continue through network loss. The product shows which session records and consented clips are waiting to sync, resumes synchronization when service returns, and keeps records associated with the same driver and session.

- **AC-08.** Losing connectivity during a usable session preserves local monitoring and warnings. After reconnect, each retained record appears once in history under its original account. The prior account’s pending data is inaccessible after sign-out and from any other account using the same browser. The driver can distinguish pending, available, and unavailable records and clips. See §8.4 and §8.6 for queue limits and retention.

### 5.3 Emergency Mode for eligible supervised sessions

**FR-09. Control entry and cancellation.** Sustained drowsiness is the only trigger for Emergency Mode in an eligible supervised session. Use distinct controls and statuses for acknowledging a regular warning and canceling a contact alert. Cancellation or observed recovery stops unsent alerts. A camera pause clears the qualifying dwell and countdown. After manual resume, a fresh qualification starts a full cancellation window. Enable live delivery per channel under §8.5.

- **AC-09.** Verify the countdown and explicit cancellation with each enabled channel. Acknowledging a warning leaves the alert state unchanged. Cancellation, recovery, or a camera pause prevents any unsent alert. Verify that an ordinary blink, an isolated yawn, and any other behavior class alone leave dispatch inactive. Resume requires a fresh qualifying observation and a full cancellation window.

**FR-10. Send an emergency message and location to registered contacts.** The driver registers contacts and their email addresses or WhatsApp numbers. RAFIQ sends the emergency message and available, separately permitted location directly over email and WhatsApp when both channels qualify for the contact. A contact can read the message and open the location in a map without a RAFIQ account or check-in. If location is unavailable or sharing permission is absent, send the message with a location-unavailable notice. RAFIQ retains precise location for a separate, bounded period.

RAFIQ tries the driver’s contacts in order. For the current contact, it attempts each eligible channel once within the time limit. Delivery on either channel stops progression to the next contact. Advance after all eligible channels for the current contact have been attempted and have reported terminal failures. Show Pending, Accepted, Delivered, Failed, and Unconfirmed per channel. A pending or ambiguous outcome expires as Unconfirmed if evidence is still missing at the deadline. See §8.5.

- **AC-10.** Test email only, WhatsApp only, both channels, and an unavailable channel. Verify that contacts can read the message and open the map location directly. Test absent or revoked location permission, WhatsApp opt-in and opt-out, delivery on one channel while the other fails, total confirmed failure, ambiguous outcomes, and duplicate callbacks. Verify that ending the session, expiry, contact edits or removal, and offline cancellation prevent stale sends.

### 5.4 History, recordings, and data lifecycle

**FR-11. Preserve session observations.** RAFIQ links detected behavior, timestamps, durations, confidence, relevant measurements, warnings, incidents, observation coverage, and recording references to the driver’s session. Overlapping detections can contribute to one incident. The session summary distinguishes elapsed monitoring time, coverage, and incident count.

- **AC-11.** In a session with overlapping behaviors, each behavior appears with its original details, and the grouped incident is counted once. Paused and unobservable time is distinguishable from observed time without a detection.

**FR-12. Record consented, bounded clips.** The driver can opt in once, choose eligible recording categories, see recording state, and stop capture. The live feed stays on-device. A consented matching incident can produce a video-only clip for private hosted storage. RAFIQ sets defaults and bounds for configurable pre-event and post-event context and a maximum clip length. Temporary pre-event context stays on the device. Unsent clips remain private to the same driver through sign-out, within capacity and retention limits. Revoking recording consent discards unsent clips.

- **AC-12.** Declining recording or a nonmatching category yields no saved clip or uploaded live feed. An eligible incident yields one owner-only video clip within the bounds or a visible unavailable state. Clip output has no audio track and the workflow requires no microphone permission. Test revocation during capture and pending upload. The revoked queue items are discarded and stay unavailable after reconnect. Each remaining eligible clip uploads once.

**FR-13. Review, expire, and delete data.** The driver can search and filter their private clip library by behavior, date, and session, replay clips, and delete a clip, session, or account. RAFIQ communicates separate service-wide clip and metadata expiry periods. Block access to affected records immediately on expiry or deletion and purge retained copies by the approved deadline. Section 8.6 specifies report and export handling and institutional retention verification. Private session data is ineligible for secondary reuse in model evaluation or training until separately approved.

- **AC-13.** Search and filters return only accessible matching clips. Expiry or deletion blocks access to affected records immediately through the UI, direct retrieval, and MCP. Verify expiry and deletion while a record is queued or uploading. A sync retry cannot restore expired or deleted data. Deleting a clip leaves independently retained session metadata. Verify the purge deadline and report and export handling in §8.6.

### 5.5 Personal analytics, simulation, and controlled experiments

**FR-14. Analyze personal driving sessions.** The private dashboard helps drivers understand what RAFIQ recorded, when it happened and for how long, which behaviors recur or overlap, how sessions and periods compare, and how much the camera could observe. It uses session timing, camera observations, warnings, Emergency Mode outcomes and available incident clips. Opening the dashboard shows the latest completed session with available analytics. Personal Overview is one click away. When a newer session is syncing, show its status and offer a shortcut when its analytics are ready. If none are ready, explain the pending or unavailable results. Give a driver with no sessions a way to start one.

**Session Detail.** Show five KPI cards for monitored time, incident count and incidents per monitored hour, total time and percentage with at least one detected behavior, observation coverage, and warning count. Show supporting descriptive statistics and sample sizes where applicable.

| View | What the driver can answer |
|---|---|
| Zoomable timeline | When did a behavior start and end? Which behaviors overlapped? Give each detected behavior a row, show pauses and gaps in an observation row, and mark warnings and Emergency Mode events. Distinguish usable time with no detections, deliberate pauses, and unavailable observation. Show the zoomed range while the KPIs and other charts retain their full-session time range. |
| Behavior breakdown | Which behaviors occurred most often or took the most time? Use horizontal bars with a count or duration toggle and show the exact values. |
| Duration distribution | Were detections short or long? Plot individual durations by behavior through 30 matching detections, then show counts grouped into fixed duration ranges. Show the sample size. |
| Incident detail and outcomes | What contributed to an incident, and what did RAFIQ do? Selecting an incident jumps to its timeline position and opens timestamps, duration, constituent and overlapping behaviors, and the clip when available. Show warning totals and recorded Emergency Mode outcomes, with links to their times and channel statuses where applicable. |

**Personal Overview.** Show five KPI cards for completed sessions and monitored hours, incident count and incidents per monitored hour, time and percentage with detected behavior, observation coverage, and warning count and warnings per monitored hour. Default to the last 30 days and offer the last 7 days, all available history, or a custom range, plus session and behavior filters. Group a session by its start date in the displayed time zone. Use completed sessions with ready analytics and show the number still syncing or unavailable. Keep a session eligible when its optional clip is missing.

| View | What the driver can answer |
|---|---|
| Trend chart | How have incidents per hour, warnings per hour, and the percentage of time with detected behavior changed? Switch between the measures. Use daily points through 30 days and weekly points for longer ranges. Show monitored time and coverage for each point, with visible gaps where usable data is absent. |
| Session comparison | How do two to four selected sessions compare? Show their KPI values and behavior breakdowns side by side, with monitored time and coverage alongside rates. |
| Ranked behavior bars and overlap matrix | Which behaviors recur, and which happen at the same time? Rank behaviors by detection count, duration, or share of eligible sessions. For each pair, show the number of incidents with an actual overlap and the number of sessions where both behaviors could be observed at the same time. |
| Time since monitoring began | How far into a session did incidents tend to start? Show the incident rate, monitored minutes, and number of contributing sessions for 0–5, 5–15, 15–30, 30–60, and 60+ monitored minutes. |
| Plain-language findings | Which behaviors recur, and what changed versus the immediately preceding period of the same length? Highlight a change only when each period has at least one completed session, 15 monitored minutes, and 90% observation coverage, and the detection versions are verified as comparable. Keep available figures visible and explain when a comparison is unavailable. |

**Interpretation.** Count an incident or warning once even when it contains several selected behaviors. A multi-behavior filter matches any selected behavior and retains the monitoring time and coverage for the selected sessions. Use total monitoring time for pooled hourly rates and for the percentage of time with a detection. Count overlapping behavior time once in that overall total and retain each behavior’s duration in the breakdown. Label units, denominators and applicable sample sizes. Show per-behavior coverage when available and use sessions with some usable observation for that behavior in its share-of-sessions denominator. Flag coverage below 90%, distinguish zero detections from unavailable observations, and mark detection rule changes on historical figures. See TRD §5.1 for the calculations.

- **AC-14.** Verify all five cards in each view, charts and filters, two to four session comparisons, timeline zoom and incident selection, direct access to Personal Overview, and the fallback while the latest session syncs. Known fixtures must reproduce counts, rates, coverage, overlap, durations and distributions. Verify coverage and sample boundaries, zero versus unavailable results, missing clips, daily and weekly grouping, and comparison eligibility across periods and detection versions.

**FR-15. Show reproducible statistical results.** The product provides confidence intervals and a small set of approved hypothesis tests for named comparisons and study designs. Design and engineering propose the prerequisites and reproducibility tolerance for each method using fixtures with known results. Results identify the observation unit, inputs, sample size, method, uncertainty, and data or analysis version. If a sample fails the approved prerequisites, the product withholds inference and provides available descriptive results and a reason.

- **AC-15.** Repeating a run with the same eligible data, filters, and method produces the same numerical results within the accepted tolerance. An ineligible sample receives descriptive output without a test conclusion. See §8.7 for the method catalog and prerequisites.

**FR-16. Run what-if simulations.** A driver can vary supported detection thresholds against eligible inputs from their own recorded sessions and compare the results with the baseline. Report accuracy comparisons, missed detections, and false alarms only when reference labels support them. Simulation settings remain independent of live policy.

- **AC-16.** A change to the simulation inputs produces a versioned comparison with the baseline, and identical inputs produce identical results. Tests cover owner isolation and the absence of accuracy claims when reference labels are unavailable. Live thresholds, session records, and emergency sequences stay independent of the simulation. See §8.7 for input eligibility.

**FR-17. Run controlled experiments.** At first release, Experiment Studio uses approved predefined study datasets and test fixtures to organize observations and compare conditions. The studio may expose cross-participant results only as aggregates that meet approved minimum group sizes and export rules. Private driver histories and clips stay private. New participant collection is outside the first release.

- **AC-17.** On an approved fixture or dataset, conditions remain distinguishable and selected analyses rerun from saved inputs. Views and exports suppress groups below the approved minimum and exclude individual cross-participant records. Drivers cannot open another driver’s experiment or private records. The first release does not collect new participants through the studio.

**FR-18. Measure and publish detection performance.** Use an approved controlled RAFIQ dataset held out from tuning. Approve the annotation guide’s mapping to the versioned behavior catalog and freeze frame-level matching rules before scoring per-behavior precision and recall. Mark unusable intervals by behavior and report per-behavior and overall coverage. Report accuracy, F1 scores, relevant confusion matrices or equivalent multi-label per-class counts, false warnings per monitored hour, and warning delay. Publish approved aggregate benchmark results to drivers.

- **AC-18.** Another evaluator can reproduce the results using the same held-out dataset, version, frame labels, and scoring policy. Outputs include per-behavior and overall coverage and show how unusable intervals were handled. The driver-facing view exposes approved aggregates without evaluation inputs or an evaluation runner.

### 5.6 Reports and assistant integration

**FR-19. Author reports through MCP and review them in RAFIQ.** Only an authorized MCP agent can start and author a session or personal-trend report. It uses approved report inputs and cites the supplied evidence for each numerical finding. RAFIQ validates the submission and renders the report from checked figures, sources, methods, and limitations. Include the approved aggregate benchmark summary in general reports. The driver reviews the finished report and exports it as PDF or Word in RAFIQ. The driver can ask the agent to create a new version.

- **AC-19.** Verify that an authorized agent can start and submit a report through MCP and that RAFIQ rejects unsupported findings or invalid evidence references. The RAFIQ screen offers review and export actions. Verify that the browser and in-app chat cannot start or author a report. PDF and Word use the same validated figures as the review screen and include the approved benchmark summary where applicable. Verify authorization and revocation for hosted reports and links. See §8.6 for downloaded copies.

**FR-20. Retrieve authorized data and author reports through MCP.** The driver connects a compatible agent to one RAFIQ MCP endpoint, signs in to RAFIQ, and can independently approve and revoke read and report-authoring permissions. Read access covers approved driver-owned session summaries, analytics, and event metadata. Report authoring lets the agent start a job, retrieve approved inputs for that job, and submit a draft. The driver reviews and downloads the result in RAFIQ. MCP cannot enable recording, change settings or live thresholds, control a session, create share links, or invoke Emergency Mode.

- **AC-20.** Use a client-neutral reference client on the deployed endpoint to verify self-service connection, independent permissions, token refresh, allowed reads, report authoring, and owner-only review in RAFIQ. Verify immediate denial after grant revocation, data expiry or deletion, including during report authoring. Reject cross-account access, clip contents, settings changes, and emergency actions. See §8.8 for the field allowlist and release gate.

**FR-21. Ask about driving data in RAFIQ.** From Settings, a signed-in driver can connect an eligible ChatGPT or Claude subscription when that provider is available. The driver can ask questions and follow-ups about their own sessions and driving trends in a temporary chat. The first-use consent for each provider explains that RAFIQ sends the driver’s messages and relevant fields from the §8.8 allowlist. Explain the provider’s data handling before use. The driver can revoke permission to share driving data and disconnect the provider in Settings. Report generation follows FR-19.

- **AC-21.** Before enabling a provider, verify eligible subscriptions, first-use consent, revocation and disconnection, isolation between drivers, filtering of outbound driving data, and disposal of the RAFIQ conversation when it closes. Show a clear status when the provider or subscription connection is unavailable or the driver’s allowance is exhausted. Verify public signup is independent of provider availability. See §8.9 for provider qualification.

### 5.7 Admin dashboard

**FR-22. Monitor RAFIQ and support driver accounts.** The internal dashboard opens on Service Health and has separate views for Adoption and Account Support. Each view requires its assigned permission. Use only aggregate operational and adoption figures and the limited account details listed below. Staff and Owners have no admin access to individual driving sessions, observations, clips, reports, emergency contacts, or precise locations. The dashboard cannot impersonate a driver or send or retry Emergency Mode alerts.

| View | What it shows |
|---|---|
| Service Health | Status cards for key services, trend charts for uptime, API error rate, and API latency, and tables for session sync and report queues, storage quotas, backup status and lag, deletion and purge progress, and emergency delivery. Default to the last 24 hours, with 1-hour, 7-day, and 30-day ranges. Show when each signal last updated. Use Healthy, Degraded, Unavailable, and Unknown statuses based on approved thresholds and freshness. Show Pending, Accepted, Delivered, Failed, and Unconfirmed counts separately for email and WhatsApp. |
| Release Readiness | Within Service Health, show each release gate as Passed, Failed, or Pending with its last verification date and an approved evidence reference when available. Release approval and activation follow the existing release process. |
| Adoption | Show five cards for signups, verified accounts, drivers completing a first session, active drivers, and completed sessions. Show a signup → email verification → first completed session funnel and trend lines for active drivers and completed sessions. Follow accounts that signed up in the selected period and count funnel milestones reached within seven days of signup. Label signup cohorts that are still in progress. An active driver is a distinct driver who completed at least one session in the selected period. |
| Account Support | Search by exact registered email or account ID. Show only the ID, registered email, verification status, account status, and signup date. Send verification or recovery messages only to the registered email through a rate-limited flow that keeps access codes and tokens private. Authorized staff can suspend or reinstate an account with a required reason. Account deletion stays with the existing driver workflow. |

**Adoption privacy and history.** Default to the last 30 days, with 7-day, all-history, and custom ranges. Use whole-product totals, one displayed time zone per view, and daily trends through 30 days or weekly trends for longer ranges. Suppress results that would reveal activity for fewer than 10 distinct drivers, including through comparisons of overlapping dates, related totals, or funnel steps. Keep only anonymous historical counts in fixed time buckets after account or session records expire or are deleted. Show exact unique-driver counts for a selected range only when complete inputs are available and the result passes the disclosure rules. Label suppressed or unavailable values.

**Admin access and audit.** Require invitations and multi-factor sign-in. Provision the first Owner during deployment. An existing Owner can invite staff, grant or revoke permissions, and appoint another MFA-protected Owner. Protect the last active Owner and enforce removal of access immediately. Assign Staff permissions separately for viewing service and adoption metrics, looking up accounts and sending verification or recovery messages, and suspension or reinstatement. Suspension and reinstatement require both account support and suspension permissions. Require recent re-verification to change access or suspend or reinstate a driver. The Owner can filter the 90-day audit history by staff member, action, outcome, and date. Record the actor, target where applicable, timestamp, and outcome for lookups and actions. Prevent editing or early deletion of audit records. Require approved reasons for suspensions and reinstatements and keep personal data out of reason fields.

**Suspension and reinstatement.** Suspension immediately removes hosted access and invalidates existing authorization. Show restricted account status and the published RAFIQ support contact. Block new sessions and hosted synchronization. A configured session already running offline keeps its local safety warnings until it ends within its existing limits. On reconnect, keep uploads locked. Retained driver data still expires on schedule. Reinstatement requires fresh sign-in and fresh driver consent to reconnect an MCP client. Release eligible queued records for sync only after fresh sign-in and subject to normal deadlines.

- **AC-22.** Verify all views, the health and adoption ranges, service and release statuses, channel-specific delivery counts, and source freshness. Verify funnel, active driver, and session counts with known fixtures, including in-progress cohorts, repeated sessions, small counts, overlapping ranges, and historical data deletion. Exercise invitations, MFA, individual permissions, immediate revocation, last-Owner protection, exact lookup, rate-limited account messages, suspension during online and offline use, reinstatement, and audit retention. Verify account fields and aggregate results are the only driver information exposed and that the admin surface cannot access individual driving data or activate releases.

## 6. Non-functional requirements

| ID | Requirement and verification |
|---|---|
| NFR-01 | **Supported setup.** Qualify the reference browser and operating system on representative laptops with built-in cameras. Document and verify the browser range, minimum hardware, camera constraints, and supported session duration. |
| NFR-02 | **Responsiveness and capacity.** Verify session and offline limits on the minimum supported device. Test dashboard response time, concurrent use, storage, and uploads against §8.4. Record the workload and the percentile or maximum used. |
| NFR-03 | **Availability and recovery.** Measure hosted availability, recovery time, and tolerated data loss. Verify interruption, reconnect, storage exhaustion, retry, and account separation. |
| NFR-04 | **Accessibility.** Verify keyboard and screen-reader access to setup and review, non-color warning cues, and configurable audio and visual presentation with a workflow checklist. Visual customization retains an accessible warning signal. |
| NFR-05 | **Private data handling.** Protect authorized hosted and queued private data in storage and during transfer. Verify isolation, expiry, deletion, revocation, and retry behavior where applicable across UI, storage retrieval, exports, in-app chat, MCP, and the admin dashboard. |
| NFR-06 | **Operating constraints.** Test the readiness, manual pause/resume, and warning behavior in controlled conditions and the approved supervised setup. Start and driver acknowledgment occur while stationary. The supervised-use procedure specifies how required interactions during motion are handled. |

## 7. Success and release evidence

**SM-01. Unassisted public user journey.** Measure how many test participants self-register, verify their email, pass camera checks, start, finish, and reach the summary unassisted. Use the test protocol and target in §8.4. Supports UJ-1 and FR-01, FR-04, and FR-11.

| Measure | Evidence required for approval |
|---|---|
| SM-02. Recall and precision | Measure each behavior against held-out frame labels under the approved matching rules. Report the number of labeled examples per behavior and the relevant test conditions. |
| SM-03. False warnings | Divide false warnings by monitored hours using an approved exposure rule. Document how combined warnings and uncertain intervals are counted. |
| SM-04. Warning delay | Measure from the approved reference qualification point to the visible warning. Record the distribution and pre-approved pass statistic. |
| SM-05. Observation coverage | Measure usable observation time relative to elapsed monitoring time. Report results overall and per behavior, by supported setup and evaluated condition. |

Excessive nuisance warnings, missed sustained high-risk conditions, low observation coverage, unexpected recording, unauthorized access, misleading analytics, and misleading emergency status can block activation even when the user journey passes. The release evidence must include normal, unsafe, overlapping, and recurring behavior. It must also cover poor light and occlusion, camera disconnection, permission denial, network and storage failures and recovery, unauthorized access, deletion and revocation, and emergency cancellation, channel fallback, expiry, and failed delivery in the eligible environment.

Use baselines to check the planning targets in §8. Ali Sameh approves and freezes the evaluation protocol, thresholds, and tested setup before collecting or scoring the corresponding sign-off evidence. Apply the approved rules to the held-out benchmark and release test results. Record a pass or an unresolved blocker for each release requirement and measure. For analysis, retain a versioned fixture and expected results that cover repeated calculations, simulation, experiment comparisons, and matching report exports.

Live contact alerts require approval of the drowsiness policy, timing, supervised-use procedure, and channel delivery tests. Public account access and each channel’s activation have separate gates. PRD approval records product intent and planned release evidence.

## 8. Planning decisions and release gates

The defaults below close the remaining product decisions under Ali Sameh’s instruction to make reasonable assumptions. Dates, target values, and selected integrations are planning baselines. Design and engineering verify them before activation. If a baseline fails or institutional policy requires a change, record the revision before sign-off and use fresh evaluation evidence for any affected threshold.

### 8.1 Public signup, milestone, and rollout

- Open free, English-language public registration to adults who verify their email and accept the controlled-use conditions. Apply the same signup path regardless of university affiliation or country of residence.
- For the campus demonstration on **15 December 2026**, show a stationary session, warning and camera-pause behavior, and the session summary. Include benchmark results and release-gate status.
- Public readiness requires a passing unassisted user journey, held-out benchmark, applicable acceptance tests, accessibility and lifecycle checks, public capacity tests, client-neutral MCP qualification, and a passing admin dashboard acceptance check (AC-22). Supervised vehicle tests follow §8.2.

### 8.2 Device and supervisor qualification

- Qualify Chrome Stable on Windows 11 x64. Test the then-current and immediately preceding Chrome major versions at their latest available patches and record the exact versions. The provisional hardware floor is four logical CPU cores, 8 GB RAM, and a built-in front-facing camera capable of 720p at 30 fps. Allow CPU-only operation. Verify the session and latency targets at the hardware floor with a usable view of the face and upper body.
- While stationary, the driver explicitly authorizes the designated supervisor for the session. The supervisor can acknowledge warnings, cancel pending contact alerts, and pause monitoring. Authorization ends on driver revocation or at session end. Starting, resuming, ending, account access, settings, and record review remain driver actions performed while stationary.
- If authorized supervision is unavailable, omit workflows that require interaction during motion. Demonstrate unsafe-behavior fixtures while stationary or in a simulator. Motion testing follows the institution-approved procedure, uses passive monitoring for the driver, and reserves setup and review for stationary use. [NHTSA distracted driving guidance](https://www.nhtsa.gov/book/countermeasures-that-work/distracted-driving)

### 8.3 Benchmark and behavior policy

- Record the baseline labels and proposed additions in the versioned **RAFIQ Controlled Annotation Guide**. Mark each sampled frame for each evaluated behavior as present, absent, or unusable. Mark a behavior unusable if its cue cannot be assessed. Mark all evaluated behaviors unusable when the feed is unavailable. Resolve ambiguous cases with a second reviewer before freezing labels.
- Use a versioned, consented stationary or simulator dataset collected for RAFIQ. Split by driver before tuning, targeting 60% development, 20% calibration, and 20% held-out. Require at least five held-out drivers, 20 independently staged positive episodes per behavior, and five held-out monitored hours. Keep all samples from any one driver in one split. Routine private sessions stay out of the benchmark.
- Match predictions to frame labels at the same sampled timestamps at 10 Hz. Exclude unusable class frames from that class’s confusion counts and report their share. Calculate coverage from elapsed session time excluding deliberate user pauses and including observation-loss pauses. Overall coverage reflects usable feed time. Per-behavior coverage reflects observable cues for that class. Count a combined warning once as false when none of its named classes matches a qualifying labeled episode. Measure visible warning delay from the point the labeled cue meets its configured dwell.
- Stage the FR-05 examples while stationary or in a simulator, including talking versus yawning, eating versus drinking, overlapping behaviors, occluded eyes or hands, and a lost camera feed. Verify that loss of a required cue produces unavailable observation for the affected class and that whole-feed loss pauses monitoring. Keep any class that fails its acceptance targets gated. A release with fewer than the five MVP behaviors requires Ali Sameh’s approval. Training or fine-tuning is a separate decision.
- The table specifies **controlled-test starting values**. The stronger-warning threshold is total persistence from observation onset. Cooldown is the minimum interval before a repeat warning after acknowledgment. A gap within tolerance keeps the dwell progress without adding time. A longer gap clears the dwell progress, and the incident closes after sustained observed recovery. Camera loss follows FR-06. Select the lowest calibrated score threshold per class that meets both precision and recall targets on calibration data. If no threshold passes both, revise before held-out scoring.

| Behavior | Initial dwell | Stronger warning at | Short gap | Sustained recovery | Cooldown | Precision target | Recall target |
|---|---:|---:|---:|---:|---:|---:|---:|
| Drowsiness | 2 s | 5 s | 0.25 s | 2 s | 10 s | 90% | 90% |
| Distraction | 3 s | 6 s | 0.5 s | 2 s | 15 s | 85% | 85% |
| Phone use | 2 s | 5 s | 0.5 s | 2 s | 15 s | 85% | 80% |
| Eating | 2 s | 6 s | 0.5 s | 2 s | 20 s | 85% | 80% |
| Drinking | 2 s | 6 s | 0.5 s | 2 s | 20 s | 85% | 80% |

- Target at most two false warnings per monitored hour, at most 750 ms from qualification to visible warning at the 95th percentile, and at least 90% overall coverage in supported normal conditions. Report degradation fixtures separately. Before adding reaching or another class, approve its label, warning timing, precision and recall targets, and held-out results. Include overlap and ordinary driving movements such as steering and adjusting controls. Validate new drowsiness cues against existing drowsiness targets. Freeze policy values and metric rules before held-out scoring. Supervised motion and live contact alerts require separate acceptance evidence.

### 8.4 User journey, capacity, and recovery

- Target **10 of 12** drivers completing the unassisted workflow in one scheduled session each within seven days. Recruit consenting test participants and use the standard public signup flow. Count camera, signup, sync, and workflow failures as failed attempts. Exclude duplicate registrations, replace withdrawals before a first attempt, and approve the rule for withdrawals after an attempt before testing.
- Size for one 30-minute session on the minimum device, including up to 30 continuous offline minutes after readiness checks. Cap the local clip queue at 100 MB or 20 clips, whichever comes first. At the cap, local monitoring and warnings continue and RAFIQ marks unavailable new clips. Verify one representative session and reconnect without missing or duplicate eligible queued records.

| Measure | Initial test target | Public release target |
|---|---:|---:|
| Dashboard response at the 95th percentile under baseline load | 3 s | 2 s |
| Concurrent signed-in users in baseline load | 20 | 100 |
| Hosted clip storage per driver | 250 MB | 500 MB |
| Concurrent clip uploads in baseline load | 5 | 20 |
| Maximum individual clip upload | 20 MB | 20 MB |
| Successful supported uploads within 60 s at 5 Mbps uplink | 95% | 95% |

- Target 99% hosted availability over the seven-day test window, recovery within 15 minutes in controlled service-recovery drills, and a recovery point of at most five minutes for hosted records in a disaster-recovery drill. Normal disconnect, reconnect, and retry tests require zero missing or duplicated eligible queued records within the supported limits.

### 8.5 Emergency alerts by email and WhatsApp

- Start controlled validation with 10 seconds of continuous qualifying drowsiness and a separate 15-second cancellation window. A camera pause clears both timers. Manual resume requires fresh qualification and the full window. Test cancellation, camera loss, recovery, and expiry while stationary or in a simulator. Obtain Ali Sameh’s approval before enabling each live channel in eligible supervised use.
- Allow up to two driver-registered contacts in driver-selected order. Attempt each eligible channel for the current contact at most once. Apply a 120-second deadline from the start of the cancellation window. Skip contacts with no eligible channel. Advance only after every eligible channel for the current contact has been attempted and reports a terminal failure. Pending or ambiguous outcomes keep progression on hold. Delivery on either channel stops progression. Duplicate events cause no duplicate sends. A later bounce can update the channel status while the closed sequence stays closed.
- Use a fixed message the driver can preview. “RAFIQ observed sustained signs of drowsiness for [driver name] at [time]. Please call [driver name] to check on them.” Append the available location as a map location or map link with separate driver permission. Otherwise show “Location unavailable.” The recipient reads the alert and location directly. Expire precise coordinates in RAFIQ 24 hours after capture. Delivered copies remain with the recipient.
- Qualify email via **Resend Free** with a verified sending domain. Qualify WhatsApp via the official Business Platform only if the recipient can opt in outside RAFIQ, the alert format qualifies under provider rules, and delivery and zero project cost can be verified. Respect opt-outs. A driver can save a contact before WhatsApp qualifies. Enable email independently. [Resend events](https://resend.com/docs/webhooks/event-types) · [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/) · [WhatsApp pricing](https://whatsappbusiness.com/products/platform-pricing/)

### 8.6 Clip and report lifecycle

- Default to three seconds of context before and after an incident. Let drivers adjust each window between zero and five seconds. Cap clips at 30 seconds and 20 MB. Keep the first bounded segment of longer incidents and show that the clip was truncated. Discard temporary context outside a consented clip.
- Expire queued clips 24 hours after capture, hosted clips seven days after capture, and session and incident metadata 90 days after session end. Expired queue items cannot upload. Revoking consent discards unsent clips. Apply the institution’s retention policy to any separate university-run study or demonstration that retains recordings.
- Block access immediately at deletion or expiry. Purge retained copies, including backups, within 30 days. A single clip deletion preserves independent session metadata and revokes clip references. Withdraw hosted reports that depend on deleted or expired records and allow regeneration from eligible data. Hosted reports expire 30 days after creation or when a required source expires, whichever happens first. Owner-authorized download links expire after five minutes. Explain at export that downloaded files remain under the driver’s control.

### 8.7 Statistical methods and data access

- Use a two-sided paired permutation test of mean within-participant differences in incident rate per monitored hour across two controlled conditions. Report its 95% paired bootstrap interval with 10,000 draws and seed 20261120. Use a two-sided Fisher’s exact test for the proportion of participants with at least one incident across two independent groups and report 95% Wilson intervals for the proportions. Use a 0.05 significance level and label results exploratory. Require at least 10 complete pairs for paired analysis or 10 participants per arm for independent analysis. Withhold inference when input or design prerequisites fail and explain why alongside eligible descriptive results. Fixture checks require exact counts and absolute numerical error of at most 0.000001 for unrounded results, using matching versions and seeds.
- Replay only the driver’s own eligible retained session measurement series, with compatible timestamps, observation flags, policy version, and sufficient values for the requested threshold. Use reference labels when reporting accuracy. Exclude clips and precise location. Save simulation results separately from source sessions and live policy.
- Start Experiment Studio with versioned synthetic paired and independent-group fixtures. Additional predefined study datasets require institution-approved use. Cross-participant views and exports are aggregate only, with at least 10 distinct participants in every visible group. Suppress complementary totals if they would reveal a hidden group. Include the method and dataset version. Keep participant rows, private driving histories, and clips out of outputs.

### 8.8 MCP qualification and data boundaries

- Publish one Streamable HTTP endpoint and generic setup instructions. Compatible clients use OAuth with Client ID Metadata Documents (CIMD), PKCE, and driver consent. OpenCode and Antigravity document this connection method and can serve as setup examples. Public launch requires the deployed endpoint to pass AC-20 with a client-neutral reference client. [OpenCode MCP documentation](https://opencode.ai/docs/mcp-servers/#oauth) · [Antigravity MCP documentation](https://antigravity.google/docs/mcp#oauth)
- The driving-data allowlist for MCP reads and in-app chat covers the driver’s session identifiers, timestamps, duration, coverage, behavior and incident counts, and validated aggregate metrics with units and methods. Event metadata includes event identifier, class, relative start time, duration, and severity. Exclude raw media, clips and links, contacts, precise location, unrestricted measurement series, report contents, and other accounts’ data.
- A scoped report job returns an opaque identifier and status. The authoring grant allows the agent to retrieve that job’s approved template and evidence fields and submit a draft. Apply the same driving-data limits to job inputs. Finished reports stay in RAFIQ for driver review and PDF or Word export. Verify authorization at each job operation and release, revocation during authoring, field filtering, and cross-account denial. Apply the lifecycle in §8.6.

### 8.9 Optional chat provider qualification

- Enable a provider only after verifying its official subscription-backed connection for hosted RAFIQ, eligible test accounts, privacy controls, and zero project cost. Qualify and enable providers independently. ChatGPT requires RAFIQ to participate in OpenAI’s program. Claude remains a future option pending an official consumer subscription route. [OpenAI website integration](https://developers.openai.com/siwc/website) · [Anthropic linked billing](https://support.claude.com/en/articles/18467148-use-your-claude-platform-account-in-a-third-party-app)

## 9. Illustrative example

- **I-1.** Nour is an illustrative driver for the public signup and first-session journey.
