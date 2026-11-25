# D05 End status and interrupted-session recovery

**Approved 25 November 2026 · Operate · Private driver desktop web workspace**

The driver needs to know observation has ended, whether session review is available, and whether any remaining work requires action. The approved **Layout A** uses one full-width status panel. The approved **D05-C00** uses immediate, static text and icon updates. When analytics becomes ready in D05, keep the driver on D05 and reveal **Open session details** in place. After interrupted recovery, retain **Interrupted** and put the explanation in the collapsed **How this session ended** disclosure.

[D05 requirements](../../SCREENS.md#d05-end-status-and-interrupted-session-recovery) · [Experience transitions](../../EXPERIENCE.md#session-and-emergency-mode-transitions) · [Approved proposal and component research](D05-REVIEW.md)

## Frame and navigation

1. **Private navigation.** Reuse D01’s private shell with **Sessions** selected. Open D05 from D03 after ending observation when review is pending, from a pending D01 or D06 session, or after eligible interrupted-session recovery begins. D03 may open D07 directly when review is already ready at entry.
2. **End status and session identity.** Use **Session ended** or **Session interrupted** as the page heading. Put **Camera off** with a steady camera-off icon immediately below, once observation closure is known. Identify the session with local date, start time, and displayed time zone. Show the confirmed end time when available. Use the staged format `25 November 2026 · Started 08:40 · Ended 09:02 · Cairo (UTC+02:00)` for a normal-end design fixture. The interrupted fixture should use its own confirmed endpoint.
3. **Recovery context.** While recovering an authorized interrupted session, keep one short explanation visible beneath the session identity. Once recovery is confirmed, keep the interrupted heading and replace the explanation with **How this session ended**. Expand it in place to show the confirmed outcome and endpoint. If it is being read or contains focus when recovery completes, preserve access to the content and focus on the disclosure summary if its previous target disappears.
4. **One status panel.** Stack **Session records**, **Analytics**, and **Clip uploads** in that order. Add **Optional** beside the third label. Each row has a steady state icon, human-readable status, and a reason or action only when applicable. Use dividers and consistent padding. Show the status and its reason together when they wrap. The panel is a read-only list with individually actionable retry buttons where supported.
5. **Actions.** Place **Open session details** (D07) in the primary action slot below the panel only when analytics is ready. Keep **Back to Sessions** (D06) visible in every authorized state, in a consistent secondary position. Restore the list’s previous filters, scroll position and selected row when returning from D06. The existing **Start session** navigation action opens D02 for fresh readiness.

[D01 status treatment](D01-SHAPE.md) · [D03 end and sync treatment](D03-SHAPE.md) · [D06 and D07](../../SCREENS.md#d06-sessions)

## Components and visual tokens

| Type | Handoff |
| --- | --- |
| Reuse | D01 private navigation and dated status treatment. D03 recording, clip and sync vocabulary. Existing pill and outline actions, visible focus, icon style and hairline dividers. |
| Standard | Destination links, native buttons, status text and a keyboard-operable disclosure. State rows are read-only and only the controls enter tab order. [Native disclosure reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) |
| RAFIQ composition | One full-width status panel with three instances of a reusable status row. One interruption block with recovering and recovered disclosure variants. Inside the recovered disclosure, use a single line for a lone confirmed endpoint, or a static ordered list for multiple authorized, timestamped recovery events. |
| Approved feedback | **D05-C00**. Keep the same icon slot, row order and action positions as state changes. Use text and signifiers such as check, waiting, or unavailable icons. The static treatment uses RAFIQ markup and styling with zero added motion dependencies. |

Use `{colors.canvas}` (#0e100f), `{colors.ink}` (#fffce1), and `{colors.accent-stone}` (#bbbaa6) for the canvas, primary text and supporting text. Apply Mori or the documented Space Grotesk fallback, `{typography.h1}` for the end-state heading, `{typography.body}` for row content and reasons, and the existing private-shell control styles. Keep semantic accents small and pair each with text and shape. Use neutral flat surfaces and `{rounded.md}` (8 px). Use `{spacing.xl}` (24 px) between regions, `{spacing.md}` (16 px) inside the status panel and around rows, and `{spacing.sm}` / `{spacing.base}` (8 / 10 px) between related lines. Use 48 px main gutters for the proposed 1440 px study, with the incumbent shell’s compact spacing at narrower sizes.

Design at 1440 px, 900 px and a 320 CSS px equivalent. Keep one column at each width. Stack a row’s title, status, reason and action when horizontal space runs out. Allow long dates, time zones, reasons and action labels to wrap. Verify the tab sequence at 200% browser zoom and reflow at 320 CSS px. Keep navigation, focused controls and terminal reasons visible without horizontal page scrolling.

[Design tokens](../../DESIGN.md) · [Pen reference boards](../../../Pen%20Design/RAFIQ.pen) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

## States and interaction

| Scope | Visible states and rules |
| --- | --- |
| Observation and lookup | On confirmed local teardown, show **Session ended** and **Camera off** immediately while hosted work continues. On history entry with no known result, show a bounded **Loading session status** placeholder. Show **Couldn’t load session status** and **Check again** for an eligible transient lookup failure. Keep known, still-authorized content during refresh. |
| Session records | Show **Waiting for connection**, **Checking account**, **Syncing session records**, or **Confirming session end** as evidenced. Show **Session records synced** once required writes and finalization are confirmed. Use **Sync delayed** for retryable delay. Use **Some records unavailable** for confirmed partial loss or **Session records unavailable** for terminal loss of required records. Give an authorized reason if known. Reflect the confirmed impact on required analytics inputs. |
| Analytics | Show **Waiting for session records** before required records and finalization are confirmed. Use **Processing analytics** for confirmed pending computation. **Analytics ready** immediately enables **Open session details**. Individual metrics can still be unavailable in a ready review. For a transient status read, use **Couldn’t check analytics status** and **Check again** when eligible. For a confirmed terminal result, show **Analytics unavailable** and an authorized reason if known. |
| Clip uploads | Show **Clips queued**, **Waiting for connection**, **Uploading clips**, **Transfer interrupted**, **Clips available**, or **Clips unavailable** as evidenced. Show mixed counts such as **1 available · 1 queued** only when known. Explain **Recording was off**, **No clips were created**, or **No clips match recording settings** where confirmed. Explain expiry, consent withdrawal or queue/storage limits at the affected scope. Review remains openable with any optional clip outcome. |
| Offline and retry | State the immediate cause and next eligible action in the affected row. Explain automatic reconnect retry where supported. Use action-specific **Retry record sync**, **Retry clip upload**, or **Check again** only where supported and eligible. Change the row to **Retrying…** or **Checking…** on activation, suppress concurrent submissions for that operation, then show the confirmed outcome. Restore the retry action on another eligible failure and keep the reason local. Honor the service retry window. |
| Interrupted recovery | Closing, reloading or crashing ends live observation. Prior to fresh eligible online sign-in by the same driver, use the appropriate sign-in or restricted-account surface and keep session identity, timestamps, clip counts and queue data private. After verification, show **Monitoring stopped when this session was interrupted. We’re recovering saved records.** Replay eligible records and finalize at the last durably recorded observation. After confirmation, keep **Session interrupted** and show the explanation inside **How this session ended**. Omit the endpoint when unavailable and use confirmed outcome copy. A new run must start through D02. |
| Permanent loss and access | End retries of expired, deleted or permanently ineligible items. If the owner can still access the session, give a safe, confirmed reason for an affected row and keep other authorized data available. Clip loss leaves eligible metadata and analytics independent. Clear private content immediately when the session or account loses authorization. Use P08 for an unavailable private session link, P07 for a restricted account, or fresh sign-in as applicable. Use P08’s generic **This item is unavailable.** and its return link. |

Use state text for all three approved status rows. Counts require measured scope and time labels require confirmed timestamps. Analytics and sync expose phase and outcome. Clip publication is confirmed independently of byte transfer. The incident timeline and analytics charts live in D07, and detailed clip discovery and playback live in D10 and D11.

[Experience state patterns](../../EXPERIENCE.md#state-patterns) · [Session and offline contracts](../../TRD.md#2-session-recording-and-offline-contracts) · [API data contracts](../../API.md#8-shared-data-contracts) · [Unavailable link](../../SCREENS.md#p08-unavailable-link)

## Static state storyboard and accessibility

| Trigger | Immediate visual and interaction result |
| --- | --- |
| Observation stops | Set the confirmed end heading and camera-off status. Render each known work state in its existing row. |
| Waiting work resumes, or a retry is activated | Update the affected icon and label in place. Keep unaffected statuses visible. A manual action shows its in-flight label immediately. |
| Analytics is confirmed ready | Update the analytics row and reveal an immediately usable **Open session details** in the action group. Keep the route, current focus and clip status. |
| Interrupted recovery is confirmed | Keep the interrupted heading and show **How this session ended** in the same context area. The default presentation is collapsed, with the reader’s access preserved during a live transition. |
| A queue item becomes permanently unavailable | Render the confirmed reason locally and remove the affected retry affordance. Preserve unrelated outcomes. Authorization loss clears private content and routes according to access state. |

- Use a skip link, navigation and main landmarks, one H1, and visible focus. On page entry focus the heading. Focus order follows the disclosure, any row actions and the action group.
- Give the disclosure its visible name and expanded state, with Enter and Space support. Treat redundant icons as decorative and pair each state with text.
- Announce meaningful changes once in a polite status region, including **Analytics ready** and the outcome of a user-initiated retry. Deduplicate polling responses. Keep focus stable on background updates. If a focused retry disappears on confirmation or permanent loss, focus the affected row heading. Use destination heading focus after a privacy route change.
- Use immediate updates with reduced motion and with default motion settings. Render the final status text, icon and action in the same update. Use the same static snapshots for both motion settings.

[RAFIQ accessibility floor](../../EXPERIENCE.md#accessibility-floor) · [WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

## Pen.dev representation and acceptance

In `RAFIQ.pen`, reference D01 **Syncing session records** (`X4dCl`), D03 **Recording, clips and sync** (`sbyzq`), and the foundations and controls boards (`v3WGH`, `giojv`). Use editable text, icons, nested frames, buttons and reusable row variants. Create static frames for the transitions below, with short annotations for triggers and focus where needed. For an unavailable session, reference P08’s existing outcome frame (`tb0lo`) and annotate the return to Sessions.

| Scenario | Pen frame or variant | Frontend acceptance |
| --- | --- | --- |
| Normal end and independent success | Camera off with records syncing, then analytics processing, then ready with a clip queued. Include 1440 px, 900 px and 320 CSS px examples across representative states. | Observation stops before pending sync. Ready appears only after the required inputs and analytics result are confirmed. D05 stays open and its review link works while the clip is pending. Back restores D06 context. |
| Offline and retry | Waiting for connection, one in-flight manual retry and its failed or successful result, with other rows unchanged. | Reconnect resumes eligible work. Repeated activation or a lost acknowledgment leaves one durable record per item. Retrying a status read refreshes the result. Focus and live announcements follow the storyboard. |
| Interrupted and recovered | Authorized recovery in progress, followed by recovered with disclosure collapsed and expanded. Show a fixture with an unavailable endpoint. | Close, reload and crash cases stop observation. Only fresh eligible online sign-in by the same driver opens recovery. The recorded end matches the last durable observation when available. Reconnection leaves the camera off and unsent emergency actions closed. |
| Empty, mixed and terminal | No clips expected, mixed pending/available, optional expiry or revocation, and required-data terminal loss. | Consent withdrawal discards affected unsent clips. Expiry or deletion prevents replay. Clip failures leave a ready review usable. Terminal failure shows a safe scope-specific reason and only eligible retries. |
| Status read and authorization | Initial loading, temporary lookup error, and a handoff to generic P08 or restricted P07 as appropriate. | A switched or signed-out account sees no previous driver’s identity, timestamps or queue. Authorized stale content refreshes without stealing focus. Access loss clears private data before a fallback is shown. |

Pen.dev depicts layout, control states, and the before/after appearance of each transition. The frontend owns camera teardown, account verification, queue replay and finalization, independent analytics and clip availability, retry gates, keyboard operation, announcements, and browser reflow. Verify focus visibility, the long-reason variants, and that the ready link is immediately usable at zoom and with reduced motion.

## Open contract decisions

- The proposed finalization payload distinguishes normal and interrupted ends. The proposed `Session` read model omits the end reason. Confirm how an authorized later D05 or D06 visit obtains reliable interruption provenance and how recovery completes if the last durable observation is absent. Show the interrupted label and timestamp only when supported by authorized evidence.
- Confirm the source of row state and safe reasons for partial or terminal record loss, mixed clip outcomes, and known no-clip cases. Confirm which manual sync and upload retry actions are supported. **Check again** for analytics refreshes its status. Use plain-language available states where detailed evidence is missing.

[Draft API and error handling](../../API.md#11-error-handling-standards) · [Frontend architecture](../../ARCHITECTURE.md#6-frontend-architecture)
