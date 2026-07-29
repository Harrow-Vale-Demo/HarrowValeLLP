# Harrow & Vale — Legal Skills Pipeline (prototype)

A contract-first, eval-gated pipeline for building and distributing Claude skills
across a 10-lawyer boutique. Prototype for Synthetic Signal Hackathon 1.

**Read `PIPELINE.md` first** — it explains the one idea: a single governed gate
every skill must pass (contract → adversarial eval → versioned publish).

## What's here
| Path | What it is |
|---|---|
| `PIPELINE.md` | The approved-skills pipeline & governance model (the core deliverable). |
| `SKILL.md` | Skill #1: `term-sheet-review` — Priya's Exception Report. |
| `SKILL-dd-checklist.md` | Skill #2: `dd-checklist` — Tom's "Thursday dump" mapper. |
| `contract/term_sheet_review.schema.json` | The strict output contract (the "deterministic constraint"). |
| `reference/bvca_baseline.md` | The standard the skill maps against (never reinvented). |
| `reference/dd-checklist.md` | Priya's fixed DD checklist, used verbatim. |
| `golden/*.json` | Golden labels for all four term-sheet formats. |
| `runs/v1`, `runs/v2` | Recorded skill outputs (first pass vs eval-driven iteration). |
| `src/run_harness.py` | The eval harness + regression gate for this skill. |
| `CHANGELOG.md` | Per-skill, per-version history (only gate-passing versions). |
| `src/evaluator.py` | Precision/recall/F1 grader (penalises misses AND over-flagging). |
| `src/dd_mapper.py` | DD-checklist mapper demo. |
| `src/generator_adapter.py` | The seam where the live skill/model plugs in. |
| `reports/` | Generated eval + DD reports. |

## Run it
```bash
python3 src/run_harness.py      # eval gate across all 4 term-sheet formats
python3 src/dd_mapper.py        # DD checklist: satisfied / partial / missing + citations
```

Promotion is not run from here. The firm-wide gate and the only sanctioned
publisher live in `tools/skill-gate/`; this directory supplies the golden labels
and recorded runs that the gate reads for `term-sheet-review`:

```bash
python3 ../skill-gate/gate.py term-sheet-review
```

## Result (this prototype)
- Term-sheet skill: v1 overall reliability **0.496** → eval-driven v2 **1.000**,
  regression gate **PASS**. Consistent extraction across SAFE, priced round,
  convertible note, and terse seed formats.
- DD mapper: turns a document dump into "**2 satisfied, 1 partial, 25 missing**"
  with document + location citations and a chase list.

## Wiring the live model
`src/generator_adapter.py` documents two wirings (Claude Code headless or the
Messages API with a schema-constrained response). Fixtures in `runs/` are recorded
real outputs so CI can gate every prompt change deterministically.
