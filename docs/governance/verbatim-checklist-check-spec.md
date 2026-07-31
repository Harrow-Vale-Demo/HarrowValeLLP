# Spec — Verbatim Checklist Check

> **For implementation by Claude Code.** Written 2026-07-30 from a Cowork session.
> Scope: one new deterministic check in `tools/skill-gate/`, plus three content fixes it will
> immediately fail on. Read the whole spec before writing code — the fixes and the check have
> to land together or CI goes red.

---

## Why

Priya's Rule 1 is *"Use the fixed checklist verbatim. Never invent, rename, or merge checklist
items."* It is currently an instruction in prose, enforced by nothing.

It is also currently being broken. Measured against
`plugins/term-sheet-review-plugin/skills/term-sheet-review/reference/dd-checklist.md`, the
shipped worked example `examples/review-safe-nimbus.md` paraphrases **22 of 28** checklist
items — "Full capitalisation table, fully diluted" becomes "Fully-diluted cap table",
"Directors' & officers' liability insurance" becomes "D&O liability insurance", and so on.

That matters more than it looks. The model pattern-matches on the worked example rather than
the checklist, so the paraphrasing propagates into live output. The artefact intended to
demonstrate Rule 1 compliance is the thing violating it.

Rule 1 is a **string-equality property**. That makes it the rare governance claim that can be
mechanically enforced rather than asserted — which is a considerably stronger thing to show
Tom than a paragraph promising care.

---

## What to build

A new checker, `tools/skill-gate/check_verbatim.py`, wired into the gate and into CI.

### Inputs

1. **Ground truth:** `reference/dd-checklist.md` in the active plugin. Parse the 28 items —
   lines matching `^- \[ \] (.+)$` — preserving order and exact text. Also parse the 9 section
   headings (`^## \d+\. (.+)$`).
2. **Targets:** every file that reproduces checklist items. At minimum, all of
   `plugins/term-sheet-review-plugin/skills/term-sheet-review/examples/*.md`. Make the target
   set a configurable list so a captured live output can be checked with the same code.

### Assertions

For each target file, locate the Part C section (between `## Part C` and `## Part D`) and
extract its checklist lines. Then assert:

| # | Assertion | Failure message should name |
|---|---|---|
| 1 | **Count** — exactly 28 items present | the count found |
| 2 | **Verbatim** — each item text matches ground truth exactly | the expected string, the found string, and the line number |
| 3 | **Order** — items appear in checklist order | the first index out of place |
| 4 | **Sections** — all 9 section headings present, verbatim, in order | which is missing or altered |
| 5 | **Status** — each item carries a status from the allowed set | the item and the offending status |
| 6 | **No extras** — no item appears that is not in the ground truth | the invented item |

Allowed statuses come from a single constant, and **`PARTIAL` is not in it** unless and until
decision D1 below says otherwise.

### Comparison rules

Normalise **only** whitespace: collapse internal runs of spaces, strip leading/trailing. Do
**not** normalise case, punctuation, ampersands, currency symbols, or the difference between
`and` and `&`. Those are precisely the differences Rule 1 is about, and a forgiving comparator
would defeat the point.

One deliberate exception: the trailing status separator. Items are written
`- <item text> — <STATUS> — <detail>`. Split on the first em-dash-with-spaces (` — `) and
compare only the left side. Note that some existing examples use a parenthetical form
(`— N/A (not provided)`) instead; the parser must handle both, or the fixes in step 2 should
standardise on one. Standardising is cleaner.

### Exit behaviour

Exit `0` on pass, `1` on any failure — matching `gate.py`'s existing contract, since that exit
code is what `publish.py` and CI act on. Print every failure, not just the first; an author
fixing 22 paraphrases wants the full list in one run.

---

## Content fixes that must land in the same change

The check will fail immediately on the current tree. That is correct. Fix the content, don't
weaken the check.

### Fix 1 — regenerate the four worked examples with verbatim wording

