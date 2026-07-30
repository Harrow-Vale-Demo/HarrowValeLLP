# AGENTS.md — Codex Protocol (BLACKBOARD-driven)

### ALWAYS ASK PERMISSION BEFORE SWITCHING FROM PLANNING TO EXECUTION (IMPLEMENTING CODE) - Docs may be updated non-destructively on-the-fly.

# What the BLACKBOARD is 🧭
`.ai/BLACKBOARD.md` is the repo’s **shared working memory** and **job dashboard**.
- **Git** = long-term record (diffs, history).
- **BLACKBOARD** = what’s happening now (jobs, tasks, evidence, blockers).
- **Job logs** = extended per-job notes live in `.ai/jobs/active/`, `.ai/jobs/backburner/`, and `.ai/jobs/done/`.

Simple Q&A does **not** require a job. Create/log a job only for multi-step tracked work.

---

## App plan documentation (project-specific process)
- When a project uses an app plan folder (e.g., `docs/app_plan/`), keep it updated as work progresses.
- Use a **two-letter prefix** for ordering (e.g., `AA_`, `BA_`, `CA_`) and spread initial sections across the alphabet so new docs can slot in between later.
- **Header files** are just filenames (no extension) with an `h` after the two-letter prefix and ALL CAPS title (e.g., `ABh_VISION_AND_PLATFORMS`). These act as section dividers in the file tree.
- **Content files** are `XY_Title.md` with the two-letter prefix.
- If an index file exists (e.g., `AA_Index.md`), update it when adding or moving sections.
- Within each planning file, each subsection should include:
  - an overview or details that must be remembered for the major plan
  - goals to achieve or achieved, with dates achieved per goal

---

## Non-negotiables ✅
- First action every session: read `.ai/BLACKBOARD.md` top-to-bottom **before any work**.
- **Agent identity:** if multiple sessions may be active, use a **unique Agent Handle** that includes your model name (e.g., `Claude/<name>`, `Codex/<name>`), and never write as plain `Codex` or `Claude`.
- **Per-agent focus:** use the **Agent Focus Board** (no global focus).
- **Don’t switch your focus** unless the user explicitly directs.
- **Job-level lock before edits.** Don’t work in a locked job without user permission.
- **Human initiator provenance:** every tracked job records `Initiated by (human): <name or team handle>`. Make three logged identification attempts at distinct checkpoints. Until resolved, use `Pending confirmation (attempt n/3)`. Never infer identity from usernames, paths, accounts, or machine metadata; only after the third attempt has genuinely gone unanswered may a closure-required record use `Unresolved after 3 documented attempts`.
- Timestamp meaningful updates in **UTC**: `YYYY-MM-DD HH:MM UTC` (always include `UTC`; UK summer ≠ UTC).
- Big rewrites allowed ✅ → leave a clean trail (files, migration notes, validation, rollback).

---

## Agent identity (multi-agent safe)
When running multiple agents (including multiple Claude/Codex sessions), each session must have a unique **Agent Handle** so focus/locks don’t collide.
- Preferred format: `<Model>/<Name>` where Model is `Claude`, `Codex`, `Kimmy`, etc.
- If missing: ask the user once; if ignored and you must proceed, self-assign a unique handle (e.g., `Claude/Auto-1`) and note it in the BLACKBOARD.
- Start every chat response with `Agent: <AgentHandle>` and include it in every BLACKBOARD write (Focus Board row, `Lock:`, activity).
- Own your row: only edit the Focus Board row for your `AgentHandle`; create it if missing (never overwrite another agent’s row).

---

## Human and agent attribution
- `Initiated by (human)` identifies the human who originated the tracked job.
- `Agent Handle` identifies the agent currently doing or coordinating the work.
- Preserve the original human initiator through agent handoffs, parking, and archiving.
- If another human materially redirects or expands the job, attribute that change in a timestamped Recent Activity entry; do not replace the original initiator.
- If the initiator’s name or team handle is unavailable, make three distinct, timestamped identification attempts:
  1. At job creation/onboarding.
  2. At the next meaningful human interaction or before a handoff.
  3. At a later interaction when closure is otherwise due, or immediately before parking/archiving.
- Repeating the question in one response is one attempt, not several. Log each attempt and its outcome in the job file.
- While unresolved, use `Pending confirmation (attempt n/3)` in every linked record. Do not park or archive at attempt 1/3 or 2/3.
- After attempt 3, prefer leaving the job waiting for an answer. Only when closure is necessary and the third attempt has genuinely gone unanswered may the fallback become `Unresolved after 3 documented attempts`.
- Never infer identity from local account names or other machine metadata.

