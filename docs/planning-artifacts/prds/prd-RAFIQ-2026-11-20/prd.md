---
title: RAFIQ Product Requirements Document
status: final
created: 2026-11-20
updated: 2026-11-20
approved_by: Ali Sameh
---

# RAFIQ Product Requirements Document

## 1. Product intent

RAFIQ is a desktop-browser SaaS application for individual drivers in controlled sessions and supervised vehicle testing. It uses the device’s built-in camera to identify visible cues associated with drowsiness, distraction, phone use, eating, and drinking. The driver receives timely warnings and can review what RAFIQ observed after the session.

RAFIQ’s differentiator is reproducible analysis of the observations behind those warnings. A driver can review a timeline, compare sessions, test how different thresholds would change recorded results, and review a report backed by verifiable measures. Drivers already using monitoring tools are the initial audience. The design and engineering team will use this PRD to define the experience, requirements, and release evidence.

The institution or project funds a free first release. A named cohort will provide pilot evidence, and public self-service signup is the launch goal. The order and availability of pilot and public capabilities remain open under OQ-1. The academic submission or demonstration drives the schedule. Ali Sameh approves the PRD and the release. The [original feature brief](../../../../RAFIQ.md) supplies product context. Interview decisions set the scope in this PRD.

## 2. MVP boundary

| Source features | Disposition |
|---|---|
| 1–10 and 12 | MVP. On-device monitoring, five behavior classes, concurrent detections, warnings with explanations, escalation within local warnings, and pause for unreliable observation. |
| 11 | MVP supervised-pilot capability. Live email enablement requires validated eligibility rules and evidence. Public availability requires a later decision based on pilot results. |
| 13–16 | Deferred. Risk score, personal calibration, behavior fingerprint, and behavior chains. |
| 17–18 and 20–24 | MVP. Session observations, descriptive and approved inferential statistics, personal dashboard, timeline, what-if simulation, and Experiment Studio. |
| 19 | Required release evidence. Driver-facing presentation or evaluation remains undecided. |
| 25–31 and 33 | MVP. Private driver accounts, profiles and settings, sessions, consented clips, private replay, and privacy controls. |
| 32 and 34 | MVP. AI-assisted reports with review and PDF/Word export, and MCP for authorized reads and report requests. |

Billing, organization workspaces, fleet dashboards, cross-driver browsing, routine unsupervised use, mobile monitoring, dedicated vehicle hardware, vehicle control, medical diagnosis, certified unconsciousness detection, accident prediction guarantees, public emergency dispatch, guaranteed GPS, manual detection correction, standalone reliability and camera stress-test modes, separate demo and research modes, and MCP sharing or control actions are outside MVP scope.

## 3. Users and core journey

**Driver.** The sole signed-in product role. The driver wants to know whether monitoring is active, understand why RAFIQ issued a warning, and review their own observations and clips. Their account, dashboard, and recordings are private.

**Supervisor.** A person present during supervised vehicle testing who handles any required application interaction during motion. The driver starts sessions and acknowledges warnings while stationary. The supervisor has no separate RAFIQ sign-in or access grant. The approved operating procedure for any supervisor interaction with a signed-in session is part of OQ-2.

**Emergency contact.** A verified email recipient registered by the driver. The contact receives eligible messages through the supervised pilot and has no dashboard or recording access.

### UJ-1. First controlled session

Nour, an illustrative first-time driver from the pilot cohort, signs in to RAFIQ on a desktop browser, checks the built-in camera, reviews recording consent, and starts a controlled monitoring session. The app shows that monitoring is active. If a behavior qualifies for a warning, Nour can see the behavior, the observed cue, and its duration. If observation is unreliable, the session pauses and Nour can resume manually after restoring a usable view. Nour ends the session and opens the summary to see recorded incidents and observation coverage. See SM-01 for the pilot check.

## 4. Product terms

| Term | Meaning |
|---|---|
| Session | A driver-started monitoring run with active, paused, and ended states. |
| Behavior detection | A model observation associated with one of the five supported behavior classes. A detection has a time span, confidence, and supporting observations when available. |
| Incident | A session record that groups overlapping behavior detections while retaining individual behavior labels and times. |
| Warning | Visual feedback, with optional audio, for qualifying behavior detections. Acknowledging a warning does not erase the underlying observation. |
| Observation coverage | Usable observation time divided by elapsed monitoring time. The release measurement plan defines exact pause and timing boundaries. |
| Incident clip | Consented, video-only recording linked to an incident, with bounded configurable context around the event. |
| Emergency Mode | The controlled escalation state that can initiate an ordered email sequence to verified contacts for eligible supervised pilot sessions. |
| Successful send | Confirmation that the email sending service accepted the message. Recipient delivery requires separate evidence. |
| Benchmark | A repeatable run against a held-out set of labeled frames or time intervals with defined test conditions and scoring rules. |

