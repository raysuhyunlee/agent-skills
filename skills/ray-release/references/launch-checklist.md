# Production Launch Checklist

## Overview

Use this skill to keep a living production-release checklist for an app. Add checklist items only when the user provides them or explicitly asks for suggestions.

## Scripts

Run bundled scripts in place from this skill's `scripts/` directory. Do not copy them
into app repositories; pass `--project-root` or explicit project-local paths.

## Workflow

1. Confirm the app, release target, and deployment surface from the current context when available.
2. Present the checklist exactly as maintained below.
3. If the user asks to add, remove, rename, or mark an item, update this skill's checklist section when appropriate.
4. Do not invent checklist items unless the user explicitly asks for suggestions or asks you to expand the checklist.
5. When walking through the checklist, handle one item at a time and record decisions, evidence, or blockers only if the user asks you to preserve them.

## Checklist

- If AdMob ads are integrated, sync iOS `SKAdNetworkItems` before production release with `scripts/sync_skadnetwork_ids.py`. For Flutter apps, run it from the app root; it defaults to `<project-root>/ios/Runner/Info.plist` and `--source auto` detects AdMob mediation adapters from `pubspec.yaml`. When selecting manually, use `--source google` for plain AdMob or `--source mediation` for AdMob mediation. For native iOS, pass `--plist-path <Info.plist>`; for Expo/prebuild apps, also pass `--expo-config-path <app.config.ts|app.config.js|app.json>` so the config-plugin source of truth stays in sync. Use `--dry-run` first when checking a new project.
- If AdMob ads are integrated, verify the AdMob app ID is set correctly, ad unit IDs are loaded from Firebase Remote Config, and Firebase Remote Config realtime updates are enabled.
- If Firebase Analytics or Crashlytics are integrated, verify they are disabled in debug builds and enabled only for release/production builds.
- Use `scripts/format_info_plist.py --project-root <app-root>` when an iOS `Info.plist` needs deterministic sorted plistlib formatting.
- If the app supports only one language, set `CFBundleDevelopmentRegion` in the app's `Info.plist` to that locale, for example `ko-KR` for Korean.
- If the app is multilingual and has in-app purchases or subscriptions, verify IAP/subscription localizations are complete and natural for every supported locale. Use `asc-subscription-localization` or `gplay-iap-setup` for repeatable store-data operations.
- Check the app's U.S. export compliance/encryption setting, including `ITSAppUsesNonExemptEncryption` in the app's `Info.plist` when applicable.
- If Android is supported, verify the app's `android/key.properties` is configured to use `/Users/ray/Documents/upload-keystore.jks` as the release keystore.
- If Android is supported and the app is multilingual, enable Android per-app language settings by setting `androidResources { generateLocaleConfig = true }` in `android/app/build.gradle.kts` and adding `android/app/src/main/res/resources.properties` with `unqualifiedResLocale=<default-locale>`, for example `unqualifiedResLocale=en`; verify a build generates `_generated_res_locale_config.xml`.
- Verify the production app icon has been changed and PNG icon assets have been compressed with `pngquant`.
- For iOS, verify the icon pipeline uses a single 1024x1024 source image and resizes generated app icon assets at build time.
- For iOS, unless iPad is explicitly supported, disable iPad support and landscape orientations before first App Store release.
- For iOS, verify the app name and App Store metadata are naturally localized, `Info.plist` display names/localized names use `.xcstrings` where appropriate, and the home-screen app name is not too long when rendered under the icon.
- For iOS, verify the built app bundle exposes every supported language with `.lproj` folders, or `CFBundleLocalizations` when localized resources are not stored in `.lproj`; the App Store Languages section is inferred from the binary, not Flutter translation JSON or App Store Connect metadata.
- For iOS, verify the in-app review prompt appears at an appropriate moment, is not shown too frequently, and is not triggered too early, such as immediately on the first app launch.
- Verify the app settings screen includes working links to the terms of service and privacy policy.
- For iOS, use the `asc` CLI when useful to configure App Store Connect, and verify the marketing URL is set to `https://www.raysuhyunlee.com` and the support URL to `https://www.raysuhyunlee.com/apps/<app-slug>/feedback`.
- Set the App Store copyright field so it includes the current year. For a first release, use only the current year, for example `2026 Ray Lee.`. For an app update, preserve the original start year and add the current year when missing, for example change `2025 Ray Lee.` to `2025-2026 Ray Lee.`.
