#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_dir="$repo_root/skills"
target_dir="${AGENT_SKILLS_DIR:-$HOME/.agents/skills}"
mode="install"
dry_run=false

usage() {
  echo "Usage: ./install.sh [--dry-run] [--unlink]"
}

for arg in "$@"; do
  case "$arg" in
    --dry-run) dry_run=true ;;
    --unlink) mode="unlink" ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      exit 2
      ;;
  esac
done

run() {
  if $dry_run; then
    printf 'Would run:'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

if [ ! -d "$source_dir" ]; then
  echo "Missing skills directory: $source_dir" >&2
  exit 1
fi

if [ "$mode" = "install" ]; then
  for source in "$source_dir"/*; do
    [ -d "$source" ] || continue
    [ -f "$source/SKILL.md" ] || continue

    target="$target_dir/$(basename "$source")"
    if [ -L "$target" ] && [ "$(readlink "$target")" = "$source" ]; then
      continue
    fi
    if [ -e "$target" ] || [ -L "$target" ]; then
      echo "Refusing to replace existing target: $target" >&2
      exit 1
    fi
  done

  run mkdir -p "$target_dir"
fi

found=false
for source in "$source_dir"/*; do
  [ -d "$source" ] || continue
  [ -f "$source/SKILL.md" ] || continue
  found=true

  name="$(basename "$source")"
  target="$target_dir/$name"

  if [ "$mode" = "unlink" ]; then
    if [ -L "$target" ] && [ "$(readlink "$target")" = "$source" ]; then
      run rm "$target"
      if ! $dry_run; then
        echo "Unlinked $name"
      fi
    elif [ -e "$target" ] || [ -L "$target" ]; then
      echo "Skipped $name: target is not managed by this repository" >&2
    else
      echo "Skipped $name: not installed"
    fi
    continue
  fi

  if [ -L "$target" ] && [ "$(readlink "$target")" = "$source" ]; then
    echo "Up to date: $name"
  elif [ -e "$target" ] || [ -L "$target" ]; then
    echo "Refusing to replace existing target: $target" >&2
    exit 1
  else
    run ln -s "$source" "$target"
    if ! $dry_run; then
      echo "Linked $name"
    fi
  fi
done

if ! $found; then
  echo "No skills found in $source_dir" >&2
  exit 1
fi
