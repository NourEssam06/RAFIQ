# D08 Incident and alert details — Pen.dev handoff

The driver opens D08 to understand what RAFIQ observed at one point in a completed session, what warning or emergency action followed, and whether there is a clip. The approved layout places D08 directly below D07’s full-width timeline and before the ordered event list. Keep key evidence visible and provide separate disclosures for supporting measurements and detailed delivery updates. Use RAFIQ’s existing visual treatments, standard disclosures, and a subtle selection accent. [D08 requirements](../../SCREENS.md#d08-incident-and-alert-details) · [D07 handoff](D07-SHAPE.md) · [Design and component research](D08-COMPONENT-RESEARCH.md)

## Composition and evidence

1. **Timeline and selection.** Keep the timeline’s range controls, behavior lanes and event markers above the panel. Give the same occurrence a selected marker and selected ordered-list row. Keep the timestamp legible in both views and repeat it in D08’s heading area. Use the distinct occurrence type and source ID to resolve events that share a timestamp. **Read selected details** moves focus to the panel heading on request.
2. **Panel heading.** Show the occurrence type, label, exact elapsed timestamp and, where useful, local time and time zone. Provide **Back to selected time** and **Close details**. Build this as a named section in page flow. Keep essential content readable at normal laptop widths, 200% browser zoom and 320 CSS px reflow. At narrow widths wrap actions, stack data and retain one page scroll. Allow horizontal scrolling inside the labeled plot region when necessary.
3. **Incident.** Show start, end and duration, each recorded behavior and detection span, actual overlap and duration, and detector confidence per detection. A shared endpoint contributes zero overlap. Show associated warning severity when recorded. Under **Supporting measurements**, group cue labels, values and units by detection. Preserve the original record during playback, partial data or disagreement.
4. **Warning.** Show issue time, constituent behaviors, recorded severity, and the cue or qualifying duration when supplied. Label acknowledgment time separately. If the related incident resolves, display its original evidence while keeping the warning selected.
5. **Emergency Mode.** Show the selected sequence occurrence and recorded milestones as an ordered list. Group latest attempt outcomes by historical contact order and label Email or WhatsApp, state, and latest recorded update. **Pending** means the attempt is in progress. **Accepted** means the provider took the alert for processing. **Delivered** requires confirmation. **Failed** is terminal. **Unconfirmed** means an attempted channel remained unresolved at the deadline. **Withheld** identifies an unsent attempt, with a reason where supplied. **Canceled** describes the sequence. Provide **Delivery updates** for authorized recorded history. Report a late callback in its original row without changing the selected occurrence. Show location only while authorized and eligible. An emergency occurrence needs an explicit relationship before it can show incident or clip evidence.
6. **Clip.** Show availability and recorded expiry, with **Open clip** only for currently playable media. If a clip is pending, expired, deleted or unavailable, show the authorized reason where known. Use a neutral fallback when the reason is absent. Leave incident evidence available independently. D11 opens on request. Preserve the authorized D07 range, exact occurrence, scroll and focus context for Back.

## Components and motion

Reuse D01’s timeline mark and event-row treatment and D06’s Sessions shell. Use titled sections, flat dividers, labeled action buttons, severity text plus a symbol, ordered milestones, and accessible disclosure buttons. The RAFIQ-specific elements are the occurrence header, detection and overlap readout, and grouped attempt records. Use Space Grotesk as the existing Mori substitute, warm ink on dark canvas, `spacing.sm` (8 px) within groups, `spacing.md` (16 px) for panel padding, `spacing.xl` (24 px) between sections and `rounded.md` (8 px) for the panel. [Design tokens](../../DESIGN.md) · [ARIA disclosure](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)

| Trigger | Presentation |
| --- | --- |
| Select a marker or row | Commit the selected marker, row, time and evidence state together. Keep focus on the trigger. An accent can fade in over 150–180 ms while its final position and the focus ring remain fixed. |
| Expand technical details | Update the disclosure control and reveal the content in place. Keep focus on the trigger. |
| Close or return | Restore the contextual focus target. On Back from D11 use **Open clip** if eligible, otherwise the clip heading or updated status. When a range move excludes the selection, keep the selected time visible and jump back on request. |
| Reduced motion | Render the same final states immediately. |

The selection treatment draws from the [Motion accent pattern](https://motion.dev/docs/react-motion-component). Native disclosure and the ordered milestone list fit this panel. Pen depicts editable visual states. The browser implementation owns the accent, disclosure activation, timeline interaction, focus restoration, access checks, and assistive announcements. [Component alternatives and licenses](D08-COMPONENT-RESEARCH.md#component-research)

## Pen.dev frames

The frames in [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>) use D07 timeline-section views and synthetic evidence. The delivery example uses a separate session from the canceled alert. The narrow examples show the incident after its clip expired.

| Frame ID | State |
| --- | --- |
| `S3YUmp` | 1280 px incident, available clip and collapsed supporting measurements |
| `O7FNIf` | 1280 px issued warning, related detection evidence and available clip |
| `p7Nrf` | 1280 px emergency countdown canceled before sending |
| `GdiNk` | 1280 px emergency delivery history expanded, with separate WhatsApp and Email outcomes |
| `nKOpH` | 390 px incident with expanded measurements, expired clip and visible action focus |
| `o4SSzo` | 320 px incident with expired clip and compact timeline controls |
| `KPjNE` | Selection accent endpoints, reduced-motion state and scoped loading, retry and missing-evidence examples |

## States and verification

- During loading, keep the authorized occurrence label and time visible. For temporary failures, offer a scoped retry. Keep partial evidence readable and distinguish confirmed absence from unknown availability. Clear affected private evidence on access loss. Announce material updates once and preserve focus, with a stable fallback when an action expires.
- Verify keyboard and pointer equivalence for same-time markers and ordered rows. Switch during loading, open and close disclosures, pan away and return, and test D11 Back after clip expiry. Check focus, exact-value text, non-color severity and selection cues, 200% zoom, 320 CSS px and reduced motion.
- Verify that overlapping detections retain their own bounds and scores. Test a canceled alert before sending and a separate accepted-to-delivered sample. Check that a late outcome leaves the sequence closed and the selection unchanged. Use only synthetic evidence in Pen.

The documented emergency endpoint supports the latest state per attempt. Full delivery history, withholding reasons, and an eligible location need authorized data contracts. Confirm stable emergency occurrence identity and any links to an incident or clip. Use warning-time cues and historical media reasons only when the service supplies them. [Contract checks](D08-COMPONENT-RESEARCH.md#contract-checks-before-implementation)
