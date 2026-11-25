# A08 Staff Access

**Approved for Pen.dev handoff on 25 November 2026 · Layout A and A08-C05. Mode · Operate.**

The user chose the **inline roster editor** and a **120 ms fade on the verification icon**. Use the existing RAFIQ table, checkbox and dialog treatments for the surrounding controls. [Design review and component research](A08-REVIEW.md)

## Purpose and entry

An Owner with verified admin access opens **Staff Access** from the internal admin navigation to identify administrators, review roles and grants, invite Staff, change or revoke access, appoint an eligible Owner, or reset another administrator’s authenticator. A01 handles recipient acceptance and authorized admin entry. A02 supplies the authenticator challenge and enrollment. A03 handles admin MFA recovery. A07 uses Staff permissions for driver account support, suspension and reinstatement. A09 shows the authorized audit history. [Screen requirements](../../SCREENS.md#a08-staff-access) · [Admin workflows](../../EXPERIENCE.md#admin-workflows) · [Technical requirements](../../TRD.md#71-admin-dashboard-fr-22)

## Frame and components

1. Keep **Staff Access** current in the internal admin shell. Put **Staff Access** and **Invite staff** at the top of the content area, above the **Administrators** table. Keep columns in this order: **Administrator**, **Role**, **Access**, **Assigned permissions**, **Manage**. Show **Admin ID** using the authorized UUID, **Owner** or **Staff**, and the returned access state as **Active**, **Enrollment required**, or **Access revoked**. Wrap the full ID in the editor and confirmation. Use **Load more** when a cursor is available. Keep row order stable through edits and refreshes.
2. **Manage access** opens an editor immediately below its row, with one editor open at a time. Lead with the target and current role, access state and grants. Place the draft checkboxes and **Review changes** after the current grants. Keep the eligible Owner-role, revoke and reset actions in a distinct group below. Show **Included with Owner role** for Owner access. If explicit assignments are returned for an Owner, label them separately from role-derived access. A local edit changes the draft. A confirmed server write changes the roster.
3. Keep the admin shell gutters and flat dividers. Use `colors.canvas`, `colors.ink`, `colors.accent-stone`, and the existing RAFIQ focus and status treatments. Use the established Space Grotesk treatment as the documented Mori substitute. Use `spacing.xl`, `spacing.md` and `spacing.sm` (24, 16 and 8 px) for sections, groups and closely related elements. Follow the existing confirmation surface and control radii. Reserve color and icons for supporting text labels and focus cues. [Visual tokens](../../DESIGN.md) · [A05 roster layout reference](A05-SHAPE.md)

| Component | Treatment and canvas reference |
| --- | --- |
| Roster | Use a semantic table with scoped column headers and an identified row action. Match the RAFIQ **Horizontal status row** (`Yh4JZ`) and **Stacked status row** (`fqIDy`). At narrow widths use a labeled list with the same information. |
| Inline access editor | New RAFIQ composition using labeled native checkboxes. Reuse visual treatment from the D20 checkbox (`B720aK`) and D24 permission row (`JoMRk`). Use one **Permissions** group with visible help. |
| Invitation and confirmation | Reuse the centered confirmation frame (`f1ZMyr`), existing labeled email field and actions, and the approved A02 six-slot visual treatment over one labeled authenticator input. Use the A02 sensitive action storyboard (`ITZ0z`) for the transition from verification to confirmation. |
| Change review, conflict and invitation receipt | New RAFIQ compositions using ordinary headings, lists, selectable text, buttons and status messages. Present important changes next to the target and operation. |

[RAFIQ canvas](<../../../Pen Design/RAFIQ.pen>) · [A02 handoff](A02-SHAPE.md) · [Table semantics](https://www.w3.org/WAI/tutorials/tables/)

## Permission editor and invitations

| Checkbox | Meaning shown in the editor and invitation form |
| --- | --- |
| **View metrics** | View Service Health, Release Readiness and approved Adoption aggregates. |
| **Account support** | Find an exact driver account and request eligible verification or recovery messages. |
| **Suspension** | Suspend and reinstate driver accounts with fresh verification. Show “Suspend and reinstate require Account support as well as Suspension” beside the checkbox. |

Keep the three assignments independent. When Suspension is assigned without Account support, use **Assigned · Account support required to use** in the effective-access explanation. If Account support is removed while Suspension stays assigned, explicitly show that suspend and reinstate will become unavailable. For example, show **Removed · Account support**, then **Suspend and reinstate will become unavailable**. Keep **Suspension** in the proposed assigned list. [Permission definitions](../../TRD.md#71-admin-dashboard-fr-22)

**Invite staff** opens the labeled **Registered email** field and the three permission choices. **Review invitation** opens **Create staff invitation?** in the same dialog with the exact email and grants. Explain that the link is single-use and expires, and that the recipient must verify the matching email and enroll an authenticator. After fresh verification, **Create invitation** sends the explicit final request. On confirmed creation show **Invitation created**, the selectable link, **Copy invitation link**, and an absolute date, time and zone derived from `expiresAt`. Report copy success inline. If copy fails, keep the text selectable and explain manual copying. Use **Invitation expired** if the link expires while displayed. Clear the link on expiry, receipt closure, workspace exit or access loss. A01 owns redemption and recipient errors. [Invitation API](../../API.md#7-detailed-endpoint--operation-specifications) · [A01 handoff](A01-SHAPE.md)

## Review, fresh verification and commit

Use one dialog for each operation. Keep the named target, exact change and consequence visible throughout review and **Verify to continue**. A successful challenge returns to the confirmation with **Identity verified** and the named final action. That action requires explicit activation. If freshness expires, show **Verify again to continue** and keep the authorized draft while the action remains eligible. Use A02 feedback for invalid or reused codes and rate limiting. The service rechecks the acting Owner’s authority, fresh verification and target eligibility at commit. [A02 sensitive actions](A02-SHAPE.md#returning-sign-in-and-sensitive-actions) · [Admin access checks](../../TRD.md#71-admin-dashboard-fr-22)

| Final action | Confirmation and outcome |
| --- | --- |
| **Save permissions** | List **Added** and **Removed** permissions and their consequences. Say when removal ends access immediately. Update the affected row on success and announce **Permissions updated**, naming the removed permission when applicable. |
| **Revoke admin access** | Show the target’s role and explain that access to the internal dashboard ends immediately, including in open sessions. On success apply **Access revoked** and update the authorized roster. Remove protected data, controls, pending responses and dialogs in the affected session as soon as invalidation is known. |
| **Appoint Owner** | Offer only for eligible MFA-protected Staff. Explain that the role includes all dashboard permissions, Staff Access and Audit. For an eligible **Change to Staff**, show the resulting Staff grants and loss of Owner privileges. Check last-Owner protection on any operation that would remove an active Owner. |
| **Reset authenticator** | Offer for another eligible administrator. Explain that their current admin sessions lose authority and they must sign in and enroll again. Show the confirmed reset inline and reload the target’s access state. A03 and A02 handle the affected administrator’s eligible recovery and enrollment. Use audited deployment recovery if the last Owner loses their authenticator and recovery codes. |

## Required states

| State | Presentation |
| --- | --- |
| Initial load, empty or read failure | **Loading administrators…**. Keep the Owner row when no Staff exist and show **No staff administrators yet** and **Invite staff**. A wholly empty authorized response shows **No administrators returned** and **Reload**. Show **Retry** for a failed read. Label visible earlier results **Last loaded results** and refresh before editing them. |
| Submitting or rejected | Name the pending operation, such as **Saving permissions…**. Suppress duplicate submits. Show action-specific errors and preserve the eligible draft. If a retry time is available, display it. |
| **Permission conflict** | Show **Permissions changed while you were editing**. Compare **Current permissions** with **Your draft**, including any role or access-state change. Block the stale confirmation. **Reload and review** gets the current grants so the Owner can reapply intended changes and review them again. Keep the old selection as a reference only while authorized. A business-rule conflict points to the affected permission or state. |
| **Last Owner protected** | With confirmed eligibility data, explain beside the protected action “At least one active Owner is required.” A concurrent rejection with `last_owner_required` shows **This is the last active Owner** and **Back to staff access**. Refresh the roster and explain that another eligible MFA-protected administrator must first be appointed. |
| Uncertain result | Show **Couldn’t confirm the result**. Reconcile with current server state before a retry. If invitation creation lost its receipt, show no link and use the qualified recovery path. Apply the same reconciliation rule before repeating a reset. |
| **Authority lost** | Close the dialog immediately. Clear affected roster data, drafts, invitation links and late responses. Recheck admin entry. Send a demoted Owner to a still-permitted destination if available, or show the appropriate A01 outcome for revoked access. If only the target changed, and the acting Owner retains authority, show the current eligible target state or **Administrator unavailable**. |

## Approved motion and accessibility

| Moment | Standard | Reduced motion |
| --- | --- | --- |
| Server confirms fresh verification | Restore the dialog content and focus immediately at 0 ms. Show **Identity verified** and the final action. Fade the decorative icon beside **Identity verified** from transparent to fully visible over **120 ms**, ease-out, with its space reserved from the start. | Show the final icon, text, action and focus immediately. |
| All other state changes | Update immediately. Keep failures, conflict, protection and access clearing independent of the cue. | Same immediate behavior. |

A08-C05 uses the existing RAFIQ icon as the decorative child of a Motion for React enter animation. The text conveys the state to assistive technology. Use `useReducedMotion` to bypass the fade entirely. Motion is MIT licensed. Preserve its copyright and permission notices when distributing covered code. [Enter animation](https://motion.dev/docs/react-animation#enter-animations) · [Reduced-motion hook](https://motion.dev/docs/react-use-reduced-motion) · [Source and license](https://github.com/motiondivision/motion/blob/main/LICENSE.md)

Use visible focus, associated field help and errors, and accessible row action names that include the target. Put focus inside the modal at the heading or first field for form entry and at the safe option for destructive confirmation where appropriate. Keep Tab and Shift+Tab within the modal, support Escape for safe cancellation, and restore focus to the initiating action or nearest safe heading if the action disappeared. Focus the restored confirmation on verified return. Announce asynchronous outcomes once and convey all access states in text. [Modal focus guidance](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

## Pen.dev frames and acceptance

- Draw **1440 px** and **1024 px** desktop frames, plus a **320 CSS px** single-column reflow. Keep long IDs and invitation links wrapping, the opened editor directly under its row or item, and dialogs scrollable along one axis. Use fictional UUIDs, an `example.net` recipient, inert invitation links and synthetic dates. Verify **200% browser zoom** during frontend acceptance. [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Include a state board for loaded, loading, no Staff, read failure, draft, conflict, successful revocation, last-Owner protection, appointment, reset, failed save, uncertain outcome and cleared access. Show invitation entry, review, receipt and expired link. On the verification board show review, active verification, restored confirmation at **0 ms**, the icon at **120 ms**, and the reduced-motion result.
- Check target continuity, including when an Owner moves from the editor into verification and back. Verify the A02 challenge alone cannot commit an operation. Exercise the Suspension dependency, a stale permission edit, concurrent last-Owner removal attempts, another administrator’s reset, and access lost mid-dialog. Confirm that the roster only reflects saved data and that loss of authority clears protected content even with motion enabled. Pen.dev frames represent composition, focus intent and motion endpoints. Frontend tests cover timers, focus, keyboard and assistive technology, confirmation gating, concurrency and live access invalidation.

## Open implementation inputs

- Use the current UUID-based roster fields for design. Confirm any additional authorized identifier, action eligibility, revoked-row retention and protection when reset could leave no active Owner. The documented invitation endpoint supports creating a receipt with a link and expiry. Persistent invitation management would require a product and API decision. [Admin endpoints and schemas](../../API.md#7-detailed-endpoint--operation-specifications)
- Define the stale-write precondition and typed conflict data. `putStaffAccess` describes a full replacement and generic `409`. Confirm how an open session learns about authority loss and how to reconcile an ambiguous invitation create or reset. Confirm the verified admin origin and the display time zone for the invitation receipt. [Access and reset operations](../../API.md#7-detailed-endpoint--operation-specifications) · [Administration architecture](../../ARCHITECTURE.md#module-m09--administration)
