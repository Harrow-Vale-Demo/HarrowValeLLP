# Contributing & Approval Process — Harrow & Vale Approved Skills

This repo is the firm's single source of truth for Claude skills. Nothing ships here without going through this process — the whole point is that a skill installed from this repo has been vetted, unlike a personal prompt.

## Who vets

- **Tom Harrow** (Ops & Knowledge Lead) — reviews every pull request for process: does it have a clear `SKILL.md` frontmatter, does it follow the house conventions in `.claude/rules/`, does it include an eval run against representative documents.
- **Priya Vale** (Managing Partner) — reviews every pull request for substance on anything touching due-diligence logic: does it correctly reflect the firm's standing checklist, does it avoid inventing categories, does its market-standard baseline hold up.
- A version is only tagged and published to `marketplace.json` once **both** have approved the PR.

## How a change ships (v1 → v2 example)

1. Open a PR against the relevant `plugins/<skill-name>/` folder with the proposed change.
2. Re-run the skill's eval set (e.g. `plugins/term-sheet-review/v1.0.0/eval/` — carry forward and extend this on every version) against all existing regression documents plus any new case that motivated the change. Attach the results to the PR.
3. Tom reviews for process/consistency; Priya reviews for substantive correctness.
4. On approval: bump the version directory (semver — patch for wording fixes, minor for new checklist coverage, major for a changed output shape), add a `CHANGELOG.md` entry, and update the version + `source` path in `.claude-plugin/marketplace.json`.
5. Merge and tag a GitHub release (e.g. `term-sheet-review-v1.1.0`).

## How a lawyer installs and updates

**First-time install (once per lawyer):**
```
/plugin marketplace add harrow-vale/harrow-vale-skills
/plugin install term-sheet-review@harrow-vale-skills
```

**Getting a new version:** once a new version is merged and tagged, each lawyer runs:
```
/plugin marketplace update harrow-vale-skills
/plugin update term-sheet-review
```
No manual file copying, no re-pasting a prompt — the update is pulled from the approved marketplace entry.

## House conventions

Shared conventions (output tone, checklist authority, plain-English requirement) live in `.claude/rules/` at the root of this repo so every skill added here — not just `term-sheet-review` — inherits the same standards without repeating them in each `SKILL.md`.
