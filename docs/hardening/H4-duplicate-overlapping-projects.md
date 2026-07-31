# H4 — Two parallel term-sheet systems, and two skills with the same name

**Found:** 2026-07-31, prompted by Emily asking whether existing vetting machinery already covered the new checks
**Class:** Source-of-truth integrity
**Status:** Open
**Severity:** Medium now, high if either the checklist or a skill definition is ever edited in the wrong copy.

---

## The question that found it

> *"Can I just check there is not stuff in the directory in place to vet and check these term
> sheets along those criteria already? There might be two projects in there already and maybe
> that's confusing things?"*

Not paranoia. There are two, and the overlap is substantial.

## The two systems

| | `tools/skill-gate/` | `tools/termsheet-harness/` |
|---|---|---|
| Purpose | Firm-wide approval gate for any skill | Term-sheet-specific evaluator + DD mapper |
| Entry points | `gate.py`, `publish.py`, `check_published.py` | `run_harness.py`, `dd_mapper.py`, `consistency_check.py` |
| Fixtures | `fixtures/<skill>/golden.json` + `runs/` | `data/`, `golden/`, `contract/` |
| Standard baseline | via the plugin's `reference/standard-terms.md` | its own `reference/bvca_baseline.md` |
| Status per `README.md` | "the single approval gate", "the only sanctioned publisher" | "still runs" |

`README.md` documents both as live. So this is a known, unconsolidated overlap rather than an
accident — but the specific duplications below are riskier than "we have two tools".

## What is duplicated

### 1. Two skills named `term-sheet-review`, with different output contracts

| | Plugin | Harness |
|---|---|---|
| Path | `plugins/term-sheet-review-plugin/skills/term-sheet-review/SKILL.md` | `tools/termsheet-harness/SKILL.md` |
| Length | 106 lines | 61 lines |
| `name:` | `term-sheet-review` | `term-sheet-review` |
| Output | Parts A–D, checklist coverage, all 28 items | "Exception Report" — non-standard and missing, as actionable bullets |
| Baseline | `reference/standard-terms.md` | "the firm's BVCA-aligned baseline" |

**Same skill name, different behaviour, different output shape.** Only the plugin one is on the
marketplace, so today only one can be installed — but the frontmatter name is identical, and
anything that loads skills by directory scan would see both. Given how much of this week went
on skills being loaded from unexpected places, this is a live hazard rather than a theoretical
one.

### 2. A third skill definition nobody registered

`tools/termsheet-harness/SKILL-dd-checklist.md` declares a skill named `dd-checklist` — maps a
folder of DD documents against the checklist, "the Thursday afternoon dump" use case. It is not
in `marketplace.json`, not in `plugins/`, and not registered with the gate. It is a real skill
definition sitting outside all governance.

**CORRECTED 2026-07-31.** The paragraph above is wrong in an important way. It said this should
"be promoted through the gate properly" — **Phurin already did exactly that, and the work never
merged.**

Commit `903368f` on branch `dd-checklist-marketplace-plugin-and-fixed-json`:

- creates `plugins/dd-checklist-mapper-plugin/` with a proper `plugin.json`, `SKILL.md`, and its
  own `reference/dd-checklist.md`
- lists it on the root shelf in `marketplace.json`
- removes the orphaned duplicate manifest (see [H5](H5-orphaned-marketplace-manifest.md))

Verified: `903368f` is **not** an ancestor of `origin/master`. So master still carries the loose
`SKILL-dd-checklist.md` and no packaged plugin.

The skill is good, and the use case is arguably worth more to the firm than single-term-sheet
review — Tom's actual trigger, in its own words: *"opposing counsel dumps ~30 documents at 4:30pm;
feedback due by Friday noon."*

**Action is "review and merge Phurin's branch", not "build this".** Check it for drift against
subsequent master changes — particularly the gate's fixture layout, which moved in `d4e1d99` — but
do not reimplement it.

### 2b. Three status vocabularies, never reconciled

This is the actual source of the `PARTIAL` confusion in
[H3](H3-answer-key-contamination.md), and it only becomes visible with all three artefacts side
by side:

| Artefact | Statuses |
|---|---|
| Active plugin `SKILL.md`, output template, lawyer guide | PRESENT / MISSING / N/A |
| Phurin's `dd-checklist` skill (unmerged) | satisfied / **partial** / missing |
| `releases/…/references/instrument-applicability.md` | Expected / Relevant / N/A |

`PARTIAL` was not invented from nothing. It is coherent with Phurin's design, which defines it
precisely: *"If a document only partially covers an item (e.g. an extract), mark `partial` and say
what's still needed."*

Decision **D1** should therefore be taken across all three vocabularies at once. Three overlapping
status sets is the defect; the undocumented `PARTIAL` is a symptom of it.

### 2c. A reference file missing from the shipping skill

`instrument-applicability.md` exists in `releases/term-sheet-review/v1.0.0/references/` and
`v1.1.0/references/` — but **not** in the active plugin's `reference/`, which holds only
`dd-checklist.md`, `output-template.md`, `standard-terms.md`, `term-extraction.md`.

Its purpose, from its own header: *"Prevents the skill from wrongly flagging a SAFE as 'omitting'
things that were never meant to be in a SAFE."*

That is exactly the over-flagging discipline the held-out fixture was built to test.

**History checked 2026-07-31 — it was never dropped, because it was never there.** The file has
only ever existed at two paths, both inside Phurin's versioned release tree:

