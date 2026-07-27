# Changelog — term-sheet-review

## v1.1.0 — 2026-07-25

### Added
- **Founder vesting schedule** extraction: duration, cliff, acceleration terms (single-trigger vs double-trigger). Standard baseline: 4 years / 1-year cliff / double-trigger. Flags deviations per Tom Harrow's requirements.
- **Legal fees & expenses** extraction: who pays, any cap on investor fees the company covers. Standard baseline: capped at £10k–£25k (early stage) or £25k–£50k (Series A). Flags uncapped or unusually high caps.

### Changed
- `SKILL.md` step 3 (Key Terms table): added two new rows for the above fields
- `references/market-standard-terms.md`: added baseline definitions for vesting and legal fees
- `references/instrument-applicability.md`: added applicability mapping for both fields across SAFE/priced/note instrument types

### Rationale
Tom Harrow explicitly listed 9 required extraction fields in the discovery call. v1.0.0 covered 7/9 (78%). This release adds the two missing fields to reach 9/9 (100%). See `v1.1.0-RATIONALE.md` for full details with quotes from the brief.

### Validation
Re-ran eval suite against all 4 sample term sheets. All correctly mark the new fields as "Not stated" (the sample docs don't contain vesting or fee info — realistic, as these often live in separate documents). No regressions.

---

## v1.0.0 — 2026-07-22
- Initial release. Extracts key economic terms from a term sheet, checks against `dd-checklist.md` (categories 1–9), flags unusual clauses against `market-standard-terms.md`, and runs a reconciliation check when a data room is supplied.
- Validated against 4 sample term sheets (priced round, SAFE, convertible loan note, bullet-format seed round) — see `eval/eval-results.md` in the source skill for the regression baseline.
- Approved by: Tom Harrow (process), Priya Vale (substantive DD accuracy).
