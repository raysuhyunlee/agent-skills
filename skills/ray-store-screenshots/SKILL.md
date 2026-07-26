---
name: ray-store-screenshots
description: Plan, capture, design, and export localized App Store screenshots from an approved shared store-positioning brief, using deterministic fastlane snapshot capture and the pen.dev CLI for editable .pen compositions and final store-ready PNGs. Includes core-value screen selection, two-line caption confirmation, app-specific visual-direction options with a separate user approval gate, locale-aware design, and exact-dimension validation. Use when creating, refreshing, automating, localizing, captioning, composing, or exporting App Store or Play Store listing screenshots.
---

# Store Screenshots

Produce the complete screenshot set: approved copy, deterministic raw captures, an
editable Pen source, and exact-size final PNGs. Capture the shipping iOS app even when
the product also ships on Android; reuse those source captures for other stores when
appropriate.

Read [references/pen-composition.md](references/pen-composition.md) before proposing a
visual direction or operating the Pen CLI.

## 1. Resolve the scope

Inspect before asking:

- the shipping app target, excluding deprecated or reference implementations
- supported locales from `.lproj`, `.xcstrings`, `.arb`, or equivalent app resources
- existing raw and final screenshots, captions, `.pen` files, and capture configuration
- product, design, brand, icon, market, and positioning documents
- app theme colors, typography, icon palette, UI appearance, and meaningful visual motifs
- current store screenshot requirements for the resolved devices

State the app, locales, devices, appearance, and output paths before work. Ask only
when inspection leaves the scope genuinely ambiguous.

Default to one current large iPhone size accepted by the target store. Add a large iPad
only when the shipping app declares iPad support. Verify current requirements rather
than relying on remembered dimensions.

## 2. Require approved positioning

Verify that `design/store/positioning.md`, or the repository's equivalent:

- has `status: approved`
- matches the shipping product
- contains the three ordered primary, differentiating, and proof values
- defines supported evidence and claim boundaries

If it is missing or stale, use `$ray-store-positioning` first when available. Otherwise
follow that artifact contract, present the positioning for confirmation, and stop.
Never create screenshot-only positioning.

## 3. Follow the repository layout

Follow an existing layout. Otherwise use:

```text
design/screenshots/
├── captions/<locale>.json
├── raw/<locale>/<device>/
├── final/<locale>/<device>/
├── direction.md
└── store-screenshots.pen
```

Keep `raw/`, `final/`, `direction.md`, and the `.pen` source version-controlled. Keep
temporary Pen previews outside `final/`. Name final images `NN_screen-name.png`, with
the same index and meaning in every locale and device.

## 4. Select exactly three screens

Map the approved values in order:

1. primary value: the single reason to download
2. differentiating value: the strongest reason to choose this app
3. proof value: the visible moment showing the outcome was achieved

For each screen record the value, source screen, required app state, visual focal point,
and capture route. Prefer rich, legible states that communicate at thumbnail size.
Reject empty, loading, login, placeholder, debug, or explanation-dependent
screens.

Assess candidate captures as **Great**, **Usable**, or **Retake**. For every Retake,
state the exact screen, seeded content, appearance, and status-bar state needed. Never
hide a poor raw capture with decorative composition.

## 5. Write and confirm the English captions

Write all three as two visible lines:

- line 1 is the strongest hook and starts with an imperative action verb
- line 2 completes the user payoff
- target three words total; five is the hard maximum
- use no terminal punctuation, ellipses, or marketing exclamation
- express an outcome rather than a feature label
- avoid repeating the same main verb or noun across the set

Store them as:

```json
{
  "01": ["Tap it out", "in Morse"],
  "02": ["Hear every", "signal"],
  "03": ["Flash a", "message"]
}
```

Present the screen pairing and all three English captions together. Stop until the user
approves them. Do not translate, configure capture for other locales, or design final
compositions before approval.

## 6. Transcreate every locale

Translate the shared intent, never the English syntax:

- write native store-advertising language for the market
- reuse established UI terminology
- keep the message understandable in under one second
- preserve natural phrase boundaries across two lines
- let Korean, Japanese, Chinese, and Arabic use their native grammar and casing
- use right-to-left direction for RTL copy
- shorten the idea before shrinking text excessively

Keep identical JSON keys and array shapes across locales.

## 7. Capture and verify the raw matrix

Use `fastlane snapshot` through a dedicated UI test target:

- inject deterministic demo state with launch arguments
- skip onboarding and prompts; disable permissions, review requests, and animation
- navigate with accessibility identifiers, never localized labels
- wait for stable elements rather than fixed sleeps
- use clean, consistent status bars and appearance
- verify one locale end to end before the full matrix

