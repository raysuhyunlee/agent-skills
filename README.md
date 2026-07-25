# Agent Skills

Personal agent skills managed as source files and installed with individual symlinks.

## Skills

- `ray-init-project-specs`: initialize `AGENTS.md`, `README.md`, and `spec/`
- `ray-localize`: localize project content across supported locales
- `ray-quality-and-spec-check`: review code quality and spec compliance
- `ray-appstore-market-research`: research app keywords, competitors, reviews, and customer needs
- `ray-production-launch-checklist`: production-release checklist workflow, including launch-time AdMob SKAdNetwork ID sync
- `ray-store-screenshots`: select store screenshot screens, write localized captions, and capture raw screenshots with fastlane snapshot

## Install

```sh
./install.sh
```

The default targets are `$HOME/.agents/skills` (Codex) and `$HOME/.claude/skills` (Claude Code), so every skill is available to both tools. Override them with a single directory using `AGENT_SKILLS_DIR`:

```sh
AGENT_SKILLS_DIR="$HOME/custom-agent-skills" ./install.sh
```

The installer creates one symlink per skill per target. It never replaces existing files, directories, or links owned by another source.

## Commands

```sh
./install.sh --dry-run
./install.sh --unlink
```
