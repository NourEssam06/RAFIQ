# RAFIQ privacy requirements review

**Verdict.** The draft establishes private driver accounts, consented video-only clips, scoped assistant access, and a gated experiment workflow. The findings below identify release acceptance gaps. Each can fit within the existing requirements or approval points.

## High priority

### 1. Confirm which camera inputs can be retained or transferred

FR-04 has a consent check and FR-12 protects saved clips. AC-12 verifies the saved output, leaving transient context, continuous input, and microphone use outside the test. Verify that a driver can monitor with recording declined, and define whether camera context can be held before a qualifying event, when it is discarded, and what happens to in-progress capture when consent ends. State which camera data, if any, may leave the device other than the bounded opted-in incident clip. Verify camera and audio boundaries in the capture workflow. Define handling of an additional person in view for any supervised use that permits recording.

### 2. Make queue isolation and the deletion lifecycle observable

FR-08, FR-12, FR-13, and NFR-05 cover ownership, expiry, retried sync, and protected retrieval. Expand the acceptance cases to cover sign-out and account changes on the same browser while data is pending, then reconnect, and exercise deletion, expiry, and consent changes during a retry. OQ-6 covers pending clips and derived copies in general. Enumerate the affected artifact classes, including hosted clips, queued records and clips, reports, and any service-held derivatives, with approved deadlines for blocking access and completing deletion or expiry. Identify what remains independently eligible for retention, including session metadata after clip-only deletion.

### 3. Define and test the report and assistant data boundary

FR-19 and FR-20 ensure authorization to use resources, reject clip requests, and leave detailed approval to OQ-9. OQ-9 should identify the fields and recipients approved for data transfer to a report-generation service or compatible assistant, including access to incident references and output after generation. Verify the handling of access revoked or underlying data deleted while a report is pending. Clarify which copies remain under RAFIQ control, what persists in a downloaded document, and how retrieval of protected references behaves after revocation, deletion, or expiry. Test that any scope approved for an assistant also applies when it requests a report from inside its integration.

## Medium priority

### 4. Cover contact and location changes in the escalation lifecycle

FR-10 and OQ-5 cover verified recipients, permitted location, payload, and retry timing. Specify what information is sent to a contact, when a location is obtained, and whether contact addresses, message details, or locations are retained and visible after the attempt. Verify behavior when a stored contact is removed or replaced, or location permission changes, after scheduling but before retry. Include contact and notification history in the applicable deletion schedules.

### 5. Extend Experiment Studio safeguards through analysis and export

FR-17 and OQ-7 gate participant collection, study inputs, and cross-driver access. State whether participant-level or pooled observations can be included in derived results, reports, or exports. Apply the approved study permissions and lifecycle to those results. Test both direct access and indirect output before approving any participant collection or cross-driver dataset. The approved fixture path can be accepted independently of a participant collection path.
