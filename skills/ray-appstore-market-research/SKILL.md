---
name: ray-appstore-market-research
description: Research an App Store or Google Play keyword with mcp-appstore and Astro MCP, covering ranked and similar apps, keyword demand and difficulty, competitor positioning, localized review themes, target customer segments, jobs-to-be-done, unmet needs, and product opportunities. Use for app-market research, ASO keyword validation, competitor analysis, review mining, customer-needs analysis, market-gap discovery, or questions about what users searching a particular app keyword want.
---

# App Store Market Research

Use `mcp-appstore` and Astro MCP as already available. Produce an evidence-backed market report, not a list of search results.

## 1. Fix the research scope

Determine and state:

- seed keyword and close variants
- platform: iOS, Android, or both
- store country and result language
- competitor and review sample sizes
- whether the user has an app to compare against

Treat every keyword score, ranking, rating, price, and review as store-, language-, platform-, and time-specific. Never merge metrics from different stores or platforms into one value.

If details are missing, infer them from the request or project context. Otherwise default to iOS, the product's primary market, 10-20 discovered apps, 5-8 deeply analyzed competitors, and about 100 reviews per competitor. State every default used.

Astro covers Apple App Store research. Use `mcp-appstore` for Android and for cross-platform comparison.

## 2. Discover the market independently

Run both discovery paths for iOS:

1. Use mcp-appstore `search_app` and `analyze_top_keywords`.
2. Use Astro `search_app_store`.
3. Deduplicate apps by store ID or package ID.
4. Note apps found by both sources, rank differences, and source-specific omissions.

For Android, use mcp-appstore `search_app` and `analyze_top_keywords`.

Inspect enough results to capture:

- direct substitutes solving the same job
- category leaders with strong distribution
- niche apps aimed at a specific audience or situation
- adjacent substitutes users could choose instead

Shortlist 5-8 competitors based on relevance, rank, rating volume, positioning diversity, and useful review coverage. Do not select only the largest apps.

Use mcp-appstore `get_app_details` for the shortlist. Call `get_pricing_details`, `get_similar_apps`, `get_developer_info`, or `get_version_history` only when the result will answer a concrete pricing, adjacency, portfolio, or maintenance question. Use Astro `get_app_ratings` when localized rating evidence or rating history materially improves the comparison.

## 3. Analyze keyword demand

Use mcp-appstore `get_keyword_scores` for the seed keyword and the strongest discovered variants. Use `analyze_top_keywords` to identify recurring title, subtitle, description, category, and positioning language among ranking apps.

Build candidates from:

- category and head terms
- problems and desired outcomes
- features and workflows
- audiences and professions
- situations, locations, and occasions
- synonyms and natural local-language phrasing
- competitor positioning and review vocabulary

For iOS, use Astro to strengthen the analysis:

- Use `list_apps` to determine whether the user's actual app is already tracked.
- Never use a different tracked app as a proxy for the user's product, even when its category, audience, language, or job appears adjacent. Do not attribute that app's keyword popularity, difficulty, ranking, suggestions, or competitor extraction to the target product.
- If the user's app is already published, match it by stable App Store ID before using its tracked data.
- If the user's product is unpublished and the user asks to analyze or track it with Astro, create a dedicated temporary app with `add_app` using a clear name such as `[Product] (concept)`, then add the research keyword set with `add_keywords`.
  - Treat an explicit request to analyze the unpublished product with Astro, create a temporary app, or track its keywords as authorization for these additions.
  - For a generic one-off market report that does not request Astro tracking, state the proposed temporary app name, platform, store, and keywords and obtain authorization before changing persistent Astro state.
  - Use the product's intended platform. Default to `iphone` only when project context indicates an iPhone app or the user leaves the platform unspecified.
  - Add the seed keyword plus the strongest feature, problem, audience, situation, synonym, and long-tail variants. Avoid speculative or unrelated keywords added only to increase the sample.
- After resolving or creating the correct app, use `get_app_keywords` for its tracked metrics.
- Use `search_rankings` for tracked keywords in the target store.
- Use `extract_competitors_keywords` when the seed keyword is already tracked.
- Use `get_keyword_suggestions` when a relevant tracked app exists.

Do not call Astro `add_app` or `add_keywords` merely to fill missing metrics when the target is not the user's product or authorization is absent. Report the temporary app ID, exact keywords added, and store after making authorized tracking changes. Never call `remove_keywords` without listing the exact deletions and receiving explicit confirmation.

