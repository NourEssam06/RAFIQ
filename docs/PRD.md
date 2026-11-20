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

The institution or project funds a free, English-language first release. The university cohort pilot comes first, with a planning milestone of 15 December 2026 for a campus demonstration and short evidence summary. Public self-service signup opens to adults in Egypt after release approval. Ali Sameh owns release sign-off. Section 8 specifies the rollout, operating limits, and evidence required before activation. The [original feature brief](../RAFIQ.md) supplies product context. Interview decisions set the scope in this PRD.

## 2. MVP boundary

| Source features | Disposition |
|---|---|
| 1–10 and 12 | MVP. On-device monitoring, five behavior classes, concurrent detections, warnings with explanations, escalation within local warnings, and pause for unreliable observation. |
| 11 | Supervised-pilot capability. Live email enablement requires validated eligibility rules and evidence. Public availability requires pilot evidence and approval of a separate public operating procedure. |
| 13–16 | Deferred. Risk score, personal calibration, behavior fingerprint, and behavior chains. |
| 17–18 and 20–24 | MVP. Session observations, descriptive and approved inferential statistics, personal dashboard, timeline, what-if simulation, and Experiment Studio. |
| 19 | Required release evidence. Publish approved aggregate benchmark results and include a summary in general reports. Running evaluations and exporting dedicated benchmark reports are outside the driver-facing scope. |
| 25–31 and 33 | MVP. Private driver accounts, profiles and settings, sessions, consented clips, private replay, and privacy controls. |
| 32 and 34 | MVP. AI-assisted reports with review and PDF/Word export, and MCP for authorized reads and report requests. |

Billing, organization workspaces, fleet dashboards, cross-driver browsing, routine unsupervised use, mobile monitoring, dedicated vehicle hardware, vehicle control, medical diagnosis, certified unconsciousness detection, accident prediction guarantees, public emergency dispatch, guaranteed GPS, manual detection correction, standalone reliability and camera stress-test modes, separate demo and research modes, raw personal data export, and MCP sharing or control actions are outside MVP scope.

### Rollout sequence

1. **Cohort pilot.** Start with the core session workflow from verified sign-in and camera readiness through monitoring, finishing, and reviewing the session summary. Admit only the approved pilot cohort.
2. **Pre-launch validation.** Add and validate the remaining public capabilities, including analytics, the What-If simulator, Experiment Studio, reports, and MCP. Validate one named MCP client in the later supervised pilot before activating the integration. Live emergency email may be tested in eligible supervised pilot sessions once its separate gates pass.
3. **Public signup.** Open English-language self-service registration to eligible adults in Egypt after the pilot and applicable public release gates pass. The initial public release has live emergency email disabled.

## 3. Users and core journey

**Driver.** The sole signed-in product role. The driver wants to know whether monitoring is active, understand why RAFIQ issued a warning, and review their own observations and clips. Their account, dashboard, and recordings are private.

**Supervisor.** A person present during supervised vehicle testing whom the driver authorizes while stationary to use the warning acknowledgment, emergency countdown cancellation, and pause controls on the driver’s device. The driver starts sessions and uses controls while stationary. The supervisor has no separate RAFIQ sign-in or account access. If authorized interaction is unavailable, workflows that require interaction during motion are unavailable for that test session. See §8.2.

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
| Observation coverage | Usable observation time divided by elapsed monitoring time as defined in §8.3. |
| Incident clip | Consented, video-only recording linked to an incident, with bounded configurable context around the event. |
| Emergency Mode | The controlled escalation state that can initiate an ordered email sequence to verified contacts for eligible supervised pilot sessions. |
| Accepted email | The email provider accepted the message for processing. The interface shows acceptance separately from confirmed delivery. |
| Confirmed delivery | Positive delivery evidence from the email provider. This is the stop condition for the contact sequence where supported. It does not indicate that the recipient read the message. |
| Benchmark | A repeatable run against a held-out, controlled RAFIQ dataset. Labeled frames are the primary matching unit for per-behavior precision and recall. |

## 5. Functional requirements

### 5.1 Accounts, privacy, and readiness

**FR-01. Account access and recovery.** Drivers can register, verify their accounts, sign in, and recover access. Self-service public registration follows the rollout in §8.1.

