# H5 — A second marketplace manifest, and version pinning against a stale checkout

**Found:** 2026-07-29 by Phurin Rintanalert; re-examined 2026-07-31
**Class:** Distribution integrity
**Status:** Orphan removed; **Phurin's fix branch is still unmerged**
**Severity:** Was high. A competing manifest and a version-pinned stale checkout can each make a skill invisible or wrong on a colleague's machine with no error shown.

---

## Two coupled faults

### 1. A second, orphaned `marketplace.json`

There were two marketplace manifests in the repository:

- `.claude-plugin/marketplace.json` — the real shelf, at the repo root
- `tools/termsheet-harness/.claude-plugin/marketplace.json` — 35 lines, **pointing at a
  directory that was not a plugin**, referenced by neither `CLAUDE.md` nor `README.md`

Phurin's commit message on `903368f` describes it exactly: *"removes the orphaned, conflicting
duplicate marketplace.json under `tools/termsheet-harness/.claude-plugin/` that pointed at a
non-plugin directory and was never referenced."*

**Why a duplicate manifest is dangerous.** Marketplaces are keyed by *name*. Two manifests
declaring overlapping names, or a manifest pointing at paths that don't resolve to plugins, give
you a shelf that registers but serves nothing installable — and the failure presents as "the
plugin isn't there" rather than as an error naming the manifest.

### 2. Version pinning against a stale checkout

Claude Code pins plugin updates to the **version string** in `plugin.json` (or, absent one, the
commit SHA). Two consequences that bit this project:

- A local checkout behind `origin/master` serves an **old catalogue** to a locally-added
  marketplace. Recorded in `PLAN.md`: local was at `37a8201`, remote at `bd3de62`, and the
  installed plugin was pinned to the older SHA. Nothing was misconfigured — the checkout was
  simply behind.
- Conversely, a one-character edit to a `version` field disseminates to every machine on the
  policy. That is the hole `check_published.py` exists to close, by asserting every published
  version is backed by a stored gate report.

Combined with the out-of-date runtime in [H1](H1-runtime-version-and-false-verification.md), this
produced the "installed and uninstalled at the same time" symptom that consumed most of two
sessions.

## Current state — checked 2026-07-31

| Item | State |
|---|---|
| Orphaned `tools/termsheet-harness/.claude-plugin/marketplace.json` | **Gone.** Only `./.claude-plugin/marketplace.json` exists on disk. Removed by another route — Lee's layout refactor `e5e2fa9` — so Phurin's deletion is now redundant. |
| Phurin's branch `dd-checklist-marketplace-plugin-and-fixed-json` | **NOT MERGED.** Confirmed: `903368f` is not an ancestor of `origin/master`. |
| The rest of that branch | Still missing from master — see [H4](H4-duplicate-overlapping-projects.md). It packages `dd-checklist` as `plugins/dd-checklist-mapper-plugin/` and lists it on the shelf. |
| Local vs origin | In sync at time of writing. |

So the *manifest* half of this issue resolved itself incidentally, and nobody recorded that it
had. The *plugin-packaging* half is still sitting on an unmerged branch.

## Preventive checks

- [x] `check_published.py` — asserts every published version is gate-backed and that
      `plugin.json` and the shelf agree
- [ ] **Assert exactly one `marketplace.json` exists**, at the repo root. A two-line check that
      would have caught the orphan immediately and will catch the next one. Cheap; add it to
      `check_published.py`.
- [ ] **Assert every `source` path in `marketplace.json` resolves to a directory containing
      `.claude-plugin/plugin.json`.** The orphan's specific fault was pointing at a non-plugin
      directory, and nothing currently tests that.
- [ ] **Document the pinning behaviour where people will hit it** — that a local checkout behind
      `origin/master` serves an old catalogue, and that `git pull` is part of demo prep. The
      symptom is indistinguishable from a broken install.
- [ ] **Add an unmerged-branch sweep to demo prep.** This issue was only found because someone
      asked about commit history. `git branch -r` plus a merge check takes seconds; see the
      command in H4.

## Lessons

1. **A manifest that points nowhere fails silently.** The plugin system reports "not available",
   not "your manifest is wrong". Assert structural validity, don't infer it from behaviour.
2. **"Fixed on a branch" is not fixed.** Phurin diagnosed and fixed this correctly on 2026-07-29.
   Two days later the diagnosis was being rediscovered from scratch because the branch never
   merged. Unmerged work is indistinguishable from work never done.
3. **Record incidental fixes.** The orphan was removed by a refactor with an unrelated commit
   message. Nobody knew the issue was closed, so it stayed live in everyone's mental model.
4. **Version pinning means "stale checkout" and "broken install" look identical.** Check
   `git status` against origin before diagnosing anything else.