## 5. Functional requirements

### 5.1 Accounts, privacy, and readiness

**FR-01. Account access and recovery.** Drivers can register, verify their accounts, sign in, and recover access. Self-service public registration follows the approved rollout in OQ-1.

- **AC-01.** A verified driver can sign in and recover access. An unverified or unauthenticated visitor cannot retrieve account history, statistics, recordings, or settings.

**FR-02. Driver data isolation.** The driver can access only their own profile, sessions, data, reports, settings, and recordings. Access restrictions apply throughout the browser and all connected product surfaces, including MCP and file retrieval.

- **AC-02.** A second driver cannot access another driver’s resources through direct links, changed identifiers, or assistant requests. Expired or revoked authorizations deny access even to resources previously available under that authorization.

**FR-03. Profile and settings.** The driver can view monitoring history and manage verified emergency contacts, the supported camera, optional warning audio, recording categories and context, and privacy settings. The product supplies the live behavior, severity, and timing rules.

- **AC-03.** The driver can save supported preferences and see them applied in a subsequent session. An unverified email address is ineligible for live escalation. Simulation and settings changes cannot alter live thresholds.

**FR-04. Session readiness and lifecycle.** A signed-in driver starts a session after camera readiness and consent checks. The app shows the current session state, supports pausing and ending, and requires manual resume after an interruption. The driver can review an ended session. A camera preview is available during stationary setup.

- **AC-04.** A supported camera and completed readiness checks enable start whether the driver grants or declines recording. Camera denial provides a recovery path and leaves monitoring inactive. After disruption, a usable camera and manual action are required to resume. Ending the session closes the monitoring run and makes its summary available when the required data syncs. Verify the supervised procedure for warnings and interruptions, including when authorized interaction during motion is unavailable.

### 5.2 On-device monitoring and warnings

**FR-05. Observe and show driver state.** Once set up, RAFIQ processes live camera input on the device. In a controlled stationary session, the driver can see a live camera feed and the current observation state. The observation state shows the supported behaviors currently qualifying, a usable observation without a qualifying behavior, or unavailable observation. The supervised-use procedure governs presentation during motion. Fixed release rules use the following observable boundaries.

| Behavior | Positive label |
|---|---|
| Drowsiness | Visible cues such as sustained eye closure or qualifying blink patterns. |
| Distraction | Sustained off-task gaze or head direction. |
| Phone use | Observable active use. Mere phone presence is outside this label. |
| Eating | Observable eating behavior. |
| Drinking | Observable drinking behavior. |

- **AC-05.** A stationary session shows the live feed and distinguishes concurrent behaviors, no qualifying behavior, and unavailable observation. Held-out positive, negative, and overlapping examples produce measurable results for each class. The approved labeling and test protocol covers ambiguous cases, including a visible unused phone and inadequate observation, and supplies matching rules under OQ-3.

**FR-06. Handle unreliable observation.** RAFIQ shows when low confidence, poor light, obstruction, or camera loss makes monitoring unreliable and pauses the session. It identifies affected intervals in the session record.

- **AC-06.** With an unusable feed, monitoring displays a plain-language pause state that takes precedence over any stale warning. The affected interval produces no new warning or escalation. Restoring the feed permits manual resume. The session summary reflects the affected interval in observation coverage.

**FR-07. Warn and explain.** RAFIQ issues a combined visual warning for overlapping qualifying behaviors and plays audio if enabled. The warning states the behaviors, the observable cues, and how long they were observed. Fixed policy governs severity, escalation, short detection gaps, sustained recovery, and repeated warnings. The product preserves the original detection when a result is disputed.

- **AC-07.** Two overlapping qualifying behaviors produce one warning naming both. A persistent behavior crossing the approved severity threshold produces a visibly stronger warning. Policy fixtures verify recurrence after acknowledgment, cooldown, short gaps, and sustained recovery. A short approved gap stays within one incident. Sustained recovery ends that incident. Audio can be switched off while visual warning remains available.

**FR-08. Continue a configured session offline.** After setup, on-device monitoring and local warnings continue through network loss. The product shows which session records and consented clips are waiting to sync, resumes synchronization when service returns, and keeps records associated with the same driver and session.

- **AC-08.** Losing connectivity during a usable session preserves local monitoring and warnings. After reconnect, each retained record appears once in history under its original account. The prior account’s pending data is inaccessible after sign-out and from any other account using the same browser. The driver can distinguish pending, available, and unavailable records and clips. OQ-4 and OQ-6 define capacity and retention of queued data.

