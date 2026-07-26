# Pen Store Screenshot Composition

Use these rules while proposing the visual direction and building the `.pen` source.
They distill the supplied ASO screenshot references while keeping the background system
app-specific and editable in Pen.

## Composition hierarchy

Build every top-level frame in this order:

1. app-specific background color and restrained motif
2. two-line caption block in the upper portion
3. centered device shell containing the exact raw capture
4. optional real-UI breakout or small story-supporting elements

Make line 1 the largest element and line 2 noticeably smaller. Keep the text centered
unless the approved direction makes another alignment clearly stronger. Reserve at
least about 15% horizontal padding on both sides and keep copy within the upper
20–25% of the frame.

Position the device high rather than leaving a dead gap below the copy. Let the device
continue past the bottom edge when that improves scale and energy. Use one device
treatment throughout the set.

## App-specific background decisions

Derive candidate palettes from:

- app icon and asset-catalog colors
- theme tokens and the dominant UI palette
- screenshots in the selected appearance
- product domain, audience, and emotional promise
- contrast with the device and app UI

Propose systems, not isolated colors. A direction may use:

- a bold solid field with a subtle vector motif
- a brand-native gradient when gradients are already part of the product identity
- a restrained domain-specific illustration or texture
- an abstract visualization of the product's core action

Keep the same visual grammar across all three screenshots. Vary motif placement only
to support composition. Reject generic particles, arbitrary icons, unrelated stock
imagery, low-contrast palettes, and graphics that compete with the headline or UI.

Prefer native Pen vectors and editable shapes. Use generated raster imagery only when
the approved concept requires it and the result can remain consistent across the set.

## Typography by locale

Prefer the app's brand font when it supports the locale well. Otherwise use a
locale-appropriate heavy sans serif:

- Latin: SF Pro Display or another high-quality brand-compatible sans
- Korean: Pretendard or a native Korean sans
- Japanese: Hiragino Sans
- Simplified Chinese: PingFang SC
- Traditional Chinese: PingFang TC
- Arabic: SF Arabic or another native Arabic sans

Do not force uppercase on scripts without case. Use character-aware wrapping for CJK
and right-to-left layout for Arabic. Preserve line meaning and natural phrase
boundaries. Shorten copy before reducing it below the set's readable scale.

## Device and raw UI integrity

Render the device shell consistently with a dark modern bezel and correct corner
geometry. Preserve the raw screenshot exactly inside its viewport:

- no regenerated UI
- no rewritten labels
- no stretched or distorted screen
- no invented status-bar content
- no crop that removes the feature proving the caption

A breakout is optional. Use one only when a complete real UI panel directly reinforces
the benefit. Keep it at the same orientation and approximately the same vertical
relationship as in the device, enlarge it deliberately, overlap the bezel, and use a
subtle shadow for depth. Never break out a random button or icon.

## Pen source structure

Use:

- exact-size top-level frames as export boundaries
- shared variables for colors and type scales
- reusable components for device, caption, and repeated motifs
- stable frame names: `<locale>/<device>/NN-screen-name`
- scale-1 PNG exports when the top-level frame already uses target pixels

Start `pen interactive` with `get_editor_state({ include_schema: true })`. Inspect
existing nodes with `batch_get`, make grouped changes through `batch_design`, check
geometry with `snapshot_layout`, and export top-level frames with `export_nodes`.

Keep the `.pen` file as the source of truth. Correct layout problems in Pen and
re-export instead of post-processing a bad PNG.

## Reference basis

- https://raw.githubusercontent.com/youngminz/claude-skill-aso-appstore-screenshots/refs/heads/main/web/renderer.html
- https://raw.githubusercontent.com/youngminz/claude-skill-aso-appstore-screenshots/refs/heads/main/AGENTS.md
- https://raw.githubusercontent.com/youngminz/claude-skill-aso-appstore-screenshots/refs/heads/main/SKILL.md
- https://docs.pen.dev/for-developers/pencil-cli
