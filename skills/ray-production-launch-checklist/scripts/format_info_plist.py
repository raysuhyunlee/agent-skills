#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

from __future__ import annotations

import argparse
import plistlib
from pathlib import Path


def format_info_plist(plist_path: Path, *, sort_keys: bool = True) -> None:
    if not plist_path.exists():
        raise FileNotFoundError(f"{plist_path} not found")

    with plist_path.open("rb") as file:
        plist_data = plistlib.load(file)

    with plist_path.open("wb") as file:
        plistlib.dump(plist_data, file, sort_keys=sort_keys)

    print(f"Formatted {plist_path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rewrite an iOS Info.plist with plistlib formatting."
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Project root used for the default plist path.",
    )
    parser.add_argument(
        "--plist-path",
        type=Path,
        help="Info.plist path. Defaults to <project-root>/ios/Runner/Info.plist.",
    )
    parser.add_argument(
        "--preserve-key-order",
        action="store_true",
        help="Preserve plistlib load order instead of sorting keys.",
    )
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    plist_path = args.plist_path or project_root / "ios" / "Runner" / "Info.plist"
    if not plist_path.is_absolute():
        plist_path = project_root / plist_path

    format_info_plist(plist_path, sort_keys=not args.preserve_key_order)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
