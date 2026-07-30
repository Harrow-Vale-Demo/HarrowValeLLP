# BLACKBOARD — Live (v4, split job logs)

## Purpose (for agents)
Shared working memory + job dashboard.
- **Git** = long-term truth (diffs, history).
- **BLACKBOARD** = short-term coordination (focus, locks, job summaries, collisions).
- **Job logs** = per-job details (tasks, activity, validation) in `.ai/jobs/`.

Reference docs (required): `AGENTS.md`, `CLAUDE.md`.
Reference doc (maintainers/optional): `BLACKBOARD_SYSTEM_PRINCIPLES.md`.

---

## Global rules (must follow)
- Use a unique **Agent Handle** when 2+ agents are active (recommended: `<Model>/<name>`).
- If no handle is provided, ask once; if ignored, self-assign (e.g., `Claude/Auto-1`).
- Every tracked job records `Initiated by (human): <name or team handle>` in its BLACKBOARD summary and job log.
- If the initiator is missing, make three distinct, timestamped attempts: at onboarding; at the next meaningful human interaction or before handoff; and at a later interaction when closure is due or immediately before parking/archive. Repetition in one response counts as one attempt.
- Until resolved, use `Pending confirmation (attempt n/3)` and keep the attempt log in the job file. Do not park or archive at attempt 1/3 or 2/3.
- After attempt 3, prefer leaving the job waiting. Only when closure is necessary and the third attempt has genuinely gone unanswered may the fallback become `Unresolved after 3 documented attempts`. Never infer identity from usernames, paths, accounts, or machine metadata.
- Preserve the original initiator through handoffs, parking, and archiving. Attribute later human redirects in timestamped Recent Activity instead of replacing the origin.
- Jobs already locked when this field was introduced may be backfilled by their lock holder at the next update; do not edit another agent's locked record solely to add it.
- When creating a new job, set `Last progress tick` to the current global progress counter.
- Don’t switch your focus unless the user explicitly directs.
- Lock a job **before edits**; don’t work in a locked job without user permission.
- Before edits: scan other jobs’ `Key files/paths` + `Collision` notes; if overlap suspected, write `OVERLAP: Jx` and ask the user.
- Timestamp meaningful updates in **UTC**: `YYYY-MM-DD HH:MM UTC`.
- Keep this file compact; put task tables, detailed activity, and validation in the job log file.
- Prefer stable job log filenames; if you rename a job file, update its pointer line here.

Progress-based staleness:
- Global progress counter (completed tasks): **18**
- Increment by 1 for each task moved to ✅ or ⛔ (any job).
- Stale thresholds (progress ticks): fast=6 | normal=12 | slow=24

Status rules (slot-level):
- If `Lock: 🔒` then `Status: 🟢 Active`.
- If `Lock: 🔓` and recent progress then `Status: 🟡 Warm`.
- If `Lock: 🔓` and `global_tick - last_progress_tick >= threshold` then `Status: 🔴 Stalled`.

Quick reference:
- Job status (slot-level): 🟢 Active | 🟡 Warm | 🔴 Stalled | ✅ Complete
- Task status (job logs): ⬜ Todo | ▶️ Active | ⏸️ Waiting | ❓ Blocked | ⚠️ Risk | ✅ Done | ⛔ Dropped

---

## Sign-off checklist (when pausing/stopping)
1) Update job log file: task statuses + activity (timestamped) + validation (ran/not run).
2) Update BLACKBOARD: your Focus Board row + job summary (status/lock/pace/last-progress/key files/collision).
3) If any tasks were set to ✅ or ⛔: increment the global progress counter and update the job’s `Last progress tick`.
4) If unlocking and not complete: set `Status: 🟡 Warm`.
5) If tasks are complete, first satisfy the initiator closure gate: no parking/archive at attempt 1/3 or 2/3; after attempt 3 prefer waiting, and use `Unresolved after 3 documented attempts` only when closure is necessary and that attempt genuinely went unanswered. Then preserve `Initiated by (human)` plus the attribution-attempt log in the archive, preserve the initiator value in `.ai/jobs/done/INDEX.md` and Recent History, move the log to `.ai/jobs/done/YYYY-MM-DD_HHMMUTC_Jx - <title>.md`, prune Recent History to 12, and reset the Jx slot to `(unassigned)`.

---

# AGENT FOCUS BOARD
Naming: one row per active **Agent Handle** (recommended: `<Model>/<name>`). Don’t reuse plain `Codex` or `Claude` when running multiple sessions.
| Agent Handle | Job | Task | Status | Since (UTC) | Notes |
|---|---|---|---|---|---|
| Codex/Vellum | — | J2 complete: approved v3 saved to repository | ✅ Complete | 2026-07-30 15:27 UTC | v3 staged; J2 archived; no lock held. |
| Codex/Meridian-1 | — | J1 archived after PR #7 merge | ✅ Complete | 2026-07-30 13:02 UTC | PR #7 merged at `d93328b`; follow-up clears the stale lock and archives the full log. |
| Codex/Proposal-Audit-1 | — | J3 complete | ✅ Complete | 2026-07-30 12:14 UTC | J3 archived at 2026-07-30 12:19 UTC; no lock held. |
| Codex/Linebreak-1 | J3 | Await initiator attribution | ⏸️ Waiting | 2026-07-30 12:34 UTC | LF policy complete and validated; archive blocked at attribution attempt 1/3. |

