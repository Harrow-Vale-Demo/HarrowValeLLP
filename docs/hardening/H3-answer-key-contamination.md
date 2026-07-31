# H3 — The skill ships worked answers for its own test documents

**Found:** 2026-07-30, clean-session acceptance test
**Class:** Evaluation integrity
**Status:** Open — spec written, not yet implemented
**Severity:** High. Breaches two of Priya's three rules, and invalidates every verification run to date.

---

## Symptom

A fresh Claude Code session with no prior context was asked to review
`assets/source/term-sheets/safe-nimbus-robotics.md`. It produced a polished, professional
review. It also said this:

> *"My extraction and flagging match the worked review already on file at
> `plugins/term-sheet-review-plugin/skills/term-sheet-review/examples/review-safe-nimbus.md`,
> so I've verified and am presenting that as the completed review rather than duplicating it."*

Confirmed: the `0 PRESENT / 1 MISSING / 1 PARTIAL / 26 N/A` tally in the output is line 86 of
that example file, verbatim.

## Root cause

The skill ships worked reviews for **all four** sample term sheets, inside its own folder:

```
plugins/term-sheet-review-plugin/skills/term-sheet-review/examples/
├── review-safe-nimbus.md
├── review-series-a-greengrid-ddroom.md
├── review-note-anchorline.md
└── review-seed-solace.md
```

Those are the same four documents used for every acceptance test. The model reads `examples/`
as part of the skill, recognises the input, and can return the stored answer without
extracting anything.

**Consequence: every verification of this skill to date has been an open-book exam.** Including
the acceptance criteria designed in the same session that found this.

The examples are not a mistake in themselves — worked examples are good skill design and they
plainly improve output quality. The mistake is using the *same documents* for teaching and for
testing.

## What else it exposed

Once the output was compared against the rules rather than against expectations, four further
defects appeared. All four were invisible for as long as testing consisted of "does the output
look right".

### 1. Rule 1 breached in the shipped artefact — 22 of 28 items renamed

Rule 1: *"Use the fixed checklist verbatim. Never invent, rename, or merge checklist items."*

`examples/review-safe-nimbus.md` paraphrases 22 of Priya's 28 items:

| Priya's wording | Shipped example |
|---|---|
| Full capitalisation table, fully diluted | Fully-diluted cap table |
| Customer contracts above £50,000 annual value | Customer contracts >£50k/yr |
| Supplier/vendor agreements with exclusivity or minimum-spend terms | Supplier agreements w/ exclusivity or min-spend |
| Last two years' audited (or management) accounts | Last 2 years' accounts |
| Directors' & officers' liability insurance | D&O liability insurance |
| Any transactions between the company and its directors/major shareholders | Company ↔ director/major-shareholder transactions |

…and 16 more. Because the model matches on the example rather than the checklist, the
paraphrasing propagates into live output. **The artefact intended to demonstrate Rule 1
compliance is the thing violating it.**

### 2. Rule 2 breached at run time — coverage summarised, not enumerated

Rule 2: *"Never skip a step. Every checklist item must appear with an explicit status."*

The delivered Part C read, in part:

> *"Every other item across Corporate Structure, Material Contracts, IP, Employment,
> Litigation & Compliance, Financials & Tax, Insurance, and Related-Party Transactions is N/A
> since no supporting documents were supplied."*

Twenty-six items asserted as covered without being shown. The assertion happens to be
correct, which is exactly what makes it dangerous — Rule 2 exists so that correctness is
*visible* rather than claimed.

### 3. `PARTIAL` — an undocumented fourth status

The sanctioned statuses are PRESENT / MISSING / N/A, in `SKILL.md`, in
`reference/output-template.md`, and in the lawyer guide's status table. `PARTIAL` appears in
**three of the four** shipped examples and is sanctioned nowhere.

It may well be a good idea — *"this SAFE is one such instrument, but the others weren't
provided"* is honestly none of the three. But an undocumented category invented at run time is
the shape of a Rule 1 breach, and it contradicts a table the firm hands to its lawyers.

### 4. A legal conclusion asserted

The output ended: *"Nothing here blocks signing."*

`SKILL.md` is explicit that the skill is *"a careful associate, not the partner"* and that no
flag may *"assert a final legal conclusion"*. Whether anything blocks signing is precisely the
partner's call.

### 5. A real defect missed

The run did not catch that the Nimbus SAFE defines *"Discount Price" = price per share …
× Discount Rate*, which read literally at 20% produces a price at 20% **of** the financing
price — an 80% discount — rather than a 20% discount. A contaminated in-session run did catch
it, which suggests the miss is about effort allocation once the answer is recognised, not
capability.

## Why the gate could not see any of this

The gate scores **recorded fixtures**: stored JSON representing what the skill produced. All
five defects above occur either at run time or in a shipped example that no check reads. The
gate is working correctly and is looking somewhere else.

## Fixes

Spec: [`docs/governance/verbatim-checklist-check-spec.md`](../governance/verbatim-checklist-check-spec.md)

| # | Fix | Kind | Status |
|---|---|---|---|
| 1 | Regenerate all four examples with verbatim checklist wording | Content | Not started |
| 2 | `check_verbatim.py` — assert item text, count, order, sections, statuses | Mechanical | Spec written |
| 3 | Assert the plugin's checklist matches the canonical client document (see H4) | Mechanical | Spec written |
| 4 | `SKILL.md`: never serve a stored example as a fresh review | Instruction | Not started |
| 5 | `SKILL.md`: Part C must enumerate 28 items; a summary sentence is a failure | Instruction | Not started |
| 6 | Held-out test document with no worked review | Process | **Done** |
| 7 | Resolve `PARTIAL` — sanction it or remove it | Decision | Deferred; see below |

### Held-out fixture

`tools/skill-gate/fixtures/term-sheet-review/heldout/` — a fifth term sheet in prose-letter
format, with expected answers as **structured labels rather than a prose review**, so they
cannot be copied into an output and passed off. Traps include an instrument conflict, an
arithmetic inconsistency that must be flagged rather than corrected, a 22% discount that must
**not** be flagged, and an absent governing law that must read `Not stated`.

Its `README.md` carries the one rule: **never write a worked review for a held-out document.**
That is precisely how the original four stopped being able to test anything.

### On `PARTIAL` — deferred by decision

Not a blocker. If there is time before the demo, decide it properly; if not, it stays as it is
and is noted as known. Recorded here so the decision is deliberate rather than forgotten:

- **(a) Sanction it** — add to `SKILL.md`, the output template, the allowed-status constant,
  and the lawyer guide's status table, with a one-line definition. Most faithful to what a real
  review needs.
- **(b) Remove it** — rewrite the three example lines as PRESENT or MISSING, with the nuance in
  the detail text. Keeps the lawyer-facing story to three statuses.

Priya or Emily decides. Not the implementer.

## Lessons

1. **Teaching material and test material must be different documents.** This is the whole
   issue in one line.
2. **"Does the output look right" is not a test.** Four of the five defects produced output
   that read as competent professional work. The rules were breached in ways a skim cannot see.
3. **A rule expressed only in prose is not enforced.** Rule 1 is a string-equality property and
   was therefore mechanically checkable all along — it just wasn't checked.
4. **A held-out document has a shelf life.** Once its answers have been discussed in sessions
   and pasted into notes, it is partially burned. Plan on rotation.
