#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests>=2.32.4",
# ]
# ///

import argparse
import html
import json
import plistlib
import re
from pathlib import Path

import requests

ADMOB_EXPO_PLUGIN = "react-native-google-mobile-ads"
GOOGLE_SKADNETWORK_URL = "https://developers.google.com/admob/ios/privacy/strategies?hl=en"
MEDIATION_SOURCE = "mediation"
SOURCE_CHOICES = ("auto", "google", MEDIATION_SOURCE)
MEDIATED_ADNETWORKS = "google,ironsource,vungle,facebook,tiktok,unityads"
MEDIATED_SKADNETWORK_URL = (
    "https://skadnetwork-ids.applovin.com/v1/skadnetworkids.json"
    f"?adnetworks={MEDIATED_ADNETWORKS}"
)

SKADNETWORK_URL = MEDIATED_SKADNETWORK_URL


def detect_source(project_root: Path) -> str:
    pubspec_path = project_root / "pubspec.yaml"
    if not pubspec_path.exists():
        return "google"
    pubspec = pubspec_path.read_text(encoding="utf-8")
    return MEDIATION_SOURCE if "gma_mediation_" in pubspec else "google"


def resolve_project_path(path: Path | None, project_root: Path) -> Path | None:
    if path is None:
        return None
    return path if path.is_absolute() else project_root / path


def fetch_google_skadnetwork_ids(url: str = GOOGLE_SKADNETWORK_URL) -> list[str]:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    ids: list[str] = []
    pattern = re.compile(r"<string>\s*([a-z0-9]+\.skadnetwork)\s*</string>")
    for source in (response.text, html.unescape(response.text)):
        for match in pattern.finditer(source):
            value = match.group(1)
            if value not in ids:
                ids.append(value)
    if not ids:
        raise ValueError("No SKAdNetwork identifiers found in Google AdMob docs")
    return ids


def fetch_skadnetwork_ids(url: str = SKADNETWORK_URL) -> list[dict[str, str]] | None:
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        if "skadnetwork_ids" in data and isinstance(data["skadnetwork_ids"], list):
            return data["skadnetwork_ids"]
        print("Error: 'skadnetwork_ids' not found in response")
        return None
    except requests.exceptions.RequestException as error:
        print(f"Error: network request failed: {error}")
        return None
    except ValueError as error:
        print(f"Error: JSON parse failed: {error}")
        return None


def normalize_skadnetwork_ids(skad_ids: list[str] | list[dict[str, str]]) -> list[str]:
    normalized: list[str] = []
    for item in skad_ids:
        if isinstance(item, str):
            value = item
        elif isinstance(item, dict):
            value = item.get("skadnetwork_id", "")
        else:
            continue
        if value and value not in normalized:
            normalized.append(value)
    return normalized


def update_info_plist(
    plist_path: str | Path,
    skad_ids: list[str] | list[dict[str, str]] | None = None,
) -> None:
    if not skad_ids:
        print("No SKAdNetwork IDs to update")
        return

    plist_path = Path(plist_path)
    ids = normalize_skadnetwork_ids(skad_ids)
    if not ids:
        print("No valid SKAdNetwork IDs after normalization")
        return

    if not plist_path.exists():
        raise FileNotFoundError(f"{plist_path} not found")

    with plist_path.open("rb") as file:
        plist_data = plistlib.load(file)

    plist_data["SKAdNetworkItems"] = [
        {"SKAdNetworkIdentifier": value}
        for value in ids
    ]

    with plist_path.open("wb") as file:
        plistlib.dump(plist_data, file, sort_keys=True)

    print(f"Updated {len(ids)} SKAdNetwork IDs in {plist_path}")


