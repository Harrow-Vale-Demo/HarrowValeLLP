# Backup slides — draw up only if asked

> Prepared 2026-07-31. **None of these are in the deck.** They exist so that if Tom pushes on
> Slide 4, or there is spare time at the end, there is something accurate to put up rather than
> something improvised.
>
> Every slide below has a **READ ALOUD** block. It is written to be read verbatim, at pace, if
> your mind goes blank. Read it exactly as written and it will make sense.

---

## Status vocabulary — verified 2026-07-31

Re-checked against the code on master before writing these. Do not upgrade any of them.

| Claim | Verified state |
|---|---|
| Packaging check | Written on `feature/gate-packaging-check`. **Not on master.** `gate.py` on master has zero references to it. |
| Verbatim checklist check | **Spec only.** No implementation in any `.py` anywhere in the repo. |
| Gate-report enforcement | **Genuinely on master.** `check_published.py` asserts a stored passing `gate-report.json` and version agreement. |
| Install verification | **Nothing exists.** No code anywhere reads the machine's install state. |
| Held-out test document | Written, on `feature/handover-02-artefacts`. **Not on master, and not wired into the gate** — `gate.py` and `scorers/termsheet.py` both have zero references to it. |
| CI enforcement | `check_published.py` is the **blocking** step. `gate.py --all` runs `continue-on-error` and is **informational** — do not say "CI blocks a low score". |

**The correction that matters:** the held-out test was briefly described as "Fixed" on Slide 4.
It is not. The document exists; the test has never been run. Row 3 was replaced with the
gate-report check, which *is* genuinely closed.

---

# T1 — "A skill can ship without the checklist"

**Status: written, on a branch. Not merged.**

### On-slide wording

> ## The skill kept working after losing its own ground truth
>
> | | |
> |---|---|
> | **What happened** | A copy shipped with `SKILL.md` but without its `reference/` folder |
> | **What it looked like** | A clean, confident, correctly formatted review |
> | **What was actually wrong** | It was using its own idea of a checklist, not Priya's |
> | **Why the gate missed it** | The gate scores a recorded output; it never inspected the package |
> | **The fix** | Block publication if `SKILL.md` names a file that is not in the shipped tree |
>
> **Written, not merged — and it would not have caught this exact case.**

### READ ALOUD

> "This is the one that worried us most. We put the skill on a second surface, and the checklist
> file didn't travel with it. The skill carried on working. It produced a review that looked
> exactly like a good one — right structure, confident tone, nothing missing on the page. But it
> had stopped using Priya's checklist and started using its own idea of one, and nothing in the
> output said so.
>
> Our evaluation gate couldn't catch it, because the gate marks the answer, not the parcel. So
> we've written a check that refuses to publish a skill if it points at a file that isn't in the
> package.
>
> And I should be straight with you about the limit of that. The check looks at our source
> folder, but this failure happened in transit to the other surface — so it would not have caught
> the case that prompted it. The fix has the same shape as the bug. That's exactly why the next
> step is checking the package where the skill actually runs, not where it's convenient for us
> to look."

### If Tom pushes further

- **"Why isn't it merged?"** — It was written today; we chose to freeze the demo rather than land
  code we could not test properly first. It's a small change and it's on a branch.
- **"How would we know today?"** — You would look at the folder on disk. Not good enough as a
  permanent answer, which is why it becomes a check.

---

# T2 — "The checklist can be summarised instead of reproduced"

**Status: specified only. No code exists.**

### On-slide wording

> ## Priya's rule is "verbatim". Today that is an instruction, not a guarantee
>
> | | |
> |---|---|
> | **The rule** | Use the checklist word for word. Never rename, merge or invent an item |
> | **Today** | The rule lives in the skill's instructions — the model is asked to comply |
> | **The gap** | A paraphrase, a merged pair of items, or a summarised section passes silently |
> | **Observed** | One run summarised a checklist section instead of listing it |
> | **The fix** | Compare the checklist in every output against the source file, character for character |
>
> **Specified, not built. The file it would enforce against is already the single source of truth.**

### READ ALOUD

