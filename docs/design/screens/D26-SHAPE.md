# D26 Temporary Chat

**Mode** · Operate. **Direction** · A, conversation with a visible scope rail. The driver confirmed two example questions and read-only scope. The Pen.dev implementation request left component selection open. Use RAFIQ controls and D26-C03 for the reply entrance storyboard.

A signed-in, verified driver opens **Temporary chat** from a qualified, currently connected and consented provider in D23 Connections. They ask about their own sessions and trends, inspect the sessions used in the reply, and ask a follow-up. **Close chat** returns to the relevant provider in Connections. D25 owns linking and consent, D23 owns sharing revocation and disconnect, and D17 and X02 own the external report-authoring path. During monitoring, the session workspace takes priority. [D26 requirements](../../SCREENS.md#d26-temporary-chat) · [J7 journey](../../EXPERIENCE.md#j7-ask-a-temporary-chat-question)

## Frame and components

1. **Shell and header.** Reuse the private app navigation and D19 Settings structure with **Settings** selected and **Connections** current. Lead with **Back to Connections**, the **Temporary chat** heading, provider identity, and a visible **Close chat** action. Set the expectation before the first send with “RAFIQ clears this conversation when you close it.” Link to the provider’s approved data-handling explanation from D25. RAFIQ's clearing applies to its own conversation. Provider handling follows the disclosed policy.
2. **Conversation and composer.** Place the transcript and **Your question** composer in one reading column. Use speaker labels, compact turn spacing, and a visible **Send** button. In an empty chat, offer “What stood out in my most recent completed session?” and “How has my recorded incident rate changed over the last 30 days?” Selecting an example fills and focuses the composer without submitting. Preserve a draft the driver has already started. Accept multiline questions up to the API’s 8,000-character limit. Enter inserts a line break and the Send button activates by keyboard. Block empty submissions. Keep one send in flight and allow drafting a follow-up without queuing a send.
3. **Data scope.** On wide frames use a side rail with the provider’s sharing status, a summary of what RAFIQ sends, expandable categories, and **Manage sharing** to the current provider in D23. Scope is read-only. On narrow or zoomed layouts, place the same information in a disclosure above the transcript. Keep a plain statement of the sharing boundary visible when it is collapsed. Move the composer into normal flow whenever an anchored position would cover content, status, or the focused control.
4. **Analytical reply.** Label the text **[Provider] reply**. Keep the answer and any material limitation visible. A **Sessions used** disclosure lists the scope returned for that reply, with recognizable dates or session labels where authorized metadata is available. Link only when the driver can access that session. Treat the provider’s prose as interpretation. The API returns reply text, session IDs, and a generated timestamp. Structured findings, claim-level citations, and verified evidence cards require an additional contract. Show an empty or unavailable scope honestly when appropriate.

Use `colors.canvas`, `colors.ink`, and `colors.accent-stone`, the established Space Grotesk treatment, `spacing.sm` / `md` / `xl` (8 / 16 / 24 px), and `rounded.md` for the restrained panels and composer. Follow D25’s desktop shell and 48 px content gutters at 1440 px, then check 1024 px, 390 px with 20 px gutters, and 320 CSS px reflow. Let heading actions, session labels, and long answers wrap. Target a readable transcript line length around 60–70 characters where room permits. Reuse D23 button, inline status, and authorization language and D24’s disclosure treatment. Use standard form, log, status, disclosure, and button semantics. The new compositions are the Temporary header, read-only provider scope panel, and reply with its per-turn scope disclosure. [Visual tokens](../../DESIGN.md) · [D25 layout](D25-SHAPE.md#approved-layout) · [D24 disclosure reference](D24-SHAPE.md#accessibility-and-motion) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

## What can be shared

RAFIQ sends the driver's message and relevant eligible fields from their own sessions. The approved categories are session identifiers and timestamps, duration, usable coverage, behavior and incident counts, validated aggregate metrics with units and methods, and event metadata such as ID, behavior, relative start time, duration, and severity. Camera media, clips and clip links, unrestricted raw measurements, contacts, precise location, report contents, and data from other accounts stay outside chat scope. The server checks the driver, connection, current consent, and scope for each send and rechecks authority before releasing a reply. Aster Chat and all sample driving figures in Pen.dev are synthetic fixtures. Each actual provider remains subject to independent qualification. [PRD data allowlist and qualification](../../PRD.md#88-mcp-qualification-and-data-boundaries) · [Response contract and lifecycle](../../API.md)

For analytical fixtures, show a change the driver can verify from the numbers. For example, 6 incidents over 2 monitored hours yields 3 incidents per monitored hour and 4 incidents over 2 monitored hours yields 2 per monitored hour. Lower observation coverage in the second period limits the comparison. Give the units in the visible answer. Keep figures and disclosures legible without a chart.

## States and recovery

| State | Visible behavior |
| --- | --- |
| Checking access | Show **Checking chat access…**. Enable Send after RAFIQ verifies connection, current consent, and eligibility. |
| Consent required or provider unqualified | Show the reason. **Review sharing** goes to D25 if there is an eligible link. An unqualified provider directs the driver back to Connections. |
| Empty or drafting | Show the suggestion buttons, scope, and composer. Filling a suggestion takes a separate Send action to share it. |
| Sending / waiting | Append the question once. Show **Sending…** only during local submission, then **Waiting for [Provider]…**. Keep feedback static. The API returns one complete reply. |
| Reply / scope expanded | Replace waiting with the complete labeled reply. Support opening individual scopes. Preserve the driver’s reading position and show **Jump to latest** when useful. |
| Known retryable failure | Keep the failed question and place **Retry** by its status. Recheck current authorization. Maintain one visible question for the turn and one outstanding attempt. |
| Ambiguous outcome | Show **We couldn’t confirm the result**. Automated resend requires a supported deduplication or recovery contract. |
| Expired connection | Disable sending and suppress invalidated pending replies. **Reconnect** goes through D25. Recheck consent on return and use a new chat after credential replacement. Require an explicit send. |
| Provider unavailable | Show **[Provider] is temporarily unavailable**. Retry an eligible transient failure or return to Connections. |
| Provider allowance exhausted | Explain the allowance limit. Include a reset time only when supplied and honor any API retry hint. Changing provider uses Connections and that provider’s own consent. |
| Close / sign-out / revoke / disconnect | Immediately remove the transcript, draft, waiting, and error content and withhold late replies. Close stays available during an outage and returns to D23 after local clearing. Sign-out returns to the signed-out flow. Revocation and disconnect expose the resulting provider state in D23. Storage is memory-only. |
| Report request | Offer **Report setup** to D17. Explain that a connected external MCP agent authors reports. D18 handles authorized review and export. |

[M08 design](../../ARCHITECTURE.md#module-m08--optional-chat) · [Experience feedback](../../EXPERIENCE.md#state-patterns) · [Report authoring](../../SCREENS.md#x02-external-mcp-agent)

## Motion, accessibility, and acceptance

- **D26-C03 · Motion for React.** Show a single proposed 120 ms ease-out opacity transition for the new reply only. The transcript takes its final layout immediately and earlier turns stay still. The accessibility announcement and interaction state update with the reply. Reduced motion shows full opacity immediately. Status, retry, disclosures, and authorization changes are immediate. Clear private content without retaining an exit frame. Core Motion is MIT licensed. Retain the copyright and permission notices when distributing covered code. [Motion entry examples](https://motion.dev/docs/react-animation) · [Reduced motion](https://motion.dev/docs/react-use-reduced-motion) · [Motion source and license](https://github.com/motiondivision/motion/blob/main/LICENSE.md)
- **Keyboard and announcements.** Give the page and log meaningful names, and preserve heading order, visible focus, and one reading path. Each disclosure exposes its expanded state and keeps focus on its trigger. The latest reply and actionable failure are announced once. Restore focus to the applicable D23 provider row after closing where it is available. Keep controls and status readable at 200% zoom and 320 CSS px. [Chat log semantics](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA23) · [Disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)
- **Pen.dev review.** Inspect the ready/empty desktop variants, the narrow and 320 px reflow examples, and the waiting, disclosure, recovery, report routing, and cleared states. Check that Temporary and Close remain identifiable, provider and consent statuses are distinct, and compact headers and expanded content wrap. Paired storyboard frames communicate the reply reveal and immediate reduced-motion state.
- **Frontend verification.** Exercise actual focus order and restoration, status announcements, scroll preservation, send limits, ambiguous outcomes, response gating, post-reconnect state, and clearing on close or authorization changes. In particular, close or revoke while a response is pending and check that neither a late result nor its original draft can reappear. Test provider qualification and privacy separately from these design fixtures.

## Canvas frames

The editable frames are in [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>) alongside D25. The five workspace frames share the **Question composer** component `kID8U`. Expanded and collapsed scope controls reuse the existing method-disclosure component `RcI4y`. The retry treatment is defined in the conversation states board.

| Frame | Pen node |
| --- | --- |
| 1440 px · Empty | `xuo2N` |
| 1440 px · Answer and sessions used | `P9fP2` |
| 1024 px · Answer and inline scope | `kHRfs` |
| 390 px · Empty and inline scope | `flgcU` |
| 320 px · Expanded scope and sessions used | `LpAeO` |
| Access, availability and closure | `qWE91` |
| Turns, recovery and report boundary | `amsxx` |
| D26-C03 · Reply entrance and reduced motion | `AOCk8` |
