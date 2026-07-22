# Shared Ledger — Harrow & Vale Engagement (Hackathon 1)

> Shared coordination log between Emily and her Claude instances.
> **Convention:** append new entries at the top of the Log section. Format:
> `### [YYYY-MM-DD HH:MM] <author> — <one-line summary>` then details.
> Don't edit others' entries; add a new one instead.

---

## Engagement at a glance

- **Client:** Harrow & Vale LLP — boutique VC/M&A law firm, Clerkenwell, London (10 lawyers).
- **Sponsor:** Tom Harrow (Ops & Knowledge Lead). **Standard-setter:** Priya Vale (Managing Partner, reviews every closing).
- **Us:** Negative Zero associates (Emily) pitching a consulting engagement.
- **Target site:** https://harrowvale.syntheticsignal.io/ — sanctioned test target.
- **Data room:** https://harrowvale.syntheticsignal.io/data-room/ (sign in with NZ identity) — sample term sheets, DD checklist, mock data room.

## Deliverables — due Wed 29 July 2026

1. **Client proposal** — approach, scope, honest time/effort estimates, priced to client budget.
2. **Solution presentation** — demo the working solution running.
3. **Next steps** — how client takes it further / next engagement.
4. **Public case study** — how Claude solved it (public-facing, Anthropic-style).

## The build

- **Core:** a Claude Skill that reviews a term sheet — extracts key economic terms
  (valuation/cap, discount, liquidation preference, board/consent, pro-rata, etc.),
  checks against Priya's DD checklist, flags deviations/omissions in plain English.
  Must work across 3 formats: **SAFE, priced round, convertible loan note.**
  Build test-driven against 2–3 real examples first.
- **Stretch:** private versioned "approved skills" repo (install + update + approval
  process) + one-page data-residency / confidentiality memo (Claude for Enterprise/Teams).

## Open questions / TODO

- [x] Recon the public site + attempt data-room access.
- [x] Pull the 3 sample term sheets + DD checklist — DONE (Emily added them; organized into `assets/`).
- [ ] **Build the term-sheet review Skill** (test-driven against the 4 term sheets). ← next big task
- [ ] Build the DD-coverage report feature (GreenGrid = worked demo with full doc set).
- [ ] Confirm client budget (mentioned as given "on the call" — do we have it?).
- [ ] Ask the client what "review" means: what they check, in what order, ideal output.
- [ ] Stretch: private versioned skills repo (install/update/approval) + data-residency memo.
- [ ] Draft the 4 deliverables (proposal, demo, next steps, case study).

## Assets on disk

- `assets/dd-checklist/harrow-vale-dd-checklist.md` — ⭐ Priya's fixed 9-section / 30-item checklist.
- `assets/term-sheets/` — 4 sheets, deliberately different formats:
  SAFE (Nimbus), Series A priced (GreenGrid), convertible note (Anchorline), seed bullets (Solace).
- `assets/data-room-set/` — GreenGrid cap table, articles, lease, MSA (support a full DD demo).
- `assets/DATA-ROOM-NOTES.md` — detailed analysis of all of the above + design implications.
- `DataRoomInfo/` — original untouched files (1–8 + checklist).

## Discovery — client priorities (from Emily's call notes)

Priya (Managing Partner) — key concerns to design around:
- **Does NOT want Claude hallucinating new checklist items or skipping steps.** The DD
  checklist is a **fixed, standardised process** — the skill must follow it exactly, no
  invention, no omission. (→ implies: load the checklist verbatim, check item-by-item,
  never generate checklist items; make coverage auditable.)
- Firm is on/near **Chancery** (Lane), Clerkenwell.

What the client wants (their words):
- **Data security & governance**
- **Efficiency & standardisation**

Stretch driver: a **skills pipeline so all 10 lawyers use the same versions** (consistency
across the firm is the point — ties directly to "standardisation").

## Notes / assets

- `Scenario-1-Harrow-Vale-Guide.md` — the official engagement pack (source of truth).
- `notes` — contains a phone number (+447915900076); left untouched.
- Support: Hackathon Helper at lab.syntheticsignal.io/hackathon; Drew (drew.perry@negativezero.com).

---

## Log

### [2026-07-22] Claude (Emily's session) — Core skill BUILT + validated ✅
- Built `skills/term-sheet-review/` — the core deliverable.
  - `SKILL.md`: frontmatter (name/description/allowed-tools/argument-hint) + procedure.
    Encodes Priya's 3 rules: use checklist verbatim, never skip an item, never fabricate.
  - `reference/`: dd-checklist (ground truth), term-extraction (fields per instrument),
    standard-terms (deviation baseline), output-template (fixed structure).
  - `examples/`: worked reviews for ALL 4 formats (SAFE / Series A + DD-room / note / seed bullets).
- Validation: all 4 reviews pass structural checks (4 parts, signals, coverage tally,
  all-28-items-accounted-for). GreenGrid reconciliation math independently verified in python
  (price £1.50, 2,133,333 shares, 21.05% — all correct). Skill genuinely checks, doesn't fabricate.
- **Next:** stretch (versioned skills repo + data-residency memo) and the 4 written deliverables.
  Still need: client budget figure for pricing the proposal.

### [2026-07-22] Claude (Emily's session) — Recon done; data room needs sign-in
- Public site (harrowvale.syntheticsignal.io) live and matches the brief. Team: Priya Vale (MP),
  Tom Harrow (Ops/Knowledge), Marcus Ade (Sr Assoc M&A), Elena Cho (Assoc VC).
- Data room (/data-room/) returns **401 Unauthorized — credentials required**. Needs Emily's
  NZ sign-in; Claude cannot enter credentials. **Emily to sign in and pull the 3 sample term
  sheets + DD checklist**, or export them into this repo (e.g. under `assets/term-sheets/`).

### [2026-07-22] Claude (Emily's session) — Workspace initialized
- Read the engagement pack; confirmed with Emily this is a sanctioned discovery/proposal exercise (not adversarial).
- `git init` done. Created this LEDGER.md as the shared coordination file.
- Next up: recon the public site and try the data room.
