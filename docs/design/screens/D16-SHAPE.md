# D16 Benchmark — approved Pen.dev handoff

The user approved **A**, the side-by-side behavior comparison and detail panel, and **C04**, standard static components with an in-place count explanation, on 25 November 2026. D16 is an **Operate** dashboard for an eligible driver reviewing the released behavior system on controlled held-out evidence. Detection quality by behavior comes first after the scope and sample. [Screen requirements](../../SCREENS.md#d16-benchmark) · [Design research](D16-COMPONENT-RESEARCH.md)

## Frame and reading order

1. Use the existing private RAFIQ shell with **Analysis** current and **Benchmark** selected. Keep **Start session** distinct. Offer **Back to Analysis** or **Back to report** according to the verified entry. The D18 return path must preserve the referring report context.
2. Lead with **Benchmark**, the controlled held-out scope, and monitored exposure. Put actual authorized participant or episode counts beside the exposure if supplied. Keep release, dataset, annotation, catalog, model, policy and scoring versions in **Evaluation details**. Indicate the stationary or simulator setting when supplied by the approved release. Mark illustrative numbers and identifiers **Example data** on the canvas.
3. At wide desktop widths, give about two thirds of the available width to **Detection by behavior** and the rest to **Confusion counts**. Default to labeled horizontal **Precision and recall** bars with a shared 0–100% scale. Offer **F1 score** and **Accuracy** on the same scale. Keep behavior order stable and show each behavior’s coverage and exact values. Each behavior action updates the evidence panel in place and retains focus on the originating control.
4. Show a 2 × 2 matrix for the selected behavior. Rows are **Reference label**, columns are **RAFIQ prediction**, and axes have **Present** and **Absent**. Present/Present is TP, Present/Absent is FN, Absent/Present is FP, and Absent/Absent is TN. Keep the exact count in each cell. Use a visible selected-state outline and update a persistent explanation when a cell is activated. Show scored and unusable frame counts and class coverage beside the matrix. Each behavior has its own matrix because behaviors can overlap.
5. Follow with **Coverage and warnings**. Show overall observation coverage, false warnings per monitored hour, and warning delay. Give p95 the primary delay position and show median or maximum if approved and returned. Keep the units and exposure or sample near the values. Finish with **Metric definitions and methods** and **View data**, which gives the same exact evidence in a semantic table.
6. Stack the comparison and then its detail as space narrows. Stack warning and coverage summaries, preserve reading order and wrap long versions. Allow wider data tables to scroll within a labeled region. Use the existing shell gutters, `spacing.sm`, `spacing.md`, `spacing.xl`, `rounded.md`, flat surfaces, `colors.canvas` (`#0e100f`), `colors.ink` (`#fffce1`) and `colors.accent-stone` (`#bbbaa6`). Use Mori where available or the established Space Grotesk substitute. [Visual tokens](../../DESIGN.md) · [Accessibility floor](../../EXPERIENCE.md#accessibility-floor)

## Data and availability

| Evidence | Display rule |
| --- | --- |
| Evaluation scope | Use the approved controlled stationary or simulator holdout. Drivers are separated before tuning and private sessions stay outside the benchmark. Keep the protocol minimums of five held-out drivers, twenty independently staged positive episodes per behavior, and five monitored hours distinct from the actual sample. |
| Detection scores | Read validated R results through FastAPI. Explain precision as TP / (TP + FP), recall as TP / (TP + FN), F1 as the harmonic mean of precision and recall, and accuracy as (TP + TN) / all scored class frames. Keep exact values and the relevant denominator. Explain the effect of abundant negative frames on accuracy. |
| Matching and observation | Predictions and labels match by timestamp at 10 Hz. Class-unusable frames are excluded from that class’s confusion counts. Show the approved unusable share with its frame base where provided. Coverage uses elapsed time excluding deliberate user pauses and including observation-loss pauses. Overall coverage measures usable feed time. Per-class coverage measures observable cue time. |
| False warnings | Divide the approved count by monitored hours. Count a combined warning once as false when none of its named classes matches a qualifying labeled episode. Show the supplied monitored-hours base and count where approved. |
| Warning delay | Measure from the labeled cue meeting its configured dwell to the visible warning. Label the statistic in milliseconds, with the approved delay sample size when supplied. Show one validated p95 value. A distribution requires approved distribution data. |
| Loading, pending and failure | Keep the shell and return link. Use **Loading benchmark results** while retrieving and **Benchmark results are awaiting approval** for `pending`. Use **Benchmark results could not be loaded** with a nearby **Retry** for a retryable retrieval failure. Pending carries no performance figures. |
| Partial availability | Keep results for approved, available measures. Show a confirmed zero explicitly. Display unavailable, incomplete or suppressed values with their state and shareable reason. Empty scoring denominators or withheld values get an explanation in place of a mark. Keep the treatment consistent in the chart, matrix and table. |

[Benchmark protocol](../../PRD.md#83-benchmark-and-behavior-policy) · [Statistical result ownership](../../TRD.md#5-statistical-analysis-and-reports) · [API contract](../../API.md#7-detailed-endpoint--operation-specifications)

## Components, interaction and scope

- Reuse the review metric card, measure selector, exact-value readout, behavior breakdown and status treatments from RAFIQ’s Pen library where they fit. The new compositions are the horizontal comparison, per-class matrix, and release metadata block. Use native controls and semantic tables when implementing the browser version. Keep definitions in a standard disclosure with short optional help text beside individual metrics. [RAFIQ Pen file](<../../../Pen Design/RAFIQ.pen>) · [Disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)
- Selection, retry feedback and disclosure changes are immediate. Keep focus visible, preserve focus on the activating control, and announce the revised result once. Pair color with a value, label or outline. Use the same state in reduced motion. The Pen frames specify these appearances. Browser work owns keyboard execution, focus, announcements, responsive reflow and authorized data binding.
- `getBenchmark` documents one approved aggregate release or `pending`. Use read-only versions. A selectable release list and an exact D18 release reference need a stable approved release ID and authorized retrieval. Keep missing sample counts and unavailable metadata explicit. Confirm denominator and sample units, the unusable-frame base, the false-warning numerator and consistency of the two p95 fields before wiring them. The driver flow reads approved aggregates and methods. The evaluation runner and raw inputs are internal. [Contract gaps](D16-COMPONENT-RESEARCH.md#states-and-contract-gaps)

## Acceptance

- A driver can name the scope, compare precision and recall for two behaviors, locate the count of misses for the selected behavior, and find its coverage and scoring base. Exact values match across the visual and table views.
- The warning delay statistic names the reference point and unit. The false-warning rate names its monitored-hours base. Confirmed zero, missing metric data, withheld data and pending release each have a distinct text treatment.
- Test the wide layout and stacked order, including long labels and versions. In the browser verify keyboard, touch, visible focus, reduced motion, 400% zoom reflow, retry, and a verified D18 return with the intended release context.

## Pen artboards

| Frame ID | Canvas state |
| --- | --- |
| `R1X5V` | 1440 px desktop with the side-by-side comparison and selected missed count |
| `pWaYl` | 390 px stacked layout |
| `c05pS` | 320 px reflow, single-behavior data view and keyboard focus appearance |
| `StWE6` | Expanded release metadata, metric definitions and five-behavior exact data |
| `GEVwp` | Alternate selected false-positive cell, F1 and accuracy comparisons |
| `AFkwT` | Awaiting approval |
| `Z1oc4` | Static loading |
| `rISvT` | Retryable retrieval failure with report return |
| `a751Z` | Withheld class counts, available coverage and unavailable p95 |
