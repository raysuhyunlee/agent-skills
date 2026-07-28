#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_dir="$repo_root/skills"
instructions_source="$repo_root/instructions/AGENTS.md"
mode="install"
dry_run=false

# Codex reads ~/.agents/skills, Claude Code reads ~/.claude/skills.
# AGENT_SKILLS_DIR overrides both with a single directory.
if [ -n "${AGENT_SKILLS_DIR:-}" ]; then
  target_dirs=("$AGENT_SKILLS_DIR")
else
  target_dirs=("$HOME/.agents/skills" "$HOME/.claude/skills")
fi

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

is_skill() {
  [ -d "$1" ] && [ -f "$1/SKILL.md" ]
}

if [ ! -d "$source_dir" ]; then
  echo "Missing skills directory: $source_dir" >&2
  exit 1
fi

if [ ! -f "$instructions_source" ]; then
  echo "Missing global instructions: $instructions_source" >&2
  exit 1
fi

# Fail before creating any link when a target is owned by another source.
if [ "$mode" = "install" ]; then
  for target_dir in "${target_dirs[@]}"; do
    for source in "$source_dir"/*; do
      is_skill "$source" || continue

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
  done

  instruction_targets=("$HOME/.codex/AGENTS.md" "$HOME/.claude/CLAUDE.md")
  for target in "${instruction_targets[@]}"; do
    if [ -L "$target" ] && [ "$(readlink "$target")" = "$instructions_source" ]; then
      continue
    fi
    if [ -e "$target" ] || [ -L "$target" ]; then
      echo "Refusing to replace existing target: $target" >&2
      exit 1
    fi
  done

  run mkdir -p "$HOME/.codex" "$HOME/.claude"
fi

found=false
for source in "$source_dir"/*; do
  is_skill "$source" || continue
  found=true

  name="$(basename "$source")"

  for target_dir in "${target_dirs[@]}"; do
    target="$target_dir/$name"

    if [ "$mode" = "unlink" ]; then
      if [ -L "$target" ] && [ "$(readlink "$target")" = "$source" ]; then
        run rm "$target"
        if ! $dry_run; then
          echo "Unlinked $name -> $target_dir"
        fi
      elif [ -e "$target" ] || [ -L "$target" ]; then
        echo "Skipped $name in $target_dir: target is not managed by this repository" >&2
      else
        echo "Skipped $name in $target_dir: not installed"
      fi
      continue
    fi

    if [ -L "$target" ] && [ "$(readlink "$target")" = "$source" ]; then
      echo "Up to date: $name -> $target_dir"
    elif [ -e "$target" ] || [ -L "$target" ]; then
      echo "Refusing to replace existing target: $target" >&2
      exit 1
    else
      run ln -s "$source" "$target"
      if ! $dry_run; then
        echo "Linked $name -> $target_dir"
      fi
    fi
  done
done

if ! $found; then
  echo "No skills found in $source_dir" >&2
  exit 1
fi

instruction_targets=("$HOME/.codex/AGENTS.md" "$HOME/.claude/CLAUDE.md")
for target in "${instruction_targets[@]}"; do
  target_dir="$(dirname "$target")"
  target_name="$(basename "$target")"

  if [ "$mode" = "unlink" ]; then
    if [ -L "$target" ] && [ "$(readlink "$target")" = "$instructions_source" ]; then
      run rm "$target"
      if ! $dry_run; then
        echo "Unlinked global instructions -> $target"
      fi
    elif [ -e "$target" ] || [ -L "$target" ]; then
      echo "Skipped $target_name in $target_dir: target is not managed by this repository" >&2
    else
      echo "Skipped $target_name in $target_dir: not installed"
    fi
  elif [ -L "$target" ] && [ "$(readlink "$target")" = "$instructions_source" ]; then
    echo "Up to date: global instructions -> $target"
  elif [ -e "$target" ] || [ -L "$target" ]; then
    echo "Refusing to replace existing target: $target" >&2
    exit 1
  else
    run ln -s "$instructions_source" "$target"
    if ! $dry_run; then
      echo "Linked global instructions -> $target"
    fi
  fi
done