### 5.3 Emergency Mode for the supervised pilot

**FR-09. Control entry and cancellation.** A supervised pilot session may activate Emergency Mode only when a condition on the validated high-risk list persists for the approved period. RAFIQ shows an opportunity to cancel before an email attempt. Cancellation or observed recovery stops unsent attempts. A camera pause suspends eligibility to send until the session resumes with usable observation and the condition qualifies again. The live email path remains disabled until the list, timing, and acceptance evidence are approved.

- **AC-09.** Ordinary qualifying warnings or absence of an approved high-risk condition cannot initiate a live email. An eligible test case reaches the cancellation window. Cancellation or recovery before send prevents transmission. Verify camera pause during both the countdown and a pending retry. When observation resumes without a qualifying behavior, the email remains unsent. A fresh qualifying observation follows the approved requalification and cancellation rules.

**FR-10. Attempt verified contact email.** RAFIQ checks session eligibility, cancellation status, and the current contact authorization before each send. It tries verified email contacts in order within the approved time limit and stops at the first successful send. Location is included only if available and permitted. The interface shows pending, sent, or failed. A retry is possible within the original time limit when connectivity and eligibility return.

- **AC-10.** With two verified contacts, a confirmed failure for the first allows the next eligible attempt within the time limit. A successful send stops the sequence. A missing or denied location leaves location out of the message. Verify that ending the session, expiry, or offline cancellation prevents stale sends after reconnect. Contact removal and revoked location permission take effect before any later attempt. Verify ambiguous send, duplicate-attempt, and later bounce scenarios against the approved policy in OQ-5.

### 5.4 History, recordings, and data lifecycle

**FR-11. Preserve session observations.** RAFIQ links detected behavior, timestamps, durations, confidence, relevant measurements, warnings, incidents, observation coverage, and recording references to the driver’s session. Overlapping detections can contribute to one incident. The session summary distinguishes elapsed monitoring time, coverage, and incident count.

- **AC-11.** In a session with overlapping behaviors, each behavior appears with its original details, and the grouped incident is counted once. Paused and unobservable time is distinguishable from observed time without a detection.

**FR-12. Record consented, bounded clips.** The driver can opt in once, choose eligible recording categories, see recording state, and stop capture. The live feed stays on-device. Only a consented matching incident can produce a video-only clip for private hosted storage. Any temporary pre-event context stays on the device and is bounded by the approved policy. A consented offline clip waits privately on the device subject to capacity and retention limits.

- **AC-12.** Declining recording or a nonmatching category yields no saved clip or uploaded live feed. An enabled qualifying incident yields one owner-only video clip or a visible unavailable state. Verify stop and consent revocation during capture and offline upload under OQ-6. Clip output has no audio track and the workflow requires no microphone permission. Reconnecting publishes each eligible clip once.

**FR-13. Review, expire, and delete data.** The driver can search and filter their private clip library by behavior, date, and session, replay clips, and delete a clip, session, or account. RAFIQ sets separate service-wide expiry periods for clips and metadata and communicates those periods. Private session data is ineligible for secondary reuse in model evaluation or training until separately approved.

- **AC-13.** Search and filters return only accessible matching clips. After expiry or deletion, affected records are inaccessible through the UI, direct retrieval, and MCP. Verify expiry and deletion while a record is queued or uploading. A sync retry cannot restore expired or deleted data. Deleting a clip leaves independently retained session metadata. Purge of retained copies and handling of reports follow the approved schedule in OQ-6.

### 5.5 Personal analytics, simulation, and controlled experiments

**FR-14. Review personal statistics and the timeline.** A driver can explore interactive charts for their own sessions and aggregates, compare sessions and behaviors, and use a timeline to examine durations and overlaps. Descriptive views show frequencies, percentages, averages, durations, and distributions when available. Use elapsed monitoring time for reported rates and show observation coverage beside the rate. Label the denominator and units.

- **AC-14.** Known test sessions produce matching counts, rates, and distributions. Selecting sessions or behaviors updates the chart and its values. Selecting an incident identifies its time and constituent detections. The dashboard identifies periods of unavailable observation separately from observed periods without detections.

**FR-15. Show reproducible statistical results.** The product provides confidence intervals and the approved hypothesis tests on eligible data. Results identify the observation unit, inputs, sample size, applicable method, uncertainty, and data or analysis version. If a sample fails the approved prerequisites, the product withholds inference and provides available descriptive results and a reason.

