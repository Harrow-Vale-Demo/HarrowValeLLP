# Situate — Output Templates

Every situate run uses ONE of these three shapes verbatim. The shape is
determined by Step 5 of the procedure in `SKILL.md`.

Every template ends with `Situate version: v0.1.0` on its own line — absence
of that line is the tell that the skill did not fire.

---

## Template A — All-clear situation report

Use when there are **zero divergences of severity 🔴 or AMBIGUOUS** in default
mode.

```
Agent: <caller handle, or "UNKNOWN — no handle declared">
Branch: <branch-name> (ahead N, behind M, dirty? Y/N)
Repo state: <one-line summary of git tree>

Active jobs on BLACKBOARD:
  <J-slot> — <title> — <handle> — <lock>
  ...
  (or "no active jobs" if all slots are (unassigned))

Most recent LEDGER entry: <YYYY-MM-DD HH:MM> — <one-liner>
Last PROGRESS.md session (if present): <YYYY-MM-DD> — <one-liner>
Last SESSION.md session (if present): <YYYY-MM-DD> — <one-liner>
Open handovers (if any): <paths, or "none">

Self-diagnosis (caller):
  Handle on Focus Board: <Yes | No | no handle declared>
  Holds job lock: <Yes: J<n> | No | N/A>
  Branch matches active job: <Yes | No | N/A>
  ✅ caller is properly registered
  (or list of self-diagnosis issues if any 🟡/⚪)

Divergences detected: 0
Suggested next action (from freshest source): <one line>

Sources read:
  - .ai/BLACKBOARD.md                (last modified <YYYY-MM-DD>)
  - .ai/jobs/active/*.md             (N active job files, X locked)
  - .ai/jobs/done/INDEX.md           (last entry <YYYY-MM-DD>)
  - LEDGER.md                        (last entry <YYYY-MM-DD>)
  - PLAN.md                          (last modified <YYYY-MM-DD>, or "absent")
  - PROGRESS.md                      (last modified <YYYY-MM-DD>, or "absent")
  - SESSION.md                       (last modified <YYYY-MM-DD>, or "absent")
  - HANDOVER-*.md                    (N files, or "none")
  - git status / log / branch        (queried <YYYY-MM-DD HH:MM UTC>)
  - memory index                     (loaded <YYYY-MM-DD>, or "absent")

Situate version: v0.1.0
```

---

## Template B — Clarifications-needed report

Use when default mode encounters **any AMBIGUOUS divergence** — i.e. sources
conflict and freshness/git-verifiability cannot decide.

```
Agent: <caller handle, or "UNKNOWN — no handle declared">
Branch: <branch-name>

I cannot produce a coherent situation report without answers to the questions
below. Please answer, then re-run `/situate:situate`.

Clarifications needed:

1. <specific question — e.g. "PLAN.md §H says branch is on commit ABC but
   git shows XYZ. Which is authoritative?">
2. <e.g. "BLACKBOARD J2 is locked by Codex/Vellum since 2026-07-30, but
   LEDGER says Lee closed that work on the same day. Is J2 done?">
3. <e.g. "No caller handle declared. Which agent handle is this session
   running under?">

Sources read (partial picture, since conflicts blocked resolution):
  <same "Sources read" list as Template A>

Situate version: v0.1.0
```

---

## Template C — Conflicts report (`--conflicts` mode)

Use in `--conflicts` mode regardless of ambiguity. Severity-ordered; purely
diagnostic. Does not request answers.

```
Agent: <caller handle, or "UNKNOWN — no handle declared">
Branch: <branch-name>
Mode: --conflicts

Divergences detected: N (severity-ordered)

🔴 BLOCKING
  1. <one-sentence disagreement>
     Sources: <a.md, b.md>
     Resolution basis: <freshness | git-verifiability | AMBIGUOUS — needs user>
  2. ...

🟡 MISLEADING
  ...

⚪ STALE
  ...

Self-diagnosis (caller):
  Handle on Focus Board: <Yes | No | no handle declared>
  Holds job lock: <Yes: J<n> | No | N/A>
  Branch matches active job: <Yes | No | N/A>
  <🔴/🟡/⚪ list of self-diagnosis divergences, if any>

Sources read:
  <same "Sources read" list as Template A>

Situate version: v0.1.0
```

---

## Severity guide

- **🔴 BLOCKING** — proceeding on this state will produce wrong work
  (e.g. an active job is locked by another agent, but the caller is about to
  edit its key files).
- **🟡 MISLEADING** — a document says something that isn't currently true
  (e.g. `PLAN.md` names a branch that no longer exists). Not blocking, but
  the reader will be confused.
- **⚪ STALE** — a document hasn't been updated in a while but isn't
  actively wrong. Noted for hygiene.
