---
name: mock-skill
description: >-
  Test fixture only — not a client deliverable. Classifies a term sheet's
  instrument type (safe, priced_round, convertible_note, seed_summary) for the
  sole purpose of exercising tools/skill-gate/gate.py and publish.py in CI.
allowed-tools: Read, Grep
argument-hint: <path-to-term-sheet>
---

# Mock Skill — Gate Smoke Test (not a real deliverable)

**Skill version:** 1.0.0

This skill exists only to prove the skill-gate pipeline works end to end: a new
skill is registered in `tools/skill-gate/gate.py`'s `SKILLS` dict, given golden
labels and a recorded run, gated, and (optionally) published through
`tools/skill-gate/publish.py`. It does not ship any client-facing value and
should not be treated as a deliverable.

## Task

Classify the instrument type of the term sheet at the given path as exactly one
of: `safe`, `priced_round`, `convertible_note`, `seed_summary`.

## Signals

- `safe` — "future equity", no interest, no maturity date, converts at a cap/discount.
- `convertible_note` — an interest rate and a maturity/redemption date.
- `priced_round` — a price per share and a stated pre/post-money valuation.
- `seed_summary` — terse bullet-format seed terms with none of the above signals.

## Output

```
Instrument: <safe | priced_round | convertible_note | seed_summary>
Signal:     <the phrase that decided it>
```
