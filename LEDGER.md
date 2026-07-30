# Shared Ledger — Harrow & Vale Engagement (Hackathon 1)

> Shared coordination log between Emily and her Claude instances.
> **Convention:** append new entries at the top of the Log section. Format:
> `### [YYYY-MM-DD HH:MM] <author> — <one-line summary>` then details.
> Don't edit others' entries; add a new one instead.

---

## Engagement at a glance

- **Client:** Harrow & Vale LLP — boutique VC/M&A law firm, Clerkenwell, London (10 lawyers).
- **Sponsor:** Tom Harrow (Ops & Knowledge Lead). **Standard-setter:** Priya Vale (Managing Partner, reviews every closing).
- **Us:** Negative Zero associates (Emily) pitching a consulting engagement.
- **Target site:** https://harrowvale.syntheticsignal.io/ — sanctioned test target.
- **Data room:** https://harrowvale.syntheticsignal.io/data-room/ (sign in with NZ identity) — sample term sheets, DD checklist, mock data room.

## Deliverables — due Wed 29 July 2026

1. **Client proposal** — approach, scope, honest time/effort estimates, priced to client budget.
2. **Solution presentation** — demo the working solution running.
3. **Next steps** — how client takes it further / next engagement.
4. **Public case study** — how Claude solved it (public-facing, Anthropic-style).

## The build

- **Core:** a Claude Skill that reviews a term sheet — extracts key economic terms
  (valuation/cap, discount, liquidation preference, board/consent, pro-rata, etc.),
  checks against Priya's DD checklist, flags deviations/omissions in plain English.
  Must work across 3 formats: **SAFE, priced round, convertible loan note.**
  Build test-driven against 2–3 real examples first.
- **Stretch:** private versioned "approved skills" repo (install + update + approval
  process) + one-page data-residency / confidentiality memo (Claude for Enterprise/Teams).

## Open questions / TODO