- **AC-01.** A verified driver can sign in and recover access. Pilot enrollment is limited to eligible cohort members. Public registration remains unavailable until the public rollout is approved. An unverified or unauthenticated visitor cannot retrieve account history, statistics, recordings, or settings.

**FR-02. Driver data isolation.** The driver can access only their own profile, sessions, data, reports, settings, and recordings. Access restrictions apply throughout the browser and all connected product surfaces, including MCP and file retrieval.

- **AC-02.** A second driver cannot access another driver’s resources through direct links, changed identifiers, or assistant requests. Expired or revoked authorizations deny access even to resources previously available under that authorization.

**FR-03. Profile and settings.** The driver can view monitoring history and manage verified emergency contacts, the supported camera, optional warning audio, recording categories and context, and privacy settings. The product supplies the live behavior, severity, and timing rules.

- **AC-03.** The driver can save supported preferences and see them applied in a subsequent session. An email address becomes eligible only after its recipient confirms it. A replacement requires fresh confirmation and a removed address is ineligible. Simulation and settings changes cannot alter live thresholds.

**FR-04. Session readiness and lifecycle.** A signed-in driver starts a session after camera readiness and consent checks. The app shows the current session state, supports pausing and ending, and requires manual resume after an interruption. The driver can review an ended session. A camera preview is available during stationary setup.

- **AC-04.** A supported camera and completed readiness checks enable start whether the driver grants or declines recording. Camera denial provides a recovery path and leaves monitoring inactive. After disruption, a usable camera and manual action are required to resume. Ending the session closes the monitoring run and makes its summary available when the required data syncs. During supervised testing, verify that the pre-authorized supervisor can use only the approved warning and interruption controls. Workflows requiring interaction during motion are unavailable when there is no authorized operator.

### 5.2 On-device monitoring and warnings

**FR-05. Observe and show driver state.** Once set up, RAFIQ processes live camera input on the device. In a controlled stationary session, the driver can see a live camera feed and the current observation state. The observation state shows the supported behaviors currently qualifying, a usable observation without a qualifying behavior, or unavailable observation. The supervised-use procedure governs presentation during motion. Fixed release rules use the following observable boundaries.

| Behavior | Positive label |
|---|---|
| Drowsiness | Visible cues such as sustained eye closure or qualifying blink patterns. |
| Distraction | Sustained off-task gaze or head direction. |
| Phone use | Observable active use. Mere phone presence is outside this label. |
| Eating | Observable eating behavior. |
| Drinking | Observable drinking behavior. |

- **AC-05.** A stationary session shows the live feed and distinguishes concurrent behaviors, no qualifying behavior, and unavailable observation. Held-out positive, negative, and overlapping examples produce measurable results for each class. The labeling and test protocol in §8.3 covers ambiguous cases, including a visible unused phone and inadequate observation.

**FR-06. Handle unreliable observation.** RAFIQ shows when low confidence, poor light, obstruction, or camera loss makes monitoring unreliable and pauses the session. It identifies affected intervals in the session record.

- **AC-06.** With an unusable feed, monitoring displays a plain-language pause state that takes precedence over any stale warning. The affected interval produces no new warning or escalation. Restoring the feed permits manual resume. The session summary reflects the affected interval in observation coverage.

**FR-07. Warn and explain.** RAFIQ issues a combined visual warning for overlapping qualifying behaviors and plays audio if enabled. The warning states the behaviors, the observable cues, and how long they were observed. Each behavior has a fixed policy for severity, qualifying duration, escalation, short detection gaps, sustained recovery, and cooldown. Validate these policies on calibration data and freeze them before release scoring. The product preserves the original detection when a result is disputed.

- **AC-07.** Two overlapping qualifying behaviors produce one warning naming both. A persistent behavior crossing the approved severity threshold produces a visibly stronger warning. Policy fixtures verify recurrence after acknowledgment, cooldown, short gaps, and sustained recovery. A short approved gap stays within one incident. Sustained recovery ends that incident. Audio can be switched off while visual warning remains available.

**FR-08. Continue a configured session offline.** After setup, on-device monitoring and local warnings continue through network loss. The product shows which session records and consented clips are waiting to sync, resumes synchronization when service returns, and keeps records associated with the same driver and session.

