# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Drivers** are adults using a laptop with a built-in camera in controlled sessions. The initial audience already uses monitoring tools. Drivers need to know when monitoring is active, understand what triggered a warning, and review their own observations afterward.
- **Supervisors** are present during approved vehicle testing. The driver can authorize them while stationary to acknowledge warnings, cancel a pending contact alert, or pause monitoring on the driver’s device.
- **Emergency contacts** receive eligible alerts directly by email or WhatsApp. They can receive and read the alert without a RAFIQ account.
- **RAFIQ Owners and Staff** use a separate, invitation-only dashboard for service health, adoption, and narrowly scoped account support.

## Product Purpose

RAFIQ uses a laptop camera to monitor visible driver behavior on-device. It explains qualifying warnings with the observed behavior, cue, and duration. After a session, drivers can review a private record of incidents, warnings, and observation coverage. The core journey succeeds when a first-time driver can register, verify their email, check the camera, complete a controlled session, and reach the summary unassisted. See the [approved PRD](docs/PRD.md#7-success-and-release-evidence).

## Positioning

RAFIQ connects a warning to evidence the driver can inspect and analyze. A driver can revisit the timeline, compare comparable sessions or periods, and use What-If to see how supported threshold changes would affect recorded results. Analyses expose the source, policy version, coverage, and limits needed to interpret the result. An authorized MCP agent can turn approved evidence into a report that RAFIQ validates before the driver reviews and exports it.

## Operating Context

- The planned public release is free, English-language, and self-service for adults after release approval. The stationary campus demonstration on 15 December 2026 is a separate milestone. Ali Sameh owns release sign-off.
- The monitoring qualification baseline is Chrome on Windows 11 with a built-in laptop camera. Drivers set up and use controls while stationary. Vehicle motion is limited to an approved supervised procedure. Mobile monitoring is outside release scope.
- A configured session must continue local monitoring and warnings during a 30-minute network outage while the monitoring tab remains open. Interrupted monitoring resumes manually after a usable camera view returns. See the [technical requirements](docs/TRD.md#2-session-recording-and-offline-contracts).

## Capabilities and Constraints

- The initial behavior catalog covers visible cues for drowsiness, distraction, phone use, eating, and drinking. Each behavior requires qualification. When the camera cannot reliably observe a cue, the experience explains the limitation. When the view is unusable, monitoring pauses.
- Live camera processing stays on-device. Hosted review uses driver-owned records and separately consented, bounded video-only incident clips. Drivers can decline clip recording and still monitor. Access, retention, deletion, and revocation apply to records and connected tools.
- What-If uses eligible personal sessions and leaves live monitoring policy intact. Experiment Studio uses approved study inputs and privacy-checked aggregates. Benchmark publishes approved held-out results. Drivers review authorized agent-authored reports and can export them as PDF or Word.
- Emergency Mode is limited to qualifying sustained drowsiness during eligible supervised sessions. Email and WhatsApp activate independently after qualification. Provider acceptance and confirmed delivery are distinct outcomes.
- Compatible MCP clients receive separately scoped, revocable permissions. In-app chat is optional and requires provider qualification and first-use consent. Public signup can open independently of chat.
- Public activation depends on release evidence for the core journey, device and detection performance, privacy, accessibility, capacity, recovery, analysis, reporting, MCP, and administration. Hosted services must qualify at zero project cost. See the [release gates](docs/PRD.md#8-planning-decisions-and-release-gates) and [system architecture](docs/ARCHITECTURE.md).

## Brand Commitments

- Use the name RAFIQ. Keep product language direct and grounded in what the camera observed, what the driver can do next, and what the evidence supports. See the [voice and tone guidance](docs/EXPERIENCE.md#voice-and-tone).
- [DESIGN.md](docs/DESIGN.md) is the sole authority for visual identity, including colors, typography, spacing, components, and brand guidelines.

## Evidence on Hand

- The [PRD](docs/PRD.md), [TRD](docs/TRD.md), [architecture](docs/ARCHITECTURE.md), [experience specification](docs/EXPERIENCE.md), and [screen specification](docs/SCREENS.md) describe the approved requirements, proposed implementation, and qualification gates. The screen specification defines the [public entry](docs/SCREENS.md#p01-public-entry), including the pending-signup state.
- The [Pen design](Pen%20Design/RAFIQ.pen) holds design boards and motion components. Existing brand assets include the [static RAFIQ wordmark](Pen%20Design/brand/rafiq-static.svg), [favicon](Pen%20Design/brand/rafiq-favicon.svg), and [logo motion prototype](Pen%20Design/brand/rafiq-prototype.html). These are design artifacts. Feature availability and performance claims require approved release evidence.

## Product Principles

1. Make monitoring state, warnings, and recovery actions understandable while the session is happening.
2. Give the driver control over recording, private review, retention actions, and external access.
3. Make comparisons reproducible and show the coverage, uncertainty, and scope that affect interpretation.
4. Treat each feature’s operating conditions and qualification as part of the product experience.

## Accessibility & Inclusion

Support keyboard and screen-reader use for setup and review, with visible focus and reflow under browser zoom. Pair warning color with readable text and a visible non-color cue. Keep warnings usable with sound disabled and reduced motion enabled. Give charts and timelines accessible values and equivalent tables or event lists. Decorative motion respects reduced-motion preferences. See the [accessibility floor](docs/EXPERIENCE.md#accessibility-floor).
