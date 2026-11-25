# D17 Reports — design and Pen handoff

**Operate.** A signed-in driver opens **Reports** from the private navigation or returns to RAFIQ after requesting a report in an external MCP client. The driver should be able to find the right session or personal-trend report, check what is happening, and open a ready report for review. D17 shows authorized report records and driver-visible job status. D18 owns the validated report, source evidence, and PDF and Word export. [Screen requirements](../../SCREENS.md#d17-reports) · [Report review and export](../../SCREENS.md#d18-report-review-and-export)

The editable Pen.dev implementation uses Layout A and static RAFIQ components. All 12 artboards are in the main RAFIQ document, below D16 Benchmark and to the left of D18 Report review and export. File verification matched the saved artboards to the standalone design. Visual inspection covered the wide, narrow and 320 px layouts, expanded help, loading, generation outcomes and access loss. [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>)

## Layout options

| | A · One reports list **(recommended)** | B · Jobs and reports in separate sections |
| --- | --- | --- |
| Composition | **Reports** heading and **How reports work** disclosure, followed by one list. Each row carries report identity, source scope when available, creation time, status and available action. | Same shell and help. **Report jobs** comes first, and **Ready reports** follows. Keep eligible historical job outcomes in Report jobs. |
| Interaction | One stable creation-ordered sequence. Keep a job in place when it becomes ready and reveal **Review report** in that row. | Scan current jobs separately from completed documents. Move an eligible ready item between sections while preserving the user’s focus and reading position. |
| Trade-off | Works with the current single cursor feed and supports direct comparison of successive requests. Status must be easy to scan. | Active work is more prominent. Section-specific pagination needs a server contract to avoid implying that a partially loaded section is complete. Movement between sections adds focus and scroll handling. |
| RAFIQ references | D06’s flat list, D01’s shell and D05’s status rows. | D01’s stacked sections and D05’s grouped status rows. |

### Recommended composition

Match D06 desktop (`m14mRu`), narrow (`ltZ40`) and static skeleton (`AXgTB`), and D05’s editable status rows (`CDaKQ`). Use the near-black `colors.canvas` (#0e100f), cream `colors.ink` (#fffce1), stone secondary text `colors.accent-stone` (#bbbaa6), Space Grotesk as the documented Mori substitute, flat dividers, and the incumbent icon and focus treatment. Use `spacing.sm` (8 px) in status groups, `spacing.md` (16 px) for row padding, `spacing.xl` (24 px) between regions and `rounded.md` (8 px) where reused controls call for it. [RAFIQ design tokens](../../DESIGN.md) · [Editable RAFIQ reference](<../../../Pen Design/RAFIQ.pen>)

1. Use the private header with **Reports** current and the existing **Start session** action. Place **Reports** first in the main landmark. Keep **How reports work** adjacent to the heading on desktop and before the list at narrow widths. On the first-use empty screen, put the workflow directly in the empty-state block.
2. At 1440 px, align a flat list to D06’s 48 px content gutters, with **Report**, **Source scope**, **Created**, **Status** and a right-aligned action column with an accessible heading. Keep the title first and type and version below it when supplied. Use the approved session label or date range for scope. Give scope the applicable time zone and label creation time separately. Keep the creation order consistent with server pagination and use **Load more reports** when a cursor exists.
3. As columns stop fitting, follow D06’s stacked row at 390 px and 320 CSS px. Keep identity, scope, created time, status, then the action in reading order. Use the 20 px narrow gutters as space permits. Wrap long titles, versions, dates and translated statuses. Keep access to the action at 200% zoom and at 320 CSS px without page-level horizontal scroll. Treat any illustrative document glyph as decorative. Use rows, labels and text for scanning the workspace.
4. Show **Review report** directly on each eligible ready row. Use a link with a screen-reader name that includes a safe title or type plus creation time. Add short guidance only to rows with an actionable next step. Returning from D18 restores the originating row, scroll and focus when still eligible. If it disappears, move focus to the nearest remaining row action or the list heading.

## External authoring handoff

Suggested expanded copy:

> Connect a compatible external agent in **Connections** and authorize **Author reports**. In that agent, ask for a session or personal trend report. RAFIQ checks the submitted findings against approved evidence. Return here and select **Review report** when it’s ready.
>
> To correct a draft or request a new version, ask the agent in the external client.

**Open Connections** links to D23 for setup, grant status and fresh authorization. D24 handles sign-in and independent **Read driving data** and **Author reports** approvals. If D17 has no reliable grant information, use the same generic help without asserting connection status. Any report creation, draft submission, correction, or request for a new version takes place in the external client. Report review and export stay in RAFIQ. [Connections](../../SCREENS.md#d23-connections) · [MCP authorization](../../SCREENS.md#d24-mcp-authorization) · [Authoring journey](../../ARCHITECTURE.md#j6-author-through-mcp-and-review-a-report) · [Product requirements](../../PRD.md#56-reports-and-assistant-integration)

## Status and recovery

| Condition | Visible treatment | Driver action |
| --- | --- | --- |
| First load | **Loading reports…** plus quiet placeholders in the final row geometry. Skeletons contain no interactive controls. | Navigation and report help stay available. |
| No authorized rows | **No reports available** and the short external workflow. Use this for an empty successful response. An account can reach this state after prior reports expire. | **Open Connections** and request a report in the external client. |
| Queued | **Queued** with a clock cue. | Check here again. |
| Processing | **Processing** with the shared processing cue. Progress is indeterminate. | Check here again. |
| Ready and eligible | **Ready to review** with a check cue and a current eligible report reference. | **Review report** opens D18. |
| Revision required | **Needs revision** with an attention cue. | “Ask your external agent to correct and resubmit the draft.” Use the workflow help for guidance. |
| Blocked | **Publication blocked** with a safe explanation when supplied and authorized. | For confirmed grant loss, point to Connections for fresh authorization. For a confirmed source problem, direct a new request to the agent using eligible data. With no approved reason, offer the generic workflow help. |
| Failed job | **Generation failed** with a safe explanation when supplied. | Return to the external agent for a new request when recovery is available. |
| Expired or withdrawn | **Expired** or **Withdrawn** only while the service authorizes a status row. Suppress previously shown title, scope and actions unless each is still authorized for that state. | Request a new report from eligible sources through the external agent. |
| Unknown status or missing eligible snapshot | **Status unavailable** or **Report unavailable**, whichever is accurate. | Retry the read if recoverable. Use the shared unavailable state for an ineligible direct destination. |
| Initial read or pagination failure | **Couldn’t load reports** or **Couldn’t load more reports**. Confirmed offline state can say **You’re offline**. Retain unaffected rows on a paging failure while their authorization remains current. | **Retry** repeats the read. Preserve the loaded list during a safe retry. |
| Account or item loses access | Clear affected private content immediately, including stale responses and pending transitions. Use the shared sign-in, restricted-account, or unavailable route when applicable. | Continue from the eligible account or the nearest safe destination. |

Render validated job status as soon as it arrives. One polite status region announces meaningful changes once, with enough safe context to identify the affected row. A repeat read with the same state stays quiet. Keep job state distinct from export state. The job API provides state and timestamps, so show indeterminate progress. A report expires 30 days after creation or earlier when a required source expires. Validate review affordances against current owner and source eligibility, including on return from D18. [Job and report contract](../../API.md#7-detailed-endpoint--operation-specifications) · [Retention and lifecycle](../../PRD.md#86-clip-and-report-lifecycle)

## Components and motion

| Classification | D17 use |
| --- | --- |
| Existing RAFIQ | Private shell and nav, D06 list and stacked rows, static skeleton and inline recovery, D05 text-and-icon status treatment, existing focus treatment. |
| Standard | Page heading, semantic table at wide widths or equivalent labeled list, inline links, a disclosure for report help, retry and pagination buttons. |
| New RAFIQ composition | Report summary row with optional metadata, eligibility-based review action, external workflow message, and safe state-specific guidance. |
| External research | Optional list, loader, skeleton, empty-state and contextual-action references. Candidates and source checks are in the companion research. [D17 component research](D17-COMPONENT-RESEARCH.md) |

Recommended baseline is static list, status, loading and empty states. A single optional accent can fade out over about 150 ms when an already-visible job becomes ready. Status and **Review report** appear immediately, focus stays put, and the row stays in position. Skip the accent with reduced motion. A revoked row or private detail disappears without an exit animation. Use a skip link, clear landmarks and headings, text with non-color status cues, visible focus, and labeled metadata. For a disclosure, use a named button and exposed expanded state or native disclosure semantics. Hide skeleton shapes from assistive technology and mark the results region busy during the initial load.

## Contract gaps and Pen handoff

- The current `ReportSummary` supplies job state, kind, creation time, nullable report ID and expiry. It has no title, source label, range, or version fields. Base fixtures use **Session report** or **Personal trend report** plus creation time and status. Optional fields appear only with an approved summary projection. Draw one illustrative enriched row and one current-contract row. Private draft data and detailed sources belong outside the index. [ReportSummary schema](../../API.md#7-detailed-endpoint--operation-specifications)
- The current list exposes cursor and limit. Confirm any future server-side filters, search, split-list pagination or live-update cadence before promising them. Verify display-safe reason mappings before exposing a more specific failure explanation. Use synthetic labels and values in the handoff.
- Verify a driver can follow first-use setup to D23 and return to a visible job, use the keyboard to review a ready row in D18, and return to the same eligible row. Test an authorized mixed list, a repeat status read, revision required, grant loss during processing, source loss after publication, account changes during retrieval, and a failed next page. A successful transition exposes the review action once. An ineligible record exposes only its currently permitted state and metadata.

## Pen artboards

| Frame | ID |
| --- | --- |
| Mixed report and job list, 1440 px | `iFsda` |
| Narrow desktop, 1024 px | `sDyjY` |
| Stacked list, 390 px | `lxNKz` |
| Minimum-width and focus example, 320 px | `h00KBc` |
| First use | `fNppo` |
| External agent help expanded | `pPVG1` |
| Initial loading with static skeleton | `QzwD5` |
| Initial read failure | `M9Wsp4` |
| Next-page failure with eligible rows retained | `MWezF` |
| Revision, publication blocked and generation failure | `kSZId` |
| Expired and withdrawn status | `O8cqa` |
| Access removed, with remaining eligible reports | `H6L9k8` |
