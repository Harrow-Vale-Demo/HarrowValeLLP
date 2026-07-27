# Contributing to Approved Skill Releases

The `releases/` tree is the auditable history of approved skill versions. Existing version folders are immutable.

## Who vets

- **Tom Harrow** (Ops & Knowledge Lead) reviews process, structure, and evaluation evidence.
- **Priya Vale** (Managing Partner) reviews substantive due-diligence accuracy.
- A new version is archived only after both reviews are complete.

## How a change ships

1. Change the active skill under `plugins/<plugin-name>/` on a feature branch.
2. Re-run the representative evaluation set and the executable harness under `tools/termsheet-harness/`.
3. Open a pull request containing the proposed behavior, evidence, and any new regression case.
4. After approval, create a new semantic-version directory under `releases/<skill-name>/`; do not alter an older version.
5. Update `releases/<skill-name>/CHANGELOG.md` and the active plugin/marketplace version when that version is actually promoted.
6. Merge into `master` and tag the approved release.

Use a patch version for wording/bug fixes, a minor version for new non-breaking coverage, and a major version for an incompatible output change.

## House rules

The fixed checklist remains authoritative, every item receives an explicit status, extracted facts require source support, and deviations are explained in plain English.