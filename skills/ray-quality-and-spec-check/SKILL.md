---
name: ray-quality-and-spec-check
description: Review code, configuration, or a change set for project-specification compliance and evidence-backed code quality issues. Use for quality checks, spec checks, compliance checks, code reviews, PR reviews, or questions such as "does this follow the spec?".
---

# Quality and Spec Check

Review without editing unless the user also asks for fixes. Prioritize correctness and verifiable contract violations over style preferences.

## 1. Set the review scope

1. Read repository instructions first.
2. Use the user-provided files, diff, commit, or PR as the scope.
3. If no scope is given, inspect the working-tree diff. If it is empty, review the smallest relevant project area that can be inferred from the request.
4. Find specifications through the repository's documentation index, linked domain documents, and configuration. Ask for a spec path only when it cannot be discovered.
5. Read every specification that governs the scoped code.

Do not treat examples or historical notes as current requirements when a document distinguishes them. Follow the repository's stated precedence rules and report contradictions between sources.

## 2. Build the compliance checklist

Extract only testable requirements relevant to the scope, including:

- required behavior and edge cases
- architecture and dependency boundaries
- naming, file placement, and schema rules
- required or forbidden APIs and patterns
- security, privacy, compatibility, and platform constraints
- required tests, validation, and documentation updates

Record the source file and line for each requirement. Do not invent requirements from general preferences.

## 3. Inspect and verify

Trace each requirement into the implementation and tests. Search call sites and related configuration when behavior crosses files.

Run focused read-only checks when useful, such as tests, linters, format checks, type checks, or build validation. Do not run commands that publish, deploy, release, rewrite files, or change external state.

For general code quality, report only concrete risks with observable impact:

- incorrect behavior or unhandled edge cases
- duplicated logic likely to diverge
- unclear ownership or mixed responsibilities that cause change risk
- dependency direction or coupling that violates project architecture
- misleading names, unsafe assumptions, dead code, or stale comments
- missing tests for changed or contract-critical behavior

Do not enforce arbitrary function-size limits or demand abstractions without a demonstrated benefit.

## 4. Report findings

Lead with findings ordered by severity:

- Critical: data loss, security exposure, release blocker, or broad outage
- High: user-visible failure or direct spec violation
- Medium: limited correctness, maintainability, or test gap with plausible impact
- Low: small, concrete issue worth fixing

For each finding include:

```text
[Severity] Short title
Evidence: path:line
Spec: path:line
Impact: What fails or becomes risky
Fix: Smallest viable correction
```

Omit `Spec` for a general quality finding. Distinguish confirmed defects from unresolved questions. Do not report a finding without file-level evidence.

End with:

- checks run and their results
- remaining validation gaps
- a brief compliance summary

If there are no findings, say so directly and still list validation gaps.
