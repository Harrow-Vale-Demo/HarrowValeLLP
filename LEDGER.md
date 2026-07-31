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

### [2026-07-31 00:45] Emily + Claude/Opus-4.7-Aurora — Merged Phurin's `dd-checklist` branch (Handover 02 Job 1, Option A — plugin only, off-shelf)

- **Merged `origin/dd-checklist-marketplace-plugin-and-fixed-json`**
  (Phurin, `903368f`, 2026-07-29) into `feature/merge-dd-checklist`. Branch
  had been unmerged for 48+ hours; the same diagnosis was rediscovered from
  scratch by two later sessions (see `docs/hardening/H4-duplicate-overlapping-projects.md`).
- **Option A per Handover 02** — plugin lands, shelf entry deferred until
  gated:
  - ✅ Took the three new plugin files under `plugins/dd-checklist-mapper-plugin/`
    (`.claude-plugin/plugin.json`, `skills/dd-checklist/SKILL.md`,
    `skills/dd-checklist/reference/dd-checklist.md`) — Phurin's authorship
    preserved in the merge commit.
  - ✅ Resolved the `.claude-plugin/marketplace.json` conflict by keeping
    master's 3 shelf entries and **rejecting** his 4th
    (`dd-checklist-mapper-plugin`). No new entry reaches the shelf until it
    has been through the gate.
  - ✅ `tools/termsheet-harness/.claude-plugin/marketplace.json` — deleted
    on both sides (already gone incidentally in Lee's `e5e2fa9`); git
    auto-resolved.
- **Verification:**
  - `python tools/skill-gate/gate.py --all` — no regression;
    leestestskill/mock-skill/term-sheet-review PASS, cool-new-skill FAIL
    (pre-existing, by design).
  - `python tools/skill-gate/check_published.py` — green;
    *"Every published version is backed by the gate."* Correctly does not
    ask for gate evidence for `dd-checklist-mapper-plugin` since it isn't
    on the shelf.
- **Naming decision deferred.** His directory is `dd-checklist-mapper-plugin`;
  every other shelf entry drops the `-plugin` suffix. Consistency says
  `dd-checklist` or `dd-checklist-mapper`. Because Option A doesn't publish
  now, kept his original directory name at merge time — settle naming (and
  the derived evidence path `releases/<name>/v1.0.0/`) before generating any
  gate artefacts.
- **Situate work (Session 1) lives on a separate held branch.** Emily flagged
  possible private-marketplace path; `feature/situate-skill` is not being
  PR'd to `Harrow-Vale-Demo/HarrowValeLLP` for now. Cowork Session 1
  artefacts (Handover 02 + `docs/hardening/` + verbatim spec + heldout
  fixture + session-notes extension) are parked on that branch as a stacked
  commit (`6860cfc`) with a STACKING NOTICE and cherry-pick recipe in
  personal `SESSION.md`.
- **Handover 02 remaining jobs** — Job 2 (`instrument-applicability.md`,
  decision required), Job 3 (verbatim checklist check + fix examples), Job 4
  (three status vocabularies, deferred D1), Job 5 (small verified items).
  Job 3 is the biggest demo-relevance body of work; separate branch when
  picked up.
- **Cross-branch note.** This branch does NOT include the Nimbus 17:37
  entry (PR #10 still open) or Aurora's 19:15 situate entry
  (feature/situate-skill, held). When either PR merges, expect a trivial
  reverse-chronological ordering conflict at the top of §Log — keep all
  entries.

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
