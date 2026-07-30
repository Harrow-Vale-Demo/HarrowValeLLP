---
name: situate
description: >-
  Multi-source sanity check for the current project. Reads every coordination
  file (BLACKBOARD, LEDGER, PLAN, PROGRESS, HANDOVER-*), git state, and the
  memory index, then reports either (a) a coherent one-page situation report
  answering "where is this project right now?" or (b) a clarifications-needed
  report when sources conflict. Also self-diagnoses the caller — are they on the
  Focus Board? do they hold a lock? — so drift is caught the moment it starts.
  Use at the start of every session, before a handoff, or when you suspect the
  coordination artifacts have drifted from git reality.
allowed-tools: Read, Grep, Glob, Bash
argument-hint: [--conflicts]
---

# Situate — Multi-Source Sanity Check (Harrow & Vale LLP)

You answer one question: **where is this project right now?** Then you report
every source you read, and you flag every disagreement between them. You never
invent a coherent story from incoherent inputs — silence about a divergence is
the failure mode that this skill exists to prevent.

## The five rules (Priya-style)

These are non-negotiable and define whether the output can be trusted:

1. **Never fabricate agreement.** If two sources disagree, name the disagreement
   explicitly. No papering over. Do not choose a "winner" without a stated
   reason (freshness, git-verifiability, or user confirmation).
2. **Zoom out.** Every report names every source read, even those with nothing
   to say. Absence of a source is a fact, not a gap.
3. **Prefer git-verifiable facts** over doc claims. If `PLAN.md` says the
   branch is at commit X and `git log` says Y, git wins and the doc is flagged
   as stale with the discrepancy shown.
4. **Ask when ambiguous.** If sources conflict and freshness/git-verifiability
   can't decide, or if context is missing ("which session are you starting?
   which job are you resuming?"), return a **clarifications-needed report** —
   list the specific questions and stop. Do **not** infer resolutions from
   usernames, paths, or machine metadata.
5. **Self-diagnose the caller.** Also report the caller's own state: are they
   on the Focus Board? do they hold a lock? does their handle look valid? This
   catches the failure mode where an agent works outside BLACKBOARD without
   knowing.

If following these rules means the output is "I can't produce a coherent
situation report without answers to these three questions," that is the correct
and desired behaviour. A partner would rather see an honest gap than a
confident guess.

## Modes

- **default** — produce a **situation report** (all-clear shape below) if
  sources are coherent, or a **clarifications-needed report** if not. Assumes
  you want to *act* on the answer.
- **`--conflicts`** — produce a **conflicts report** ordered by severity;
  purely diagnostic, no clarifications requested. Use when you want the full
  picture of every divergence, not the shortest path to a coherent one.

Both modes read the same sources (see `reference/sources.md`).

## Procedure

### Step 1 — Establish the caller

Before reading anything else, note the caller's declared **Agent Handle** (from
`Agent: <handle>` line in the current session, if any) and the current branch
and dirty state via `git branch --show-current` and `git status --short`.

If no handle is declared, flag this in the report as a self-diagnosis
divergence — the caller may be operating outside the BLACKBOARD protocol.

### Step 2 — Read every source, in order

Use `reference/sources.md` for the full list. For each source, record:

- **Path** — absolute or repo-relative.
- **Last modified** (or `git log -1 --format=%aI -- <path>` for tracked files).
- **Key claim(s)** relevant to "where is this project right now?" — one line each.
- **Present / absent** — absence is a fact, not skipped.

Do **not** skip a source because it looks unlikely to matter. Rule 2.

### Step 3 — Cross-check every source pair against git

For every claim about the tree, branch, commit, or PR state, verify it against
`git status`, `git log`, `git branch -vv`, and (if network available)
`git ls-remote origin` or the GitHub API. Rule 3.

Record disagreements as **divergences**, each with:

- **Sources involved** (two or more paths).
- **The disagreement** (one sentence).
- **Severity** — 🔴 blocks action / 🟡 misleading but non-blocking / ⚪ noted stale.
- **Resolution basis** — freshness, git-verifiability, or `AMBIGUOUS — needs user`.

Rule 1: never invent a winner.

### Step 4 — Self-diagnose the caller

Cross-reference the caller's declared Agent Handle and branch against the
Focus Board and any active job locks. Report as a self-diagnosis section:

- Handle present on Focus Board? Yes / No / `no handle declared`.
- Handle holds a job lock? Yes (which J-slot) / No / N/A.
- Caller's branch matches a job's expected working branch? Yes / No / N/A.
- Any Focus Board rows or J-slots claim the caller's current work? Yes / No.

If the caller has no handle, no Focus Board row, and no lock while doing
substantive work, that is a Rule 5 self-diagnosis divergence — flag it 🔴.

### Step 5 — Choose the output shape

- If **zero divergences of severity 🔴 or 🟡 AMBIGUOUS**: emit an **all-clear
  situation report**, name the suggested next action from the freshest source.
- If **any AMBIGUOUS divergence** in default mode: emit a **clarifications-
  needed report**. Do not attempt to guess through it.
- If in **`--conflicts` mode**: emit a **conflicts report** ordered by severity,
  regardless of ambiguity.

Use `reference/output-templates.md` verbatim for the exact shape.

## Output format

Every situate run stamps its own version (`Situate version: v0.1.0`) at the end
of the report. Absence of this line is the tell that the skill did not fire —
by design, per Phase 1c hardening.

## Self-check before returning

Confirm all of the following before you emit the report:

- [ ] Every source in `reference/sources.md` appears in the "Sources read"
      section — present or absent, none omitted (Rule 2).
- [ ] Every git-checkable claim was checked against git (Rule 3).
- [ ] No divergence was silently resolved (Rule 1).
- [ ] Caller self-diagnosis section is present (Rule 5).
- [ ] Output shape matches one of the three templates in
      `reference/output-templates.md` verbatim.
- [ ] `Situate version: v0.1.0` line is at the end.
