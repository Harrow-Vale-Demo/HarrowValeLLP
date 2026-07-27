# Mock source and fixture convention

All documents in this directory belong to the fictional Harrow & Vale hackathon scenario.

## Canonical inputs

- `source/term-sheets/` contains the four preferred term-sheet captures.
- `source/dd-checklist/harrow-vale-dd-checklist.md` is the preferred captured checklist.
- `source/data-room/greengrid-captable-and-articles.md` is the preferred combined GreenGrid corporate source.

When wording conflicts with an older normalized or annotated copy, these files take priority for extraction and evaluation.

## Supporting source documents

The remaining files in `source/data-room/` split the GreenGrid mock data room into individual document fixtures for checklist mapping and citation demonstrations.

## Legacy provenance

`legacy-raw-import/` preserves the original numbered import. It is retained for provenance and should not be treated as the working source set.

Harness goldens and versioned skill references are intentionally frozen beside the code or release that consumes them. Update those copies only through their evaluation/versioning process.