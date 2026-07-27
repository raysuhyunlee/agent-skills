---
name: ray-manage-agent-skills
description: Find and manage Ray's personal agent-skills source repository. Use when creating, auditing, simplifying, updating, validating, installing, or removing custom skills, or when maintaining the repository's skill catalog and installation links.
---

# Manage Agent Skills

Manage skills in their source repository, not through installed copies.

## 1. Locate the repository

Run:

```sh
python3 scripts/find_agent_skills_repo.py
```

Use the returned directory as the repository root. The script resolves installed skill
symlinks first, then searches conventional locations and nearby Git repositories. If it
returns more than one candidate, prefer the repository containing the skill being
updated; otherwise show the candidates and ask the user to choose.

Inspect repository instructions, status, README, installer, and existing skill patterns
before editing. Preserve unrelated work in a dirty worktree.

## 2. Choose the operation

- **Create:** confirm that no existing skill already covers the request, then use the
  system `skill-creator` initializer inside `<repo>/skills`.
- **Update:** read the complete target `SKILL.md` and every directly required resource.
  Preserve its user-visible contract unless the user requested a behavior change.
- **Audit:** assess triggering, instruction value, degrees of freedom, progressive
  disclosure, duplication, portability, validation, and stale interfaces.
- **Remove:** resolve source and installed links exactly. Delete only with explicit user
  authorization, then remove links owned by that source.

Read [references/context-engineering.md](references/context-engineering.md) before
creating a skill or materially restructuring an existing one.

## 3. Design or revise

Keep `SKILL.md` as a lightweight workflow and router:

- encode Ray-specific preferences, domain knowledge, real hazards, and approval points
- let the agent use judgment for context-dependent choices
- place detailed procedures, rubrics, schemas, and variants in one-level references
- place deterministic repeated operations in scripts
- place copied output material in assets
- replace long demonstrations with expressive interfaces or templates
- remove repeated, obvious, contradictory, or obsolete instructions

Use strict rules only for fragile operations, irreversible external changes, secrets,
evidence integrity, or an explicit product contract. Treat numbers and approval gates as
defaults unless they are intentional invariants.

Keep frontmatter limited to `name` and `description`. Make the description concise but
include both capability and trigger conditions. Generate or refresh
`agents/openai.yaml` after material changes.

## 4. Integrate with the repository

For a new or renamed skill:

1. add it under `<repo>/skills/<skill-name>`
2. update the repository skill catalog without overwriting unrelated README edits
3. run the repository installer in dry-run mode
4. install only after the dry run shows links owned by this repository

Use relative paths inside a skill. Do not embed the current checkout path in
instructions or scripts.

## 5. Validate

Run the system `quick_validate.py` for every changed skill using an environment that
provides PyYAML. Also verify:

- referenced local files exist and are one level from `SKILL.md`
- bundled scripts run or at least pass their language syntax checker
- `agents/openai.yaml` still describes the skill and mentions `$skill-name`
- the repository installer dry run succeeds
- installed links resolve to the canonical source
- no duplicate skill name or near-identical trigger remains in another install root

Report changed skills, important contract changes, validation evidence, installation
state, and anything intentionally left unchanged.
