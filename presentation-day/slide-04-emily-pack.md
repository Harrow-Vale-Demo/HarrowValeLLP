# Slide 4 — "How Claude helped" · Emily's pack

> Prepared 2026-07-31 for the Friday presentation. Emily owns this slide per the presenter
> allocation in `group-presentation-wording-and-script.md`.
>
> Slot: immediately after Live Demo 1 (review + lawyer control). Hand back to lead for Slide 5.
> Budget: roughly 60–75 seconds of a 10–12 minute deck. **Do not overrun** — Slide 5 is the
> strongest slide in the deck and it needs its air.

---

## The existing slide (unchanged — this is what's in the HTML now)

> ## Claude handled the interpretation; evidence made it usable
>
> | Claude contributed | The firm stayed in control |
> |---|---|
> | Interpreted differently structured term sheets | Defined the checklist and legal standards |
> | Produced a structured, source-linked first pass | Set expected results and the release threshold |
> | Helped iterate the skill against synthetic examples | Reviewed outputs and retained final sign-off |
>
> **Claude accelerates the first pass. It does not replace legal judgement.**

This is good. The two-column contrast is the right structure and the closing line is the right
closing line. **Recommendation: change at most one row.** A slide that grows in the last hours
before a presentation is a slide that gets misread on stage.

---

## The one change worth making

The current three rows all describe Claude *producing* things. Nothing describes Claude
**finding its own mistakes**, which is the more interesting claim and the one that speaks to
reliability rather than capability.

Optional replacement for row 3 — swap, don't add:

| Claude contributed | The firm stayed in control |
|---|---|
| Interpreted differently structured term sheets | Defined the checklist and legal standards |
| Produced a structured, source-linked first pass | Set expected results and the release threshold |
| **Surfaced defects in its own output that a skim would pass** | **Turned each one into a mechanical check, not a promise** |

Why this row earns its place: every other reliability claim in the deck is an assertion about
design. This one is an assertion about *behaviour under test*, which is much harder to say and
therefore much more credible.

**If in doubt, leave the slide alone and put this in the spoken track instead.** The material is
strong; it does not need to be on the wall.

---

## Spoken track — primary version (~60 seconds)

Use this if the hardening story stays off the slide.

> "Two things were genuinely hard here, and only one of them was the extraction.
>
> The easy part — relatively — was reading four differently structured term sheets and pulling
> the same fields out of each. A table, a priced-round sheet, a convertible note, and a page of
> terse bullets. Claude handled that.
>
> The hard part was making the output *checkable*. Priya's position was clear: she did not want
> a confident summary, she wanted to see the checklist followed, with nothing invented and
> nothing skipped. So every finding is linked back to the clause it came from, absent terms read
> 'not stated' rather than being filled in from a typical deal, and the whole checklist appears
> in every review whether or not it applies.
>
> The firm set all of that. Priya's checklist is the ground truth, the firm defined what a good
> answer looks like, and the firm holds the sign-off. Claude accelerated the first pass — the
> legal judgement never moved."

**Landing line, said slowly:** *"Claude accelerates the first pass. It does not replace legal
judgement."*

---

## Spoken track — variant with the reliability beat (~75 seconds)

Use this if you decide the hardening story is woven in lightly. Replaces the third paragraph
above:

> "…The hard part was making the output checkable — and the useful discovery was that we could
> not take our own word for it.
>
> We tested the skill against our four sample documents and it passed. Then we noticed the skill
> shipped worked examples for those same four documents — so it could recognise the document and
> return the stored answer without doing the work. Every test we had run was an open-book exam.
>
> So we wrote a fifth term sheet the skill had never seen, in a format unlike the others, with
> deliberate traps in it. And where the firm's rule was 'use the checklist word for word', we
> stopped asking the model to be careful and made it a check that fails the build.
>
> That is the difference between a clever prompt and a workflow a firm can govern."

**Why this is worth 15 extra seconds:** it directly answers the question a technical person in
the room is already forming — *how do you know it works?* — and answers it with a specific
failure you found yourselves. It also maps onto the programme's stated exam alignment,
**Context Management & Reliability (15%)**, which nothing else in the deck addresses as
directly.

**Risk to weigh:** it admits a defect. In a 12-minute client pitch that can read as
transparency or as instability depending on delivery. Said briskly and without apology, it is
the strongest 15 seconds available. Said hesitantly, it is a wobble. Your call — and if you are
not certain, use the primary version.

---

## Q&A defences — the four questions most likely to come at this slide

