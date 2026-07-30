# Blackboard System Principles

Audience: maintainers. Agents should rely on `AGENTS.md`, `CLAUDE.md`, and `.ai/BLACKBOARD.md` unless explicitly asked to consult this document.

## Purpose
The BLACKBOARD is the project's **shared working memory** and **job dashboard**. It keeps multiple ongoing jobs readable and non-overlapping so different agents (Claude/Codex/etc.) can collaborate without re-explaining context or accidentally working on the same files.
- **Git** = long-term truth (diffs, history, accountability).
- **BLACKBOARD** = short-term coordination (jobs, task status, recent activity, validation, blockers).
- The BLACKBOARD is **not** a wiki, not a diary, and not a substitute for git history.

---

## Core goals
1. **Continuity:** any agent can resume a job in ~30 seconds.
2. **Parallel-safe coordination:** multiple jobs can progress simultaneously without file or structural collisions.
3. **Momentum-first:** large rewrites allowed; the constraint is **traceability + validation**, not diff size.
4. **Context efficiency:** the BLACKBOARD stays compact enough to scan quickly.

---

## Key concepts
### Job vs task
- A **Job** is a substantial, definable chunk of work ("lane"), typically within a larger project.
- Each job contains a task table (recommended ≤18 tasks; if it grows beyond that, split the job or move overflow into a separate backlog section).

### Non-job interactions
- Simple questions or one-off suggestions **do not** require creating a job.
- Create/log a job only when the work is **multi-step**, involves **code/structure changes**, or benefits from tracked progress/validation.

### Multi-job scope
- Support **up to 12 concurrent job slots** (J1–J12).
- Each job has a short description and a task table (recommended ≤18 tasks).

### Per-agent focus (parallel-safe)
- There is **no single global focus job**.
- The BLACKBOARD maintains an **Agent Focus Board** where each agent declares the job + task they are currently working on (with timestamp).
- Agents must **not switch their own focus** unless explicitly directed by the user.
- Agents may **log** new jobs into empty slots without starting them.

---

## Status system
### Job status (slot-level)
| Status | Meaning | Safe to park/overwrite? |
| --- | --- | --- |
| 🟢 **Active** | Work in progress, job is locked | No |
| 🟡 **Warm** | Unlocked, has recent progress | Ask first |
| 🔴 **Stalled** | Unlocked, no recent progress, may be blocked | Yes |
| ✅ **Complete** | All tasks resolved (✅ or ⛔) and initiator closure gate satisfied | Archive it |

**How to assess job status:**
- Job is locked → 🟢 Active
- Job is unlocked + within staleness threshold → 🟡 Warm
- Job is unlocked + past staleness threshold → 🔴 Stalled
- All tasks ✅ or ⛔ and initiator closure gate satisfied → ✅ Complete (then archive and clear slot)

**When to update job status (so it stays correct):**
- **On lock (before edits):** set `Status: 🟢 Active`.
- **On unlock (sign-off, not complete):** set `Status: 🟡 Warm` and ensure the job slot’s `Last progress tick` is up to date (if any tasks were completed/dropped).
- **On board scan:** if a job is `Lock: 🔓` and `global_tick - last_progress_tick` exceeds the threshold for its pace, flip it to `Status: 🔴 Stalled`.
- **On completion:** once the initiator closure gate is satisfied, archive the job log to `.ai/jobs/done/`, add Recent History + INDEX entry, then clear the slot (it becomes `(unassigned)` instead of staying `✅ Complete`).

### Task status emoji vocabulary
⬜ **Todo** | ▶️ **Active** | ⏸️ **Waiting** | ❓ **Blocked** | ⚠️ **Risk** | ✅ **Done** | ⛔ **Dropped**

### Task status rules
- Multiple ▶️ tasks within a job is fine when held by the same agent.
- If work cannot continue, mark the task ❓ Blocked and record **one crisp question** in that job's notes/activity.
- Use ⛔ Dropped when a task is intentionally abandoned (scope change, superseded, no longer relevant). Do not mark dropped tasks as ✅.

