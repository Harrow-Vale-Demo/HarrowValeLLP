# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a hackathon project for Harrow & Vale LLP, a boutique VC/M&A law firm. The core deliverable is a Claude Skill that reviews venture term sheets against the firm's fixed due-diligence checklist.

## Repository Structure

- README.md - Project map, run commands, source priority, and presentation entrypoints
- demo/ - Standalone interactive review demo
- presentation/ - Standalone browser presentation
- deliverables/ - Client-facing written outputs and proposal source
- 	ools/termsheet-harness/ - Executable contract/golden evaluation and publish gate
- `plugins/term-sheet-review-plugin/` - The packaged skill as a shareable plugin
  - `skills/term-sheet-review/SKILL.md` - Main skill definition and procedure
  - `skills/term-sheet-review/reference/` - Reference materials (checklist, standard terms, templates)
  - `skills/term-sheet-review/examples/` - Worked review examples for all 4 term sheet formats
- `assets/` - Sample documents for testing
  - `term-sheets/` - 4 sample term sheets (SAFE, Series A, convertible note, seed)
  - `data-room-set/` - GreenGrid supporting documents (cap table, articles, lease, MSA)
  - `dd-checklist/` - Priya's fixed 28-item due-diligence checklist
- `LEDGER.md` - Shared coordination log between sessions
- `.claude-plugin/marketplace.json` - Plugin marketplace manifest

## Skill Usage

```
/term-sheet-review <path-to-term-sheet>
/term-sheet-review <path-to-term-sheet> --dd-room <path-to-folder>
```

## Key Design Constraints (Priya's Rules)

These are non-negotiable requirements from the Managing Partner:

1. **Use the fixed checklist verbatim** - The DD checklist in `reference/dd-checklist.md` is the ground truth. Never invent, rename, or merge checklist items.
2. **Never skip a step** - Every one of the 28 checklist items must appear with an explicit status (PRESENT/MISSING/N/A).
3. **Never fabricate** - Only report values that appear in documents. Mark absent terms as "Not stated", not guessed.

## Instrument Types

The skill classifies term sheets into three types based on signals:
- **SAFE** - "future equity", no interest, no maturity, converts at cap/discount
- **Convertible loan note** - has interest rate AND maturity/redemption date
- **Priced round** - price per share, stated pre/post-money valuation

## Coordination

Use `LEDGER.md` for session handoffs. Append new entries at the top of the Log section with format: `### [YYYY-MM-DD HH:MM] <author> — <one-line summary>`