Files: `examples/review-safe-nimbus.md`, `review-series-a-greengrid-ddroom.md`,
`review-note-anchorline.md`, `review-seed-solace.md`.

Replace each paraphrased item with the exact text from `dd-checklist.md`. **Change only the
item text and status formatting** — leave the analysis, flags, and commentary alone. The
substantive review content in these examples is good and was approved; the wording of the
checklist lines is the defect.

### Fix 2 — resolve `PARTIAL` (decision D1) — **DEFERRED, do not block on this**

**Status as of 2026-07-31: deferred by decision. Nice-to-have if there is time before the demo;
otherwise it stays as it is and is carried as known.**

Implement the check with `PARTIAL` **temporarily permitted** in the allowed-status constant, with
a `TODO: D1` comment pointing here. That keeps the check green on the current examples and lets
the valuable assertions (verbatim wording, count, order, enumeration) land now. Tighten it if and
when D1 is decided.

The background, so the decision stays deliberate rather than forgotten:

`PARTIAL` appears in three of the four examples and is sanctioned nowhere — not in `SKILL.md`,
not in `reference/output-template.md`, not in `deliverables/lawyer-installation-guide.md`,
which tells lawyers there are exactly three statuses.

It is arguably a *good* idea: "this SAFE is one such instrument, but the others weren't
provided" is genuinely neither PRESENT nor MISSING nor N/A. But it is currently an undocumented
fourth category invented at run time, which is the shape of a Rule 1 breach.

Two coherent options — **Emily or Priya decides, not the implementer**:

- **(a) Sanction it.** Add `PARTIAL` to `SKILL.md`, `reference/output-template.md`, the
  allowed-status constant, and the lawyer guide's status table, with a one-line definition.
  Most faithful to what a real review needs.
- **(b) Remove it.** Rewrite those three example lines as `PRESENT` or `MISSING` with the
  nuance in the detail text. Simplest, and keeps the lawyer-facing story to three statuses.

Either is defensible. Leaving it undecided *and* undocumented is the only bad outcome, which is
why it is written down here rather than left in a chat.

---

### Fix 2b — assert the checklist derives from the canonical client document

**This is the assertion that makes the whole check mean anything.** Added 2026-07-31 in answer to
the obvious objection: if output is only ever compared against
`plugins/…/reference/dd-checklist.md`, then that file can drift and every check still passes.

**Canonical source (decided by Emily, 2026-07-31):**
`plugins/term-sheet-review-plugin/skills/term-sheet-review/reference/dd-checklist.md`.

The plugin's own reference copy is the root of trust. Rationale: it is what actually ships, what
the gate governs, and what the skill reads at run time. `assets/source/dd-checklist/` is a
captured input artefact, and the `releases/` copies are frozen historical snapshots — neither
should drive what the live skill uses.

Add a second, separate assertion, with the canonical file as the **source** and all other copies
as **derived**:

> Every other copy of the checklist in the repository must have **normalised item text**
> identical — 28 items, same wording, same order — to the plugin's `reference/dd-checklist.md`.

Copies in scope:

| Copy | Relationship |
|---|---|
| `plugins/…/skills/term-sheet-review/reference/dd-checklist.md` | **canonical** |
| `assets/source/dd-checklist/harrow-vale-dd-checklist.md` | must match |
| `tools/termsheet-harness/reference/dd-checklist.md` | must match, or be deleted with the harness (see H4) |
| `releases/term-sheet-review/v*/references/dd-checklist.md` | **exempt** — frozen snapshots, immutable by design per `releases/CONTRIBUTING.md` |

Compare **item text, not file bytes.** The copies legitimately differ in markup: the plugin copy
uses `- [ ] item` and carries a mock-document HTML comment, the assets copy uses `- item`. Those
differences are fine. The wording is not permitted to differ.

Measured state at time of writing: five real copies of the checklist exist across the repo, with
**four different file hashes but identical item text** (`01e65f1c`). So there is no semantic drift
today — but nothing asserts that, and it is maintained by hand. See
[`docs/hardening/H4-duplicate-overlapping-projects.md`](../hardening/H4-duplicate-overlapping-projects.md).