- **AC-15.** Repeating a run with the same eligible data, filters, and method produces the same numerical results within the accepted tolerance. An ineligible sample receives descriptive output without a test conclusion. The method catalog and prerequisites are in OQ-7.

**FR-16. Run what-if simulations.** A driver can vary supported detection thresholds against eligible recorded inputs and compare the resulting recorded or labeled outcomes with the baseline. Show missed detections or false alarms only when reference labels support them. Simulation settings remain independent of live policy.

- **AC-16.** A changed simulation input produces a versioned comparison with the baseline. Repeating the same input produces the same result. No live threshold, session record, or emergency sequence changes during the run. Exact dataset access is part of OQ-7.

**FR-17. Run controlled experiments.** A separate Experiment Studio lets the authorized driver use approved study data and conditions to organize observations and compare results using supported methods. Driver-private access continues to apply. Participant collection, cross-driver access, and the source of eligible study data require an approved protocol under OQ-7.

- **AC-17.** On an approved fixture or dataset, conditions and their observations remain distinguishable and selected analyses rerun from the saved inputs. Drivers cannot open another driver’s experiment or private records. Participant collection, cross-driver inputs, and resulting views and exports are limited to the approved protocol.

**FR-18. Measure detection against held-out labels.** RAFIQ provides repeatable release evidence using labeled frames or time intervals. Report per-behavior precision and recall, accuracy, F1 scores, relevant confusion matrices or equivalent per-class counts for multi-label data, false warnings per monitored hour, warning delay, and coverage. Driver-facing benchmark visibility is open under OQ-8.

- **AC-18.** Another evaluator can repeat the benchmark with the same dataset, version, label rules, and scoring policy and reconcile the reported metrics and cohort or condition slices. The labels used for release evaluation are held out from tuning.

### 5.6 Reports and assistant integration

**FR-19. Review and export AI-assisted reports.** The driver can review a generated report in RAFIQ and export the reviewed report in PDF and Word. The report uses verified application statistics and identifies the source and method for numerical findings. Where the underlying evidence is insufficient, the report preserves the limitation. Benchmark summaries in reports depend on the visibility decision in OQ-8.

- **AC-19.** Exported figures match the validated analysis shown in review. Missing or invalid results are flagged or omitted with a reason. File creation follows the approved data scope and recipient rules even when an assistant starts the request. Verify authorized access and revocation for hosted reports and links. Treat previously downloaded copies according to the lifecycle policy in OQ-6.

**FR-20. Retrieve authorized data and request reports through MCP.** A compatible, authorized assistant can read approved driver-owned data and request report generation for review in RAFIQ. It cannot enable recording, change settings or live thresholds, control a session, create share links, or invoke Emergency Mode.

- **AC-20.** A valid authorization permits a scoped read and report request. Verify authorization before data is released or a report becomes retrievable, including revocation during generation. Requests for another driver’s data, clip contents, settings changes, or emergency actions are rejected. The launch client, outbound fields, and authorized recipients are in OQ-9.

## 6. Non-functional requirements

| ID | Requirement and verification |
|---|---|
| NFR-01 | **Supported setup.** Qualify one named desktop browser and version range with a built-in camera. Document the supported operating system, minimum hardware, camera setup, and session duration. Verify on the minimum configuration. |
| NFR-02 | **Responsiveness and capacity.** Establish approved limits for warning latency, active session duration, dashboard response times, concurrent use, and clip storage and upload capacity. Record the workload and percentile or maximum used for each measurement. |
| NFR-03 | **Availability and recovery.** Establish service availability, recovery time, tolerated data loss, and offline queue bounds. Verify interruption, reconnect, storage exhaustion, retry, and account separation with measured outcomes. |
| NFR-04 | **Accessibility.** Verify keyboard and screen-reader access to setup and review, non-color warning cues, and configurable audio and visual presentation with a workflow checklist. Visual customization retains an accessible warning signal. |
| NFR-05 | **Private data handling.** Protect authorized hosted and queued private data in storage and during transfer. Verify isolation, expiry, deletion, revocation, and retry behavior across UI, storage retrieval, exports, and MCP. |
| NFR-06 | **Operating constraints.** Test the readiness, manual pause/resume, and warning behavior in controlled conditions and the approved supervised setup. Start and driver acknowledgment occur while stationary. The supervised-use procedure specifies how required interactions during motion are handled. |

## 7. Success and release evidence

**SM-01. Unassisted pilot completion.** Divide the number of eligible cohort drivers who sign in, pass camera checks and start, finish, and reach the session summary unassisted by all eligible participants who attempt the workflow under the approved pilot protocol. Set the sample size, target rate, observation window, and exclusion rules before collecting sign-off evidence. Supports UJ-1 and FR-01, FR-04, and FR-11.

