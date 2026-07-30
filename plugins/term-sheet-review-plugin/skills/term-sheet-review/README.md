# term-sheet-review

A Claude Skill for Harrow & Vale LLP that produces a consistent, plain-English
first-pass review of a venture term sheet, checked against the firm's fixed
due-diligence checklist.

## What it does
- Classifies the instrument (SAFE / priced round / convertible loan note) from signals.
- Extracts key economic terms with a **source reference for every value** (never invents one).
- Flags deviations from standard, unusual clauses, and omissions — triaged 🔴 Review / 🟡 Note / ⚪ Omission — **described, not adjudicated** (the lawyer decides).
- Walks Priya's fixed checklist **item-by-item, every item**, with `PRESENT / MISSING / N/A`.
- With `--dd-room`, reconciles figures across documents (term sheet ↔ cap table ↔ articles).

## Design principle (Priya's rules)
1. Use the fixed checklist verbatim — never invent categories.
2. Never skip a step — every item gets an explicit status.
3. Never fabricate — absent terms are `Not stated`, not guessed.

## Usage

*Verified against Claude Code 2.1.140, 2026-07-30.*

Two invocation routes, either works:

**Plain English.** Claude selects the skill from what you ask for:

> Review this term sheet against our DD checklist: `NimbusRobotics-SAFE.pdf`

To include a data room, say so and give the folder:

> Review `GreenGrid-SeriesA.md` against our DD checklist, with the data room at `assets/source/data-room/`

**Namespaced slash.** Plugin skills are named `plugin:skill`:

```
/term-sheet-review:term-sheet-review <path-to-term-sheet>
/term-sheet-review:term-sheet-review <path-to-term-sheet> --dd-room <path-to-folder>
```

## Files
- `SKILL.md` — the skill definition and procedure.
- `reference/dd-checklist.md` — Priya's fixed checklist (ground truth).
- `reference/term-extraction.md` — fields to extract per instrument type.
- `reference/standard-terms.md` — the "standard" baseline for deviation flagging.
- `reference/output-template.md` — the fixed output structure.
- `examples/` — worked reviews across all four sample formats (the test set):
  - `review-safe-nimbus.md` — SAFE (table + prose)
  - `review-series-a-greengrid-ddroom.md` — priced round + full DD-room coverage & reconciliation
  - `review-note-anchorline.md` — convertible loan note
  - `review-seed-solace.md` — seed (terse bullets)

## Validation
Built test-driven against the four sample term sheets (deliberately different
formats). All four produce the same section structure, account for all 28
checklist items, and cite sources. The GreenGrid reconciliation figures were
independently verified (price/share, share counts, ownership % all check out).
