# Approved Skill Releases

This directory is the immutable release archive for vetted Harrow & Vale skill versions.

## Current archive

| Skill | Versions | Purpose |
|---|---|---|
| `term-sheet-review` | `v1.0.0`, `v1.1.0` | Frozen skill instructions, references, evaluation evidence, rationale, and changelog. |

The current installable plugin lives at `plugins/term-sheet-review-plugin/` and is registered by the root `.claude-plugin/marketplace.json`. Do not install directly from this archive.

## Rule

Do not edit an approved version folder in place. Proposed changes belong in the active plugin and evaluation harness; after review, create a new semantic-version snapshot and update `releases/term-sheet-review/CHANGELOG.md`.

See `CONTRIBUTING.md` for the approval and release process.