---

# ACTIVE JOB SLOTS (J1–J12)
Extended per-job logs (tasks, ideas, recent activity, validation) live in `.ai/jobs/active/`.

## J1 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J1 - (unassigned).md`

## J2 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J2 - (unassigned).md`
## J3 — Standardize repository text files on LF
Description: Enforce LF for repository text and editors, retaining CRLF only for Windows command scripts.
Initiated by (human): Lee
Status: 🟡 Warm
Lock: 🔓
Pace: normal
Last progress tick: 12
Key files/paths: `.gitattributes`, `.editorconfig`, repository-local Git configuration
Collision: None found; implementation and validation are complete, with archive awaiting initiator attribution.
Job file: `.ai/jobs/active/J3 - Standardize repository text files on LF.md`

## J4 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J4 - (unassigned).md`

## J5 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J5 - (unassigned).md`

## J6 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J6 - (unassigned).md`

## J7 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J7 - (unassigned).md`

## J8 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J8 - (unassigned).md`

## J9 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J9 - (unassigned).md`

## J10 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J10 - (unassigned).md`

## J11 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J11 - (unassigned).md`

## J12 — (unassigned)
Description: —
Initiated by (human): —
Status: —
Lock: 🔓
Pace: normal
Last progress tick: —
Key files/paths: —
Collision: —
Job file: `.ai/jobs/active/J12 - (unassigned).md`

---

# BACK BURNER (B1–B12)
Use when you want to park jobs without cluttering Active slots.
Prefer parking: 🔴 Stalled + 🔓 unlocked. If 🟡 Warm, ask the user first.
Preserve `Initiated by (human)` and its attribution-attempt log when parking and rehydrating a job. Never park while attribution remains at attempt 1/3 or 2/3.
If you start work on a back-burner item: rehydrate it into an active job slot and lock it.

Extended back burner notes live in `.ai/jobs/backburner/`.

## B1 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B1 - (unassigned).md`

## B2 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B2 - (unassigned).md`

## B3 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B3 - (unassigned).md`

## B4 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B4 - (unassigned).md`

## B5 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B5 - (unassigned).md`

## B6 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B6 - (unassigned).md`

## B7 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B7 - (unassigned).md`

## B8 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B8 - (unassigned).md`

## B9 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B9 - (unassigned).md`

## B10 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B10 - (unassigned).md`

## B11 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B11 - (unassigned).md`

## B12 — (unassigned)
Summary: —
Initiated by (human): —
Last update (UTC): —
Job file: `.ai/jobs/backburner/B12 - (unassigned).md`

---

# RECENT HISTORY (completed milestones worth remembering)
- 2026-07-30 15:27 UTC — J2 completed by Codex/Vellum; initiated by: Lee: designed and iterated the Harrow & Vale identity, approved the dark subtly cyber v3, saved it under `assets/brand/`, and staged only the selected asset. Log: `.ai/jobs/done/2026-07-30_1527UTC_J2 - Create wide Harrow & Vale logo concept.md`
- 2026-07-30 13:02 UTC — J1 completed by Codex/Meridian-1; initiated by: Lee: implemented the three-attempt attribution protocol, backfilled linked records, published all workspace changes, and merged PR #7 with the GitHub gate passing. Log: `.ai/jobs/done/2026-07-30_1302UTC_J1 - Require three initiator-identification attempts and publish workspace.md`
- 2026-07-30 12:19 UTC — J3 completed by Codex/Proposal-Audit-1; initiated by: Lee: separated data residency, repository security and open decisions; excluded pricing; added provisional presenter ownership; validation passed. Log: `.ai/jobs/done/2026-07-30_1219UTC_J3 - Refine presentation structure and presenter plan.md`
- 2026-07-30 12:08 UTC — J1 completed by Codex/Meridian-1; initiated by: Lee: removed personal conversational preferences and added durable human-initiator provenance across active, parked, and archived job records; validation passed. Log: `.ai/jobs/done/2026-07-30_1208UTC_J1 - Remove personal style and add human initiator provenance.md`
- 2026-07-30 12:00 UTC — J2 completed by Codex/Proposal-Audit-1; initiated by: Lee: added the how-Claude-helped slide and truthful live/prerecorded demo sequence to the Friday presentation plan; validation passed. Log: `.ai/jobs/done/2026-07-30_1200UTC_J2 - Add presentation slide and demo cues.md`
- 2026-07-30 09:35 UTC — J1 completed by Codex/Meridian-1; initiated by: Lee: merged the current v4 BLACKBOARD protocol into `CLAUDE.md` while preserving HarrowVale guidance; validation passed. Log: `.ai/jobs/done/2026-07-30_0935UTC_J1 - Merge BLACKBOARD protocol into CLAUDE.md`

Guardrail: keep this short (recommended: last 12 entries). Full history lives in `.ai/jobs/done/` and `.ai/jobs/done/INDEX.md`.

---

# Emergency procedures (short)
- **BLACKBOARD conflict/corruption:** stop edits → restore last good from git → replay clearly-valid updates.
- **Disputed locks:** both stop → compare timestamps → ask user if unclear.
- **Unknown changes:** log discrepancy → ask user before overwriting.
