# Project Instructions

- Follow these instructions for every edit in this repository.

## Core Contract

- Markdown documents under `spec/` are the source of truth for project behavior and architecture.
- Root `README.md` contains the index of every specification document.
- When code and specifications disagree, confirm the intended behavior before changing the contract.

## Read Before Editing

- Read root `README.md`.
- Read every specification document related to the task.
- Do not rely on memory when the specifications define the behavior.

## Update After Editing

- Re-read related documents after every meaningful change.
- Update related documents for new features, new domains, or architecture changes.
- Do not update specifications for small refactors, bug fixes, or copy changes unless the documented behavior changed.
- Remove stale or contradictory text immediately.
- Create a domain document when a new domain is introduced.

## Document Shape

Use this section order for domain documents:

1. Status: recent changes and WIP items
2. Domain Definition: interests and non-interests
3. Details: modules and behavior
4. Implementation: file trees and roles for each platform or service
5. Revision History: dated one-line entries

## Style

- Keep documentation and code concise, current, and readable.
- Do not duplicate behavior descriptions across documents.
- Prefer direct bullets with explicit names.
- Follow the document shape. Explain when a different shape is necessary.
- Use ASCII characters in prose. Box-drawing glyphs are allowed in file trees.

## User Preferences

- Record durable workflow or behavior preferences in this file.
- Ask before making a change that would break this contract.
- Ask when missing information would materially change the result.
