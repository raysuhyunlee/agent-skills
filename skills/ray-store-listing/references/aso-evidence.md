# ASO evidence routing

Use Astro's current tool schemas rather than remembered parameters.

1. Identify whether the user's actual app is tracked.
2. Match a published app by stable App Store ID before using product-specific data.
3. Use its tracked keywords and native popularity and difficulty metrics.
4. Inspect live search results and title patterns for every serious candidate.
5. Use rankings, suggestions, and competitor-keyword extraction only when the required
   tracked state exists.

For an unpublished app, do not borrow metrics from an adjacent tracked product. Create a
dedicated temporary app only after the user approves the proposed name, platform, stores,
and exact keyword set. Report persistent additions after making them.

If tracking is unavailable or not authorized, continue with read-only search and label
the unavailable metrics. Do not infer or substitute them.
