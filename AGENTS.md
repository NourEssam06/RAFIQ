# RAFIQ repository instructions

<!-- Verified 2026-11-25 against repository revision 1407624. -->

RAFIQ is a desktop-browser driver-monitoring application for controlled sessions and approved supervised vehicle testing. It issues local warnings and gives drivers private access to session evidence, clips, analysis and reports. The planned stack is Next.js and TypeScript on Vercel, a FastAPI modular monolith with a Python worker and R, Supabase PostgreSQL, and Clerk identity. This baseline contains planning and design artifacts. Check the selected branch for an executable scaffold before choosing build or test commands.

## Start a task

1. Run `git status --short --branch`. Identify the applicable phase, requirement and acceptance IDs, journey, screen IDs and dependencies. Keep existing work outside the task intact.
2. Read the sources for the work below. Resolve conflicting behavior or open contract decisions before implementing the affected boundary. Record approved changes in the owning document and update its linked acceptance criteria.
3. For phase planning, start with the [implementation guide](docs/IMPLEMENTATION_GUIDE.md). Use [`to-spec`](.agents/skills/to-spec/SKILL.md) for one phase and [`to-tickets`](.agents/skills/to-tickets/SKILL.md) for verifiable end-to-end slices. Carry forward blocking edges and human-owned approvals. Confirm the tracker and labels before publishing.

## Where to look