Copy the results into `raw/<locale>/<device>/`. Verify the same indexed screen appears
everywhere, the intended locale rendered, and no text is truncated. Recapture failures;
never repair app UI by editing pixels.

## 8. Gate the visual direction

Analyze the icon, app UI, theme tokens, target audience, domain, and approved positioning.
Derive exactly three distinct design directions tailored to this app. Do not ask the
user to choose a color in isolation.

For each direction present:

- direction name and one-sentence concept
- background palette with exact hex values
- background graphic or motif and why it belongs to this product
- typography treatment
- device framing and any real-UI breakout treatment
- how it supports the three-screen story
- main tradeoff or risk

Include one conservative, one expressive, and one strategically different option when
the brand permits it. Recommend one with a concrete rationale. Stop and obtain one
explicit user approval for the set-wide visual direction.

Do not create or modify the `.pen` composition, render final variants, or export final
screenshots before this approval. Once approved, record the decision in `direction.md`.
Do not ask for another aesthetic choice unless the rendered result materially violates
the approved direction or the user requests alternatives.

## 9. Prepare Pen

Use the installed `pen` CLI, not ad hoc HTML/CSS compositing:

```sh
command -v pen
pen version
pen status
```

If missing, report that `@pen.dev/cli` is required. If unauthenticated, ask the user to
run `pen login`; do not expose or request tokens in chat.

Prefer `pen interactive` because it exposes deterministic node operations, layout
inspection, screenshots, and per-frame export. Start every interactive session with:

```text
get_editor_state({ include_schema: true })
```

Use `get_guidelines` when a compatible Pen design guide helps. Inspect existing `.pen`
files with `batch_get` before modifying them. Save after meaningful changes.

## 10. Build the editable composition

Create or update `store-screenshots.pen` after the visual direction is approved:

- create one exact-dimension top-level frame per locale, device, and screenshot
- name frames `<locale>/<device>/NN-screen-name`
- use shared variables and reusable components for palette, typography, device shell,
  caption block, and recurring background motif
- place the unmodified raw capture inside a precise device viewport
- keep the device centered and high enough to feel dynamic; let its bottom bleed off
  canvas when appropriate
- keep copy in the upper area with generous horizontal safe margins
- render line 1 as the dominant hook and line 2 as the supporting payoff
- use locale-appropriate fonts, wrapping, casing, and direction
- keep the approved background system cohesive across all three screens

Prefer vector-native, editable background graphics. Use Pen image generation or stock
imagery only when the approved direction genuinely calls for illustration or
photography. Never add generic sparkles, random icons, or decoration unrelated to the
product story.

Optional breakout elements must come from a real, relevant UI panel in the raw capture.
Keep their content, orientation, and visual language faithful to the app. Do not invent
UI, rotate panels arbitrarily, or let breakouts obscure the headline or essential app
content.

Build and visually inspect the complete primary-locale set first. Use it as the style
template for every remaining locale and device; change copy and raw screen content, not
the approved design language.

## 11. Inspect and export

Use `snapshot_layout({ problemsOnly: true })` to catch clipping and overflow. Use
`get_screenshot` sparingly on completed top-level frames to inspect visual fidelity at
full size and thumbnail scale.

Export each top-level frame separately with Pen `export_nodes`, PNG format, and a scale
that produces the exact required pixel dimensions. Put only approved production files
in `final/<locale>/<device>/`.

Pen PNG exports include an alpha channel even when the top-level frame has a fully
opaque background. After export, remove only the alpha channel with Xcode's
`pngcrush`, writing to a temporary file before replacing the export:

```sh
tmp_png="$(mktemp).png"
xcrun pngcrush -q -rem alla -reduce input.png "$tmp_png"
mv "$tmp_png" input.png
sips -g hasAlpha input.png
```

Require `hasAlpha: no` for every final PNG. This channel removal is an allowed
technical normalization for store compatibility, not a visual correction. It must not
resize, crop, stretch, repaint, or otherwise alter the rendered composition.

Verify:

- exact width, height, color mode, and PNG format
- no alpha channel (`sips -g hasAlpha` reports `hasAlpha: no`)
- one final image per index, locale, and device
- no clipped, overlapping, untranslated, or unnaturally wrapped copy
- legibility at store thumbnail size
- consistent palette, motif, typography, device treatment, and spacing
- raw UI remains accurate and undistorted
- no watermark, debug layer, accidental Pen selection, or extra store chrome

If dimensions or content are wrong, fix the top-level Pen frame and re-export. Do not
stretch, crop, or repaint an incorrect export as a substitute.

## 12. Report

Report:

- positioning brief and selected screen-to-value mapping
- approved captions and visual direction
- raw capture matrix
- `.pen` source and `direction.md` paths
- final output paths and exact dimensions
- locales needing native review
- Pen version and validation results
- any intentionally omitted breakout or decorative treatment and why
