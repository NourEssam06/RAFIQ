# RAFIQ screen specification

This is the screen-by-screen handoff for RAFIQ’s UI/UX designer. Use it to build the page frames, interactive panels, dialogs, and state variants for the English-language desktop web app. RAFIQ helps an adult driver set up a controlled monitoring session, understand what the built-in camera observed, and review private evidence afterward. The other audiences are supervisors using delegated controls on the driver’s device, invited RAFIQ staff, and recipients or agents using a connected external service.

The qualification baseline for monitoring is Chrome on Windows 11 with a built-in front-facing camera. Setup and driver interaction take place while stationary. An approved supervised session can use a passive presentation during motion. The screen IDs are design references. Use the display order below as the starting point for wireframes, including at narrower desktop widths and with browser zoom. [PRD](PRD.md) · [Experience](EXPERIENCE.md) · [Visual design](DESIGN.md) · [Frontend architecture](ARCHITECTURE.md#6-frontend-architecture)

## Contents

| Area | Screens and views |
| --- | --- |
| Public access | [P01 Public entry](#p01-public-entry) · [P02 Create account](#p02-create-account) · [P03 Verify email](#p03-verify-email) · [P04 Sign in](#p04-sign-in) · [P05 Recover access](#p05-recover-access) · [P06 Controlled-use onboarding](#p06-controlled-use-onboarding) · [P07 Restricted account](#p07-restricted-account) · [P08 Unavailable link](#p08-unavailable-link) |
| Dashboard and monitoring | [D01 Dashboard](#d01-dashboard) · [D02 Start session and readiness](#d02-start-session-and-readiness) · [D03 Monitoring](#d03-monitoring) · [D04 Emergency Mode](#d04-emergency-mode) · [D05 End status and interrupted-session recovery](#d05-end-status-and-interrupted-session-recovery) |
| History and evidence | [D06 Sessions](#d06-sessions) · [D07 Session Detail](#d07-session-detail) · [D08 Incident and alert details](#d08-incident-and-alert-details) · [D09 Personal Overview](#d09-personal-overview) · [D10 Clips](#d10-clips) · [D11 Clip replay](#d11-clip-replay) |
| Analysis and reports | [D12 What-If](#d12-what-if) · [D13 What-If result](#d13-what-if-result) · [D14 Experiment Studio](#d14-experiment-studio) · [D15 Study result](#d15-study-result) · [D16 Benchmark](#d16-benchmark) · [D17 Reports](#d17-reports) · [D18 Report review and export](#d18-report-review-and-export) |
| Settings and connections | [D19 Profile](#d19-profile) · [D20 Monitoring settings](#d20-monitoring-settings) · [D21 Emergency contacts](#d21-emergency-contacts) · [D22 Privacy](#d22-privacy) · [D23 Connections](#d23-connections) · [D24 MCP authorization](#d24-mcp-authorization) · [D25 Chat connection and consent](#d25-chat-connection-and-consent) · [D26 Temporary chat](#d26-temporary-chat) |
| Administration | [A01 Admin entry and invitation](#a01-admin-entry-and-invitation) · [A02 Authenticator enrollment and challenge](#a02-authenticator-enrollment-and-challenge) · [A03 Admin MFA recovery](#a03-admin-mfa-recovery) · [A04 Service Health](#a04-service-health) · [A05 Release Readiness](#a05-release-readiness) · [A06 Adoption](#a06-adoption) · [A07 Account Support](#a07-account-support) · [A08 Staff Access](#a08-staff-access) · [A09 Audit](#a09-audit) |
| External touchpoints | [X01 Emergency recipient](#x01-emergency-recipient) · [X02 External MCP agent](#x02-external-mcp-agent) |

See [shared design rules](#shared-design-rules), [requirements and prototype walkthroughs](#requirements-and-prototype-walkthroughs), and [items awaiting approval or visual design](#items-awaiting-approval-or-visual-design).

## Shared design rules

- **Navigation.** The private navigation order is **Dashboard**, **Sessions**, **Clips**, **Analysis**, **Reports**, **Settings**. Give **Start session** a distinct action. Analysis opens What-If and links to Experiment Studio and Benchmark. Settings contains Profile, Monitoring, Emergency contacts, Privacy, and Connections. Personal Overview sits one action from Dashboard. The live workspace takes priority during monitoring. Administration has its own permission-scoped navigation.
- **Returning to context.** Use links for destinations and buttons for actions. Back restores list filters, date range, scroll position, and the selected row when still accessible. A protected link resumes only after current identity, conditions, and permission checks succeed. Close private content when access is lost. A signed-out or switched account cannot see the previous driver’s private data or pending queue.
- **Feedback.** Label progress next to the affected work. Distinguish verification, loading, saving, queued, syncing, uploading, processing, and ready. Preserve valid inputs and unaffected sections during recoverable errors. Provide a specific reason and a recovery action where one exists. Distinguish empty, unavailable, stale, zero, and privacy-suppressed values. An example of suppression copy is “Hidden to protect participant privacy.”
- **Dialogs and forms.** Use persistent field labels, inline errors, and an error summary on failed submissions. For destructive or privileged actions, name the target, consequences, and required verification. Show success after confirmation. Give each dialog an accessible name, manage focus, allow Escape where safe, and return focus to the opener or nearest surviving item. Keep emergency countdown cancellation direct.
- **Visual and accessibility requirements.** Apply DESIGN.md’s canvas, ink, typography, spacing, and applicable navigation and input tokens. Use a skip link, landmarks, predictable reading and tab order, accessible labels, visible focus, and a meaningful heading on navigation. Pair critical status with plain text and a visible non-color cue. The warning must work with audio off and reduced motion on. Announce meaningful transitions once. Keep the countdown readable on demand without reading each tick aloud.
- **Charts and media.** Name the scope, time zone, units, denominator, sample size, and version where they affect interpretation. Provide keyboard access to exact values and an equivalent data table or ordered event list. Keep gaps and suppressed values distinguishable from zero. Label playback controls, playback position, and the incident represented by a clip. Stack content in reading order at higher zoom. Allow wide tables to scroll in a labeled region.

[Experience component patterns, states, and accessibility](EXPERIENCE.md#component-patterns) · [RAFIQ monitoring states](DESIGN.md#rafiq-monitoring-states) · [API error handling](API.md#11-error-handling-standards)

## Public access and onboarding

### P01 Public entry

- **Purpose and entry.** An adult visitor arriving at RAFIQ should be able to decide whether the product fits a controlled session and choose how to enter.
- **Display.** Put the RAFIQ name, a short explanation of local camera monitoring and private review, adult eligibility, and the desktop and controlled-use requirements before the account actions. Explain stationary setup and that vehicle motion requires an approved supervised procedure.
- **Actions and variants.** **Create account** opens P02 and **Sign in** opens P04. Show **Public signup is pending release** when registration is closed. Keep the sign-in path available where authorized. Public registration uses the same path regardless of university affiliation or country of residence.

### P02 Create account

- **Purpose and entry.** A new driver enters from P01 or P04. Use Clerk for the identity steps.
- **Display.** Show labeled email and password fields, Clerk’s password requirements and errors, and the adult eligibility statement. Show Google and Apple only for independently qualified providers. Place **Sign in** near the form for an existing driver.
- **Actions and variants.** Submit to the email verification step, or continue through the selected provider. Show field errors, submission progress, and safe retry. If the provider detects an existing identity, guide the user through verified linking. Include the Apple relay-address case. A canceled social flow returns to P04 with an explanation. When release pending blocks signup, return the visitor to P01.

### P03 Verify email

- **Purpose and entry.** A driver arrives from P02 or P04 with a pending Clerk verification. Explain that email verification is required before private access.
- **Layout and display.** Carry over P02’s RAFIQ wordmark, static lens artwork on the left, and flat form on the right. At narrow widths or high zoom, show the wordmark and form in one column. Lead with **Verify your email**, the destination address, and **Change email**. Present six visual slots as one labeled control for Clerk’s emailed code. Allow paste and one-time-code autofill. Use **Verify email** as the primary action and **Resend verification** below it when available.
- **Correct the address.** For a pending signup, **Change email** opens an inline edit with **Send code** and **Cancel**. After Clerk confirms the send, show the corrected address, clear the former code, and focus the code field. On the P04 path, restart sign-in for the corrected identifier when Clerk requires it. Editing the destination during sign-in leaves the registered account email intact.
- **Verification states.** Show **Verifying…** and prevent repeat submissions while Clerk processes the code. For an invalid code, explain how to retry next to the input. For an expired code, show **This code has expired. Request a new one.** and make **Resend verification** the primary action. Respect Clerk’s resend availability and limits. After a successful resend, restore the code form, confirm the send to the displayed address, and focus the empty code input. Show retry guidance if the send fails.
- **Verified.** Announce **Email verified** once. Resume the intended authorized destination or D01 after checking the session and eligibility. Send drivers who still need to accept the controlled-use conditions to P06 and return to P04 when Clerk requires sign-in.

[Default verification comp](../Pen%20Design/RAFIQ-verify-email-comp-01.png) · [Expired code comp](../Pen%20Design/RAFIQ-verify-email-expired-comp-01.png)

### P04 Sign in

- **Purpose and entry.** A returning driver arrives from P01, a private link, verification, recovery, or reinstatement.
- **Display.** Use Clerk’s email and password controls. Include qualified social actions, **Recover access**, and **Create account** when signup is open. Preserve the intended private destination during verification or linking.
- **Actions and variants.** Continue to P03, P06, the authorized destination, or D01 according to current state. Send a restricted driver to P07. Show invalid credentials, provider cancellation, and retry or recovery inline. Verified linking returns the driver to the existing account history.

### P05 Recover access

- **Purpose and entry.** Open from **Recover access** on P04. Treat the Clerk reset steps as consecutive views of the same flow.
- **Display.** Show registered email input, submission feedback, guidance for checking email, and the verification and password reset steps supplied by Clerk.
- **Actions and variants.** Provide resend or restart for an expired or invalid recovery link. Show rate-limit feedback and confirmation when the reset succeeds. Return to P04. Preserve the entered email where safe and use Clerk’s account-safe disclosure behavior.

### P06 Controlled-use onboarding

- **Purpose and entry.** A verified driver sees this on first use or when the required conditions version changes.
- **Display.** Present the current conditions in readable order. Explain stationary use, the approved supervised-use boundary, initial camera setup, and that recording consent is a separate choice at readiness.
- **Actions and variants.** Require explicit acceptance before continuing. Show acceptance progress, failed submission, and any newly required version. On success, use the intended eligible destination or D01. Offer an exit or sign-out while acceptance is incomplete.

### P07 Restricted account

- **Purpose and entry.** A driver reaches this view at sign-in or when the browser learns that hosted access was restricted.
- **Display.** Lead with **Account restricted** and the approved published RAFIQ support contact. Explain the block on new starts and hosted synchronization. When relevant, explain that records on the device remain locked and expire on schedule.
- **Actions and variants.** Offer fresh **Sign in** after reinstatement. A configured session already offline can continue local warnings within its existing limits. Surface the hosted restriction on reconnect and keep uploads locked. After verification of a fresh eligible sign-in, eligible queued items can sync. Connecting a previous MCP client requires fresh consent.

### P08 Unavailable link

- **Purpose and entry.** Use when a private resource link cannot be opened after authorization checks or when opened content loses eligibility.
- **Display and action.** Show “This item is unavailable.” Remove the resource content and its actions and return the user to the relevant authorized list. Use the same presentation for a missing, expired, deleted, or inaccessible private link. Inside an already authorized record, explain a known item-level cause such as clip expiry when that information is available to the driver.

[PRD accounts and privacy](PRD.md#51-accounts-privacy-and-readiness) · [Experience information architecture](EXPERIENCE.md#information-architecture)

## Dashboard and monitoring

### D01 Dashboard

- **Purpose and entry.** Default destination after eligible driver sign-in. A returning driver should immediately see the latest reviewable session.
- **Display.** Use D07’s full-session review layout for the latest completed session with ready analytics. Identify the session and its date at the top. Put **Personal Overview** within one action and keep **Start session** visible. If a newer session is syncing or processing, show its date and status near the ready result and provide a link when it is ready.
- **Actions and variants.** First use shows a short empty message and **Start session**. With sessions but no ready result, show the applicable pending or unavailable reason and a path to D05 or D06. Keep the currently displayed session identified while newer data loads.

### D02 Start session and readiness

- **Purpose and entry.** Open from **Start session**. The driver completes readiness while stationary.
- **Display.** Show the session context and current conditions, the built-in camera preview with face and upper-body framing guidance, the camera and usable-view check, vision file verification and initialization, online account eligibility, and clip consent. Show a saved opt-in and selected recording categories or an explicit decline. Offer the stationary context and show the supervised option when eligible. For a supervised session, show the designated supervisor’s delegated actions, current authorization, revocation, and Emergency Mode eligibility.
- **Actions and variants.** **Start monitoring** is available when the applicable checks pass, including when the driver declines clips. **Cancel** returns to the origin. For permission denied, a missing camera, or poor framing, explain what to correct and offer **Recheck**. Distinguish “Monitoring files couldn’t be verified” from “Monitoring couldn’t start,” and offer **Retry setup**. Explain the approved setup on unsupported browsers or devices. Keep new starts unavailable offline. Request camera permission only.

### D03 Monitoring

- **Purpose and entry.** Open after readiness or manual resume. The screen answers whether observation is usable, what RAFIQ detected, and what is happening with capture and sync.
- **Display.** Put the session and observation state first, followed by the warning area and stationary camera preview. Show recording and sync as separate labeled statuses and place Emergency Mode alongside them when the session is eligible. Show **Pause monitoring**, **End session**, and **Stop recording** where applicable. A combined warning names each qualifying behavior and gives each behavior’s visible cue and duration on a separate line. Use stronger wording and visual emphasis for escalation. Optional warning audio follows the driver’s setting.

Use the qualified behavior labels **Drowsiness**, **Distraction**, **Phone use**, **Eating**, and **Drinking** where enabled. Example visible cues include sustained eye closure, sustained off-task gaze, active interaction with a phone, and a hand-to-mouth action with food or a drink container. Example combined warning copy is “Drowsiness and phone use observed,” followed by separate cue and duration lines. Treat reaching as a candidate pending release qualification.

| State | What the frame shows and what can happen next |
| --- | --- |
| Usable observation | “Monitoring active. No qualifying behavior observed.” With a warning, show its explanation and **Acknowledge warning**. Acknowledgment preserves the observation. Apply the approved persistence, gap, recovery, and cooldown policy to subsequent warnings. |
| Partly usable observation | Keep observable behaviors active. Name an unavailable behavior and the missing cue when known, for example “Phone use is unavailable because your hands aren’t visible.” |
| Deliberately paused | Identify the deliberate pause. Offer the stationary driver **Resume monitoring** when the view is usable, plus **End session**. Exclude this pause from elapsed monitoring exposure. |
| Observation-loss pause | Replace any stale warning with the reason, such as obstruction, poor lighting, low confidence, or camera loss. Stop escalation and clear emergency qualification. After a usable view returns, require **Resume monitoring**. Include the observation gap in elapsed monitoring exposure. |
| Offline or syncing | Show that local monitoring and warnings continue in the open tab after readiness. Distinguish pending records and clips from unavailable items. Retry eligible data on reconnect. The qualified baseline to validate is up to 30 continuous offline minutes after readiness. |
| Recording stopped or limited | Identify capture, queued clip, uploading, and unavailable clip states. When the local queue reaches 100 MB or 20 clips, new affected clips become unavailable while monitoring continues. Consent revocation stops capture and discards unsent clips, including pending transfers. |
| Supervised motion | Use the approved passive presentation and suppress stationary preview and navigation. Only the authorized supervisor can acknowledge a warning, cancel a countdown, or pause on the driver’s device. The stationary driver retains start, resume, end, and delegation control. |

- **Leaving the workspace.** An in-app action that would leave live monitoring offers **Stay in session** and **End session** while stationary. Ending stops camera, capture, and unsent emergency actions, releases delegation, and opens D05 or ready D07. Closing, reloading, or crashing the tab follows D05 recovery.

### D04 Emergency Mode

- **Purpose and placement.** Use a labeled panel or status region inside D03. It describes the alert process in an eligible supervised session. While unavailable, explain the applicable reason at setup, such as missing supervision or eligible channels. Ordinary warnings remain available.

| State | What the driver or authorized supervisor sees |
| --- | --- |
| Standing by | Show whether Emergency Mode is eligible. Sustained qualifying drowsiness alone can start a countdown. |
| Contact alert countdown | Show the remaining time and a direct **Cancel contact alert** action. Keep **Acknowledge warning** separately labeled. Use 10 seconds of continuous qualifying drowsiness, a separate 15-second cancellation window, and a 120-second attempt deadline from countdown entry as controlled-test starting values. |
| Canceled, withheld, or closed | Clearly label the known outcome. Cancellation, observed recovery, camera pause, or session end stops unsent attempts. Offline or stale eligibility can also withhold a send. Resume after camera pause starts fresh qualification and a full cancellation window. Reconnect leaves stale sequences closed. |
| Attempting or outcome recorded | Show channel and contact order as authorized. **Pending** is an in-progress attempt. **Accepted** means the provider took the alert for processing. **Delivered** requires confirmed delivery. **Failed** is terminal failure. **Unconfirmed** identifies an attempted channel still unresolved at the deadline. Give separate text to an attempt that was withheld before sending. |

- **Fallback.** The active tab must supply fresh authenticated online confirmation for each attempt. Skip contacts with no eligible channels. Attempt each eligible channel for the current contact once. Delivery on either channel closes fallback. Advance only after every eligible channel for that contact has been attempted and has terminally failed. A pending or ambiguous outcome holds progression. Later delivery evidence can update the history without reopening a closed sequence. Inspect channel history in D08.

### D05 End status and interrupted-session recovery

- **Purpose and entry.** Open from **End session**, a pending session row, or the return from an interrupted run. The driver should know the camera is off and when review will be available.
- **Display.** Identify the session and its ended or interrupted state. Show required records syncing, analytics processing, and optional clip uploads as separate lines. Use **Open session details** when analytics are ready, and offer **Back to Sessions**. An optional missing or pending clip never blocks review.
- **Recovery variants.** Closing, reloading, or crashing ends live observation. After fresh eligible online sign-in by the same driver, finalize the interrupted session at the last durably recorded observation and sync eligible data. Explain connection loss, retry, expiry, and permanent unavailability. Keep other accounts’ queues out of the view. A new session starts from D02.

[Experience session and emergency transitions](EXPERIENCE.md#session-and-emergency-mode-transitions) · [TRD session, recording, and offline contracts](TRD.md#2-session-recording-and-offline-contracts) · [Vision reuse](VISION-REUSE.md)

## History and evidence

### D06 Sessions

- **Purpose and entry.** Open from the driver navigation, D05, or the history link in D19. The driver should be able to find a past run and tell whether it is reviewable.
- **Display.** List the driver’s sessions newest first. Each row identifies the session by date and local start time, with end time or duration where available, and a clear review status. Distinguish ended, interrupted, syncing, processing, ready, and unavailable. Give each row one named link to D05 or D07.
- **Actions and variants.** Offer **Start session** for first use, paging for longer history, retry for a recoverable load error, and an unavailable reason at an authorized row. Keep row selection and position on Back. If a record expires or is deleted while open, return via P08.

### D07 Session Detail

- **Purpose and entry.** Open from D01, D05, D06, or an authorized link. The driver should be able to connect observed behaviors and warnings to exact moments and judge the quality of the available observation.
- **Header.** Show the session date, displayed time zone, start and end, status, and relevant catalog, model, or warning-policy versions. Link to **Personal Overview** and to **What-If** for an eligible source. Place **Delete session** in a secondary action area.
- **KPI cards.** Use the same order in Dashboard and Session Detail.

| Card | What it displays |
| --- | --- |
| Monitored time | Total elapsed monitoring time. Deliberate pauses are excluded. Observation-loss pauses are included. |
| Incidents | Distinct incident count and incidents per monitored hour. An incident containing multiple behaviors contributes once. |
| Time with detected behavior | Total time and percentage of monitored time with at least one detected behavior. Count overlapped time once in this total. |
| Observation coverage | Usable feed time as a share of elapsed monitoring. Show usable time and the denominator. Flag coverage below 90% using the unrounded value. |
| Warnings | Count distinct issued warnings. A combined warning contributes once. |

- **Timeline.** Label the axis **Elapsed time since session start**. Give each detected behavior a row and use an observation row for deliberate pauses, observation-loss intervals, and usable time without detections. Mark warnings and Emergency Mode events. Provide **Zoom in**, **Zoom out**, **Reset zoom**, and a keyboard-operable way to move the visible range. Display the range boundaries. Timeline zoom affects the timeline only. Select an event by its marker or its ordered list entry and open D08 at that timestamp.
- **Breakdown and duration.** Show horizontal bars with a **Count / Duration** selector, exact values, and per-behavior coverage where available. Show individual detection durations by behavior through 30 matching detections. For more than 30, use **0–<2 s**, **2–<5 s**, **5–<10 s**, **10–<30 s**, and **30 s or longer**. Show sample size in both modes and any available supporting descriptive statistics.
- **Variants and deletion.** Distinguish usable observation with zero detections, an unavailable class, no usable observations, and no exposure. Mark low coverage and version changes near relevant results. Missing media leaves independent evidence visible. The delete dialog identifies the session, affected incidents and clips, and dependent hosted reports. Show progress and confirmed removal before returning to D06.

### D08 Incident and alert details

- **Purpose and entry.** Open as a detail panel within D07 when a driver selects an incident, warning, or emergency marker or row. The selected timestamp stays visible and focused in context.
- **Incident contents.** Show elapsed and local times where helpful, start, end, duration, constituent behaviors, any overlap, detector confidence, and available supporting measurements with units. Show associated warning and severity where recorded. Preserve the original observation evidence, including if the driver disagrees with it. Show the linked clip’s availability and expiry, or describe the reason a known clip is unavailable.
- **Warning and emergency contents.** Show the warning’s issue time, named behaviors, cue or duration where recorded, and severity. For an emergency entry, show the recorded sequence timeline and contact/channel outcomes. Distinguish withheld, accepted, delivered, failed, and unconfirmed outcomes using D04’s meanings. Show authorized location information only while eligible. A later status change updates the recorded evidence.
- **Actions and variants.** Give an available clip an **Open clip** action to D11 and keep a link back to the selected occurrence. On Back from clip replay, restore timeline range, occurrence, and incident selection. Use an accessible ordered event list as an equivalent to selecting markers.

### D09 Personal Overview

- **Purpose and entry.** Reach from Dashboard in one action or from Session Detail. Help the driver interpret repeated behaviors and compare exposure and coverage across sessions and periods.
- **Scope controls.** Default to **Last 30 days**. Offer **Last 7 days**, **All available history**, and a custom range, plus session and behavior filters. Show the time zone, active filters, **Apply**, and **Clear filters**. Include completed sessions with ready analytics and show separate syncing and unavailable counts. When recalculating, identify the selected scope and the scope of any previous figures still on screen.
- **KPI cards.** Show completed sessions and monitored hours, incidents and incidents per monitored hour, time and share with detected behavior, observation coverage, and warnings and warnings per monitored hour.

| Section | How the designer should present it |
| --- | --- |
| Trends | Switch between incidents/hour, warnings/hour, and share of time with detected behavior. Show daily points through 30 days and local Monday-starting weeks for longer ranges. Assign a whole session to its start date in the displayed zone. Give each point monitored exposure and coverage. Show gaps for unusable observations. |
| Session comparison | Select two to four sessions. Show KPI values and behavior breakdowns side by side, with monitored time and coverage next to each rate. Link back to Sessions or selected incident evidence. |
| Behavior ranking | Rank by detection count, duration, or share of eligible sessions. Show exact values and the number of sessions with usable observation for that behavior in the share denominator. |
| Overlap matrix | Show incident count for actual overlaps and the number of sessions in which both behaviors were observable together. Distinguish an eligible pair with zero overlap from a pair with no joint observation. |
| Time since monitoring began | Use **0–<5**, **5–<15**, **15–<30**, **30–<60**, and **60+** monitored-minute bands. Per band show incident rate, monitored minutes, coverage, and contributing sessions. Assign each incident by its start in cumulative monitored time. |
| Findings | Explain recurring behaviors and compare with the immediately preceding equal-length period under the same filters and time zone. Require available figures, one eligible session, at least 15 monitored minutes, at least 90% coverage, and verified comparable versions in both periods. Show available figures and the reason for any withheld comparison. Report absolute change when the previous value is zero. |

- **Interpretation and states.** Pool counts over total monitored hours for rates. Divide the union of detected time by total monitored exposure for the overall share. A multi-behavior filter matches any selected behavior and preserves monitored exposure and overall coverage for the selected sessions. Keep per-behavior durations visible in breakdowns. Mark low coverage, changed catalog/model/policy versions, unavailable samples, and empty filters. Offer relevant recovery such as clearing filters or selecting comparable sessions.

### D10 Clips

- **Purpose and entry.** Open the private clip library from the driver navigation. A driver can find a clip by the behavior or session they remember.
- **Display.** Show search with behavior, date, and session filters and active selections. Each authorized row identifies the behavior, incident time, source session, clip state, and expiry where applicable. Use **Open clip** for playable recordings and keep deletion individually named.
- **Actions and variants.** Show first-use empty, no matching clips with **Clear filters**, and item-level queued, uploading, available, or unavailable states. In an authorized incident context, explain when recording was declined, the category was excluded, the clip expired, or a limit prevented capture or upload. Return from D11 to the same filters and row. Session analytics remain available independently of a clip.

### D11 Clip replay

- **Purpose and entry.** Open from D10 or D08. Make it clear what the driver is watching and where it came from.
- **Display.** Show behavior, incident timestamp, clip timing and duration, source-session link, and expiry. Label truncated video as the available first segment. Put a video-only player after the context, with named play/pause and seek controls and a readable time position. Start playback on request.
- **Actions and variants.** Provide **Back to incident** or **Back to clips** according to entry. Distinguish loading, eligible retry, and unavailable playback. If access is revoked while open, stop playback and clear the media. **Delete clip** opens a confirmation that identifies the clip, explains the loss of replay and linked access, and explains that the independent session record remains. Return to a surviving context on success.

[PRD history and analytics](PRD.md#54-history-recordings-and-data-lifecycle) · [TRD personal dashboard calculations](TRD.md#51-personal-dashboard-fr-14) · [Experience review and retention](EXPERIENCE.md#review-analysis-and-data-lifecycle)

## Analysis and reports

### D12 What-If

- **Purpose and entry.** Analysis opens here by default, or D07 can open it with an eligible session selected. The driver can try how an adjustable threshold would change a past result.
- **Display.** Show links to Experiment Studio and Benchmark, then an eligible source selector, selected session date, supported behavior thresholds, measurement and policy versions, and whether reference labels exist. List saved runs with creation time, source, and status. Explain that the run uses a retained compatible measurement series and saves a separate simulation. Live monitoring uses the approved release policy.
- **Actions and variants.** Select a source, adjust the supported thresholds, and **Run simulation** to D13. Allow only behaviors and thresholds supported by the selected source. Use the approved range for the form. The proposed numeric score range in the API is 0–1. Show invalid inputs inline and explain when no compatible or sufficiently observed source is available. Recover from expired sources by returning to selection.

### D13 What-If result

- **Purpose and entry.** Open after a run or from a saved entry in D12. Show the difference between the recorded baseline and the replay under the selected thresholds.
- **Display.** Keep the source session, selected thresholds, run status, data version, and analysis or policy version above the results. Label the two columns **Recorded baseline** and **Simulated result**. Show available counts and rates with exact values and scope. Add precision, recall, accuracy, false alarms, and missed detections only when reference labels support them. Where labels are absent, explain the unavailable evidence.
- **Actions and variants.** Distinguish queued, processing, ready, retryable, invalid-input, and unavailable-source states. A transient retry uses the same inputs. Return to D12 to change inputs and start another run. A saved result keeps its original scope and versions.

### D14 Experiment Studio

- **Purpose and entry.** Open from Analysis. The driver chooses an approved predefined study or versioned synthetic fixture and compares two conditions.
- **Display.** Show dataset name and version, paired or independent design, observation unit, two condition selectors, and the approved method for that design. Keep saved runs visible with their dataset, conditions, method, creation time, and status. Use descriptive condition labels supported by the dataset.
- **Actions and variants.** **Run study** opens D15. Open saved results or rerun their eligible inputs. Explain a missing dataset, invalid condition pair, unsupported method, or expired source at the selector. The dataset picker uses approved predefined sources.

### D15 Study result

- **Purpose and entry.** Open from an active run or saved result. Help the driver interpret the approved descriptive output and decide how much weight to give exploratory inference.
- **Display.** Show status first, then dataset and analysis versions, design, conditions, observation unit, sample sizes, estimates, intervals, and limitations. State the test and show its p-value when eligible. Label inference **Exploratory** and show the 0.05 significance level. Expand reproducibility settings in **Method details**.

| Design | Required result detail |
| --- | --- |
| Paired | Show the mean within-participant difference in incidents per monitored hour, the two-sided paired permutation test, and 95% paired bootstrap interval. Require at least 10 complete pairs. Show 10,000 bootstrap draws and seed 20261120. |
| Independent groups | Show the proportion of participants with at least one incident in each group, the two-sided Fisher’s exact test, and 95% Wilson intervals for the proportions. Require at least 10 participants per arm. |

- **States and actions.** Show queued, processing, transient failure with **Retry**, and ineligible inputs with a return to D14. Withhold inference if prerequisites fail and show the reason beside available descriptive output. Show and export only disclosure-approved aggregates with at least 10 distinct participants in every visible group. Suppress subtotals or complementary results that could reveal a hidden group. **Export aggregate** requires a qualified format and an eligible result. Design its unavailable state before specifying a file label.

### D16 Benchmark

- **Purpose and entry.** Open from Analysis or an approved reference in D18. Explain how the released behavior system performed on controlled held-out evidence.
- **Display.** Show benchmark version, dataset and held-out scope, annotation catalog, model and policy versions, evaluation sample, and monitored exposure. Present class-level precision, recall, F1, accuracy, and confusion counts or matrices. Show overall and per-class observation coverage, false warnings per monitored hour, and warning delay. Explain frame matching at 10 Hz and the exclusion of unusable class frames from that class’s confusion counts. Provide a table or definition panel that makes the denominators and limitations available.
- **Actions and variants.** Show loading, retryable retrieval failure, awaiting approval, and a metric unavailable for a class or version. The driver view presents approved aggregates and their methods. Link back to Analysis or the referring report.

### D17 Reports

- **Purpose and entry.** Open from the driver navigation or after requesting a report in the external agent. Help the driver find a session or personal-trend report and see what action is available.
- **Display.** List authorized reports or visible jobs with report type, creation time, and status. Where the available summary includes them, add the title, related session or date scope, and version. Use **Queued**, **Processing**, and **Ready to review** for progress. Show **Needs revision**, publication blocked, expired, or withdrawn where the job state is authorized for display. Keep job state distinct from export state.
- **Actions and variants.** Open a ready report in D18. Explain how to request a report or a new version through MCP and link to D23. Direct draft correction to the agent. The first-use state explains the agent workflow. When authorization or a required source changes, remove the affected review and export actions and explain the available next step.

### D18 Report review and export

- **Purpose and entry.** Open a ready report from D17 or an eligible direct link. The driver should be able to verify what the document says before exporting.
- **Display.** Show report title, type, generation date, and expiry. Identify the source session or period and applicable versions from the validated sources. Present checked findings with their numerical evidence, methods, source references, and limitations. Show units, coverage, and sample sizes where relevant. Include the approved aggregate benchmark summary for general reports with a link to D16 when available.
- **Actions and variants.** Offer **Export PDF** and **Export Word (.docx)**. Show preparing, ready to download, failure with eligible retry, and a five-minute link expiry. The preview and each export use the same validated figures and snapshot. An expired link can be reissued only while the report and driver remain eligible. If required sources expire or are deleted, show the withdrawal state and direct regeneration from eligible sources to the external agent. Explain at export that downloaded files remain under the driver’s control.

[PRD analysis and reporting](PRD.md#55-personal-analytics-simulation-and-controlled-experiments) · [Statistical methods](PRD.md#87-statistical-methods-and-data-access) · [API open qualifications](API.md#18-open-questions-and-decisions-requiring-approval)

## Settings and connections

### D19 Profile

- **Purpose and entry.** Open from Settings. The driver can see which account is active and find account and history actions.
- **Display.** Show the editable display name, registered email, and verification state. Give identity management to the applicable Clerk flow. Include **View session history**, **Sign out**, and a link to Privacy for account deletion.
- **Actions and variants.** Show field validation, saving, saved, and retryable failure. On **Sign out**, clear visible private data across open tabs and lock the signed-out account’s pending records. A later sign-in follows P04.

### D20 Monitoring settings

- **Purpose and entry.** Open from Settings. The driver can prepare preferences for a subsequent session.
- **Display.** Group settings in this order. Show the supported built-in camera choice and any permission issue. Show optional warning audio and **Default / Enhanced visibility**. Enhanced visibility makes warning text and the non-color cue more prominent. Show recording consent, eligible behavior categories, and separate **Before incident** and **After incident** controls. Each defaults to 3 seconds and accepts 0–5 seconds. Explain video-only clips, the 30-second and 20 MB limits, and the label used for a truncated clip.
- **Actions and variants.** Provide **Save** with validation and confirmed feedback. Explain when changes apply to later sessions. Show an explicit action for recording consent withdrawal and explain its immediate effect on capture and unsent clips. Link to Privacy for expiry and deletion. Use the fixed qualified live policy for behaviors, severity, and timing.

### D21 Emergency contacts

- **Purpose and entry.** Open from Settings or readiness while stationary. The driver should know who will be tried, in which order, and what they may receive.
- **Display.** Show up to two saved contacts in driver-selected order. Each row shows the contact’s email and/or WhatsApp number and the state of each channel. Distinguish saved, eligible, opted out, and unavailable. Give each contact **Edit**, **Remove**, and labeled move controls where applicable. Keep the location-sharing control separate and show the fixed message preview with the location variants.

> RAFIQ observed sustained signs of drowsiness for [driver name] at [time]. Please call [driver name] to check on them.

- **Location preview.** Append the map location or link when a usable location is available and separately permitted. Otherwise append “Location unavailable.”
- **Actions and variants.** Provide add, edit, remove, reorder, and save feedback. Keep editable values on field or save errors. A WhatsApp number change requires an eligibility recheck. A saved but unqualified or opted-out channel is ineligible for dispatch. Confirm edits or removals before showing them as saved and prevent stale sends to the old destination. Show the reason when no contact has an eligible channel.

### D22 Privacy

- **Purpose and entry.** Open from Settings or relevant evidence screens. Explain what RAFIQ keeps, what expires, and what deletion affects.
- **Display.** Put recording and location-sharing status with links to their controls above the retention table. Link to Clips and Sessions for item deletion and to Connections for sharing and grants. Explain that private monitoring data requires separate approval for reuse in evaluation or training.

| Data or access | Retention or expiry to display |
| --- | --- |
| Queued clip | 24 hours from capture. |
| Hosted clip | 7 days from capture. |
| Session and incident metadata | 90 days from session end. |
| Precise location | 24 hours from capture. |
| Hosted report | 30 days from creation or earlier when a required source expires. |
| Authorized report download link | 5 minutes, with current authorization required when used. |

- **Deletion explanation.** Access ends immediately on deletion or expiry. Retained copies, including backups, are purged within 30 days. A deleted clip leaves independent session metadata. A deleted session or other required source removes affected access and withdraws dependent hosted reports. Downloaded files remain under the driver’s control. An expired or deleted queued item cannot be restored by retrying sync.
- **Delete account.** Put **Delete account** in a clearly marked area. The confirmation identifies the account and names account access, sessions, recordings, dependent hosted reports, and connections affected by deletion. Show in-progress, recoverable failure, and confirmed access removal. On confirmation of removal, close private views and return the driver to public access.

### D23 Connections

- **Purpose and entry.** Open from Settings or report help. Keep compatible external MCP clients and optional in-app chat providers in clearly labeled groups.
- **MCP contents.** Show the single RAFIQ HTTPS endpoint and generic compatible-client setup instructions. List connected clients and each active read or author grant. Provide independently named revoke actions. Explain report authoring through the external agent and link to Reports. Show no grants, expired or revoked grants, and fresh authorization for reconnection.
- **Chat provider contents.** Show each provider’s current qualification, connection, and sharing-consent state separately. Offer **Connect**, **Reconnect**, **Review sharing**, **Open chat**, **Revoke sharing**, or **Disconnect** only when applicable. An unavailable provider can show the reason. Public signup remains independent of chat availability.
- **Feedback.** Show changes per client or provider, with saving and confirmed outcomes. Revocation applies immediately. Closing an invalidated chat clears it and suppresses any affected response. Revoking an author grant during authoring can block report publication.

### D24 MCP authorization

- **Purpose and entry.** The external client opens a RAFIQ authorization screen. After sign-in, the driver decides what that client may do.
- **Display.** Name the requesting client. Present independent choices for **Read driving data** and **Author reports**. Explain that reading covers approved session summaries, analytics, and event metadata. Explain that authoring lets the agent start a report job, receive approved job inputs and a template, check status, and submit a draft. The finished report is reviewed in RAFIQ.
- **Actions and variants.** Allow the driver to approve selected permissions or decline and return to the client. Show sign-in required, invalid or expired authorization, and confirmed choices. Show separately revocable grants in D23. Explain approved data categories in plain language. Keep raw media and measurements, clip links, contacts, precise location, and finished report contents outside the client’s access.

### D25 Chat connection and consent

- **Purpose and entry.** Open from a provider in D23. Provider linking and RAFIQ’s first-use sharing consent are separate steps.
- **Display.** Name the provider, the eligible subscription requirement, connection status, and the provider’s approved data-handling explanation. Before the first send, explain that chat sends the driver’s messages and relevant authorized data. Name session identifiers, timestamps, duration, coverage, behavior and incident counts, validated aggregate metrics, and event metadata such as class, start, duration, and severity. Explain the scope and how to revoke it.
- **Actions and variants.** Provide qualified **Connect** or **Reconnect**, then explicit consent or decline. Handle provider cancellation, expired connection, unavailable service, and failed consent save. Enable chat only when the provider, subscription connection, and consent are current. Declining returns to Connections with sharing disabled.

### D26 Temporary chat

- **Purpose and entry.** Open from the eligible provider in D23 after consent. The driver can ask questions and follow-ups about their own sessions and trends.
- **Display.** Name the provider and mark the conversation **Temporary**. Show the message list, labeled composer, send progress, and **Close chat**. Make the current data scope understandable. Keep provider data and interpretations separate from validated report actions.
- **Actions and variants.** Show the empty conversation, sending, answer, retryable failure, expired connection, provider unavailable, and allowance exhausted. Give **Reconnect** or **Retry** where applicable. Close, sign-out, sharing revocation, and disconnect clear the conversation and suppress any response invalidated before it reaches the driver. Report requests go through the external agent described in D17 and X02.

[PRD clip and report lifecycle](PRD.md#86-clip-and-report-lifecycle) · [MCP and chat data boundaries](PRD.md#88-mcp-qualification-and-data-boundaries) · [Optional chat qualification](PRD.md#89-optional-chat-provider-qualification)

## Administration

Use a separate internal shell. Owners can open all dashboard views and manage Staff Access and Audit. Staff see the entries their current permissions allow. **View metrics** covers Service Health, Release Readiness, and Adoption. **Account support** covers exact lookup and eligible verification or recovery messages. **Suspension** combines with Account support for suspend and reinstate actions. Clear affected views immediately after revocation. The dashboard presents aggregates and, in Account Support, the five permitted account fields.

### A01 Admin entry and invitation

- **Purpose and entry.** Enter from the separate internal sign-in page or an invitation link. The app uses verified identity, an active admin grant or eligible bound invitation, and MFA.
- **Display.** Explain the staff access requirement and show the verified sign-in step. For invitations, show validation progress and the invite acceptance action when the signed-in identity matches. Invitations are single-use, expiring, and bound to the designated identity.
- **Actions and variants.** Show expired, used, invalid, wrong identity, and revoked access. Offer applicable sign-in or sign-out. Continue to A02 for enrollment or challenge. After verification, land on Service Health when permitted or the first permitted view. If no views are permitted, explain why the dashboard cannot open and offer sign-out.

### A02 Authenticator enrollment and challenge

- **Purpose and entry.** An invited admin enrolls. A returning admin verifies the current session. Sensitive actions can also open fresh verification from their originating view.
- **Display.** During enrollment, show authenticator-app setup instructions and the enrollment information, a labeled six-digit code field, and the issued recovery codes after successful setup. Explain that recovery codes are single-use and should be stored securely. For challenge, show code input, verify action, and the link to A03. Identify the action being re-verified when launched from a privileged form.
- **Actions and variants.** Show waiting, verified, invalid or reused code, and rate limit. On success enter the authorized destination or return to the action that required verification. If authorization changes during the challenge, close that flow and show current access status.

### A03 Admin MFA recovery

- **Purpose and entry.** Open from the authenticator challenge when the admin cannot use the enrolled device.
- **Display.** Explain the verified sign-in requirement and show one labeled unused recovery code field. Describe the applicable path if another eligible Owner must reset enrollment.
- **Actions and variants.** Show invalid, used, rate-limited, and verified outcomes. Once recovered or reset, the admin completes fresh enrollment in A02. An affected previous admin session loses access as required. Loss of the last Owner’s authenticator and recovery codes follows the audited deployment recovery procedure.

### A04 Service Health

- **Purpose and entry.** Default admin view for metrics permission. Help staff distinguish current operational problems from missing or stale telemetry.
- **Display.** Put the range selector and query cutoff at the top. Default to **Last 24 hours**. Offer **1 hour**, **7 days**, and **30 days**. Show service status cards, trends for uptime, API error rate and p95 latency, and operational tables. Give each signal its last update time, units, denominator where relevant, and approved health state.

| Section | Required signals |
| --- | --- |
| Availability and performance | Key service states, uptime as successful scheduled checks divided by observed checks, API error rate as failed server requests divided by eligible requests, and p95 API latency. Label units and denominator counts. |
| Queues and storage | Session sync and report queue depth and oldest pending age, upload or worker health where available, and storage usage and quotas. |
| Backup and deletion | Last successful backup, lag, deletion and purge progress, and overdue purge counts where available. |
| Emergency delivery | Distinct attempt counts for **Pending**, **Accepted**, **Delivered**, **Failed**, and **Unconfirmed**, for email and WhatsApp separately. Mark a channel awaiting qualification independently of runtime health. |

- **Actions and variants.** Use **Healthy**, **Degraded**, **Unavailable** for a fresh confirmed outage, and **Unknown** for missing or stale telemetry. Show zero activity only with fresh evidence. Preserve valid sections and selected range when another source fails. Provide retry at the affected section and an entry to A05.

### A05 Release Readiness

- **Purpose and entry.** Open within Service Health with metrics permission. Review the status of release conditions and supporting evidence.
- **Display.** Show a row per gate with its name, **Passed / Failed / Pending**, last verification date, and the approved evidence link when available. Identify public launch, email, WhatsApp, and each optional chat provider separately. Use readable state text when evidence has yet to be recorded.
- **Actions and variants.** Open approved evidence and return to Service Health with its range preserved. Show loading, missing evidence, and read failure. Gate decisions and activation follow the release process outside this view.

### A06 Adoption

- **Purpose and entry.** Open from admin navigation with metrics permission. Staff use aggregate figures to see product uptake and where first use drops off.
- **Display.** Put date range, displayed time zone, and data freshness before the five cards. Default to **Last 30 days**, with **Last 7 days**, **All history**, and custom dates. Show **Signups**, **Verified accounts**, **Drivers completing a first session**, **Active drivers**, and **Completed sessions**. Show the signup → verification → first completed session funnel with conversion denominators and ordered milestones achieved within seven days of signup. Label in-progress cohorts.
- **Trends.** Plot active drivers and completed sessions daily through 30 days and in local Monday-starting weeks after that. An active driver completed at least one session and is counted once for the selected range and once per trend bucket. Count completed sessions once by their recorded end, after durable completion sync.
- **States and privacy.** Distinguish provisional or incomplete figures, privacy suppression, and unavailable exact totals. Withhold results that could reveal fewer than 10 distinct drivers, including inferable differences across overlapping dates, funnel steps, totals, or related views. Show eligible anonymous historical buckets after source expiry or deletion. An exact total that depends on expired detail or combining anonymous buckets is unavailable. Keep the requested range and valid results visible after a partial failure.

### A07 Account Support

- **Purpose and entry.** Open from admin navigation with Account support permission. Staff locate one driver account and perform only actions available for that account’s state.
- **Display.** Show an exact registered email or account ID search. Return only **Account ID**, **Registered email**, **Verification status**, **Account status**, and **Signup date**. Use a separate action area below the matched account.
- **Actions and variants.** Show no match, rate-limited lookup, and safe action outcomes. Offer eligible verification or recovery messages only to the registered email. Keep credentials, codes, and message payloads private. Show **Suspend account** or **Reinstate account** only with both permissions and an applicable account state. The dialog names the target and consequences, requires an approved reason code and fresh verification, and shows the confirmed outcome. Preserve the selected reason during recoverable failure. Recheck eligibility before committing. Account deletion is available to the driver in D22.

### A08 Staff Access

- **Purpose and entry.** Owner-only. Manage who can enter the internal dashboard and what they can do.
- **Display.** List current admins with an authorized identifier, role, access state, and assigned permissions. Provide an invitation form with the intended registered email and requested permissions. On creation, show the invitation link and expiry. Show separate controls for metrics, support, and suspension permissions. Give an eligible MFA-protected admin an Owner appointment action.
- **Actions and variants.** Require fresh verification for invitations, permission and Owner changes, and MFA reset. Use a confirmation that identifies the affected administrator and change. Show save errors, permission conflict, immediate revocation, and last-Owner protection. An eligible Owner reset for another admin leads to A03 and A02 as applicable.

### A09 Audit

- **Purpose and entry.** Owner-only. Review the last 90 days of admin access and support actions in a read-only view.
- **Display.** Show filters for staff member, action, outcome, and date. List timestamp, actor, action, applicable permitted target, and outcome in reverse chronological order. Include failed lookups and actions. Omit unmatched lookup email values, access codes, and private driving data.
- **Actions and variants.** Apply or clear filters and page through older records within retention. Show no matching activity, load failure with retry, and access loss. Use readable time-zone and status labels.

[PRD admin requirements](PRD.md#57-admin-dashboard) · [TRD admin contracts](TRD.md#71-admin-dashboard-fr-22) · [Release process](GIT_WORKFLOW.md#10-continuous-deployment-strategy) · [Deployment procedure](DOCKER.md#11-production-deployment)

## External touchpoints

### X01 Emergency recipient

- **Channel and entry.** A registered contact receives the message in email or WhatsApp when an eligible alert is sent. Show the exact preview from D21, the driver name and observation time, and the request to call the driver.
- **Variants and action.** Include a usable map link or location only with driver permission. Otherwise include “Location unavailable.” The recipient can read the message and open the available location directly from the message. Reply and reading are separate from confirmed provider delivery. RAFIQ’s in-app evidence appears in D08.

### X02 External MCP agent

- **Channel and entry.** A driver follows D23’s compatible-client setup and grants the chosen permissions in D24. The driver asks the external agent for a session or trend report or for a new version.
- **Touchpoint.** The authorized agent starts the job, retrieves approved job evidence and template, checks status, and submits or revises the draft. The driver sees the eligible status in D17 and reviews or exports the validated result in D18. If access expires or is revoked, the driver returns to D23 for fresh authorization when eligible.

## Requirements and prototype walkthroughs

Use example data that makes the workflow visible. For instance, show an incident with two overlapping behaviors, a newer session still syncing, an accepted email attempt with delivery awaiting confirmation, and an Adoption result with a suppressed cohort. Pair each example with the state that changes the user’s next action.

For a Session Detail example, use 12 monitored minutes, of which 10 were usable. Show 83.3% coverage with a low-coverage label. Two distinct incidents yield 10 incidents per monitored hour. One incident can contain both drowsiness and phone use while contributing one to the overall incident count. If the total time with any detected behavior is 20 seconds, show approximately 2.8% of monitored time.

| Requirement | Screen IDs to review |
| --- | --- |
| FR-01 Public account access and recovery | P01–P06 |
| FR-02 Driver data isolation | P07–P08, D05–D11, D18, D23–D26 |
| FR-03 Profile and settings | D19–D22 |
| FR-04 Readiness and session lifecycle | D02–D06 |
| FR-05 Observation state | D02–D03 |
| FR-06 Unreliable observation | D03, D05, D07 |
| FR-07 Warning and explanation | D03, D07–D08 |
| FR-08 Offline monitoring and sync | D03, D05–D06, D10 |
| FR-09 Emergency entry and cancellation | D02–D04 |
| FR-10 Contact alerts and location | D04, D08, D21, X01 |
| FR-11 Session observations | D05–D09 |
| FR-12 Consented clips | D02–D03, D10–D11, D20 |
| FR-13 Review, expiry, and deletion | P08, D07, D10–D11, D18, D22 |
| FR-14 Personal analytics | D01, D06–D09 |
| FR-15 Reproducible statistics | D14–D15 |
| FR-16 What-If | D12–D13 |
| FR-17 Controlled experiments | D14–D15 |
| FR-18 Published benchmark | D16, D18 |
| FR-19 Reports | D17–D18, D23–D24, X02 |
| FR-20 MCP | D23–D24, X02 |
| FR-21 Optional chat | D23, D25–D26 |
| FR-22 Administration | A01–A09, P07 |

| Journey | Prototype walkthrough |
| --- | --- |
| J1 First controlled session | Sign up, verify, accept conditions, deny then recover camera permission, decline or accept recording, monitor, see a warning, restore a lost camera view and resume, then end and open the summary. |
| J2 Private recovery, clips, and deletion | Queue a clip offline, interrupt the tab, and recover only after the same eligible account signs in. Open a clip from both library and incident, delete it, and return to the surviving incident metadata. Exercise expiry while transfer or playback is in progress. |
| J3 Supervised warning and contact alert | Set contact order and location consent, delegate while stationary, acknowledge a warning while the countdown runs, then cancel it. In a second outcome show acceptance, delivery, and unconfirmed evidence as distinct states. Exercise camera loss and fresh resume. Use a stationary or simulator fixture. |
| J4 Understand and compare | Keep an older ready session visible during newer sync, select an overlapping incident, switch period and behavior filters, compare several sessions, and inspect a withheld finding. Exercise zero, unavailable, low coverage, and changed versions. |
| J5 Simulate, study, and benchmark | Run a simulation without reference labels, reopen a versioned study, exercise withheld inference and disclosure suppression, and compare the meaning of those results with approved benchmark evidence. |
| J6 Author, review, and export a report | Grant authoring independently, request through the agent, open a validated report, export both formats, handle an expired link, and exercise withdrawal or grant loss during processing. |
| J7 Ask a temporary chat question | Link and consent to a qualified provider, ask a follow-up, handle an expired connection or allowance limit, and revoke sharing while a reply is pending. |
| J8 Operate RAFIQ and support an account | Invite Staff, enroll MFA, visit permission-scoped views, inspect stale telemetry and suppression, look up and suspend a driver with fresh verification, reinstate, and verify the audit entry. Exercise last-Owner protection and immediate access revocation. |

Walk the prototype with a keyboard, with enlarged text, and with screen-reader announcements. Check warning visibility with audio off and reduced motion enabled. Verify that list filters and timeline selections survive Back and that access revocation removes private content immediately. Use known analytics and operations fixtures to check visible values, units, status, and the distinction between empty and unavailable.

[Experience journeys](EXPERIENCE.md#key-flows) · [PRD acceptance and release evidence](PRD.md#7-success-and-release-evidence) · [TRD measurable acceptance](TRD.md#8-measurable-acceptance-and-release-gates)

## Items awaiting approval or visual design

| Item | Design treatment until resolved |
| --- | --- |
| Warning, focus, and chart visuals | Use the shared visual tokens and accessibility requirements above. Design RAFIQ-specific warning emphasis, focus states, and dense chart treatments. Consult the Pen.dev chart reference when available to the designer. |
| Published support address | Use an explicit design placeholder on P07 until the approved support contact is supplied. |
| Release and independent qualification | Design pending and unavailable states for public signup and for each social provider, emergency channel, optional chat provider, and applicable behavior. Use release evidence to determine live availability. |
| Motion presentation and safety timing | Use stationary or simulator examples. The approved supervised procedure controls the motion frame. Treat D04 timings as controlled-test starting values. |
| Studio export | Design the eligibility and unavailable states. Supply file label and format after approval. |

[Experience visual handoff](EXPERIENCE.md#qualification-and-visual-handoff) · [API open decisions](API.md#18-open-questions-and-decisions-requiring-approval) · [PRD release gates](PRD.md#8-planning-decisions-and-release-gates)
