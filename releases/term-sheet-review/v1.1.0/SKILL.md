---
name: term-sheet-review
description: Review a venture term sheet (SAFE, priced equity round, or convertible loan note) against Harrow & Vale's standard due-diligence checklist. Extracts key economic terms, flags checklist omissions and unusual/non-market clauses, and produces a plain-English summary a lawyer can act on. Use whenever asked to review, check, or summarise a term sheet against the firm's DD checklist.
allowed-tools: Read, Glob
argument-hint: <path-to-term-sheet> [path-to-data-room-folder]
---

# Term Sheet Review

You are reviewing a term sheet the way a Harrow & Vale associate would before handing it to Priya Vale: extract the numbers, check it against the firm's fixed checklist, and surface anything unusual — in plain English, not legalese.

## Reference material (read these first, every time)

- `references/dd-checklist.md` — the firm's exact due-diligence checklist. This is a fixed authority. Never add, remove, rename, or reinterpret its categories. Every checklist-related statement in your output must map to an item on this list.
- `references/market-standard-terms.md` — baseline of what's market-standard per instrument type, used only to flag unusual clauses (this is separate from, and additional to, checklist compliance).
- `references/instrument-applicability.md` — tells you which checklist items are ever expected to appear *in a term sheet itself* versus which live only in the wider data room, so you don't wrongly flag a SAFE for "omitting" an employment-agreements summary.

## Procedure

1. **Read the target term sheet.** The path is given as the skill argument. If a second argument (a data-room folder) is given, or if other markdown files sit alongside the term sheet (e.g. a cap table, articles of association, contracts), read those too — they're used for the reconciliation check in step 6.

2. **Identify the instrument type from the document's own content** — SAFE, priced equity round (preferred shares), convertible loan note, or other. Do not infer it from the filename.

3. **Extract key economic terms** into a fixed table. Always include every row below; write "Not stated" rather than guessing or omitting a row:
   - Instrument type
   - Amount raised / principal
   - Pre-money / post-money valuation (or valuation cap)
   - Discount rate
   - Price per share (if stated or derivable)
   - Interest rate (convertible notes only; N/A otherwise)
   - Maturity date (convertible notes only; N/A otherwise)
   - Liquidation preference
   - Anti-dilution provision
   - Board composition
   - Protective provisions / investor consent items
   - Information rights
   - Pro-rata rights
   - Founder vesting schedule (duration, cliff, acceleration terms — single-trigger or double-trigger)
   - Legal fees & expenses (who pays, any cap on investor fees the company covers)
   - Conditions precedent / conditions to closing
   - Exclusivity period
   - Governing law

4. **Build the checklist matrix.** Go through every category in `references/dd-checklist.md` in order. For each item, using `references/instrument-applicability.md` to judge relevance, mark one of:
   - **Present** — addressed in the term sheet or confirmed present in a supplied data-room document.
   - **Flagged** — present, but the term deviates from `references/market-standard-terms.md`'s baseline (explain the deviation in one plain-English sentence).
   - **Omitted** — relevant to this instrument type and not found anywhere in the reviewed documents.
   - **Not applicable** — this checklist item doesn't apply to this instrument/document (per `instrument-applicability.md`), or it's an "expected data room" item that simply wasn't part of what you were given (state this distinction explicitly — don't conflate "not supplied to me" with "doesn't exist").

5. **Flag unusual clauses.** Independent of the checklist matrix, scan for clauses that deviate from `references/market-standard-terms.md` even if nothing is technically "omitted" — e.g. an above-market change-of-control premium, an MFN clause, a missing maturity date on a convertible note, non-standard governing law. For each flag, give a one-line plain-English explanation of *why it matters* to the deal, not just that it's unusual.

6. **Reconciliation check (only if supporting data-room documents were supplied).** Cross-check headline numbers — valuation, share counts, ownership percentages, protective provisions — against any cap table or Articles of Association found. Flag any mismatch explicitly; state clearly if everything reconciles.

7. **Output**, in this exact order and shape every time (this consistency matters more than any individual wording choice):
   1. One-line instrument identification (type, company, investor, date).
   2. **Key Terms** table (from step 3).
   3. **Checklist Review** — the matrix from step 4, grouped under the checklist's own numbered section headings, only listing items that are Flagged or Omitted in full detail (Present/N/A items can be summarised in one line each to keep the output scannable).
   4. **Unusual Clauses** — bullet list from step 5, each with its plain-English "why it matters."
   5. **Reconciliation** — only included if step 6 ran; state pass/fail and detail per any mismatch.
   6. **Summary for Reviewer** — 3–5 sentences a lawyer could act on immediately: what's standard, what needs a decision, what's missing before this can close.

## Ground rules

- Never invent a checklist category. If something seems worth flagging but isn't covered by the fixed checklist, put it under "Unusual Clauses," not the checklist matrix.
- Keep the output shape identical regardless of the term sheet's own formatting style (numbered-clause, dense prose, or terse bullets) — the source document's structure should not leak into the review's structure.
- Write for a lawyer, not a layperson, but avoid restating legal jargon unexplained — every flag should be readable by someone doing a first pass before their morning coffee.
- If a figure can't be found or derived, say "Not stated" — never estimate or assume a number that isn't in the document.
