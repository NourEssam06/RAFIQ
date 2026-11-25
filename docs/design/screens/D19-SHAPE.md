# D19 Profile

**Mode:** Operate. A signed-in driver opens **Settings → Profile** to check which account is active, update their display name, manage sign-in details, open past monitoring runs, or sign out. The user approved moving from shaping to the Pen.dev implementation. The selected direction uses one column, restrained save feedback, steady verification, and confirmation when sign-out discards an unsaved name edit. [Screen requirements](../../SCREENS.md#d19-profile)

## Layout and components

Use RAFIQ’s private shell with **Settings** selected and **Profile** current in the settings navigation. Start from the 1440 px driver shell and its 48 px desktop content gutters. Use the 390 px narrow reference with 20 px gutters. Keep the document in this order at every width:

1. **Profile**, then **Display name**, its labeled field, and **Save changes** with adjacent status feedback.
2. **Registered email** as readable, selectable text, with a verification word and icon and **Manage sign-in details**. Wrap long addresses at narrow widths.
3. **View session history** to [D06 Sessions](../../SCREENS.md#d06-sessions) and **Privacy** to [D22 Privacy](../../SCREENS.md#d22-privacy), where account deletion is addressed.
4. **Sign out** on its own action row.

Reuse the D01/D06 navigation, flat dividers, labeled fields, visible focus, existing button roles and status treatments. Refer to D07’s confirmation dialog anatomy for its title, body and two actions. Use one RAFIQ-specific composition for the read-only identity row and one stable feedback area for saving. Use Space Grotesk as the documented Mori substitute, `colors.canvas` (#0e100f), `colors.ink` (#fffce1), and `colors.accent-stone` (#bbbaa6). Follow `spacing.sm` (8 px) for compact status groups, `spacing.md` (16 px) within controls and rows, `spacing.xl` (24 px) between sections, and the existing 8 px panel and control treatment where applicable. Keep one page scroll at 390 px, 200% browser zoom, and 320 CSS px reflow. [D06 shell](D06-SHAPE.md#visual-references-and-proposed-dimensions) · [Dialog reference](D11-COMPONENT-RESEARCH.md) · [Tokens](../../DESIGN.md)

## States and feedback

| Trigger or state | Visible behavior | Frontend expectation |
| --- | --- | --- |
| Initial account read | Static placeholders. If the read fails, show **Couldn’t load profile** and **Retry**. | Keep private details hidden until the authorized response. Encountering a restricted account or an authentication or verification gate uses the existing eligible public path. |
| Display name ready or edited | Show the current server value or an empty field when the account has no name. Enable **Save changes** for a changed draft. Show validation next to the input on submit and clear the error after correction. | Accept the API’s 1–100 character save range. Link the error to the field and focus the field on an invalid submit. Send only the owned display-name change. |
| Saving | Keep the action position and show **Saving…**. | Prevent repeat submissions without losing keyboard focus. |
| Save confirmed | Show **Saved** with a check beside the action. | Announce completion once in a persistent polite status region. Keep the text immediately visible. The decorative check may fade in over 150 ms. Reduced motion shows the finished state immediately. |
| Save failed | Show **Couldn’t save your display name** and **Retry**. Preserve the entered name. | Recheck authorization before replay. Apply the latest authorized save response and suppress stale or late results after loss of access. |
| Registered email | Show **Verified** with an icon after confirmation. During an active refresh, show **Checking verification…**. Offer a scoped retry if refreshing fails. | Use the authorized account response for the displayed address and verification. Delegate identity management to the eligible Clerk flow. Refresh after return. If verification is required, use P03 before restoring private content. Use P07 for known restriction. |
| Sign out, no changes | Start sign-out directly. | Clear visible private data and active keys across tabs, stop private processing, and lock pending records to the same eligible account. A later eligible sign-in follows P04. |
| Sign out, unsaved change | **Sign out without saving?** with **Keep editing** and **Sign out**. Open immediately with **Keep editing** focused. | Trap focus within the modal. Escape and **Keep editing** close and return focus to the trigger. Confirmation proceeds with the same privacy transition. |
| Sign-out pending or failed | Show a neutral screen with **Signing out…**, or a scoped failure and retry. | Keep private data hidden throughout. Retry sign-out without restoring the profile or other private views. |

[Account read and write contract](../../API.md) · [Offline and sign-out contract](../../TRD.md#2-session-recording-and-offline-contracts) · [Clerk account management](https://clerk.com/docs/nextjs/reference/components/user/user-profile) · [Status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) · [Dialog keyboard behavior](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/)

## Motion and Pen.dev handoff

Use existing RAFIQ visuals and native Pen layers for the account field, verification, save feedback and confirmation. Use the dependency-free motion treatment from the shape. The component research references are [Motion opacity](https://motion.dev/docs/react-motion-component), [Motion SVG path animation](https://motion.dev/docs/react-svg-animation), [Motion Primitives Animated Group](https://motion-primitives.com/docs/animated-group), [Radix Alert Dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog), and [Animate UI Alert Dialog](https://animate-ui.com/docs/primitives/radix-ui/alert-dialog). Pen.dev shows the state frames. Check timing, reduced motion, keyboard and live announcements, authorization, provider return, and cross-tab privacy in the frontend.

The editable [RAFIQ Pen canvas](<../../../Pen Design/RAFIQ.pen>) contains **D19 / Profile / Desktop** (`m9Bu2`), **D19 / Profile / Narrow 390 px** (`Tl48f`), and **D19 / Profile / 320 px reflow** (`sDEqS`). The desktop reuses the driver navigation layers with Settings selected. The narrow layouts use the compact RAFIQ header and a settings section selector. **Form and identity states** (`WrddM`) shows the expanded selector, load and retry, verification refresh, and save states. Its **Saved** example instances RAFIQ’s existing inline job status component. **Sign-out states** (`qo6BQ`) includes the focused confirmation and private-data-free pending and retry outcomes.

## Acceptance checks

- Driver can find the current account, edit and save its display name, and reach D06, D22, Clerk, or sign-out from the expected settings location.
- Name feedback stays next to the action in every state. The verification text and form errors convey their meaning independently of color or motion.
- At narrow widths and browser zoom, values wrap, controls remain reachable with a keyboard, and the dialog and feedback fit the viewport.
- Canceling a confirmation preserves the name draft. Signing out stops private access across tabs and leaves pending records locked to their original account.

Confirm the exact Clerk entry point and enabled identity actions during integration. Treat screen values as synthetic design fixtures.