- `harrow-vale-skills/plugins/term-sheet-review/v1.0.0/references/` — Phurin, `dcac354`, 07-23
- `harrow-vale-skills/plugins/term-sheet-review/v1.1.0/references/` — Emily, `adbe113`, 07-25

It has **never** existed in `plugins/term-sheet-review-plugin/skills/term-sheet-review/reference/`.
So this is not a refactor casualty. Two possibilities remain, and they have different fixes:

**(a) The release snapshots are not faithful copies of the active plugin.** They are a parallel,
slightly richer artefact. If so, the snapshots overstate what was released, and the honest fix is
to make snapshots mechanically derived from the plugin rather than hand-assembled.

**(b) It was intended as skill guidance and never wired in.** Emily carried it forward into v1.1.0
by hand, which suggests it was considered live.

There is also a partial refactor: `SKILL.md` step 4 collapses the whole applicability question into
one line — *"For a single term sheet, most items will be `N/A (not a DD document set)`"*. That is
the same idea at much lower resolution, losing the per-instrument nuance (a priced round *should*
address Articles and cap-table reconciliation in the sheet; a SAFE should not).

**Do not reinstate it unilaterally.** It may have been deliberately superseded by that `SKILL.md`
line, and adding a fifth reference file changes skill behaviour, which means a version bump through
the gate. Decide (a) vs (b) first — Emily or Phurin, since Phurin wrote it.

Regardless of the decision, the check is worth having: **assert the active plugin's `reference/`
file set matches the latest release snapshot's**, so the two artefacts can never silently disagree
about what the skill contains.

### 3. The four term sheets exist twice, byte-identical

| `assets/source/term-sheets/` | `tools/termsheet-harness/data/` |
|---|---|
| `safe-nimbus-robotics.md` | `nimbus-safe.md` |
| `series-a-greengrid-analytics.md` | `greengrid-series-a.md` |
| `convertible-note-anchorline-biotech.md` | `anchorline-convertible.md` |
| `seed-solace-data.md` | `solace-seed.md` |

All four verified identical in content, under different filenames. Two names for one document
is how a fix gets applied to one copy and not the other.

### 4. Two different "standard" baselines

`plugins/…/reference/standard-terms.md` and `tools/termsheet-harness/reference/bvca_baseline.md`
have **different content**. Both describe what counts as market-standard. Which one is
authoritative is undocumented. If a lawyer disputes a flag, there are two possible answers to
"what did you compare it against".

### 5. Six copies of the DD checklist

Covered below, because it is also the answer to a separate question.

## The checklist copies — and what they show

Six files, four distinct file hashes:

| File hash | Item-text hash | Path |
|---|---|---|
| `5327f82f` | `01e65f1c` | `assets/source/dd-checklist/harrow-vale-dd-checklist.md` ← canonical client document |
| `bd186076` | `01e65f1c` | `plugins/…/skills/term-sheet-review/reference/dd-checklist.md` ← **what the skill reads** |
| `8cb27dfb` | `01e65f1c` | `releases/term-sheet-review/v1.0.0/references/dd-checklist.md` |
| `8cb27dfb` | `01e65f1c` | `releases/term-sheet-review/v1.1.0/references/dd-checklist.md` |
| `5327f82f` | `01e65f1c` | `tools/termsheet-harness/reference/dd-checklist.md` |
| `4283d5f8` | — | `tools/termsheet-harness/SKILL-dd-checklist.md` (a skill definition, not a checklist) |

**The good news, stated precisely:** all five real copies have **identical item text** — 28
items, same wording, same order (`01e65f1c`). The four differing file hashes are markup only:
`- item` versus `- [ ] item`, and a mock-document HTML comment. **There is no semantic drift
today.**

**The bad news:** that is luck and diligence, not structure. Nothing asserts it. Five copies
maintained by hand, with the authoritative one undeclared, is a drift generator with the drift
not yet having happened.

## Fixes

- [ ] **Declare one canonical checklist.** `assets/source/dd-checklist/harrow-vale-dd-checklist.md`
      is the captured client document and the natural root of trust. State it in `CLAUDE.md`.
- [ ] **Assert derivation, not equality.** Add to `check_verbatim.py`: the plugin's
      `reference/dd-checklist.md` must have identical **normalised item text** to the canonical
      file. Compare item text, not file bytes — the markup difference is legitimate.
- [ ] **Record the canonical hash with provenance.** A small `PROVENANCE.md` or a field in the
      gate config: the item-text hash, the date, and who approved it. A change to the canonical
      file then requires updating a recorded, reviewed value — it cannot be a silent edit.
- [ ] **Resolve the two `term-sheet-review` skills.** Either rename the harness one (e.g.
      `term-sheet-exception-report`) or move it under `docs/` as a design record. Two live skill
      definitions with the same name is not survivable long-term.
- [ ] **Decide on `dd-checklist`.** Promote it through the gate, or move it out of `tools/`.
      Currently it is an ungoverned skill definition.
- [ ] **De-duplicate the term sheets.** Point the harness at `assets/source/term-sheets/`
      rather than keeping a second copy under different filenames.
- [ ] **Reconcile the two baselines**, or document explicitly which governs and why the other
      exists.
- [ ] **Decide the future of `termsheet-harness`.** Consolidate into `skill-gate`, or scope it
      down to the DD-mapper function that `skill-gate` does not cover, and say so in `README.md`.

## Note for the demo

Do not show both systems. "Here is our gate" is a strong story; "here is our gate, and also
this other evaluator, and these two baselines" invites exactly the question you do not want on
stage. Pick `skill-gate`, and if the harness comes up, describe it accurately as the earlier
prototype the gate generalised.
