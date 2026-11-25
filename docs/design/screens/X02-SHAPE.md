# X02 · External MCP agent

**Operate.** A driver authorizes a compatible MCP client, asks it for a session or personal trend report, and opens the checked result in RAFIQ. The Pen.dev implementation uses static journey references. Client wording is illustrative. The client controls how its native interface presents the request and tool activity. [X02 requirements](../../SCREENS.md#x02-external-mcp-agent) · [Authoring journey](../../EXPERIENCE.md#j6-author-through-mcp-and-review-a-report)

## Journey

| Moment | Driver experience and service outcome |
| --- | --- |
| Connect and authorize | The driver gets setup instructions from **Settings → Connections** in D23. The compatible client initiates D24. The driver signs in, checks the requester, and approves **Author reports** if desired. **Read driving data** is a separate permission for general reads. Return through the supported authorization flow. |
| Request a report | The driver asks for a specific session, a personal trend report for an eligible scope, or a new version. With the target resolved, `start_report` creates a job and returns its opaque ID and state. A request for a new version starts a new job. |
| Retrieve evidence | `get_report_inputs` supplies the job’s approved template, evidence, and limitations. Cite supplied evidence IDs for numerical findings. Job inputs exclude raw media, clips and clip links, raw measurement series, contacts, precise location, and finished report contents. |
| Check status | The client uses `get_report_status` with the opaque job ID. Show **Queued** and **Processing** when those states are confirmed. Check again when inputs are pending or a submitted draft is still processing. D17 can show the owner’s eligible job status. |
| Submit or revise | `submit_report_draft` returns **accepted** or **revision required**. Acceptance can still leave the job processing. On revision, the agent uses safe field feedback and the approved evidence to correct and resubmit the draft for the same job. |
| Return to RAFIQ | When ready, use the illustrative handoff “Your report is ready to review. Open Reports in RAFIQ and select Review report.” D17 exposes **Review report** for the eligible owner. D18 presents the validated findings, methods, sources, and limitations. PDF and Word exports use the same snapshot. |

The MCP result provides a job ID and state. The driver gets the eligible review destination from D17. RAFIQ checks the initiating driver, client, current authoring grant, and sources at the applicable operation and release boundaries. Review and export recheck the browser user’s eligibility. [MCP tools and schemas](../../API.md#mcp-streamable-http-and-tools) · [M07 ownership](../../ARCHITECTURE.md#module-m07--mcp-and-reports) · [Report review and export](D18-SHAPE.md)

## Pen.dev implementation

The three editable boards sit immediately to the right of X01 in [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>). They use Space Grotesk, the canvas, ink and stone tokens, and the existing lime and orange status accents. [Design tokens](../../DESIGN.md)

| Board | Pen node | Coverage |
| --- | --- | --- |
| X02 · External MCP agent / Journey storyboard | `P8F6b` | Six steps from authorization to review. The four external tool examples share the editable **X02 · Client storyboard state** component (`pNZeB`). |
| X02 · RAFIQ authorization and review handoffs | `amIpw` | Existing D23 endpoint setup, D24 consent result, D17 ready row, and D18 review and withdrawal excerpts. Each excerpt uses its own example data. |
| X02 · External MCP agent / Recovery and status references | `OCnNm` | Revision and error recovery plus status presentation references. **Needs revision** reuses the existing **Horizontal status row** component (`Yh4JZ`). |

## Recovery

| Condition | Next step |
| --- | --- |
| Decline or read-only grant | Authoring is unavailable. Use D23 to start fresh authorization if the driver chooses to grant **Author reports**. |
| Inputs pending, scope unclear, or inputs unavailable | Check status again when inputs are pending. Ask the driver to clarify the target when the scope is unclear. Request a report using eligible sources when the original sources cannot be used. |
| Status read unavailable | Report that status is unavailable and retry the authorized read when recoverable. A failed status check does not establish job failure. |
| Start or submit response lost | Repeat the equivalent operation with the original request or submission identity. Confirm the resulting state before describing the job as accepted or ready. |
| Draft needs revision | Correct the affected findings against the job’s approved evidence and resubmit. D17 directs the driver back to the agent when a visible job needs revision. |
| Authoring grant expires or is revoked | Stop affected tool access and in-progress publication. Suppress stale results. Eligible drivers can return to D23 for fresh authorization. Recheck the job’s grant binding before further work. |
| Source expires or is deleted | Withhold publication or withdraw the report. Clear affected review and export actions. If eligible, request a new report through the agent using available sources. |
| Generation fails or publication is blocked | Present the safe status and next action when available. Use grant or source recovery when confirmed. Otherwise ask the agent for a fresh request only when recovery is available. |

## Presentation and qualification

- Use short, explicit text for job states and the action available at each boundary. Optional MCP progress notifications are scoped to a request. The durable report job uses its own status read, and its contract supplies neither percentage nor time remaining. A successful tool response and an eligible report are separate outcomes. [MCP progress](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress) · [AI SDK tool states](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage)
- Reuse D17’s text-led status and D18’s existing review actions. On RAFIQ surfaces, preserve focus during status updates, announce meaningful changes, and keep labels and actions readable without motion or color and at narrow widths or zoom. External keyboard and screen-reader behavior depends on the client’s native interface. [D17 status and recovery](D17-SHAPE.md#status-and-recovery) · [WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- Qualify the deployed journey with a client-neutral reference client. Exercise author-only and read-only authorization, a session report and a trend report, draft revision, a lost response and safe retry, source loss and grant revocation, and owner-only review and export. Verify how an author-only client obtains the mandatory session identifier when it has no prior authorized context. General session discovery is independently scoped. [MCP release criteria](../../PRD.md#88-mcp-qualification-and-data-boundaries) · [Authorization qualification](D24-SHAPE.md)
