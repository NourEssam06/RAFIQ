# D01 Dashboard

## Approved design

The driver lands here after eligible sign-in. Lead with the latest completed session with ready analytics. The driver should be able to identify the session, assess observation coverage, and open the evidence behind a timeline event. **Start session** opens D02 readiness. **Personal Overview** opens D09 in one action.

Approved direction is the full-width timeline with its event list underneath, static analytic values, and a brief selection highlight. Use standard controls and the shared RAFIQ review components. Selecting a timeline marker or event row opens D07 with D08 focused at the selected timestamp.

## Frame structure

1. Use the private navigation order **Dashboard, Sessions, Clips, Analysis, Reports, Settings**. Show Dashboard as current and give **Start session** a distinct primary treatment.
2. In the page header, keep **Start session** and **Personal Overview** visible. Identify the displayed session with its date, start and end times, displayed time zone, ready status, and relevant catalog, model, and warning-policy versions.
3. When applicable, place the newer session’s date and status in a separate row beside the review header. Keep the current session identity with its analytics.
4. Show the five KPI cards in the D07 order below.
5. Give the elapsed-time timeline the full review width. Follow it with an ordered event list and the behavior breakdown and duration distribution. Place the lower charts side by side when labels, units, and exact values fit.

| KPI | Display rule |
| --- | --- |
| Monitored time | Exclude deliberate pauses and include observation-loss pauses. |
| Incidents | Show distinct incidents and incidents per monitored hour. An incident with overlapping behaviors contributes once. |
| Time with detected behavior | Show total usable time with one or more detected behaviors and its share of monitored time. Count overlap once. |
| Observation coverage | Show usable time, monitored time, and the percentage. Flag **Low coverage** if the unrounded value is below 90%. |
| Warnings | Show distinct issued warnings. A combined warning contributes once. |

