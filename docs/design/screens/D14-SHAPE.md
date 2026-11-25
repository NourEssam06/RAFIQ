# D14 Experiment Studio — Pen.dev handoff

D14 is an **Operate** workspace for a signed-in driver working outside a monitoring session. The driver selects an approved dataset revision, compares two conditions, understands the outcome the study will measure, and starts or reopens a saved study. The user selected a wide-screen history panel that stacks below the form and plain-language guidance with expandable technical details. For the authorized Pen implementation, use standard RAFIQ selectors, a single disclosure, and text-and-icon status rows. [Screen requirements](../../SCREENS.md#d14-experiment-studio) · [Experiment Studio journey](../../EXPERIENCE.md#what-if-experiment-studio-and-benchmark)

## Frame and hierarchy

1. Use the private RAFIQ shell with **Analysis** current and **Start session** distinct. **Experiment Studio** is the page heading. Retain links to **What-If** and **Benchmark** through the Analysis navigation. Use D06’s desktop and narrow shell and list rhythm, and D05’s status-row treatment. [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>) · [D06 handoff](D06-SHAPE.md)
2. Give **Study setup** the larger column. Put **Dataset** first, then the selected revision and read-only design and observation unit, two condition fields, the comparison explanation, **Method details**, and **Run study**. Use the design system’s near-black canvas (`colors.canvas`, `#0e100f`), cream ink (`colors.ink`, `#fffce1`), stone secondary text (`colors.accent-stone`, `#bbbaa6`), Space Grotesk when Mori is unavailable, flat surfaces, `spacing.sm` (8 px), `spacing.md` (16 px), `spacing.xl` (24 px) and `rounded.md` (8 px). Use 48 px wide and 20 px narrow gutters where the existing shell supports them. [Design tokens](../../DESIGN.md)
3. Place **Saved studies** beside the form at 1440 px. Stack it below the primary action as the workspace narrows. Stack the two condition selectors and their errors when the labels need more room. Test 390 and 320 CSS px and browser zoom. Keep page reading and tab order from setup to history. Keep actions next to their study and allow long dataset names, condition labels and versions to wrap.

## Study setup and methodology

- **Dataset.** Start blank for a new study. List only versioned synthetic fixtures or institution-approved predefined datasets. Identify a synthetic fixture as such. Show approved descriptors and the immutable selected revision. Resolve the design, observation unit and method from that revision. On dataset change, clear incompatible selections and tell the driver where a new choice is required.
- **Conditions.** Use a fieldset with two labeled standard selectors. Use approved display names and expose supported options for the current revision and pairing. Prevent identical selections and explain unsupported pairs inline. Preserve the submitted order when opening or loading a saved setup. The contract must define the direction of an ordered difference before the UI labels it.
- **Method.** Keep the outcome visible in plain language and put technical details behind a single disclosure. Both methods are exploratory at α = 0.05. D15 owns the actual estimates, intervals, p-value where eligible, inference-withheld reasons and disclosure-checked results. [Statistical methods and access rules](../../PRD.md#87-statistical-methods-and-data-access) · [Study result](../../SCREENS.md#d15-study-result)

| Design | Visible explanation and observation unit | Method details |
| --- | --- | --- |
| Paired | The same participants are measured in both conditions. Compare incident rates per monitored hour within each participant. One participant with measurements in both conditions contributes one complete pair. | Two-sided paired permutation test of the mean within-participant rate difference, 95% paired bootstrap interval, at least 10 complete pairs, 10,000 draws, seed `20261120`. |
| Independent groups | Different participants are measured in each group. Compare the share of participants with at least one incident. One participant in a single group is the observation unit. | Two-sided Fisher’s exact test, 95% Wilson intervals for the proportions, at least 10 participants per group. |

## Submission, history and recovery

- **Run study** submits an immutable snapshot. Show **Submitting** next to the action, keep the valid form values visible and prevent duplicate submission. Open D15 once scheduling is durably accepted. An ambiguous response retains the same submission identity while the outcome is reconciled. New studies and eligible reruns become distinct saved runs.
- Each authorized history row shows dataset name and revision, the condition pair, method, creation time with time-zone context, and status. **Open study** opens the eligible D15 record. **Use saved setup** loads the exact inputs for review before a new run. Require an explicit replacement when the form contains other changes. Returning from D15 restores the originating eligible row or draft, scroll and focus.
- Show independent loading, empty and retry states for the catalog and history. A catalog failure can coexist with usable history. On invalid pairs, unavailable methods or expired sources, use a specific message and correction near the field. Preserve other valid inputs through recoverable failures. Revalidate a saved source before restoring it. Reveal protected details only while authorized.
- Use **Queued**, **Processing**, **Ready**, confirmed retryable failure and unavailable or expired states as text with a non-color cue. Announce meaningful transitions once. A ready result can still have inference withheld. Show eligible descriptive results in D15 and apply the approved minimum of 10 distinct participants for each exposed aggregate group, including complementary suppression. [Shared screen rules](../../SCREENS.md#shared-design-rules) · [Run and result endpoints](../../API.md#7-detailed-endpoint--operation-specifications)

## Components and validation

- Reuse private navigation, buttons, text inputs and focus treatment, D05 status rows, D06 list rows, and the established loading and error treatments. The new RAFIQ compositions are the structured dataset choice, two-condition group, method summary and saved-study row. The launch fixtures use standard choices and a single disclosure. The plain disclosure and static status indicators are the selected implementation defaults. [Disclosure interaction](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) · [Combobox interaction if catalog search is later warranted](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
- Represent disclosure open/closed, picker open/focused, paired and independent study setups, loading, no datasets, empty history, invalid pair, expired dataset, submission and saved run outcomes as editable Pen states. Use only labeled synthetic examples. Pen represents the states visually. Verify actual keyboard navigation, focus, announcements, responsive behavior, durable submission and permissions in the browser implementation. Static states give reduced-motion users the same information.
- Acceptance checks cover both study designs from Analysis to an accepted D15 run, selection and revalidation of both conditions, eligible saved setup reuse, stale-source recovery, and account change while a request is in flight. Check keyboard-only operation, visible focus, meaningful status messages, and wrapping of long metadata at 320 CSS px. Verify that history cannot expose another driver’s information.

## Open API contracts

- The catalog schema contains condition handles and the design and method enums. Resolve approved condition labels, observation-unit descriptors, supported pair rules and ordered-difference direction before wiring the form. [StudyDataset and StudyCreate](../../API.md#7-detailed-endpoint--operation-specifications)
- `StudyRun` permits `result: null`, and `Job.updatedAt` describes a status update. The saved list needs the immutable dataset summary, display-safe conditions and method, original `createdAt`, and reliable retryability and unavailable-source mapping before and after a result exists. The aggregate export format remains pending and is outside D14. [API qualifications](../../API.md#18-open-questions-and-decisions-requiring-approval)

## Pen artboards

| Frame ID | Visual reference |
| --- | --- |
| `C9cxW` | Desktop 1440 with paired setup and saved studies alongside |
| `viU77` | Paired setup with Method details expanded |
| `A9FAqr` | Independent-group setup at 960 px with Method details expanded |
| `s870J1` | Stacked 390 px layout |
| `MCsXB` | 320 px reflow with the dataset picker open and focused |
| `eMpVe` | First study with a blank setup and empty history |
| `S2aHKv` | Catalog, validation, history, submission and recovery states |
| `lwTma` | Saved study lifecycle states |