| Measure | Evidence required for approval |
|---|---|
| SM-02. Recall and precision | Measure each behavior against held-out labels under the approved matching rules. Report the number of labeled examples per behavior and the relevant test conditions. |
| SM-03. False warnings | Divide false warnings by monitored hours using an approved exposure rule. Document how combined warnings and uncertain intervals are counted. |
| SM-04. Warning delay | Measure from the approved reference qualification point to the visible warning. Record the distribution and pre-approved pass statistic. |
| SM-05. Observation coverage | Measure usable observation time relative to elapsed monitoring time and report results by supported setup and evaluated condition. |

Excessive nuisance warnings, missed sustained high-risk conditions, low observation coverage, unexpected recording, unauthorized access, misleading analytics, and misleading emergency status can block release even when pilot completion passes. The release evidence must include normal, unsafe, overlapping, and recurring behavior. It must also cover poor light and occlusion, camera disconnection, permission denial, network and storage failures and recovery, unauthorized access, deletion and revocation, and emergency cancellation, retry, expiry, and failed delivery in the eligible environment.

Use baselines to propose exact pass thresholds and operating limits. Ali Sameh approves and freezes the evaluation protocol, thresholds, and tested setup before collecting or scoring the corresponding sign-off evidence. Apply the approved rules to the held-out benchmark and pilot results. Record a pass or an unresolved blocker for each release requirement and measure. For analysis, retain a versioned fixture and expected results that cover repeated calculations, simulation, experiment comparisons, and matching report exports.

Live pilot emails require approval of the validated high-risk list, timing, supervised-use procedure, and contact delivery tests. Public live alerts require a separate decision after pilot evidence. PRD approval records product intent and the planned evidence for release acceptance.

## 8. Open decisions and approval points

Ali Sameh owns approval. Design and engineering prepare the proposals and evidence for each checkpoint.

| ID | Decision | Needed by |
|---|---|---|
| OQ-1 | Confirm rollout order, pilot cohort and eligibility, public registration eligibility, launch market, UI languages, and academic due date. Approve the capabilities exposed at each stage, including the public-readiness criteria. | Set cohort eligibility before recruiting. Set rollout order and public scope before opening public signup. |
| OQ-2 | Select the browser, OS, minimum hardware, and camera constraints. Approve the supervised-use procedure, including allowed supervisor actions, driver authorization, and the stationary fallback when interaction during motion is unavailable. | Before testing that setup or enabling supervised motion use. |
| OQ-3 | Approve the five-class annotation rules, exact severity, dwell, gap, recovery and cooldown defaults, coverage rules, held-out dataset, matching policy, and pass thresholds. | Freeze the protocol and thresholds before running the held-out release benchmark. |
| OQ-4 | Use baselines to set thresholds for pilot completion, session duration, offline time and capacity, application response, concurrency, storage and uploads, availability, and recovery. | Freeze each threshold before collecting or scoring its sign-off evidence. |
| OQ-5 | Validate the high-risk list, dwell and cancellation reset after a pause, distinction between warning acknowledgment and emergency cancellation, contact verification and changes, email payload, retry timing, and handling of ambiguous sends, duplicates, and bounces. Approve location precision, access, and retention. | Before enabling live pilot emails. Decide public availability after pilot evidence. |
| OQ-6 | Set clip context, maximum length, and expiry periods for clips and metadata. Define which records become inaccessible immediately, purge deadlines for retained copies and derived records, report and export handling, and the disposition of queued clips on sign-out, expiry, or consent revocation. | Before retaining pilot recordings or accepting lifecycle tests. |
| OQ-7 | Approve the test catalog, prerequisites, numerical tolerances, eligible what-if and study inputs, and experiment protocols. Approve any participant intake, consent, cross-driver data, views, and exports. Private model evaluation and training reuse stays disabled pending approval. | Before analyzing or collecting participant data and before accepting analysis features. |
| OQ-8 | Decide whether drivers see benchmark results or run evaluations and whether an evaluation report is available to them. | Before committing driver-facing Feature 19 or evaluation reports. |
| OQ-9 | Approve initial report types and source data, whether a separate raw personal data export is in scope, and its content if included. Approve the MCP launch client, readable fields, report authorization and handling rules, and integration test path. | Before committing report templates, a raw data export, or the MCP launch scope. |

## 9. Illustrative example and provisional definition

- **I-1.** Nour is an illustrative driver for the confirmed pilot journey. Replace the name and context if the cohort supplies a representative example.
- **I-2.** The provisional definition of “successful send” requires approval under OQ-5.