def find_matching_delimiter(
    text: str,
    opening_index: int,
    opening_char: str,
    closing_char: str,
) -> int:
    depth = 0
    in_string: str | None = None
    escaped = False
    in_line_comment = False
    in_block_comment = False

    index = opening_index
    while index < len(text):
        char = text[index]
        next_char = text[index + 1] if index + 1 < len(text) else ""

        if in_line_comment:
            if char == "\n":
                in_line_comment = False
            index += 1
            continue

        if in_block_comment:
            if char == "*" and next_char == "/":
                in_block_comment = False
                index += 2
                continue
            index += 1
            continue

        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == in_string:
                in_string = None
            index += 1
            continue

        if char == "/" and next_char == "/":
            in_line_comment = True
            index += 2
            continue

        if char == "/" and next_char == "*":
            in_block_comment = True
            index += 2
            continue

        if char in ("'", '"', "`"):
            in_string = char
            index += 1
            continue

        if char == opening_char:
            depth += 1
        elif char == closing_char:
            depth -= 1
            if depth == 0:
                return index

        index += 1

    raise ValueError(f"Could not find matching `{closing_char}`")


def find_matching_bracket(text: str, opening_index: int) -> int:
    return find_matching_delimiter(text, opening_index, "[", "]")


def find_matching_brace(text: str, opening_index: int) -> int:
    return find_matching_delimiter(text, opening_index, "{", "}")


def format_js_skadnetwork_property(
    ids: list[str],
    property_indent: str,
    item_indent: str,
    quote: str,
) -> str:
    lines = [f"{property_indent}skAdNetworkItems: ["]
    lines.extend(f"{item_indent}{quote}{value}{quote}," for value in ids)
    lines.append(f"{property_indent}],")
    return "\n".join(lines)


def insert_js_skadnetwork_items(text: str, ids: list[str]) -> str:
    plugin_match = re.search(rf"(['\"]){re.escape(ADMOB_EXPO_PLUGIN)}\1", text)
    if plugin_match is None:
        raise ValueError(f"Could not find `{ADMOB_EXPO_PLUGIN}` in Expo config")

    opening_index = text.find("{", plugin_match.end())
    if opening_index == -1:
        raise ValueError(f"Could not find config object for `{ADMOB_EXPO_PLUGIN}`")

    closing_index = find_matching_brace(text, opening_index)
    body = text[opening_index + 1 : closing_index]
    object_line_start = text.rfind("\n", 0, opening_index) + 1
    object_indent_match = re.match(r"[ \t]*", text[object_line_start:opening_index])
    object_indent = object_indent_match.group(0) if object_indent_match else ""
    property_indent_match = re.search(
        r"\n(?P<indent>[ \t]*)[A-Za-z_$][\w$]*\s*:",
        body,
    )
    property_indent = (
        property_indent_match.group("indent")
        if property_indent_match
        else object_indent + "  "
    )
    item_indent = property_indent + "  "
    quote_match = re.search(r"['\"]", body)
    quote = quote_match.group(0) if quote_match else "'"
    property_text = format_js_skadnetwork_property(
        ids,
        property_indent,
        item_indent,
        quote,
    )
    separator_after = "" if body.startswith("\n") else "\n"
    insertion = "\n" + property_text + separator_after

    return text[: opening_index + 1] + insertion + text[opening_index + 1 :]


def replace_js_skadnetwork_items(text: str, ids: list[str]) -> str:
    match = re.search(r"(?m)^(?P<indent>[ \t]*)skAdNetworkItems\s*:\s*\[", text)
    if match is None:
        return insert_js_skadnetwork_items(text, ids)

    indent = match.group("indent")
    opening_index = match.end() - 1
    closing_index = find_matching_bracket(text, opening_index)
    body = text[opening_index + 1 : closing_index]

    item_indent_match = re.search(r"\n(?P<indent>[ \t]*)['\"]", body)
    item_indent = item_indent_match.group("indent") if item_indent_match else indent + "  "

    quote_match = re.search(r"['\"]", body)
    quote = quote_match.group(0) if quote_match else "'"
    lines = [f"{item_indent}{quote}{value}{quote}," for value in ids]
    replacement = "[\n" + "\n".join(lines) + "\n" + indent + "]"

    return text[:opening_index] + replacement + text[closing_index + 1 :]


