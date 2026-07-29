# Harrow & Vale LLP — Hackathon Project

A working prototype for the Synthetic Signal Harrow & Vale scenario: a governed Claude skill for term-sheet review, backed by a deterministic evaluation harness, mock data-room fixtures, client deliverables, and a presentation-ready demo.

All client, deal, contact, passphrase, and data-room material in this repository is fictional hackathon content.

## Start here

| Path | Purpose |
|---|---|
| `.claude-plugin/marketplace.json` | HarrowVale Legal Skills — the firm's shelf of approved skills. |
| `plugins/term-sheet-review-plugin/` | Current installable Claude plugin used for the skill demonstration. |
| `plugins/cool-new-skill/` | Instrument-triage skill; the worked example for the pipeline demo. |
| `tools/skill-gate/` | The single approval gate (`gate.py`), the only sanctioned publisher (`publish.py`), and every skill's fixtures and scorers. |
| `releases/term-sheet-review/` | Frozen version history and approval evidence, including v1.0.0 and v1.1.0. |
| `tools/termsheet-harness/` | Term-sheet contract, reference baselines, source docs, DD mapper, and generated reports. |
| `assets/source/` | Canonical mock term sheets, DD checklist, and GreenGrid data-room documents. |
| `assets/legacy-raw-import/` | Original legacy import retained only for provenance. |
| `deliverables/` | Client proposal, case study, security briefing, rollout guidance, and next steps. |
| `demo/harrowvale-review-demo.html` | Standalone browser demo for the presentation. |
| `presentation/harrowvale-presentation.html` | Standalone presentation deck. |
| `docs/` | Discovery evidence, engagement briefs, governance notes, and the migration record. |
| `LEDGER.md` | Short handoff log for the team and its coding agents. |

## Run the evidence

The approval gate and the publisher live in `tools/skill-gate/`. From the repository root:

```powershell
python tools/skill-gate/gate.py --all
python tools/skill-gate/publish.py cool-new-skill --dry-run
python tools/skill-gate/publish.py cool-new-skill --candidate 1.0.0
```

The first scores every registered skill against its golden labels and applies the threshold and no-regression rules. The second shows exactly what a promotion would change, writing nothing. The third grades a known-bad recorded run and is refused — proving a failing skill cannot reach the shelf.

The term-sheet eval report and the DD mapper run from `tools/termsheet-harness/`. They report; the gate decides:

```powershell
python src/run_harness.py
python src/dd_mapper.py
```

The first evaluates all four instrument formats. The second produces the DD coverage/chase report.

`docs/governance/pipeline-rehearsal.md` walks the whole install-and-update loop end to end on one machine.

## Present the prototype

Open these files directly in a browser:

- `presentation/harrowvale-presentation.html`
- `demo/harrowvale-review-demo.html`

The final proposal is at `deliverables/proposal/Harrow-Vale-Proposal.pdf`; its editable Word version and JavaScript generator are stored beside it.

## Source-of-truth rules

- `plugins/term-sheet-review-plugin/` is the current installable product.
- `releases/term-sheet-review/` is immutable release history; existing version folders should not be edited in place.
- `tools/skill-gate/` owns scoring and promotion: `fixtures/<skill>/` holds every skill's golden labels and recorded runs, `scorers/` holds the graders.
- `tools/termsheet-harness/` owns the term-sheet contract, reference baselines, and generated reports.
- `assets/source/` contains the preferred captured source documents used as canonical inputs.
- Harness goldens and versioned skill references stay beside the code or release that consumes them.
- `assets/legacy-raw-import/` is retained for traceability but is not canonical.
- Client-facing outputs belong in `deliverables/`; internal working knowledge belongs in `docs/`.

See `assets/README.md`, `releases/README.md`, and `docs/README.md` for the component conventions.

## Team workflow

`master` is the shared integration branch. Work happens on short-lived `feature/`, `fix/`, `docs/`, or `refactor/` branches and enters `master` through pull requests. Organize files by project purpose rather than by contributor; after a pull request is merged, delete its branch.

Use the ledger for quick handoffs and GitHub issues for work that needs an owner, discussion, or acceptance criteria. See `CONTRIBUTING.md`.

The absolute clone location may differ between contributors. Keep active Git checkouts outside cloud-synchronised folders such as Google Drive, because generated metadata inside `.git` can corrupt Git refs.