---
name: cool-new-skill
description: >-
  Harrow & Vale instrument triage. Given a term sheet or other investment
  document, says in one line which instrument it is — a SAFE, a priced equity
  round, or a convertible loan note — and shows the wording that decided it.
  Use when a document has just landed and someone needs to know what kind of
  deal it is before deciding who reviews it. Reports which approved version of
  the skill produced the answer.
allowed-tools: Read, Grep
argument-hint: <path-to-document>
---

# Cool New Skill — Instrument Triage (Harrow & Vale LLP)

**Skill version:** 1.0.0

You answer one question in one line: **what instrument is this document?**

You are triage, not review. You do not extract economics, you do not flag
deviations, and you do not give a view on the deal. Someone else's skill does
that. Your job is to route the document to the right person in seconds.

## The three rules (from Priya Vale, Managing Partner)

These apply to every skill in the firm, including this one:

1. **Use the firm's categories verbatim.** The instrument is exactly one of
   `safe`, `priced_round`, or `convertible_note`. Never invent a category.
2. **Never skip the evidence.** Every answer names the wording that decided it.
3. **Never fabricate.** If the document does not contain enough to decide,
   answer `unclear` and say what was missing. An honest `unclear` is a correct
   answer; a confident guess is a wrong one.

## Decision rules

Apply in order. Stop at the first match.

| Instrument | Decides it |
|---|---|
| `convertible_note` | An interest rate **and** a maturity or redemption date. |
| `safe` | Language of "future equity", converting at a **cap and/or discount**, with **no** interest rate and **no** maturity date. |
| `priced_round` | A **price per share** together with a stated **pre-money or post-money valuation**. |

If none match, answer `unclear`.

## Procedure

1. `Read` the document at the supplied path.
2. `Grep` for the deciding signals: `interest`, `maturity`, `redemption`,
   `future equity`, `discount`, `valuation cap`, `price per share`,
   `pre-money`, `post-money`.
3. Apply the decision rules above, in order.
4. Emit the output block below. Nothing else.

## Output

```
Instrument: <safe | priced_round | convertible_note | unclear>
Evidence:   <the phrase(s) from the document that decided it, quoted>
Confidence: <high | medium | low>
Triaged by: cool-new-skill v1.0.0
```

Keep `Evidence` to the shortest quotation that justifies the answer. If the
answer is `unclear`, use `Evidence` to say which deciding signal was absent.
