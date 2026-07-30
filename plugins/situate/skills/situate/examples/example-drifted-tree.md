# Example — Drifted tree, clarifications-needed report

Scenario: the actual tree state on 2026-07-30 evening when this skill was
being built. `feature/situate-skill` branched off `origin/master` but multiple
sources drift from git:

- `PLAN.md` (gitignored) references the older `feature/gate-packaging-check`
  branch as active work.
- `PROGRESS.md` (gitignored) says "session close — clean stopping point" but
  the working tree has multiple uncommitted files.
- `BLACKBOARD.md` Focus Board has five ✅ Complete rows from three prior
  handles plus one new 🟢 Active row for `Claude/Opus-4.7-Aurora`.
- `git remote get-url origin` still points at `f7-rage-gremlin/HarrowValeLLP`,
  but the API redirects (HTTP 301) to `Harrow-Vale-Demo/HarrowValeLLP`.
- PR #10 (`Feature/gate packaging check`) is open in the new org repo — not
  reflected in any doc on the current branch.

Caller declared `Agent: Claude/Opus-4.7-Aurora` and asked "situate this repo".

## Expected output

```
Agent: Claude/Opus-4.7-Aurora
Branch: feature/situate-skill

I cannot produce a coherent situation report without answers to the questions
below. Please answer, then re-run `/situate:situate`.

Clarifications needed:

1. `git remote get-url origin` reports `git@github.com:f7-rage-gremlin/HarrowValeLLP`,
   but the GitHub API returns HTTP 301 redirecting to
   `Harrow-Vale-Demo/HarrowValeLLP`. Should the local remote be updated to the
   new org URL, or is the redirect being tolerated intentionally?

2. `PROGRESS.md` says "session close — clean stopping point" at the top
   (2026-07-30 late), but the working tree has 4 modified files and 2
   untracked files on `feature/situate-skill`. Which is authoritative — the
   log claim or the git tree?

3. `PLAN.md §H` treats the `situate` skill as unstarted, but this branch is
   `feature/situate-skill` with situate files already authored. `PLAN.md` needs
   an update — is the caller planning to update it before session close, or
   should situate treat it as already stale?

4. PR #10 (`Feature/gate packaging check`) is open on the remote but no source
   on this branch mentions its state. Is the caller expected to act on it, or
   is it explicitly not this session's concern?

Sources read (partial picture, since conflicts blocked resolution):
  - .ai/BLACKBOARD.md                (last modified 2026-07-30, 1 active job: J1 locked by caller)
  - .ai/jobs/active/*.md             (12 files, 1 locked — J1 by caller)
  - .ai/jobs/done/INDEX.md           (last entry 2026-07-30 15:27 UTC — J2)
  - LEDGER.md                        (last entry 2026-07-30 17:37 — packaging-check branch pushed for PR)
  - PLAN.md                          (last modified 2026-07-30 18:06)
  - PROGRESS.md                      (last modified 2026-07-30 17:47)
  - SESSION.md                       (last modified 2026-07-30 18:30 — this session)
  - HANDOVER-*.md                    (none — HANDOVER-to-claude-code.md was deleted per its own instruction 2026-07-30)
  - git status / log / branch        (queried 2026-07-30 18:45 UTC)
  - memory index                     (loaded 2026-07-30 — 7 entries)

Situate version: v0.1.0
```

## Why this is the clarifications-needed shape

- Four AMBIGUOUS divergences: none can be resolved by git alone or by
  freshness alone; each needs the user's input.
- Rule 4: situate does not infer a "winner" from usernames or paths. It asks.
- The Sources read section is still complete — Rule 2 holds even in the
  partial picture.
- The self-diagnosis section is omitted from this template (it lives in
  Template A and Template C only) because the clarifications block the whole
  situation report.

## Tree state (for the gate)

`tree_state: drifted` — matches golden.

## Note on this example

This scenario is *real* — it's the actual state of the repository at the time
this file was written. That makes it a live demo opener candidate: run situate
against the tree with no rehearsal and let it call out the drift on the spot.