- [x] Recon the public site + attempt data-room access.
- [x] Pull the 3 sample term sheets + DD checklist — DONE (Emily added them; organized into `assets/`).
- [x] **Build the term-sheet review Skill** (test-driven against the 4 term sheets).
- [x] Build the DD-coverage report feature (GreenGrid = worked demo with full doc set).
- [x] Confirm client budget — £2k–£5k (from Tom's conversation screenshots).
- [x] Tom's 9 required extraction fields — all 9 now covered in v1.1.0.
- [x] Stretch: private versioned skills repo (install/update/approval) + data-residency memo.
- [x] Draft the 4 deliverables (proposal, demo, next steps, case study).

**All tasks complete. Ready for Wednesday demo.**

## Assets on disk

- `assets/source/dd-checklist/harrow-vale-dd-checklist.md` — ⭐ Priya's fixed 9-section / 30-item checklist.
- `assets/source/term-sheets/` — 4 sheets, deliberately different formats:
  SAFE (Nimbus), Series A priced (GreenGrid), convertible note (Anchorline), seed bullets (Solace).
- `assets/source/data-room/` — GreenGrid cap table, articles, lease, MSA (support a full DD demo).
- `docs/discovery/data-room-notes.md` — detailed analysis of all of the above + design implications.
- `assets/legacy-raw-import/` — original untouched files (1–8 + checklist).

## Discovery — client priorities (from Emily's call notes)

Priya (Managing Partner) — key concerns to design around:
- **Does NOT want Claude hallucinating new checklist items or skipping steps.** The DD
  checklist is a **fixed, standardised process** — the skill must follow it exactly, no
  invention, no omission. (→ implies: load the checklist verbatim, check item-by-item,
  never generate checklist items; make coverage auditable.)
- Firm is on/near **Chancery** (Lane), Clerkenwell.

What the client wants (their words):
- **Data security & governance**
- **Efficiency & standardisation**

Stretch driver: a **skills pipeline so all 10 lawyers use the same versions** (consistency
across the firm is the point — ties directly to "standardisation").

## Notes / assets

- `docs/engagement/scenario-guide.md` — the official engagement pack (source of truth).
- `docs/discovery/client-call-notes.md` — contains a phone number (+447915900076); left untouched.
- Support: Hackathon Helper at lab.syntheticsignal.io/hackathon; Drew (drew.perry@negativezero.com).

---

## Log

### [2026-07-30 17:37] Emily + Claude/Opus-4.7-Nimbus — HANDOVER jobs 1–5 all closed; packaging check landed in the gate; branch pushed for PR

- **HANDOVER-to-claude-code.md is now complete.** All five jobs shipped:
  - **Job 1** — Emily manually removed the shelf-reader Python one-liner from
    `.claude/settings.local.json`.
  - **Job 2** — commit `0db5727` fixed `.claude/skills/publish-hv-skill/SKILL.md`
    line 130: replaced `claude plugin list` with `/plugin` panel guidance and a
    note not to fall back on reading `.claude-plugin/marketplace.json` (that's the
    shelf, not the install state).
  - **Job 3** — commit `df64f1a` undid the "no slash command" claim across
    `CLAUDE.md`, `deliverables/lawyer-installation-guide.md`,
    `deliverables/skills-pipeline-process.md`,
    `docs/governance/pipeline-rehearsal.md`, and
    `plugins/term-sheet-review-plugin/skills/term-sheet-review/README.md`. Each
    kept the correct `/plugin` panel additions the drift session also made,
    restored the namespaced slash invocation, and carries a
    `Verified against Claude Code 2.1.140, 2026-07-30` stamp.
  - **Job 4** — Emily's live check on Claude Code 2.1.140 confirmed the
    namespaced slash form registers and fires.
  - **Job 5** — acceptance test on `assets/source/term-sheets/safe-nimbus-robotics.md`
    passed all four criteria: Parts A–D output structure, £6m cap flagged as
    post-money with 20% discount (🟡) and MFN (🔴) called out, all 28 checklist
    items with statuses, and reads bundled `reference/dd-checklist.md` from the
    installed cache — no repo-globbing.
- **Substantial governance addition:** commit `6d4ff4d` added a **packaging
  check** to `tools/skill-gate/gate.py`. The gate now asserts every file each
  skill's `SKILL.md` references actually exists in the shipped tree; a broken
  package is a hard FAIL that blocks publication before the scorer runs. Closes
  the silent Rule-1-breach path the Desktop upload demonstrated. Negative-tested
  live: renaming `reference/dd-checklist.md` produces
  `packaging FAIL — 1 referenced file(s) missing from shipped tree`.
- **Merged origin/master** (BLACKBOARD protocol from PRs #7 and #8) into the
  feature branch — one small conflict in `CLAUDE.md` §"Skill Usage", resolved
  in favour of the feature branch's version. Gate + `check_published.py` both
  green post-merge.
- **BLACKBOARD adoption:** skinny. Focus Board row + one Recent History entry
  under `Claude/Opus-4.7-Nimbus`, initiated by Emily. Retroactive record; work
  happened pre-adoption without a lock. Close-out (this LEDGER entry + PR + file
  delete) is single-agent sequential, no collision risk, stays outside
  BLACKBOARD per the "simple Q&A does not require a job" rule.
- **New skill spec queued:** `situate` — the multi-source sanity-check skill
  Emily proposed. Spec written up in `PLAN.md` §H. Cross-references sources of
  truth (`.ai/BLACKBOARD.md`, `LEDGER.md`, `PLAN.md`, `PROGRESS.md`, git state,
  memory), catches drift, and asks the user for clarification when conflicts
  can't be resolved from the sources themselves. Proposed as the Phase-5
  demo-opening candidate; ~2 sessions of work through the gate.
- **Branch pushed** at `6a17f69`. PR pending; URL:
  `https://github.com/f7-rage-gremlin/HarrowValeLLP/pull/new/feature/gate-packaging-check`

### [2026-07-30 01:30] Emily + Claude — The plugins were installed all along; our docs and our check were both wrong

- Symptom: plugins appeared "both installed and uninstalled". `/term-sheet-review` never
  showed up under `/`, so we assumed the install had failed and kept reinstalling.
- **Cause 1 — the slash command does not exist.** Every plugin under `plugins/` ships only a
  `skills/` directory. A slash command exists only if a plugin provides a `commands/`
  directory; none does. Skills are model-invoked from their `description` frontmatter, so
  `/term-sheet-review:term-sheet-review` could never appear no matter what we did.
  `CLAUDE.md`, `docs/governance/pipeline-rehearsal.md`, `tools/org-policy/README.md` and
  `deliverables/skills-pipeline-process.md` all documented that invocation. All four corrected.
- **Cause 2 — our verification was a false positive.** `claude plugin list` is not a valid
  subcommand in this Claude Code version ("unknown command 'list'"). Asked inside a session,
  an agent instead ran a pre-approved python one-liner from `.claude/settings.local.json`
  that reads `.claude-plugin/marketplace.json`, and printed the result under the heading
  "Installed plugins:". That is the **shelf**, not the install state — it prints identically
  on a machine with nothing installed. The tell was `mock-skill v1.0.0` appearing as
  "installed" the moment it was committed to the shelf.
- Ground truth came from the `/plugin` panel: "All plugins from this marketplace are already
  installed." Nothing was ever broken.
- **Rule going forward:** verify installs from the `/plugin` panel only — Installed vs
  Discover. Never accept an agent's summary of install state, and never document a slash
  command without a `commands/` directory behind it.
- Untouched, needs a human: remove the marketplace-reading python entry from
  `.claude/settings.local.json` (protected file, agents cannot edit it). While it sits in the
  allow-list it runs without prompting and will mislead the next person the same way.
- Unrelated but worth knowing: the Cowork/desktop app keeps a **separate** skill store. Its
  copy of `term-sheet-review` has only `SKILL.md` — no `reference/`, `examples/` or
  `templates/` — so it cannot read Priya's verbatim checklist and will improvise one. Getting
  Claude Code working tells you nothing about the desktop app, or vice versa.
- Gate re-run after all edits: term-sheet-review 1.000 PASS, leestestskill 1.000 PASS,
  mock-skill 1.000 PASS, cool-new-skill 0.750 FAIL (unpublished by design).
  `check_published.py` green on all three shelf entries. No skill behaviour was changed.

### [2026-07-28 00:40] Lee + Claude — Added `.gitattributes` to stop phantom whole-file diffs

- Symptom: all 107 tracked files showed as modified on a clean Windows checkout, with a
  symmetric 6,965-insertion / 6,965-deletion diffstat. `git diff --ignore-all-space` was empty.
- Cause: history stores LF, Windows working copies hold CRLF, and the repo had no
  `.gitattributes` and no `core.autocrlf` to reconcile the two on comparison.
- Fix: added `.gitattributes` with `* text=auto`, explicit text formats, `assets/legacy-raw-import/*`
  as text, and binary declarations for PNG/PDF/DOCX/XLSX/PPTX/ZIP.
- No renormalization commit was needed — `HEAD` already stored LF, so the policy alone
  cleared it. Working-tree files keep CRLF; history is untouched. Status went 107 → 0.
- Also confirmed `master` in sync with `origin/master` (0 ahead, 0 behind), no untracked
  files, no stashes, and `feature/term-extraction-v1.1.0` fully merged.
- Note for others: `refactor/repository-layout` still exists locally one commit past origin's
  copy. It is the PR #3 merge commit and is fully merged — safe to delete.

### [2026-07-27] Lee + Codex — Implemented issue #2 repository layout refactor

- Moved approved version history to `releases/`, canonical inputs to `assets/source/`, and legacy imports to `assets/legacy-raw-import/`.
- Classified remaining discovery, engagement, and governance material under `docs/`.
- Kept the active plugin, evaluation harness, deliverables, demo, and presentation in their component-owned paths.
- Updated retired path references and recorded the migration map in `docs/governance/repository-layout-migration.md`.
- Validation evidence and the review link are recorded in the refactor pull request.

### [2026-07-26] Lee + Codex — Integrated canonical sources, eval harness, demo, deck, and proposal

- Promoted Lee's mock-site term-sheet and DD-checklist captures to the canonical `assets/` paths.
- Added the executable contract/golden evaluation harness under `tools/termsheet-harness/`.
- Added standalone demo and presentation entrypoints plus the generated proposal and its source.
- Added a root project map, source-priority convention, and pull-request workflow so contributors share one structure rather than personal folder trees.
- Legacy raw imports and Emily's versioned skill history remain available for provenance and review.
- Validation results and pull-request link are recorded in the integration PR rather than presumed complete here.

### [2026-07-25] Claude (Emily's session) — ALL DELIVERABLES COMPLETE ✅

**Evaluation & gap analysis:**
- Read Tom Harrow's conversation screenshots (9 required extraction fields)
- Found v1.0.0 missing 2 fields: founder vesting schedule + legal fees
- Created `docs/governance/prototype-evaluation.md` documenting gaps and action plan

**Core skill updates (v1.1.0):**
- Added founder vesting: duration, cliff, acceleration (single/double-trigger)
- Added legal fees: who pays, caps (£10k-£25k early, £25k-£50k Series A)
- Updated `standard-terms.md` with baselines
- Updated `instrument-applicability.md` with applicability mapping
- Re-ran eval suite: 4/4 pass

**Stretch goals completed:**
- `deliverables/data-security-briefing.md` — UK GDPR, SRA guidelines, Anthropic policies
- `deliverables/skills-pipeline-process.md` — approval workflow, versioning, roles
- `deliverables/lawyer-installation-guide.md` — step-by-step for non-technical users
- `templates/memo-format.html` — professional H&V letterhead styling

**Client deliverables drafted:**
- `deliverables/client-proposal.md` — £4k full package, scope, effort breakdown
- `deliverables/next-steps.md` — pilot, Phase 2, long-term roadmap
- `deliverables/case-study.md` — public-facing Anthropic-style writeup

**Merged into colleague's structure:**
- Created branch `feature/term-extraction-v1.1.0`
- Added `v1.1.0-RATIONALE.md` with justification from brief
- Pushed to origin — ready for PR review

**Status:** 100% complete against requirements. Ready for Wednesday demo.

### [2026-07-22] Claude (Emily's session) — Core skill BUILT + validated ✅
- Built `skills/term-sheet-review/` — the core deliverable.
  - `SKILL.md`: frontmatter (name/description/allowed-tools/argument-hint) + procedure.
    Encodes Priya's 3 rules: use checklist verbatim, never skip an item, never fabricate.
  - `reference/`: dd-checklist (ground truth), term-extraction (fields per instrument),
    standard-terms (deviation baseline), output-template (fixed structure).
  - `examples/`: worked reviews for ALL 4 formats (SAFE / Series A + DD-room / note / seed bullets).
- Validation: all 4 reviews pass structural checks (4 parts, signals, coverage tally,
  all-28-items-accounted-for). GreenGrid reconciliation math independently verified in python
  (price £1.50, 2,133,333 shares, 21.05% — all correct). Skill genuinely checks, doesn't fabricate.
- **Next:** stretch (versioned skills repo + data-residency memo) and the 4 written deliverables.
  Still need: client budget figure for pricing the proposal.

### [2026-07-22] Claude (Emily's session) — Recon done; data room needs sign-in
- Public site (harrowvale.syntheticsignal.io) live and matches the brief. Team: Priya Vale (MP),
  Tom Harrow (Ops/Knowledge), Marcus Ade (Sr Assoc M&A), Elena Cho (Assoc VC).
- Data room (/data-room/) returns **401 Unauthorized — credentials required**. Needs Emily's
  NZ sign-in; Claude cannot enter credentials. **Emily to sign in and pull the 3 sample term
  sheets + DD checklist**, or export them into this repo (e.g. under `assets/source/term-sheets/`).

### [2026-07-22] Claude (Emily's session) — Workspace initialized
- Read the engagement pack; confirmed with Emily this is a sanctioned discovery/proposal exercise (not adversarial).
- `git init` done. Created this LEDGER.md as the shared coordination file.
- Next up: recon the public site and try the data room.
