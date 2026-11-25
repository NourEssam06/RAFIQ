# D09 Personal Overview

**Status** · Implemented in Pen.dev. **Mode** · Operate.

The signed-in driver opens Personal Overview after monitoring to see what RAFIQ recorded across sessions and periods, and how much observation supports each result. In the first viewport, the driver should be able to identify the applied scope, see the five KPIs, and start reading the period trend. From any rate or finding, the driver should be able to recover the underlying exposure, coverage and relevant version context. The discovery choices were **period trend after the KPIs** and **brief selector and focus transitions**. [D09 requirements](../../SCREENS.md#d09-personal-overview) · [Analytics calculations](../../TRD.md#51-personal-dashboard-fr-14)

## Layout concepts

| | A · Period review with inline comparison **(recommended)** | B · Period review with an evidence rail |
| --- | --- | --- |
| First viewport | Private nav, title and scope, five KPIs, then a full-width trend. The trend header includes a link to the comparison section. | Same nav, scope and KPIs. Trend leads a wide column. A narrow rail holds findings and a shortcut to compare sessions. |
| Reading order | Trend and exact values → session comparison → behavior ranking and overlap → monitored-time bands → findings. A short section-link row makes findings and comparison reachable from the top. | Trend → session comparison → behavior ranking and overlap → monitored-time bands in the main column. Findings stay visible alongside the trend at wide widths and follow the trend in narrow reading order. |
| Trade-off | Gives the trend and four-session comparison maximum width and matches D01/D07’s full-width chart and inline evidence. Findings sit farther down. | Gives findings earlier visibility. The rail reduces chart space and needs a deliberate stack at laptop widths and zoom. Four-session comparison can span the full content width below. |

Use the private shell and existing navigation order. Keep **Personal Overview** one action from Dashboard and linked from D07. Use Dashboard’s product context for this overview. Offer **Back to Sessions** from the comparison and **Open session detail** on each selected session. Open D08 through D07 only for a confirmed, authorized incident reference, and use D07 as the evidence destination when only a session ID is available. Back restores the authorized applied scope, selection, scroll position and focus. Preserve the live workspace’s navigation priority during monitoring. [Shared screen rules](../../SCREENS.md#shared-design-rules) · [D07 handoff](D07-SHAPE.md)

## Scope and request states

- Default to **Last 30 days**. Offer **Last 7 days**, **All available history** and **Custom range**, with inclusive **From** and **Through** dates. Show the displayed time zone next to the scope, and show concrete dates once resolved. Assign each entire session to its local start date, including sessions that cross midnight. Surface invalid or incomplete ranges beside the relevant fields. Provide typed date entry and allow a single-day range.
- Offer session and behavior filters with an applied summary. Show draft edits in the controls and commit them together with **Apply**. **Clear filters** restores the default period and all eligible sessions and behaviors. Selecting multiple behaviors matches any selected behavior. It changes matching records and behavior results while preserving overall monitored exposure and coverage for the same sessions.
- Roll up only completed sessions with ready analytics. Show separate **Syncing** and **Unavailable** counts for the scope. Explain pending processing where the source distinguishes it. Optional missing, expired or pending clips leave ready analytics eligible.
- During recalculation show the requested scope and, if authorized previous figures remain visible, place their complete applied scope on the result region. Apply the new labels and values together when ready. Ignore stale responses and preserve the user’s inputs for a scoped Retry. Remove affected figures and destinations when access or source eligibility changes. [Experience states](../../EXPERIENCE.md#session-detail-and-personal-overview) · [Overview API](../../API.md)

## Five KPI cards

| Card | What the driver sees |
| --- | --- |
| Completed sessions | Eligible completed session count and total monitored hours for those sessions. Deliberate pauses are excluded from monitored time. Observation-loss pauses are included. |
| Incidents | Distinct incident count and incidents per monitored hour. Each incident counts once, including an incident with multiple matching behaviors. |
| Time with detected behavior | Observed duration and share of monitored time. Take the union of usable matching detection intervals within each session across behaviors before summing, so concurrent observations count once. |
| Observation coverage | Usable-feed time, total monitored time and usable-feed percentage. Show **Low coverage** below 90% using the unrounded value or the authoritative flag. Class-level coverage stays with its behavior where supplied. |
| Warnings | Distinct issued warning count and warnings per monitored hour. Each combined warning counts once. |

Use pooled counts over pooled monitored hours and coverage over pooled monitored exposure. Keep numerators, denominators, exact units and contributing sample sizes in the visible annotation or exact-value view. Use the authorized values and availability returned by FastAPI from R. An available zero is a value. Zero exposure, no usable observation, unavailable classes, incomplete results and suppressed results have distinct labels and supporting reasons where supplied. [KPI and availability contracts](../../TRD.md#51-personal-dashboard-fr-14)

## Analysis sections

### Period trend

- Use one line plot at a time. Start with **Incidents per monitored hour** and offer **Warnings per monitored hour** and **Share of time with detected behavior** in the same labeled single-select group. Switch the label, scale, unit, readout and table together, preserving the applied analytics scope. Use daily buckets through 30 inclusive calendar days. Use local Monday-starting weeks for longer ranges, with partial first or last weeks labeled by covered dates.
- Plot an isolated point when only one bucket is usable. Leave breaks for unusable buckets. An observed zero has a point at zero. Use a linear connection between adjacent comparable, available buckets. Show available figures at known version boundaries and break the line when comparability is absent or unverified for the metric. Display relevant catalog, model and warning-policy changes with text. When the API only gives a scope-level version list, show the mixed-version notice and exact data without inventing a boundary.
- Pointer hover and keyboard inspection expose the same selected period, value and units, monitored exposure, coverage and available sample size. Click, tap or Enter pins a readout. Provide an always reachable **View trend data** disclosure and labeled table including every bucket’s status. Chart inspection leaves the applied scope intact.

### Compare sessions

- The proposed API-aligned design uses the **Sessions** scope picker for the comparison selection. Show ready, in-range sessions by local start date and time with status. With no selection, use all eligible sessions and invite the driver to choose two to four. A one-session draft shows “Choose at least 2 sessions to compare” and offers **Open session detail** where eligible. A fourth selection reaches the maximum. Keep removal available and explain that removing a session makes room for another. When a draft date change makes a selection invalid, show the affected session and offer to remove it before Apply.
- For two to four applied sessions, show aligned session columns with stable order and consistent metrics. Each header includes local date and start time, monitored time, coverage, relevant versions and its D07 link. Use the five KPI definitions and align each behavior’s count, duration and observable-session share where supplied. Repeat monitored time and coverage in the rate readout. Preserve available values for low coverage and version differences, label the affected rows and use neutral styling for those comparisons.
- Use a flat comparison table at narrow widths. The Pen layout shows two session columns at a time, with stable metric labels, repeated session headings and **Next two sessions** or **Previous two sessions**. Mark a deleted or no-longer-eligible selection and give a way to replace it. [Selection scope and provenance](#questions-for-implementation)

### Behavior ranking and overlap

- Reuse D07’s labeled horizontal bars and add **Share of eligible sessions** to **Detection count** and **Duration**. Sort by the selected available measure in descending order, with a predictable tie order. Use a common zero baseline, exact values and units. Count matching constituent detections. Show usable within-behavior union duration. For share show sessions with a recorded detection divided by sessions where that enabled behavior had usable observation, e.g. **2 of 3 observable sessions (66.7%)**. A class with an empty denominator is unavailable. Keep all measures readable in the data table when the chart changes.
- Use a two-header overlap matrix with one triangular half and a labeled diagonal. A cell shows the distinct incident count with positive-duration overlap while both behaviors were observable, plus the number of jointly observable sessions. Count each qualifying incident once for that pair. A shared endpoint alone contributes zero. **0 overlaps · 3 jointly observable sessions** is a measured zero. **Unavailable · 0 jointly observable sessions** uses a distinct text and pattern. State that any shading encodes incident counts. Provide a narrow pair list with both behavior names, exact counts and eligibility. With fewer than two behaviors, explain the requirement and offer to adjust the filter.

### Time since monitoring began

Show ordered bars with a common zero baseline for incidents per monitored hour. Label the bands **0–<5**, **5–<15**, **15–<30**, **30–<60**, and **60+ monitored minutes**. For each band show the exact rate, pooled monitored minutes, coverage and count of sessions with positive exposure in that band. Assign each incident once by its start in cumulative monitored time. Deliberate pauses stop that clock and observation-loss pauses advance it. A band without exposure has an unavailable rate. Include all five bands and their reasons in the exact-value table. [Time-axis contract](../../TRD.md#51-personal-dashboard-fr-14)

### Findings

- Show validated recurring behaviors with their measure, figures and sample context. For a change finding show the selected and immediately preceding equal-length calendar windows, matching filters and time zone, values and relevant exposure and coverage. Use descriptive wording such as **Recorded incident rate**.
- Gate each change finding on both values being available, both windows having at least one eligible completed session, at least 15 monitored minutes, at least 90% overall observation coverage, and verified comparability for the metric. Use exact inputs when testing boundaries. When the prior value is zero, report the absolute change in the metric’s unit or percentage points for a share. Use relative change only when validated and the prior value allows it.
- Where a change is withheld, keep available figures and state the authorized reason, e.g. **Change unavailable · The prior period had less than 15 monitored minutes**. If both versions are documented but comparability is unverified, label that condition. When a bounded prior window cannot be established for **All available history**, use the explicit unavailable state returned by the service. [Period comparisons](../../TRD.md#51-personal-dashboard-fr-14)

## Components, motion and reflow

| Class | Components |
| --- | --- |
| Existing RAFIQ | D01 private shell, KPI card anatomy and review statuses. D06 session identity and status rows. D07 measure selector, horizontal bars, non-color evidence marks and exact-value disclosure. |
| Standard | Named links and buttons, form controls and validation, labeled checkboxes and radios, text date fields, disclosure, table, busy/status feedback and scoped Retry. |
| New RAFIQ | Applied scope summary, calendar trend/readout, aligned session comparison, pair matrix and narrow pair list, exposure-band rows, recurring and period-change findings with evidence. |
| Potential external references | Verified examples and selectable IDs for charts, selector motion, comparison cards, heatmaps and date range. [Component alternatives](D09-COMPONENT-RESEARCH.md) |

Use D01’s 76 px shell, 48 px desktop and 20 px narrow gutters as Pen references. Use Space Grotesk as the established Mori substitute, warm canvas and ink, secondary stone and restrained semantic accents. Use `spacing.sm` (8 px) within groups, `spacing.md` (16 px) for panels, `spacing.xl` (24 px) between sections, and `rounded.md` (8 px) for panel geometry. Match the existing focus rings, flat dividers and outlined controls. Draw a 1440 px desktop, a 390 px stacked state and a 320 CSS px reflow reference. At 200% zoom, wrap scope controls, stack KPIs and sections in reading order and keep page scrolling vertical. Confine necessary horizontal scrolling to named dense plots or tables. Test long behavior labels and localized dates, decimals and units. [RAFIQ Pen design](<../../../Pen Design/RAFIQ.pen>) · [Design tokens](../../DESIGN.md)

Use one predictable tab sequence from filters through results, with a skip link, visible focus, labeled chart controls and headers, and a polite announcement for each committed result or status. Keep one entry into an interactive plot, with arrow keys to inspect buckets and an equivalent table for exact values. Keep focus on the trigger during updates. A measure change may move an accent or fade its emphasis over **150–180 ms**. A focus or selection accent can fade in while the focus ring and figures appear immediately. Use static final states for reduced motion and as a selectable treatment for all drivers. Keep axes, values, tooltips and accessible focus stable during transitions.

## State boards and acceptance

| Pen board or variant | Demonstrates |
| --- | --- |
| Ready desktop and reflow | All five KPIs, a gap and an observed zero, four compared sessions, behavior ranking, a measured-zero pair and an unavailable pair, five bands and one withheld finding. The comparison state board also illustrates two and three selected sessions. |
| Scope interaction | Draft custom range, validation, selection at 0/1/2/4 sessions, focused control and recalculation with the previous scope labeled. |
| No ready result | First use with **Start session**, filtered-empty with **Clear filters**, pending or unavailable counts with a Sessions destination, and initial loading with a static skeleton. |
| Partial or changed result | Low coverage, missing class observation, changed versions, expired or removed input, scoped retry, protected access loss and comparison withheld with available values. |
| Motion frames | Initial and settled selector/focus states, a reduced-motion settled frame and no delayed evidence. |

Use synthetic records in Pen. One coherent KPI fixture has **4 completed sessions, 120 monitored minutes, 112 usable minutes (93.3%), 6 incidents (3.0/h), 6 minutes with detected behavior (5.0%), and 4 warnings (2.0/h)**. Check pooled rates with unequal session lengths, deduplication and interval union, OR filters with invariant exposure, local midnight and the 30/31-day boundary, Monday grouping, pair joint eligibility, starts exactly at band boundaries, 14:59 versus 15:00 exposure and just below versus exactly 90% coverage. Test a zero prior value and a version-based withholding. Verify 2- and 4-session alignment, exact-value parity, missing clips, keyboard return paths, reflow and reduced motion. Pen depicts these visual states. Browser code owns the actual filter and polling behavior, plot navigation, data table, media authorization, announcements and focus restoration. [FR-14 acceptance](../../PRD.md#55-personal-analytics-simulation-and-controlled-experiments)

## Questions for implementation

- Confirm whether the overview’s `scope.sessionIds` intentionally covers both the aggregate scope filter and the compared sessions. The request exposes a single array capped at four, the resolved scope constrains it to two through four if present, and the response provides `selected`. Independent comparison while retaining all-session aggregates would need an explicit contract. Confirm how historical-period matching should apply a concrete session-ID filter.
- Confirm how the service resolves a prior window for All available history and how the frontend gets its dates, period-level exposure and coverage, affected metric comparability and version boundaries. The documented response has current period bounds, scope-level `sessionVersions`, individual trend metrics and a finding reason. It does not expose an explicit prior-window object or an authoritative version marker per trend point. Until supplied, use available values and the returned reasons, with scope-level version notes and no unsupported connected trend across mixed versions.
- Confirm status detail for first use versus a filtered-empty result, syncing versus processing, and conditionally available evidence links. The overview status groups pending records and does not give incident IDs in trend, overlap or finding rows. Resolve session names and direct links from current authorized session metadata and incident references. [API operation and schemas](../../API.md)

## Pen.dev handoff

The user confirmed period-trend priority and brief selector and focus feedback in discovery, then requested Pen.dev implementation with suitable components. The implementation uses **Layout A** and the RAFIQ treatments **C02, C03, C06, C08, C11 and C13**. [Component research](D09-COMPONENT-RESEARCH.md)

| Frame | Pen ID |
| --- | --- |
| Personal Overview · desktop 1440 | `DQsAR` |
| Personal Overview · 390 px | `h8lXG` |
| Personal Overview · 320 px | `Ll52j` |
| Scope, session selection and recalculation | `SVx5x` |
| Availability and scoped recovery | `uEfxP` |
| Selector, keyboard focus and reduced motion | `Z00dpr` |
| Trend exact values, daily and weekly | `D9wHnk` |
| Applied comparisons, narrow second pair and prior-zero finding | `dps7J` |

The frames contain synthetic evidence. The selector states show the start, settled and reduced-motion appearances. The browser implementation supplies live analytics, navigation, keyboard behavior and motion. [RAFIQ Pen design](<../../../Pen Design/RAFIQ.pen>)
