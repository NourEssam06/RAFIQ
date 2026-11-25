# A07 Account Support

**Mode** · Operate. **Status** · Approved for Pen.dev handoff on 25 November 2026.

The user approved **A · Stacked lookup and result** and **A07-C01 · Static RAFIQ feedback and native Reason select**. This handoff covers the design of one staff workspace and its confirmation states. [Layout alternatives and component research](A07-REVIEW.md)

## Entry and page structure

Open **Account Support** from the internal navigation for an Owner or Staff member with Account support. It can also be the first permitted destination after A01 and A02. The task is to find one known driver account, check its identity and act within the viewer’s current permission. A02 supplies the fresh authenticator challenge inside A07. A03 handles authenticator recovery, A09 is the Owner-only audit view, and D22 is the driver’s deletion flow. Leaving A07 clears the query, record and action draft. [A07 requirements](../../SCREENS.md#a07-account-support) · [Support journey](../../EXPERIENCE.md#j8-operate-rafiq-and-support-an-account)

Use the established RAFIQ admin shell with **Account Support** marked current. Stack the following in one working column.

1. **Account Support** heading. Use a native text field labeled **Registered email or account ID**, hint “Enter the full registered email or account ID.” and a **Find account** button. Support paste and Enter. Suppress suggestions, autocorrection and automatic capitalization. Submit a single email or full account UUID through the exact-match API, which applies provider normalization. Use a nearby search status. Clear the old record and its actions when the input is edited, cleared or submitted again. Ignore superseded responses. [Search form reference](https://designsystem.digital.gov/components/search/) · [Exact lookup contract](../../API.md#7-detailed-endpoint--operation-specifications)
2. **Account record**. Use a five-row description list in the order below. Keep the ID and email selectable. Wrap them without ellipses or character changes. No driver attributes beyond the five fields enter this view. [Summary list reference](https://design-system.service.gov.uk/components/summary-list/) · [Field allowlist](../../SCREENS.md#a07-account-support)
3. **Support actions**, below a divider. Offer **Request verification email** for an eligible unverified account, or **Request recovery email** when the identity lifecycle permits it. Show the fixed registered destination and local feedback. Show **Suspend account** for an eligible active account or **Reinstate account** for an eligible restricted account when the viewer is an Owner or has both Account support and Suspension. If the account has no available actions for the viewer, show “No support actions are available for this account.” Keep the lookup and message progress independent. [Permission and message rules](../../TRD.md#71-admin-dashboard-fr-22)

| Label | Pen.dev example | Source field |
| --- | --- | --- |
| Account ID | 8e3a6200-4d85-4abd-a790-000000000001 | `accountId` |
| Registered email | nour@example.net | `registeredEmail` |
| Verification status | Verified / Unverified | `verificationStatus` |
| Account status | Active / Restricted | `accountStatus` |
| Signup date | 9 Nov 2026 | `signedUpAt` |

## Confirmation and fresh verification

Use one named modal with three phases. Bind the draft to the matched target and action throughout. [Approved A02 interactive pattern](A02-SHAPE.md) · [Modal accessibility](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

| Phase | Drawing and behavior |
| --- | --- |
| **Review** | **Suspend account?** or **Reinstate account?** followed by the registered email, account ID, consequence, required **Reason** select, **Cancel** and **Continue to verification**. Start with “Select a reason.” Display only approved codes for that action using staff-facing labels. If the catalog is unavailable, explain why progression is blocked. Use annotated illustrative choices in the Pen.dev frame. |
| **Verify** | Keep the title, target, consequence and selected reason in view. Reuse A02-C01, one labeled pasteable **Authenticator code** field represented by six slots, with **Verify to continue**, **Cancel**, and inline A02-C06 feedback. Clear the submitted code. A03 recovery exits this action. |
| **Confirm** | Replace code entry with **Identity verified**. Show **Cancel** and the explicit final **Suspend account** or **Reinstate account** button. Verification returns to this phase. The final button commits after current grants, fresh verification, target eligibility and approved reason are checked. On confirmed success, close the modal, apply the five-field response and show **Account suspended** or **Account reinstated** in Support actions. |

**Suspend consequence.** “This removes hosted access immediately, stops sync, and invalidates existing hosted sessions and grants. A monitoring session already running offline keeps its local warnings within its existing limits.”

**Reinstate consequence.** “The driver must sign in again to regain eligible hosted access and sync. Reconnecting an MCP client requires fresh consent.” [Lifecycle requirements](../../TRD.md#71-admin-dashboard-fr-22)

## State board

| State to draw | Visible result or recovery |
| --- | --- |
| Empty, searching, invalid input, no match | Empty shows the input and hint. Searching shows “Searching…” in place. Associate malformed input feedback with the field. For an authorized exact miss, show “No account matches that email or account ID.” These states have no account record or support actions. |
| Lookup rate limited or unavailable | Show “Too many lookup attempts. Try again later.” or “Couldn’t look up the account. Try again.” Preserve the query for correction or retry. Respect a server retry hint when provided. |
| Matched with different permissions or eligibility | Include a support-only account with a message action, an active account with Suspend, a restricted account with Reinstate, and a record with no eligible actions. Keep verification and lifecycle status distinct. |
| Message pending, accepted, or unsuccessful | Show a pending state adjacent to the action and prevent duplicate activation. A confirmed 202 produces **Verification email request accepted** or **Recovery email request accepted**. For a rate limit, unavailable operation or unconfirmed response, show the safe retry state. “We couldn’t confirm the email request” covers an ambiguous outcome. Retry the same intent with its original idempotency key and current eligibility. |
| Reason missing or rejected | Keep the dialog open, associate the error with **Reason**, and require a valid choice before continuing. If the reason is still valid, retain it across recoverable failures for the same action and target. |
| Verification pending, invalid, reused, limited or expired | Show **Verifying…** or “That code couldn’t be verified. Enter a new code from your authenticator app.” Honor rate limits. If fresh verification expires before commitment, return to the challenge with the reason preserved. |
| Commit pending, confirmed, conflicting or unconfirmed | Show **Suspending account…** or **Reinstating account…** and prevent duplicate submits. Claim success only after a confirmed result. For conflict, refresh eligibility and require new review if the action changes. For an ambiguous result, show “We couldn’t confirm the account change,” then reconcile through an authorized refresh or an identical retry as supported by the contract. |
| Target or permission withdrawn | Target unavailable clears its record and actions and returns to lookup. Suspension permission loss closes and clears the privileged dialog and leaves authorized support available. Account support or session loss clears the query, record, draft and pending UI, then routes to a permitted view or admin entry. Late responses from the old authority or target are discarded. |

The server binds message delivery to the registered email and protects rate limits, exact lookup, private uncached responses and audit. Staff feedback contains no credentials, message payloads, raw provider errors or audit rows. [Admin API operations](../../API.md#7-detailed-endpoint--operation-specifications) · [Error handling](../../API.md#11-error-handling-standards)

## Pen.dev layout and component references

- Use `colors.canvas`, `colors.ink` and `colors.accent-stone`. Use the established Space Grotesk treatment as the Mori substitute. Use `typography.h1` for the page title, `typography.h2` for the dialog title, and the established form and body styles for operational text. Use the RAFIQ cyan focus treatment, thin dividers and `rounded.md` for form surfaces. Keep the action labels literal and pair all status colors with text. [RAFIQ design tokens](../../DESIGN.md)
- Start with a working column up to 720 px inside the available admin content area. Use `spacing.xl` (24 px) between sections, `spacing.md` (16 px) inside panels and `spacing.sm` (8 px) between related elements. At desktop size, align labels on one edge and allow values the remaining width. Use the A02 600 px dialog reference with a neutral `#191c19` surface and 24 px padding. At narrow widths use about 20 px gutters where space permits. Keep the label above each value, and stack form controls and action buttons in reading order when they no longer fit.
- Inspect **1440 px** and **1024 px** desktop frames plus **320 CSS px** reflow. Include a long synthetic email, a full UUID and long illustrative reason labels. Check 200% browser zoom when implemented. Keep content on one scroll axis with focused controls fully visible. [WCAG Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Reuse the A02 confirmation visual reference (`f1ZMyr`), verification and verified-return frames (`ANDVZ`, `FbmoT`), the A02-C01 six-slot field and A02-C06 info, success and error variants (`dWj0o`, `iDe41`, `agm17`). Compose the record and support actions from RAFIQ typography, buttons, dividers and status treatments. Show the closed empty select, an open list and a selected reason. Keep fixture credentials masked or clearly illustrative. [RAFIQ Pen.dev file](../../../Pen%20Design/RAFIQ.pen)

## Static feedback and acceptance

Make a storyboard of three static dialog states, followed by a confirmed outcome in Support actions. Each state updates immediately on its event. Use text for pending states. Reduced motion uses the same sequence and presentation. Pen.dev frames show composition, values, feedback, keyboard-focus appearance and state changes. The frontend supplies actual authorization, asynchronous state, keyboard semantics and screen-reader announcements.

The handoff is ready for review when the Pen.dev frames show the exact lookup, all five fields, eligible actions below the record, both confirmation types, and the state board. Frontend acceptance includes the following.

- Test exact email and UUID search, privacy on authorization loss, stale lookup responses, and the five-field response boundary. Test the message destination and distinguish acceptance from delivery.
- Test support-only and support-plus-suspension Staff and Owners, stale target state, invalid or reused authenticator codes, expired verification, reason retention, duplicate submits, uncertain outcomes and permission loss during every action phase.
- Test visible focus, associated errors, Escape before committing, focus containment in the modal, and restoration to the initiating action or next surviving control after it closes. Initial focus goes to the dialog heading so the target and consequences can be read in order. Announce ordinary status via a live region and urgent blocking errors with alert semantics. Enter in the code field submits verification only. [WCAG Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) · [Modal keyboard guidance](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#keyboardinteraction)

**Open product inputs.** Confirm the reason catalog and labels, how the UI receives message eligibility within the five-field boundary, fresh verification duration and safe retry/error mapping, and the date display basis. The sample reason labels, working column width and narrow layout measurements are design proposals for Pen.dev. [API contract](../../API.md) · [Technical requirements](../../TRD.md#71-admin-dashboard-fr-22)
