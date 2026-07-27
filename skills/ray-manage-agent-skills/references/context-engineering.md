# Context-engineering rubric

Use this rubric when creating or materially updating a skill.

## Keep

- Ray-specific opinions, vocabulary, workflows, and quality bars
- facts the agent cannot reliably infer from the repository or tools
- hazards involving secrets, destructive actions, production state, or external users
- explicit approval gates that represent real product or business decisions
- verification criteria that distinguish a plausible result from a correct result

## Simplify

- replace universal prohibitions with a principle tied to surrounding context
- describe the desired outcome and boundary, then allow implementation judgment
- remove repeated instructions already enforced by a tool interface or higher-level rule
- shorten examples that anchor the agent to one implementation
- qualify arbitrary numbers as defaults unless the number is a real contract

## Split

Keep the core workflow and routing conditions in `SKILL.md`. Move these out:

- detailed tool command catalogs and platform variants to `references/`
- output schemas, rubrics, and long templates to `references/` or `assets/`
- repeatable deterministic transformations to `scripts/`
- files copied into user projects to `assets/`

Link every optional resource directly from `SKILL.md` and state exactly when to read it.
Avoid references that require another reference to discover them.

## Prefer interfaces

Use schemas, typed arguments, templates, tests, and scripts to express exact structure.
Prefer these over prose examples when the interface can carry the same constraint.

## Audit questions

1. Would a capable agent already know this instruction?
2. Is this rule true for every valid invocation?
3. Does it conflict with user or repository context?
4. Can the requirement live in a tool, test, schema, script, or reference?
5. Is the same idea stated elsewhere?
6. Does the description trigger narrowly enough without implementation detail?
7. Are strict gates proportional to the cost of a wrong action?
8. Can the result be verified from raw artifacts rather than claimed success?

The aim is not minimum length. The aim is high-value context loaded at the moment it is
needed.