**"How do you know the output is actually right?"**
> Three layers. Every extracted value carries the clause it came from, so a lawyer verifies
> rather than trusts. The checklist appears in full in every review, so nothing can be quietly
> dropped. And a skill cannot be published until it passes a scored evaluation — which is the
> next slide.

**"What stops it inventing a checklist item, or paraphrasing one?"**
> The checklist is a fixed file the skill reads; it is not in the model's head. And we have
> written a check that compares the checklist in any output against that file character for
> character, so a paraphrase fails rather than passing quietly. *(Honest caveat if pressed: the
> check is specified and being implemented — the file it enforces against is already the single
> source of truth.)*

**"Did it get anything wrong?"**
> Yes, and that is the part worth telling you about. It found a definitional problem in one of
> the sample SAFEs that a first read would miss — a discount defined in a way that, read
> literally, gives an eighty percent discount rather than twenty. It also, in one run, summarised
> a section of the checklist instead of listing it out, which is exactly the behaviour Priya said
> she would not accept. That one is now a hard check rather than an instruction.

**"Is this just a prompt?"**
> No — and that distinction is the whole engagement. A prompt lives on one lawyer's machine and
> nobody knows which version anyone is using. This is a versioned skill with a fixed checklist,
> a scored gate before release, and a single approved shelf all ten lawyers install from.

---

## Coverage check against the brief (`docs/engagement/scenario-guide.md`)

What the engagement pack asks for, and whether the deck says it:

| Brief requirement | Deck | Note |
|---|---|---|
| Extract key economic terms — valuation/cap, discount, liq pref, board/consent, pro-rata | ✅ Slide 3 | Covered |
| Flag deviations, unusual clauses **and omissions** | ✅ Slides 3, 6 | Covered |
| **Consistent across the three formats** | ⚠️ implied | The brief stresses this. You built for **four** formats, including the terse seed bullets that weren't asked for. **Say the number** — it's a free win currently going unclaimed. |
| **Built test-driven against 2–3 examples first** | ⚠️ not said | The brief explicitly asks for this approach. Slide 5 covers evaluation but not that testing came *first*. One clause in your track fixes it. |
| Lawyer installs from a private repo, gets updates | ✅ Slide 8 + Demo 3 | Covered |
| Documented approval + versioning — **who vets, how v2 rolls out** | ✅ Slides 5, 8 | Covered |
| One-page data-residency / confidentiality memo | ✅ Slide 7 + `deliverables/data-security-briefing.md` | Covered |
| Exam alignment: **Context Management & Reliability (15%)** | ⚠️ thin | The hardening work is the most direct evidence of this in the whole project, and it is currently entirely absent from the deck. Strongest single argument for the 75-second variant. |

**Two small wins available in your 60 seconds, at no cost:** say "four formats", and say
"test-driven from the start". Both are in the brief, both are true, neither is currently claimed.

---

## The silent-failure beat — honest wording (added 2026-07-31)

**Status check before using any of this.** Three different tenses are needed, because the
three hardening artefacts are at three different stages:

| Artefact | Actually in the working tree? | Safe verb |
|---|---|---|
| Held-out test (Vantor Health) | ✅ real, on disk | "we wrote", "we tested against" |
| Verbatim checklist check | 📄 spec only (`docs/governance/verbatim-checklist-check-spec.md`) | "we've specified" |
| Packaging check (the silent failure) | ⛔ **not merged** — sits on `feature/gate-packaging-check` | **"we've written"** — never "our gate blocks this" |

### ~25 seconds, drop-in

> "One more thing worth telling you about. We uploaded the skill to a second surface, and it
> shipped without the checklist file attached. It still ran. It still produced a clean,
> confident review — it just wasn't using Priya's checklist any more, it was using its own idea
> of one. Nothing in the output said so.
>
> That's the failure that actually worries me: not a crash, but a plausible answer produced
> without the ground truth. And our evaluation gate couldn't see it, because the gate scores the
> output — it never looked at what was in the package. We've written the check that closes that
> gap: every file the skill refers to has to be present in what ships, or it doesn't publish."

### ~12 seconds, if running long

> "We found the skill could ship without its checklist file attached — still running, still
> confident, just no longer using Priya's checklist. Nothing in the output revealed it. That's
> the failure mode worth designing against, and we've written the packaging check that closes it."

### If asked "is it live?"

> "The check is written, not yet merged. What's merged is the diagnosis and the held-out test.
> We'd rather tell you where the line is than blur it."

A team that knows precisely what is and isn't deployed reads as *more* governed, not less.

---

