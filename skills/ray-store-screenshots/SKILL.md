---
name: ray-store-screenshots
description: Create or refresh localized store screenshots from approved positioning, including screen selection, captions, deterministic capture, editable Pen composition, export, and validation. Use for App Store or Play Store screenshot planning, automation, localization, design, or delivery.
---

# Store Screenshots

Produce approved copy, deterministic raw captures, an editable Pen source, and validated
store-ready PNGs. Follow repository instructions and existing layout first.

## 1. Resolve scope and evidence

Inspect the shipping app, supported locales, target stores and devices, existing
screenshots, capture configuration, brand assets, product specs, and current store
requirements. State the resolved scope and ask only about genuine ambiguity.

Default to one accepted large iPhone size. Add iPad when the shipping app supports it,
and use a different matrix when the user or repository defines one. Verify current
dimensions rather than relying on memory.

Require an approved, current store-positioning brief with an ordered value hierarchy and
claim boundaries. If it is missing or stale, use `$ray-store-positioning` and obtain
confirmation before continuing. Do not derive a competing screenshot-only strategy.

## 2. Plan screens and captions

Map the approved values to a compact screenshot story. Default to three screens, one for
each primary, differentiating, and proof value; use another count when the approved
strategy or store plan requires it.

For each screen record the value, source screen, seeded state, visual focal point, and
capture route. Prefer rich, legible shipping UI. Mark weak captures with a concrete
retake prescription rather than hiding them with decoration.

Read [references/copy-and-direction.md](references/copy-and-direction.md), draft the
primary-locale screen pairing and captions, and obtain approval before localization or
composition.

## 3. Capture the raw matrix

Read [references/capture-and-export.md](references/capture-and-export.md) before changing
capture configuration. Prefer deterministic UI-test capture with accessibility
identifiers and stable seeded state. Verify one locale end to end, then capture the full
matrix.

Follow an existing repository layout. Otherwise use:

```text
design/screenshots/
├── captions/<locale>.json
├── raw/<locale>/<device>/
├── final/<locale>/<device>/
├── direction.md
└── store-screenshots.pen
```

Keep the same indexed meaning across locales and devices. Recapture incorrect UI; do not
repair application content by editing pixels.

## 4. Approve the visual direction

Use the app icon, UI, theme tokens, audience, domain, and positioning to propose a small
set of meaningfully different directions. Default to three when that creates useful
choice; present fewer when the evidence supports only one or two credible directions.

For each, show the palette, product-specific motif, typography, device treatment, story
support, and main tradeoff. Recommend one and obtain a single set-wide approval. Record
the choice in `direction.md`; do not create the final composition before approval.

## 5. Compose in Pen

Read [references/pen-composition.md](references/pen-composition.md) before using Pen.
Inspect its schema and any existing `.pen` source before editing.

Create one exact-dimension top-level frame per locale, device, and screenshot. Name it
`<locale>/<device>/NN-screen-name`. Use shared variables and components for recurring
visual language, keep raw UI accurate, and adapt typography and direction by locale.

Build and inspect the complete primary-locale set first, then apply the approved system
to the remaining matrix. Use generated or stock imagery only when the approved direction
calls for it.

## 6. Export and validate

Install the bundled `scripts/export_screenshot.sh` as `tools/export_screenshot.sh` only
when the project lacks its own helper. Do not overwrite a project-local copy
automatically.

Follow the export and validation procedure in
[references/capture-and-export.md](references/capture-and-export.md). Validate layout,
dimensions, format, alpha, locale coverage, copy legibility, visual consistency, and raw
UI fidelity. Fix the Pen source and re-export when an output is wrong.

Report the positioning source, screen mapping, approved captions and direction, capture
matrix, editable source, final paths and dimensions, validation results, and locales
needing native review.