---
## Collision avoidance
### Collision risk is about shared context, not just shared files
Two overlap types:
- **File overlap:** editing the same files simultaneously (merge conflicts).
- **Structural overlap:** interacting architectural changes without awareness (conceptual conflicts).

Examples of structural overlap:
- One agent refactors authentication while another adds endpoints assuming the old pattern.
- One agent changes the data model while another builds features depending on the previous shape.
- One agent reorganizes module boundaries while another adds modules following the old structure.

### Default behavior: one agent per job
This is simple and avoids both file and structural risks. When in doubt, use this default.

### Parallel work across different jobs
Allowed if **key files don’t overlap** and there’s **no structural interaction**.

### Parallel work within the same job
Allowed only when:
- Tasks touch separate regions (different files **and** no structural interaction)
- Both agents note the coordination in their Focus Board entries
- The job’s collision check field notes the arrangement
- Any uncertainty is resolved by **asking the user first**

### Key files/paths
- Each job lists likely **Key files/paths** in its metadata.
- Before editing, agents scan other jobs’ key files for potential overlap.
- If overlap is suspected: write **OVERLAP: Jx** in the collision field and ask the user before proceeding.

### Resolving overlap
Prefer: split responsibilities by file/path or structural region, use separate branches/worktrees, or park one job to Back Burner.

---

## Timestamps, ordering, and staleness
### Timestamp format
- **Format:** `YYYY-MM-DD HH:MM UTC`
- **Use UTC consistently.** (Avoid local/UK time ambiguity.)
- If exact time is unavailable, use approximate time or write **TIME?**.
- Timestamps are for ordering/audit; **staleness is tracked by progress ticks**.

### Where to use timestamps
- Agent Focus Board entries
- Recent activity bullets
- Back Burner summaries
- Lock markers

### Staleness guidance (progress-based)
**Progress tick rule:** increment the global progress counter **by 1 for each task moved to ✅ or ⛔** (across any job). Each job stores the **last progress tick** when it last completed/dropped a task.

**Stale thresholds (by pace):**
- **Fast:** stale if `global_tick - last_progress_tick >= 6`
- **Normal:** stale if `global_tick - last_progress_tick >= 12`
- **Slow:** stale if `global_tick - last_progress_tick >= 24`

Staleness is used to:
- determine safe candidates for parking,
- identify jobs needing cleanup or attention,
- assess job status (🔴 Stalled vs 🟡 Warm).

When choosing what to park/resume/clean up, prefer the **largest progress delta** (oldest last progress tick).

---

## Ease scale (task complexity)
| Ease | Meaning | Typical duration |
| ---: | --- | --- |
| 1 | Trivial | Minutes; quick fix/config tweak |
| 2 | Simple | <1 hour; straightforward, low risk |
| 3 | Moderate | 1–3 hours; some complexity/deps |
| 4 | Substantial | Half day; multiple files/coordination |
| 5 | Complex | Full day; significant scope/testing/risk |
| 6 | Major | Multi-day; large rewrite/unknowns |

---
## Agent Focus Board
### Schema
| Agent | Job | Task | Status | Since (UTC) | Notes |
| --- | --- | --- | --- | --- | --- |
| Claude/Ivy | J2 | Add rate limiting | ▶️ | 2026-01-25 14:00 | Refactoring auth module |
| Codex/Atlas | J1 | Set up CI pipeline | ⏸️ | 2026-01-25 09:30 | Waiting on API keys |

### Rules
- Each agent has **at most one row** (one focus at a time).
- Agent Handle should include the model name (e.g., `Claude/<name>`, `Codex/<name>`).
- If no handle is provided, ask once; if ignored, self-assign a unique handle and proceed.
- Use task **name** (not task number).
- Update your row when you start, pause, switch, or finish.
- If your row exists and shows a job, work only inside that job unless the user redirects you.
- If your row doesn’t exist, create one when you begin work.
- Do not modify another agent’s row.
- If parallel work is agreed within the same job, both agents should note this in Notes.

