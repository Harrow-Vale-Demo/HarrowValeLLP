# CLAUDE.md — Repository and BLACKBOARD Operating Instructions

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## BLACKBOARD Operating Protocol (v4)

### What the BLACKBOARD is 🧭

`.ai/BLACKBOARD.md` is the repository's **shared working memory** and **job dashboard**.

- **Git** is the long-term record: diffs, history, and completed changes.
- **BLACKBOARD** is the live coordination layer: agent focus, jobs, locks, blockers, and collision notes.
- **Job logs** hold extended task tables, activity, evidence, and validation in `.ai/jobs/active/`, `.ai/jobs/backburner/`, and `.ai/jobs/done/`.

Simple Q&A does **not** require a job. Create and log a job only for multi-step tracked work.

### Non-negotiables ✅

- First repository action every session: read `.ai/BLACKBOARD.md` top-to-bottom **before any work**.
- If multiple Claude sessions or agents may be active, use a unique **Agent Handle** that includes the model name, such as `Claude/<name>`. If no handle is provided, ask once; if unanswered and work must proceed, self-assign one.
- Every tracked job records `Initiated by (human): <name or team handle>`. Make three logged identification attempts at distinct checkpoints. Until resolved, use `Pending confirmation (attempt n/3)`; only after the third attempt has genuinely gone unanswered may a closure-required record use `Unresolved after 3 documented attempts`. Never infer identity.
- Start every chat response with `Agent: <AgentHandle>`. Include the same handle in every BLACKBOARD Focus Board row, lock, and activity entry.
- Use the **Agent Focus Board** for per-agent focus. Own only your row; create it if missing and never overwrite another agent's row.
- Do not switch focus unless the user explicitly directs it.
- Acquire a **job-level lock before edits**. Do not work in a job locked by another agent without user permission.
- Before edits, scan every other job's key files and structural collision notes. If overlap is suspected, write `OVERLAP: Jx` and ask the user before proceeding.
- Timestamp meaningful updates in UTC using `YYYY-MM-DD HH:MM UTC`.
- Big rewrites are allowed, but leave a clean trail: files, migration notes, validation, and rollback guidance.

### Claude's default role 🎓

Prioritize clarifying intent, edge cases, and acceptance criteria; architecture and maintainability trade-offs; broad debugging plans; review of other agents' large changes for regressions and assumptions; and translating "vibe goals" into concrete tasks, DONE means, and validation.

If implementation is straightforward and unambiguous, hand off execution to Codex through the BLACKBOARD.

### Human and agent attribution

`Initiated by (human)` records the human who originated the tracked job. `AgentHandle` records the agent currently executing or coordinating it. Preserve the original human initiator through handoffs, parking, and archiving. If another human materially redirects or expands the work, attribute that change in a timestamped Recent Activity entry rather than replacing the origin.

If no name or stable team handle is supplied, make three distinct, timestamped identification attempts:

1. At job creation/onboarding.
2. At the next meaningful human interaction or before a handoff.
3. At a later interaction when closure is otherwise due, or immediately before parking/archiving.

Repeating the question in one response counts as one attempt. Log each attempt and outcome in the job file. While unresolved, use `Pending confirmation (attempt n/3)` everywhere. Do not park or archive at attempt 1/3 or 2/3. After attempt 3, prefer waiting for an answer; only when closure is necessary and that attempt has genuinely gone unanswered may the fallback become `Unresolved after 3 documented attempts`. Never infer identity from usernames, paths, accounts, or machine metadata.

### Operational loop 🔁

#### Onboarding

0. Establish the `AgentHandle` without doing repository work.
1. Read `.ai/BLACKBOARD.md` top-to-bottom.
2. Update only your **Agent Focus Board** row: Job, Task, Status, Since (UTC), and Notes.
3. Select a job slot and inspect its lock, freshness, key paths, and collision notes.
4. If the selected slot is missing or unassigned, create both:
   - A compact summary in `.ai/BLACKBOARD.md` containing title, one-sentence description, `Initiated by (human)`, status, `Lock: 🔒 <AgentHandle> since <UTC>`, pace, current global progress tick, key files/paths, collision notes, and a link to the job log.
   - A job log in `.ai/jobs/active/` containing provenance with the same `Initiated by (human)` value, a timestamped attribution-attempt log, a task table (recommended maximum 18 tasks), one-line DONE means, Ease 1–6, recent activity, validation, and an Ideas holding area.
