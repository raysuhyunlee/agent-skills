---
name: ray-localize
description: Localize project content while preserving meaning, tone, structure, placeholders, terminology, and locale conventions. Use for UI strings, settings, paywalls, screenshots, store metadata, documentation, or translation updates.
---

# Localize

Create natural localized content, not literal translations. Treat repository instructions and product specifications as the source of truth.

## 1. Resolve the scope

1. Read repository instructions and the documentation index before editing.
2. Infer the requested content scope, source locale, target files, and target locales from the request and repository.
3. Inspect localization configuration and existing locale files. Do not assume paths, formats, or a fixed language list.
4. Ask the user only when the scope or source locale remains ambiguous after inspection.
5. Do not add keys or locales unless the request includes them.

Prefer the repository's canonical source file. If no source locale is explicit, infer it from configuration and existing content, then state the assumption before editing.

## 2. Gather context

Read only the context needed for the scope:

- product positioning, audience, and tone
- the scope's domain specification
- platform or store length limits
- terminology already established in nearby translations
- locale-specific file syntax and pluralization rules

Build the complete source-string set before translating. Preserve identifiers, interpolation tokens, markup, escape sequences, line breaks, and intentional whitespace.

## 3. Localize

For every locale:

- preserve meaning and product intent
- write naturally for the target market
- keep terminology consistent within the product
- retain placeholders and structural tokens exactly
- respect length, capitalization, punctuation, and script conventions
- preserve existing keys and unrelated content

## 4. Validate

Run the repository's localization validation, formatter, tests, or build when available. Also verify:

- every requested locale is present
- source and target keys match
- placeholders and format specifiers match
- JSON, strings, XML, YAML, or catalog syntax parses
- plural and gender forms remain valid
- no unrelated locale or domain changed

Spot-check at least one RTL locale, one CJK locale, and one Latin-script locale when those groups are in scope. Fix issues before reporting.

## 5. Report

Report the scope, source locale, completed locales, validation performed, and any text that still needs native review. Include only a few representative samples.