Also record provenance, so a change to the canonical file is a reviewed event rather than a silent
edit: a small `PROVENANCE.md` beside the canonical checklist, or a field in the gate config,
holding the item-text hash, the date, and who approved it. Changing the checklist then requires
updating a recorded value that a human signed — which is the point.

### Fix 3 — add two prohibitions to `SKILL.md`

Both are live failures observed in a clean-session run on 2026-07-30:

1. **Never serve a stored answer.** Add, near the three rules: *the skill must perform the
   extraction even when it recognises the document, and must never present a worked example
   from `examples/` as the output of a fresh review.* In the observed run the agent read
   `examples/review-safe-nimbus.md`, recognised the input, and presented the stored example —
   including a verbatim `1 PARTIAL` tally traceable to line 86 of that file.
2. **Never enumerate by summary.** The self-check already requires every item to carry a
   status. Strengthen it so a summary sentence cannot satisfy it: *Part C must contain 28
   individually listed items; a sentence asserting that a group of items is N/A is a Rule 2
   failure regardless of accuracy.* The observed run collapsed 26 items into one sentence.

While there: the same run ended with *"Nothing here blocks signing"*. The self-check already
forbids asserting a final legal conclusion — consider whether that line needs sharpening so
it plainly catches summary-level conclusions, not just flags.

---

## Wiring

- Add to `gate.py --all` output as an information line per skill, consistent with how the
  packaging check was added.
- Add to the **required** CI status check alongside `check_published.py`. Rule 1 conformance is
  a property of what ships, so it belongs with the published-consistency check rather than with
  run scoring — an author mid-iteration must not turn the repo red for everyone else.
- Extend `tools/org-policy/README.md`'s six-link chain table if the chain now has a link for
  "the checklist a lawyer sees is Priya's exact wording".

---

## Held-out test fixture

Separate but related, and already created:
`tools/skill-gate/fixtures/term-sheet-review/heldout/`.

Contains a fifth term sheet — a prose letter, a format unlike any of the four samples — with
structured expected labels rather than a worked review. Read that folder's `README.md` before
touching it; the one rule is that **no worked review may ever be written for it**, because that
is exactly how the existing four stopped being able to test anything.

The document carries deliberate traps: an instrument conflict (presented as a SAFE, but with 6%
interest and a 24-month maturity), an arithmetic inconsistency that must be flagged rather than
corrected, a 22% discount that must **not** be flagged (in-band — an over-flagging trap), and
an absent governing law that must read `Not stated` rather than being filled in from
familiarity with the other four samples.

Wiring it into `gate.py` as a scored case is a **later, separate change**. It needs a scoring
approach for structured labels, which the current fixtures don't use.

---

## Definition of done

- [ ] `check_verbatim.py` exists, exits non-zero on the current tree before fixes
- [ ] All four examples pass assertions 1, 3, 4, 6 and — pending D1 — 2 and 5
- [ ] D1 recorded in `LEDGER.md` with who decided
- [ ] `SKILL.md` carries both new prohibitions
- [ ] `gate.py --all` and `check_published.py` still green
- [ ] CI required check updated
- [ ] `LEDGER.md` entry, and the paste-back queue in
      `docs/cowork/cowork-session-notes.md` ticked off

## What this does not fix

Worth stating plainly, because it is the third instance of one problem. The gate scores
recorded fixtures; this check scores shipped files. **Neither observes a live run.** All six
failures found on 2026-07-30 happened at run time. This check closes the specific hole where
paraphrased wording ships in an artefact — it does not stop a live run from paraphrasing, from
summarising Part C, or from asserting a conclusion.

The honest framing for Tom: the gate proves the skill was right once, in a recording; these
checks prove what ships is internally consistent; live-run conformance is still verified by a
human reading the output. Naming that boundary is more credible than implying it is covered.
