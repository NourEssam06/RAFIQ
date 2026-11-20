# Provider fit review

Reviewed on 20 November 2026. The selected providers are credible qualification candidates. No account settings, deployment, pricing acceptance, or restore drill was tested.

| Decision | Finding and handoff |
|---|---|
| Vercel | Confirm Hobby eligibility for the team’s noncommercial course deployment and recheck before public signup. Hobby caps included usage. Keep the selected host conditional on the strict zero-spend rule. [Pricing](https://vercel.com/pricing) |
| Render | Free web services sleep after 15 idle minutes. Without a payment method, exceeding included outbound usage can suspend service. A standalone background worker has no free instance offering. Evaluate the R worker during an attended demo and record its arrangement and interruption behavior. [Free hosting limits](https://render.com/docs/free) |
| Supabase PostgreSQL | The Free plan lists a 500 MB database allowance. Document independent encrypted recovery and log replay. Validate volume, replay lag, restore time and deletion handling at pilot load. [Pricing](https://supabase.com/pricing) · [Backups](https://supabase.com/docs/guides/platform/backups) |
| Neon | Free includes 5 GB of object storage and requires no card. A private Neon bucket supports the architecture. Verify transfer, ranged reads, expiry, branch copies and retention with the selected configuration. Twelve drivers at 250 MB each represent 3 GB before overhead. [Pricing](https://neon.com/pricing) · [Object storage behavior](https://neon.com/blog/building-neon-object-storage) |
| Clerk | Clerk documents passwords, email verification, custom OAuth scopes, PKCE and configurable opaque tokens for immediate revocation. Confirm current free-plan entitlement, the preregistered public client's exact callback, per-request verification, consent and loss of authorization during report generation in the named Codex CLI integration. [Pricing](https://clerk.com/pricing) · [OAuth](https://clerk.com/docs/guides/configure/auth-strategies/oauth/how-clerk-implements-oauth) |

Exact builds, model and license fit, quotas, service availability, and supported throughput remain release evidence. The spine defers those results as the user requested.
