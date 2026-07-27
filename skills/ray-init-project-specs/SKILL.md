---
name: ray-init-project-specs
description: Initialize or repair a project's source-of-truth specifications, including AGENTS.md, a README index, overview, and domain specs. Use when bootstrapping project documentation, adding a spec-driven agent contract, or repairing an incomplete spec system.
---

# Initialize Project Specs

Set up a concise specification contract that agents can follow before and after code changes. Use the bundled assets as structure, then adapt them to the project.

## 1. Inspect before writing

1. Read existing repository instructions, starting with `AGENTS.md` when present.
2. Read the root `README.md` and existing design, architecture, and specification documents.
3. Inspect the top-level tree, manifests, build files, and primary source directories.
4. Identify the product, supported platforms, shared infrastructure, feature domains, composition points, and external systems from evidence.
5. Check the working tree and preserve unrelated changes.

Do not infer detailed behavior that code or user context does not establish. Mark unknown decisions as WIP. Ask the user when an unresolved domain boundary or product decision would materially change the document structure.

## 2. Install the contract

Create or merge root `AGENTS.md` using `assets/AGENTS.md`.

- Preserve existing project-specific and stricter instructions.
- Remove duplicate or contradictory rules.
- Keep `spec/*.md` as the behavioral source of truth.
- Keep the root `README.md` as the index of every spec document.
- Use the standard filename `AGENTS.md`, not `.AGENTS.md`.

Do not overwrite an existing instruction file wholesale. Merge the contract into its current structure.

## 3. Build the spec map

Update the root `README.md` without discarding existing setup or usage content. Add:

- a concise top-level directory map
- a Spec Index table containing every `spec/*.md` file exactly once
- a one-line description of each document's ownership

Create `spec/overview.md` from `assets/spec-overview.md`. Keep only product-wide content there:

- product and platform context
- screen, service, or entry-point composition
- architecture and dependency direction
- cross-domain wiring

Create one document per domain from `assets/spec-domain.md`. A domain owns one cohesive product capability. Put reusable cross-cutting infrastructure in `spec/foundation.md` when the project has enough shared infrastructure to justify it.

Do not split one domain across documents. Do not create speculative domains only to mirror folders. Prefer a small initial map that can grow.

## 4. Populate from evidence

For each document:

- describe current behavior, not aspirations
- label planned or incomplete work as WIP
- name interests and non-interests explicitly
- describe modules and observable behavior concisely
- add implementation trees only for platforms or services that exist
- add a dated initialization entry to Revision History

Replace every template placeholder. Do not copy project-specific examples from another repository.

## 5. Validate

Re-read `AGENTS.md`, `README.md`, and every new or changed spec after editing. Verify:

- every spec is indexed in `README.md`
- every index entry points to an existing file
- domain ownership does not overlap
- overview and domain documents do not duplicate details
- implementation trees match the repository
- current and WIP behavior are distinguishable
- no stale or contradictory text remains
- prose is concise and uses ASCII characters, except box-drawing glyphs in file trees
- the diff contains no unrelated changes

Report created and updated files, inferred domains, WIP items, and decisions that still need user confirmation.

## Assets

- `assets/AGENTS.md`: project instruction contract
- `assets/README-spec-index.md`: README sections to adapt or merge
- `assets/spec-overview.md`: project-wide specification shape
- `assets/spec-domain.md`: domain specification shape
