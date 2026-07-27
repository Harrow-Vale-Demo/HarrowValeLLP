# Harrow & Vale LLP — Hackathon Project

A working prototype for the Synthetic Signal Harrow & Vale scenario: a governed Claude skill for term-sheet review, backed by a deterministic evaluation harness, mock data-room fixtures, client deliverables, and a presentation-ready demo.

All client, deal, contact, passphrase, and data-room material in this repository is fictional hackathon content.

## Start here

| Path | Purpose |
|---|---|
| `plugins/term-sheet-review-plugin/` | Current installable Claude plugin used for the skill demonstration. |
| `releases/term-sheet-review/` | Frozen version history and approval evidence, including v1.0.0 and v1.1.0. |
| `tools/termsheet-harness/` | Executable contract, golden fixtures, regression evaluator, DD mapper, and publish gate. |
| `assets/source/` | Canonical mock term sheets, DD checklist, and GreenGrid data-room documents. |
| `assets/legacy-raw-import/` | Original legacy import retained only for provenance. |
| `deliverables/` | Client proposal, case study, security briefing, rollout guidance, and next steps. |
| `demo/harrowvale-review-demo.html` | Standalone browser demo for the presentation. |
| `presentation/harrowvale-presentation.html` | Standalone presentation deck. |
| `docs/` | Discovery evidence, engagement briefs, governance notes, and the migration record. |
| `LEDGER.md` | Short handoff log for the team and its coding agents. |

## Run the evidence

From `tools/termsheet-harness/`:

```powershell
python src/run_harness.py
python src/dd_mapper.py
python src/publish.py term-sheet-review --simulate-regression
```

The first command evaluates all four instrument formats. The second produces the DD coverage/chase report. The third demonstrates that a regressing skill is blocked from promotion.

## Present the prototype

Open these files directly in a browser:

- `presentation/harrowvale-presentation.html`
- `demo/harrowvale-review-demo.html`

The final proposal is at `deliverables/proposal/Harrow-Vale-Proposal.pdf`; its editable Word version and JavaScript generator are stored beside it.

## Source-of-truth rules

- `plugins/term-sheet-review-plugin/` is the current installable product.
- `releases/term-sheet-review/` is immutable release history; existing version folders should not be edited in place.
- `tools/termsheet-harness/` owns executable evaluation and promotion machinery.
- `assets/source/` contains the preferred captured source documents used as canonical inputs.
- Harness goldens and versioned skill references stay beside the code or release that consumes them.
- `assets/legacy-raw-import/` is retained for traceability but is not canonical.
- Client-facing outputs belong in `deliverables/`; internal working knowledge belongs in `docs/`.

See `assets/README.md`, `releases/README.md`, and `docs/README.md` for the component conventions.

## Team workflow

`master` is the shared integration branch. Work happens on short-lived `feature/`, `fix/`, `docs/`, or `refactor/` branches and enters `master` through pull requests. Organize files by project purpose rather than by contributor; after a pull request is merged, delete its branch.

Use the ledger for quick handoffs and GitHub issues for work that needs an owner, discussion, or acceptance criteria. See `CONTRIBUTING.md`.

The absolute clone location may differ between contributors. Keep active Git checkouts outside cloud-synchronised folders such as Google Drive, because generated metadata inside `.git` can corrupt Git refs.