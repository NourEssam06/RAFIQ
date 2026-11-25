# D25 Chat Connection and Consent

**Mode** · Operate. **Status** · Approved for design handoff.

The user approved **A · One-column guided flow** and **D25-C02 · Motion for React** for a brief confirmation cue. Keep the existing RAFIQ controls, semantic progress list, and native disclosure for supplemental provider policy details when approved material is available.

A signed-in, verified driver opens a named chat provider from **Settings → Connections**. Their task is to link an eligible subscription and decide whether RAFIQ may send their chat messages and relevant driving data to that provider. They can stop after linking and keep the account connected with sharing off. [D25 requirements](../../SCREENS.md#d25-chat-connection-and-consent) · [J7 temporary chat journey](../../EXPERIENCE.md#j7-ask-a-temporary-chat-question)

## Flow and action hierarchy

1. **Connect your subscription.** Name the provider, give the verified subscription requirement, and show availability, connection, and sharing as separately labeled states. For an eligible connection, **Connect** or **Reconnect** opens the provider’s official authorization flow. Explain that the driver will leave RAFIQ to authorize the link and return to review sharing. Linking never grants RAFIQ sharing permission.
2. **Review what RAFIQ shares.** After RAFIQ confirms the link, show **Connected** alongside **Sharing off** and move to the RAFIQ consent heading. Present the full decision-critical disclosure before two visible choices, **Allow sharing** and **Decline**. Use one affirmative action for this provider and disclosure version, with no preselection. Decline returns to D23 with the link intact and sharing off. D23 can reopen this stage via **Review sharing** when the link is current.
3. **Confirm and return.** While consent saves, keep the disclosure visible and prevent duplicate writes. On confirmed grant, show **Sharing on** and **Back to Connections**. D23 offers **Open chat** only when availability, the eligible connection, and consent to the current disclosure are confirmed. D26 owns the composer, send status, reply handling, and temporary conversation. Loss of any gate returns the applicable recovery without sending a message. [D23 Connections](../../SCREENS.md#d23-connections) · [D26 Temporary chat](../../SCREENS.md#d26-temporary-chat) · [M08 Optional Chat](../../ARCHITECTURE.md#module-m08--optional-chat)

Keep **Back to Connections** as a visible navigation affordance throughout. If the driver returns to D23 after a write or an uncertain provider handoff, refresh that provider row before offering the next action. Leave MCP grants in D23/D24 and account-wide retention and deletion in D22. Chat availability does not affect RAFIQ signup or core use.

## Approved layout

Use one content column inside the D19 Settings workspace. Keep these layers in the same order at desktop and narrow widths:

1. **Back to Connections** and the **Chat connection and consent** heading.
2. Compact provider identity card containing the name, eligibility statement, and separately labeled availability, account, and sharing values.
3. Static two-step indicator for **Connect your subscription** and **Review sharing**. Use an ordered list with distinct current and completed treatments. Wrap or stack the labels in order as space narrows.
4. Active step. Before linking, show the provider handoff explanation. After confirmed linking, show **Share driving data with [Provider]?** followed by the complete consent content. The provider card above shows **Connected** and **Sharing off**.
5. Action row directly after the active content, with the operation’s status beside or below it. Use **Connect** or **Reconnect** for the link step and **Allow sharing** and **Decline** for the consent step. After confirmation, replace the consent content with **Sharing on** and keep **Back to Connections** as the only action.

Use the existing private app navigation with **Settings** selected and **Connections** current. Read-only inspection found the desktop and narrow D19 Settings frames in `RAFIQ.pen` (`m9Bu2`, `Tl48f`, `sDEqS`) and the two-column D21 frame (`Z0Q6h`) with narrow and 320 px versions (`b41j1A`, `NFjMo`). Use the same 1440 px desktop reference, 48 px desktop content gutters, and 20 px narrow gutters at 390 px. Preserve `colors.canvas`, `colors.ink`, `colors.accent-stone`, the existing focus and status treatments, Space Grotesk as the established Mori substitute, `spacing.sm`/`md`/`xl` (8/16/24 px), and `rounded.md` (8 px) where controls or restrained panels call for a radius. Use a single scroll and a 60–70 character target reading measure where room allows. Wrap long copy and buttons in reading order. Check at 1024 px, 390 px, 200% browser zoom, and 320 CSS px. D25 has no chart requirement. [D19 handoff](D19-SHAPE.md) · [D21 handoff](D21-SHAPE.md) · [RAFIQ tokens](../../DESIGN.md) · [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

## Provider identity and eligibility

Use a compact identity card with the plain provider name as its anchor. Add the provider mark only when an approved asset and usage rules are available. The card is informational, with its own labeled action and three explicit status values. An example after a successful link is **Availability: Available · Account: Connected · Data sharing: Off**. Show the provider name and confirmed link state rather than sample emails or plan badges. The API supplies provider, qualification, connection, consent, and disclosure text and version. Exact plan names, connection identity details, and outage or subscription-specific reasons need verified provider evidence and an agreed UI data source. [API schema and operations](../../API.md)

| Condition | Driver-facing direction |
| --- | --- |
| Qualified provider | **Requires an eligible [Provider] subscription.** If the integration verifies and supplies eligible plan names, use that approved wording. Distinguish provider availability from the link result. |
| Provider qualification pending | **[Provider] isn’t available in RAFIQ yet.** Show an approved reason when known and return to D23. A subscription alone does not unlock the integration. |
| Provider confirms subscription ineligible | **This subscription isn’t eligible for RAFIQ chat.** Offer reauthorization if the driver can use another eligible subscription, or return to Connections. Use this copy only when eligibility is confirmed. |
| Qualified provider temporarily unavailable | **[Provider] is temporarily unavailable.** If the last confirmed link or sharing state is shown, label it as last confirmed. Mark unavailable status data as unknown. Offer an applicable status retry and preserve access to D23 management. |

RAFIQ qualifies each provider independently against hosted subscription-backed linking and inference, eligible test accounts, privacy controls, and zero project cost. Treat enabled examples as design fixtures until the provider passes. OpenAI documents limited partner availability for website sign-in and a separate plan-usage route for open-source and locally hosted apps, with an interest path for hosted offerings. Neither establishes RAFIQ’s hosted eligibility. Anthropic’s Console linked billing excludes consumer subscriptions for this flow. Keep Claude unavailable under the current requirement. Browser and API behavior must come from RAFIQ’s qualified integration. [PRD §8.9](../../PRD.md#89-optional-chat-provider-qualification) · [OpenAI website flow](https://developers.openai.com/siwc/website) · [OpenAI plan usage](https://developers.openai.com/siwc/token-sharing-open-source) · [Claude linked billing](https://support.claude.com/en/articles/18467148-use-your-claude-platform-account-in-a-third-party-app)

## Disclosure shown before consent

**Share driving data with [Provider]?**

> When you send a chat message, RAFIQ sends your message and relevant data from your own eligible driving sessions to [Provider] so it can answer your question.

| Visible section | Content |
| --- | --- |
| **What RAFIQ sends** | Your chat messages. Relevant session details such as session IDs, timestamps, duration and observation coverage. Behavior and incident counts. Validated summary metrics with their units and methods. Event details such as event ID, behavior type, when it started within the session, duration and severity. |
| **Data RAFIQ excludes** | Raw camera media, clips and clip links, contact details, precise location, raw measurement series, finished reports, and data from other accounts. Describe these as limits on the driving data RAFIQ adds to a message. |
| **How [Provider] handles data** | Show the approved, current provider-specific explanation and verified policy link if supplied. Keep the decision-critical explanation visible. When extra approved policy details are available, use a native **More about [Provider]’s data handling** disclosure immediately below the explanation. Missing current approved disclosure or version keeps **Allow sharing** unavailable. |
| **How to stop sharing** | **Settings → Connections → [Provider] → Revoke sharing** stops future sharing and clears an active RAFIQ conversation. The account can stay linked. **Disconnect** removes the saved connection and also clears the conversation. RAFIQ discards its temporary conversation on close or sign-out. Any provider handling of data already sent follows the approved provider disclosure. |

The decision is per provider and disclosure version. The approved data list is the maximum scope, and RAFIQ sends only relevant, currently authorized fields for each message. A new disclosure version requires a fresh decision. Keep the grant and the decline visible and comparable in size and legibility. [PRD §8.8](../../PRD.md#88-mcp-qualification-and-data-boundaries) · [TRD §6](../../TRD.md#6-external-protocols) · [API consent operation](../../API.md)

## State and recovery map

| State | What D25 shows and what the driver can do |
| --- | --- |
| Reading provider status | **Checking [Provider]…** in a stable status region. Keep the back link usable. On failure, show **Couldn’t check [Provider]** and **Retry**. |
| Available, unlinked | **Not connected** and **Sharing off**. Show the eligibility requirement and **Connect**. |
| Starting link or returning from provider | **Opening [Provider]…**, then **Checking your connection…** on return. Keep the action position stable. Use text or a static pending indicator with unknown duration. Progress advances only when RAFIQ confirms the new state. |
| Provider canceled, authorization expired, or link failed | Show the specific reason when confirmed, such as **Connection canceled** or **This connection attempt expired**. Offer a fresh **Connect** or **Reconnect**. For an uncertain outcome, check current provider state first. If an existing valid link remains, reconcile that state and keep the appropriate review path. |
| Connected, sharing required or revoked | Show **Connected** and **Sharing off**, put focus on the consent heading after provider return, and render the current disclosure with **Allow sharing** and **Decline**. |
| Connection expired or qualification lost | Show **Connection expired** with **Reconnect** when qualified. If qualification is lost, show provider unavailable and return to Connections. Keep D26 gated until the current connection and applicable consent are confirmed. |
| Saving consent | **Saving your choice…** next to the action. Keep focus stable and suppress repeat submissions. D26 stays gated. |
| Failed or unconfirmed consent write | Show **Couldn’t confirm your sharing choice** and **Retry**. Refresh current state first so an accepted write need not be repeated. Keep sharing unavailable until confirmed. If the disclosure changed, load the new version and request a new explicit choice. |
| Grant confirmed | **Sharing on** with a readable status and optional static check. **Back to Connections** returns to the provider row. D23 rechecks before exposing **Open chat**. |
| Declined | Return to D23 with **Connected** and **Sharing off**, with **Review sharing** available when eligible. Record or display only the outcome supported by the current API. **Decline** in the first-use flow does not invoke **Revoke sharing**. |
| Revoked or disconnected in D23 | Pending and confirmed feedback live on the provider row. Confirmed revoke stops future sharing, clears active chat, and suppresses affected replies. Disconnect also removes the saved connection. D25 reads the updated state on entry. Keep these management actions accessible in D23 when available, including during provider outages. |
| Allowance exhausted | D26 owns the send result and applicable recovery. If an authoritative allowance status is available in D23/D25, keep it distinct from expiry and unavailable service. Show a reset only when confirmed. |

The API grant example returns `required`, although the documented operation records a grant. Use confirmed `granted` for the success design and flag the example for contract verification. Also confirm how consent is bound when reconnect changes the subscription account. D25 must wait for the server to return the applicable link and consent state before enabling chat. [API contract](../../API.md) · [TRD chat acceptance](../../TRD.md#8-measurable-acceptance-and-release-gates)

## Approved components

- **Reuse from RAFIQ.** Use the D19 Settings navigation and compact section selector, back navigation, primary and secondary buttons, keyboard focus treatments, and inline job status. Use D21’s inline consent layout as a placement reference.
- **Use standard controls.** Use buttons for consent actions, an ordered list for the two stages, native `details` and `summary` for supplemental policy content, and a persistent status region for operation feedback. Essential scope, provider handling, and revocation instructions stay visible when the disclosure is collapsed. [GOV.UK Details](https://design-system.service.gov.uk/components/details/) · [WAI disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)
- **Compose for D25.** Use a named provider identity card, a versioned sharing panel, and a stable inline feedback slot. The provider owns its authorization screen and RAFIQ owns the sharing decision on return.

### Research references

The GOV.UK task list shows how to label the status of each task in text. D25 uses that cue for two sequential stages. Google’s authorization guidance illustrates how account identity and explicit permissions can be presented as distinct decisions. [GOV.UK Task list](https://design-system.service.gov.uk/components/task-list/) · [Google authorization guidance](https://developers.google.com/identity/oauth2/web/guides/how-user-authz-works)

**D25-C02** is the approved animation. Keep the static treatment as the resting and reduced-motion state. The other animation candidates are retained as research references.

| ID | Component | Library | Intended placement | Animation behavior | Free/license verification | Demo URL | Trade-offs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **D25-C00** | Static stages, disclosure, and feedback | RAFIQ and browser-native controls | Entire flow | State text and icons update immediately. Supplemental details expand instantly. | Existing and native controls. No package. | [Details pattern](https://design-system.service.gov.uk/components/details/) | Provides the resting and reduced-motion states. Pen.dev can show every resting state. |
| **D25-C01** | Stepper | React Bits | Two-stage status indicator | Gliding markers and spring transitions. Treat the demo as visual reference for the indicator only. | Free to use under MIT + Commons Clause. Keep notices. The license restricts standalone component redistribution. [Source](https://github.com/DavidHDev/react-bits/blob/main/src/ts-default/Components/Stepper/Stepper.tsx) · [License](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md) | [Stepper](https://reactbits.dev/components/stepper) | React and TypeScript/CSS with Motion. The source controls its own progression and navigation. Adopting it would require stripping that behavior, binding the indicator to server state, and adding verified keyboard semantics and a static reduced-motion path. Pen.dev can show the two markers as snapshots. |
| **D25-C02** | `motion` component | Motion for React | Confirmed stage marker or status glyph | One 120–150 ms opacity change on confirmation, with state text visible immediately. | Free MIT core. Keep copyright and license notice when distributing. [Source](https://github.com/motiondivision/motion) · [License](https://github.com/motiondivision/motion/blob/main/LICENSE.md) | [Motion component examples](https://motion.dev/docs/react-motion-component) | Add `motion` in the Next.js interactive client component if already justified by the app. Use `useReducedMotion` to skip decorative opacity as well. Low local rendering work, extra client dependency if new. Pen.dev can show the start and end glyph. |
| **D25-C03** | Collapsible | Animate UI · Radix UI primitive | Optional provider policy details | Default animates height with a fade and blur. The docs say reduced motion still plays fade and blur. | Free MIT + Commons Clause. Keep notices. The license restricts selling or redistributing the original components. [Source](https://github.com/imskyleen/animate-ui) · [License](https://github.com/imskyleen/animate-ui/blob/main/LICENSE.md) | [Collapsible](https://animate-ui.com/docs/primitives/radix-ui/collapsible) | `@animate-ui/react` and `motion` add client dependencies. Height changes can reflow adjacent content. For RAFIQ, omit blur and make reduced motion instant, using a static alternative if the component cannot meet that behavior. Pen.dev can show expanded and collapsed states. |
| **D25-C04** | Collapsible | Radix Primitives | Optional provider policy details | Optional CSS height change using the documented content-height variable. | Free MIT. Keep copyright and license notice when distributing. [Source](https://github.com/radix-ui/primitives/blob/main/packages/react/collapsible/src/collapsible.tsx) · [License](https://github.com/radix-ui/primitives/blob/main/LICENSE) | [Collapsible demos](https://www.radix-ui.com/primitives/docs/components/collapsible) | React primitive fits a Next.js client component. Adds a dependency unless already present. A height change costs layout work. Use a short duration and disable it under reduced motion. Pen.dev can show both heights with the same trigger. |
| **D25-C05** | CSS opacity on existing status glyph | RAFIQ | Confirmed link and sharing outcomes | Optional 120–150 ms fade on the decorative glyph only. Failure text, actions, and privacy state update immediately. | No library or copied component. | [Status pattern](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) | Recommended if motion is desired. No added JavaScript dependency. Show the finished glyph immediately for reduced motion. Pen.dev can annotate both glyph states and timing. |

## State transitions and motion

| Trigger | Approved visual change |
| --- | --- |
| Driver starts linking or returns from provider | Show **Opening [Provider]…** or **Checking your connection…** immediately in the stable status slot. Maintain the current stage until the result arrives. |
| RAFIQ confirms an eligible link | Mark the link stage complete and switch immediately to the sharing decision. Show **Connected · Sharing off** for first use and focus the consent heading. Fade in the link-success check once. |
| Consent save begins or resolves | Replace the inline status with **Saving your choice…**, the confirmed **Sharing on** state, or the applicable retry. Keep status text and actions available as soon as the state is known. Fade in the check once on confirmed consent. |
| Driver toggles policy details | Switch instantly between collapsed and expanded. Keep focus on the disclosure trigger and leave the essential consent content visible. |

For each success, use **D25-C02** for a single **150 ms ease-out** opacity change from 0 to 1 on the decorative check glyph. The status text, layout, focus and available actions update at 0 ms. Keep the same icon slot throughout and use static pending and failure states. Reduced motion shows the icon at full opacity immediately. Include the two glyph-opacity keyframes and the reduced-motion state on the Pen storyboard. In the frontend, use Motion for React’s `motion` component and `useReducedMotion`. [Motion component reference](https://motion.dev/docs/react-motion-component) · [Reduced-motion hook](https://motion.dev/docs/react-use-reduced-motion)

## Accessibility and Pen.dev review

- Mark the current stage programmatically and leave the indicator out of the tab sequence. Use explicit status words with icons or color as support. Use headings and real buttons and links. An optional disclosure keeps focus on its trigger, supports Enter and Space, and exposes expanded state.
- After provider return, focus the current RAFIQ task heading when the result is known. For in-place pending, save success or failed consent, preserve focus where possible and announce a concise change once. Keep a visible error and recovery action beside the operation. Return focus to the originating provider row on D23. Preserve visible focus and reading order at zoom. [WAI status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) · [WAI disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)
- In [the RAFIQ Pen canvas](<../../../Pen Design/RAFIQ.pen>), draw editable desktop and narrow frames for eligible unlinked, linked with sharing off, and sharing confirmed. Include 320 px consent reflow and a state board for pending link, cancellation, expiry, unqualified versus outage, consent saving/failure, and decline return. Use synthetic fixtures. Include a collapsed and expanded supplemental-details pair. Annotate the external handoff and D23/D26 destinations. Pen.dev can represent visual states and annotated transitions. Verify provider handoff, eligibility, authorization, keyboard operation and announcements in the frontend.

### Canvas frames

| Frame | Pen node |
| --- | --- |
| Connect, review sharing, sharing confirmed · 1440 px | `d25016eb3c78`, `d25d88ad3405`, `d25c34670b76` |
| Connect, review sharing, sharing confirmed · 390 px | `d2598f3e2f52`, `d25f214fb01c`, `d2501035d942` |
| Review sharing · 1024 px | `d259259a4477` |
| Review sharing with policy details expanded · 320 px | `d251d75b5e86` |
| Link and eligibility states, sharing and return states | `d25ed1187f0a`, `d25846a79412` |
| D25-C02 confirmation storyboard | `d256e9b85a7b` |

The enabled examples use **Aster Chat**, a fictional provider with illustrative policy copy. Use the approved disclosure and confirmed availability when implementing an actual provider.

## Acceptance checks

- The driver can distinguish provider availability, a linked subscription and their RAFIQ sharing choice before and after a provider return. Linking alone and failed or pending consent leave D26 gated. Decline returns to a linked but non-sharing provider row.
- Before granting, the driver can read the data categories, excluded categories, approved provider handling and exact revocation path without expanding supplemental material. An outdated or missing disclosure cannot yield a grant.
- A provider outage, an ineligible subscription, an expired connection and a canceled authorization each yield the applicable next action. Revoke and disconnect are distinguishable and tests cover pending replies after invalidation.
- The decision path remains usable with a keyboard, reduced motion, long provider copy, browser zoom and 320 CSS px reflow.

Provider eligibility, consent binding on relink, the grant response example, and production provider wording remain integration verification items.