### Human and agent attribution
- `Initiated by (human)` records the human who originated the tracked job.
- The Agent Handle and lock record which agent is currently responsible for execution.
- Preserve the original initiator through handoffs, parking, and archiving.
- Attribute a later human's material redirect or scope expansion in timestamped Recent Activity rather than overwriting the original initiator.
- When the initiator's name or team handle is missing, make three distinct, timestamped identification attempts:
  1. At job creation/onboarding.
  2. At the next meaningful human interaction or before a handoff.
  3. At a later interaction when closure is otherwise due, or immediately before parking/archiving.
- Repeating the question in one response is one attempt, not several. Log every attempt and its outcome in the job file.
- Until resolved, use `Pending confirmation (attempt n/3)` consistently in the BLACKBOARD, job log, and linked history.
- The initiator closure gate is not satisfied at attempt 1/3 or 2/3, so the job must not be parked or archived. After attempt 3, prefer leaving it waiting; only when closure is necessary and that attempt has genuinely gone unanswered may the fallback become `Unresolved after 3 documented attempts`.
- Never infer identity from usernames, paths, accounts, or machine metadata.

---

## Job slot schema
Each active job slot (in the BLACKBOARD) contains:
1. **Title** (short)
2. **Description** (1 sentence: what "done" means)
3. **Initiated by (human)** (name or stable team handle; otherwise `Pending confirmation (attempt n/3)`, with `Unresolved after 3 documented attempts` allowed only by the closure gate)
4. **Job status** (🟢/🟡/🔴/✅)
5. **Lock marker** (🔒/🔓 + agent + timestamp)
6. **Pace** (fast/normal/slow)
7. **Last progress tick** (integer; used for staleness)
8. **Key files/paths** (main files likely touched)
9. **Collision check** (overlap warnings/parallel notes)
10. **Job file pointer** (path under `.ai/jobs/active/`)

Detailed tasks, recent activity, and validation live in the per-job job log file (keep the BLACKBOARD compact).

---

## Job log schema (per-job file)
Each job log file (in `.ai/jobs/active/`) contains:
1. **Provenance** (`Initiated by (human)` copied unchanged from the BLACKBOARD summary; Agent owner may also be listed)
2. **Attribution attempts** (three timestamped checkpoints with outcome; required while initiator is unresolved)
3. **Task table** (recommended ≤18 rows)
4. **Ideas** (holding area)
5. **Recent activity** (newest-first; timestamped; keep short; attribute later human redirects)
6. **Validation** (most recent: commands run + results, or "not run")

### Task table schema (example)
| Status | Task | DONE means | Ease | Note |
| --- | --- | --- | ---: | --- |
| ⬜ | Implement login endpoint | Returns 200 with valid JWT | 3 | |
| ▶️ | Add rate limiting | 429 after 100 req/min | 2 | Using express-rate-limit |
| ✅ | Write auth tests | All auth tests pass | 2 | Validated: 12 tests, 100% pass |
| ⛔ | Add OAuth support | OAuth flow end-to-end | 4 | Descoped: revisit v2 |

### Task table requirements
- Columns: **Status | Task | DONE means | Ease (1–6) | Note**
- **DONE means:** one-line outcome definition (completion criterion).
- **Note:** use for validation evidence, `TEST:` failing-test-first intent, `ROLLBACK:` escape hatch, or reason when ⛔.

### Task completion rules
- A task should not be ✅ unless DONE means is met **and** a validation signal exists (or "not run" is explicitly noted).
- Dropped tasks must be ⛔ (not ✅) with a brief reason.

---
## Locking / unlock policy
### Principle
- Lock is **job-level** (not per-task). If you are working in a job, it should be locked.
- Locking is the default safeguard against file + structural collision.
- Parallel locking is allowed only with explicit coordination + user agreement.

### Lock markers
- `Lock: 🔒 <Agent> since YYYY-MM-DD HH:MM UTC`
- `Lock: 🔒 <Agent> + <Agent> since YYYY-MM-DD HH:MM UTC` (agreed parallel work)
- `Lock: 🔓`

### When to lock
- **Onboarding:** before editing, set lock to 🔒 with agent + timestamp.
- Simple Q&A → no lock.

