# Handover 02 → Claude Code

> Written 2026-07-31 from a Cowork session. Supersedes `HANDOVER-to-claude-code.md`, whose Jobs
> 1–5 are all closed (Job 2 was closed by decision — see note below).
>
> **Read the reconciliation note first.** The Claude Code side appears to have independently found
> some of the same issues. Where that is true, reconcile rather than duplicate — and if your record
> disagrees with anything here, your record was probably written from the live machine and wins.
>
> Delete this file when the jobs are done. Log outcomes in `LEDGER.md`.

---

## Reconciliation note — we may have found the same bugs

Emily's read is that the Claude Code side caught similar or the same issues. Likely overlaps:

| Issue | If you already have it | Action |
|---|---|---|
| The `examples/` answer-key contamination | You may have found it via a different route | Compare against `docs/hardening/H3-answer-key-contamination.md`; merge the records, don't keep two |
| Checklist item paraphrasing (22 of 28) | Possibly recorded as a wording nit | H3 has the full measured table |
| Phurin's unmerged branch | You may have already merged it | **Check first.** If merged, Job 1 below is done — verify against the blocker list rather than skipping it |
| `PARTIAL` as an unsanctioned status | Possibly flagged | See H4 §2b — there are actually *three* status vocabularies, which reframes it |

**One thing to correct if your record says otherwise:** `claude plugin list` is a *valid, useful*
command on 2.1.140. An earlier Cowork session wrongly flagged it as a defect — that objection only
ever applied to 2.0.51, where the subcommand didn't exist. HANDOVER 01 Job 2 was therefore closed by
Emily's decision to keep the line. The only outstanding nicety is adding the `/plugin` panel method
*beside* it, not instead of it.

---

## Environment constraints

- **NixOS.** No `npm install -g`, no `pip install --user`, no `curl … | sh`, no `sudo` to install
  software. Tooling comes from the nix configuration or a dev shell.
- **Ask before** `git push`, deleting files, or anything reaching outside this project.
- Do not edit anything under `releases/` in place — see `releases/CONTRIBUTING.md`.
- `gate.py --all` and `check_published.py` must be green before you commit.

---

## Job 1 — Merge Phurin's `dd-checklist` branch ⭐ do this first

**Branch:** `origin/dd-checklist-marketplace-plugin-and-fixed-json`
**Commit:** `903368f`, Phurin Rintanalert, 2026-07-29
**Verified:** not an ancestor of `origin/master`. Unmerged for two days, during which its diagnosis
was rediscovered from scratch by two separate sessions.

### What it contains

| Change | Status on master |
|---|---|
| `A plugins/dd-checklist-mapper-plugin/.claude-plugin/plugin.json` | missing — needed |
| `A plugins/dd-checklist-mapper-plugin/skills/dd-checklist/SKILL.md` | missing — needed |
| `A plugins/dd-checklist-mapper-plugin/skills/dd-checklist/reference/dd-checklist.md` | missing — needed |
| `M .claude-plugin/marketplace.json` — adds the shelf entry | needed |
| `D tools/termsheet-harness/.claude-plugin/marketplace.json` | **already gone** — removed incidentally by Lee's refactor `e5e2fa9`. This half of his fix is redundant. |

Merge base is `071bd2b` (2026-07-28). His branch touches 5 files; master has touched 101 since.

### Expected conflicts — only one real

**`.claude-plugin/marketplace.json` — will conflict, resolution is additive.** Master has grown to
four entries (`term-sheet-review`, `leestestskill`, `mock-skill`, `situate`); his branch adds a fifth
to a two-entry version. Keep all four from master and add his entry. No entry should be lost.

`tools/termsheet-harness/.claude-plugin/marketplace.json` is deleted on both sides, so git resolves
it without help.

### 🚨 Blocker: merging as-is will fail `check_published.py`

His branch predates the gate landing on master (`03c7288`, 07-29). `check_published.py` requires, for
every shelf entry:

1. `plugin.json` version agrees with the marketplace entry — ✅ both say `1.0.0`
2. `releases/<name>/v1.0.0/gate-report.json` exists and records a PASS — ❌ **absent**
3. …or a `PRE_GATE_APPROVED` entry — ❌ absent
4. …or a passing recorded run, which needs registration in `gate.py`'s `SKILLS` dict — ❌ **not
   registered**
5. `SKILL.md` reports the version it ships as — ❌ verify; his `SKILL.md` has no version marker

So a plain merge puts a plugin on the shelf with no gate evidence, and CI goes red. That is the gate
working correctly.

### Two ways through — Emily decides

**(a) Merge the plugin, hold it off the shelf.** Take the three new files, leave
`marketplace.json` alone. His work is preserved and reviewable; it just isn't published until it has
been through the gate. Lowest risk, and consistent with the documented model that publishing is a
separate deliberate act.