---

## How Codex uses the BLACKBOARD (operational loop) 🔁

### Onboarding (start of work)
0) Confirm your `AgentHandle` (user-provided or self-assigned after one ask) and use it consistently.
1) Read BLACKBOARD.
2) Update your **Agent Focus Board** row: Job, Task, Status, Since (UTC), Notes.
3) If your chosen job slot is missing or empty, create it (summary + job log):
   - Summary block in `.ai/BLACKBOARD.md`: title + 1 sentence description, `Initiated by (human)`, status/lock, pace, last progress tick (set to current global counter on creation), key files, collision notes, link to job log
   - Job log file in `.ai/jobs/active/`: provenance with the same `Initiated by (human)` value, a timestamped attribution-attempt log, task table (recommended ≤18 tasks, each with DONE means), recent activity, validation, and an Ideas holding area
   - Ease scale: 1 trivial, 2 simple, 3 moderate, 4 substantial, 5 complex, 6 major
4) **Collision check before edits:** scan other jobs’ key files + structural collision notes; if overlap suspected, write `OVERLAP: Jx` and ask the user.
5) Begin work (multiple ▶️ tasks within the job is fine **while you hold the job lock**).

### Sign-off (pause/stop/switch agent/model)
Update the job you worked on:
- Task statuses (job log file)
- Recent activity (timestamped): `tried -> observed -> next` (job log file)
- Validation: what you ran + result, or explicitly "not run" (job log file)
- If any tasks moved to ✅ or ⛔: increment BLACKBOARD global progress counter and update `Last progress tick` in the job summary block
- Collision notes (if newly discovered) (summary block in `.ai/BLACKBOARD.md`)
- Update your Agent Focus Board row (status/notes)
- If leaving job idle: set `Lock: 🔓`, set `Status: 🟡 Warm`, and keep `Last progress tick` current
- If initiator attribution is pending, make the next due identification attempt and update its log. Do not park or archive at attempt 1/3 or 2/3.
- If all tasks are Done or Dropped and initiator attribution is resolved or has reached the allowed closure fallback: archive the job log to `.ai/jobs/done/` (recommended: `YYYY-MM-DD_HHMMUTC_Jx - <title>.md`), preserve `Initiated by (human)` plus the attribution-attempt log in the archived log, include the initiator value in Recent History and `.ai/jobs/done/INDEX.md`, and reset the Jx slot to `(unassigned)`

### User-facing wrap-up (in chat) 🗣️
When pausing/stopping/finishing, include briefly: Current job, Current task(s), Recommended next (or one unblock question).

---

## Locking rules 🔒
- Lock is **job-level**. Lock before edits.
- If a job is locked by another agent and you think you should work on it: ask the user to unlock or explicitly approve parallel work.
- Returning to a job you touched before: freshness check (scan timestamps; if newer activity exists, re-orient before edits).

---

## Collision avoidance (file + structural) 🧩
Two overlap types: **File overlap** (same files/paths) and **Structural overlap** (same architecture assumptions).
If overlap suspected: mark `OVERLAP: Jx`, ask user before proceeding, prefer resolving via file split / separate branches / or parking one job to Back Burner.

---

## Debugging discipline (avoid looping) 🧪
If a narrow fix fails ~2 times (or is unlikely): stop “guess-and-patch”, list 3–6 plausible causes, pick the fastest discriminating test for each, gather evidence before more changes, record `tried → observed → next`.

---

## Evidence habits (make fixes real) ✅
- **Repro-first:** expected vs actual + minimal repro + proof signal.
- Prefer a **failing test first** for non-trivial/regression-prone bugs (or state why not).
- **Rollback note** for risky changes: `ROLLBACK: revert <commit/PR> / flip flag / restore entrypoint`.
- Timebox + checkpoint: timebox loops; checkpoint (commit/stash) before risky moves.
- Assumptions must be explicit.

---

## Safety + scope 🧯
- No destructive actions (deletes, wipes, irreversible migrations, key rotation) without explicit user permission.
- No stealth scope creep: trade off tasks or log a new job/back-burner entry; don’t silently expand.

---

## Back Burner (B1–B12)
If J1–J12 are full: extended notes live in `.ai/jobs/backburner/` (one file per slot). Prefer parking 🔴 Stalled + 🔓 unlocked jobs; if parking 🟡 Warm, ask user first. Preserve `Initiated by (human)` and the attribution-attempt log, and store a compact summary (objective/state/files/next/blockers) with timestamp. Never park a job whose initiator remains at attempt 1/3 or 2/3.
