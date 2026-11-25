# D23 Connections

**Approved** · **A · Stacked settings** with **C00 · RAFIQ-native components**. Use the static treatment. This is an Operate screen for a signed-in, eligible driver managing external access in Settings while stationary. The driver can identify who has access, revoke one permission, and tell whether an optional provider is qualified, linked, and allowed to receive driving data. [Screen requirements](../../SCREENS.md#d23-connections) · [Connections and chat journeys](../../EXPERIENCE.md#mcp-connection-reports-and-optional-chat)

## Frame and navigation

1. Reuse the D19 private shell with **Settings** selected and **Connections** current. Use **Connections** as the page heading. Entry points are Settings, **Manage connections** in D22 Privacy, and external-agent help in D17 Reports. Preserve the originating context on Back while it remains accessible.
2. Put **MCP clients** first. In order, show the RAFIQ endpoint and copy action, **Setup instructions**, a short explanation with **View reports**, and the client list or its state. Report requests start in the external agent (X02). **View reports** opens D17 for review and export through D18. MCP authorization starts in the client and opens D24.
3. Follow with **Optional chat providers**. Stack a card per returned provider. **Connect**, **Reconnect**, and **Review sharing** open the applicable step in D25. **Open chat** opens D26 when eligible. Returning from D25 refreshes the provider before exposing actions that depend on the result.

Use D19 desktop `m9Bu2`, narrow `Tl48f`, and 320 px reflow `sDEqS` for navigation and D21 desktop `Z0Q6h` for spacing. Start with a 1440 px reference and 48 px desktop content gutters. Use 20 px at the 390 px reference. Use the compact Settings selector at narrow widths. Keep the same reading order, single page scroll, and single content column at 1024 px, 390 px, 200% browser zoom, and 320 CSS px reflow. Wrap long names, endpoint text, and actions. Let dialog content scroll within the viewport when needed. [RAFIQ Pen canvas](<../../../Pen Design/RAFIQ.pen>) · [D19 shell](D19-SHAPE.md) · [D21 spacing](D21-SHAPE.md) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

Use `colors.canvas` (#0e100f), `colors.ink` (#fffce1), `colors.accent-stone` (#bbbaa6), and Space Grotesk, the documented Mori substitute. Use flat dividers, `spacing.sm` (8 px) for compact label groups, `spacing.md` (16 px) inside rows and cards, `spacing.xl` (24 px) between groups, and `rounded.md` (8 px) on existing control and panel treatments. Keep the established focus and destructive styles. [Visual tokens](../../DESIGN.md)

## MCP clients

- **Endpoint and copy.** Render the single server-configured HTTPS endpoint as selectable, wrapping text. The **Copy endpoint** button writes the exact value. After a successful write, show **Endpoint copied** with a check beside the button and announce it once. If the clipboard write fails, show **Couldn’t copy. Select and copy the endpoint.** Keep the button focused and the text selectable. Use `https://api.rafiq.example/mcp` only in design fixtures. [Connection API](../../API.md#7-detailed-endpoint--operation-specifications) · [Clipboard behavior](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/writeText)
- **Setup instructions.** Reuse RAFIQ’s method disclosure (`RcI4y`), collapsed by default. On expansion, show three steps. Add the HTTPS endpoint as a remote Streamable HTTP server in a compatible client. Start the RAFIQ authorization flow from that client and sign in. Review the two permissions independently in D24 and return to the client. Explain that the driver can request a report in the authorized client and review or export it in RAFIQ. [Setup and data boundaries](../../PRD.md#88-mcp-qualification-and-data-boundaries) · [External agent](../../SCREENS.md#x02-external-mcp-agent)
- **Client identity and scopes.** Group server grants by `clientId` and display `clientName`. Keep same-name clients distinct and show the metadata hostname when needed to disambiguate. Bind each revoke to its own `grantId`. Each card has both labeled permission rows in a stable order, with its own state and available action. Keep grant descriptions visible with setup collapsed. [Grant schema](../../API.md#7-detailed-endpoint--operation-specifications) · [D24 authorization](D24-SHAPE.md)

| Permission | Visible summary | Action on an active grant |
| --- | --- | --- |
| **Read driving data** (`driving:read`) | View approved session summaries, analytics, and event details from your own driving sessions. | **Revoke read access** |
| **Author reports** (`reports:author`) | Start a report job, use its approved inputs and template, check its status, and submit a draft for review in RAFIQ. | **Revoke report authoring** |

The read grant covers approved summaries, analytics, and event metadata. The author grant gives access to approved inputs scoped to the authorized job. Show the shared exclusions below the permissions or in setup detail: raw media and measurement series, clips and clip links, contacts, precise location, finished reports, and other accounts’ data. [PRD data boundaries](../../PRD.md#88-mcp-qualification-and-data-boundaries)

| State | What the driver sees |
| --- | --- |
| Checking or read failure | **Checking MCP connections…** or **Couldn’t load MCP connections** with scoped **Retry**. Show the endpoint and permissions when the authorized read supplies them. |
| No active grants | **No MCP clients have access.** Keep setup and endpoint copy available. |
| Read only, author only, or both | Render **Active** on each grant supplied and **No active grant** on the other permission when applicable. |
| Just revoked | Confirm the exact permission and client. Keep an immediate result in context even when the last active grant is gone. |
| Known expired or revoked authorization | Identify the affected client or permission when an authoritative outcome provides it. Explain how to start fresh authorization from the client. |

The current MCP read returns the endpoint and active grants. The grant schema has no status, expiry timestamp, or history. A persistent expired or revoked list needs an API addition. Represent identified expired and revoked states as conditional Pen examples. A grant missing from a fresh read is **No active grant** unless its outcome is known. Fresh authorization returns through D24. [API contract](../../API.md#7-detailed-endpoint--operation-specifications)

## Optional chat providers

Give the provider card a name and three visible label–value rows. Use the provider response as the state authority. The contract supports up to two providers. Use ChatGPT and Claude as design fixtures and label qualified examples as illustrative until RAFIQ verifies each integration. Use the provider name in text. Add a provider logo only with an approved asset. [Qualification requirements](../../PRD.md#89-optional-chat-provider-qualification) · [D25 consent flow](../../SCREENS.md#d25-chat-connection-and-consent)

| Row | Text values |
| --- | --- |
| **Qualification** | **Qualified** or **Not qualified** |
| **Connection** | **Connected**, **Not connected**, **Connection expired**, or **Unavailable** |
| **Driving-data sharing** | **On**, **Off · review required**, or **Revoked** |

| Condition | Action and feedback |
| --- | --- |
| Qualified and disconnected, or qualified and expired | **Connect** or **Reconnect** opens D25. Linking and consent require separate actions. |
| Qualified and connected, with consent required, revoked, or out of date | **Review sharing** opens the current provider disclosure in D25. After decline, the connection can remain **Connected** with sharing off. |
| Qualified, connected, consent current, and chat eligible | **Open chat** opens D26. Recheck eligibility before sending. |
| Current sharing grant | **Revoke sharing** stops future driving-data sharing immediately, clears the provider’s temporary chat, and suppresses invalidated replies. The provider can stay linked. |
| Existing linked account | **Disconnect** removes the saved connection and local sharing permission, ends the temporary chat, and suppresses invalidated replies. |
| Unqualified, unavailable, or allowance exhausted | Show the known reason and applicable recovery. Use generic unavailable copy when a reason is absent. Keep removal actions available where current grant or link data supports them. |
| Checking, fetch failure, or no provider entries | Use **Checking chat providers…**, **Couldn’t load chat providers** with scoped **Retry**, or **No chat providers are available**. Keep MCP independently usable. |

The provider-list schema lacks a dedicated allowance field, unavailability reason, and linked-credential indicator for the generic unavailable state. Use quota or reason copy only when the service establishes it. A generic unavailable response alone cannot establish that a connection still exists. Reconcile after returning from D25 or after an uncertain mutation. Public signup stays independent of chat availability. [Provider contract](../../API.md#7-detailed-endpoint--operation-specifications) · [Temporary conversation rules](../../TRD.md#6-external-protocols)

## Revocation and feedback

Reuse D21’s **Reorder and remove** board (`pb6JC`) for the dialog and mutation states. Use these titles and action labels with an explicit **Cancel**. Cancel restores focus to the specific opener. On success, restore focus to the surviving permission or provider, or to the group heading when the last client leaves. Label repeated actions with both the visible action text and the affected client or provider name for assistive technology.

| Dialog title | Consequence | Confirm action |
| --- | --- | --- |
| **Revoke read access for [client]?** | The client loses access to approved driving summaries, analytics, and event details through this grant. A separately granted report-authoring permission stays active. | **Revoke read access** |
| **Revoke report authoring for [client]?** | This client loses permission to author reports. A report in progress can be blocked from publication. A separate read grant stays active. | **Revoke report authoring** |
| **Revoke sharing with [provider]?** | RAFIQ stops sharing driving data and clears the open temporary chat. The account can stay connected. | **Revoke sharing** |
| **Disconnect [provider]?** | RAFIQ removes the saved connection, turns off sharing, and clears the open temporary chat. | **Disconnect** |

Name a separate surviving MCP grant only when it is active. Open the dialog immediately with focus on **Cancel**. Contain focus and support Escape before submission. On confirm, show **Revoking…** or **Disconnecting…** in the affected dialog, prevent duplicate submissions, and retain context through a recoverable failure. On confirmed success, update only the affected grant or provider and announce the outcome once. After an uncertain response, refresh the authorized state before claiming success or retrying the write. On account access loss, clear private values and actions and follow the existing sign-in or restricted-account route. [D21 dialog](D21-SHAPE.md) · [MCP and chat mutations](../../API.md#7-detailed-endpoint--operation-specifications) · [Alert-dialog semantics](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/) · [Status announcements](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

## Pen.dev handoff and acceptance

The [RAFIQ Pen canvas](<../../../Pen Design/RAFIQ.pen>) contains these editable D23 layouts and state boards.

| Frame | Pen node |
| --- | --- |
| Connections · Desktop 1440 px | `USNTi` |
| Connections · Narrow desktop 1024 px | `hGTFH` |
| Connections · Narrow 390 px | `SFRCN` |
| Connections · 320 px reflow | `K8bS8` |
| Endpoint and setup | `l7q5VX` |
| MCP access states | `z1o9N` |
| Provider actions | `p9L3ct` |
| Revocation and disconnect | `HtnPk` |
| Report authoring revocation dialog · 320 px | `T0RLX` |

The client and provider cards use existing RAFIQ layers, including its text-plus-icon status rows (`Yh4JZ` and `fqIDy`). Use standard buttons, headings, status, disclosure, and dialog behavior in the frontend. The selected component set uses existing RAFIQ and browser primitives.

Show a mixed desktop frame, narrow desktop and reflow frames, and focused state boards for copy outcome and setup, MCP grant combinations and scoped revocation, the provider action matrix, and each named confirmation with pending, failure, and success. Use synthetic clients and the example HTTPS endpoint. Include a long client name and a linked provider with sharing off. Keep text status visible with a non-color cue, verify contrast, and show the focus ring on the opening control and dialog cancel button.

The storyboard is instantaneous. Copy success swaps to a check after the write resolves. The disclosure reveals or hides its content on activation. Dialog opening and focus happen together. Server-confirmed mutations replace their pending state immediately. Use the same endpoints with reduced motion. Pen.dev represents those frames and focus positions. Frontend verification exercises the actual clipboard, authorization, provider actions, announcements, and state changes.

- Follow D17 and D22 into D23, authorize through D24, and verify that fresh grants appear only after an authorized read. Verify that each individual revoke denies only its own grant and that loss of authoring can block a pending report release.
- Confirm endpoint copy and manual-copy fallback. With a keyboard, expand and collapse setup, revoke each type of access, cancel safely, and recover focus when a client disappears. Verify one accessible announcement per meaningful outcome.
- Exercise each provider’s three independent state rows, including linked with sharing off, qualified but expired, and unqualified. Confirm that stale consent or unavailable eligibility gates D26. Verify that revoking or disconnecting during a chat clears it and suppresses late replies.
- Check scoped read and mutation failures, timeout reconciliation, duplicate clicks, and access loss. At narrow widths and zoom, verify full values, readable state labels, reachable controls, and absence of page-level horizontal scrolling.