Use the documented fixture with 12 monitored minutes, 10 usable minutes, 83.3% coverage, two incidents at 10 per monitored hour, and 20 seconds with detected behavior at about 2.8%. The Pen sample spans 13 elapsed minutes, including the deliberate pause at 05:00–06:00 and observation loss at 07:00–09:00. The simulated supervised session has one combined warning and a contact alert canceled at 02:11 before sending. The full-range marker groups the nearby emergency entries and the ordered list shows each entry separately. The zoomed example shows both markers. Treat the illustrated times, versions, and events as sample data. [Fixture and screen walkthrough](../../SCREENS.md#requirements-and-prototype-walkthroughs)

## Analytics and navigation

- Label the timeline axis **Elapsed time since session start**. Give detected behaviors separate lanes. On the observation lane, distinguish deliberate pauses, observation loss, and usable time without detections. Give warnings and recorded Emergency Mode events identifiable markers and text equivalents.
- Show **Zoom in**, **Zoom out**, **Reset zoom**, visible range boundaries, and keyboard-operable range movement. Zoom changes the timeline alone. Analysis KPIs and lower charts stay scoped to the full session.
- Selecting an event in the chart or ordered list opens D07 and D08 at the same session and occurrence. Browser Back restores the previous Dashboard review, timeline range, scroll position, and focus when the target is still authorized. D07 holds eligible What-If and session deletion actions.
- Show horizontal behavior bars with **Count / Duration**, exact units and values, and per-behavior coverage where supplied. For at most 30 matching detections, show individual durations grouped by behavior. Above 30, show counts in **0–<2 s**, **2–<5 s**, **5–<10 s**, **10–<30 s**, and **30 s or longer**. Show the sample size in both modes and available descriptive statistics.
- Distinguish a confirmed zero with usable observation, an unavailable behavior class, no usable observations, and zero exposure. A missing optional clip leaves independent eligible analytics visible.

## State matrix

| State | Content and actions |
| --- | --- |
| First use | “No sessions yet.” Give **Start session** primary emphasis. Keep **Personal Overview** visible. |
| Initial retrieval | Keep the shell and actions visible. Reserve space for the session header, KPI strip, and timeline with geometry-matched static placeholders. Announce **Loading dashboard** once. |
| Sessions exist, required records syncing | Show the identified session and date, **Syncing session records**, and **View session status** to D05. |
| Sessions exist, analytics processing | Show the identified session and date, **Processing analytics**, and **View session status** to D05. |
| Ready | Show the identified session with all available analytics. |
| Ready with a newer syncing or processing session | Preserve the review and its controls. The separate dated status row links to D05. |
| Newer session becomes ready | The row offers **Open newer session**. Announce readiness once and preserve the current review and focus. A fresh Dashboard entry resolves the latest ready session. |
| Unavailable | Show a specific authorized reason where supplied and offer **View sessions** to D06. Use D05 for a specific session with a recoverable status. If the dashboard supplies only a page-level state, say “Session analytics are unavailable.” |
| Temporary failure | Offer **Retry**. Preserve any still-authorized review and keep the current session identity visible. |
| Access changes | Remove private results when access is lost. Use P07 for a restricted account and P08 for an unavailable protected session link. |

Dashboard state comes from the authorized `GET /api/v1/dashboard` projection and its `latestReady` and `newestPending` references. Resolve session analytics through the authorized session endpoint. The dashboard response has no unavailable reason or unavailable session reference. Detailed unavailable copy requires an authorized source. A pending session uses qualitative status text unless the service supplies reliable measurable progress. [API contract](../../API.md) · [Experience state patterns](../../EXPERIENCE.md#state-patterns)

## Components and tokens

- Reuse the existing RAFIQ brand mark and Pen Foundations and Controls styling. Shared primitives are links, buttons, status text with icons, a segmented selector, an ordered list, a data table, and a retry control. The specialized review components are the session header, five-card strip, elapsed-time timeline, event selection, behavior breakdown, duration plot, and availability treatments.
- Use DESIGN.md’s `colors.canvas`, `colors.ink`, and `colors.accent-stone` roles, with sparse semantic accents and a redundant shape or text cue. Use Mori where licensed or the documented Space Grotesk substitute. Use `spacing.sm` and `spacing.base` for compact internal gaps, `spacing.md` for panel padding and card gaps, and `spacing.xl` between major sections as a starting rhythm. Apply `rounded.md` to data panels and the established outlined treatment to secondary controls.
- Keep actual values and data marks static. A short selection treatment of approximately 150–200 ms can ease the highlight around the selected occurrence. Update values and labels as soon as the underlying state changes. Under reduced motion, apply the same highlight immediately. The approved design uses RAFIQ controls and has no external animation dependency.

## Pen and frontend acceptance

- Pen contains editable layout, state, and data layers. Use state variants to show full review, narrowed review, selected event, and the visible state changes. Stamp analytics samples as examples in the design annotation. The visual variants specify the behavior of routes, state updates, keyboard navigation, and announcements for the frontend implementation.
- At laptop width and browser zoom, keep the actions visible, wrap labels, preserve KPI reading order, and stack the charts. Any plot or wide table that needs horizontal overflow should use a labeled local scroll region. Check the frontend at 200% zoom and with a narrow reflow viewport.
- Give the frontend a skip link, landmarks, logical heading and tab order, visible focus, exact-value data tables, and keyboard-operable event entries. The state, units, sample size, version context, and coverage must remain understandable without color or animation. Announce each meaningful availability change once.
- Compare both chart modes to the same approved analytics scope. Verify the 30/31 boundary, zero and unavailable variants, semantic distinctions in the observation lane, independent timeline zoom, and linked event navigation and return. Verify pending to ready preserves focus and the active session until the driver opens the newer result.

In [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>), the desktop review frame is **D01 · Ready review · desktop** (`v2yld`, 1440 px). The 390 px reflow frame is **D01 · Ready review · narrow** (`bhsYb`). The **Review controls and alternate data** board (`NjEkM`) shows the Duration selection, 32-sample binned distribution, and zoomed keyboard-focus state. Separate full-width review frames cover readiness without a newer session and readiness with a newer result available. Compact variants show first use, initial loading, syncing, processing, unavailable analytics, and temporary failure.

[Screen specification](../../SCREENS.md) · [Experience and accessibility](../../EXPERIENCE.md#accessibility-floor) · [Design foundations](../../DESIGN.md) · [Technical analytics rules](../../TRD.md#51-personal-dashboard-fr-14)
