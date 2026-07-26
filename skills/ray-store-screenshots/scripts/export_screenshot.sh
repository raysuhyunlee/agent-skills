#!/usr/bin/env bash
#
# Export one top-level App Store screenshot frame from the Pen source.
#
# Usage:
#   ./tools/export_screenshot.sh <pen-node-id>

set -euo pipefail

usage() {
  echo "Usage: ./tools/export_screenshot.sh <pen-node-id>" >&2
}

if [ "$#" -ne 1 ]; then
  usage
  exit 2
fi

node_id="$1"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pen_file="$repo_root/design/screenshots/store-screenshots.pen"
final_root="$repo_root/design/screenshots/final"
export_scale=3

for command_name in pen perl base64 pngcrush sips; do
  command -v "$command_name" >/dev/null || {
    echo "Missing required command: $command_name" >&2
    exit 1
  }
done

[ -f "$pen_file" ] || {
  echo "Missing Pen source: $pen_file" >&2
  exit 1
}

staging_dir="$(mktemp -d "$repo_root/design/screenshots/.export.XXXXXX")"
session_log="$staging_dir/pen.log"
rendered_png="$staging_dir/rendered.png"
normalized_png="$staging_dir/normalized.png"
trap 'rm -rf "$staging_dir"' EXIT

pen interactive --app desktop --in "$pen_file" >"$session_log" 2>&1 <<EOF
batch_get({ nodeIds: ["$node_id"], readDepth: 0 })
export_nodes({ nodeIds: ["$node_id"], outputDir: "$staging_dir", format: "png", scale: $export_scale })
exit()
EOF

frame_name="$(
  perl -ne 'if (/"name": "([^"]+)"/) { print $1; exit }' "$session_log"
)"
frame_width="$(
  perl -ne 'if (/"width": ([0-9]+)/) { print $1; exit }' "$session_log"
)"
frame_height="$(
  perl -ne 'if (/"height": ([0-9]+)/) { print $1; exit }' "$session_log"
)"

if [[ ! "$frame_name" =~ ^([^/]+)/([^/]+)/([0-9][0-9]-.+)$ ]]; then
  tail -n 30 "$session_log" >&2
  echo "Node must be named <locale>/<device>/NN-screen-name: $node_id" >&2
  exit 1
fi

locale="${BASH_REMATCH[1]}"
device="${BASH_REMATCH[2]}"
screen_name="${BASH_REMATCH[3]}"
filename="${screen_name/-/_}.png"
target_dir="$final_root/$locale/$device"
target_png="$target_dir/$filename"

perl -ne 'print "$1\n" if /"image": "([^"]+)"/' "$session_log" \
  | base64 -D >"$rendered_png"

[ -s "$rendered_png" ] || {
  tail -n 30 "$session_log" >&2
  echo "Pen did not export node: $node_id" >&2
  exit 1
}

if ! pngcrush -q -rem alla -reduce "$rendered_png" "$normalized_png" >/dev/null 2>&1; then
  echo "Failed to remove the PNG alpha channel" >&2
  exit 1
fi

expected_width=$((frame_width * export_scale))
expected_height=$((frame_height * export_scale))
actual_width="$(sips -g pixelWidth "$normalized_png" | awk '/pixelWidth:/ { print $2 }')"
actual_height="$(sips -g pixelHeight "$normalized_png" | awk '/pixelHeight:/ { print $2 }')"
has_alpha="$(sips -g hasAlpha "$normalized_png" | awk '/hasAlpha:/ { print $2 }')"

if [ "$actual_width" != "$expected_width" ] || [ "$actual_height" != "$expected_height" ]; then
  echo "Invalid dimensions: ${actual_width}x${actual_height}; expected ${expected_width}x${expected_height}" >&2
  exit 1
fi
if [ "$has_alpha" != "no" ]; then
  echo "Alpha channel remains in exported PNG" >&2
  exit 1
fi

mkdir -p "$target_dir"
mv "$normalized_png" "$target_png"

echo "Exported $frame_name -> $target_png (${actual_width}x${actual_height}, no alpha)"