5. Perform the collision check across other jobs. If either file or structural overlap is plausible, mark `OVERLAP: Jx` and ask the user.
6. Begin work only while holding the job lock. Multiple active tasks inside that locked job are allowed.

Ease scale: 1 trivial, 2 simple, 3 moderate, 4 substantial, 5 complex, 6 major.

#### Sign-off when pausing, stopping, or switching agent/model

- Update the job log's task statuses (`⬜` `▶️` `⏸️` `❓` `⚠️` `✅` `⛔`).
- Add a timestamped recent-activity entry in the form `tried → observed → next`.
- Record validation that was run and its result, or explicitly state `not run`.
- Update the BLACKBOARD job summary and your Focus Board row.
- Whenever a task moves to `✅` or `⛔`, increment the BLACKBOARD global progress counter and set that job's `Last progress tick` to the new value.
- If leaving an incomplete job idle, set `Lock: 🔓` and `Status: 🟡 Warm`.
- If initiator attribution remains pending, make the next due identification attempt and update its log. A fully resolved task table does not permit parking or archiving at attempt 1/3 or 2/3.
- If every task is `✅` or `⛔` and initiator attribution is resolved or has reached the allowed closure fallback:
  - Archive the job log to `.ai/jobs/done/YYYY-MM-DD_HHMMUTC_Jx - <title>.md`.
  - Append an entry to `.ai/jobs/done/INDEX.md` that includes `Initiated by (human)`.
  - Add a concise BLACKBOARD Recent History entry that includes `Initiated by (human)` and prune it to the most recent 12 entries.
  - Reset the active slot to `(unassigned)`, unlock it, and ensure its unassigned placeholder log exists.

#### User-facing wrap-up

Briefly state the current job, current task or tasks, and the recommended next action or one unblock question.

### Locking and freshness 🔒

- Locks are job-level, not task-level.
- If a job is locked by another agent, stop and ask the user to unlock it or explicitly approve parallel work.
- When returning to a job previously touched, scan timestamps and recent activity. If newer work exists, re-orient before editing.
- If a lock is disputed, both agents stop, compare timestamps, and ask the user when ownership remains unclear.

### Collision avoidance 🧩

Treat both kinds of overlap as real:

- **File overlap:** two jobs touch the same files or paths.
- **Structural overlap:** two jobs depend on incompatible architecture or data-model assumptions.

When overlap is suspected, mark it, ask before proceeding, and prefer a file split, separate branches, or parking one job in the Back Burner.

### Back Burner

Use `B1`–`B12` to park work without cluttering active slots. Prefer parking stalled and unlocked work. Ask the user before parking a warm job. Preserve `Initiated by (human)` and its attribution-attempt log when parking and rehydrating work. Never park a job whose initiator remains at attempt 1/3 or 2/3. Before resuming a back-burner item, rehydrate it into an active job slot and acquire its lock.

### Debugging discipline 🧪

If a narrow fix fails about twice, or confidence is low, stop guess-and-patch loops. List three to six plausible causes, choose the fastest discriminating test for each, gather evidence, and record `tried → observed → next` before further edits.

### Evidence habits ✅

- Reproduce first: expected versus actual, minimal repro, and a proof signal.
- Prefer a failing test first for non-trivial or regression-prone bugs, or state why one is not appropriate.
- For risky changes, record `ROLLBACK: revert <commit/PR> / flip flag / restore entrypoint`.
- Timebox investigative loops and checkpoint before risky moves.
- State assumptions explicitly.

### Safety and scope 🧯

- Do not perform destructive actions—deletes, wipes, irreversible migrations, or key rotation—without explicit user permission.
- Do not expand scope silently. Trade off tasks or log a new job or back-burner entry.
- If the BLACKBOARD is conflicted or corrupted, stop edits, restore the last good version from Git, and replay only clearly valid updates.
- If changes are of unknown ownership, log the discrepancy and ask before overwriting.

## App plan documentation

When a project uses an app plan folder such as `docs/app_plan/`:

- Keep it updated as work progresses.
- Use a two-letter prefix for ordering, such as `AA_`, `BA_`, or `CA_`, and spread initial sections across the alphabet so later documents can slot between them.
- Header files have no extension, use an `h` after the two-letter prefix, and use an all-caps title, for example `ABh_VISION_AND_PLATFORMS`.
- Content files use `XY_Title.md`.
- Update the index, such as `AA_Index.md`, whenever sections are added or moved.
- Each planning subsection should record:
  - The overview or details that must be remembered for the major plan.
  - Goals to achieve or already achieved, including the achievement date for completed goals.