| Task | Read |
| --- | --- |
| Product behavior, actors, terminology or scope | [PRODUCT](docs/PRODUCT.md) and [approved PRD](docs/PRD.md). The PRD governs requirements, acceptance and rollout. |
| Phase sequencing, screen ownership or release dependencies | [Implementation guide](docs/IMPLEMENTATION_GUIDE.md), including the [Pen index](docs/IMPLEMENTATION_GUIDE.md#4-pen-design-and-screen-ownership) and [evidence matrix](docs/IMPLEMENTATION_GUIDE.md#5-traceability-and-release-evidence). |
| Runtime, module ownership, database or provider integration | [TRD](docs/TRD.md) for engineering requirements and pinned baselines, and [architecture](docs/ARCHITECTURE.md) for responsibilities and trust boundaries. |
| HTTP, events, jobs, binary transfer or MCP | [API](docs/API.md) for proposed wire contracts and [open decisions](docs/API.md#18-open-questions-and-decisions-requiring-approval). Confirm unresolved contracts with the owning contributor. |
| Camera models or benchmark | [Vision reuse](docs/VISION-REUSE.md), [browser vision contract](docs/TRD.md#21-pretrained-browser-vision), and [benchmark protocol](docs/PRD.md#83-benchmark-and-behavior-policy). |
| Screens, interactions, copy or accessibility | [EXPERIENCE](docs/EXPERIENCE.md), [SCREENS](docs/SCREENS.md), [DESIGN](docs/DESIGN.md), and the approved [screen briefs](docs/design/screens/). |
| Visual implementation from Pen | Use the [shared RAFIQ canvas](https://app.pen.dev/s/fZ1Fr2k_GIRpAwvABYPvw8LcwmOajmza6vjtx0ivitU) as the primary visual reference. Use [RAFIQ.pen](<Pen Design/RAFIQ.pen>) and [local design assets](<Pen Design/>) for supplemental frames, tokens and prototypes. Read or edit `.pen` through the Pen integration. Use the approved shape brief for behavior when research or review files show alternatives. |
| Docker, CI, deployment, rollback or recovery | [Docker guide](docs/DOCKER.md), [Git workflow](docs/GIT_WORKFLOW.md), and [TRD release gates](docs/TRD.md#8-measurable-acceptance-and-release-gates). Verify actual environments, workflow files and exact candidate revisions. |

## Product and implementation boundaries

- Qualify monitoring on Windows 11 and the supported Chrome versions with a built-in front-facing camera. Set up and operate driver controls while stationary. For motion, use the approved supervised procedure, passive driver presentation and only the explicitly delegated controls. Test staged unsafe behavior while stationary or in a simulator. [Operating conditions](docs/PRD.md#82-device-and-supervisor-qualification)
- Keep live camera frames, inference, warning timing and unused pre-event footage on-device. Allow only consented, bounded video-only clips through the private media path. Observation loss overrides stale warnings and clears emergency qualification. Resume manually after observation is usable again. [Session and offline contracts](docs/TRD.md#2-session-recording-and-offline-contracts)
- Keep configured-session warnings working during the supported offline window. Isolate encrypted queued data by driver and device. Use stable event IDs, durable per-item outcomes and idempotent retries. Require the same eligible driver for recovery. Recheck consent, expiry and ownership at upload finalization, playback, export and retry. Restore deletion, suspension and revocation state before reopening reads. [Data lifecycle](docs/PRD.md#86-clip-and-report-lifecycle)
- Derive resource ownership and operation authority on the server. Scope browser, worker, callback, staff, chat and MCP access separately. Staff receive aggregate signals and the approved account fields. MCP read and report-authoring grants are independent, and only authorized MCP authoring starts or submits a report. Apply the approved driving-data allowlist to external contexts. [Authorization](docs/ARCHITECTURE.md#11-authentication-authorization-and-security) · [MCP data boundaries](docs/PRD.md#88-mcp-qualification-and-data-boundaries)
- Require fresh authenticated confirmation from the active monitoring tab for every emergency delivery attempt, including fallback. Recheck live eligibility, cancellation and expiry at dispatch. Treat provider acceptance and confirmed delivery as separate outcomes. Use synthetic events or approved test recipients for verification. [Emergency protocol](docs/TRD.md#6-external-protocols)
- Use versioned, eligible inputs and R for published statistics. Honor inference and disclosure limits, preserve original observations during What-If replay, and derive report review and both export formats from the same validated snapshot. [Statistics and reports](docs/TRD.md#5-statistical-analysis-and-reports)
- Use synthetic or sanitized fixtures in Git, PRs and CI. Keep credentials, live camera data, private driving records, contacts and precise coordinates in their approved environments. Ali Sameh approves the exact public release candidate. The campus demo and production rollout each need their own evidence. Keep social sign-in, email, WhatsApp and optional chat behind their independent qualification gates and verify hosting and provider costs against the zero-project-cost baseline. [Release policy](docs/PRD.md#8-planning-decisions-and-release-gates)

## Verify changes

- For docs and Pen changes, check local links and anchors, requirement and screen references, prototype asset paths and whitespace. Use `git diff --check` for tracked changes and `git diff --cached --check` for staged changes. Check new files explicitly. For an edited standalone JavaScript prototype, use `node --check` and exercise the relevant preview interaction when behavior changes. Static checks and Pen frames are design evidence. Browser behavior and external integrations require their own checks.
- For application changes, use the actual manifests, lockfiles and CI jobs on the branch. Trace the highest relevant seam from the browser, API, provider, or remote client through durable state and back to an observable result. Exercise permission denied, expired or revoked access, interruption, retries and recovery wherever they affect the slice. [API verification matrix](docs/API.md#15-api-testing-and-contract-validation)
- For release work, record the exact build, environment, workload, device, fixture or dataset as applicable, expected result, observed result and gate status. Report which checks ran and which evidence is pending. Compare against the approved [TRD acceptance targets](docs/TRD.md#8-measurable-acceptance-and-release-gates).

## Git and GitHub

- Use short-lived task branches and reviewed PRs into `master`. Follow the branch naming, Conventional Commits, review and squash guidance in the [Git workflow](docs/GIT_WORKFLOW.md). Verify current merge requirements. Use the `RAFIQ CI gate` when configured and record the exact checks that ran.
- Inspect the staged diff before committing. Stage the requested changes and their required assets. Keep local configuration and logs out of the PR unless the task specifically requires them. Obtain explicit authorization for commits, pushes, PRs, merges and deployments under the repository handbook.

### Local GitHub CLI access on Windows

The offline sandbox cannot read the signed-in GitHub CLI configuration or reach GitHub. From the first attempt, run `gh` through `exec_command` with `sandbox_permissions: "require_escalated"`. Use one direct `gh` command per call so command rules can match it. Common reads use the existing command rules. GitHub writes go through normal approval review. Use the existing signed-in configuration and keep credentials out of the workspace and tool output. Treat a sandboxed `Access is denied` as an execution-context error and retry with elevated access using the same authentication. Diagnose and report the actual error if the escalated command fails.