- **AC-08.** Losing connectivity during a usable session preserves local monitoring and warnings. After reconnect, each retained record appears once in history under its original account. The prior account’s pending data is inaccessible after sign-out and from any other account using the same browser. The driver can distinguish pending, available, and unavailable records and clips. See §8.4 and §8.6 for queue limits and retention.

### 5.3 Emergency Mode for the supervised pilot

**FR-09. Control entry and cancellation.** Sustained drowsiness is the sole candidate for Emergency Mode in the supervised pilot. Use distinct controls and visible statuses for acknowledging a regular warning and canceling an emergency email. Cancellation or observed recovery stops unsent attempts. A camera pause clears the qualifying dwell and countdown. After manual resume, a fresh qualification starts a full cancellation window. Live email enablement requires the approved pilot evidence in §8.5.

- **AC-09.** Ordinary warnings alone cannot initiate a live email. An eligible test case reaches the cancellation window. Acknowledgment leaves the emergency email state unchanged. Cancellation or recovery before send prevents transmission. Verify a camera pause during both countdown and retry. When observation resumes without a fresh qualifying behavior, the email remains unsent. A fresh qualifying observation follows the approved cancellation reset rule.

**FR-10. Attempt verified contact email.** RAFIQ checks eligibility, cancellation, and current contact authorization before each attempt. Contact email contains a minimal driver identifier, event time, and a request to check in. Precise location may be included only when available and separately permitted for precise sharing. The driver and eligible recipient may access the shared location. RAFIQ retains location for a separate, bounded period.

RAFIQ tries verified contacts in order within the approved time limit. Positive delivery evidence stops the sequence. Show Pending, Accepted, Delivered, Failed, and Unconfirmed as distinct states. Hold an ambiguous result without another send. Retry after confirmed failure only when the sequence remains eligible and within the original time limit. The sequence expires as Unconfirmed if evidence is still missing at the deadline. See §8.5.

- **AC-10.** With two verified contacts, a confirmed failure for the first permits the next eligible attempt. An ambiguous result leaves the sequence pending without retry and becomes Unconfirmed at expiry. Provider acceptance displays Accepted. Positive delivery evidence displays Delivered and stops the sequence. Missing or denied precise location leaves location out. Ending the session, expiry, removal of a contact, and offline cancellation prevent stale or ineligible attempts. Revoked precise location permission takes effect before a later attempt. Verify location access, expiry, duplicate handling, and bounce scenarios in §8.5.

### 5.4 History, recordings, and data lifecycle

**FR-11. Preserve session observations.** RAFIQ links detected behavior, timestamps, durations, confidence, relevant measurements, warnings, incidents, observation coverage, and recording references to the driver’s session. Overlapping detections can contribute to one incident. The session summary distinguishes elapsed monitoring time, coverage, and incident count.

- **AC-11.** In a session with overlapping behaviors, each behavior appears with its original details, and the grouped incident is counted once. Paused and unobservable time is distinguishable from observed time without a detection.

**FR-12. Record consented, bounded clips.** The driver can opt in once, choose eligible recording categories, see recording state, and stop capture. The live feed stays on-device. A consented matching incident can produce a video-only clip for private hosted storage. RAFIQ sets defaults and bounds for configurable pre-event and post-event context and a maximum clip length. Temporary pre-event context stays on the device. Unsent clips remain private to the same driver through sign-out, within capacity and retention limits. Revoking recording consent discards unsent clips.

- **AC-12.** Declining recording or a nonmatching category yields no saved clip or uploaded live feed. An eligible incident yields one owner-only video clip within the bounds or a visible unavailable state. Clip output has no audio track and the workflow requires no microphone permission. Test revocation during capture and pending upload. The revoked queue items are discarded and stay unavailable after reconnect. Each remaining eligible clip uploads once.

**FR-13. Review, expire, and delete data.** The driver can search and filter their private clip library by behavior, date, and session, replay clips, and delete a clip, session, or account. RAFIQ communicates separate service-wide clip and metadata expiry periods. Block access to affected records immediately on expiry or deletion and purge retained copies by the approved deadline. Section 8.6 specifies report and export handling and institutional retention verification. Private session data is ineligible for secondary reuse in model evaluation or training until separately approved.

