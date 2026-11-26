# Phase 0 shared Pen component handoff

FND-03 and NFR-04 preparation · [Issue #8](https://github.com/alisameh05/RAFIQ/issues/8) · [Pen inventory baseline](../IMPLEMENTATION_GUIDE.md#4-pen-design-and-screen-ownership) · [Shared design rules](../SCREENS.md#shared-design-rules)

## Screen and touchpoint inventory

Use **Find layers** in the [shared RAFIQ canvas](https://app.pen.dev/s/fZ1Fr2k_GIRpAwvABYPvw8LcwmOajmza6vjtx0ivitU). Each row gives a screen ID, its approved brief and a starting board. The implementation guide lists additional nodes and owning slices. The [local Pen canvas](<../../Pen Design/RAFIQ.pen>) accompanies the versioned briefs.

On 26 November 2026 the shared URL opened without sign-in in read-only mode. One representative board per ID was found. D10 and D11 matched by name. D08's additional local references are listed below. Individual contributor access and any required edit access are pending confirmation from the workstream owners.

| ID and approved brief | Shared board lookup |
| --- | --- |
| [P01 Public entry](../SCREENS.md#p01-public-entry) | `C1FjLG` RAFIQ / Landing • Desktop, `dYJ5V` Landing ending / Launch, `mXNJd` Landing ending / Film release, `NfQH8` Prototype handoff |
| [P02 Create account](../SCREENS.md#p02-create-account) | `T8ElF1` |
| [P03 Verify email](../SCREENS.md#p03-verify-email) | `cYZwN` |
| [P04 Sign in](../SCREENS.md#p04-sign-in) | `A2pKS` |
| [P05 Recover access](../SCREENS.md#p05-recover-access) | `O8GPEq` |
| [P06 Controlled-use onboarding](../SCREENS.md#p06-controlled-use-onboarding) | `n4mRND` |
| [P07 Restricted account](../SCREENS.md#p07-restricted-account) | `Evx5p` |
| [P08 Unavailable link](../SCREENS.md#p08-unavailable-link) | `tb0lo` |
| [D01 Dashboard](screens/D01-SHAPE.md) | `v2yld` |
| [D02 Start and readiness](screens/D02-SHAPE.md) | `Umfho` |
| [D03 Monitoring](screens/D03-SHAPE.md) | `rshez` |
| [D04 Emergency Mode](screens/D04-SHAPE.md) | `kdm50` |
| [D05 End and recovery](screens/D05-SHAPE.md) | `SM6Bl` |
| [D06 Sessions](screens/D06-SHAPE.md) | `m14mRu` |
| [D07 Session Detail](screens/D07-SHAPE.md) | `JMZok` |
| [D08 Incident and alert details](screens/D08-SHAPE.md) | `S3YUmp` and the recovery references below |
| [D09 Personal Overview](screens/D09-SHAPE.md) | `DQsAR` |
| [D10 Clips](screens/D10-SHAPE.md) | `D10 · Mixed evidence · Desktop` (local `a4E9dg`) |
| [D11 Clip replay](screens/D11-SHAPE.md) | `D11 · 01 · Ready from Clips` (local `mO84X`) |
| [D12 What-If](screens/D12-SHAPE.md) | `Vkofe` |
| [D13 What-If result](screens/D13-SHAPE.md) | `wLURY` |
| [D14 Experiment Studio](screens/D14-SHAPE.md) | `C9cxW` |
| [D15 Study result](screens/D15-SHAPE.md) | `onvGo` |
| [D16 Benchmark](screens/D16-SHAPE.md) | `R1X5V` |
| [D17 Reports](screens/D17-SHAPE.md) | `iFsda` |
| [D18 Report review and export](screens/D18-SHAPE.md) | `FRz35` |
| [D19 Profile](screens/D19-SHAPE.md) | `m9Bu2` |
| [D20 Monitoring settings](screens/D20-SHAPE.md) | `CLW1T` |
| [D21 Emergency contacts](screens/D21-SHAPE.md) | `Z0Q6h` |
| [D22 Privacy](screens/D22-SHAPE.md) | `Q3ZGZd` |
| [D23 Connections](screens/D23-SHAPE.md) | `USNTi` |
| [D24 MCP authorization](screens/D24-SHAPE.md) | `bl12N` |
| [D25 Chat connection and consent](screens/D25-SHAPE.md) | `d25016eb3c78` |
| [D26 Temporary chat](screens/D26-SHAPE.md) | `xuo2N` |
| [A01 Admin entry and invitation](screens/A01-SHAPE.md) | `y37Fa` |
| [A02 Authenticator](screens/A02-SHAPE.md) | `Q3KI57` |
| [A03 MFA recovery](screens/A03-SHAPE.md) | `DBNnU` |
| [A04 Service Health](screens/A04-SHAPE.md) | `KDEbz` |
| [A05 Release Readiness](screens/A05-SHAPE.md) | `o585O` |
| [A06 Adoption](screens/A06-SHAPE.md) | `PuMuP` |
| [A07 Account Support](screens/A07-SHAPE.md) | `z9GEa` |
| [A08 Staff Access](screens/A08-SHAPE.md) | `Dh0sT` |
| [A09 Audit](screens/A09-SHAPE.md) | `AzYl3` |
| [X01 Emergency recipient](screens/X01-REFERENCES.md) | `x0PSF` |
| [X02 External MCP agent](screens/X02-SHAPE.md) | `P8F6b`, `amIpw`, `OCnNm` |

### D08 recovery and narrow layouts

- `S3YUmp` is the shared incident board. D08 sits below D07’s timeline and above the ordered event list. The panel keeps occurrence, timestamp and evidence visible while the driver opens supporting measurements or delivery updates.
- The approved brief places the warning and related detections at `O7FNIf`, the canceled-before-send example at `p7Nrf` and expanded channel outcomes at `GdiNk`.
- `nKOpH` shows 390 px reflow with expanded measurements, expired clip and action focus. `o4SSzo` shows 320 px reflow with compact timeline controls and an expired clip. At 200% zoom use the same stacking and reading order. Keep incident evidence available after expiry.
- `KPjNE` documents selection accent endpoints, reduced motion, scoped loading, retry and missing evidence. Keep selection and the elapsed time stable during scoped feedback. On close and return, restore the selected trigger or the nearest eligible target.
- The six variant IDs above are recorded in the approved local handoff and did not resolve by ID in the shared viewer. Product UI owns locating or publishing the equivalent shared references. [D08 frame and state table](screens/D08-SHAPE.md#pendev-frames) · [D07 timeline](screens/D07-SHAPE.md)

### X02 external client handoffs

- `P8F6b` traces connect and authorize, request, retrieve eligible evidence, check status, submit or revise, and return to RAFIQ. The four external tool examples use `pNZeB`.
- `amIpw` maps D23 setup → D24 consent → external client → D17 review entry → D18 validated report or withdrawal. Read and author grants are independent, and a successful submit can still leave the report processing.
- `OCnNm` documents recovery and status, including draft revision via `Yh4JZ`. Trace decline, missing inputs, lost replies, revision, withdrawal and revocation against the approved recovery table. The external client owns its native presentation. [X02 storyboard and recovery](screens/X02-SHAPE.md#pendev-implementation) · [J6 journey](../EXPERIENCE.md#j6-author-through-mcp-and-review-a-report)

## Reusable patterns and assets

Shared boards verified by ID are **RAFIQ UI · Design foundations** `v3WGH`, **Desktop composition** `kSXKr`, **Mobile composition** `KBsd3`, **Controls and usage** `giojv` and **RAFIQ · Motion components** `GtBsN`.

| Pattern | Approved examples and browser fixture |
| --- | --- |
| Tokens and typography | `v3WGH` and D01 specify warm canvas, ink and stone, 8/16/24 px spacing and 8 px radius. A02 and D08 use Space Grotesk as the Mori substitute. The fixture uses those palette and spacing roles, scalable type and a system fallback. [Design](../DESIGN.md) · [D01](screens/D01-SHAPE.md) · [A02](screens/A02-SHAPE.md#layout-and-visual-references) |
| Driver and admin shells and navigation | D06 establishes the Sessions shell and narrow layout. A04 and A05 establish the separate staff shell. The fixture uses separate named navigation landmarks and local destinations for both examples. [D06](screens/D06-SHAPE.md#frame-structure) · [A04](screens/A04-SHAPE.md#frame-and-components) · [A05](screens/A05-SHAPE.md) |
| Status rows | D05 `CDaKQ`, D17 and X02 `Yh4JZ` pair text with a symbol. The fixture shows Ready, Operational and Pending, and announces the session refresh through a persistent status region. [D05](screens/D05-SHAPE.md) · [D17](screens/D17-SHAPE.md#status-and-recovery) |
| Forms, dialogs and focus | D06 filter labels and A02 confirmation anatomy inform the named period filter and confirmation. The fixture uses native form and dialog controls, a skip link, a cyan visible focus ring, safe initial focus, Escape and focus return. [D06](screens/D06-SHAPE.md#accessibility-and-acceptance) · [A02](screens/A02-SHAPE.md#state-frames-and-accessibility) |
| Loading and motion | D06 `AXgTB` and D08 `KPjNE` show scoped loading and a static alternative. The fixture keeps previous values readable, moves through Loading and Ready, and renders its decorative indicator without animation when reduced motion is active. [D06](screens/D06-SHAPE.md#back-restoration-and-motion) · [D08](screens/D08-SHAPE.md#components-and-motion) |
| Charts | D09 specifies exact values and an equivalent data table. The fixture puts synthetic warning counts and their decorative bars in the same semantic table and identifies the period, sample size and scale. [D09](screens/D09-SHAPE.md#components-motion-and-reflow) |

| Asset or conflict | Existing decision or evidence | Accountable follow-up |
| --- | --- | --- |
| Token exports and action styles | DESIGN and the approved briefs establish the palette, spacing and cyan focus. The exported GSAP-derived primary label (`#7c7c6f`) and pill treatment need reconciliation with RAFIQ’s cyan outline, cream label and control radius. The fixture uses the approved RAFIQ form treatment. [CSS variables](<../../Pen Design/variables.css>) · [JSON tokens](<../../Pen Design/tokens.json>) · [Tailwind mapping](<../../Pen Design/tailwind.css>) | Product UI confirms the shared application mapping and issues the canonical export before dependency pinning. Pending. |
| Typography | Approved briefs document Mori where licensed and Space Grotesk as substitute. Mori has no recorded RAFIQ web entitlement. Space Grotesk upstream provides OFL 1.1. The fixture uses a locally available Space Grotesk with a system fallback and makes no font request. [Mori foundry](https://pangrampangram.com/products/mori) · [Space Grotesk source and license](https://github.com/floriankarsten/space-grotesk) | Product UI records the chosen family and, for a redistributed build, its exact source and license notice. Pending. |
| Scanner and compact loader | The adapted scanner has a checked-in Lottie Simple License and creator attribution. The vendored lottie-web renderer has an MIT notice. Compact arc and static references are in the handoff. The fixture uses its own CSS indicator. [Loader handoff](<../../Pen Design/RAFIQ-loader.md>) · [Scanner license](<../../Pen Design/brand/loaders/LICENSE.txt>) · [Renderer notice](<../../Pen Design/brand/loaders/lottie-web-LICENSE.md>) | Product UI incorporates the scanner notice if reused and records compact asset provenance before distribution. Pending. |
| Brand and landing | The brand direction records the approved wheel, RAFIQ wordmark and static fallback. The landing handoff includes a GLB and still/turntable fallbacks. Three.js has a bundled MIT notice. The GLB, landing images, GSAP and ScrollTrigger need source-version and reuse-rights confirmation before distribution in the shared application. [Brand handoff](<../../Pen Design/brand/brand-logo-direction.md>) · [Landing preview](<../../Pen Design/RAFIQ Scroll Prototype.html>) · [Three.js notice](<../../Pen Design/agent/three-LICENSE.txt>) | Product UI and the asset owner document model, graphics and motion-library provenance and retain the necessary notices. Pending. |

The standalone fixture has no added package pins or vendored design assets.

## Preview and verification

Open [the standalone HTML preview](../../web/public/pen-fixture/index.html) from a checkout and keep its sibling CSS and JS beside it. On a running local RAFIQ web fixture, open [the same preview over HTTP](http://localhost:3000/pen-fixture/index.html). It uses synthetic data and runs without an API. From `web`, run `npm run test:e2e -- pen-fixture.spec.ts`. [Browser test](../../web/tests/pen-fixture.spec.ts)

### Recorded browser run

On 26 November 2026, all six fixture tests passed on Windows 10 22H2 with Chrome `158.0.8127.88` and bundled Chromium `159.0.8154.6`. The synthetic fixture and tests in this change are the evidence source.

| Check | Observed result |
| --- | --- |
| Keyboard, focus and dialog | Tab order reached the skip control, driver navigation, labeled period input and actions. The refresh button had a 3 px solid outline. The dialog focused Cancel and returned focus to the opener after Escape and Cancel. |
| Loading, reduced motion and chart | The browser exposed Loading and Ready through the same status role without moving focus. Reduced motion removed the loading animation. The warning rows exposed counts of 9 and 4, matching the bars. Actual screen-reader speech is pending. |
| Desktop and narrow reflow | The workspace was side by side at 1440 CSS px and stacked at 640, 390 and 320 CSS px. The page and open dialog fit without horizontal overflow. |
| 200% browser zoom | Chrome's Page zoom setting changed the layout viewport from 1424 to 712 CSS px. The page had no horizontal overflow, the dialog actions fit in view, and Escape restored focus to the opener. |
| Preview over HTTP | The production Next.js build returned HTTP 200 for the HTML, CSS and JS. |

### Reviewer walkthrough

For a reviewer run, keep Chrome at 100% for the 1440, 390 and 320 CSS px checks. Then use Chrome’s zoom menu to set 200% on a desktop viewport and repeat the control and dialog checks. Record the browser, viewport, zoom, revision, reviewer, and observed result.

1. Tab to **Skip to content**, press Enter, and follow the Sessions and Personal Overview links in tab order before the named Session period field and its two buttons. Check that focused controls have an unobstructed visible ring.
2. Open **Clear selection**, verify that **Cancel** has initial focus, dismiss with Escape, and verify focus returns to the opener. Repeat with Cancel and check that confirm resets the period to seven days.
3. With a screen reader running, select **Last 30 days** and activate **Refresh summary**. Expect one loading message and one ready message, with focus staying on Refresh summary. Verify the period label, the named dialog, and the Drowsiness and Distraction rows with counts of 9 and 4. Check the status delivery itself in the reader’s speech output.
4. Enable reduced motion, refresh again and check that the indicator remains static while the same loading and ready text appears. Open **Clip availability** with the keyboard and check that the expired clip explanation is readable. Verify that the dialog controls and chart values fit at narrow widths and zoom.

### Review and open design questions

| Check or decision | Accountable role | Status |
| --- | --- | --- |
| Record read or edit access for each assigned contributor and reconcile the D08 variant IDs on the shared canvas. | Product UI and canvas owner | Pending individual confirmations and shared variant lookup. |
| Confirm canonical typography, token export and distribution decisions in the asset register above. | Product UI and asset owner | Pending approval. |
| Approve fidelity of the representative fixture and coverage of the shared patterns. | Product UI | Pending sign-off. |
| Record screen-reader speech evidence and approve the interactive fixture on the reviewed revision. | Independent accessibility reviewer | Pending assignment and sign-off. |

The [Phase 0 staffing register](../PHASE_0_QUALIFICATION_REGISTER.md#1-day-1-ownership-staffing-and-review-coverage) records the Product UI and independent review assignments. Attach the reviewer results and exact revision to [issue #8](https://github.com/alisameh05/RAFIQ/issues/8).
