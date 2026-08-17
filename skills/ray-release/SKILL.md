---
name: ray-release
description: Prepare, build, sign, upload, submit, release, and monitor App Store or Google Play releases. Use for production readiness checks, store builds, App Review materials, version creation, review submission, phased or production rollout, release-status monitoring, and release troubleshooting.
---

# Release

Own the release from readiness through public availability while preserving existing
store configuration and keeping each external mutation within the user's request.

## Route the request

- Read [references/launch-checklist.md](references/launch-checklist.md) for production
  readiness reviews and public-launch preparation.
- Read [references/production-build.md](references/production-build.md) when creating,
  signing, validating, or uploading a store build.
- Read [references/app-review.md](references/app-review.md) and
  [references/review-package.md](references/review-package.md) when preparing App
  Review notes, reviewer access, evidence, or a physical-device demo plan.
- Use the installed `asc-*` skills for App Store Connect operations and `gplay-*`
  skills for Google Play operations. This skill owns Ray's release policy; platform
  skills provide current commands and API workflows.

Read every selected reference completely before acting.

## Workflow

1. Read repository instructions and release-related source-of-truth documents.
2. Inspect the working tree, shipping target, store app, current version, existing
   release settings, build history, metadata state, and authentication.
3. State the requested boundary: prepare, build, upload, stage, submit, release, or
   monitor. Do not expand one boundary into another.
4. Run the relevant readiness checks and tests. Resolve blocking failures before an
   irreversible store action.
5. Build and upload when requested, then wait for store processing and verify the
   resulting build state.
6. Preserve existing store settings, attach the intended build and metadata, validate
   the prepared version, and summarize any non-blocking warnings.
7. Submit, start rollout, or release only when the user explicitly requests that
   action. Monitor until the requested terminal state is reached.
8. Report repository commits, store resource IDs, version/build, release setting,
   processing state, submission state, and remaining user actions.

## Store-setting integrity

- Treat store settings as user-owned state, not command defaults.
- Before creating an App Store version, read the release type from the current or
  latest version and reuse it.
- Preserve rollout mode, phased release, territory availability, pricing, and other
  existing release controls unless the user requests a change.
- Never pass `MANUAL`, `AFTER_APPROVAL`, or an equivalent rollout value merely as a
  conservative default when an existing value is available.
- If an existing value cannot be determined, ask the user before creating or updating
  the version.
- State any proposed setting change and get explicit approval before applying it.
- Upload approval does not authorize review submission. Review-submission approval
  does not authorize changing post-approval release behavior.

## Verification

- Confirm the uploaded build is valid through the store, not only the local command.
- Confirm the prepared version references the intended build and retains the expected
  release settings.
- Run the platform submission-readiness validator before review submission.
- After submission or rollout, query the store again and report the observed state.
- Do not claim physical-device testing, reviewer access, approval, or public
  availability without direct evidence.

## Bundled scripts

- Run `scripts/sync_skadnetwork_ids.py` for launch-time AdMob SKAdNetwork syncing.
- Run `scripts/format_info_plist.py` when deterministic plist formatting is required.
- Execute scripts in place and pass project-local paths; do not copy them into apps.