- **AC-13.** Search and filters return only accessible matching clips. Expiry or deletion blocks access to affected records immediately through the UI, direct retrieval, and MCP. Verify expiry and deletion while a record is queued or uploading. A sync retry cannot restore expired or deleted data. Deleting a clip leaves independently retained session metadata. Verify the purge deadline and report and export handling in §8.6.

### 5.5 Personal analytics, simulation, and controlled experiments

**FR-14. Review personal statistics and the timeline.** A driver can explore interactive charts for their own sessions and aggregates, compare sessions and behaviors, and use a timeline to examine durations and overlaps. Descriptive views show frequencies, percentages, averages, durations, and distributions when available. Use elapsed monitoring time for reported rates and show observation coverage beside the rate. Label the denominator and units.

- **AC-14.** Known test sessions produce matching counts, rates, and distributions. Selecting sessions or behaviors updates the chart and its values. Selecting an incident identifies its time and constituent detections. The dashboard identifies periods of unavailable observation separately from observed periods without detections.

**FR-15. Show reproducible statistical results.** The product provides confidence intervals and a small set of approved hypothesis tests for named comparisons and study designs. Design and engineering propose the prerequisites and reproducibility tolerance for each method using fixtures with known results. Results identify the observation unit, inputs, sample size, method, uncertainty, and data or analysis version. If a sample fails the approved prerequisites, the product withholds inference and provides available descriptive results and a reason.

- **AC-15.** Repeating a run with the same eligible data, filters, and method produces the same numerical results within the accepted tolerance. An ineligible sample receives descriptive output without a test conclusion. See §8.7 for the method catalog and prerequisites.

**FR-16. Run what-if simulations.** A driver can vary supported detection thresholds against eligible inputs from their own recorded sessions and compare the results with the baseline. Report accuracy comparisons, missed detections, and false alarms only when reference labels support them. Simulation settings remain independent of live policy.

- **AC-16.** A change to the simulation inputs produces a versioned comparison with the baseline, and identical inputs produce identical results. Tests cover owner isolation and the absence of accuracy claims when reference labels are unavailable. Live thresholds, session records, and emergency sequences stay independent of the simulation. See §8.7 for input eligibility.

**FR-17. Run controlled experiments.** At first release, Experiment Studio uses approved predefined study datasets and test fixtures to organize observations and compare conditions. The studio may expose cross-participant results only as aggregates that meet approved minimum group sizes and export rules. Private driver histories and clips stay private. New participant collection is outside the first release.

- **AC-17.** On an approved fixture or dataset, conditions remain distinguishable and selected analyses rerun from saved inputs. Views and exports suppress groups below the approved minimum and exclude individual cross-participant records. Drivers cannot open another driver’s experiment or private records. The first release does not collect new participants through the studio.

**FR-18. Measure and publish detection performance.** Use an approved controlled RAFIQ dataset held out from tuning. Approve the supplied annotation guide’s mapping to the five behavior labels and freeze frame-level matching rules before scoring per-behavior precision and recall. Mark unusable intervals by behavior and report per-behavior and overall coverage. Report accuracy, F1 scores, relevant confusion matrices or equivalent multi-label per-class counts, false warnings per monitored hour, and warning delay. Publish approved aggregate benchmark results to drivers.

- **AC-18.** Another evaluator can reproduce the results using the same held-out dataset, version, frame labels, and scoring policy. Outputs include per-behavior and overall coverage and show how unusable intervals were handled. The driver-facing view exposes approved aggregates without evaluation inputs or an evaluation runner.

### 5.6 Reports and assistant integration

**FR-19. Review and export AI-assisted reports.** Initial templates cover driver sessions and personal trends using verified personal statistics. The driver can review a generated report in RAFIQ and export the reviewed report in PDF and Word. Reports identify the source and method for numerical findings and preserve limitations in the evidence. Include the approved aggregate benchmark summary in general reports. Dedicated evaluation reports and raw personal data exports are deferred.

