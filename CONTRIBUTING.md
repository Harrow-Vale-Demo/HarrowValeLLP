# Contributing to the Hackathon Repository

This repository is the team's single shared project, not a collection of personal copies.

## Minimal workflow

1. Pull the latest `master` before starting a task.
2. Create one short-lived branch for one coherent change.
3. Put files in the component they belong to (`assets`, `demo`, `deliverables`, `docs`, `plugins`, `releases`, or `tools`), not in a contributor-named folder.
4. Run the checks relevant to the change.
5. Open a pull request into `master` and record the check results in its description.
6. Ask at least one teammate to review, then merge and delete the branch.

Suggested branch names:

- `feature/<short-description>`
- `fix/<short-description>`
- `docs/<short-description>`
- `refactor/<short-description>`

## Coordination

Use GitHub issues for tasks that need ownership or discussion. Keep `LEDGER.md` as a concise chronological handoff log; do not use it as a substitute for evidence that a deliverable has actually been run or reviewed.

Changes to approved release history have additional requirements in `releases/CONTRIBUTING.md`. Existing version folders under `releases/` are immutable; create a new semantic version instead of modifying an approved snapshot.

## Local checkouts

Contributors may clone the repository to different absolute paths. Keep the active checkout outside Google Drive or similar synchronisation folders, and use GitHub for collaboration and backup.