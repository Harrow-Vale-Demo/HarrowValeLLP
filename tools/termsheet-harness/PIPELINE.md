# Harrow & Vale — The Approved-Skills Pipeline
### One governed home where every skill a lawyer builds is contract-bound and deterministically eval-gated before it goes firm-wide.

Today ten lawyers each build their own prompts and skills in isolation: nothing
is shared, approved, or kept current, and nobody can point to *why* a given skill
is safe to trust on a live deal. This pipeline fixes that. It is not ten skills —
it is **one approval gate** that any skill must pass.

## The gate (every skill, no exceptions)
```
   Author a skill                Prove it                    Ship it
  ┌───────────────┐   contract  ┌──────────────┐  version  ┌──────────────────┐
  │  SKILL.md +   │────────────▶│  EVAL HARNESS │──────────▶│ private repo /   │
  │  JSON contract│   golden    │  (adversarial │   gate    │ marketplace      │
  │  (schema)     │   dataset   │   grader)     │  PASS     │ 10 lawyers install│
  └───────────────┘             └──────────────┘           └──────────────────┘
        every field typed         precision/recall            semver + changelog
        no free-form for          vs golden, regression        install path,
        critical extraction       gate blocks publish          auto-update to v2
```

1. **Contract first.** No skill is "done" until it declares a strict JSON Schema
   output (see `contract/`). Critical extraction is typed, never free-form prose.
   This is what makes it *deterministically constrained* — the output shape is
   fixed and machine-checkable.
2. **Prove it — adversarial eval.** Each skill ships a golden dataset of known-good
   and known-bad examples. The evaluator (a separate Claude instance / grader)
   scores precision & recall and **fails the build on regression**
   (`src/run_harness.py`, threshold 0.90). A skill that hasn't passed the gate
   cannot be published.
3. **Ship it — versioned distribution via a private marketplace.** Passing skills
   are published to the firm's private GitHub repo, catalogued in a
   `.claude-plugin/marketplace.json` (the firm's single shelf of approved skills).
   Each skill is a plugin bundling its `SKILL.md`, JSON contract, reference
   baseline/checklist and golden dataset, carrying a semantic version + changelog.
   Lawyers add the marketplace once (`/plugin marketplace add f7-rage-gremlin/HarrowValeLLP`),
   install with `/plugin install <skill>@harrowvale-legal-skills`, and pull updates with
   `/plugin marketplace update harrowvale-legal-skills`. The repository's own
   `.claude/settings.json` declares the marketplace and the enabled skills, so a
   colleague who trusts the project folder is prompted to install it rather than
   being told to. A live matter can pin a known-good version so a review never
   shifts mid-deal.

   This whole promotion is one command (`tools/skill-gate/publish.py`): it runs the
   gate, and only on PASS does it write the graded version into `plugin.json`, the
   marketplace entry, the skill text, the changelog, and a stored gate report. The
   version it publishes *is* the version the gate graded — there is no separate bump
   step that can be got wrong. A failing gate writes nothing at all.

## Governance (who vets, how v2 rolls out)
- **Author:** any lawyer/associate. Writes SKILL.md + contract + golden cases.
- **Approver:** Tom (ops/security) signs the pipeline run; Priya owns the
  domain baselines (e.g. the BVCA baseline, the DD checklist) that skills must
  respect verbatim.
- **Promotion:** a change to a skill re-runs the harness in CI. Green + no
  regression → version bumped, published, auto-served to all installs. Red →
  blocked, stays at current version.
- **Auditability:** every approved version has a stored eval report
  (`reports/eval_report.json`) — the firm can always answer "why do we trust
  this skill?" with numbers.

## Why this is the actual deliverable
The term-sheet-review and dd-checklist skills in this repo are the **first two
skills through the gate** — the proof that the pipeline produces something a
lawyer will reach for mid-deal. The reusable asset Harrow & Vale keeps is the
gate itself.