def update_json_expo_config(config_path: Path, ids: list[str]) -> None:
    with config_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    expo_config = data.get("expo", data)
    plugins = expo_config.get("plugins")
    if not isinstance(plugins, list):
        raise ValueError("Expo config does not contain a `plugins` array")

    updated = False
    for index, plugin in enumerate(plugins):
        if plugin == ADMOB_EXPO_PLUGIN:
            plugins[index] = [ADMOB_EXPO_PLUGIN, {"skAdNetworkItems": ids}]
            updated = True
            break

        if isinstance(plugin, list) and plugin and plugin[0] == ADMOB_EXPO_PLUGIN:
            if len(plugin) == 1 or not isinstance(plugin[1], dict):
                plugin[:] = [ADMOB_EXPO_PLUGIN, {}]
            plugin[1]["skAdNetworkItems"] = ids
            updated = True
            break

    if not updated:
        raise ValueError(f"Could not find `{ADMOB_EXPO_PLUGIN}` in Expo config plugins")

    with config_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def update_expo_config(
    expo_config_path: str | Path,
    skad_ids: list[str] | list[dict[str, str]] | None = None,
) -> None:
    if not skad_ids:
        print("No SKAdNetwork IDs to update")
        return

    expo_config_path = Path(expo_config_path)
    ids = normalize_skadnetwork_ids(skad_ids)
    if not ids:
        print("No valid SKAdNetwork IDs after normalization")
        return

    if not expo_config_path.exists():
        raise FileNotFoundError(f"{expo_config_path} not found")

    if expo_config_path.suffix == ".json":
        update_json_expo_config(expo_config_path, ids)
    else:
        text = expo_config_path.read_text(encoding="utf-8")
        updated_text = replace_js_skadnetwork_items(text, ids)
        expo_config_path.write_text(updated_text, encoding="utf-8")

    print(f"Updated {len(ids)} SKAdNetwork IDs in {expo_config_path}")


def fetch_ids_for_source(source: str) -> list[str] | list[dict[str, str]]:
    if source == "google":
        return fetch_google_skadnetwork_ids()

    fetched_ids = fetch_skadnetwork_ids(MEDIATED_SKADNETWORK_URL)
    if fetched_ids is None:
        raise RuntimeError("Failed to fetch AdMob mediation SKAdNetwork IDs")
    return fetched_ids


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Project root used for Flutter defaults and --source auto.",
    )
    parser.add_argument(
        "--plist-path",
        type=Path,
        help="Info.plist path to update. Defaults to <project-root>/ios/Runner/Info.plist when it exists.",
    )
    parser.add_argument(
        "--expo-config-path",
        type=Path,
        help="Expo app config path to update, such as app.config.ts, app.config.js, or app.json.",
    )
    parser.add_argument(
        "--source",
        default="auto",
        metavar="{auto,google,mediation}",
        help=(
            "SKAdNetwork source. auto uses mediation when gma_mediation_* "
            "is present in pubspec.yaml."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and parse IDs without writing files.",
    )
    args = parser.parse_args()
    if args.source not in SOURCE_CHOICES:
        parser.error(f"--source must be one of: {', '.join(SOURCE_CHOICES)}")

    project_root = args.project_root.resolve()
    plist_path = resolve_project_path(args.plist_path, project_root)
    expo_config_path = resolve_project_path(args.expo_config_path, project_root)
    if plist_path is None:
        default_plist_path = project_root / "ios" / "Runner" / "Info.plist"
        if default_plist_path.exists():
            plist_path = default_plist_path

    if plist_path is None and expo_config_path is None:
        parser.error("At least one of --plist-path or --expo-config-path is required")

    source = detect_source(project_root) if args.source == "auto" else args.source
    ids = fetch_ids_for_source(source)

    if args.dry_run:
        print(f"Fetched {len(normalize_skadnetwork_ids(ids))} SKAdNetwork IDs")
        print(f"Source: {source}")
        if plist_path is not None:
            print(f"Would update Info.plist: {plist_path}")
        if expo_config_path is not None:
            print(f"Would update Expo config: {expo_config_path}")
        return 0

    if plist_path is not None:
        update_info_plist(plist_path, ids)
    if expo_config_path is not None:
        update_expo_config(expo_config_path, ids)
    print(f"Source: {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