## Project Overview

This is a hackathon project for Harrow & Vale LLP, a boutique VC/M&A law firm. The core deliverable is a Claude Skill that reviews venture term sheets against the firm's fixed due-diligence checklist.

## Repository Structure

- `plugins/term-sheet-review-plugin/` - Current packaged and installable skill
  - `skills/term-sheet-review/SKILL.md` - Main skill definition and procedure
  - `skills/term-sheet-review/reference/` - Checklist and standard-term references
  - `skills/term-sheet-review/examples/` - Worked examples for all four formats
- `plugins/cool-new-skill/` - Instrument-triage skill; worked example for the pipeline demo
- `releases/term-sheet-review/` - Frozen semantic-version snapshots and approval evidence
- `tools/skill-gate/` - The firm-wide approval gate (`gate.py`), every skill's fixtures under
  `fixtures/<skill>/` and graders under `scorers/`, the only sanctioned publisher
  (`publish.py`), and the published-version consistency check (`check_published.py`)
- `tools/termsheet-harness/` - Term-sheet contract, reference baselines, DD mapper, generated reports
- `assets/source/` - Canonical mock source documents
  - `term-sheets/` - SAFE, Series A, convertible note, and seed samples
  - `data-room/` - GreenGrid supporting documents
  - `dd-checklist/` - Priya's fixed due-diligence checklist
- `assets/legacy-raw-import/` - Legacy import retained only for provenance
- `deliverables/` - Client-facing written outputs and proposal source
- `demo/` - Standalone interactive review demo
- `presentation/` - Standalone browser presentation
- `docs/` - Discovery, engagement, and governance material
- `LEDGER.md` - Durable coordination and audit log
- `.claude-plugin/marketplace.json` - Root plugin marketplace manifest

Do not edit an existing release snapshot in place. Change the active plugin, validate it, and create a new release version through the approval process in `releases/CONTRIBUTING.md`.

## Skill Usage

*Verified against Claude Code 2.1.140, 2026-07-30.*

Plugin skills are namespaced by plugin name. Once installed from the
marketplace, either invocation route works and both hit the same `SKILL.md`:

**As a namespaced slash command** — deterministic, useful in a demo:

```
/term-sheet-review:term-sheet-review <path-to-term-sheet>
/term-sheet-review:term-sheet-review <path-to-term-sheet> --dd-room <path-to-folder>
/cool-new-skill:cool-new-skill <path-to-document>
```

**In plain language** — Claude reads each skill's `description` frontmatter and
picks the right skill from what you ask for:

```
Review assets/source/term-sheets/safe-nimbus-robotics.md against our DD checklist
Review the GreenGrid Series A, with the data room at assets/source/data-room/
Triage assets/source/dd-checklist/harrow-vale-dd-checklist.md
```

To confirm a plugin is installed, open the `/plugin` panel and read which section
it sits in — **Installed** means on this machine, **Discover** means on the shelf
but not installed. Do not verify by asking an agent to "list installed plugins":
reading `.claude-plugin/marketplace.json` returns the *shelf*, which looks
identical on a machine with nothing installed.

If a skill is installed but does not trigger, the running session is still holding
the plugins it launched with. Run `/reload-plugins`, or restart.

## Key Design Constraints (Priya's Rules)

These are non-negotiable requirements from the Managing Partner:

1. **Use the fixed checklist verbatim** - The checklist is the ground truth. Never invent, rename, or merge checklist items.
2. **Never skip a step** - Every checklist item must appear with an explicit status (PRESENT/MISSING/N/A).
3. **Never fabricate** - Only report values that appear in documents. Mark absent terms as "Not stated", not guessed.

## Instrument Types

The skill classifies term sheets from document content:

- **SAFE** - "future equity", no interest, no maturity, converts at cap/discount
- **Convertible loan note** - interest rate and maturity/redemption date
- **Priced round** - price per share and stated pre/post-money valuation

## Coordination and LEDGER

- Use `.ai/BLACKBOARD.md` as the authoritative live dashboard for focus, job ownership, locks, collisions, blockers, and current status.
- Use the corresponding `.ai/jobs/` log for detailed tasks, activity, evidence, and validation.
- Use Git as the durable record of code and document changes.
- Keep `LEDGER.md` for durable project coordination and audit handoffs; it does not replace a BLACKBOARD lock or Focus Board update.
- Add new LEDGER entries at the top of its Log section using `### [YYYY-MM-DD HH:MM] <author> — <one-line summary>`.
