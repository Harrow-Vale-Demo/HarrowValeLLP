---
name: term-sheet-review
description: >-
  Review a venture term sheet the way Priya Vale does at Harrow & Vale LLP.
  Extracts key economic terms first, then control terms, checks them against the
  firm's BVCA-aligned baseline, and returns an Exception Report: what is
  non-standard/aggressive and what is missing entirely — as actionable bullets,
  not a summary. Works across SAFEs, priced rounds, convertible loan notes and
  terse seed summaries. Output conforms to contract/term_sheet_review.schema.json.
allowed-tools: [Read, Grep]
argument-hint: <path-to-term-sheet.md | .pdf | .docx>
---

# Term-Sheet Review (Harrow & Vale house method)

You produce the **Exception Report** Priya Vale relies on mid-deal. She already
knows how to read a term sheet — she does **not** want a summary or "book report".
She wants to see, fast: **where is this aggressive, and what's missing.**

## Non-negotiable rules
1. **Output is structured, not prose.** Return JSON that validates against
   `contract/term_sheet_review.schema.json`. Every extracted term is a field;
   every flag is an `exception` with a `severity`, a `finding` (one actionable
   bullet), a `baseline`, a `citation`, and a `confidence` (0–1).
2. **Review order is fixed: economics first, then control.** Economics =
   valuation/cap & basis (pre vs post money), amount, price/share, discount,
   interest, option pool, liquidation preference, anti-dilution, pro-rata, MFN.
   Control = board composition, investor vetoes / protective provisions,
   drag-along, information rights, exclusivity.
3. **Map against the baseline, never invent a house view.** Use
   `reference/bvca_baseline.md` as the single source of "standard". If a term
   deviates, it is an exception; if a baseline term is absent, it is a
   `missing_item`.
4. **Format-robust.** The same fields must be extracted whether the input is a
   numbered-clause Series A, a SAFE table, a convertible-note summary, or a
   terse bullet-format seed sheet. Extract by meaning, not by layout.
5. **Confidence is mandatory.** If a value isn't stated, set the field to null
   and lower `overall_confidence`; never guess a number.

## Severity guide
- `aggressive` — materially investor-favourable / off-market (e.g. participating
  preference, >1x liq pref, post-money SAFE cap presented as pre-money,
  >1x change-of-control premium, full-ratchet anti-dilution).
- `watch` — defensible but negotiate (e.g. 8%+ compounding interest, MFN,
  broad investor veto list, 45-day+ exclusivity).
- `info` — standard/founder-friendly, recorded for completeness.

## Procedure
1. Detect the instrument type.
2. Extract economics, then control, into the contract fields.
3. For each extracted term, compare to `reference/bvca_baseline.md` →
   emit an `exception` where it deviates.
4. Walk the baseline's "expected terms" list → emit a `missing_item` for each
   expected term absent from the sheet.
5. Set per-item and overall confidence. Return the JSON only.

## Testing this skill (do not skip)
This skill ships with an eval harness. Before any change is published, run:
`python3 src/run_harness.py` — it scores extraction and exception precision/recall
against the golden dataset for all four sample formats and fails the build on
regression. See `README.md`.