- **AC-19.** PDF and Word exports of the session and personal trend templates match the validated figures shown in review, including the approved benchmark summary where applicable. Missing or invalid results are flagged or omitted with a reason. File creation follows the approved data scope and recipient rules even when an assistant starts the request. Verify authorized access and revocation for hosted reports and links. See §8.6 for downloaded copies.

**FR-20. Retrieve authorized data and request reports through MCP.** The driver grants scoped access for approved driver-owned session summaries, analytics, and event metadata, and grants scoped report access for requests. The assistant requests generation and the driver reviews the result in RAFIQ. Qualify one named assistant client in the supervised pilot. MCP cannot enable recording, change settings or live thresholds, control a session, create share links, or invoke Emergency Mode.

- **AC-20.** Run controlled integration checks, then repeat the same end-to-end coverage on Codex CLI before activation. Verify allowed reads and report requests, owner-only review in RAFIQ, authorization when data becomes available, and revocation during generation. Reject cross-account access, clip contents, settings changes, and emergency actions. See §8.8 for the field allowlist.

## 6. Non-functional requirements

| ID | Requirement and verification |
|---|---|
| NFR-01 | **Supported setup.** Participants use their own laptops and built-in cameras. Qualify one browser and operating system combination from the cohort’s actual devices. Document the browser version range, minimum hardware, camera constraints, and supported session duration. Verify on the minimum configuration. |
| NFR-02 | **Responsiveness and capacity.** Size and verify the session and offline limits to cover one observed pilot session on the minimum supported device. Use baseline load and storage tests to set separate pilot and public limits for dashboard response time, concurrent use, storage, and uploads. Record workload and the percentile or maximum used for each measure. |
| NFR-03 | **Availability and recovery.** Use disconnect and recovery tests to set measurable pilot availability, recovery time, and tolerated data-loss targets. Set offline duration and queue capacity with NFR-02. Verify interruption, reconnect, storage exhaustion, retry, and account separation. |
| NFR-04 | **Accessibility.** Verify keyboard and screen-reader access to setup and review, non-color warning cues, and configurable audio and visual presentation with a workflow checklist. Visual customization retains an accessible warning signal. |
| NFR-05 | **Private data handling.** Protect authorized hosted and queued private data in storage and during transfer. Verify isolation, expiry, deletion, revocation, and retry behavior across UI, storage retrieval, exports, and MCP. |
| NFR-06 | **Operating constraints.** Test the readiness, manual pause/resume, and warning behavior in controlled conditions and the approved supervised setup. Start and driver acknowledgment occur while stationary. The supervised-use procedure specifies how required interactions during motion are handled. |

## 7. Success and release evidence

**SM-01. Unassisted pilot completion.** Divide the number of eligible cohort drivers who sign in, pass camera checks and start, finish, and reach the session summary unassisted by all eligible participants who attempt the workflow. Use the institution’s pilot plan and approve the sample size, target rate, observation window, and exclusion rules before measuring completion. Supports UJ-1 and FR-01, FR-04, and FR-11.

| Measure | Evidence required for approval |
|---|---|
| SM-02. Recall and precision | Measure each behavior against held-out frame labels under the approved matching rules. Report the number of labeled examples per behavior and the relevant test conditions. |
| SM-03. False warnings | Divide false warnings by monitored hours using an approved exposure rule. Document how combined warnings and uncertain intervals are counted. |
| SM-04. Warning delay | Measure from the approved reference qualification point to the visible warning. Record the distribution and pre-approved pass statistic. |
| SM-05. Observation coverage | Measure usable observation time relative to elapsed monitoring time. Report results overall and per behavior, by supported setup and evaluated condition. |

Excessive nuisance warnings, missed sustained high-risk conditions, low observation coverage, unexpected recording, unauthorized access, misleading analytics, and misleading emergency status can block release even when pilot completion passes. The release evidence must include normal, unsafe, overlapping, and recurring behavior. It must also cover poor light and occlusion, camera disconnection, permission denial, network and storage failures and recovery, unauthorized access, deletion and revocation, and emergency cancellation, retry, expiry, and failed delivery in the eligible environment.

Use baselines to check the planning targets in §8. Ali Sameh approves and freezes the evaluation protocol, thresholds, and tested setup before collecting or scoring the corresponding sign-off evidence. Apply the approved rules to the held-out benchmark and pilot results. Record a pass or an unresolved blocker for each release requirement and measure. For analysis, retain a versioned fixture and expected results that cover repeated calculations, simulation, experiment comparisons, and matching report exports.

