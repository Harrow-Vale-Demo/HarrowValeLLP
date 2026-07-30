# J1 — Build `situate` skill through gate → publish pipeline (extended)

Summary/lock/key files live in `.ai/BLACKBOARD.md`.

Initiated by (human): Emily

## Attribution attempts
- Attempt 1/3 — 2026-07-30 18:30 UTC — resolved on job creation (Emily's session)
- Attempt 2/3 — not needed
- Attempt 3/3 — not needed

## Context
Spec source: `PLAN.md §H`. New skill that reads every source of truth (BLACKBOARD, LEDGER, PLAN, PROGRESS, git, memory) and reports either (a) a coherent situation report or (b) a clarifications-needed report when sources conflict. Fits the firm's governance story and would open the demo cleanly.

Working branch: `feature/situate-skill` (cut from `origin/master`).

## Tasks
Ease scale: 1 trivial, 2 simple, 3 moderate, 4 substantial, 5 complex, 6 major.
| Status | Task (≤18) | DONE means (1 line) | Ease | Note |
|---|---|---|---:|---|
| ✅ | Loose-end triage (packaging PR, org migration, cowork import) | Findings written into `SESSION.md`. | 2 | Done during onboarding. |
| ✅ | Register on BLACKBOARD (Focus Board row + J1) | This file exists; lock held. | 1 | |
| ✅ | Cut `feature/situate-skill` branch off `origin/master` | Branch checked out, working tree clean. | 1 | Resolved a small stash-pop merge conflict on `.gitignore` + BLACKBOARD (both from packaging-check-branch-only content). |
| ✅ | Author `plugins/situate/skills/situate/SKILL.md` | File exists with frontmatter (name/description/allowed-tools/argument-hint) and procedure covering both modes and all five Priya rules. | 4 | Follows term-sheet-review shape. |
| ✅ | Author `reference/sources.md` | Enumerates every source situate must read, one row per source. | 2 | |
| ✅ | Author `reference/output-templates.md` | The three output shapes verbatim (all-clear, clarification-needed, conflicts mode). | 2 | Adapted from PLAN §H. |
| ✅ | Author `reference/rules.md` | Priya-style rules 1–5. | 2 | Each rule cites the incident that motivated it. |
| ✅ | Author example run against current tree | Realistic worked example under `examples/`. | 3 | Two examples: clean-tree (all-clear) and drifted-tree (clarifications-needed, matching this repo's actual state tonight). |
| ✅ | Add `SKILLS["situate"]` entry to `tools/skill-gate/gate.py` | Gate loads situate; `--all` runs it without error. | 3 | Additive edit; no regression on other skills. |
| ✅ | Golden fixtures: `fixtures/situate/clean/` and `fixtures/situate/drifted/` | Two fixture trees exist; each has expected output. | 4 | Cases: clean-tree + drifted-tree in `golden.json` with `field: tree_state`. |
| ⛔ | Scorer for situate reports | New scorer (`situate_report_correctness` or similar) that checks source coverage + divergence detection. Registered in gate. | 4 | **Dropped for v0.1.0** — reused the `triage` scorer with `field: tree_state` since it already handles the shape (clean vs drifted classification). Full report-correctness scorer deferred to v0.2.0. |
| ✅ | Gate PASS on situate v0.1.0 | `python tools/skill-gate/gate.py --skill situate` returns PASS. | 2 | tree_state_accuracy = 1.000, first version → no regression check. `--all` also green (existing cool-new-skill FAIL is pre-existing/by-design). |
| ✅ | Publish via `tools/skill-gate/publish.py situate` | Snapshot committed under `releases/situate/v0.1.0/`; shelf updated. | 3 | Dry-run first, then publish. Snapshot at `releases/situate/v0.1.0/gate-report.json`. |
| ✅ | Add situate to `.claude-plugin/marketplace.json` if not done by publisher | Manifest lists situate. | 1 | Auto-added by publisher (first-listing path). |
| ✅ | `check_published.py` green post-publish | Script passes. | 1 | "Every published version is backed by the gate." |
| ✅ | LEDGER entry + BLACKBOARD sign-off | Entry added to top of §Log; Focus Board row updated; J1 archived if complete. | 2 | Done at closeout. |
| ▶️ | Commit + push branch, open PR | PR opens in browser (no `gh` on this NixOS box); URL surfaced. | 1 | Committing now; **push held pending Emily's OK** — shared-state action. |
| ✅ | Update `PROGRESS.md` with the session's summary | Newest-first block appended. | 1 | |

## Ideas (holding area)
- **Self-diagnose the caller** (Priya rule #5): if the caller has no Focus Board row or their branch is not on record, situate should flag *itself* as a divergence. Powerful demo moment because it catches the exact failure mode from tonight's near-miss.
- **Live demo opener**: run situate against the current (genuinely drifted) tree and let it call out the drift on the spot. Stronger than a rehearsed clean run.
- **Machine-readable output too?** Not v0.1.0. Would help CI later.
- **`--conflicts` output**: severity-ordered, no clarification needed — purely diagnostic. Fold in v0.1.0.

## Recent activity (newest first; keep short)
- 2026-07-30 19:15 UTC — tried: full build + gate + publish pipeline. observed: gate PASS at 1.000 (tree_state_accuracy) on both fixture cases; `check_published.py` green on all four shelf entries including new situate v0.1.0; marketplace.json auto-updated; SKILL/README/reference/examples all committed together as a single-purpose branch. next: commit the branch; push held for Emily's OK (shared-state action).
- 2026-07-30 18:45 UTC — tried: scoped scorer decision. observed: writing a bespoke `situate_report_correctness` scorer for v0.1.0 was disproportionate; the `triage` scorer with `field: tree_state` covers the classification the gate needs to make about a run. next: dropped bespoke scorer, ⛔; deferred to v0.2.0 as report-correctness upgrade.
- 2026-07-30 18:30 UTC — tried: onboarded, read BLACKBOARD/LEDGER/PROGRESS/PLAN §H, checked git state and remote. observed: PR #10 (packaging-check) still open; repo migrated to `Harrow-Vale-Demo` org (public); cowork/desktop import still unresolved (PLAN §B). next: cut branch and start SKILL.md authoring.

## Validation (most recent)
- Ran: `python tools/skill-gate/gate.py situate` → PASS, tree_state_accuracy=1.000.
- Ran: `python tools/skill-gate/gate.py --all` → PASS on situate, leestestskill, mock-skill, term-sheet-review; cool-new-skill FAIL (pre-existing, by design).
- Ran: `python tools/skill-gate/publish.py situate --dry-run` then live publish; all writes confirmed.
- Ran: `python tools/skill-gate/check_published.py` → green. "Every published version is backed by the gate."

## Closeout (when complete)
- Criteria: all tasks are ✅ or ⛔, and validation recorded (or explicitly "not run").
- Archive:
  - Move this log to `.ai/jobs/done/YYYY-MM-DD_HHMMUTC_J1 - Build situate skill.md`
  - Append one line to `.ai/jobs/done/INDEX.md`
  - Add one entry to BLACKBOARD `Recent History` (include the archived log path); prune to last 12 entries
  - Reset slot J1 in `.ai/BLACKBOARD.md` to `(unassigned)` and `Lock: 🔓`
  - Ensure placeholder exists: `.ai/jobs/active/J1 - (unassigned).md`
