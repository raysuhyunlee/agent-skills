# Screenshot capture and export

## Deterministic capture

Prefer `fastlane snapshot` through a dedicated UI-test target:

- inject deterministic demo state through launch arguments
- suppress onboarding, permissions, review requests, and animation when not being shown
- navigate with accessibility identifiers rather than localized labels
- wait for stable elements instead of fixed sleeps
- keep appearance and status bars consistent
- verify locale, content, clipping, and indexed screen meaning

Copy captures to `raw/<locale>/<device>/`.

## Pen export

Name each top-level frame `<locale>/<device>/NN-screen-name` and run:

```sh
./tools/export_screenshot.sh <pen-node-id>
```

The helper exports at 1× to `final/<locale>/<device>/NN_screen-name.png`, removes the
alpha channel, and checks dimensions. Use a current standalone `pngcrush`; do not use the
obsolete copy embedded in Xcode.

Validate:

- exact width, height, PNG format, color mode, and `hasAlpha: no`
- one output for every expected index, locale, and device
- no clipped, overlapping, untranslated, or unnatural copy
- legibility at store thumbnail size
- consistent approved visual language
- undistorted source UI and no debug, editor, watermark, or store chrome

Never stretch, crop, repaint, or pixel-repair an incorrect export. Correct the capture or
top-level Pen frame and export again.
