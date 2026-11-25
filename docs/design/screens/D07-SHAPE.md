# D07 Session Detail — approved Pen.dev handoff

The user selected **A · Full-width timeline with inline evidence** and asked to use all suitable components. Use the full RAFIQ review set described below. The design defaults are named zoom and range buttons, a brief selection accent, and exact data values that appear immediately. The external examples support the visual and interaction treatment. The component set can use native controls, HTML, SVG and CSS within RAFIQ. [Layout and component research](D07-COMPONENT-RESEARCH.md)

## Purpose and routes

Give the signed-in driver a private review of one completed session. They should be able to judge the quality of observation, locate a behavior, warning or recorded Emergency Mode event, and read its supporting evidence. Enter from D01, D05, D06 or an authorized session link. D01 may preselect a particular occurrence. **Personal Overview** opens D09. Show **What-If** when the specific session qualifies and open D12 with that source selected. **Start session** retains its private navigation role and opens D02. [D07 screen specification](../../SCREENS.md#d07-session-detail)

Back restores the originating review or history context where authorized. Restore D01's timeline range and focus or D06's page, scroll position and row. Offer **Back to Sessions** for direct entry. D08 opens in D07. When **Open clip** leads to D11, restore D07's range, selected occurrence, scroll and focus on Back if access still holds. [Shared navigation rules](../../SCREENS.md#shared-design-rules) · [Sessions handoff](D06-SHAPE.md)

## Composition and tokens

1. Reuse the private shell, with **Sessions** current. Keep the nav order **Dashboard, Sessions, Clips, Analysis, Reports, Settings** and retain the distinct **Start session** action.
2. Put **Session Detail** and the review destinations in the header. Show the local session date, start and end, displayed time zone, review status, and relevant catalog, model and warning-policy versions. Include the local end date when different. Show **Interrupted** alongside **Ready** when both apply. Put known changes in versions that affect interpretation near the affected results.
3. Place the five KPI cards in one strip when they fit. Follow with the full-width timeline, the selected D08 evidence panel directly beneath it when open, and the chronological event list. Below the list, put the behavior breakdown and detection duration distribution side by side when their labels, scales and exact values fit. Place **Delete session** in the secondary session-actions area below the review.
4. At narrow widths and high browser zoom, wrap metadata and navigation actions, reduce KPI columns in reading order, and stack the analysis panels. Keep the timeline controls and exact-value views within reach. Allow local horizontal scrolling for wide plots or tables in an identified region. Draw the main desktop at 1440 px, a 390 px reflow reference and a 320 CSS px zoom/reflow sample. Check use at 200% browser zoom during implementation.

Use **D01 · Ready review · desktop** (`v2yld`), **D01 · Ready review · narrow** (`bhsYb`) and **D01 · Review controls and alternate data** (`NjEkM`) as the visual baseline. Use D06 desktop (`m14mRu`) for the active Sessions treatment. Start from D01's 76 px navigation, 48 px desktop gutters and 20 px narrow gutters. Match Space Grotesk as the documented Mori substitute. Use `colors.canvas` / `$canvas` (#0e100f), `colors.ink` / `$ink` (#fffce1), and `colors.accent-stone` (#bbbaa6) for secondary text. Start from `spacing.sm` (8 px) within a label group, `spacing.md` (16 px) for panel padding and card gaps, `spacing.xl` (24 px) between sections, and `rounded.md` for data panels. Match the existing flat dividers, icon style, outline controls and focus treatment. Pair semantic accents with labels, symbols or patterns. [RAFIQ Pen design](<../../../Pen Design/RAFIQ.pen>) · [Design tokens](../../DESIGN.md) · [D01 handoff](D01-SHAPE.md)

## Full-session KPIs

| Order | Card | Display |
| --- | --- | --- |
| 1 | Monitored time | Elapsed monitored time, excluding deliberate pauses and including observation-loss pauses. |
| 2 | Incidents | Distinct incidents and incidents per monitored hour. Each incident counts once, including incidents with multiple behaviors. |
| 3 | Time with detected behavior | Total usable time with at least one detected behavior and its percentage of monitored time. Count overlapping time once. |
| 4 | Observation coverage | Usable-feed time, monitored-time denominator and percentage. Show **Low coverage** when the unrounded result is below 90%. Use the authoritative `belowTarget` value where supplied. Keep the label readable if the displayed percentage rounds to 90%. |
| 5 | Warnings | Distinct issued warnings. Count a combined warning once. |

Keep the cards and lower charts labeled **Full session**. Present fixed values and clear units. Use tabular figures where supported, expose durations to the API's available precision, and provide denominator inputs alongside derived percentages and rates. Use the authorized R results returned by FastAPI. Keep the same analytics scope during timeline zoom, pan, selection and panel navigation. [Analytics calculations](../../TRD.md#51-personal-dashboard-fr-14)

## Timeline and inline evidence

- Label the shared axis **Elapsed time since session start**. Keep pauses at their elapsed positions. Draw one observation lane, a row per detected behavior, and chronologically aligned event markers. Show usable time with no detections, deliberate pauses and recorded observation loss with different patterns and labels. Show per-class unavailable observation when the feed is usable but the relevant cues are unavailable. Label a missing record only where the source establishes that gap. A loading or failed window uses its own status.
- Use separate shapes and text for incident, warning and Emergency Mode markers. At full scale, a dense group can show its member count and expose the ordered members. Zoom reveals separate occurrences when space allows. Preserve each underlying ID and original time. Clip interval marks at the viewport boundary and preserve exact start, end and duration in the readout and interval data table. Keep emergency evidence read-only here and use recorded outcome names such as **Canceled**, **Withheld**, **Accepted**, **Delivered**, **Failed** and **Unconfirmed** as applicable.
- Show the visible start and end near **Zoom in**, **Zoom out**, **Reset zoom**, **Earlier** and **Later**. Start with the full-session domain. Zoom around the selected occurrence when visible, otherwise around the current midpoint. Clamp the result to the session bounds. Earlier and Later move the same-sized window by a predictable step. Reset restores the overview. Show clear endpoint states and retain authorized unaffected results during a window fetch. Announce the committed range once. Keep the buttons operable by pointer and keyboard.
- Under the timeline and its evidence slot, show a chronological list of the visible range's incidents, warnings and Emergency Mode entries. Each row gives exact elapsed time, type and recorded label, plus local time where helpful. Use a deterministic order for ties and retain every member of an overview group. Give the keyboard one entry into the interactive plot, arrow navigation among its marks, and Enter/Space activation. The event list offers equivalent actions. Use a labeled table for observation intervals and detection bounds.
- A marker or row selects the same occurrence and opens D08 directly below the plot. Mark and retain focus on the triggering occurrence and provide **Read selected details** and **Close** controls. The evidence heading identifies the selected time and event. An authorized event link opens the containing range and focuses the corresponding marker or row. If the driver moves the visible range away from the event, keep the selected time in the panel and offer **Back to selected time**. D08 supplies event evidence and eligible media actions. [D08 requirements](../../SCREENS.md#d08-incident-and-alert-details) · [Experience accessibility](../../EXPERIENCE.md#accessibility-floor)

## Analysis panels and components

| Component | Pen and interaction specification |
| --- | --- |
| Metric card and scope header | Reuse D01 card geometry and content order. Provide slots for label, exact value, secondary measure, unit, denominator, scope and availability. |
| Behavior breakdown | Horizontal bars on a common zero baseline for the current measure. Keep a stable behavior order, exact values and units beside the bars, and class-level coverage where supplied. **Count** represents matching constituent detection records. **Duration** represents each behavior's usable-time union. Use separately labeled scales. Show both metrics and their availability in the data table. |
| Measure selector | A labeled native radio group styled as **Count / Duration** segments, initially Count. Tab enters the group and arrows change the selection. Update the selected state, axis and values together. Keep focus and selection visually distinct. |
| Individual durations | For up to 30 matching detections, use a dot or strip plot grouped by behavior on a seconds axis. Show `n`, exact duration, and available descriptive statistics with their units and sample sizes. Place coincident samples off the time axis or show multiplicity while preserving each sample in the data view. |
| Binned duration distribution | For 31+ detections, display the server's per-behavior counts for **0–<2 s**, **2–<5 s**, **5–<10 s**, **10–<30 s**, and **30 s or longer**. Use ordered equal-width categories and a shared integer count scale. Use small multiples if needed to keep behavior labels and counts readable. Show matching `n`. The table reports the same ranges, counts and availability. |
| Exact-value readout | Hover and keyboard focus show a supplemental tooltip. Escape dismisses it and hovering the tooltip keeps it visible. Click, tap or keyboard activation gives a persistent inline readout where useful. Show behavior and exact duration for a point, or behavior, range, count and sample size for a bin. Provide a keyboard-accessible exact-value table independently. |
| Standard controls | Reuse links, buttons, ordered event list, table and data disclosures, inline status and Retry, and the named destructive confirmation dialog. Use a visible focus ring and reserve accents for selection and meaning. |

Share metric cards, scope labels, timeline, event selection and the breakdown and distribution views with D01. D01 activates an occurrence by routing to D07. D07 displays inline evidence. D09 reuses the metric card slots, measure selector, horizontal bar rows, exact-value readout and availability patterns. D09 uses its own period filters, metric labels, denominators and time axes. [D01 review components](D01-SHAPE.md) · [D09 requirements](../../SCREENS.md#d09-personal-overview)

## States and deletion

| State | Required presentation |
| --- | --- |
| Loading, syncing, processing | Still placeholders in the affected region and a single status announcement. Keep any authorized session context available. Offer **View session status** to D05 where appropriate. |
| Usable observation and confirmed zero | Show a numeric zero with its unit and usable context. For zero confirmed detections, retain the timeline and display **No detections recorded during usable observation** and `n = 0` in the distribution. |
| Class unavailable | Show **Unavailable** and the reason when known, with a textual row and no quantitative mark. Keep other usable classes visible. |
| No usable observations | With positive monitored exposure and confirmed complete records, show `0%` measured coverage with usable time and denominator. Label **No usable observations**. Preserve independent evidence and returned metric availability. |
| No monitored exposure | Show `0` monitored time where known and **Unavailable · No monitored exposure** for ratios and rates with zero denominators. |
| Missing data, unconfirmed outcome or missing clip | Label the specific missing or unconfirmed evidence where authorized. Preserve independent timeline, metrics, incident and warning details when available. |
| Partial or retryable failure | Put **Retry** in the affected region. Preserve independent authorized evidence and the current range. Label the scope and status of any prior result shown during recovery. |
| Eligibility lost | Clear private results, selection and stored return context. Use P07 for a restricted account and P08 for an unavailable protected link where applicable. |
| Delete session | The confirmation identifies the session by date, time and zone, and explains the effect on incidents, clips, dependent hosted reports and downloaded copies. Show counts only if authorized. Show pending and an inline retryable failure where eligible. Announce confirmed **Session deleted** and return to D06, focusing the nearest surviving row or Sessions heading. |

The deletion dialog uses a visible title, contained keyboard focus, Escape when safe, and return focus on dismissal. Cover named regions, heading order, skip link, predictable focus order, accessible names, non-color cues and contrast in every state. [Experience accessibility](../../EXPERIENCE.md#accessibility-floor) · [Deletion and retention](../../TRD.md#2-session-recording-and-offline-contracts)

## Motion and reference sources

| Trigger | Visual storyboard | Reduced motion |
| --- | --- | --- |
| Event, measure or bin selection | The selected content, values and focus indicator change immediately. A 150–180 ms accent opacity transition settles around the new selection. | Draw the same final selected and focused treatments immediately. |
| Zoom or pan | Show a localized retrieval state if needed. Plot the committed range with correct bounds and marks together. | Same immediate range change. |
| Load, refresh, open D08, warning or emergency state | Show values, geometry and status at their final positions. | Same immediate presentation. |

The adoption pattern is RAFIQ's existing controls and a CSS selection accent. Use C01 for the accent reference, C04 for dense marker grouping, C05 for horizontal bars, C06 for changing the active measure and category readout, C07 for visible selection, C09 for anchored hover/focus feedback, and C11 for the selected-bin readout. The exact code, licenses and trade-offs are in the [component research table](D07-COMPONENT-RESEARCH.md#component-research). [Motion component](https://motion.dev/docs/react-motion-component) · [Grouped timeline](https://codepen.io/ghaliano/pen/vXKVPM?anon=true&view=pen) · [Horizontal bar and interactive bar demos](https://ui.shadcn.com/charts/bar) · [Selection background](https://motion-primitives.com/docs/animated-background) · [Tooltip](https://animate-ui.com/docs/primitives/base-ui/tooltip) · [Histogram readout](https://codepen.io/lymons/pen/rNbWEEd?anon=true&view=pen)

## Pen deliverables and frontend acceptance

- **Pen frames.** Draw desktop overview, selected D08 at a zoomed timestamp, narrow reflow, Count and Duration, individual plot at 30 and binned plot at 31, keyboard focus and exact-value tables, all observation/availability states, and delete dialog progress, failure and completion. Show the start and rest of the selection accent with the same geometry. Use sample data in editable layers. Keep the D08 evidence slot within D07.
- **Shared fixture.** Use the D01 example with 13 minutes elapsed, a deliberate pause at 05:00–06:00, and observation loss at 07:00–09:00. The five KPIs show 12 monitored minutes, two incidents and 10 incidents/hour, 20 seconds with detected behavior (about 2.8%), 10 of 12 usable minutes (83.3% and **Low coverage**), and one combined warning. Show the recorded alert canceled before sending around 02:11. At overview scale group close entries, then reveal separate markers in the zoomed view. [D01 fixture](D01-SHAPE.md)
- **Frontend verification.** Check distinct incident/warning counting, overlap union, the unrounded 90% threshold, fixed bin boundaries at 2, 5, 10 and 30 seconds, and the 30/31 mode switch against authorized results. Verify that zoom and pan leave whole-session values in place. Exercise keyboard and pointer parity, exact-value tables, focus and Back restoration, status announcements, access revocation, reduced motion, dense markers, high zoom and confirmed deletion. Pen shows the visual states and the browser verifies their runtime behavior.

## Build dependencies to confirm

Confirm an explicit usable-time numerator or a lossless derivation from the coverage payload. Confirm which typed reasons establish unavailable classes, confirmed observation loss and missing observation records. Clarify the API's maximum timeline window, full-session overview and event-list assembly across bounded reads, and stable authorized occurrence keys for deep links. Confirm the per-session What-If eligibility lookup when the source is outside the current result page. Session deletion confirms with `204`. Any preflight dependency counts need their own authorized data. Use these fields when the contract supplies them. [API operations and schemas](../../API.md#7-detailed-endpoint--operation-specifications)
