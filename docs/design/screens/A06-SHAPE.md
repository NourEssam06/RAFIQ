# A06 Adoption

**Direction · Layout A. Mode · Operate.** After admin sign-in and MFA, an Owner or Staff member with **View metrics** opens **Adoption** in the permission-scoped admin navigation. They read product uptake and where recent signups stop progressing, then inspect usage across the same calendar range. The dashboard presents whole-product aggregates. Navigation follows the current grant. [Screen requirements](../../SCREENS.md#a06-adoption) · [Admin workflows](../../EXPERIENCE.md#admin-workflows) · [Adoption rules](../../TRD.md#71-admin-dashboard-fr-22)

## Layout and components

1. **Admin shell and scope.** Follow A04 and A05 for navigation, gutters, focus, and flat panels. Set **Adoption** current. Place the applied range, one display time zone, and server **Data through** timestamp above the cards. Default to **Last 30 days** and offer **Last 7 days**, **All history**, and **Custom dates**.
2. **Five cards.** Reuse the **Review metric card** (`uw6Ef`) styling for **Signups**, **Verified accounts**, **Drivers completing a first session**, **Active drivers**, and **Completed sessions** in that order. Group the first three under **Signup cohort** and the last two under **Usage**, with exact values or clear states.
3. **Funnel and trends.** At wide desktop, place the three ordered funnel rows beside separate **Active drivers** and **Completed sessions** time series. Each chart has its own count axis and shares the date scale with the other. Reuse the **Exact-value readout** (`pmHUW`) and D09's **View trend data** pattern for keyboard and pointer inspection and the equivalent table.
4. **Reflow.** Preserve the cohort and activity grouping as cards wrap. Stack the analytical sections when their labels need more space. Verify 1440 px and 1024 px desktop, 200% zoom, and reflow at 320 CSS px. Let long card labels, dates, and status text wrap without page-wide horizontal scrolling.

Keep RAFIQ's existing type treatment, `colors.canvas`, `colors.ink`, `colors.accent-stone`, `rounded.md`, and the 8/16/24 px spacing steps. The selected design references are **A06-C01** RAFIQ metric cards, **A06-C03** custom labeled funnel rows, **A06-C05** disconnected line chart geometry, and **A06-C07** standard date controls. The Recharts example demonstrates gap treatment. The production package choice and pins follow the TRD. Values, chart geometry, and disclosure changes are immediate. [Visual tokens](../../DESIGN.md) · [Recharts gap example](https://recharts.github.io/en-US/examples/LineChartConnectNulls/) · [Recharts MIT license](https://github.com/recharts/recharts/blob/main/LICENSE) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

## Scope and calculations

| Result | Presentation |
| --- | --- |
| Signup cohort | Distinct drivers who signed up in the selected range. Count verification and the first completed session in order, before seven days elapse after each driver's signup. The first three cards match these funnel counts. Show **Cohort in progress** when the observation window is open. |
| Conversion | Show the server-released rate with its labeled denominator. The design example uses verified drivers ÷ signups, then drivers completing a first session ÷ verified drivers. A withheld or unavailable rate, numerator, or denominator, or a zero denominator, leaves the rate unreported. An approved zero numerator with a positive denominator can show 0% when the server releases the rate. |
| Active drivers | Count each qualifying driver once in the requested range and once per trend bucket. The exact range total requires an independently published distinct count. |
| Completed sessions | Count each completed session once at its recorded end after durable completion sync. Distinct-driver disclosure applies even when a driver contributed multiple sessions. |
| Trend buckets | Use calendar days through 30 days and local Monday-starting weeks for longer ranges in the displayed time zone. Label the bucket date or date span. Use straight segments between adjacent released observations and a gap at withheld, incomplete-without-value, or unavailable points. |

The API example includes available one-driver values and gives both conversions a count unit and null denominators. Resolve the production rate units and bases before wiring the display. Confirm the default display-zone policy and how the backend signals stale coverage. The fixtures use synthetic numbers and an illustrative zone. [Adoption operation](../../API.md#7-detailed-endpoint--operation-specifications) · [Shared adoption contract](../../API.md#8-shared-data-contracts)

## Date and inspection controls

- Presets apply directly. Custom dates use keyboard-operable **From**, **Through**, **Apply**, and **Cancel** controls. Validate dates inline, preserve valid draft values, and update the report on Apply. Escape or Cancel restores focus to the opener when the editor closes. The visible range and dates describe the applied scope.
- Keep visible focus on range and inspection controls. Give each chart one keyboard entry point with bucket navigation and an exact-value display shared with pointer inspection. **View trend data** exposes the same dates, approved figures, and states in a table. Announce a user-requested loading or completion state once without moving focus.

## States and privacy

| State | Presentation |
| --- | --- |
| Loading and ready | Keep the requested scope visible. Reserve the result layout with a static loading state, then render the authorized result. |
| Provisional or incomplete | Qualify released provisional values. An incomplete metric with a null value shows a short state and approved explanation. |
| Privacy suppression | Show **Hidden to protect participant privacy**. The suppressed reading has no value, conversion, shaped mark, or inferred geometry. Use the same state in the chart, table, focus readout, and accessible text. |
| Historical and unavailable | Keep anonymous eligible historical buckets. Show **Exact total unavailable** when source expiry or deletion removed detail an exact range total requires. |
| Confirmed zero, empty, or stale | Render an explicitly published zero at zero. Use an empty message for no results and a separate freshness state for unknown or stale coverage. |
| Partial read failure | Retain the requested range and independently valid results. Offer **Retry** at the affected read. If a previously loaded snapshot is separately authorized for simultaneous display, show its actual range and cutoff. |
| Session expiry or revoked permission | Clear values, inspected points, and open result details immediately. Ignore late responses and follow the admin access flow. |

Backend disclosure checks protect groups of fewer than ten distinct drivers, both directly and through subtraction across overlapping dates, funnel steps, totals, related views, and publication revisions. Use only released values and statuses for all text, marks, scales, and interactions. A safe stage count alone does not authorize a related rate. Anonymous buckets must not be joined or summed to manufacture an exact unique-driver total. [TRD disclosure rules and acceptance tests](../../TRD.md#71-admin-dashboard-fr-22)

## Frontend acceptance

- Exercise 7-, 30-, and 31-day ranges and All history. Verify time zone, coverage cutoff, the daily-to-weekly boundary, elapsed seven-day cohort eligibility, repeated sessions, and late durable completion.
- Verify 9 versus 10 distinct contributors, otherwise releasable adjacent stages whose difference is unsafe, overlapping ranges and revisions, incomplete data, and historical data after expiry. Check that hidden values stay out of trend geometry, readouts, tables, and assistive text.
- Verify the date editor, chart inspection, exact-value table, scoped retry, and access clearing with keyboard and screen-reader testing. Pen.dev illustrates those states. Runtime authorization, data disclosure, and accessibility require frontend and API verification.

## Saved Pen.dev frames

The editable frames are in [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>). The screen frames mark sample dates, display zone, and conversion bases as illustrative. The 30 daily session buckets sum to 1,221. The 15 November readout, plot, and table use the same 24-driver and 41-session values.

| Frame | Pen node |
| --- | --- |
| A06 · Adoption / 1440 | `PuMuP` |
| A06 · Adoption / 1024 | `psgcu` |
| A06 · Adoption / 320 | `uXC2H` |
| A06 · Range and publication states | `tdeyd` |
| A06 · Exact daily trend data | `G6XDn0` |
| A06 · Weekly trends and disclosure gaps | `pMJxd` |
