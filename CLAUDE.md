# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a hackathon project for Harrow & Vale LLP, a boutique VC/M&A law firm. The core deliverable is a Claude Skill that reviews venture term sheets against the firm's fixed due-diligence checklist.

## Repository Structure

- `plugins/term-sheet-review-plugin/` - Current packaged and installable skill
  - `skills/term-sheet-review/SKILL.md` - Main skill definition and procedure
  - `skills/term-sheet-review/reference/` - Checklist and standard-term references
  - `skills/term-sheet-review/examples/` - Worked examples for all four formats
- `plugins/cool-new-skill/` - Instrument-triage skill; worked example for the pipeline demo
- `releases/term-sheet-review/` - Frozen semantic-version snapshots and approval evidence
- `tools/skill-gate/` - The firm-wide approval gate (`gate.py`), every skill's fixtures under
  `fixtures/<skill>/` and graders under `scorers/`, the only sanctioned publisher
  (`publish.py`), and the published-version consistency check (`check_published.py`)
- `tools/termsheet-harness/` - Term-sheet contract, reference baselines, DD mapper, generated reports
- `assets/source/` - Canonical mock source documents
  - `term-sheets/` - SAFE, Series A, convertible note, and seed samples
  - `data-room/` - GreenGrid supporting documents
  - `dd-checklist/` - Priya's fixed due-diligence checklist
- `assets/legacy-raw-import/` - Legacy import retained only for provenance
- `deliverables/` - Client-facing written outputs and proposal source
- `demo/` - Standalone interactive review demo
- `presentation/` - Standalone browser presentation
- `docs/` - Discovery, engagement, and governance material
- `LEDGER.md` - Shared coordination log
- `.claude-plugin/marketplace.json` - Root plugin marketplace manifest

Do not edit an existing release snapshot in place. Change the active plugin, validate it, and create a new release version through the approval process in `releases/CONTRIBUTING.md`.

## Skill Usage

*Verified against Claude Code 2.1.140, 2026-07-30.*

Plugin skills are namespaced by plugin name. Once installed from the
marketplace, either invocation route works and both hit the same `SKILL.md`:

**As a namespaced slash command** — deterministic, useful in a demo:

```
/term-sheet-review:term-sheet-review <path-to-term-sheet>
/term-sheet-review:term-sheet-review <path-to-term-sheet> --dd-room <path-to-folder>
/cool-new-skill:cool-new-skill <path-to-document>
```

**In plain language** — Claude reads each skill's `description` frontmatter and
picks the right skill from what you ask for:

```
Review assets/source/term-sheets/safe-nimbus-robotics.md against our DD checklist
Review the GreenGrid Series A, with the data room at assets/source/data-room/
Triage assets/source/dd-checklist/harrow-vale-dd-checklist.md
```

To confirm a plugin is installed, open the `/plugin` panel and read which section
it sits in — **Installed** means on this machine, **Discover** means on the shelf
but not installed. Do not verify by asking an agent to "list installed plugins":
reading `.claude-plugin/marketplace.json` returns the *shelf*, which looks
identical on a machine with nothing installed.

If a skill is installed but does not trigger, the running session is still holding
the plugins it launched with. Run `/reload-plugins`, or restart.

## Key Design Constraints (Priya's Rules)

These are non-negotiable requirements from the Managing Partner:

1. **Use the fixed checklist verbatim** - The checklist is the ground truth. Never invent, rename, or merge checklist items.
2. **Never skip a step** - Every checklist item must appear with an explicit status (PRESENT/MISSING/N/A).
3. **Never fabricate** - Only report values that appear in documents. Mark absent terms as "Not stated", not guessed.

## Instrument Types

The skill classifies term sheets from document content:

- **SAFE** - "future equity", no interest, no maturity, converts at cap/discount
- **Convertible loan note** - interest rate and maturity/redemption date
- **Priced round** - price per share and stated pre/post-money valuation

## Coordination

Use `LEDGER.md` for session handoffs. Add new entries at the top of the Log section using: `### [YYYY-MM-DD HH:MM] <author> — <one-line summary>`.