# Example — Clean tree, all-clear situation report

Scenario: freshly-cloned repo on `master`, working tree clean, no active jobs,
no open handovers, LEDGER and BLACKBOARD in sync with git.

Caller declared `Agent: Claude/Sonnet-4.6-Demo` and asked "situate this repo".

## Expected output

```
Agent: Claude/Sonnet-4.6-Demo
Branch: master (ahead 0, behind 0, dirty? N)
Repo state: clean working tree; head at 1ad2382 "Merge pull request #11 from f7-rage-gremlin/demo/mock-skill-v1.1.0"

Active jobs on BLACKBOARD:
  no active jobs — all J-slots are (unassigned)

Most recent LEDGER entry: 2026-07-30 17:37 — HANDOVER jobs 1–5 all closed; packaging check landed in the gate; branch pushed for PR
Last PROGRESS.md session (if present): absent
Last SESSION.md session (if present): absent
Open handovers (if any): none

Self-diagnosis (caller):
  Handle on Focus Board: No
  Holds job lock: No
  Branch matches active job: N/A (no active job)
  ✅ caller is properly registered — no active job to claim; clean starting state

Divergences detected: 0
Suggested next action (from freshest source): start a new job in an unassigned J-slot if you plan to do substantive tracked work; otherwise proceed with simple Q&A per BLACKBOARD protocol.

Sources read:
  - .ai/BLACKBOARD.md                (last modified 2026-07-30)
  - .ai/jobs/active/*.md             (12 active job files, 0 locked)
  - .ai/jobs/done/INDEX.md           (last entry 2026-07-30)
  - LEDGER.md                        (last entry 2026-07-30)
  - PLAN.md                          (absent)
  - PROGRESS.md                      (absent)
  - SESSION.md                       (absent)
  - HANDOVER-*.md                    (none)
  - git status / log / branch        (queried 2026-07-31 09:15 UTC)
  - memory index                     (loaded 2026-07-31)

Situate version: v0.1.0
```

## Why this is the all-clear shape

- Zero divergences of any severity.
- Self-diagnosis is a ✅ — no lock needed for a fresh session that hasn't
  started substantive work yet.
- Suggested next action comes from the freshest source (BLACKBOARD's rules on
  when to claim a J-slot).
- Every source in `reference/sources.md` appears with a status; the absent
  ones (`PLAN.md`, `PROGRESS.md`, `SESSION.md`, `HANDOVER-*.md`) are named
  present-or-absent, not omitted.

## Tree state (for the gate)

`tree_state: clean` — matches golden.
