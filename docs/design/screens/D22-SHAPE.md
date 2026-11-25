# D22 Privacy

**Status** · Approved layout and accordion implemented in Pen.dev

**Mode** · Operate. A signed-in driver opens **Settings → Privacy**, follows the account deletion link from D19 Profile, or arrives from a privacy link in Monitoring, Clips, Sessions, or report review. The driver’s first job is to understand what RAFIQ keeps and when it expires. The user confirmed that the main deletion consequences should be visible, with supporting detail available on demand. Back returns to the originating view and restores its context when it is still accessible. [D22 requirements and shared design rules](../../SCREENS.md#d22-privacy) · [Experience](../../EXPERIENCE.md#retention-privacy-and-export)

## Approved layout

The user chose **A · One reading column** and **D22-C03 · Radix Primitives Accordion**. Use this order at every width:

1. **Privacy** heading, then the **Incident recording** and **Precise location sharing** rows with their settings links.
2. **How long RAFIQ keeps data**, a two-column table filling the reading column, followed immediately by the access and purge explanation.
3. **What deletion affects**, with the clip, session, and external-copy consequences and the **Open Clips** and **Open Sessions** links. Place the two accordion triggers beneath this visible content.
4. **External access**, with the grant and provider-sharing explanation and **Manage connections**.
5. **Delete account**, with a short consequence summary and the button that opens the confirmation.

Reuse the D19 private shell with **Settings** selected and **Privacy** current. The approved D21 desktop and narrow frames (`Z0Q6h`, `b41j1A`) show both shell forms. Carry over the 48 px desktop and 20 px narrow content gutters, flat dividers, existing focus and danger styles, and Mori typography with the established Space Grotesk substitute. Use `colors.canvas`, `colors.ink`, `colors.accent-stone`, and the existing `spacing.sm`/ `spacing.md`/ `spacing.xl` rhythm. Give table values typographic emphasis and reserve the destructive treatment for the account deletion action. [D19 shell](D19-SHAPE.md) · [D21 Settings layout](D21-SHAPE.md) · [Visual tokens](../../DESIGN.md)

## Consent and sharing

| Visible row | Status and explanation | Destination |
| --- | --- | --- |
| **Incident recording** | **Allowed for selected incidents** or **Off**. RAFIQ can save video-only clips for selected incident categories when consent is on. Monitoring runs with recording off. Withdrawing consent stops capture, discards unsent clips, and blocks pending publication. Clips already hosted follow the expiry and deletion rules below. The status describes consent even when there is no active session. | **Manage recording** → D20 Monitoring settings |
| **Precise location sharing** | **Allowed for eligible alerts** or **Off**. RAFIQ includes a map location or link only when permission is current and a usable location is available for an eligible emergency alert. Turning sharing off prevents location inclusion in future sends. Delivered copies stay with the recipient. | **Manage location sharing** → D21 Emergency contacts |
| **External access** | Explain that **Read driving data** lets a compatible client access approved session summaries, analytics and event details. **Author reports** lets the client submit drafts for review in RAFIQ. The grants can be revoked independently. Optional chat uses separate provider-by-provider linking and sharing consent. Revocation ends the affected access immediately. Revoking authoring can stop a report awaiting publication. Revoking chat sharing clears the temporary conversation and suppresses invalidated replies. | **Manage connections** → D23 |

Use a text status with a non-color cue next to each consent label. The status is read-only on D22. The links lead to the settings that change consent. Use **Checking…** while loading and **Couldn’t check status** with a scoped **Retry** when the read fails. Return or refresh after settings changes to show the confirmed status. Place the note about separate approval for use in evaluation or training at the end of **External access**. In that section, explain that MCP and chat exclude clips and links, raw media or measurement series, contacts, precise location, and finished report contents. Chat sends the driver’s messages and approved driving context. Direct provider-specific handling and consent to D25. [D20 recording](D20-SHAPE.md) · [D21 location](D21-SHAPE.md) · [PRD data boundaries](../../PRD.md#88-mcp-qualification-and-data-boundaries) · [Connections journeys](../../EXPERIENCE.md#mcp-connection-reports-and-optional-chat)

## Retention and deletion

Present a plain two-column table titled **How long RAFIQ keeps data**. Keep the six rows visible, with the time and its starting event together. The table describes service policy and appears even for a driver with no retained sessions. Item-specific expiry remains at the point of use.

| Data or access | When it expires |
| --- | --- |
| Clip waiting to upload | **24 hours** after capture |
| Clip stored in RAFIQ | **7 days** after capture |
| Session and incident details | **90 days** after the session ends |
| Precise location in RAFIQ | **24 hours** after capture |
| Report stored in RAFIQ | **30 days** after creation, or sooner if a required source expires |
| Report download link | **5 minutes** from issuance. RAFIQ also checks current authorization and report eligibility when the link is used. |

Place this immediately below the table:

> Deletion or expiry ends access in RAFIQ immediately. RAFIQ purges retained copies, including backups, within 30 days.

Under **What deletion affects**, keep these consequences visible:

- **Delete a clip.** The clip becomes unavailable. Independent session and incident details remain. **Open Clips** takes the driver to D10 for selection and D11 for the item action.
- **Delete a session.** Its records and dependent clips become unavailable. RAFIQ also withdraws hosted reports that need the deleted source. **Open Sessions** takes the driver to D06 for selection and D07 for the item action.
- **Copies outside RAFIQ.** Downloaded reports stay under the driver’s control. Delivered emergency messages and any included location stay with their recipients.

Use **D22-C03 Radix Accordion** for two independently expandable sections. **What happens to clips waiting to upload?** explains that sync retry cannot restore expired or deleted items and that withdrawal removes unsent clips. **What happens to dependent reports?** explains withdrawal on required-source expiry or deletion, immediate loss of review and download access, and how the driver can request a new report from eligible sources through the external agent. Keep the primary consequences visible above both disclosures. [PRD lifecycle](../../PRD.md#86-clip-and-report-lifecycle) · [Architecture deletion workflow](../../ARCHITECTURE.md#j2-private-recovery-clips-and-deletion)

## Delete account

Use the same confirmation anatomy as D07’s delete-session dialog. Place **Delete account** below the explanation and management links, in a section of its own. The confirmation identifies the current account by registered email and presents the consequences before the final action.

> **Delete your RAFIQ account?**
>
> This permanently removes account access for [registered email]. Your sessions, recordings and dependent reports stored in RAFIQ will become unavailable immediately. Your external grants and connections will be revoked. RAFIQ purges retained copies, including backups, within 30 days. Downloaded reports and emergency messages already delivered stay with the people who have them.

| State | Behavior |
| --- | --- |
| Confirm | Use **Cancel** and **Delete account**. Place initial focus on **Cancel**, trap focus, support Escape before submission, and return focus to the opener after dismissal. Keep the action explicit and keep backdrop clicks from confirming. |
| In progress | Show **Deleting account…** in the dialog. Keep the target visible and prevent another submission. Present progress without implying that the request can be withdrawn after submission. |
| Recoverable failure | With current eligible access and confirmed failure, keep the confirmation open with an inline error and explicit retry. For a lost or ambiguous response, show **Checking whether account access was removed…** while reconciling with authoritative account state. Use the ordinary signed-out or restricted flow for authorization errors without verified deletion. |
| Confirmed access removal | On `accessRevoked`, clear visible private data and close private views across tabs. Clear account-scoped local private state and return to public access. Put focus on a public confirmation heading such as **Account access removed**. Explain the purge window in plain language. |

The account deletion response confirms access revocation. The public confirmation should reflect that state. The identity verification requirements, the status and retry path after a lost response, and the exact public acknowledgment destination need confirmation from the account flow. [Account API operations](../../API.md#7-detailed-endpoint--operation-specifications) · [D07 confirmation](D07-SHAPE.md) · [W3C dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) · [Carbon modal guidance](https://www.carbondesignsystem.com/building-blocks/core/components/modal/guidelines)

## Components and motion

- **Reuse from RAFIQ.** Private navigation, compact Settings selector, links and button treatments, inline status feedback and the D07/D11 confirmation pattern. Borrow status typography and icon treatment from D20 and D21.
- **Standard components.** Two-column table with structural column and row headers, descriptive links, straightforward disclosures, noninteractive status text and names, and a modal with an explicit destructive action. A switch conveys an actionable binary input, so D22’s status uses text and a link to the editable control. [W3C table guidance](https://www.w3.org/WAI/tutorials/tables/) · [W3C disclosure guidance](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) · [W3C switch guidance](https://www.w3.org/WAI/ARIA/apg/patterns/switch/) · [W3C alert dialog guidance](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/)
- **New RAFIQ compositions.** Consent summary row, six-row retention table, and account deletion content and feedback variants. The table uses text rather than a chart or animated countdown because each deadline has its own starting event and the report rule has an early cutoff.
- **Selected disclosure.** Use the vertical Radix Accordion in multiple mode, with both items collapsed on entry. Each heading contains a trigger with an end-aligned chevron. Enter, Space, or click toggles that item immediately and keeps focus on its trigger. The indicator switches orientation and the content appears in flow. Both items can be open or closed, and reduced motion uses the same immediate behavior. Reuse the shared Radix import if adopted. The source is MIT, with the license and copyright notice retained on distribution. [Accordion API and demo](https://www.radix-ui.com/primitives/docs/components/accordion) · [Component source](https://github.com/radix-ui/primitives/tree/main/packages/react/accordion) · [License](https://github.com/radix-ui/primitives/blob/main/LICENSE)
- **Motion treatment.** Accordion state, status feedback, and account deletion transitions appear immediately. Use the existing RAFIQ dialog anatomy with static presentation.

### Research references

| ID | Component | Library | Intended placement | Animation behavior | Free/license verification | Demo URL | Trade-offs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **D22-C00** | Native disclosure | HTML `details` / `summary` | Two optional consequence sections | Immediate open and close | Built-in browser behavior, no package | [MDN example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) | Lowest implementation cost. Style visible focus and the expanded cue in RAFIQ’s language. Pen frames can show both endpoints. |
| **D22-C01** | Accordion | Animate UI, Radix UI variant | Optional consequence sections | Stock effect unfolds over 350 ms with fade and blur. Its reduced-motion mode still plays the fade and blur. | Free for application use under MIT plus Commons Clause. Keep the license and copyright notice. The license restricts selling or redistributing the original components themselves. [License](https://github.com/imskyleen/animate-ui/blob/main/LICENSE.md) | [Accordion demo and installation](https://animate-ui.com/docs/primitives/radix-ui/accordion) | React-compatible package with `@animate-ui/react` and `motion`. Only worth considering if already adopted. Requires adapting the effect or using its static equivalent for reduced motion. Pen can capture endpoints. |
| **D22-C02** | Motion component | Motion for React | Inner text of an accessible RAFIQ disclosure | Optional 150 ms entry fade only, with immediate state change and no exit delay | Free MIT package with public source. Keep the license and copyright notice. [License](https://github.com/motiondivision/motion/blob/main/LICENSE.md) | [Motion component docs and examples](https://motion.dev/docs/react-motion-component) | React/Next.js client integration. Reuse only if Motion is already available. Supply semantics through the underlying disclosure and use `useReducedMotion` to bypass the fade. Opacity keeps layout steady. Pen can show endpoints and annotate timing. |
| **D22-C03 · Selected** | Accordion | Radix Primitives | Optional consequence sections | Immediate open and close | Free MIT source. Keep the license and copyright notice. [License](https://github.com/radix-ui/primitives/blob/main/LICENSE) | [Accordion demo and source example](https://www.radix-ui.com/primitives/docs/components/accordion) | React-compatible, with built-in keyboard interactions. Pen can show the collapsed and expanded states. |
| **D22-C04** | Alert Dialog | Radix Primitives | Account deletion confirmation, if a standard primitive is needed | Static for D22 | Free MIT source. Keep the license and copyright notice. [License](https://github.com/radix-ui/primitives/blob/main/LICENSE) | [Alert Dialog demo and source example](https://www.radix-ui.com/primitives/docs/components/alert-dialog) | Provides modal keyboard and focus behavior. Use the same RAFIQ styling and failure states. Verify asynchronous state handling and focus in the frontend. Pen can show the dialog and its states. |

The approved frontend is Next.js with TypeScript. Integration and runtime cost in RAFIQ remain unmeasured. [Frontend architecture](../../TRD.md)

## States, reflow, and handoff

- At 1440 px verify the two consent rows and full table fit the main reading area. At a 390 px viewport, 200% zoom, and 320 CSS px reflow, use the compact Settings selector, preserve reading order, and wrap the table’s labels, values, links, and long email addresses. Keep the two-column table semantic and check narrow cell wrapping before considering a labeled overflow region. Keep the whole dialog operable within the viewport, with internal scrolling if needed. [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Use proper headings, a skip link, landmark and current-page semantics, visible focus, and predictable tab order. Each disclosure responds to keyboard activation and exposes its state, supports independent expansion, and keeps focus on its trigger. Announce meaningful progress, errors and confirmation once, independently of motion. Use static loading placeholders and scoped recovery for consent reads. Where one read fails, keep the other confirmed value and retention policy visible. On sign-out, account switch or restriction, remove account-specific content. [WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- Read confirmed consent through `getRecordingConsent` and `getEmergencySettings`. Render only the sharing decision from the emergency settings response. Keep unavailable or stale values visibly separate from **Off**. The D22 grants section explains and links out using static content. Per-provider and per-client states live in D23. [API operations](../../API.md#7-detailed-endpoint--operation-specifications) · [D23 ownership](../../SCREENS.md#d23-connections)

## Pen.dev frames and acceptance

| Frame | Required content |
| --- | --- |
| **D22 / Privacy / Desktop** | 1440 px Settings shell and the full reading column, with both accordion items closed. Use the six production policy rows, mixed consent states, and the visible deletion consequences. |
| **D22 / Privacy / Narrow** | 390 px and 320 px references with the compact Settings selector. Wrap labels and expiry rules and show one accordion item open. |
| **D22 / Consent and disclosure states** | Use editable variants for allowed, off, checking and unavailable consent, a scoped retry, and the accordions closed, individually open, and both open. Use visible focus on one trigger. |
| **D22 / Delete account states** | Confirmation, submitting, recoverable failure, uncertain outcome, and public confirmation. Use a synthetic registered email in the private dialog and put no private content on the public confirmation. |

The editable [RAFIQ canvas](<../../../Pen Design/RAFIQ.pen>) contains the following frames:

| Frame | Pen node |
| --- | --- |
| Privacy desktop, 1440 px | `Q3ZGZd` |
| Privacy narrow, 390 px | `HMHda` |
| Privacy reflow, 320 px | `JNdak` |
| Consent and disclosure states | `hutXP` |
| Delete account states | `F8Dyt` |

The Pen frames show the table and the accordion’s collapsed and expanded states as editable layers. The deletion board includes narrow confirmation and public acknowledgment. Screenshots and bounds checks covered all five frames. In the frontend, verify the following behaviors:

- A driver with partial or unavailable consent data can read all six deadlines and the main consequences. Unknown consent and **Off** remain visually distinct.
- Accordion items toggle independently with keyboard and pointer, retain trigger focus, and announce their expanded state. Test the same immediate behavior with reduced motion.
- The destructive confirmation names the account and consequences, supports cancellation before submission, and reports confirmed access removal before rendering the public acknowledgment. Test a failed request and a lost response separately.
- A deleted or expired source blocks dependent report access, including previously issued download links. Verify this through authorized point-of-use screens and the API.
