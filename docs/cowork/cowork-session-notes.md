# Cowork Session Notes

> Running notes from Emily's Cowork/Desktop sessions. **Appended to as we go** so nothing
> has to be held in your head or reconstructed from chat scrollback.
>
> Companion to `docs/cowork/cowork-briefing.md` (written by the Claude Code side *to* Cowork).
> This file is the reverse direction: what Cowork found, decided, or still needs.
>
> Newest section at the bottom. Don't delete history — annotate corrections inline.

---

## ✅ Which directory is the right one — settled 2026-07-31

**We have been working in the right place.** Verified against commit history, not assumption.

| Path | Verdict | Provenance |
|---|---|---|
| **`plugins/term-sheet-review-plugin/`** | ✅ **THE LIVE PRODUCT.** All work belongs here. | Created by **Emily**, 2026-07-22 (`43835da`, `5776772`). On master, on the shelf, gate-governed, and what actually installs. |
| `plugins/term-sheet-review-plugin/skills/term-sheet-review/reference/dd-checklist.md` | ✅ **CANONICAL checklist** (Emily's decision, 2026-07-31) | It ships, the gate governs it, the skill reads it. Everything else derives. |
| `tools/skill-gate/` | ✅ live — the approval gate | **Lee (AiioApeira)**, 2026-07-29 (`03c7288`) |
| `releases/` | ✅ live — frozen release history | Grew out of **Phurin's** `harrow-vale-skills/` (2026-07-23, `dcac354`), renamed by Lee's layout refactor `e5e2fa9` |
| `tools/termsheet-harness/` | ⚠️ **earlier prototype, leftover artefact** | **Lee**, 2026-07-26 (`b4fa838`, "Integrate harness, demo, and canonical project assets") |
| `assets/source/` | ✅ captured input documents | Lee, 2026-07-27, during the layout refactor |
| `harrow-vale-skills/` | ❌ gone — became `releases/` | Phurin, deleted in `e5e2fa9` |

**Correcting one thing in the record:** the recollection was that Phurin built the gate and
pipeline. Close, but it splits differently — **Phurin** built the *versioned release structure* and
the evaluation evidence (`harrow-vale-skills/`, the CONTRIBUTING guide, `eval-results.md`, the
v1.0.0 reference files) which became `releases/`. **Lee** built the gate scripts
(`gate.py`, `publish.py`, `check_published.py`). **Emily** built the skill itself. All three
contributions are live; none is the leftover.

The only genuine leftover is `tools/termsheet-harness/` — and it is Lee's, not Phurin's.

### 🔴 Phurin's work that never merged

`origin/dd-checklist-marketplace-plugin-and-fixed-json` — commit `903368f`, 2026-07-29.
Confirmed **not an ancestor of `origin/master`**.

Two other branches are also unmerged, both Emily's and both known:
`feature/gate-packaging-check` and `feature/situate-skill`.

To re-check at any time:

```bash
for b in $(git branch -r --format='%(refname:short)' | grep -v HEAD); do
  git merge-base --is-ancestor "$b" origin/master 2>/dev/null \
    && echo "merged      $b" || echo "NOT MERGED  $b"
done
```

### Transfer list — what needs bringing across, and whether it is still needed

| # | Item | Source | Still needed? |
|---|---|---|---|
| 1 | `plugins/dd-checklist-mapper-plugin/` — `dd-checklist` packaged as an installable plugin, plus its shelf entry | Phurin's unmerged branch | **YES.** Master still has only a loose `SKILL-dd-checklist.md` in the harness, ungoverned. **Review and merge his branch — do not rebuild it.** Check for drift against the gate's fixture move in `d4e1d99`. |
| 2 | Removal of the orphaned `tools/termsheet-harness/.claude-plugin/marketplace.json` | Phurin's unmerged branch | **NO — already achieved.** Lee's refactor `e5e2fa9` removed it incidentally. Only one manifest exists on disk. Nobody recorded that it was closed, which is why it kept resurfacing. See H5. |
| 3 | `instrument-applicability.md` | `releases/…/v1.1.0/references/` — in snapshots, **never in the active plugin** | **FLAGGED, do not transfer yet.** History checked: it was never dropped, it was never there. Only ever existed in Phurin's release tree. `SKILL.md` step 4 already carries a low-resolution version of the same idea ("most items will be N/A"), so it may have been deliberately superseded. Adding a fifth reference file changes behaviour → version bump through the gate. **Decision needed from Emily or Phurin before acting.** |
| 4 | `bvca_baseline.md` | `tools/termsheet-harness/reference/` | **Probably not.** The active plugin's `standard-terms.md` supersedes it, but the two differ in content. Diff them before deleting, in case the harness version carries anything the live one lost. |
| 5 | The four term sheets under `tools/termsheet-harness/data/` | harness | **NO.** Byte-identical to `assets/source/term-sheets/`, just different filenames. Delete with the harness. |
| 6 | `run_harness.py`, `consistency_check.py` | harness | **Probably not** — `gate.py` supersedes them. |
| 7 | `dd_mapper.py` | harness | **Check.** `README.md` says the DD mapper "still runs" from here and `gate.py` does not cover it. If item 1 merges, Phurin's plugin may replace it entirely — confirm before deleting. |

**Nothing from the past few sessions needs relocating.** Every change made in this Cowork
thread — the hardening docs, the spec, the held-out fixture, the session notes — went into
`docs/`, `tools/skill-gate/fixtures/`, or the live plugin. No work landed in the prototype.

---

## Where things stand right now

| Thing | State |
|---|---|
| Claude Code version | **2.1.140** (was 2.0.51 — that gap was the root cause of the plugin confusion) |
| Namespaced slash invocation | ✅ works — `/term-sheet-review:term-sheet-review` verified live |
| CLI plugin install | ✅ working, complete plugin folder with `reference/` |
| **Desktop copy of the skill** | ❌ **`SKILL.md` only, no `reference/`** — silently improvises the checklist |
| Desktop fix | ✅ **tested and ready** — `.skill` package built, needs installing + acceptance test |
| Org migration | ⚠️ barely started — git remote and 4 of 5 `plugin.json` files still point at the old account |

**The one job outstanding for Emily:** install the `.skill` package and run the acceptance
test. Instructions in the next section.

---

## Session 1 — 2026-07-30

### What the original confusion actually was

Two unrelated faults stacked, which is why it looked like plugins were "both installed and
uninstalled":

1. **Claude Code was on 2.0.51**, ~170 releases behind. `/reload-plugins` and
   `claude plugin list` didn't exist on that build, and plugin skills weren't registering.
   Updating to 2.1.140 fixed it. This was the real cause.
2. **The install check was self-confirming.** A pre-approved shell command in
   `.claude/settings.local.json` read `.claude-plugin/marketplace.json` and reported it
   under the heading "Installed plugins:". That's the *shelf* — identical output on a
   machine with nothing installed. Removed. Ground truth is the `/plugin` panel:
   **Installed** vs **Discover**.

### A wrong turn worth remembering

Cowork concluded these plugins have no slash-command invocation, reasoning that none ships a
`commands/` directory. **That was wrong**, and it got written into five files including a
client-facing deliverable before anyone checked the docs. Skills in a `skills/` directory
*are* exposed as `/plugin-name:skill-name`; `commands/` is only the older flat-file form.

Undone on the Claude Code side (commit `df64f1a`), each file now carrying a
`Verified against Claude Code 2.1.140, 2026-07-30` stamp.

**Standing rule that came out of it:** no invocation syntax goes into any document until
someone has typed it in a live session and watched it work.

### Correction to an earlier note (logged 2026-07-30, later)

Cowork flagged "`claude plugin list` still in `publish-hv-skill/SKILL.md` line 130" as an
unfinished job. **Emily kept that line deliberately** — it's a valid, useful debugging
command on 2.1.140. The original objection only ever applied to 2.0.51 where the subcommand
didn't exist, and was over-applied.

Still worth adding: the `/plugin` panel method *below* that line, so a reader has both. Small
Claude Code job, not a bug.

---

## The Desktop `reference/` blocker — tested, fix ready

### The problem

The hand-uploaded Desktop copy of `term-sheet-review` contains **only `SKILL.md`**. Its four
reference files never came across: `dd-checklist.md`, `term-extraction.md`,
`standard-terms.md`, `output-template.md`.

**Why it's serious:** the skill still runs and still looks authoritative, but without
`reference/dd-checklist.md` it falls back on general knowledge instead of Priya's fixed
checklist. That's a silent breach of Rule 1, and nothing on screen distinguishes it from a
correct run.

Confirmed still broken as of this session — unchanged since 00:57.

### The fix, tested

`skill-creator`'s `scripts/package_skill.py` zips a whole skill folder into a `.skill`
archive that installs in one click. **Hypothesis confirmed** — built successfully with all
11 files, `reference/` intact.

### But: the two surfaces diverge by one frontmatter key

First attempt **failed validation**:

```
Unexpected key(s) in SKILL.md frontmatter: argument-hint.
Allowed: allowed-tools, compatibility, description, license, metadata, name
```

`argument-hint` is valid for a Claude Code **plugin** skill and **rejected** by the Desktop
**personal** skill schema. So byte-identical `SKILL.md` cannot ship to both surfaces. It was
stripped from the packaged copy only — **the repo source is untouched**.

**Implication for the gate:** the new packaging check verifies referenced files exist, which
is right. It should *also* validate the frontmatter against the Desktop schema — otherwise a
skill can pass the gate and still be unpackageable for Desktop, discovered at upload time on
demo morning.

### 👉 Emily's next job — install and verify

1. **Install the package.** Use the `term-sheet-review.skill` file Cowork produced (look for
   the card with a **Save skill** button). One click installs it with `reference/` intact.
2. **Confirm the old copy doesn't shadow it.** There was already a `term-sheet-review` skill
   on Desktop with only `SKILL.md`. If you're offered a choice, overwrite. If both end up
   present, remove the incomplete one.
3. **Restart the Desktop session.** Newly installed skills load at session start.
4. **Run the acceptance test.** In a fresh Cowork/Desktop session, ask:

   > Review assets/source/term-sheets/safe-nimbus-robotics.md against our DD checklist

5. **Judge it against these criteria.** It fired correctly only if *all* hold:

   - Output uses **Parts A / B / C / D** (from `reference/output-template.md`)
   - Instrument **SAFE**; cap **£6,000,000 flagged as post-money**; discount **20%**;
     **MFN present and flagged**; pro-rata **yes**; interest and maturity **none, and stated
     as correct for a SAFE** rather than missing
   - **All 28 checklist items** present, each with PRESENT / MISSING / N/A
   - Items appear in **Priya's exact wording** — a general-knowledge fallback won't
     reproduce phrasing like "Customer contracts above £50,000 annual value"
   - It did **not** search for a checklist — a real run reads its own bundled
     `reference/dd-checklist.md`

**The wording check in bullet 4 is the decisive one.** Everything else can be faked by a
competent guess; Priya's exact item phrasing cannot.

If it passes, the blocker is closed on both surfaces and Phase 2 of `PLAN.md` unblocks.

---

## Desktop install — DONE, acceptance test run (contaminated)

**Install verified objectively.** `.skill` package installed; the Desktop skill folder now
holds all 11 files with `reference/`, `examples/` and `templates/` intact (timestamp 23:30).
This is disk evidence, independent of anything a model says. **The blocker is closed.**

**Acceptance test run in-session.** Results against the criteria:

| Criterion | Result |
|---|---|
| Parts A / B / C / D structure | ✅ conforms to `reference/output-template.md` |
| SAFE, correct signals cited | ✅ |
| Cap £6,000,000 flagged post-money | ✅ flagged 🔴 with founder-dilution reasoning |
| Discount 20% | ✅ (within the 10–25% standard band, so correctly *not* flagged) |
| MFN present and flagged | ✅ 🔴 |
| Pro-rata yes | ✅ |
| Interest / maturity none, stated as correct for a SAFE | ✅ not treated as missing |
| All 28 items, each with a status | ✅ 0 PRESENT / 0 MISSING / 28 N/A out of 28 |
| Priya's exact item wording | ✅ verbatim, in her order |

**Caveat, stated plainly:** this session had already discussed the expected answers at
length, so the run does **not** independently prove the reference files are being *read*.
The disk check proves installation; a fresh session with no prior context is the clean
behavioural test. Worth doing before demo day.

### One finding worth keeping

The review surfaced a drafting issue in the Nimbus SAFE that had not come up in any prior
discussion: **"Discount Price" is defined as "price per share … × Discount Rate"**. Read
literally with a 20% rate, that gives a price at 20% *of* the financing price — an 80%
discount — not a 20% discount. The economic gap between the two readings is very large.

Also confirmed as *not* a contradiction: the terms table says conversion at the **lower** of
cap price or discount price, while the Events section says the **greater** of
`Purchase Amount ÷ Discount Price` or `÷ Safe Price`. Dividing by the lower price yields the
greater share count, so these reconcile. A naive checker would flag this as an inconsistency;
it isn't.

Both are useful demo material — they're the kind of thing that distinguishes a real review
from a formatting exercise, and neither is retrievable from general knowledge about SAFEs.

**Housekeeping:** the source file `assets/source/term-sheets/safe-nimbus-robotics.md` ends
with a "NOTES vs BVCA baseline (for skill)" section — authoring scaffolding left in the mock
document. Excluded from extraction and flagged. Harmless for a mock, but worth deciding
whether it should be stripped before anything is shown to a client.

---

## 🚨 Clean-session test — blocker closed, but Rules 1 and 2 are being breached

Fresh Claude Code session, no prior context. **This is the test that counts.**

### What it proved (good)

The tool trace shows all four reference files read: `dd-checklist.md`, `term-extraction.md`,
`standard-terms.md`, `output-template.md`. **The `reference/` bundling blocker is closed and
verified on both surfaces.** That question is settled.

### What it exposed (bad — and this is the important part)

**1. The run did not do the work. It recognised the answer and served the answer key.**

The agent said so plainly: *"my extraction and flagging match the worked review already on
file at `examples/review-safe-nimbus.md`, so I've verified and am presenting that as the
completed review rather than duplicating it."*

Confirmed verbatim: the `0 PRESENT / 1 MISSING / 1 PARTIAL / 26 N/A` tally is line 86 of that
example file.

**Consequence: the acceptance test is an open-book exam.** The skill ships worked reviews for
**all four** sample term sheets — Nimbus, GreenGrid, Anchorline, Solace. Any test using those
four documents can be passed by reading `examples/`, without extracting anything. Every
"verification" run to date has been contaminated this way, including the one designed in this
session.

**2. The shipped answer key breaches Rule 1 — 22 of 28 checklist items are renamed.**

Rule 1 is *"Never invent, rename, or merge checklist items."* Measured against
`reference/dd-checklist.md`, `examples/review-safe-nimbus.md` paraphrases 22 of the 28:

| Priya's wording | Shipped example |
|---|---|
| Full capitalisation table, fully diluted | Fully-diluted cap table |
| Customer contracts above £50,000 annual value | Customer contracts >£50k/yr |
| Last two years' audited (or management) accounts | Last 2 years' accounts |
| Directors' & officers' liability insurance | D&O liability insurance |
| Any transactions between the company and its directors/major shareholders | Company ↔ director/major-shareholder transactions |

…and 17 more. Because the model pattern-matches on the example rather than the checklist, the
paraphrasing propagates into live output. **The artefact meant to demonstrate Rule 1
compliance is the thing violating it.**

**3. `PARTIAL` is an invented fourth status.** The sanctioned set is PRESENT / MISSING / N/A —
in `SKILL.md`, in `reference/`, and in the lawyer guide. `PARTIAL` appears in **3 of the 4**
shipped examples and is sanctioned nowhere. It may well be a *good* idea; it is currently an
undocumented one.

**4. The delivered Part C collapsed to prose — Rule 2 breach.** Rule 2 requires every item to
appear with an explicit status. The output summarised instead: *"Every other item across
Corporate Structure, Material Contracts, IP, Employment… is N/A."* Twenty-six items were
asserted as covered without being shown. Silence is exactly what Rule 2 forbids.

**5. It stated a legal conclusion.** *"Nothing here blocks signing"* — the skill's own
self-check requires that no flag "assert a final legal conclusion", and the role is explicitly
*"you are a careful associate, not the partner"*. That sentence is the partner's call.

**6. It missed a real drafting defect** that the contaminated in-session run did catch: the
`"Discount Price" = price per share × Discount Rate` definition, which read literally gives an
80% discount rather than 20%.

### Why the gate cannot see any of this

The gate scores **recorded fixtures**, not live runs. Items 1–6 all occur at run time, in the
gap the gate does not cover. Same shape as the two gaps already in `PLAN.md` Phase 1c
(packaging, runtime version). This is now the third instance of one underlying issue:
**everything verified about this skill is verified somewhere other than where the lawyer
actually uses it.**

### Fixes, in priority order

- [ ] **Regenerate all four worked examples with verbatim checklist wording.** Mechanical,
      and it removes the Rule 1 breach at source.
- [ ] **Add a deterministic gate check:** every checklist item string appearing in an example
      or output must match `reference/dd-checklist.md` **exactly**. Rule 1 becomes
      machine-enforced rather than aspirational — and it is exactly the kind of check the gate
      is good at.
- [ ] **Decide on `PARTIAL`.** Either sanction it properly across `SKILL.md`, `reference/`,
      the output template and the lawyer guide, or remove it from the examples. Not left
      undocumented.
- [ ] **Forbid serving a stored example as a fresh run's output.** Add it to `SKILL.md` as an
      explicit prohibition — the model must do the extraction even when it recognises the
      document.
- [ ] **Acceptance-test on a document with no worked example.** Any of the four sample sheets
      is now unusable for verification. Write a fifth term sheet, keep it out of `examples/`,
      and treat it as the held-out test case.
- [ ] **Add Part C enumeration and "no legal conclusions" to the self-check** in a form that
      cannot be satisfied by a summary sentence.

### Honest read for the demo

The governance story is still the strongest thing here — but it is currently *"the gate proves
the skill was right once, in a recording"*. Priya's three rules are the product claim, and two
of them are being breached by the shipped artefacts today. Better to fix the wording, add the
verbatim check, and demo **that** — a rule made mechanically enforceable is a far better beat
than a rule asserted.

---

## Open on the Cowork side (not started)

- **Package `situate` v0.1.0** the same way — it also has a `reference/` folder (three
  files). Confirm whether it hits the same `argument-hint` wall.
- **Org migration / private-flip readiness note.** More URLs need updating than the briefing
  lists: the **git remote itself** is still `f7-rage-gremlin/HarrowValeLLP`, and **4 of 5**
  `plugin.json` `repository` fields still point there (only `situate` was updated). If the
  repo goes private before those are fixed, the marketplace source breaks for everyone.
- **Deck choice** — `presentation/harrowvale-presentation.html` (older, 11 slides) vs
  `presentation-day/harrow-vale-presentation.html` (newer, PR #9). Plus the open question of
  whether the hardening story belongs in the deck at all.
- **Client deliverable review** — tone, consistency, and anywhere they overpromise. Note
  that cross-surface consistency now has a real caveat worth wording carefully.

---

## Built this session — ready for Claude Code

Three new files. Nothing else in the repo was touched.

| File | What it is |
|---|---|
| `docs/governance/verbatim-checklist-check-spec.md` | Implementation spec for the verbatim check, plus the three content fixes that must land with it |
| `tools/skill-gate/fixtures/term-sheet-review/heldout/documents/heldout-01-vantor-health.md` | Fifth term sheet — prose letter format, never seen by the skill, with deliberate traps |
| `tools/skill-gate/fixtures/term-sheet-review/heldout/labels/…labels.json` | Expected answers as **structured labels, not a prose review** — so they can't be copied into an output and passed off |
| `tools/skill-gate/fixtures/term-sheet-review/heldout/README.md` | The one rule: never write a worked review for a held-out document |

### The held-out document's traps

Deliberately chosen so that each one tests a *stated* behaviour of the skill rather than
general competence:

- **Instrument conflict** — presented as a SAFE, but carries 6% compounding interest and a
  24-month maturity. `SKILL.md` step 1 says report the conflict, don't force a category.
- **Arithmetic inconsistency** — "£1,200,000 for 15% … implying a post-money valuation of
  £6,000,000" (it implies £8m). `term-extraction.md` says report as stated and flag; never
  recompute or correct.
- **Over-flagging trap** — a 22% discount, inside the 10–25% standard band. Flagging it is a
  false positive and should cost marks. A review that flags everything is as useless as one
  that flags nothing.
- **Fabrication trap** — governing law is absent. All four shipped samples say England and
  Wales, so a model working from familiarity rather than the document will fill it in. That's
  a Rule 3 breach.
- **Prose-letter format** — no tables, no term headings. The four samples are a table, a
  priced sheet, a note and a bullet list. Tests the structure-independence the skill claims.
- Plus the genuinely off-market terms: 1.5x participating preference, full-ratchet
  anti-dilution described without using the term, single-trigger acceleration, uncapped
  investor legal fees, 2-of-4 board seats on a 15% stake, and consent over budgets and any
  hire above £45,000.

### Session 2 additions — 2026-07-31

**Hardening directory created:** `docs/hardening/`, one document per issue, plus `INDEX.md`.
There was no existing hardening doc, so H1 and H2 were backfilled from `PLAN.md` and
`PROGRESS.md` to make the set coherent. H3 (answer-key contamination) and H4 (duplicate
projects) are new and written in full.

The index makes a point worth carrying into the demo: **all four incidents are the same failure
mode** — something verified somewhere other than where it is used. That is the boundary of the
gate, not a defect in it, and naming the boundary is more credible than implying it is covered.

**`PARTIAL` downgraded to deferred.** Not a blocker. The spec now says to implement the check
with `PARTIAL` temporarily permitted and a `TODO: D1` comment, so the valuable assertions land
now. Decide it if there's time.

**Two projects — confirmed, and it's worth untangling.** See
`docs/hardening/H4-duplicate-overlapping-projects.md`. Short version:

- Two skills both named `term-sheet-review` — the plugin (106 lines, Parts A–D, 28-item
  coverage) and `tools/termsheet-harness/SKILL.md` (61 lines, "Exception Report", its own
  BVCA baseline). Same frontmatter name, different output contracts.
- A third skill definition, `dd-checklist`, in `tools/termsheet-harness/SKILL-dd-checklist.md` —
  not on the marketplace, not in `plugins/`, not registered with the gate. Ungoverned, and
  arguably more useful to the firm than single-sheet review.
- The four term sheets exist twice, byte-identical, under different filenames.
- Two different "standard" baselines — `reference/standard-terms.md` and
  `reference/bvca_baseline.md` — with no statement of which governs.

**Demo note:** don't show both systems. "Here is our gate" is strong; "here is our gate, and
also this other evaluator, and these two baselines" invites the question you least want on
stage.

### One decision, deferred (D1)

**Is `PARTIAL` a sanctioned status or not?** It appears in three of the four shipped examples
and nowhere in `SKILL.md`, `reference/`, or the lawyer guide — which tells lawyers there are
exactly three statuses.

It's arguably a genuinely useful category: *"this SAFE is one such instrument, but the others
weren't provided"* is honestly neither PRESENT nor MISSING nor N/A. But right now it is an
undocumented fourth category invented at run time, which is the shape of a Rule 1 breach.

Either sanction it properly everywhere, or remove it from the examples. **Emily or Priya
decides — not the implementer**, and the spec blocks on it deliberately.

---

## For Claude Code (paste-back queue)

Small, verified items to hand back next time Emily is in a Claude Code session:

- [ ] Add the `/plugin` panel method below the `claude plugin list` line in
      `.claude/skills/publish-hv-skill/SKILL.md` — keep the CLI command, it's useful.
- [ ] Extend the gate's packaging check to validate `SKILL.md` frontmatter against the
      **Desktop personal-skill schema** (`allowed-tools`, `compatibility`, `description`,
      `license`, `metadata`, `name`). `argument-hint` passes the plugin schema and fails
      Desktop's — currently invisible until upload.
- [ ] Update the git remote and the 4 remaining `plugin.json` `repository` fields to
      `Harrow-Vale-Demo/HarrowValeLLP` **before** any decision to flip the repo private.
- [ ] **Implement `docs/governance/verbatim-checklist-check-spec.md`** — the check, plus the
      three content fixes that must land with it. Blocks on decision D1 (`PARTIAL`).
- [ ] Decide whether to strip the "NOTES vs BVCA baseline (for skill)" scaffolding section from
      `assets/source/term-sheets/safe-nimbus-robotics.md` before anything is shown to a client.
- [ ] Later, separate change: wire the held-out fixture into `gate.py` as a scored case. Needs
      a scoring approach for structured labels, which the existing fixtures don't use.
