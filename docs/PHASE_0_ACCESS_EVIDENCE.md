# Phase 0 validation access evidence

This handoff records the checks completed for [issue #3](https://github.com/alisameh05/RAFIQ/issues/3) and the evidence Release must review before closure. Follow the [zero-cost hosting runbook](PHASE_0_HOSTING.md) for setup and recovery. Keep provider identifiers, secret-store references and credentials in the private operations handoff.

## Verified provisioning

| Area | Result |
| --- | --- |
| Web and API hosting | Vercel Hobby and the approved cardless Render Hobby workspace were accessible. Vercel was set to Node.js 24.x and checked with a separate project read. Use one Render Free web service and an attended local worker. |
| Worker host | Docker Desktop was started on the Windows test computer. Its Linux/amd64 engine answered. |
| PostgreSQL | The isolated Supabase Free database was accessible through the CLI. Separate migration, API and worker roles each passed temporary TLS 1.3 logins from Windows through the free session pooler with hostname and CA verification. The temporary passwords were cleared and login was disabled again. |
| Clerk | Two synthetic users were created and verified in the development instance. The instance uses email-code sign-in. |
| Private objects | Authorized CLI access downloaded the synthetic fixture with a matching SHA-256. Anonymous reads returned no file. The bucket is private and Storage RLS is enabled. |
| Shared vault | The requester reported a successful read of the dummy note from the invited member's own account. |

## Release verification before closure

- [ ] Record the accountable operator, independent reviewer and deployment owner. Confirm those people have the access required for their duties.
- [ ] Link the reviewed candidate and record the exact browser and API HTTPS origins, approved Clerk redirects, and the worker host and operator. Confirm the approved validation configuration can be handed to the deployment owner.
- [ ] Verify the reviewed database grants and role access from the actual migration, API and worker hosts. Confirm runtime credentials and object access are scoped to the isolated validation environment.
- [ ] Record the signed test callback registration and signing-secret custodian. Keep the secret in the approved operations store.
- [ ] Record resource limits, cost exposure, exhaustion behavior and fallback. Assign an owner and escalation date to any remaining prerequisite.
- [ ] Link the privacy-safe access attestation from the designated release operator before merging this PR.

The deployed browser-to-R smoke and callback behavior checks are tracked in [issue #11](https://github.com/alisameh05/RAFIQ/issues/11). Production qualification, account-level limits and the Day 2 escalation are recorded in the [qualification register](PHASE_0_QUALIFICATION_REGISTER.md) and [Day 2 escalation record](PHASE_0_DAY_2_ESCALATION.md).
