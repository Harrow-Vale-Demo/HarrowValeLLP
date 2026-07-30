# Situate — Sources to read

Every situate run reads every source below, in this order. Absence is a fact,
not a skipped step. If a source is missing, report it as `absent` in the
"Sources read" section — do not omit the row.

## Repository coordination files

| Source | Purpose | Where to look for the key fact |
|---|---|---|
| `.ai/BLACKBOARD.md` | Live focus board, active jobs, locks | Focus Board table + Active Job Slots + Global progress counter |
| `.ai/jobs/active/*.md` | Per-job details | Each active job's Tasks table + Recent activity + Validation |
| `.ai/jobs/done/INDEX.md` | Recent completions | Most recent 3–5 entries |
| `LEDGER.md` | Durable coordination history | Most recent Log entry at the top of §Log |
| `PLAN.md` | Master intent & status *(gitignored)* | "Where we are" section + "What's next" |
| `PROGRESS.md` | Personal running log across sessions *(gitignored)* | Top block (newest-first) |
| `SESSION.md` | Current session working doc *(gitignored)* | "Session goal" + "Running log" |
| `HANDOVER-*.md` | Cross-machine or cross-session handovers | Existence alone matters — an open handover is a claim |
| `CLAUDE.md` / `AGENTS.md` | Repository operating protocol | Not typically a divergence source; report if modified since last commit |

## Git ground truth

Run each of these fresh; do not trust cached values from docs.

- `git branch --show-current` — the branch the caller is on
- `git status --short` — dirty state
- `git log -1 --format='%h %s' HEAD` — head commit
- `git log --oneline origin/master ^HEAD | head` — commits behind master
- `git log --oneline HEAD ^origin/master | head` — commits ahead of master
- `git stash list` — any pending stashes (often forgotten)
- `git branch -vv` — tracked-branch relationships
- `git remote get-url origin` — for org-migration or redirect detection

## Remote state (best-effort)

Only if the network is available and unauthenticated calls suffice:

- `curl -sIL https://api.github.com/repos/<owner>/<repo>` — follows redirects,
  reveals org moves and visibility (`private: true|false`)
- `curl -s https://api.github.com/repos/<owner>/<repo>/pulls?state=open` — open PRs

Never assume the local `origin` URL is current. GitHub silently redirects
moved repos; verify.

## Session context

- **Agent Handle** — the `Agent: <handle>` line the caller declared. If none,
  self-diagnose (Rule 5).
- **Memory index** — `~/.claude/projects/<slug>/memory/MEMORY.md` if present.
  Useful for prior-session learnings that might contradict current docs.

## What NOT to read

- Skill implementations, source code, test fixtures — situate is about
  *coordination state*, not code correctness.
- Anything under `.git/objects` or `.git/refs` directly — use `git` commands.
- Anything outside the current working directory or the memory dir.
