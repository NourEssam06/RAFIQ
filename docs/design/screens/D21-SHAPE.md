# D21 Emergency Contacts

The driver opens **Settings → Emergency contacts** or follows the contact link from **D02 Start session and readiness** while stationary. They can see who RAFIQ will try first, which contact channels are eligible, and what the recipient may receive. Use the private Settings shell and return the driver to the readiness context when they arrived from there. D04 owns the live countdown, D08 shows attempt outcomes, and X01 covers the recipient’s message. [Screen requirements](../../SCREENS.md#d21-emergency-contacts)

## Approved layout

The user selected **A · Two columns** and approved implementation in Pen.dev with suitable components. At 1440 px, the left column contains **Contacts**, **Add contact**, and the two possible positions in dispatch order. The inline add or edit form occupies the same column as its contact. The right column contains **Share precise location**, followed by the read-only **Alert message preview**. Keep the preview visible while the driver edits on desktop.

Reuse D19’s private navigation, its **Settings** selection, and its compact section selector at narrow widths. Mark **Emergency contacts** as current. Use the 48 px desktop gutters and 20 px gutters at 390 px as reference. Follow `colors.canvas` (#0e100f), `colors.ink` (#fffce1), `colors.accent-stone` (#bbbaa6), and Space Grotesk, the documented Mori substitute. Use `spacing.sm` (8 px) for compact status groups, `spacing.md` (16 px) within controls and rows, and `spacing.xl` (24 px) between sections. Apply the existing 8 px control radius and flat dividers where appropriate. At 390 px, 200% browser zoom, and 320 CSS px reflow, stack contacts, editor, location sharing, and preview in the same reading order. Wrap destinations and action groups instead of truncating them. [D19 Settings reference](D19-SHAPE.md) · [Visual tokens](../../DESIGN.md)

Reuse RAFIQ’s navigation, inputs, buttons, focus and status treatments, and the D07 destructive dialog anatomy. Use standard ordered-list, button, consent, and status semantics. The new compositions are the contact row with channel status and the alert preview with location variants. Give these recurring states editable Pen layers. [Shared screen rules](../../SCREENS.md#shared-design-rules)

## Contacts and location

| State or action | Design and behavior |
| --- | --- |
| Loading and read failure | Show a labeled loading state. On read failure, show a scoped **Retry**. Display private data only for the current eligible driver and clear it if access is lost. |
| Empty, one, or two contacts | Show **Add contact** while a slot is available. At capacity, show **2 of 2 saved**. Use an ordered list with visible positions **1** and **2** and expose **First contact** and **Second contact** to assistive technology. Pair each configured destination with its channel name and textual eligibility. |
| Add or edit | Show a labeled name field and optional email and WhatsApp fields with a group instruction requiring at least one valid destination. The API accepts names of 1–100 characters and an international-format number starting with `+`. One editor is open at a time. Focus the first field on entry. **Save contact** submits a new contact. **Save changes** submits an edit. **Cancel** returns to the opener. Associate input errors with the relevant field or field group and keep valid fields and edits. |
| Contact save | Keep adjacent **Saving…**, confirmed **Saved**, and retryable failure states. A destination change invalidates pending authorization for the old destination. A changed WhatsApp number gets server-rechecked eligibility. Preserve the draft on failure and apply only the confirmed server result to the saved row. |
| Reorder | With two contacts, provide **Move down** on the first and **Move up** on the second. Include the contact name in each accessible label. Keep the confirmed order visible during the write. On success, swap the rows in the DOM and visually, retain focus on the moved contact’s available move control, and announce its new position once. On failure, keep the confirmed order and offer retry. Refresh the contact set after a stale-order conflict. |
| Remove | Open **Remove [name]?** and explain that RAFIQ will stop trying that contact and block pending sends to the removed destinations. Put initial focus on **Cancel**. Trap focus, support Escape before confirmation, keep the row during the request, and remove it after server confirmation. Show progress and failure near the action. Return focus to the opener after cancel, or to a surviving row or **Add contact** after success. |
| Location consent | Save **Share precise location** independently of contact changes. Show saving, confirmed on/off, and retryable failure at the control. If a write has an uncertain outcome, refresh the authorized consent before presenting it as saved. Dispatch checks current permission separately. |

Use the server’s channel state. A destination being **Saved** means it is on file. The eligibility copy maps `eligible` to **Eligible**, `notQualified` to **Channel not qualified**, `optInRequired` to **Recipient opt-in required**, `optedOut` to **Opted out**, and `unavailable` to **Unavailable**. Pair text with a non-color cue. If no contacts have an eligible channel, explain why using the available reason and retain the affected row actions. WhatsApp requires off-app recipient opt-in and separate provider qualification. Email qualifies independently. [Emergency settings and contact changes](../../API.md) · [Eligibility and delivery](../../EXPERIENCE.md#emergency-mode-and-delivery-evidence)

An eligible supervised session tries contacts in their saved order, skipping contacts with no eligible channel. RAFIQ tries each eligible channel at most once for the current contact. It advances after all those channels reach terminal failure. Pending or ambiguous outcomes hold progression, and delivery on either channel stops it. D21 displays configuration and eligibility while D08 displays delivery outcomes. [Alert sequence](../../PRD.md#85-emergency-alerts-by-email-and-whatsapp)

## Alert message preview

> RAFIQ observed sustained signs of drowsiness for [driver name] at [time]. Please call [driver name] to check on them.

Render the fixed server template as selectable, read-only text. Append exactly **Location unavailable.** whenever permission or usable location is absent. Represent the other variant with an illustrative map location or link when both conditions hold. Label the fixture **Example with location**. Opening the preview requires no browser location request, and the examples use synthetic data. The recipient reads the dispatched message and opens any included map link directly in their channel. [Fixed message and location policy](../../PRD.md#85-emergency-alerts-by-email-and-whatsapp)

## Motion and verification

Storyboard a 140 ms editor opacity transition and a 140 ms row move after the server confirms the new order. Dialog focus, saved status, and errors appear immediately. Reduced motion shows the finished state instantly. Animate only presentation and keep focus, assistive announcements, and backend confirmation independent. If Motion is already part of the frontend, C01 and C03 supply the relevant primitives. Use RAFIQ’s existing remove confirmation behavior or a standard accessible dialog. [C01 Layout Animation](https://motion.dev/docs/react-layout-animations) · [C03 AnimatePresence](https://motion.dev/docs/react-animate-presence) · [C05 Radix Alert Dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog) · [Move button guidance](https://www.w3.org/WAI/WCAG22/Techniques/general/G219)

The editable [RAFIQ Pen canvas](<../../../Pen Design/RAFIQ.pen>) includes these D21 frames and state boards.

| Frame | Pen node |
| --- | --- |
| Emergency contacts / Desktop | `Z0Q6h` |
| Emergency contacts / Desktop inline edit | `NnZt3` |
| Emergency contacts / Narrow 390 px | `b41j1A` |
| Emergency contacts / 320 px reflow | `NFjMo` |
| Contact list states | `rT4iv` |
| Add and edit contacts | `q7Me2` |
| Reorder and remove | `pb6JC` |
| Location and message variants | `gRMIB` |

Pen.dev represents layout, action placement, states, and motion endpoints. Frontend acceptance requires keyboard and assistive technology checks, all five channel states, save/retry and focus behavior, authorization and stale-destination checks, and both exact location previews. Verify the layout with long destinations at 390 px, 200% zoom, and 320 CSS px reflow. [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) · [WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
