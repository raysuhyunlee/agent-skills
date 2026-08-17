# App Review Notes

Prepare an evidence-backed App Review package from the shipping project. Produce a
paste-ready Notes draft and a practical recording script. Never present an inference as
a tested fact.

## 1. Resolve the shipping app

Read repository instructions first. Inspect the shipping target rather than deprecated,
demo, or reference targets. Establish:

- product name, bundle ID, platforms, version, and business model
- specifications, README files, release documents, and existing store metadata
- onboarding, account creation, login, logout, and in-app account deletion
- primary user flow and the features that deliver the main value
- subscriptions, in-app purchases, paid content, and restore-purchase behavior
- user-generated content and its reporting, blocking, and moderation controls
- permission prompts, entitlements, privacy manifests, and sensitive capabilities
- supported locales, storefront conditions, feature flags, and regional restrictions
- external SDKs, APIs, authentication, payments, analytics, advertising, AI, storage,
  content, and data providers
- regulated functions and protected third-party brands, content, data, or services

Use source code, configuration, dependency manifests, product specifications, and
committed test records as evidence. Treat build destinations and deployment targets as
configuration, not proof of physical-device testing.

State which findings are observed, inferred, or unknown. If the repository contains
conflicting evidence, report the conflict instead of choosing silently.

## 2. Build the review evidence matrix

Cover all seven submission areas:

1. A physical-device screen recording on the latest public operating system. It starts
   from launching the app and demonstrates the typical path through its core features.
2. The exact physical device models and operating system versions used for testing.
3. The app's purpose, target audience, problem, and user value.
4. Setup and access instructions, including review login details or sample files when
   required.
5. External services, tools, and platforms used for core functionality.
6. Regional differences, or an explicit confirmation that behavior is consistent.
7. Authorization evidence for regulated services or protected third-party material,
   when applicable.

For the recording, explicitly determine whether the app includes:

- registration, login, and in-app account deletion
- purchases, subscriptions, paid access, and restore purchases
- user-generated content, reporting, and blocking
- prompts for location, contacts, camera, microphone, photos, Bluetooth, health data,
  tracking, or other sensitive data and device capabilities

Do not infer any of these facts:

- device models or operating system versions actually tested
- successful purchases, account deletion, report handling, or regional availability
- working reviewer credentials
- legal authorization, licenses, or rights to protected material
- production availability of an external service

Ask concise, grouped questions for missing facts only after inspecting the project.
Continue by producing a provisional draft with conspicuous placeholders when answers
are unavailable.

## 3. Protect credentials and private information

Never write passwords, access codes, API keys, private document links, or other secrets
into a tracked repository file. Use placeholders such as `[ENTER IN APP STORE CONNECT]`
in saved drafts. Recommend entering reviewer credentials in App Store Connect's
dedicated sign-in fields when available.

If a recording or sample file needs a link, require a stable link that App Review can
open without requesting access. Mention a separate access code only when necessary.
Exclude personal notifications, real customer data, private account details, and
unrelated device content from the recording.

## 4. Draft the Notes field

Write the paste-ready draft in English unless the user requests another language. Use
plain text that survives pasting into App Store Connect.

Read [review-package.md](review-package.md) for the output contract,
writing rubric, and length validation. Adapt the structure to the app without weakening
evidence boundaries. Do not leave placeholders in a final submission.

## 5. Create the physical-device recording plan

Require a physical device running the latest public OS available at recording time.
Verify the current version through an official platform source rather than memory.
Begin on the device Home Screen and show the reviewer tapping the app icon. Plan the
normal user journey first, followed by every applicable review-sensitive flow.

Create a shot list with:

- sequence number and approximate duration
- starting app state and test account
- exact taps, screens, and expected result
- the review requirement demonstrated
- reset or seed steps needed before recording

Include applicable sequences for:

1. first launch, onboarding, and permission prompts
2. registration and login
3. the shortest representative path through the core value
4. paid content, purchase or subscription presentation, and restore access
5. creating user content, reporting content, and blocking a user
6. account deletion from inside the app
7. region-specific behavior

Use a dedicated review account and harmless sample data. Prepare permission state,
subscription state, region, network access, and seeded content before recording. Keep
text readable, touch actions deliberate, and the flow free of debug overlays, crashes,
loading stalls, notifications, and unrelated detours.

Do not tell the user to perform a real production charge solely for the video. Use the
app's appropriate review or sandbox purchase environment. If mutually exclusive states
cannot be demonstrated clearly in one recording, propose the smallest clearly labeled
set of recordings and explain why.

Finish with a preflight checklist:

- physical device model and exact OS version are visible or documented
- the recording starts with app launch
- the typical core flow is complete
- every applicable sensitive flow is shown
- reviewer credentials and sample data work
- links open without an access request
- no private data or secrets are visible
- the Notes statements match what the video and submitted build demonstrate

## 6. Deliver the result

Return:

1. a concise project findings summary with evidence paths
2. unresolved questions and submission blockers
3. the paste-ready Notes draft in one plain-text block
4. the ordered physical-device recording shot list
5. the final preflight checklist

Write files only when the user requests saved artifacts or the repository already
defines a review-document location. Keep secrets as placeholders in every saved file.
Do not upload the recording, change App Store Connect, or submit the app unless the user
explicitly asks.
