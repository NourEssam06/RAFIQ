# D15 Study Result — Pen.dev handoff

D15 is an **Operate** workspace for a signed-in driver reviewing a new or saved Experiment Studio run. The reader should be able to identify the exact run, understand the magnitude and uncertainty of its result, and see which evidence is eligible for exploratory inference or export. The user selected a plot-first layout with exact values immediately below and **Method details** collapsed on entry. The Pen design uses the recommended standard disclosure (**D15-C01**), static plots, and inline export feedback. [Screen requirements](../../SCREENS.md#d15-study-result) · [Experiment Studio setup](D14-SHAPE.md) · [Pen design](<../../../Pen Design/RAFIQ.pen>)

## Layout and navigation

1. Use the private RAFIQ shell with **Analysis** current and **Start session** distinct. At the top of the results workspace, show **Study result**, the job state, and **Back to Experiment Studio**. Restore the eligible originating setup or saved row, including scroll and focus.
2. Show the approved dataset name and revision, analysis version, study design, condition labels in submitted order, and observation unit before the evidence. Label synthetic fixtures explicitly. Show authorized provenance as it becomes available during loading, queued, and processing states.
3. Lead with the comparison plot and put the exact-value table immediately underneath. Use a semantic caption, row and column headers, units, approved sample sizes and applicable denominators, estimates, and interval endpoints. The p-value belongs to the whole paired or independent comparison. Keep the test name, eligibility or withholding reason, and **Exploratory · α = 0.05** outside the disclosure.
4. Show the run’s approved limitations above the inline **Method details** disclosure. When expanded, show the recorded input revision, analysis and method versions, observation unit, confidence interval method, and applicable reproducibility settings. Use one predictable reading and tab order across widths.
5. Reuse the Analysis shell, RAFIQ buttons and focus treatment, and existing status-row vocabulary. Use `colors.canvas` (`#0e100f`), `colors.ink` (`#fffce1`), `colors.accent-stone` (`#bbbaa6`), and the documented Space Grotesk fallback for Mori. Maintain the flat surfaces, 8 px and 16 px group spacing, and 24 px section spacing. The artboards use a 980 px results column at 1440 px, 48 px desktop gutters, and 20 px and 16 px gutters at 390 px and 320 px. On narrow layouts, wrap dataset and condition text, retain readable axis labels, and limit any horizontal scrolling to a named table region. [Design tokens](../../DESIGN.md#colors) · [Accessible tables](https://www.w3.org/WAI/tutorials/tables/) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

## Evidence and reproducibility

| Study design | Plot and table | Exploratory method |
| --- | --- | --- |
| Paired | A dot and whisker for the mean within-participant difference in incidents per monitored hour. Center the interpretation on the labeled zero reference of a signed axis. Spell out the approved subtraction order. Show the number of complete pairs where eligible and put approved condition summaries in descriptive rows. | Two-sided paired permutation test. Require at least **10 complete pairs**. Show the **95% paired bootstrap interval** when approved. Method details shows **10,000 draws** and seed **`20261120`**. |
| Independent groups | Directly labeled dots and whiskers on one **0–100%** axis for each arm’s proportion with at least one incident. Label and tabulate the approved **95% Wilson interval** for each arm, including applicable denominators and sample sizes. | Two-sided Fisher’s exact test. Require at least **10 participants per arm**. Keep the Fisher p-value distinct from arm-level intervals. |

Label both tests **Exploratory** with α = 0.05. Use a neutral p-value treatment and direct labels, with an equivalent exact-value table available without hover. Interpret a point by its estimate and units and a whisker by its disclosed interval bounds. Show limitations without implying a causal, accuracy, or safety claim. Pen examples are illustrative synthetic data. Browser figures must come from the same validated server snapshot. [Statistical and access rules](../../PRD.md#87-statistical-methods-and-data-access) · [Execution contract](../../TRD.md#5-statistical-analysis-and-reports) · [Estimation graphics](https://doi.org/10.1038/s41592-019-0470-3) · [Wilson intervals](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm) · [ASA p-value guidance](https://doi.org/10.1080/00031305.2016.1154108)

## Run and export states

| State | Required behavior |
| --- | --- |
| Loading a saved result | Show **Loading result** while access and availability are checked. Announce meaningful changes once and leave focus in place. |
| Queued or processing | Distinguish **Queued** from **Processing**. Preserve authorized known inputs. Use textual progress unless the service supplies a meaningful percentage. |
| Ready with inference withheld | Show a disclosure-safe prerequisite reason next to eligible descriptive evidence. Omit withheld interval and p-value values and their marks. Keep a measured zero numeric. |
| Privacy suppression | Use **Hidden to protect participant privacy.** Require **at least 10 distinct participants** per visible aggregate group. Apply complementary suppression to subtotals, totals, comparisons, intervals, and other results that could reveal protected information. Use only release-approved values in plot geometry, the table, accessible descriptions, tooltips, and export. |
| Transient failure | Show **Retry** for a confirmed retryable failure. Distinguish retrying a read of the same job from retrying computation with the same authorized input snapshot. |
| Ineligible or expired inputs | Remove affected evidence and export actions and offer a return to Experiment Studio. On access loss, clear protected content and use the safe unavailable-link treatment when applicable. |
| Export unavailable | Show **Export aggregate** unavailable with the reason nearby. Use **Aggregate downloads aren’t available yet** while the format is pending. After qualification, distinguish shared availability from this run’s current eligibility. |
| Export eligible or attempted | Keep progress, success, and recoverable failure beside **Export aggregate**. Prevent duplicate requests. Show **Download started** after handing the file to the browser. Recheck source, current authorization, and disclosure immediately before sending the same run’s approved aggregate. |

Keep the plot, table, status, and disclosure static. Use visible text and icons for states, a native button or disclosure with a visible focus state and Enter/Space activation, and a polite live region for meaningful job or export changes. Draw the plot and table with editable Pen layers. Pen represents the endpoint states visually. Browser implementation owns keyboard behavior, semantic relationships, announcements, authorization, and actual downloads. [Disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) · [Status messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages) · [Study and download contracts](../../API.md#7-detailed-endpoint--operation-specifications)

## Pen.dev frames

| Frame or component | Pen node |
| --- | --- |
| Paired study result at 1440 px | `onvGo` |
| Independent study result at 1440 px | `k7dqDn` |
| Paired Method details expanded at 1440 px | `Yp43Z` |
| Independent Method details expanded at 960 px | `JrsVG` |
| Paired study result at 390 px | `VCjbs` |
| Independent study result at 320 px with disclosure focus | `U5PkZE` |
| Loading, queued, processing, retry, and ineligible or expired sources | `Flfvy` |
| Withheld inference, measured zero, and partial or full suppression | `K1Hjto` |
| Aggregate export states | `mtIT0` |
| Reusable D15-C01 disclosure | `RcI4y` |

The independent fixture shows **5 of 24** participants with at least one incident in Standard prompts and **11 of 30** in Quiet prompts. The paired fixture uses an illustrative Quiet prompts minus Standard prompts difference of **−0.40 incidents per monitored hour**, a 95% interval of **−0.68 to −0.12**, and **24 complete pairs**. In the disclosure board, the suppressed arm has no exact count, estimate, interval or plot mark, and the paired descriptive example shows a measured zero while withholding inference.

## Browser acceptance and open contracts

- Verify the paired and independent designs at desktop and narrow widths, keyboard-only navigation, visible focus, browser zoom and reflow down to 320 CSS px, exposure of full labels and intervals, and consistent table and chart values. Cover positive and negative paired differences, zero, intervals spanning zero, and independent bounds at 0% and 100%.
- Exercise 9 and 10 complete pairs and 9 and 10 participants per arm. Test participant-count disclosure separately, including complementary suppression and authorization or source changes during result retrieval and export. Verify chart, table, accessible text, and export parity after each change.
- Confirm display-safe pending metadata when `result: null`, condition labels, the paired subtraction order, retry semantics for computation, and the qualified aggregate format and media type before browser wiring. Pen fixture labels and eligibility states illustrate these cases. [API qualifications](../../API.md#18-open-questions-and-decisions-requiring-approval)