## The pattern beat — one failure shape, five costumes (added 2026-07-31)

**Emily's call on presentation day: the hardening story is in.** This is the version that
generalises, rather than telling five separate war stories. It is stronger than any single
incident because it shows you understood the *class*, not just the bug.

### The finding, in one line

> Every defect we found had the same shape: **something was verified somewhere other than
> where it is used — and none of them announced themselves.**

Two properties, and the second is what makes it dangerous:

1. **Displaced verification** — we checked in one place; the thing that mattered ran in another.
2. **Silent divergence** — when the two drifted apart, nothing said so. No error, no warning,
   no missing section. The system kept working and kept looking confident.

### The five, in one table (for a backup slide or Q&A, not the main slide)

| | Verified here | Actually used here |
|---|---|---|
| H1 | The shelf manifest | The machine's install state |
| H2 | A recorded output | The package that reached the machine |
| H3 | A test document | ...whose answer shipped inside the skill |
| H4 | One of five copies of the checklist | Whichever copy was loaded |
| H5 | A manifest | ...pointing at a directory that wasn't a plugin |

### The improvement — say this, not just the diagnosis

A diagnosis without a fix reads as an apology. Three levels, cheapest first:

**1. Make the artefact check itself, at the point of use.**
The skill asserts it can read `reference/dd-checklist.md` before it does anything, and
**refuses to produce a review if it cannot**. One change fixes both properties at once: it
moves the check to where the work happens, and it converts silence into a loud refusal.
*A refusal is worth more to a partner than a plausible answer.*

**2. Gate-stamped provenance — the version that closes the whole class.**
The gate already records what it graded. Extend that record to the **exact file list and a
hash of each file**, ship it with the skill, and check it at install and at run time. Anything
that differs from what was graded refuses loudly.

That single mechanism catches all five: a missing reference file, a stale install, a manifest
pointing nowhere, the wrong copy of the checklist, a test document whose answer shipped
alongside it.

**3. The principle, stated once and remembered:**
> **Verify where it runs, not where it's convenient. Make absence refuse, not degrade.**

### The framing that lands with a law firm — chain of custody

This is the analogy to use with Priya and Tom, because it is already how they think:

> "In evidence terms, our gate proves the document was authentic **when we examined it**. What
> it didn't prove was chain of custody — that the thing on the lawyer's machine is that same
> document, unaltered. Every defect we found was a break in the chain, and none of the breaks
> were logged. So we're closing it the way you would: the package is stamped with what was
> approved, and anything that doesn't match refuses to run rather than quietly carrying on."

That reframes five embarrassing-sounding bugs as **one well-understood problem with a standard
professional answer** — which is exactly the impression you want to leave.

### Spoken track — the pattern beat (~35 seconds)

Use *instead of* the single-incident version if you want the stronger claim. Pairs with the
~25-second H2 wording above; **do not use both**, you will overrun.

> "We found five defects during the build, and the useful thing wasn't any one of them — it was
> that they turned out to be the same defect five times.
>
> In every case we had verified something in one place, and the thing that actually mattered
> was running somewhere else. And not one of them announced itself. Nothing crashed. The output
> stayed clean and confident the whole time. In a legal review that is the failure that should
> worry you, because it doesn't look like a failure.
>
> It's a chain-of-custody problem. Our gate proved the skill was right when we examined it; it
> didn't prove that what reached the lawyer was that same thing. So the fix is the one you'd
> expect: stamp the package with what was approved, check it where it actually runs, and make a
> mismatch refuse rather than quietly carry on."

**Landing line:** *"A governance system that has never found anything isn't evidence of
quality. It's evidence of not having looked."*

### Honesty tags for this beat

- "We found five defects" — ✅ true, documented in `docs/hardening/`
- "We're closing it" / "the fix is" — describe as **intended design**. Level 1 and Level 2 are
  **not built**. Say *"that's the design we'd take into the next phase"* if pressed.
- The packaging check specifically — 🟡 written, unmerged. "We've written" only.

---

## Do not say

- **"Verified"** or **"validated"** about anything that has only been tested against the four
  sample documents. The held-out test exists precisely because those four no longer prove much.
- **"Two skills"** as a demonstrated capability. The DD-mapper is merged but deliberately
  off-shelf until it has been through the gate. It is a real thing, correctly withheld — describe
  it that way if it comes up, and let the lead handle Slide 3.
- Anything implying UK or EU data residency. Slide 7 is careful about this and the careful
  wording is deliberate.
- **"It never makes mistakes."** It does, the process catches them, and that is the better story.