### When to unlock
- **On sign-off:** if leaving idle, set lock 🔓; if user asked you to keep working later, you may leave it 🔒 but update timestamp/notes.

### Locked-job permission
- If locked by another agent: ask user to unlock or explicitly approve parallel work.
- Do not silently override locks.

### Freshness check
- Returning to a job you touched before: scan Recent activity timestamps; if newer activity exists, re-orient before edits. Log discrepancies if found.

---

## Back burner slots (parking)
Use Back Burner slots to park jobs you don’t want cluttering Active slots (and when all active job slots are full).

### Structure
- Maintain **BACK BURNER** slots (B1–B12).
- Store compact summaries so active slots remain focused.

### Safe candidate selection
Prefer parking a job that is:
1) 🔴 Stalled, 2) 🔓 Unlocked, 3) Beyond staleness threshold, and/or 4) Mostly not started (⬜) or blocked (❓).
If a 🟡 Warm job should be parked, ask the user first.
Avoid parking jobs that are 🟢 Active, locked, recently active, or mid-change on shared files.

### How to park a job
1) Confirm the initiator closure gate is satisfied; never park at attempt 1/3 or 2/3. Copy `Initiated by (human)` and its attribution-attempt log unchanged, plus a compact summary (3–6 bullets): objective, current state, main files, next actions, blockers.
2) Add a timestamp.
3) Clear the original job slot for reuse.

### Resuming a back-burner job
Rehydrate into an active job slot: restore `Initiated by (human)` and its attribution-attempt log unchanged with the title/description/key files, restore up to 18 tasks, lock when work begins, then clear the back-burner slot.

---

## Archiving / compression
When a job is finished (all tasks ✅ or ⛔) and its initiator closure gate is satisfied, archive it so the BLACKBOARD stays scannable but history remains recoverable.

### Where completed work lives
- **Full job history:** job log moved to `.ai/jobs/done/`.
- **Index/snippet:** a short entry in BLACKBOARD `Recent History`.

### Completion workflow (recommended)
1) Finalize the job log: all tasks ✅/⛔, final activity line (timestamped), validation recorded, and initiator resolved or the allowed `Unresolved after 3 documented attempts` closure fallback reached.
2) Move the job log to `.ai/jobs/done/`.
   - Recommended filename: `YYYY-MM-DD_HHMMUTC_Jx - <title>.md`
3) Add one BLACKBOARD `Recent History` entry:
   - `YYYY-MM-DD` + `Jx — <title>` + `initiated by: <human name or handle>`
   - 3–6 bullets (outcomes + key files + validation)
   - include path to the archived log
   - if `Recent History` exceeds 12 entries, prune the oldest entries
4) Append a one-line entry to `.ai/jobs/done/INDEX.md` (append-only):
   - `YYYY-MM-DD HH:MM UTC — Jx — <title> — initiated by: <human name or handle> — log: <path> — validation: <signal or not run>`
5) Clear the job slot: reset to `(unassigned)`, `Lock: 🔓`, ensure placeholder exists at `.ai/jobs/active/Jx - (unassigned).md`.

### Recent History guardrail
Keep `Recent History` short (recommended last 12 entries). Older detail lives in `.ai/jobs/done/` (and git history); `INDEX.md` is the long-term index.

---
## Handoff rituals
### Onboarding (when an agent begins)
1) Read BLACKBOARD top-to-bottom.
2) Check the **Agent Focus Board**.
3) If you already have a focus entry, work only inside that job.
4) If you do not have a focus entry, set one (job + task name + timestamp) as directed by the user.
5) Establish `Initiated by (human)` from the user's supplied name or stable team handle. If missing, record `Pending confirmation (attempt 1/3)`, make and timestamp attempt 1 at onboarding, then follow the three-checkpoint schedule under Human and agent attribution. Do not infer identity.
6) If the chosen job slot is empty or missing details, create/complete it:
   - title + 1-sentence description
   - `Initiated by (human)` in both the BLACKBOARD summary and job-log provenance, plus the job log's timestamped attribution-attempt section
   - job status (assess using guidance)
   - lock marker
   - key files/paths
   - populate up to 18 tasks from the user’s request (with DONE means)
