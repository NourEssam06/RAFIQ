# D06 Sessions — approved Pen.dev handoff

On 25 November 2026, the user selected **A · Aligned table with stacked rows at high zoom** and **one brief accent when Back restores the row**. Use native history controls and RAFIQ styling. The proposed accent can use CSS. [Layout exploration and component research](D06-COMPONENT-RESEARCH.md)

## Purpose and navigation

Give the signed-in driver a private, newest-first index of past sessions. The driver should be able to identify a session by date and local start time, see whether they can review it, and return to the same place after opening it. Entry points are the private **Sessions** item, **Back to Sessions** in D05, and **View session history** in D19. **Start session** opens D02 readiness. Each row has one destination, **View details** opens ready D07 and **View status** opens the authorized D05 status and recovery view. [Screen specification](../../SCREENS.md#d06-sessions) · [Component patterns](../../EXPERIENCE.md#component-patterns)

## Frame structure

1. Reuse D01’s private navigation with **Sessions** marked current. Retain the distinct **Start session** action in populated history. Give first use one prominent **Start session** action inside its empty state.
2. Place the **Sessions** heading above a short scope line such as **Newest first · Cairo (UTC+02:00)**. Use the driver’s displayed local zone. Display a row-specific offset when needed to distinguish times, including a repeated clock hour or a session spanning an offset change.
3. Use a full-width table with **Started**, **Ended**, **Duration**, **Review status**, and **Open**. Give the timestamp and review status the most room. Use flat horizontal dividers and align numeric durations. Keep the row link distinct from the status. Let reasons wrap. Show the start date and time in every row, add the end date when it crosses midnight, and use explicit duration units. Use **End time unavailable** or **Duration unavailable** where the data is missing.
4. Place **Newer sessions** and **Older sessions** below the rows. The newest-first API provides a forward cursor, with a proposed default of 25 rows. Use the previously requested cursor for the newer page. Omit the unavailable direction as an action and omit the pager for an unpaged result. During a paging request, keep the current authorized page readable and prevent duplicate requests. On success, replace rows and paging affordances together, then bring the results heading into view and focus it. Background refresh preserves focus and position. [List API and pagination](../../API.md#10-pagination-filtering-sorting-and-caching)
5. At narrow desktop widths, wrap the time and status details. When the columns no longer fit, use one stacked semantic list with visible field labels and the same row order, information and single link per entry. Keep paging and the Start action within the viewport. Use the same session identity across both presentations so a resize or zoom change preserves the return point.

### Visual references and proposed dimensions

Use **D01 · Ready review · desktop** (`v2yld`) and **D01 · Ready review · narrow** (`bhsYb`) for the shell and data density. Reuse the nav, primary and secondary action treatments, flat dividers, icon style and focus treatment. Match Space Grotesk as the existing Mori substitute. Use `$canvas` / `colors.canvas` (#0e100f), `$ink` / `colors.ink` (#fffce1), and `colors.accent-stone` (#bbbaa6) for secondary text. Use `spacing.sm` (8 px) for compact status groupings, `spacing.md` (16 px) for row padding and column separation, and `spacing.xl` (24 px) between major groups. Use the existing corner treatment for controls and inline feedback.

Start from D01’s 1,440 px desktop shell, 76 px navigation and 48 px content gutters, and its 390 px narrow reference with 20 px gutters. Use `typography.body` as the row-text floor and the existing D01 page-heading role. Let each row grow with wrapped content. The backed-out row marker should be an inset edge and quiet neutral fill. Keep the focused link’s ring independently visible. [Design tokens and components](../../DESIGN.md#components) · [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>)

## Review and recovery states

| State | Row or page treatment | Action |
|---|---|---|
| Ended, waiting for review | **Ended** with short waiting copy when neither syncing nor processing has been confirmed. | **View status** in D05. |
| Interrupted | Show **Interrupted** as lifecycle context, including alongside **Syncing** or **Ready** when supplied. | **View status** in D05 for eligible same-driver recovery. **View details** in D07 once review is ready. |
| Syncing | **Syncing** for required records still transferring. Show a known connection issue or recovery direction through D05. | **View status** in D05. |
| Processing | **Processing** once the status confirms that analytics are being prepared. | **View status** in D05. |
| Ready | **Ready** once required records and analytics are ready. | **View details** in D07. Optional clips can still be pending. |
| Unavailable, still authorized | **Unavailable** with the authorized reason underneath. Draw a synthetic example with “No usable observations.” | **View status** in D05. Recovery is shown there when eligible. |
| First load | **Loading sessions…** with still, noninteractive skeleton rows aligned to the final geometry. | Keep the shell usable. |
| First use | **No sessions yet.** “After you finish a session, its review status will appear here.” | **Start session**. |
| Empty retained history | **No sessions to show.** Use this state if the cause of an empty history is unknown. | **Start session**. |
| Recoverable load or paging failure | **Couldn’t load sessions.** Keep valid rows in a paging failure. Add reconnect guidance when offline is known. | **Retry** the failed request. For a rejected or expired cursor, offer **Reload sessions**. |
| Record removed or access lost | Clear content when authorization or eligibility is lost. A deleted, expired or inaccessible detail uses P08’s **This item is unavailable.** | **Back to Sessions**, after the list’s access check. |

Use text and a visible non-color cue for review status. Update labels and link destinations together. Preserve focus if the same row changes from status to details while on screen. D05 owns session-specific retry and sync recovery. [D05 recovery](../../SCREENS.md#d05-end-status-and-interrupted-session-recovery) · [P08](../../SCREENS.md#p08-unavailable-link)

## Back restoration and motion

On departure to D05 or D07, retain the list scope and page request, the opened session ID, the row’s offset within the viewport and the originating link in ephemeral state for the current driver and history entry. Recheck access and restore the page before showing or focusing private content. After layout, put the same row at its prior relative offset and focus its link without a second scroll. If the row moved between pages, use an authorized lookup within the prior scope where the data contract supports it. If the saved row has disappeared, focus the nearest surviving row from that page, or the results heading if no row survives. When the saved page or history entry cannot be recovered, go to the latest authorized page. Clear restoration state on sign-out, account change or eligibility loss. [Shared return rules](../../SCREENS.md#shared-design-rules) · [Private caching contract](../../API.md#10-pagination-filtering-sorting-and-caching)

| Beat | Visual behavior |
|---|---|
| Before departure | Save the current position and row identity. Open the target immediately. |
| Back restored | Show the stable marker and focus ring immediately once the row is positioned. On normal motion, fade a secondary highlight out once over about **150 ms**. Keep the stable marker visible. |
| Reduced motion or fallback return | Render the same final marker where applicable with immediate scrolling and focus. Skip the accent. |

Keep skeleton rows, page changes, empty states and review-status transitions still. For Pen, show **restored row at the start of the accent** and **restored row at rest** using the same crop and geometry. Draw a ready mixed-state desktop frame, a 390 px stacked variant and a 320 CSS px reflow sample, plus the loading, first-use, empty, retry, unavailable and restored-focus variants. Use synthetic sessions. Pen illustrates the visual endpoints. Browser implementation verifies focus order, status announcements, authorization, real pagination and scroll restoration. [Motion references and licensing](D06-COMPONENT-RESEARCH.md#component-research)

## Accessibility and acceptance

- Use a skip link, landmarks, a single page heading, captioned table semantics with scoped headers, and a semantic list in the stacked presentation. Use a real, timestamp-specific link name that starts with its visible action, such as **View details for 24 November 2026 at 09:42**. Keep each row to one tab stop and retain a visible focus ring. [WAI table patterns](https://www.w3.org/WAI/tutorials/tables/)
- Hide visual skeletons from assistive technology, mark the results busy, and announce meaningful load, paging and recovery outcomes once. Verify at a supported laptop width, a narrow desktop, 200% zoom, and 320 CSS px. Labels, reasons and controls remain visible in reading order. [WAI status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) · [WAI reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Verify an older-page session can be opened by keyboard and returned to via Browser Back and in-app Back. Verify the same row, offset and focus after a normal return and zoom reflow. Check a removed row, a cursor failure, an account switch, a modified page, and reduced-motion mode. Verify pending clips leave ready review available and a pagination failure preserves the current authorized page.

## Product data to confirm before frontend implementation

The documented list returns lifecycle and analytics enums, start and sometimes end timestamps, and a forward cursor. Confirm the authoritative interruption and processing signals, unavailable reason and permitted recovery action, treatment of active records, and discovery of eligible local interrupted sessions before sync. Confirm whether **Duration** means elapsed start-to-end time. The Pen examples use that convention provisionally and keep D07’s pause-adjusted **Monitored time** distinct. An empty page does not establish first use. Exact Back restoration when the row shifts outside the original cursor page depends on how the history contract locates that row in the same authorized scope. [Session schema and operations](../../API.md#7-detailed-endpoint--operation-specifications) · [Session and offline contracts](../../TRD.md#2-session-recording-and-offline-contracts)
