# D13 What-If Result

On 25 November 2026, the user approved **Layout A · Metric-first comparison** and **D13-C06 · Ready reveal** in Pen.dev. Use RAFIQ's paired KPI rows and signed differences (**C01** and **C02**), with native comparison bars (**C03**) when compatible behavior rows are returned. The driver uses this private **Operate** workspace to compare the recorded session with a replay under selected thresholds. [Screen requirements](../../SCREENS.md#d13-what-if-result) · [Design research](D13-COMPONENT-RESEARCH.md) · [Pen design](<../../../Pen Design/RAFIQ.pen>)

## Layout and navigation

1. Use the private review shell with **Analysis** current and **Start session** distinct. Place **Back to What-If** above the H1. Restore the eligible submitted draft or selected saved-run row, together with scroll and focus, on return to D12. **Change inputs** leads to D12 for a new run when the source is still eligible.
2. Before the metrics, show the authorized source session date and time with zone, run status, selected thresholds, measurement version, recorded policy version, and analysis version where available. Wrap facts and thresholds while preserving reading order. Use **Show all thresholds** if the list needs progressive disclosure. A reopened run keeps its original snapshot.
3. Present **Recorded baseline** and **Simulated result** as equally weighted columns. Align each metric and its unit across the pair in returned scope. Put descriptive counts and rates first, a compact comparison chart after the KPIs when a returned breakdown supports it, and reference-label evidence after the descriptive results. Link **View exact values** to a named table with visible row and column labels. On narrow widths, keep pairs side by side while their labels fit, then stack both labeled values under each metric.
4. Use the same flat panels, nav, UI typography and focus treatments as D07 and D09. Apply Space Grotesk as the documented Mori substitute, canvas `#0e100f`, ink `#fffce1`, and secondary stone `#bbbaa6`. Use 48 px desktop and 20 px narrow gutters, `spacing.sm` for related content, `spacing.md` for panels and `spacing.xl` between sections. Use text plus series styling such as outline and solid to identify chart marks. [D12 configuration and saved runs](D12-SHAPE.md) · [D07 tokens](D07-SHAPE.md#composition-and-tokens) · [D09 comparison](D09-SHAPE.md#compare-sessions) · [Design tokens](../../DESIGN.md#colors)

## Metric display

| Evidence | Presentation |
| --- | --- |
| Descriptive results | Show available incident counts, warning counts and incident rates with the applicable behavior or overall scope, unit, monitoring exposure and sample context where returned. Compare counts or rates of the same definition and scope. |
| Compatible reference labels | Show precision, recall, accuracy, false alarms and missed detections only for sides and scopes supported by labels and the returned metric status. Give an authorized reason for an unsupported side. |
| No reference labels | Omit the five scored metrics. Say **Reference labels are unavailable for this replay, so detection quality cannot be evaluated.** Keep eligible descriptive results visible. |
| Zero or unavailable | Render a measured zero with its unit. Use the specific available reason for an unavailable, incomplete or suppressed value. A chart can mark a measured zero at the origin. An unavailable side gets an explanation and no mark. |
| Difference | Calculate **simulated minus recorded** only for comparable pairs with the same definition, unit, scope and exposure or scoring basis. Use signed counts, signed rate units and signed percentage points. Use **No difference** for a true tie and give an explicit reason when a comparison cannot be made. Keep the values and difference neutral, including when scored metrics move in opposite directions. |

For the chart, display one measure and unit at a time. Align both bars on a common zero-based scale and keep their order stable. Show direct labels and final values immediately. Omit the chart if the response contains only aggregate pairs with no meaningful breakdown. Use synthetic data in Pen. An illustrative descriptive pair is **2 → 3 incidents**, **1 → 2 warnings**, and **10 → 15 incidents per monitored hour** over the same 12 monitored minutes. The scored example can show **80% → 75% precision**, **40% → 60% recall**, **86% → 88% accuracy**, **2 → 4 false alarms** and **12 → 8 missed detections** for a fictional 100-observation labeled scope. [API contract](../../API.md#7-detailed-endpoint--operation-specifications) · [Shared chart rules](../../SCREENS.md#shared-design-rules)

## States and C06 motion

| State | Treatment |
| --- | --- |
| Loading a saved run | Show **Loading result** with a neutral skeleton while access is checked. Reveal authorized context when confirmed. |
| Queued or processing | Use the exact state label. Preserve any confirmed inputs and reserve result space. Show a progress percentage only when available from the service. |
| Ready | Render the complete final comparison immediately. Present the labeled, unlabeled, partial or empty result according to available evidence. For empty results, show the authorized reason when supplied and offer return to D12. |
| Transient failure | **Retry simulation** uses the same input snapshot after revalidation. A fetch failure uses **Retry loading result** for the same run and leaves other authorized context intact. |
| Invalid inputs | Explain the affected source or threshold where known and return to D12 with eligible fields retained. |
| Source unavailable | Clear withdrawn or inaccessible content immediately. Use the safe authorized message and return to What-If or source selection. For an inaccessible protected link, apply the P08 unavailable-link treatment. |

On the actual queued or processing → ready transition, commit the final figures, labels, and chart together. Fade only a noninteractive accent or placeholder overlay to transparent over **160 ms**, ease-out, once. Keep controls and values available from the first ready frame. Opening an already-ready saved run uses the finished state. Reduced motion uses the immediate finished state. Announce **Simulation ready** once through a polite status region and keep focus where the driver left it. Pen can depict the editable states and timing storyboard. The browser owns the live job transition, CSS timing, reduced-motion preference, and announcements. [Experience accessibility](../../EXPERIENCE.md#accessibility-floor)

## Pen.dev frames

| Frame | Pen node |
| --- | --- |
| Desktop result with reference labels, behavior bars, and exact values | `wLURY` |
| Desktop result without reference labels | `W1EZ0e` |
| 390 px paired result | `Z61dLK` |
| 320 CSS px stacked result | `Eoi7C` |
| Partial evidence, measured zero, and equal counts | `j4DPO` |
| Run states and recovery | `rJs1b` |
| C06 ready reveal storyboard | `GxQha` |

## Implementation checks

- Verify that 1440 px desktop, 390 px narrow, 320 CSS px reflow, and 200% browser zoom keep source, status, results and return controls readable in order. Preserve predictable keyboard navigation, visible focus, clearly labeled differences and an accessible exact-value table. Use a named scroll region if the table needs horizontal scrolling.
- Exercise labeled and unlabeled replays, insufficient labeled observations on one side, a genuine zero, a true tie, mixed movement, and incompatible input or scope. Inspect source withdrawal during loading or ready and distinguish same-job fetch retry from same-input run retry.
- Confirm the authorized pending input snapshot, retry operation and per-metric comparability metadata before qualifying browser behavior. The proposed queued response supplies a job with `result: null`. Show only known input facts and omit unsupported differences. [What-If run contract](../../API.md#7-detailed-endpoint--operation-specifications)
