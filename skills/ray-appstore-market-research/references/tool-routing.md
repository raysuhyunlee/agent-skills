# Store research tool routing

Use the tools that are currently available and inspect their live schemas rather than
assuming remembered parameters.

## Discovery and metadata

- For iOS, compare Astro App Store search with mcp-appstore search when both are
  available.
- For Android, use mcp-appstore discovery and keyword analysis.
- Fetch details for shortlisted apps. Request pricing, similar apps, developer portfolio,
  version history, or rating history only to answer a concrete research question.

## Keyword evidence

Use mcp-appstore keyword scores and top-keyword analysis for demand and recurring
metadata language. Use Astro tracked metrics only for the user's actual product:

1. match a published product by stable App Store ID
2. never borrow metrics from an adjacent tracked app
3. for an unpublished product, create temporary tracked state only when the user
   explicitly requests tracking or approves the proposed app name, platform, store, and
   keyword set
4. report persistent additions after making them
5. require explicit confirmation before deleting tracked keywords

When tracking is unavailable or unauthorized, continue with read-only search and other
native scores. Report the missing step rather than inventing metrics.

## Reviews

Use aggregate review analysis for broad themes. Fetch raw reviews only for exact wording,
rating segmentation, or verification. Request recent and helpful samples according to
the research question rather than treating one sorting mode as comprehensive.