> "Priya's first rule is that the checklist is used word for word — nothing renamed, nothing
> merged, nothing invented. Right now that rule is written into the skill's instructions, which
> means we are asking the model to comply rather than requiring it.
>
> Most of the time it does. But we saw a run where it summarised a section of the checklist
> instead of listing every item out, which is precisely the behaviour Priya told us she would not
> accept. It passed unnoticed, because a summary of a checklist still looks like a checklist.
>
> The fix is not cleverer wording. It's a comparison: take the checklist out of the output, put
> it next to the source file, and require them to match character for character. A paraphrase
> then fails the build instead of reaching a lawyer.
>
> That one is specified and not yet built. What is already true is that there's a single file
> that counts as the checklist, so there is something definite to compare against."

### If Tom pushes further

- **"Is it hard?"** — No. It is a string comparison. The reason it isn't done is sequencing, not
  difficulty.
- **"What about legitimate rewording?"** — There isn't any. That's the point of a fixed checklist;
  if Priya changes it, the file changes and the check follows.

---

# T3 — "A version could reach the shelf with no evidence it passed"

**Status: genuinely fixed and on master. The one place you may speak in the present tense.**

### On-slide wording

> ## The version on the shelf is the version that was graded
>
> | | |
> |---|---|
> | **The risk** | A hand-edited version number publishes to every machine with no evidence behind it |
> | **The control** | One publisher. It writes nothing unless the gate passes |
> | **What it stamps** | The graded version into the plugin, the shelf, the skill text and the changelog |
> | **The assertion** | Every published version must have a stored, passing gate report |
> | **Proof it refuses** | A deliberately bad test skill that the gate rejects on demand |
>
> **There is no separate "bump the version" step that can be got wrong.**

### READ ALOUD

> "This is the part that is genuinely finished, so I'll say it plainly.
>
> The danger with a shared shelf is that a version number is just text. Change one character and
> ten machines update to something nobody assessed. So publishing is not a manual step here. One
> script does it, and it writes nothing at all unless the gate passes. When it does pass, it
> stamps the same version the gate just graded into the plugin, the shelf listing, the skill text
> and the changelog — all at once. There is no separate bump step to get wrong.
>
> On top of that there is a check that every published version has a stored gate report saying it
> passed. If the evidence isn't there, the version isn't legitimate.
>
> And we can prove the gate says no, not just yes — there's a deliberately broken test skill in
> the repository that exists purely to be rejected. A gate that has only ever approved things
> isn't a gate."

### If Tom pushes further

- **"Who can publish?"** — Anyone can propose. Only the gate can approve, and the branch is
  protected in the production model.
- **"Can we roll back?"** — Yes. Every version keeps its changelog entry and its gate report, so
  you can identify and withdraw the version used on a given matter.

---

# T4 — "A lawyer's machine can run a version nobody approved"

**Status: nothing exists. This is the honest gap.**

### On-slide wording

> ## We verify the shelf. We do not yet verify the machine
>
> | | |
> |---|---|
> | **What is checked** | The shelf, the plugin manifest and the stored gate evidence agree |
> | **What is not** | Whether the copy on a given laptop matches any of that |
> | **How it goes wrong** | A checkout behind the shelf silently serves an old catalogue |
> | **Why it is nasty** | A stale install and a broken install look identical — no error either way |
> | **The fix** | Stamp the package with what was approved; verify it where it runs; refuse on mismatch |
>
> **Not built. This is the boundary of what the gate can see.**

### READ ALOUD

> "This is the gap, and I'd rather name it than have you find it.
>
> Everything I've described checks the shelf — that the approved version is consistent and backed
> by evidence. None of it checks the laptop. Nothing today looks at what a particular lawyer
> actually has installed and compares it to what was approved.
>
> We hit this ourselves. A machine that was simply behind on updates served an old catalogue, and
> it took a while to work out, because a stale install and a broken install look exactly the same
> — no error in either case.
>
> The fix follows the same principle as everything else here: stamp the package with a record of
> what was approved, check that record where the skill actually runs, and make a mismatch refuse
> rather than quietly carry on. Think of it as chain of custody. Our gate proves the document was
> sound when we examined it; this proves the copy in the room is that same document.
>
> That's not built. It's the first thing we'd do in a next phase."