If an Astro analysis requires untracked state, report which step was unavailable and continue with read-only Astro search plus mcp-appstore scores. Do not invent missing Astro metrics.

For every recommended keyword, report the original metrics returned by the tools and assess:

- relevance to the promised product
- search intent
- popularity or demand
- ranking difficulty or competitiveness
- competitor coverage
- fit for a head-term or long-tail strategy

Keep tool-native scores in their original scales. Do not manufacture a combined numeric score unless its formula and normalization are shown. Prefer a qualitative priority of high, medium, or low with a short rationale.

## 4. Analyze competitor reviews

Use mcp-appstore `analyze_reviews` for each shortlisted app in the target country and language. Prefer recent reviews for current product problems. Add a helpfulness-sorted sample when durable or high-impact themes need confirmation. Use `fetch_reviews` only when raw examples, exact wording, rating-level segmentation, or verification of an aggregate theme is necessary.

Extract:

- reasons users choose and keep the app
- moments that trigger use
- praised outcomes and must-have features
- recurring failures, friction, and reliability issues
- missing features and explicit requests
- pricing, subscription, trial, ad, and paywall reactions
- trust, privacy, safety, accuracy, and localization concerns
- switching triggers and comparisons with alternatives

Record the sample size, store, language, sort order, and collection date. Distinguish:

- recurring theme: repeated across several reviews or apps
- emerging signal: repeated but limited to one app or small sample
- anecdote: isolated review; do not generalize

Never fabricate quotations. Quote only text returned by `fetch_reviews`, keep quotes short, and identify the app and rating. Paraphrase when exact wording is unnecessary.

Avoid treating review frequency as market share. Reviews are a self-selected sample and store APIs may return fewer items than requested.

## 5. Infer customers and unmet needs

Derive customer segments from observed jobs, contexts, constraints, and review language rather than demographics alone.

For each segment, describe:

- context and trigger
- job-to-be-done
- desired outcome
- current workaround or competitor choice
- pain points and anxieties
- decision criteria
- willingness-to-pay signal, if any
- evidence and confidence

Separate evidence from inference:

- **Observed:** directly supported by metadata, rankings, keyword metrics, or reviews.
- **Inferred:** a reasoned interpretation of observed evidence.
- **Unknown:** important question the available data cannot answer.

Identify opportunities where demand evidence overlaps a repeated unmet need and weak competitor execution. Rank opportunities qualitatively using frequency, severity, demand, competitive supply, differentiation, feasibility, and monetization signal. Do not equate a popular keyword with a validated product need by itself.

## 6. Cross-check before concluding

Verify that:

- every analyzed app actually ranks for, targets, or closely substitutes the seed job
- every product-specific Astro metric belongs to the user's actual app or its dedicated temporary app, never an adjacent proxy
- keyword metrics use the requested store and platform
- review language matches the requested market
- app IDs are not mixed between iOS and Android
- current facts are not inferred from descriptions alone
- conclusions name the supporting apps, keywords, or review themes
- conflicts between mcp-appstore and Astro are disclosed rather than silently resolved

If data is sparse, narrow the claims and lower confidence. Recommend interviews, surveys, ad tests, or landing-page tests for questions store data cannot answer.

## 7. Report

Use this structure unless the user requests another format:

```markdown
# Market Research: [keyword]

## Scope and evidence
- Platform / store / language / collected at
- Sources and sample sizes
- Defaults, gaps, and limitations

## Executive summary
- Market shape
- Strongest demand signal
- Most important unmet need
- Best differentiated opportunity

## Competitor landscape
| App | Platform | Rank/source | Rating volume | Price/model | Positioning | Strengths | Gaps |

## Keyword analysis
| Keyword | Store/platform | Popularity | Difficulty | Intent | Competitor coverage | Priority | Rationale |

## Review findings
| Theme | Sentiment | Frequency class | Apps | User impact | Evidence |

## Target customers and jobs
| Segment | Trigger | Job-to-be-done | Pain | Decision criteria | Evidence | Confidence |

## Opportunity map
| Opportunity | Demand evidence | Need evidence | Competitive gap | Priority | Risks |

## Recommendations
1. Product and positioning
2. Keyword portfolio: head terms and long-tail terms
3. Validation experiments

## Unknowns
- Questions not answerable from store data
```

Lead with conclusions, then show the evidence. Include app names and stable IDs so the research can be reproduced. Keep facts, interpretations, and recommendations visibly distinct.
