---
name: ray-store-screenshots
description: Plan and capture localized App Store screenshots with fastlane snapshot, covering core-value screen selection, two-line English caption copywriting, user confirmation, marketing transcreation into every supported locale, deterministic XCUITest capture, and versioned raw screenshot output. Use when the user asks to create, refresh, automate, localize, or caption store screenshots, App Store or Play Store listing images, or screenshot capture pipelines.
---

# Store Screenshots

Produce raw store screenshots and the localized caption copy that goes on top of them. Capture iOS only, even when the product also ships on Android; the iOS assets are the single source for every store.

Scope ends at raw screenshots plus confirmed captions. Compositing raw screenshots into final marketing images is handled by a separate tool and is out of this skill's scope.

## 1. Resolve the scope

Inspect before asking:

- the shipping app target, not deprecated or reference implementations in the same repository
- supported locales, from the app's own localization resources (`.lproj`, `.xcstrings`, `.arb`, catalogs), never from an assumed list
- existing screenshot directories, caption files, and fastlane configuration
- product specifications, design specifications, and market research already in the repository

State the resolved app, locales, devices, and output paths before doing any work. Ask the user only when inspection leaves the scope genuinely ambiguous.

Default devices: one 6.9-inch iPhone. Add a 13-inch iPad only when the app declares iPad support. Do not capture device sizes the store no longer requires.

## 2. Follow the repository's layout

If the repository already has a screenshot layout, follow it exactly. Otherwise create:

```text
design/screenshots/
├── captions/<locale>.json    # caption copy, one file per locale
├── raw/<locale>/<device>/    # fastlane snapshot output, committed
└── final/<locale>/<device>/  # composited marketing images, committed
```

Both `raw/` and `final/` are version-controlled. Never add them to `.gitignore`. Keep fastlane's working output outside the repository or move it into `raw/` after each run, so the committed tree holds exactly one copy.

Name files `NN_screen-name.png` with a fixed numeric order shared by every locale and device. The same index must always mean the same screen.

## 3. Select the screens

Choose exactly three screens, ranked by the product's core value rather than by feature count:

1. the single reason the product exists, shown in its most legible state
2. the capability that most clearly separates it from substitutes
3. the moment that proves the product works or pays off for the user

Ground the selection in the repository's product and market documents when they exist. Reject screens that need explanation, show empty states, or depend on text too small to read at store thumbnail size.

Record for each screen: index, screen name, what it must show on screen, and the app state required to reach it.

## 4. Write the English captions

English is the source locale for every caption. Write all three before showing anything to the user.

Rules:

- two lines per caption
- the first line starts with an action verb in the imperative
- three words total across both lines is the target, five is the hard maximum
- no terminal punctuation, no ellipses, no marketing exclamation
- each caption states a user outcome, not a feature name
- the three captions do not repeat the same verb or the same noun
- avoid words that break badly when the layout gets narrow

Split the two lines where a person would naturally pause, not where the character count happens to be even.

Store captions as an ordered object keyed by screenshot index, with the two lines as an array:

```json
{
  "01": ["Tap it out", "in Morse"],
  "02": ["Hear every", "signal"],
  "03": ["Flash a", "message"]
}
```

## 5. Get confirmation before translating

Stop and present the three English captions to the user with the screen each belongs to. Do not translate, do not write locale files, and do not start the capture setup for other locales until the user approves the English copy.

Revise and re-present as many times as the user asks. Approval of the English set is the gate for the whole localized pipeline; once locales are generated, changing the English copy invalidates all of them.

## 6. Transcreate into every locale

Translate the intent, never the sentence. For each target locale, write the caption a native marketer in that market would write for the same screen.

- Keep the promise and the emotional register; discard the English word order.
- Lead with whatever carries the message first in that language. In Korean the core keyword or noun leads and the verb closes the phrase, because a verb-first line reads as an abrupt command. Apply the same reasoning per language rather than copying this example.
- The English rule "first line starts with a verb" is an English constraint. In other locales preserve the sense of action, not the part of speech.
- Match the market's marketing idiom: register, formality level, and sentence ending conventions.
- Reuse terminology already established in the app's own translations. The caption must use the same word for a feature as the UI does.
- Count length in what the script renders, not in English words. CJK captions should stay short in characters; German and Romance locales usually need a longer second line, so keep the first line tighter.
- Break the two lines at a phrase boundary valid in that language.

Write one file per locale under `captions/`, with identical keys and array shape across all locales.

## 7. Set up capture

Use `fastlane snapshot` driven by a dedicated UI test target. Keep the pipeline deterministic:

- Add or reuse a UI test target that only navigates and calls `snapshot(...)`. It must not assert product behavior.
- Install `SnapshotHelper.swift` into that target and call `setupSnapshot(app)` before `app.launch()`.
- Drive app state through launch arguments, not through tapping the real onboarding flow: skip onboarding, seed demo content, disable review prompts, freeze anything animated, and disable anything that needs a permission dialog.
- Choose demo content that is meaningful in every locale and does not require translation, or seed it from the caption file's locale.
- Address elements by accessibility identifier. Add identifiers to the app when they are missing; never match on localized text.
- Wait for a stable element before each capture, never on a fixed sleep.
- Configure `Snapfile` with the resolved devices, the locales from step 1, `clear_previous_screenshots`, and no HTML report.

Verify one locale end to end before running the full matrix.

## 8. Capture and verify

Run the full matrix, then move or copy the output into `design/screenshots/raw/<locale>/<device>/`.

Check every locale before reporting done:

- one file per screen per locale per device, with matching indices
- the same screen appears under the same index everywhere
- localized UI actually rendered in the target language, with no untranslated or truncated strings
- no permission dialogs, debug overlays, placeholder content, or mid-animation frames
- status bar is clean and consistent across the set

Re-capture failures rather than editing pixels. Fix truncated UI in the app or in the seeded content, not in the screenshot.

## 9. Report

Report the selected screens and why each earned its slot, the approved English captions, the locales translated with any wording that deserves a native check, the devices and locales captured, the output paths, and anything the compositing step needs to know, such as safe areas or captions that ran long in a specific locale.
