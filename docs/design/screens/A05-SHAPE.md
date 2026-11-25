# A05 Release Readiness

**Approved direction · Layout A and A05-C02.** A stable gate table with an optional 120 ms Motion for React reveal inside expanded evidence details. **Mode · Operate.**

An Owner or Staff member with **View metrics** opens **Release Readiness** from A04 Service Health after admin sign-in and MFA. They compare gate results, check verification dates, and open approved evidence. **Back to Service Health** restores the selected health range and returns focus to the A05 entry where available. A05 shows the release process’s recorded results. Release approval and feature activation happen through that external process. [Screen requirements](../../SCREENS.md#a05-release-readiness) · [Admin workflows](../../EXPERIENCE.md#admin-workflows) · [Technical requirements](../../TRD.md#71-admin-dashboard-fr-22)

## Frame and hierarchy

1. **Admin shell.** Keep **Service Health** current in the permission-scoped admin navigation. In the content area, place **Back to Service Health** above the **Release Readiness** heading.
2. **Status summary.** Use one compact line of exact counts in this order, **Passed**, **Failed**, **Pending**. Count every displayed gate once and update counts from the same response as the rows. The counts describe the displayed catalog and carry no release verdict. The Service Health date range belongs to A04.
3. **Gate table.** Use one row per gate with **Gate**, **Status**, **Last verified**, and **Approved evidence**. Give public launch, emergency email, emergency WhatsApp, and each optional chat provider separate identities. Follow the approved catalog order and keep positions stable when statuses change. Display the status as text with a supporting icon. Use absolute verification dates in the admin display time zone once defined. Keep names and status text legible with color disabled.
4. **Evidence.** Put the approved link in the row. Use an accessible name that identifies the gate or the approved artifact. If the source also supplies approved supporting detail, place a separate **Evidence details** button in the evidence cell and reveal the detail in a companion row immediately below the gate. On narrow layouts the detail opens within the same gate item. A gate carrying a single evidence link uses the visible link alone. The evidence destination applies its own access rules.

Use the A04 admin shell and its gutters. Match the existing **Horizontal status row** (`Yh4JZ`), **Stacked status row** (`fqIDy`), and **Method details disclosure** (`RcI4y`) for visual treatment. Use `colors.canvas`, `colors.ink`, and `colors.accent-stone`, the established RAFIQ UI type treatment, and `spacing.sm`, `spacing.md`, and `spacing.xl` (8, 16, and 24 px). Keep table dividers flat and accents local to state cues. Use standard table, link, button, and status semantics. The A05 compositions are the count summary and gate row. [Visual tokens](../../DESIGN.md) · [RAFIQ canvas](<../../../Pen Design/RAFIQ.pen>) · [A04 design research](A04-COMPONENT-RESEARCH.md)

## States and recovery

| State | Presentation |
| --- | --- |
| Loading | Keep the heading and return link visible. Show **Loading release gates…**. |
| Loaded | Render all returned gates and exact counts. Use **Passed**, **Failed**, and **Pending** from the source. |
| Missing date or evidence | Show **No verification date recorded** or **No approved evidence recorded** in the corresponding field. Preserve the returned gate status. |
| Evidence reference cannot be opened | Keep the gate and its verification date visible. Use **Evidence unavailable** when the app can establish that state. An approved destination that denies access handles its own recovery. |
| Empty response | Show **No release gates are available**. |
| Read failure | Show **Couldn’t load release gates** and **Retry**. After a failed refresh, label any still-authorized previous results **Last loaded results**. |
| Fresh read changes a gate | Apply status, date, evidence, and summary together. Keep row order and focus stable where the focused element still exists. Announce the result of a user-requested refresh once without moving focus. |
| Expiry or permission revocation | Clear rows, counts, evidence, and open details immediately. Ignore late responses and follow the applicable admin access flow. |

The proposed API supplies `gateId`, `status`, nullable `lastVerifiedAt`, and nullable `evidenceReference`. The approved gate names and order, verification date display zone, and authorized reference-to-link resolution are open implementation inputs. The current response carries one reference and no supporting-detail field. A05-C02 applies when an approved source supplies that detail. Any storyboard artifact labels, statuses, or dates are synthetic. [Endpoint and ReleaseGate schema](../../API.md#7-detailed-endpoint--operation-specifications)

## Approved motion · A05-C02

| Moment | Standard motion | Reduced motion |
| --- | --- | --- |
| Activate **Evidence details** | Set the expanded state and allocate the panel’s final space immediately. Fade in only the supporting content over 120 ms with ease-out. | Show the final panel and its contents immediately. |
| Close the disclosure | Close immediately. The trigger retains focus. | Close immediately. |
| Read, update, or lose access | Apply the state immediately. Gate statuses, counts, verification dates, and primary links stay static. | Apply the state immediately. |

Use a native button with an exposed expanded state and a stable association to the panel. Enter and Space activate it. Give each trigger an accessible name that identifies the gate. Closed details stay out of the tab order. If refresh removes the focused link or detail, return focus to the nearest surviving gate control or the section heading. Use Motion’s React enter animation and explicitly branch on the reduced-motion preference so the optional opacity fade is skipped. Motion is MIT licensed. Retain the copyright and permission notices when distributing covered code. [Motion animation](https://motion.dev/docs/react-animation) · [Reduced-motion hook](https://motion.dev/docs/react-use-reduced-motion) · [Source and license](https://github.com/motiondivision/motion/blob/main/LICENSE.md) · [WAI disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)

## Pen.dev handoff and acceptance

- Draw a **1440 px** table with a mix of all three statuses, a visible evidence link, and explicit missing-date and missing-evidence labels. Draw a **1024 px** narrow desktop frame and a **320 CSS px** stacked variant with field labels. Check the layout at **200% browser zoom** in the frontend. Preserve reading order and let long gate names and links wrap. [Table semantics](https://www.w3.org/WAI/tutorials/tables/) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Storyboard the conditional disclosure with **collapsed**, **expanded at 0 ms with final layout**, **120 ms settled**, and **reduced-motion expanded** states. Include loading, empty, read failure with Retry, and cleared access states on a separate state board.
- Verify the counts match the displayed rows. Confirm status changes preserve row order, missing date and evidence remain independent, and returning to A04 restores its range. Confirm the only controls are navigation, approved evidence, conditional disclosure, and read recovery.
- In the frontend, exercise the table with keyboard and a screen reader, verify evidence destination authorization and clearing on revoked access, and check reduced motion and refresh announcements. Pen.dev frames show layout and storyboard endpoints. Runtime verification covers focus, live messages, permissions, and motion.

## Saved Pen.dev frames

The editable designs are in [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>) beside A04. The count strip is one linked component with compact spacing and type overrides at 320 px. The disclosure uses the existing RAFIQ control. Gate results, dates, and evidence labels are sample data. Evidence links, navigation, and the 120 ms reveal are represented as design states.

| Frame or component | Pen node |
| --- | --- |
| A05 · Release Readiness / 1440 | `o585O` |
| A05 · Release Readiness / 1024 | `Ct6jW` |
| A05 · Release Readiness / 320 | `qWjQc` |
| A05 · Gate read and access states | `p572Ff` |
| A05-C02 · Evidence details storyboard | `o8ojM` |
| A05-C02 · Expanded evidence / 320 | `qJO3w` |
| A05 · Gate status counts | `Lbpmm` |
