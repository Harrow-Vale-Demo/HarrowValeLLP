# Situate — The Five Rules

Same shape as Priya's three rules for `term-sheet-review`: non-negotiable,
short, and every rule exists because breaking it caused a real incident on
this project.

## Rule 1 — Never fabricate agreement

If two sources disagree, name the disagreement explicitly. Do not pick a
"winner" without stating why (freshness, git-verifiability, or user
confirmation). No papering over.

*Why:* the incident on 2026-07-30 where an earlier agent invented a plausible
story that all sources agreed the plugin was "installed and working" — because
the shelf reader returned data that matched the assumption. Ground truth
(`/plugin` panel) showed the opposite. A confident false report is worse than
"I don't know."

## Rule 2 — Zoom out; absence is a fact

Every report names every source read, even ones with nothing to say. If
`PLAN.md` doesn't exist, the report line reads `PLAN.md — absent`. Never omit
a source; omission looks identical to "no problem there" and hides drift.

*Why:* the `HANDOVER-to-claude-code.md` file was untracked and gitignored
during the drift session. Because no report mentioned it, the fact that a
handover was open at all went unnoticed. An `absent` line is a fact worth
seeing.

## Rule 3 — Prefer git-verifiable facts over doc claims

If `PLAN.md` says the branch is at commit X and `git log` says Y, git wins
and the doc is flagged as stale with the discrepancy shown.

*Why:* PLAN.md, LEDGER.md, and PROGRESS.md all drift when work moves faster
than the human writing them. Git doesn't drift — it's the ground truth for
anything git can answer.

## Rule 4 — Ask when ambiguous

If sources conflict and freshness/git-verifiability can't decide, or if
context is missing ("which session are you starting? which job are you
resuming?"), return a **clarifications-needed report** — list the specific
questions and stop. Do not infer resolutions from usernames, paths, or
machine metadata.

Model this on BLACKBOARD's three-attempt attribution loop, but a single
`situate` run counts as ONE attempt. The user re-runs after answering; the
skill does not loop.

*Why:* the BLACKBOARD protocol explicitly forbids inferring identity from
machine metadata. The same discipline applies to situate — an inferred
answer that's wrong is a Rule 1 breach in disguise.

## Rule 5 — Self-diagnose the caller

Also report the caller's own state:

- Is their Agent Handle on the Focus Board?
- Do they hold a job lock?
- Is their branch matched by any active job?
- Was their handle declared at all?

*Why:* the exact failure mode from the 2026-07-30 evening session: an agent
did substantial work (the packaging check) with no BLACKBOARD row, no lock,
and no handle. It only got caught retroactively. A situate run at session
start would have flagged it immediately.
