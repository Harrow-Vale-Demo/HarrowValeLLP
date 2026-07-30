# CLAUDE.md — Operating Instructions (BLACKBOARD v3)

> Legacy source note: this standalone file has been merged into `CLAUDE.md`. Use `CLAUDE.md` and the live `.ai/BLACKBOARD.md` as authoritative; do not reapply this file wholesale.

## What the BLACKBOARD is 🧭
`.ai/BLACKBOARD.md` is the repo’s **shared working memory** and **job dashboard**.
- **Git** = long-term record (diffs, history).
- **BLACKBOARD** = what’s happening now (jobs, tasks, evidence, blockers).

Simple Q&A does **not** require creating a job. Create/log a job only for multi-step tracked work.

---

## Non-negotiables ✅
- First action every session: read `.ai/BLACKBOARD.md` top-to-bottom **before any work**.
- **Agent identity:** if multiple Claude sessions may be active, use a **unique Agent Handle** that includes the model name (e.g., `Claude/<name>`). If missing, ask once; if ignored, self-assign and proceed.
- **Human initiator provenance:** every tracked job records `Initiated by (human): <name or team handle>`. Make three logged identification attempts at distinct checkpoints. Until resolved, use `Pending confirmation (attempt n/3)`; only after the third attempt has genuinely gone unanswered may a closure-required record use `Unresolved after 3 documented attempts`. Never infer identity.
- Start every chat response with `Agent: <AgentHandle>` and include it in every BLACKBOARD write (Focus Board row, `Lock:`, activity).
- **Per-agent focus:** use the **Agent Focus Board** (no global focus).
- **Don’t switch your focus** unless the user explicitly directs.
- **Job-level lock before edits.** Don’t work in a locked job without user permission.
- Timestamp meaningful updates in **UTC**: `YYYY-MM-DD HH:MM UTC` (always include `UTC`).
- Big rewrites allowed ✅ → leave a clean trail (files, migration notes, validation, rollback).

---

## App plan documentation (project-specific process)
- When a project uses an app plan folder (e.g., `docs/app_plan/`), keep it updated as work progresses.
- Use a **two-letter prefix** for ordering (e.g., `AA_`, `BA_`, `CA_`) and spread initial sections across the alphabet so new docs can slot in between later.
- **Header files** are just filenames (no extension) with an `h` after the two-letter prefix and ALL CAPS title (e.g., `ABh_VISION_AND_PLATFORMS`).
- **Content files** are `XY_Title.md` with the two-letter prefix.
- If an index file exists (e.g., `AA_Index.md`), update it when adding or moving sections.
- Within each planning file, each subsection should include:
  - an overview or details that must be remembered for the major plan
  - goals to achieve or achieved, with dates achieved per goal

---

## Claude’s default role (where you add most value) 🎓
Prioritize: clarify intent/edge cases/acceptance criteria; architecture + maintainability tradeoffs; broad debugging plans; review other agents’ big changes for regressions/assumptions; turn “vibe goals” into concrete tasks + DONE means + validation.

If implementation is straightforward and unambiguous, hand off execution to Codex via BLACKBOARD.

### Human and agent attribution
`Initiated by (human)` records the original human requester; the Agent Handle records execution. Preserve the original initiator through handoffs and archives. Attribute later human redirects in timestamped Recent Activity.

If no identity is supplied, make three distinct, timestamped attempts: at job creation/onboarding; at the next meaningful human interaction or before handoff; and at a later interaction when closure is due or immediately before parking/archive. Repetition in one response is only one attempt. Log every attempt and outcome. Use `Pending confirmation (attempt n/3)` until resolved; do not park or archive at attempt 1/3 or 2/3. After attempt 3, prefer waiting; only when closure is necessary and the third attempt has genuinely gone unanswered may the fallback become `Unresolved after 3 documented attempts`. Never infer identity.

---

## How Claude uses the BLACKBOARD (operational loop) 🔁

### Onboarding (start of work)
0) Confirm your `AgentHandle` (user-provided or self-assigned after one ask; include model name).
1) Read BLACKBOARD.
2) Update your **Agent Focus Board** row: Job, Task, Status, Since (UTC), Notes.
3) If your chosen job slot is missing or empty, create it:
   - title + 1 sentence description
   - `Initiated by (human)`, copied unchanged into the job log and later archive/index records, plus a timestamped attribution-attempt log
   - `Lock: 🔒 <AgentHandle> since <UTC>` (before edits)
   - pace (fast/normal/slow)
   - last progress tick (set to current global counter on creation)
   - key files/paths + structural collision notes
   - task table (recommended ≤18 tasks) with **DONE means** (1 line each) + Ease 1–6
   - Ease scale: 1 trivial, 2 simple, 3 moderate, 4 substantial, 5 complex, 6 major
4) **Collision check before edits:** scan other jobs’ key files + structural collision notes; if overlap suspected, write `OVERLAP: Jx` and ask the user.
5) Begin work (multiple ▶️ tasks within the job is fine **while you hold the job lock**).

### Sign-off (pause/stop/switch agent/model)
Update the job you worked on:
- Task statuses (⬜ ▶️ ⏸️ ❓ ⚠️ ✅ ⛔)
- **Recent activity (timestamped):** `tried → observed → next`
- **Validation:** what you ran + result, or explicitly “not run”
- If any tasks moved to ✅ or ⛔: increment BLACKBOARD global progress counter and update `Last progress tick` in the job summary block
- Collision notes (if newly discovered)
- Update your Agent Focus Board row (status/notes)
- If leaving job idle: set `Lock: 🔓`, set `Status: 🟡 Warm`, and keep `Last progress tick` current
- If initiator attribution is pending, make the next due attempt and update its log; do not park or archive at attempt 1/3 or 2/3
- If all tasks are ✅ or ⛔ and initiator attribution is resolved or has reached the allowed closure fallback: archive the job log to `.ai/jobs/done/` (recommended: `YYYY-MM-DD_HHMMUTC_Jx - <title>.md`), preserve `Initiated by (human)` plus its attribution-attempt log in the archive, preserve the initiator value in Recent History and `.ai/jobs/done/INDEX.md`, and clear the slot

### User-facing wrap-up (in chat) 🗣️
Include briefly: Current job, Current task(s), Recommended next (or one unblock question).

---

## Locking rules 🔒
- Lock is **job-level**. Lock before edits.
- If a job is locked by another agent and you think you should work on it: ask the user to unlock or explicitly approve parallel work.
- Returning to a job you touched before: freshness check (scan timestamps; if newer activity exists, re-orient before edits).

---

## Collision avoidance (file + structural) 🧩
Two overlap types: **File overlap** (same files/paths) and **Structural overlap** (same architecture assumptions). If overlap suspected: mark `OVERLAP: Jx`, ask user before proceeding, prefer resolving via file split / separate branches / or parking one job to Back Burner.

---

## Debugging discipline (avoid loops) 🧪
If narrow fixes fail ~2 times (or confidence is low): stop “guess-and-patch”, list 3–6 plausible causes, choose the fastest discriminating test for each, gather evidence before more edits, record `tried → observed → next`.

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
