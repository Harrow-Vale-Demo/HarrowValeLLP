# Term-Sheet Prototype — Reference Material and Reports

The original term-sheet-review prototype. It is **not** the gate: the firm-wide
approval gate and the only sanctioned publisher live in
[`tools/skill-gate/`](../skill-gate/). Read
[`PIPELINE.md`](PIPELINE.md) for the governance model.

What remains here is the term-sheet skill's *source and reference* material, plus
two demos that are not part of the publish path. Its golden labels, recorded runs
and scorer moved to the gate so that every skill's fixtures sit in one place —
see [`tools/skill-gate/fixtures/term-sheet-review/`](../skill-gate/fixtures/term-sheet-review/).

## What's here

| Path | What it is |
|---|---|
| `PIPELINE.md` | The approved-skills pipeline & governance model. |
| `SKILL.md` | The original `term-sheet-review` draft. The shipped skill is `plugins/term-sheet-review-plugin/`. |
| `SKILL-dd-checklist.md` | The original `dd-checklist` draft. Never packaged as a plugin. |
| `contract/term_sheet_review.schema.json` | The strict output contract for term-sheet review. |
| `reference/bvca_baseline.md` | The standard the skill maps against (never reinvented). |
| `reference/dd-checklist.md` | Priya's fixed DD checklist, used verbatim by `dd_mapper.py`. |
| `data/*.md` | Copies of the four sample term sheets, kept beside the contract. |
| `src/run_harness.py` | Formats the term-sheet eval report from the gate's fixtures. |
| `src/dd_mapper.py` | DD-checklist mapper demo. |
| `src/consistency_check.py` | Term sheet vs Articles drift check (roadmap demo). |
| `reports/` | Generated eval + DD reports. |
| `CHANGELOG.md` | Early per-version history. Approved releases now live in `releases/`. |

## Moved to the gate

| Was | Now |
|---|---|
| `golden/*.json` | `tools/skill-gate/fixtures/term-sheet-review/golden/` |
| `runs/v1`, `runs/v2` | `tools/skill-gate/fixtures/term-sheet-review/runs/` |
| `src/evaluator.py` | `tools/skill-gate/scorers/termsheet.py` |
| `src/generator_adapter.py` | `tools/skill-gate/generator_adapter.py` |

## Run it

```bash
python3 src/run_harness.py      # eval report across all 4 term-sheet formats
python3 src/dd_mapper.py        # DD checklist: satisfied / partial / missing + citations
python3 src/consistency_check.py
```

`run_harness.py` reads the gate's fixtures and writes `reports/`. It reports; it
does not decide. Scoring and promotion are the gate's:

```bash
python3 ../skill-gate/gate.py term-sheet-review
python3 ../skill-gate/publish.py term-sheet-review
```

## Result (this prototype)

- Term-sheet skill: v1 overall reliability **0.496** → eval-driven v2 **1.000**,
  regression gate **PASS**. Consistent extraction across SAFE, priced round,
  convertible note, and terse seed formats.
- DD mapper: turns a document dump into "**2 satisfied, 1 partial, 25 missing**"
  with document + location citations and a chase list.

## Wiring the live model

[`../skill-gate/generator_adapter.py`](../skill-gate/generator_adapter.py)
documents two wirings — Claude Code headless, or the Messages API with a
schema-constrained response. The fixtures the gate reads are recorded outputs, so
CI can gate every prompt change deterministically and for free.