**(b) Take it all the way through the gate now.** Write `fixtures/dd-checklist/golden.json`, record a
run, register it in `SKILLS`, run `gate.py`, then `publish.py`. Correct, but it is a full skill
publication and not a merge.

**Recommend (a)** unless the DD-mapper is wanted in the demo — in which case (b), with time budgeted
for golden labels.

### Naming decision while you are in there

His marketplace entry is `dd-checklist-mapper-plugin`. Every other entry drops the suffix — the
directory is `term-sheet-review-plugin` but the shelf name is `term-sheet-review`. Consistency
suggests `dd-checklist` or `dd-checklist-mapper`. It also determines the evidence path
(`releases/<name>/v1.0.0/`), so settle it before generating any gate artefacts.

### Do not reimplement

The skill is good and the use case is arguably worth more to the firm than single-sheet review —
Tom's actual trigger, in its own words: *"opposing counsel dumps ~30 documents at 4:30pm; feedback
due by Friday noon."* Review and merge it. Check for drift against the gate's fixture-layout move
(`d4e1d99`), but do not rebuild what Phurin already built.

---

## Job 2 — `instrument-applicability.md`: flagged, needs a decision, do NOT act unilaterally

`instrument-applicability.md` exists in `releases/term-sheet-review/v1.0.0/references/` and
`v1.1.0/references/`, but **not** in the active plugin's `reference/`.

**History checked — it was never dropped, because it was never there.** Its only two paths, ever:

- `harrow-vale-skills/plugins/term-sheet-review/v1.0.0/references/` — Phurin, `dcac354`, 07-23
- `harrow-vale-skills/plugins/term-sheet-review/v1.1.0/references/` — Emily, `adbe113`, 07-25

Its purpose, from its own header: *"Prevents the skill from wrongly flagging a SAFE as 'omitting'
things that were never meant to be in a SAFE."* It maps each checklist item to
Expected / Relevant / N/A per instrument type.

**Why not to just add it back:**

- `SKILL.md` step 4 already carries a low-resolution version of the same idea — *"For a single term
  sheet, most items will be `N/A (not a DD document set)`"*. It may have been deliberately
  superseded.
- Adding a fifth reference file **changes skill behaviour**, so it needs a version bump through the
  gate, not a quiet commit.
- It introduces a *third* status vocabulary (Expected / Relevant / N/A) on top of the two already in
  play. See Job 4.

**The question to answer:** are the release snapshots faithful copies of the active plugin, or a
parallel richer artefact? If the former, the snapshots currently overstate what was released and
should be mechanically derived rather than hand-assembled. Emily or Phurin decides — Phurin wrote it.

**Worth adding either way:** assert that the active plugin's `reference/` file set matches the latest
release snapshot's, so the two artefacts cannot silently disagree about what the skill contains.

---

## Job 3 — Implement the verbatim checklist check

Spec: **`docs/governance/verbatim-checklist-check-spec.md`** — read it in full, it is the
implementation brief.

Summary: build `tools/skill-gate/check_verbatim.py` asserting that Part C of any review reproduces
Priya's 28 items **verbatim**, in order, with all 9 section headings, each carrying an allowed status.
Rule 1 is a string-equality property, so it is mechanically enforceable — which is a much stronger
thing to show Tom than a paragraph promising care.

Two points that are easy to get wrong:

- **Normalise whitespace only.** Not case, not ampersands, not `and` vs `&`. Those *are* the
  differences Rule 1 is about; a forgiving comparator defeats the purpose.
- **Canonical source is the plugin's own `reference/dd-checklist.md`** (Emily's decision, 07-31).
  Everything else derives from it. `releases/` copies are exempt as frozen snapshots.

It will fail on the current tree — 22 of 28 items in `examples/review-safe-nimbus.md` are
paraphrased. **Fix the content, not the check.** Change only the item text and status formatting;
leave the analysis and commentary alone, it was approved.

Measured state, so you know what you're starting from: five real copies of the checklist exist, with
**four different file hashes but identical item text**. No semantic drift today — but nothing asserts
it, and it is maintained by hand.

---

## Job 4 — Reconcile the three status vocabularies (decision D1, deferred)

**Deferred by Emily 2026-07-31 — nice-to-have, not a blocker.** Implement Job 3 with `PARTIAL`
temporarily permitted and a `TODO: D1` comment.

Recorded so the decision stays deliberate. Three vocabularies exist:

| Artefact | Statuses |
|---|---|
| Active plugin `SKILL.md`, output template, lawyer guide | PRESENT / MISSING / N/A |
| Phurin's `dd-checklist` skill (Job 1) | satisfied / **partial** / missing |
| `releases/…/instrument-applicability.md` (Job 2) | Expected / Relevant / N/A |