### If Tom pushes further

- **"So we can't trust installs today?"** — You can, with a manual step: confirm the machine is
  up to date before relying on it. What is missing is the automatic assertion.
- **"Does this block a pilot?"** — No. A pilot is small enough to check by hand. It blocks
  firm-wide rollout without a manual step, which is why it is first in the next phase.

---

# T5 — "If time" — how we would run the build itself better

**Not a defect slide. This is process improvement, and it is honest about hindsight.**

### On-slide wording

> ## What we would set up on day one, next time
>
> | | |
> |---|---|
> | **Shared working memory** | A single file agents read first and write status to — who holds what, what changed |
> | **Shared skills, not shared prompts** | The team's methods packaged and versioned, so every session starts equal |
> | **A build loop with separated roles** | Planner, generator and evaluator kept apart, with an agreed contract between them |
> | **Adversarial grading by default** | Something whose job is to attack the output, from the first hour |
>
> **Most of what we found late, we would have found on day one.**

### READ ALOUD

> "One last thing, on how we worked rather than what we built.
>
> We ran this across several parallel sessions, and the coordination was the hard part. We adopted
> a shared working memory partway through — one file that every session reads before starting and
> updates when it stops, recording who is working on what and what has changed. That helped a
> great deal, and it should have been there from the first hour rather than the middle.
>
> The bigger lesson is about testing. We have a house pattern at Negative Zero for this kind of
> build: you separate the roles, so the thing that plans, the thing that produces and the thing
> that grades are kept apart and have to agree a contract between them, and you have something
> adversarial attacking the output from the start. We brought that discipline in late, and every
> significant defect we found came from it.
>
> If we started again on Monday, that setup would be the first day's work, not the last. It is
> also, frankly, the most transferable part of this engagement — it isn't specific to term
> sheets."

### The honest framing, if challenged

Do not claim the loop harness was used to build this. It was not. The claim is narrower and
still true: **the defects were found by adversarial testing, and adopting that discipline earlier
would have found them earlier.** Coordination via a shared working-memory file *was* genuinely
adopted mid-build, so that one may be described in the past tense.

---

# B6 — "Every test we had run was an open-book exam"

**Status: the problem is real and current. The fix is written but not wired in.**

Added because the open-book story has no home on the main slide — it came off Slide 4 when the
"Fixed" label turned out to be false, and it is too good a finding to lose.

### On-slide wording

> ## Every test we had run was an *open-book exam*
>
> | | |
> |---|---|
> | **What we did** | Graded the skill against our four sample term sheets. It passed |
> | **What we missed** | The skill ships worked answers for those same four documents |
> | **Why that matters** | It can recognise the document and return the stored answer without doing the work |
> | **What we did about it** | Wrote a fifth term sheet it has never seen — unfamiliar format, deliberate traps |
> | **Where it stands** | The document exists. Not wired into the gate; nothing graded against it |
>
> **The four samples no longer prove much. That is why we stopped saying "verified".**

### Language discipline

Never say "we tested against it", "the held-out test passes", or "verified". Correct verbs:
**we have written**, and **the principle we took from it**. If asked directly whether the fifth
document has been run — **it has not**.

---

## How to add any of these to the deck

Copy an existing `<section class="slide">` block and replace the contents. For a two-column
detail table, the pattern used on Slide 4 works:

```html
<section class="slide" data-eyebrow="Detail" data-title="Short title">
  <h2>Headline with <span class="hl">highlight</span></h2>
  <div class="headrule"></div>
  <div class="rows an">
    <div class="split"><div>Left label</div><div>Right text</div></div>
  </div>
  <div class="claim an">The honest closing line</div>
  <template data-notes><span class="presenter">Emily</span><p>…</p></template>
</section>
```

Add them **after** the close slide if they are backup only — the slide counter includes every
section, so anything added mid-deck shifts the numbering the rest of the group is working from.
