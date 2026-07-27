#!/usr/bin/env python3

import argparse
import os
from pathlib import Path


def is_repo(path: Path) -> bool:
    return (
        path.is_dir()
        and (path / "skills").is_dir()
        and (path / "install.sh").is_file()
    )


def add_candidate(candidates: list[Path], path: Path) -> None:
    try:
        resolved = path.expanduser().resolve()
    except OSError:
        return
    if is_repo(resolved) and resolved not in candidates:
        candidates.append(resolved)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Locate a personal agent-skills source repository."
    )
    parser.add_argument("--all", action="store_true", help="print every candidate")
    args = parser.parse_args()

    candidates: list[Path] = []
    home = Path.home()

    for install_root in (home / ".agents/skills", home / ".claude/skills"):
        if not install_root.is_dir():
            continue
        for installed in install_root.iterdir():
            if installed.is_symlink():
                source = installed.resolve()
                if source.parent.name == "skills":
                    add_candidate(candidates, source.parent.parent)

    configured = os.environ.get("AGENT_SKILLS_REPO")
    if configured:
        add_candidate(candidates, Path(configured))

    for path in (
        home / "Documents/agent-skills",
        home / "Developer/agent-skills",
        home / "Projects/agent-skills",
        home / "agent-skills",
    ):
        add_candidate(candidates, path)

    if not candidates:
        for parent in (home / "Documents", home / "Developer", home / "Projects"):
            if not parent.is_dir():
                continue
            for path in parent.glob("*/.git"):
                add_candidate(candidates, path.parent)

    if not candidates:
        return 1

    selected = candidates if args.all else candidates[:1]
    print("\n".join(str(path) for path in selected))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
