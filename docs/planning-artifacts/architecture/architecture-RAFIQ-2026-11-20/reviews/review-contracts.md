# Component contract review

**Verdict at review.** The provider, stack and ownership choices match both MCQ rounds. Four interactions need tighter contracts to preserve the approved guarantees.

| Decision | How compliant components could disagree | Acceptance contract |
|---|---|---|
| AD-3, offline acknowledgement | A browser drops an item on receipt of a batch response while ingestion still has an uncommitted transaction. A conflicting replay might silently change history. | Acknowledge each committed item separately. Treat an identical replay as success. Reject conflicting reuse of a stable ID. Keep retryable items queued and stop retrying deleted or expired items. |
| AD-5 and AD-6, worker completion | A job lease expires mid-render. Both workers finish and an old worker publishes after deletion or grant revocation. | Only the current lease holder may publish, once per logical job. Recheck source validity, ownership and any initiating grant at release. Verify interruption, reclaim and stale completion. |
| AD-7, live email | The browser cancels while disconnected. The server still sees a recent qualifying observation, and could send after cancellation. | Require contemporaneous online eligibility for each attempt. If the server cannot establish it, suppress the send. An offline sync item cannot authorize a live email. Exercise loss of connectivity immediately before each attempted send. |
| AD-8, hosted recovery | A change log stored only with the failed primary can satisfy normal operation but cannot restore acknowledged writes. A stale restore can bring back a deleted clip reference. | Keep recovery evidence independently recoverable within the five-minute objective. Reconcile deletion, expiry and revocation before enabling reads. Test restoration with acknowledged writes and concurrent withdrawals. |

These checks refine existing user-approved behavior. Provider qualification, selected model weights, capacity measurements and university hosting still require evidence.
