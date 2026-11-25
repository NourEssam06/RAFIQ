# A02 Authenticator enrollment and challenge

**Mode** · Operate. **Status** · Approved for Pen.dev handoff on 25 November 2026.

The user approved **A · Three guided steps**, **Copy recovery codes with a saved acknowledgement**, and **static RAFIQ feedback**. Use **A02-C01** for the six-slot field treatment, **A02-C03** for the step indicator, and **A02-C06** for verification and copy status. [Design proposal and component research](A02-REVIEW.md)

## Entry and outcome

An eligible invited or recovering Owner or Staff member sets up an authenticator and saves their recovery codes. An enrolled admin verifies their sign-in. An admin who has reached a sensitive action verifies again inside its confirmation dialog. A01 establishes verified identity and admin eligibility. A03 handles recovery and returns eligible admins to fresh enrollment. A07 and A08 own their privileged confirmations and final submit actions. [A02 screen requirements](../../SCREENS.md#a02-authenticator-enrollment-and-challenge) · [Admin journey](../../EXPERIENCE.md#j8-operate-rafiq-and-support-an-account)

## Layout and visual references

- **Pre-dashboard route.** Use the compact RAFIQ wordmark and an admin access heading above a centered form column. The header, progress, active heading, instructions, controls, status and actions appear in that order. Use the same panel position across enrollment steps. The returning sign-in challenge uses the same column and places its recovery link after Verify. Keep admin navigation behind confirmed access.
- **Sensitive-action dialog.** Reuse the origin’s single confirmation dialog. Place the named action, authorized target, consequence and approved reason, when applicable, before the OTP field. Follow it with status, **Cancel** and **Verify to continue**. On verified return, restore the confirmation phase with **Identity verified** and the original final action button. The admin explicitly confirms the action after returning. Place the final result in the originating view.
- **Visual tokens.** Use `colors.canvas` for the page, `colors.ink` for text, and `colors.accent-stone` for secondary content. Follow the existing Space Grotesk treatment documented as Mori’s substitute. Reuse P03/P05’s cyan outline for the verification control, six-slot field treatment, and the confirmation dialog’s focus, surface and action hierarchy. Use `spacing.xl` / `md` / `sm` (24 / 16 / 8 px) between regions, within groups and between related labels. Use `rounded.md` where the established form components call for it. Give the desktop column roughly 480–520 px at 1440 px and 20 px gutters at 390 px. At 1024 px, 200% zoom and 320 CSS px, let text and actions wrap in reading order. Keep the QR square, the OTP field within the column, and focused controls visible while pages and dialogs scroll. Use standard single-axis scrolling to reach Verify with the mobile keyboard open. [DESIGN.md](../../DESIGN.md) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

| Component | Treatment and reference |
| --- | --- |
| Header, OTP field and Verify button | Reuse visual conventions from P03 Verify email (`cYZwN`) and P05 Verifying (`hpVN8`). A02-C01 is one native labeled field behind six visual slots. |
| Confirmation dialog | Reuse the confirmation frame (`f1ZMyr`) for the dialog’s content order and focus treatment. A07 and A08 supply action-specific labels. |
| Enrollment progress | A02-C03. Render a static ordered list with the current item marked in text and with `aria-current="step"`. A narrow layout can summarize the current item as “Step 2 of 3 · Verify code”. Back and Continue are panel actions. |
| Status feedback | A02-C06. Reuse RAFIQ controls and standard status semantics. Keep visible feedback near the control that produced it. |
| Authenticator setup and recovery panel | New RAFIQ compositions built from an ordinary disclosure, selectable text, button, list and checkbox. Use fake, visibly marked credentials and a non-scannable QR illustration in Pen.dev. |

[RAFIQ Pen.dev design](../../../Pen%20Design/RAFIQ.pen) · [USWDS step indicator](https://designsystem.digital.gov/components/step-indicator/) · [WCAG status examples](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

## Guided enrollment

1. **Connect authenticator.** Show a short instruction to add RAFIQ in the authenticator app, then the QR and **Enter a setup key instead**. The disclosure provides a selectable setup key and same-device instructions. **Continue** opens step 2 while the enrollment is current. Tie the QR and manual key to the same enrollment. The frontend renders the QR locally from the private setup URI.
2. **Verify code.** Show the labeled **Authenticator code** field and “Enter the 6-digit code from your authenticator app.” Place **Verify** and **Back** below the field with feedback adjacent. Back returns to the same setup details while they remain eligible. Verify or Enter submits the current value. Move focus to the next heading only when the server confirms setup and returns codes.
3. **Save recovery codes.** Lead with “You’ll only see these codes once. Store them somewhere secure. Each code works once if you lose access to your authenticator.” Display the issued array as selectable text. Let long values wrap without changing their characters or order. Stack each code on its own row on narrow frames. Then place **Copy recovery codes**, its adjacent status, the unchecked **I’ve saved my recovery codes** acknowledgement, and **Continue**. Explain the acknowledgement requirement before Continue and associate any missing-confirmation error with the checkbox. After Continue, clear the codes and resolve the authorized destination. The acknowledgement gates this screen’s Continue action and enrollment is already verified at this step.

**Copy recovery codes** copies one exact code per line on explicit activation. Keep the button label and focus stable. After a confirmed write, show **Recovery codes copied**. On denial or failure, show **Couldn’t copy. Select the codes to copy them manually.** Keep the list selectable in both cases. Copying leaves the acknowledgement for the admin to complete. The setup key has the manual selection path. [Clipboard write behavior](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/writeText) · [Recovery-code presentation reference](https://www.login.gov/help/create-account/authentication-methods/backup-codes/)

## Returning sign-in and sensitive actions

- **Verify your sign-in.** Reuse the authenticator input and **Verify** action. **Can’t use your authenticator?** opens A03. On success, resolve the authorized requested destination, Service Health when permitted, or the first permitted view. With no eligible views, explain the current access status and offer sign-out.
- **Verify to continue.** Keep the action and target visible through step-up. Success restores the confirmation and focuses its heading or appropriate control. **Cancel** or Escape exits verification through the origin’s cancel behavior. Restore the draft and approved reason after recoverable failures only while the action and target remain authorized. If the admin follows an eligible A03 recovery route from this flow, discard the pending privileged continuation. A03 requires a verified sign-in and consumes an unused recovery code or follows the approved reset path before fresh enrollment in A02.

## State frames and accessibility

| State | Pen.dev frame and frontend behavior |
| --- | --- |
| Preparing setup | **Preparing authenticator setup…** in the form location. Show **Try again** after a confirmed temporary failure, when eligible. |
| Default and keyboard focus | Show slots with one visible focus treatment for the field. Annotate the single input’s label, hint, numeric input mode, and `autocomplete="one-time-code"` where supported. Test full-code paste, spaced paste, leading zeros, edit, replacement and supported autofill. Preserve explicit verification after paste or autofill. |
| Incomplete | Show **Enter all 6 digits** in the associated field error. Focus the field when correction is needed. |
| Verifying | Keep the form and button position stable. Display and announce **Verifying code…** once. Guard duplicate submissions until the attempt resolves. Keep the step-up cancel action available. |
| Rejected or reused | Show **This code didn’t work. Enter a new code from your authenticator app.** Clear the rejected value and return focus when correction is needed. |
| Expired enrollment | Clear the QR, setup key and entered code. Show **Setup expired** and, if eligible, **Start setup again**. |
| Rate limited | Show **Too many attempts. Try a new code later.** Display a readable retry time only when supplied by the server. Preserve an eligible recovery or exit path. Announce the start and end of the wait once each and recheck current authority before allowing a fresh attempt. |
| Offline or uncertain outcome | Explain that verification could not be confirmed and provide an eligible exit. On reconnect, resolve admin entry and authority before retry. If enrollment completed but the response that issued codes was lost, show **Recovery codes unavailable** and the authorized recovery or reset path when needed. Step-up remains pending until fresh verification is established. |
| Verified | Show **Save recovery codes** on authorized enrollment receipt, the permitted destination after sign-in, or **Identity verified** on the returned action confirmation. The originating form shows its own final outcome after it receives one. |
| No permitted views or access changed | Show the appropriate current access state. On session loss, identity switch, or revocation, close the affected flow, clear secrets and newly unauthorized context, and discard late responses. Offer fresh sign-in, sign-out or return to a still-authorized view as applicable. |

Use visible focus and a logical tab order. Associate hints and errors to their controls and pair color with text. On a route or step change, focus the heading. Announce routine updates through a status region without automatically announcing the codes. Use the existing modal focus boundary and restore focus to the opener or nearest authorized surviving control on exit. [Accessible authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) · [Modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

## Static feedback storyboard and Pen.dev checks

- Build separate labeled frames for **Setup / QR**, **Setup / manual key**, **Verify code / focus**, **Save recovery codes**, **Verify your sign-in**, and **Sensitive action / verify / confirmation restored**. Use 1440 px for the main flow, 1024 px for a narrow desktop pass, and 390 px and 320 px to prove reflow for setup, the longest code list and a long action target. Include copies of the affected component or frame for the states in the table.
- Storyboard **ready → verifying → result**, **ready to copy → copied or copy unavailable**, and **step-up → confirmation restored or access changed** as immediate visual state changes. Use stable control geometry, visible status text and an optional static icon. The reduced-motion version uses the same frames and timing. Annotate the triggering event and the focus destination on every changed frame.
- Pen.dev shows visual hierarchy, focus examples, copy and status variants, and reflow. Browser and API acceptance requires keyboard and screen-reader operation, a single tabbable OTP control, copy success and denial, one-time issuance and single-use redemption, credential teardown on exit and browser restore, throttle enforcement, rejection of reused codes, and authority changes during slow or in-flight requests. Test that a late success cannot reopen a revoked flow and that step-up never commits the privileged action by itself.

## Security and open contracts

Enrollment uses the active enrollment ID and server `expiresAt`. Challenge and step-up accept a current unused TOTP. Keep verification and freshness tied to the verified Clerk session. Recheck grants and target eligibility at commit. Use `private, no-store` responses and transient client state. Keep setup information and codes out of URLs, persistent state, diagnostics, audit and analytics. Discard secrets on exit, reload, session changes and access loss. Store encrypted TOTP secrets and hashed single-use recovery codes on the server. After a lost response, resolve current entry state before another attempt and preserve the distinction between normal sign-in verification and fresh verification for a sensitive action.

Confirm recovery-code count and format, the freshness window, safe problem codes and retry metadata, and how open screens detect permission changes. Use illustrative code values and an unspecified delay in the Pen.dev frames until the API contracts are qualified. [API operations](../../API.md#7-detailed-endpoint--operation-specifications) · [Security and reliability](../../API.md#12-security-and-reliability-requirements) · [Open contract decisions](../../API.md#18-open-questions-and-decisions-requiring-approval) · [MFA and recovery requirements](../../TRD.md#6-external-protocols)
