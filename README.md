# Agent Skills

Personal agent skills managed as source files and installed with individual symlinks.

## Skills

- `ray-init-project-specs`: initialize `AGENTS.md`, `README.md`, and `spec/`
- `ray-localize`: localize project content across supported locales
- `ray-quality-and-spec-check`: review code quality and spec compliance
- `ray-manage-agent-skills`: create, audit, update, validate, and install personal skills
- `ray-appstore-market-research`: research app keywords, competitors, reviews, and customer needs
- `ray-production-launch-checklist`: production-release checklist workflow, including launch-time AdMob SKAdNetwork ID sync
- `ray-production-build`: create, sign, validate, and upload production builds for App Store Connect or Google Play
- `ray-app-review-notes`: draft first-submission App Review notes and a physical-device demo recording plan
- `ray-store-positioning`: derive and confirm shared core-value positioning for store assets
- `ray-store-listing`: create ASO-backed store metadata with separate name and keyword approval gates
- `ray-store-screenshots`: capture localized app screens and compose final store-ready PNGs with the pen.dev CLI

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