7) Lock the job and set status 🟢 Active before edits.
8) Check for potential collision (file/structural) with other active jobs; note concerns in collision check.
9) If blocked, mark task ❓ and add one crisp question in job notes/activity.

### Sign-off (when an agent pauses/stops/switches)
1) Update the job log file (task statuses, recent activity, validation).
2) Update the BLACKBOARD summary block (lock/status/key files/collision/last progress tick).
3) If any tasks were set to ✅ or ⛔, increment the global progress counter by the number completed/dropped.
4) Update your Agent Focus Board row.
5) If leaving idle: unlock the job (🔓) and set status 🟡 Warm or 🔴 Stalled as appropriate.
6) If all tasks are ✅ or ⛔ and the initiator closure gate is satisfied: archive the job (move log to `.ai/jobs/done/`, add Recent History + INDEX), then clear the slot. Otherwise keep it unlocked and Warm while awaiting attribution.

### User-facing wrap-up (when stopping/pausing/finishing)
Include briefly: **Current job (Jx — title)**, **Current task(s)**, **Recommended next** (or one unblock question).

---

## Large rewrites policy (vibe-coding friendly)
Agents may rewrite entire files or restructure folders. Requirements:
- explain what changed (briefly)
- list files touched
- note migrations/renames if applicable
- provide validation steps/results
- include a rollback note for high-risk changes
Note: large rewrites increase structural collision risk; coordinate if other jobs are active in related areas.

---

## Validation policy
Confidence is not evidence. When a change is claimed to work, include at least one validation signal (build/lint/tests/manual check). If nothing was run, state **"not run"**.

---

## Debugging discipline (avoid going in circles)
If simple fixes fail (or are unlikely), step back and widen the hypothesis space. After ~2 failed attempts on the same narrow idea: list 3–6 plausible causes, choose the fastest discriminating test for each, gather evidence before more edits, record **tried → observed → next**.

---
## Additional best-practice principles (recommended)
- **Repro-first:** expected vs actual, minimal repro, proof signal.
- **Failing test first (when feasible):** for non-trivial/regression-prone bugs.
- **Rollback plan for high-risk changes:** one-line `ROLLBACK:` note.
- **Timebox loops + checkpoint state:** timebox further attempts; commit/stash checkpoints.
- **Assumptions explicit:** write down and verify quickly.
- **Destructive actions require permission:** no deletes/wipes/irreversible migrations without explicit ask.
- **Avoid stealth scope creep:** trade off tasks or log new job/back-burner entry.
- **Dependency/config changes traceable:** note files changed + validation results.

---

## Emergency procedures
### Blackboard corruption or conflict
Stop edits → restore last good from git → replay clearly-valid updates. If unrecoverable, notify user and reconstruct; log incident in Recent History.

### Disputed locks
Both agents stop → compare timestamps → ask user if unclear. Yielding agent waits or finds other work.

### Unknown agent activity
Note discrepancy in Recent activity; do not assume invalid; ask user before overwriting.

---

## Document maintenance workflow
### Principles-first workflow (this document)
When changing the BLACKBOARD system: update principles first, then the empty template, then live BLACKBOARD content (preserve active data).

### Data-preserving updates
When updating a live BLACKBOARD, do not overwrite active job data; reshape/wrap using the empty template structure.

---

## Scope boundaries
The BLACKBOARD is a coordination surface, not a full spec. If detail grows, move it to README/spec docs/issues/PRs/code comments.

---

## Quick reference
- Task status: ⬜ Todo | ▶️ Active | ⏸️ Waiting | ❓ Blocked | ⚠️ Risk | ✅ Done | ⛔ Dropped
- Job status: 🟢 Active | 🟡 Warm | 🔴 Stalled | ✅ Complete
- Ease scale: 1 Trivial | 2 Simple | 3 Moderate | 4 Substantial | 5 Complex | 6 Major
- Collision checklist: key files don’t overlap; no structural interaction; if unsure ask user.
