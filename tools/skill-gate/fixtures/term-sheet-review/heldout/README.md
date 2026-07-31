# Held-out test documents — READ THIS FIRST

## The one rule

**Never write a worked review for a document in this folder, and never move one of these
documents into `plugins/term-sheet-review-plugin/skills/term-sheet-review/examples/`.**

The moment a worked example exists for a document, that document stops being able to test
anything. It becomes an answer key the model reads instead of doing the extraction.

## Why this folder exists

On 2026-07-30 a clean-session acceptance test of `term-sheet-review` was run against
`assets/source/term-sheets/safe-nimbus-robotics.md`. The agent read
`examples/review-safe-nimbus.md`, recognised the document, and presented the stored example
as its output — saying so explicitly. The verbatim `1 PARTIAL` tally in its answer traces to
line 86 of that example file.

The skill ships worked reviews for **all four** sample term sheets. So all four are
compromised as test inputs, and every verification run before this date was an open-book
exam.

## The structural distinction that matters

| Location | Model can read it at run time | Purpose |
|---|---|---|
| `plugins/…/skills/term-sheet-review/examples/` | **yes** — inside the skill | teaching material, shipped to users |
| `tools/skill-gate/fixtures/…/heldout/` | not loaded by the skill | scoring, never shipped |

Expected answers for held-out documents live in `labels/` as **structured field values**, not
as prose reviews. That is deliberate: a JSON label set cannot be copied into an output and
passed off as a review, whereas a finished prose review can.

**Honest limitation:** nothing physically stops a model with filesystem access from reading
`labels/`. The real control is the prohibition in `SKILL.md` against serving a stored answer,
plus the fact that these files are not auto-loaded as part of the skill. Treat this as raising
the cost of cheating, not eliminating it. If you need a genuinely sealed test, keep a document
outside the repository entirely.

## How to use these

1. Ask for a review of the document in `documents/`, in a **fresh session**.
2. Score the output against `labels/` by hand, or via the gate once scoring is wired up.
3. If you find yourself wanting to write down the "right answer" in prose to make scoring
   easier — don't. That is exactly how the existing four were spoiled.

## Rotation

A held-out document has a shelf life. Once it has been discussed at length in sessions, or
its answers have been pasted into notes and ledgers, it is partially burned. Plan on writing
a new one periodically rather than trusting one document forever.