Live pilot emails require approval of the validated drowsiness policy, timing, supervised-use procedure, and contact delivery tests. The initial public release runs with live email disabled. A future public activation requires pilot evidence and a separately approved public operating procedure. PRD approval records product intent and the planned evidence for release acceptance.

## 8. Planning decisions and release gates

The defaults below close the remaining product decisions under Ali Sameh’s instruction to make reasonable assumptions. Dates, target values, and selected integrations are planning baselines. Design and engineering verify them before activation. If a baseline fails or institutional policy requires a change, record the revision before sign-off and use fresh evaluation evidence for any affected threshold.

### 8.1 Cohort, milestone, and rollout

- Recruit one cohort of 12 consenting adults aged 18 or older from the project team’s university. The project supervisor sponsors enrollment under the institution’s pilot plan. Participants use their own qualifying laptops. Only licensed participants may take part in institution-authorized vehicle testing. The recruiting team supplies the campus name and participant list.
- Plan for **15 December 2026**, about three and a half weeks from the follow-up, for a campus demonstration and short evidence packet. Demonstrate a stationary session, warning and camera-pause behavior, and the session summary. Include pilot completion, benchmark results to date, and release-gate status in the packet.
- Open free, English-language public registration to adults aged 18 or older in Egypt who verify their email and accept the controlled-use conditions. Launch with live emergency email disabled.
- Core pilot readiness requires a passing device check, sign-in and session workflow, warnings and camera pause, and consent and privacy checks. Public readiness requires the pilot completion target, held-out benchmark, applicable acceptance tests, accessibility and lifecycle checks, public capacity tests, and named-client MCP qualification. The campus demonstration has its own milestone and evidence packet.

### 8.2 Device and supervisor qualification