`PARTIAL` was not invented from nothing — Phurin defines it precisely: *"If a document only partially
covers an item (e.g. an extract), mark `partial` and say what's still needed."* Three overlapping
status sets is the real defect; the undocumented `PARTIAL` is the symptom.

Decide across all three at once, not for term-sheet-review in isolation. Priya or Emily.

---

## Job 5 — Small, verified, safe to do any time

- [ ] Add the `/plugin` panel method **beside** the `claude plugin list` line in
      `.claude/skills/publish-hv-skill/SKILL.md`. Keep the CLI command — it is valid on 2.1.140.
- [ ] Extend the gate's packaging check to validate `SKILL.md` frontmatter against the **Desktop
      personal-skill schema** (`allowed-tools`, `compatibility`, `description`, `license`,
      `metadata`, `name`). `argument-hint` passes the plugin schema and **fails** Desktop's — found
      when packaging for Desktop, currently invisible until upload time.
- [ ] Assert **exactly one `marketplace.json`** exists, at the repo root, and that every `source`
      path resolves to a directory containing `.claude-plugin/plugin.json`. Two lines; would have
      caught the orphan Phurin found. See `docs/hardening/H5-orphaned-marketplace-manifest.md`.
- [ ] Update the git remote and the **4 remaining** `plugin.json` `repository` fields to
      `Harrow-Vale-Demo/HarrowValeLLP` (only `situate` was updated) **before** any decision to flip
      the repo private. The remote itself is still `f7-rage-gremlin`.
- [ ] Decide whether to strip the `NOTES vs BVCA baseline (for skill)` scaffolding section from
      `assets/source/term-sheets/safe-nimbus-robotics.md` before anything is shown to a client.
- [ ] Add an **unmerged-branch sweep** to demo prep. Job 1 exists only because someone asked about
      commit history:

      ```bash
      for b in $(git branch -r --format='%(refname:short)' | grep -v HEAD); do
        git merge-base --is-ancestor "$b" origin/master 2>/dev/null \
          && echo "merged      $b" || echo "NOT MERGED  $b"
      done
      ```

      Currently unmerged: Phurin's branch (Job 1), plus `feature/gate-packaging-check` and
      `feature/situate-skill` — both Emily's and both known.

---

## New since Handover 01

**`docs/hardening/`** — new directory, one document per issue, with `INDEX.md`. H1 and H2 were
backfilled from `PLAN.md` and `PROGRESS.md`; H3, H4 and H5 are new.

| Doc | Issue |
|---|---|
| H1 | Out-of-date runtime + an install check that confirmed itself |
| H2 | Desktop upload shipped `SKILL.md` without its `reference/` files |
| H3 | Skill ships worked answers for its own test documents; Rules 1 and 2 breached |
| H4 | Two parallel term-sheet systems; two skills named `term-sheet-review`; three status vocabularies |
| H5 | Orphaned second marketplace manifest; version pinning against a stale checkout |

**`tools/skill-gate/fixtures/term-sheet-review/heldout/`** — a fifth term sheet, prose-letter format,
never seen by the skill, with expected answers as **structured labels rather than a prose review** so
they cannot be copied and passed off. Read its `README.md`: the one rule is that **no worked review
may ever be written for it.** Traps include an instrument conflict (SAFE framing with 6% interest and
a 24-month maturity), an arithmetic inconsistency that must be flagged rather than corrected, a 22%
discount that must **not** be flagged, and an absent governing law that must read `Not stated`.

**Desktop `reference/` blocker closed.** `skill-creator`'s `scripts/package_skill.py` produces a
`.skill` archive; installed and verified on disk — 11 files, `reference/` intact.

**`docs/cowork/cowork-session-notes.md`** — running Cowork log. Its top section settles which
directory is authoritative, with provenance per path and a transfer list with keep/drop verdicts.

**Directory question settled.** `plugins/term-sheet-review-plugin/` is the live product (Emily,
07-22). `tools/termsheet-harness/` is the leftover prototype — and it is **Lee's** (07-26), not
Phurin's. Phurin built the versioned release structure that became `releases/`; Lee built the gate
scripts; Emily built the skill. All three are live. No Cowork work landed in the prototype.

---

## The honest framing for Tom

Five incidents, one shape: **something was verified somewhere other than where it is used.** The
check read the shelf instead of the machine; the gate scored a recording while the packaging went
unchecked; the test scored a document whose answer shipped inside the skill; five checklist copies
with no assertion that the one in use is the one approved; a manifest pointing at a non-plugin
directory.

That is the gate's boundary, not a defect in it. Naming the boundary and adding cheap deterministic
checks on the other side is a better story than implying the gate covers ground it does not — and
"our process caught five before a lawyer relied on any of them" is stronger than silence. A
governance system that has never found anything is not evidence of quality.
