# D02 — Start session and readiness

## Approved direction

An eligible adult driver opens **Start session** from D01 and prepares a controlled session while stationary. The camera-first workspace keeps the built-in camera preview and the readiness checks in view together. **Start monitoring** opens D03 after admission. **Cancel** returns to the originating surface and restores focus to its start action when it is still available.

The approved motion is brief RAFIQ status feedback. Use the existing Compact arc for real verification and initialization waits and a short change of treatment on a passed check. Use standard form controls and a custom static framing guide. The chosen design uses no external component dependency. If the driver chooses **Don’t save clips this session**, the session starts without clip capture when the other checks pass. The saved account preference remains in effect for future sessions.

The layout comparison included a three-step setup for **Camera**, **Session and clips**, and **Review**. That option borrows the focused reading order of P06 and gives each decision more space, especially at narrow widths. The driver may have to return to the Camera step if the feed changes before starting. The approved workspace uses D01’s private-app hierarchy and keeps the preview and its current blocker visible together while the driver adjusts the camera view. It also keeps the clip choice and start action on the same page.

[Screen requirements](../../SCREENS.md#d02-start-session-and-readiness) · [Session transitions](../../EXPERIENCE.md#readiness-monitoring-and-recovery) · [Approved Dashboard](D01-SHAPE.md)

## Frame and hierarchy

1. Use a compact RAFIQ workspace header, followed by **Start session** and **Complete setup while stationary.** Show the current controlled-use conditions status and a route to review the conditions. Send required acceptance to P06. Use the RAFIQ identity and button treatment from D01 and the succinct conditions presentation from P06.
2. On a 1440 px review frame, start with D01’s 48 px outer gutters. Give the camera panel roughly three fifths of the workspace and the configuration column the remaining width. Treat the split as a starting proportion and stack when the preview or configuration becomes cramped.
3. In the camera panel, show **Camera preview**, a stable preview area with the feed’s proportions preserved, and a fixed face and upper-body framing guide. Show readable guidance beneath the preview, for example “Sit so your face and upper body are visible. Keep your face evenly lit.” Put **Enable camera** or **Recheck** in this panel when applicable. Show “Live preview stays on this device” next to the preview.
4. In the configuration column, place **Readiness checks** first, followed by **Session type** and **Incident clips**. The checklist contains **Camera access**, **Usable view**, **Monitoring files**, **Monitoring initialization**, and **Account and conditions**. Each row pairs a short text state with an icon. Place corrective actions beside their affected section with a clear label. Readiness rows reflect verified results and have no user-controlled checkboxes.
5. Place **Cancel**, **Start monitoring**, and the current reason for any unavailable start together in a workspace action row. Allow the reason to wrap. When all gates pass, show **Ready to start**. Start remains a driver action even when the system finishes the last check.

Use `{colors.canvas}`, `{colors.ink}`, `{colors.accent-stone}`, and the existing accent for focused and active controls. Use text and icon shape as well as color for statuses. Follow `{typography.h1}`, `{typography.h2}`, and `{typography.body}` with Mori where licensed or the D01 Space Grotesk fallback. Use `{spacing.xl}` between primary sections, `{spacing.md}` for panel insets and field groups, and `{spacing.base}` or `{spacing.sm}` inside rows. Apply `{rounded.md}` to panels and the shared outline treatment to secondary actions. Keep the four framing corners legible against light and dark video with a contrasting edge. [Design foundations](../../DESIGN.md)

## Camera and readiness behavior

**Enable camera** requests built-in camera video through the browser while stationary. The browser supplies the permission prompt. In RAFIQ, show the waiting status beside the preview. Keep the preview surface stable while it opens, checks the view, or shows an actionable error. The overlay shows the intended composition. A separate text result reports whether RAFIQ currently has a usable view, using a specific reason when available. The camera and vision module owns usable-view decisions. Preview proportions and overlay placement must remain consistent as the panel resizes. [Browser media permissions](https://www.w3.org/TR/mediacapture-streams/) · [Chrome camera permission recovery](https://support.google.com/chrome/answer/2693767?hl=en)

| State | Visible result and next action |
| --- | --- |
| Initial, camera off | Reserve the preview area and explain the camera-only request. Offer **Enable camera** when the setup can proceed. |
| Permission request open | Show **Waiting for camera permission** and keep **Cancel** available. |
| Permission blocked or no access granted | Keep the preview off. Explain how to allow RAFIQ’s camera in Chrome site permissions and, when applicable, Windows settings. Offer **Recheck** after correction. |
| Missing camera or camera busy/unavailable | Name the reason when known. Ask the driver to enable the built-in camera or close the app using it as applicable. Offer **Recheck**. |
| Camera connected, checking or correcting the view | Show the preview, **Checking view**, or a specific correction such as **Move into better light** or **Keep your face and upper body in view**. Offer **Recheck** after correction. Confirm **Usable view** once supported. Camera or feed loss invalidates its prior result. |
| Vision bundle verification | Show **Verifying monitoring files…**. Mark the row passed when verification completes. |
| Vision initialization | Show **Initializing monitoring…** after verification passes. Keep the initialization result separate. |
| Missing or invalid assets | Show **Monitoring files couldn’t be verified** with **Retry setup**. |
| Verified assets fail to initialize | Show **Monitoring couldn’t start** with **Retry setup**. Keep the verified-files result visible while it is still valid. |
| Account loading or temporary eligibility failure | Show **Checking account eligibility…** or an inline **Retry**. A ready state requires current online eligibility and current accepted conditions. |
| Signed out, verification required, conditions changed, restricted | Follow the matching P04, P03, P06, or P07 route. When access is lost, release preview and clear private setup details. Resume an authorized D02 entry with fresh checks where applicable. |
| Offline before start | Show **Connect to the internet to start a new session**. After reconnect, recheck current eligibility. An already admitted session follows the D03 offline rules. |
| Unsupported setup | Identify the supported desktop setup. Treat Chrome on Windows 11 with a built-in camera as the qualification baseline. Provide a route back. |
| Start submitted | Show **Starting monitoring…** and prevent duplicate submission. A rejected or interrupted admission keeps or restores valid inputs. Refresh the affected authority or device checks and offer recovery from the specific result. Open D03 only after admission. |

Keep the preview on-device. Cancel or leaving D02 without admission releases the camera and clears the temporary setup. The frontend handles cleanup if a permission request resolves after the driver has left. Active monitoring and optional clip capture belong to the admitted D03 session. [TRD session requirements](../../TRD.md#2-session-recording-and-offline-contracts) · [Local monitoring and admission contract](../../API.md#9-real-time-and-event-contracts)

## Session type and supervision

- Use a labeled session-type radio group. Offer **Stationary** and show **Supervised** when eligible. Both complete setup while stationary. Keep the approved supervised-use procedure available at the point of choice.
- In the supervised section, show the designated supervisor and **Authorize supervisor**. Explain the exact delegated actions on the driver’s device: acknowledge warnings, cancel pending contact alerts, and pause monitoring. Show whether authorization is pending, active, or revoked. Give the stationary driver **Revoke access**. Start, resume, end, settings, and record review stay with the driver. Authorization expires when the session ends.
- Show **Emergency Mode** as a separate status under supervised setup, with the current eligibility or unavailable reason where known. If qualified contact channels are missing, link to **Emergency contacts** in D21 for the stationary driver. Ordinary warnings remain available in an otherwise eligible session. If supervision is unavailable, offer the stationary setup and keep supervised workflows that require interaction during motion unavailable.
- Illustrate supervised eligibility, delegation, and revocation as conditional Pen variants. Use the approved supervised procedure and release evidence to determine when ship-ready eligibility can be shown. D03 owns the passive presentation during motion. [Supervised procedure and release gates](../../PRD.md#82-device-and-supervisor-qualification) · [Emergency Mode](../../SCREENS.md#d04-emergency-mode)

## Incident clips and admission

Use an equal-weight labeled radio group with **Save incident clips** and **Don’t save clips this session**. Explain that RAFIQ can save video-only clips of eligible incidents for selected categories, and that monitoring is available either way. For first use, show an unresolved decision until the driver explicitly chooses. A current saved opt-in can supply the effective choice. Show **Saved preference** and list its selected categories. Show the session’s effective choice clearly alongside the saved preference when they differ. Category checkboxes, where presented, use available categories. Link to D20 for recording preferences and D22 for account-wide consent controls.

| Decision state | Start behavior |
| --- | --- |
| Choice pending | Explain that a recording choice is required. Keep the two choices equally readable. |
| Current saved opt-in or confirmed opt-in | Show eligible selected categories and the confirmed choice. Start when the other gates pass. |
| Explicit decline | Show **Clips off for this session** and treat the decision as complete. Start when the other gates pass. Open D03 with **Recording off**. No pre-event clip buffer or new clip transfer begins for that session. |
| Consent load, save, or revision conflict | Show the actual pending or failure state beside the choice. Preserve the driver's selection for recovery. Refresh the revision before retrying and keep capture off until current consent is confirmed. |

**Contract follow-up.** The approved design treats a D02 decline as a session-only choice. `startSession` accepts `recordingDecision: declined` and a `consentRevision`. The documented contract leaves two rules open. Confirm whether admission accepts a decline against a revision with recording enabled and how capture and clip admission enforce that session’s decision. Distinguish an initial unset choice from a previously saved off preference where the UI needs that distinction. Account-wide withdrawal and its effects on unsent clips belong to the separate D22 revocation action. Persist the decline on the session path. [API admission and consent](../../API.md) · [Recording requirements](../../PRD.md#54-history-recordings-and-data-lifecycle)

## Components and motion

| Classification | Approved treatment |
| --- | --- |
| Existing RAFIQ | Reuse the wordmark, primary and outline controls, token styles, and **Loading / Compact arc** (`P8LWJ8`) where a real asynchronous check is in progress. |
| Standard | Use buttons for actions, links for destinations, labeled fieldsets and radios, category checkboxes where shown, a read-only list of results, text status, and inline recovery. |
| Custom RAFIQ | Build the native preview treatment with an editable static framing guide and text guidance, the labeled readiness rows, and the supervised eligibility and authorization section. |

At verified passage, update the text and icon immediately. If motion is enabled, ease the check icon or row emphasis once over roughly 150 ms. Keep wording and placement steady during camera corrections. Show the compact arc with **Verifying monitoring files…**, **Initializing monitoring…**, or **Checking account eligibility…** when the corresponding operation is pending. Stop it on success, failure, cancellation, or exit. Use the same steady labels, icons, and a static pending mark under reduced motion. Use named phases because the verification contract supplies no reliable percentage. [RAFIQ loader](../../../Pen%20Design/RAFIQ-loader.md) · [Component research](D02-COMPONENT-RESEARCH.md)

## Pen.dev handoff and acceptance

- Use editable preview, overlay, text, and status layers with a staged face-and-upper-body image or neutral illustration in the preview. Show the overlay at the same position across live-view and framing-correction variants. Annotate state triggers, focus destination, and the start/stop conditions for the loader. Represent the browser permission prompt as an annotated handoff to Chrome. The frontend supplies the stream, permission result, live checks, account and consent authority, and monitoring transition.
- Provide a 1440 px stationary ready frame with clips off and a saved-opt-in example with selected categories. Cover first use, permission pending and blocked, missing or busy camera, poor framing, verification and initialization progress and failures, offline/unsupported setup, account unavailable, consent saving/retry, starting, supervised authorization pending/active/revoked, and Emergency Mode unavailable. Show the reduced-motion state with a steady pending indicator. Use compact component variants for states that share page structure.
- At a narrow laptop width and 200% browser zoom, stack header, preview and guidance, checks, session type, clips, and actions in reading order. Include a narrow reflow view at roughly 320–390 CSS px to represent zoom. Wrap error guidance and action labels. Keep the route back and current blocker reachable without horizontal page scrolling.
- Check keyboard traversal, visible focus, programmatic form labels, and logical heading order. Announce each meaningful status transition once through a polite status region. Keep focus in place during background checks. Focus the relevant summary or corrective control after a failed Start when useful, and restore focus to the origin on Cancel. Verify that all states remain legible without color and that preview instructions and readiness results are available as text. [Experience accessibility floor](../../EXPERIENCE.md#accessibility-floor) · [Status semantics](https://www.w3.org/TR/wai-aria-1.2/#status)
- Verify that both recording choices enable **Start monitoring** after the same applicable readiness checks. Exercise saved opt-in → session-only decline → D03 recording off → later session showing the saved choice. Check zero new buffered or uploaded clips for the declined session and preservation of the saved preference. Check that camera denial, unverified assets, initialization failure, stale or ineligible account, offline new start, and invalid supervised authorization each produce their own recovery state. Confirm that a qualified supervised session with Emergency Mode unavailable still shows its ordinary warning eligibility. Test the approval variants with motion on and off.
