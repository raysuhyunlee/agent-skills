---
name: ray-store-listing
description: Create and localize ASO-backed App Store listing metadata from an approved shared positioning brief, with separate mandatory user approvals for app-name candidates and keyword portfolios before drafting the remaining metadata. Use when creating, refreshing, optimizing, or localizing an app name, subtitle, keywords, promotional text, description, or complete App Store listing.
---

# Store Listing

Create evidence-backed App Store metadata that expresses the product's approved core
values. App-name approval and keyword approval are separate hard gates.

## 1. Resolve the scope

Inspect before asking:

- the shipping app, platform, App Store ID or bundle ID, and release version
- supported locales and intended store countries from project localization resources
- the primary locale and primary market
- existing canonical metadata, App Store Connect records, and store limits
- product specifications, market research, and the shared positioning brief

State the resolved app, markets, locales, existing metadata layout, and intended output
paths. Never infer supported locales from an assumed list.

Use an existing metadata layout. For App Store Connect projects, prefer the canonical
`asc metadata` layout:

```text
metadata/
├── app-info/<locale>.json             # name, subtitle, privacy fields
└── version/<version>/<locale>.json     # description, keywords, promotionalText, etc.
```

Pull existing metadata before editing when App Store Connect access and an app record
are available. Drafting local files does not authorize pushing them remotely.

## 2. Require approved positioning

Look for `design/store/positioning.md` or the repository's equivalent. Verify that it:

- has `status: approved`
- matches the shipping product, audience, business model, and current capabilities
- contains the three ordered values: primary, differentiating, and proof
- cites evidence and defines unsupported claims

If it is missing or stale, use `$ray-store-positioning` first when available. Otherwise
follow that artifact contract, present the positioning for confirmation, and stop.
Do not invent a listing-only positioning or let existing metadata override the approved
brief without calling out the conflict.

## 3. Build current ASO evidence

Use Astro for Apple App Store name and keyword decisions:

1. Use `list_apps` to identify whether the user's actual app is tracked.
2. Match a published app by stable App Store ID before using product-specific data.
3. Use `get_app_keywords` for its tracked keywords and native metrics.
4. Use `search_app_store` to inspect search results and title patterns for each serious
   candidate term in the target store.
5. Use `search_rankings`, `get_keyword_suggestions`, and
   `extract_competitors_keywords` when the required tracked state exists.

For an unpublished app, never borrow metrics from an adjacent tracked app. To obtain
native popularity and difficulty, create a dedicated temporary Astro app and add the
serious candidate keywords after the user authorizes that persistent change. Before
making it, state the proposed temporary app name, platform, stores, and exact keyword
set. Then call `get_app_keywords` and use the returned popularity and difficulty in the
name and keyword decisions. Continue with read-only Astro search, and label those
metrics unavailable, only when the change is not authorized or Astro cannot track the
requested market.

Keep every metric attached to its store, platform, locale, and collection date. Preserve
Astro's native popularity and difficulty scales. Do not manufacture a combined score.
Assess each term by:

- semantic relevance to the approved promise
- search intent
- popularity
- difficulty
- competitor coverage
- the product's credible ability to convert that searcher

Use current store or canonical tooling limits when validating fields. Do not rely on a
remembered limit when a validator is available.

## 4. Gate 1: app-name selection

Generate three to five app-name candidates for the primary locale. Include meaningful
strategic variation such as:

- brand-led
- category or head-term-led
- differentiated outcome-led

Reject names that overpromise, imitate a competitor, read like keyword stuffing, or
conflict with the approved positioning. For every candidate show:

| Candidate | Length | Target terms | Astro evidence | Positioning fit | Tradeoff |
|---|---:|---|---|---|---|

Recommend one candidate with a concise reason. Then stop.

Do not propose keyword-field portfolios, write remaining metadata, localize the name,
or edit metadata files until the user explicitly approves an app name. Revise and
re-present candidates as needed.

## 5. Gate 2: keyword selection

After app-name approval, rerun or reinterpret keyword evidence in the context of the
confirmed name. Avoid wasting indexed fields on unnecessary duplication and use the
confirmed name as part of the allocation strategy.

Present three keyword portfolios:

- **Balanced:** strongest mix of demand, relevance, and attainability
- **Reach:** more competitive, higher-demand terms
- **Attainable:** lower-difficulty, high-intent terms and long tails

For each portfolio show:

- the exact proposed keyword field
- length under the current store rules
- included and deliberately excluded terms
- each important term's Astro popularity, difficulty, store, and intent
- overlap with the confirmed name and planned subtitle
- expected strength and principal risk

Recommend one portfolio. Then stop again.

Do not write keyword files, draft the subtitle or description, localize metadata, or
change Astro tracking until the user explicitly approves a keyword portfolio. App-name
approval never implies keyword approval.

## 6. Draft the remaining source metadata

After both gates pass, write the source locale:

- **Subtitle:** reinforce the primary or differentiating value without mechanically
  repeating the name
- **Promotional text:** communicate the strongest timely or conversion-relevant promise
- **Description:** lead with the customer outcome, then explain differentiators and
  proof in message-hierarchy order
- **Keywords:** use the exact approved portfolio
- **What's New:** write only when release-specific changes are in scope and evidenced
- **URLs and privacy fields:** preserve verified existing values; never invent them

Prefer concrete verbs, recognizable situations, and verifiable outcomes. Do not lead
with a feature inventory. Preserve intentional user-authored marketing voice, including
subjective superlatives such as "easiest," unless the user asks to change it or it
creates a specific policy or compliance risk. Distinguish ordinary promotional
language from objective claims: require evidence for awards, rankings, quantified
outcomes, accuracy, privacy, offline behavior, pricing, and compatibility.

Show the completed source-locale draft before writing other locales when the user has
not already approved the full copy.

## 7. Localize by market

Treat each locale as a separate market, not a translation slot:

- reuse terminology established in the app UI
- transcreate the value proposition into native store language
- research local search phrasing with Astro in the corresponding store
- never translate a keyword portfolio literally
- validate the localized app name and keyword allocation independently
- preserve the same claims and evidence boundaries across locales

Batch app-name candidates across locales if helpful, but keep the app-name approval
gate separate from the keyword approval gate. Obtain explicit approval for localized
names and then for localized keyword portfolios before writing those fields.

## 8. Write and validate

Preserve unrelated existing metadata fields. Write only approved content into the
repository's canonical files. Validate:

- every required locale exists
- field lengths and formats pass the current store validator
- app-info and version fields are in the correct files
- the approved name and keyword portfolio are reproduced exactly
- no locale contains untranslated source copy or UI terminology drift
- repeated claims remain supported by the positioning brief

When `asc` is available, run `asc metadata validate --dir "./metadata"` after writing.
Use a dry run before any requested remote push. Never push, apply, or otherwise mutate
App Store Connect unless the user explicitly asks.

## 9. Report

Report:

- the approved app name and why it won
- the approved keyword portfolio with Astro evidence date and market
- remaining source and localized metadata
- files written and validation results
- unavailable metrics, wording needing native review, and unsupported claims omitted
- whether anything was changed in Astro or App Store Connect