- Qualify Chrome Stable on Windows 11 x64. Test the then-current and immediately preceding Chrome major versions at their latest available patches and record the exact versions. The provisional hardware floor is four logical CPU cores, 8 GB RAM, and a built-in front-facing camera capable of 720p at 30 fps. Allow CPU-only operation. Survey the cohort’s laptops, then verify the session and latency targets at the hardware floor with a usable view of the face and upper body.
- While stationary, the driver explicitly authorizes the designated supervisor for the session. The supervisor can acknowledge warnings, cancel pending emergency email, and pause monitoring. Authorization ends on driver revocation or at session end. Starting, resuming, ending, account access, settings, and record review remain driver actions performed while stationary.
- If authorized supervision is unavailable, omit workflows that require interaction during motion. Demonstrate unsafe-behavior fixtures while stationary or in a simulator. Motion testing follows the institution-approved procedure, uses passive monitoring for the driver, and reserves setup and review for stationary use. [NHTSA distracted driving guidance](https://www.nhtsa.gov/book/countermeasures-that-work/distracted-driving)

### 8.3 Benchmark and behavior policy

- Use the supplied annotation guide as the source and record its five-label mapping in **RAFIQ Controlled Annotation Guide v1**, a pilot deliverable. Mark each sampled frame independently for each FR-05 behavior as present, absent, or unusable. For example, mere phone presence is absent for active use if the cue is visible. Mark a behavior unusable when its cue cannot be assessed and mark all five unusable when the feed is unavailable. Resolve ambiguous cases with a second reviewer before freezing labels.
- Use a versioned, consented stationary or simulator dataset collected for RAFIQ. Split by driver before tuning, targeting 60% development, 20% calibration, and 20% held-out. Require at least five held-out drivers, 20 independently staged positive episodes per behavior, and five held-out monitored hours. Keep all samples from any one driver in one split. Routine private sessions stay out of the benchmark.
- Match predictions to frame labels at the same sampled timestamps at 10 Hz. Exclude unusable class frames from that class’s confusion counts and report their share. Calculate coverage from elapsed session time excluding deliberate user pauses and including observation-loss pauses. Overall coverage reflects usable feed time. Per-behavior coverage reflects observable cues for that class. Count a combined warning once as false when none of its named classes matches a qualifying labeled episode. Measure visible warning delay from the point the labeled cue meets its configured dwell.
- The table specifies **controlled-test starting values**. The stronger-warning threshold is total persistence from observation onset. Cooldown is the minimum interval before a repeat warning after acknowledgment. A gap within tolerance keeps the dwell progress without adding time. A longer gap clears the dwell progress, and the incident closes after sustained observed recovery. Camera loss follows FR-06. Select the lowest calibrated score threshold per class that meets both precision and recall targets on calibration data. If no threshold passes both, revise before held-out scoring.

| Behavior | Initial dwell | Stronger warning at | Short gap | Sustained recovery | Cooldown | Precision target | Recall target |
|---|---:|---:|---:|---:|---:|---:|---:|
| Drowsiness | 2 s | 5 s | 0.25 s | 2 s | 10 s | 90% | 90% |
| Distraction | 3 s | 6 s | 0.5 s | 2 s | 15 s | 85% | 85% |
| Phone use | 2 s | 5 s | 0.5 s | 2 s | 15 s | 85% | 80% |
| Eating | 2 s | 6 s | 0.5 s | 2 s | 20 s | 85% | 80% |
| Drinking | 2 s | 6 s | 0.5 s | 2 s | 20 s | 85% | 80% |

- Target at most two false warnings per monitored hour, at most 750 ms from qualification to visible warning at the 95th percentile, and at least 90% overall coverage in supported normal conditions. Report degradation fixtures separately. Freeze all policy values and metric rules before held-out scoring. Supervised motion and live email require separate acceptance evidence.

### 8.4 Pilot outcome and capacity

- Target **10 of 12** drivers completing the unassisted workflow in one scheduled session each within seven days. Confirm the protocol with the university before recruitment. Count camera, signup, sync, and workflow failures as failed attempts. Exclude duplicate registrations and replace withdrawals before a first attempt to reach 12 eligible attempts. Use the institution’s approved protocol for withdrawals after an attempt.
- Size for one 30-minute session on the minimum device, including up to 30 continuous offline minutes after readiness checks. Cap the local clip queue at 100 MB or 20 clips, whichever comes first. At the cap, local monitoring and warnings continue and RAFIQ marks unavailable new clips. Verify one representative session and reconnect without missing or duplicate eligible queued records.

| Measure | Pilot target | Public target |
|---|---:|---:|
| Dashboard response at the 95th percentile under baseline load | 3 s | 2 s |
| Concurrent signed-in users in baseline load | 20 | 100 |
| Hosted clip storage per driver | 250 MB | 500 MB |
| Concurrent clip uploads in baseline load | 5 | 20 |
| Maximum individual clip upload | 20 MB | 20 MB |
| Successful supported uploads within 60 s at 5 Mbps uplink | 95% | 95% |

- Target 99% hosted availability over the seven-day pilot, recovery within 15 minutes in controlled service-recovery drills, and a recovery point of at most five minutes for hosted records in a disaster-recovery drill. Normal disconnect, reconnect, and retry tests require zero missing or duplicated eligible queued records within the supported limits.

### 8.5 Supervised pilot emergency email

- Start controlled validation with drowsiness as the only candidate, 10 seconds of continuous qualifying observation, and a separate 15-second pre-send cancellation window. A camera pause clears both timers. Manual resume requires fresh qualification and the full cancellation window. Validate cancellation, camera loss, recovery, and expiry while stationary or in a simulator. Obtain Ali Sameh’s approval before enabling real email. Vehicle-motion testing uses no staged drowsiness or other unsafe behavior.
- Use up to two verified contacts in driver-selected order, with one application-level attempt per contact and a 120-second deadline from the start of the cancellation window. Qualify **Resend Free** with a verified sending domain. The plan includes up to 100 transactional emails per day and 3,000 per month. Confirm the pilot’s planned sends fit within the available quota. If the quota is exhausted, report Failed and stop the sequence. [Resend pricing](https://resend.com/pricing) · [Verified domains](https://resend.com/docs/dashboard/domains/introduction)
- Use verified Resend events to track each attempt. `email.sent` indicates Accepted. `email.delivered` indicates Delivered when the recipient’s mail server accepts the message. Confirmed terminal failures and bounces follow the failure rule below. A delivery delay alone keeps the attempt pending. [Resend webhook events](https://resend.com/docs/webhooks/event-types)
- Advance to the next eligible contact only after confirmed failure or a terminal bounce before delivery. Repeated events for the same sequence, contact, and provider message cause no duplicate send. A later bounce corrects status but leaves a delivered sequence closed. An unresolved result at expiry becomes Unconfirmed. Live sending requires a configuration that exposes positive delivery evidence. Require zero unintended emails across the controlled cancellation, camera pause, expiry, stale-contact, and duplicate tests.
- Include driver display name, event time, and a request to check in. Add precise location only with separate permission and an available reading. Allow the driver to see it in RAFIQ and the verified recipient to receive it by email. Expire precise coordinates in RAFIQ 24 hours after capture. Delivered email copies remain with the recipient. The initial public release keeps live email disabled.

### 8.6 Clip and report lifecycle

- Default to three seconds of context before and after an incident. Let drivers adjust each window between zero and five seconds. Cap clips at 30 seconds and 20 MB. Keep the first bounded segment of longer incidents and show that the clip was truncated. Discard temporary context outside a consented clip.
- Expire queued clips 24 hours after capture, hosted clips seven days after capture, and session and incident metadata 90 days after session end. Expired queue items cannot upload. Revoking consent discards unsent clips. Check these schedules against the university retention policy before retaining pilot recordings.
- Block access immediately at deletion or expiry. Purge retained copies, including backups, within 30 days. A single clip deletion preserves independent session metadata and revokes clip references. Withdraw hosted reports that depend on deleted or expired records and allow regeneration from eligible data. Hosted reports expire 30 days after creation or when a required source expires, whichever happens first. Owner-authorized download links expire after five minutes. Explain at export that downloaded files remain under the driver’s control.

### 8.7 Statistical methods and data access

- Use a two-sided paired permutation test of mean within-participant differences in incident rate per monitored hour across two controlled conditions. Report its 95% paired bootstrap interval with 10,000 draws and seed 20261120. Use a two-sided Fisher’s exact test for the proportion of participants with at least one incident across two independent groups and report 95% Wilson intervals for the proportions. Use a 0.05 significance level and label results exploratory. Require at least 10 complete pairs for paired analysis or 10 participants per arm for independent analysis. Withhold inference when input or design prerequisites fail and explain why alongside eligible descriptive results. Fixture checks require exact counts and absolute numerical error of at most 0.000001 for unrounded results, using matching versions and seeds.
- Replay only the driver’s own eligible retained session measurement series, with compatible timestamps, observation flags, policy version, and sufficient values for the requested threshold. Use reference labels when reporting accuracy. Exclude clips and precise location. Save simulation results separately from source sessions and live policy.
- Start Experiment Studio with versioned synthetic paired and independent-group fixtures. Additional predefined study datasets require institution-approved use. Cross-participant views and exports are aggregate only, with at least 10 distinct participants in every visible group. Suppress complementary totals if they would reveal a hidden group. Include the method and dataset version. Keep participant rows, private driving histories, and clips out of outputs.

### 8.8 MCP qualification and data boundaries

- Qualify **OpenAI Codex CLI** as the named pilot client for RAFIQ’s remote MCP server. Connect over Streamable HTTP with scoped driver authorization. Run controlled integration checks and repeat them in Codex CLI during the supervised pilot before activation. [Codex MCP documentation](https://developers.openai.com/codex/mcp)
- Limit the authorized client to the driver’s session identifiers, timestamps, duration, coverage, behavior and incident counts, and validated aggregate metrics with units and methods. Event metadata includes event identifier, class, relative start time, duration, and severity. Exclude raw media, clips and links, contacts, precise location, unrestricted measurement series, and other accounts’ data.
- A scoped report request returns an opaque identifier and status to the authorized client. The driver reviews the report in RAFIQ and controls PDF or Word export. Verify authorization at request and release, revocation during generation, field filtering, and cross-account denial. Apply the lifecycle in §8.6.

## 9. Illustrative example

- **I-1.** Nour is an illustrative driver for the confirmed pilot journey. Replace the name and context if the cohort supplies a representative example.
