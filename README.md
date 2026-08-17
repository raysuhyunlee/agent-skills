# Agent Skills

Personal agent skills and global instructions managed as source files and installed
with individual symlinks.

## Global Instructions

- `instructions/AGENTS.md`: shared communication guidance for Codex and Claude Code

## Skills

- `ray-init-project-specs`: initialize `AGENTS.md`, `README.md`, and `spec/`
- `ray-localize`: localize project content across supported locales
- `ray-quality-and-spec-check`: review code quality and spec compliance
- `ray-manage-agent-skills`: create, audit, update, validate, and install personal skills
- `ray-appstore-market-research`: research app keywords, competitors, reviews, and customer needs
- `ray-release`: prepare, build, upload, submit, release, and monitor App Store or Google Play releases
- `ray-store-positioning`: derive and confirm shared core-value positioning for store assets
- `ray-store-listing`: create ASO-backed store metadata with separate name and keyword approval gates
- `ray-store-screenshots`: capture localized app screens and compose final store-ready PNGs with the pen.dev CLI

## Install

```sh
./install.sh
```

The default skill targets are `$HOME/.agents/skills` (Codex) and
`$HOME/.claude/skills` (Claude Code), so every skill is available to both tools.
The global instructions are linked to `$HOME/.codex/AGENTS.md` and
`$HOME/.claude/CLAUDE.md`.

Override the skill targets with a single directory using `AGENT_SKILLS_DIR`:

```sh
AGENT_SKILLS_DIR="$HOME/custom-agent-skills" ./install.sh
```

The installer creates one symlink per skill per target and one link per global
instruction target. It never replaces existing files, directories, or links owned by
another source.

## Commands

```sh
./install.sh --dry-run
./install.sh --unlink
```
