---
name: ray-production-build
description: Create, sign, validate, upload, or troubleshoot production builds for App Store Connect or Google Play. Use for store archives and exports, new bundle IDs, provisioning failures, or production-build delivery.
---

# Production Build

## Scope

Build and upload the current app. Do not submit it for store review or start a production rollout unless the user explicitly asks.

Identify the active product and platform from repository documentation and source. Do not build an archived or abandoned implementation.

## Workflow

1. Inspect the working tree, app identifier, version, build number, signing configuration, and store authentication.
2. Run relevant tests and resolve a remote-safe build number before archiving.
3. Follow the platform workflow below.
4. Wait for store processing and verify the uploaded build is valid.
5. Report the version, build ID, processing state, artifact path, and any repository changes.

## iOS

Use `asc-xcode-build`, `asc-signing-setup`, and `asc-cli-usage`.

Treat these paired export errors as a missing or unusable App Store signing profile, not proof that the Apple Account is logged out:

```text
exportArchive No Accounts
exportArchive No profiles for '<bundle-id>' were found
```

Each new bundle ID needs its own `IOS_APP_STORE` provisioning profile. Reuse a valid Apple Distribution certificate and private key; do not create or revoke certificates unnecessarily.

### Prepare signing

1. Resolve the App Store Connect app ID and Apple bundle-resource ID.
2. Verify a matching Apple Distribution identity exists both remotely and in the local keychain.
3. Find an active `IOS_APP_STORE` profile linked to the exact bundle-resource ID and distribution certificate.
4. If none exists, create one:

```bash
asc profiles create \
  --name "<App Name> App Store <Year>" \
  --profile-type IOS_APP_STORE \
  --bundle "<BUNDLE_RESOURCE_ID>" \
  --certificate "<DISTRIBUTION_CERTIFICATE_ID>"
```

5. Install it locally:

```bash
asc profiles local install --id "<PROFILE_ID>"
```

### Archive and export

Archive the Release configuration for `generic/platform=iOS`. Export with manual signing so the command does not depend on Xcode's GUI account session or automatic profile creation.

Use an `ExportOptions.plist` equivalent to:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>destination</key>
  <string>export</string>
  <key>method</key>
  <string>app-store-connect</string>
  <key>provisioningProfiles</key>
  <dict>
    <key>BUNDLE_ID</key>
    <string>PROFILE_NAME</string>
  </dict>
  <key>signingCertificate</key>
  <string>Apple Distribution</string>
  <key>signingStyle</key>
  <string>manual</string>
  <key>teamID</key>
  <string>TEAM_ID</string>
  <key>uploadSymbols</key>
  <true/>
</dict>
</plist>
```

Run an upload dry run, upload with `--wait`, then verify `asc builds info --build-id "<BUILD_ID>"` reports `processingState: VALID`.

## Android

Use `gplay-release-flow`, `gplay-submission-checks`, and `gplay-cli-usage`. Build a signed AAB with the configured release keystore, run preflight and a production-track dry run, upload, and verify the resulting track state. Keep rollout or review submission outside scope unless explicitly requested.

Expand this section when a real Android production build establishes project-specific signing and upload requirements.

## Guardrails

- Never infer review submission from “build and upload.”
- Never replace or revoke existing signing assets without explicit authorization.
- Do not rely on `-allowProvisioningUpdates` as the only iOS distribution-signing strategy.
- Keep generated archives, profiles, export options, and IPA/AAB files out of version control.
