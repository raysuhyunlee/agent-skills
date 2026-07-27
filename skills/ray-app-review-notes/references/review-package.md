# App Review package contract

## Notes writing rubric

- use concise, complete sentences and plain text
- address the reviewer politely and directly
- lead with verified facts and exact navigation paths
- identify non-applicable items explicitly
- avoid promotional hype, vague claims, and internal engineering jargon
- do not treat tests or build configuration as proof of physical-device testing
- avoid em dashes and middle dots so the saved text follows Ray's store-copy style

Verify the current Notes limit with App Store Connect tooling or official Apple
documentation. Validate UTF-8 bytes, not only visible characters. If no current limit can
be verified, target fewer than 4,000 UTF-8 bytes and disclose the assumption outside the
paste-ready text.

## Output contract

```text
Thank you for reviewing [App Name].

1. Demo Recording
[Accessible recording URL and essential access instruction.]

2. Tested Devices
[Verified physical device models and operating system versions.]

3. Purpose and Audience
[Purpose, target audience, problem, and value.]

4. Setup and Feature Access
[Concise navigation and reviewer access instructions.]

5. External Services
[Verified service names and roles.]

6. Regional Availability
[Verified differences or consistency.]

7. Authorization
[Relevant evidence and access instructions, or not applicable.]
```

Use placeholders in saved drafts when facts or secrets must be entered outside the
repository. Remove unresolved placeholders before final submission.
