---
name: ray-store-positioning
description: Derive, confirm, and maintain a shared app-store positioning brief from product specifications, market research, competitor evidence, and user needs. Use when store listings and screenshots need a common set of core values, when creating multiple store-marketing assets together, when positioning is missing or stale, or when product, audience, pricing, or differentiation has materially changed.
---

# Store Positioning

Create the single source of truth for store listings, screenshot captions, and other
store-marketing assets. Finish with an approved positioning brief, not finished
store copy.

## 1. Resolve the product and evidence

Inspect before asking:

- the shipping product and platforms, excluding deprecated or reference implementations
- product, design, pricing, monetization, and launch specifications
- existing market research, ASO research, competitor analysis, and review findings
- existing store metadata, screenshot captions, and positioning documents
- supported locales and primary markets

Separate the evidence into:

- **Observed:** stated in product specifications or supported by market, keyword,
  competitor, or review evidence
- **Inferred:** a reasoned interpretation of the observed evidence
- **Unknown:** important claims that cannot yet be supported

Never turn a planned feature into a current promise. Treat keyword demand as evidence
of search behavior, not proof that the product satisfies the need.

## 2. Reuse or invalidate the shared brief

Follow an existing repository layout. Otherwise use:

```text
design/store/positioning.md
```

Reuse an approved brief when its product, audience, business model, and evidence still
match the current repository. Treat it as stale when any of these materially changed:

- the primary job or target customer
- a capability used as a core value or proof point
- pricing, monetization, privacy, offline behavior, or platform support
- competitor conditions or market evidence behind the differentiation

Report why the brief is reusable or stale. Do not silently overwrite an approved brief.

## 3. Derive the positioning

Identify:

1. the primary customer and the moment that triggers the search
2. the job the customer is trying to complete
3. the desired outcome and emotional payoff
4. the alternatives or workarounds they would otherwise choose
5. the product's credible differentiation
6. the proof available in the actual product
7. the claims the store assets must avoid

Reduce these findings to exactly three ordered core values:

1. **Primary value:** the single reason the product deserves to exist
2. **Differentiating value:** the strongest credible reason to choose it over substitutes
3. **Proof value:** the visible moment that shows the promised outcome was achieved

Write each value as a user outcome, not a feature label. Attach one or more proof
points and source references to every value. A capability without a user consequence
is not a core value.

## 4. Present directions and get confirmation

When more than one credible positioning exists, present two or three directions.
For each direction show:

- primary audience and trigger
- one-sentence positioning statement
- the three ordered core values
- strongest evidence
- tradeoff or audience excluded by the direction

Recommend one direction and explain why. Stop and ask the user to approve or revise
the positioning before writing or updating the shared brief. Do not begin store
listing copy, screenshot captions, or localization before this approval.

If only one direction is credible, still present it for explicit confirmation.

## 5. Write the approved brief

Use this contract so downstream skills can consume the file without re-deriving the
strategy:

```markdown
---
status: approved
approved_at: YYYY-MM-DD
primary_market: en-US
---

# Store Positioning

## Product snapshot
- Product:
- Shipping platforms:
- Business model:
- Supported locales:

## Target customer
- Primary segment:
- Trigger:
- Job to be done:
- Desired outcome:
- Alternatives:

## Positioning statement
[For audience, this product creates outcome through differentiation.]

## Message hierarchy
### 1. Primary value
- Outcome:
- Proof:
- Evidence:

### 2. Differentiating value
- Outcome:
- Proof:
- Evidence:

### 3. Proof value
- Outcome:
- Proof:
- Evidence:

## Vocabulary
- Prefer:
- Avoid:

## Claim boundaries
- Supported claims:
- Unsupported or risky claims:

## Sources
- [repository paths, store evidence, and collection dates]
```

Keep source paths repository-relative. Preserve unresolved unknowns instead of filling
them with marketing assumptions.

## 6. Hand off

Report the approved direction, file path, evidence limitations, and any event that
should trigger revalidation. Tell downstream work to:

- use `$ray-store-listing` for ASO-backed metadata
- use `$ray-store-screenshots` for screen selection, captions, and capture

When both are requested, reuse this one approved brief for both workflows.
