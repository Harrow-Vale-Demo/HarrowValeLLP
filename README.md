# Harrow & Vale LLP — Hackathon Project

A working prototype for the Synthetic Signal Harrow & Vale scenario: a governed Claude skill for term-sheet review, backed by a deterministic evaluation harness, mock data-room fixtures, client deliverables, and a presentation-ready demo.

All client, deal, contact, passphrase, and data-room material in this repository is fictional hackathon content.

## Start here

| Path | Purpose |
|---|---|
| `demo/harrowvale-review-demo.html` | Standalone browser demo for the presentation. |
| `presentation/harrowvale-presentation.html` | Standalone presentation deck. |
| `deliverables/` | Client proposal, case study, security briefing, rollout guidance, and next steps. |
| `plugins/term-sheet-review-plugin/` | Installable Claude plugin used for the skill demonstration. |
| `harrow-vale-skills/` | Versioned skill releases and approval history, including v1.1.0. |
| `tools/termsheet-harness/` | Executable contract, golden fixtures, regression evaluator, DD mapper, and publish gate. |
| `assets/` | Canonical mock term sheets, DD checklist, and GreenGrid data-room documents. |
| `docs/discovery/` | Engagement notes and the hackathon discovery log. |
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

## Source priority

The Markdown files under `assets/term-sheets/` and `assets/dd-checklist/` are the canonical mock source set for evaluation. They were captured from the sanctioned mock data room and take precedence over older normalized copies when wording differs. `DataRoomInfo/` is retained as a legacy raw import for traceability.

See `assets/README.md` for the exact source/fixture convention.

## Team workflow

`master` is the shared integration branch. Work happens on short-lived `feature/`, `fix/`, or `agent/` branches and enters `master` through pull requests. Organize files by project purpose rather than by contributor; after a pull request is merged, delete its branch.

Use the ledger for quick handoffs and GitHub issues for work that needs an owner, discussion, or acceptance criteria. See `CONTRIBUTING.md`.