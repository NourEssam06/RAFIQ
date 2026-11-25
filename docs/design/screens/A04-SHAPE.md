# A04 Service Health

**Mode** · Operate. **Design direction** · Status first, using static RAFIQ components **A04-C01**, **A04-C05**, and **A04-C08**. The Pen.dev implementation request delegated component selection. Use UTC for the design fixtures. [Layout and component research](A04-COMPONENT-RESEARCH.md)

An Owner or Staff member with **View metrics** enters after verified admin sign-in and MFA, selects **Service Health** in the admin shell, or follows an authorized link. Put current service evidence before the selected period’s trends. Provide an entry to **Release Readiness** within Service Health. Returning from A05 restores the selected range, scroll position and focus to that entry. Other destinations depend on the current admin grant. A04 shows aggregate operational evidence and supports read recovery. [A04 requirements](../../SCREENS.md#a04-service-health) · [A05 handoff](A05-SHAPE.md) · [Admin access and telemetry](../../TRD.md#71-admin-dashboard-fr-22)

## Frame and components

| Region | Design and behavior |
| --- | --- |
| Admin shell and range | Keep **Service Health** current. Place the **Release Readiness** link near the heading. Show the server **Query cutoff**, display zone, and four range options in order: **Last 1 hour**, **Last 24 hours** (default), **Last 7 days**, **Last 30 days**. Use one labeled, single-select control. Keep the chosen range distinct from the range of any last-loaded results shown during a pending or failed read. |
| Key service cards | Lead with frontend, API and worker health where provided. Use the existing Review metric card and status row treatments. Give each card a status in text, a supporting icon, its sample time if known, and the reason when applicable. Keep the current health evidence distinct from the aggregates across the selected range. |
| Availability and performance | Show **Uptime (%)**, **API error rate (%)**, and **API p95 latency (ms)** on aligned time axes with their own y-scales. Uptime uses successful scheduled checks divided by observed checks. Error rate uses failed server requests divided by eligible requests. Show numerator and denominator when supplied and label p95 with eligible sample size. Use the supplied p95 for the represented window or bucket. A gap represents an unreported observation. Keep valid observations, including measured zero, on the applicable scale. Provide a **View data** disclosure with exact values, timestamps, units, counts and availability. |
| Queues and storage | Show session sync and report queue depth and oldest pending job age, upload or worker health where available, and storage usage alongside quota in matching units. Label each point-in-time reading with its observation time. A known empty queue can show **No pending jobs** for oldest age when supported by the same queue observation. |
| Backup and deletion | Show last successful backup time, backup lag, deletion and purge progress, and overdue purge counts where available. The backup time and telemetry sample time are separate. An observed zero overdue purges describes only that measure. |
| Emergency delivery | Use separate **Email** and **WhatsApp** rows. Show **Pending**, **Accepted**, **Delivered**, **Failed**, and **Unconfirmed**. Count distinct attempts created in the selected window, classified by their recorded status at the query cutoff. Provider acceptance and delivery have their own columns. Keep qualification, telemetry evidence and runtime health readable independently. Display **Awaiting qualification** for an unqualified channel, leave its counts unreported and provide the approved route to A05 evidence. |

Use `colors.canvas`, `colors.ink`, `colors.accent-stone`, the established RAFIQ application type treatment, `rounded.md`, and the `spacing.sm` / `spacing.md` / `spacing.xl` steps of 8, 16 and 24 px. Apply accents to meaningful status, selection and chart marks. Keep work surfaces flat, align numeric columns and support status with label and icon. Reuse D09’s metric card and exact-value readout treatment, D06’s table hierarchy and horizontal/stacked status treatments, and the existing admin shell. Use a 1440 px desktop reference, 1024 px compact desktop, and a single-column 320 CSS px reflow reference. At compact widths, wrap the toolbar, reduce the card column count and stack charts in reading order. Use labeled stacks or localized table scrolling for wide operational rows. [RAFIQ design tokens](../../DESIGN.md) · [Shared screen design rules](../../SCREENS.md#shared-design-rules)

## Evidence and recovery

| State | Visible result |
| --- | --- |
| Healthy or degraded | Use **Healthy** or **Degraded** from approved, fresh evidence. The exact value and sample time remain visible, with a supplied threshold or reason where helpful. |
| Fresh confirmed outage | Show **Unavailable · Outage confirmed**, with its observation time. An availability reading of 0% requires observed checks. |
| Stale telemetry | Show **Unknown · Stale telemetry**, with the last sample time. Any retained reading is explicitly last known. Valid historic observations remain in range, and the unobserved intervals remain gaps. |
| Missing or insufficient evidence | Show **Unknown · No sample** or **Unknown · Insufficient data** with an unreported reading. Zero observed checks or eligible requests leaves its ratio undefined, and zero eligible requests leaves p95 undefined. |
| Confirmed zero | Render **0** with unit and scope for a complete, fresh observation, including zero jobs, zero failed requests with an eligible population, or zero emergency attempts with qualifying coverage. Show service health from its own evidence. |
| First load or range change | Show static loading treatment and preserve the toolbar and focus. Keep any still-visible prior data labeled with its applied range and cutoff. Publish the new range and cutoff with the corresponding snapshot. Ignore late responses to superseded range selections. |
| Scoped read failure | Show a section-specific message and local **Retry**. Keep valid sections, selected range and evidence timestamps readable. A retry that re-reads the whole range publishes the actual cutoff and labels any cases where retained evidence comes from an earlier snapshot. |
| Empty response or whole-page read failure | Explain when there are no samples in a successful range. A failed first load shows **Couldn’t load Service Health** and **Retry**. A dashboard read failure carries no assertion about service health. |
| Access lost | Clear affected readings, details and retained snapshots immediately when sign-out, expiry or revocation invalidates access. Follow current admin routing and disregard responses that arrive after the clear. |

## Interaction, accessibility and acceptance

- Use landmarks, a skip link, a clear heading order, visible focus and native links, buttons, and range inputs. Announce a meaningful status, range result, or retry result once. Keep focus on the control through reads and ordinary failures.
- Provide one keyboard entry to each interactive chart, arrow-key bucket selection and an equivalent table access point. The exact readout identifies its time span, value, unit, relevant counts and data availability. Pointer, keyboard and touch expose equivalent evidence. Use true data gaps and readable zero marks. Keep the same evidence in the visual and tabular forms.
- Use native table captions and scoped headers. Keep row positions stable. Verify all five emergency counts and their column labels survive narrow reflow. At 200% zoom and the 320 CSS px equivalent, preserve the reading order, access to range controls and A05, and visible focus without page-wide horizontal scroll.
- **Static treatment.** Range selection, badges, charts, exact readouts, disclosures and error feedback go straight to their next visual state. Skeletons stay still. Reduced motion uses the same states. Pen.dev can depict their endpoints. Requests, focus movement, announcements, authorization and telemetry decisions require frontend verification.

## Telemetry dependencies

The frames are synthetic fixtures. The runtime needs approved per-signal thresholds, stale deadlines and bucket semantics, plus a way to distinguish missing evidence from stale telemetry. Confirm the numerator mappings, the report queue oldest-age source, deletion and purge progress, and partial-source read/retry semantics. The proposed delivery schema carries qualification and counts or null. It still needs per-channel sample timing, coverage and independent runtime health to support the depicted freshness and confirmed-zero states. The display zone and refresh cadence are frontend contract decisions. [Health endpoint](../../API.md#7-detailed-endpoint--operation-specifications) · [Admin freshness gap](../../API.md#18-open-questions-and-decisions-requiring-approval)

## Pen.dev frames

The editable frames are in [RAFIQ.pen](<../../../Pen Design/RAFIQ.pen>).

| Frame | Pen node |
| --- | --- |
| Service Health · 1440 px | `KDEbz` |
| Service Health · 1024 px | `C8bdIS` |
| Service Health · 320 px | `tIdOh` |
| First load | `sloSo` |
| No samples | `SaleI` |
| Partial source failure | `eBWz1` |
| Read failed | `In5Ic` |
| Metrics access revoked | `G7bxG` |
| Range change in progress | `XLD4w` |
| Inspect API error rate | `joGA3` |
