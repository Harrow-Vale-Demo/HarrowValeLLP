# Hardening Index

> One document per issue. An issue earns a document here when it is a **class of failure**
> worth designing against, not a one-off bug that was fixed and forgotten.
>
> Naming: `H<n>-<short-slug>.md`. Numbers are permanent — never reuse one, even after an issue
> is closed.
>
> These are internal engineering records. They are deliberately blunt about what went wrong.
> Decide separately, and deliberately, how much of this belongs in client-facing material —
> the current default is that hardening lives here and not in the deck or case study.

| # | Issue | Class | Status |
|---|---|---|---|
| [H1](H1-runtime-version-and-false-verification.md) | Out-of-date runtime, plus an install check that confirmed itself | Verification integrity | Closed |
| [H2](H2-skill-packaging-dropped-references.md) | Desktop upload shipped `SKILL.md` without its `reference/` files | Packaging integrity | Closed, check outstanding |
| [H3](H3-answer-key-contamination.md) | Skill ships worked answers for its own test documents; Rules 1 and 2 breached | Evaluation integrity | Open |
| [H4](H4-duplicate-overlapping-projects.md) | Two parallel term-sheet systems, two skills with the same name, three status vocabularies | Source-of-truth integrity | Open |
| [H5](H5-orphaned-marketplace-manifest.md) | A second marketplace manifest, and version pinning against a stale checkout | Distribution integrity | Orphan closed; fix branch unmerged |

## The pattern across all five

Every one is the same failure mode wearing different clothes: **something was verified
somewhere other than where it is used.**

- **H1** — the check read the shelf manifest instead of the machine's install state
- **H2** — the gate scored a recording; the packaging that reached the machine was never checked
- **H3** — the test scored a document whose answer shipped inside the skill
- **H4** — five copies of the checklist, and no assertion that the one in use is the one approved
- **H5** — a manifest pointing at a non-plugin directory, and a catalogue served from a stale checkout

### A second pattern, which H4 and H5 share

**Work that was done correctly, then lost.** Phurin diagnosed and fixed the orphaned manifest and
packaged the `dd-checklist` skill properly on 2026-07-29. The branch never merged, so two days
later the same problems were being rediscovered from scratch. Separately, `instrument-applicability.md`
exists in two release snapshots but not in the shipping plugin.

Unmerged work is indistinguishable from work never done, and a file dropped in a refactor is
indistinguishable from a file that never existed. Both are cheap to detect — a merge-status sweep,
and a check that the plugin's `reference/` set matches the latest snapshot. Neither is currently run.

The gate is good at what it does. What it does is score recorded fixtures. Every incident so
far has lived in the gap between *"the artefact is correct"* and *"the thing running on a
lawyer's machine is correct"*.

That gap is not a defect in the gate — it is the boundary of the gate. The useful response is
to name the boundary and add cheap, deterministic checks on the other side of it, rather than
to imply the gate covers ground it does not.

## What to say to the client about this

The temptation is to hide it. The better story is that the firm's own process caught all four
before a lawyer relied on any of them, and each produced a permanent, mechanical check rather
than a promise to be careful. A governance system that has never found anything is not
evidence of quality; it is evidence of not having looked.
