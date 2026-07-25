# Proposal: AI-Assisted Term Sheet Review
## Negative Zero for Harrow & Vale LLP

**Date:** July 2026
**Prepared by:** Emily Donovan, Negative Zero
**For:** Tom Harrow, Ops & Knowledge Lead

---

## Executive Summary

Harrow & Vale's lawyers each use Claude AI individually, with no shared skills, no governance, and no consistency. This proposal delivers:

1. **A working term-sheet review skill** that extracts key economic terms and maps documents against Priya's DD checklist — tested across SAFEs, priced rounds, and convertible notes
2. **A partner-ready data security briefing** addressing UK GDPR, SRA compliance, and Anthropic's data handling
3. **An approved skills pipeline** with versioning, approval process, and installation instructions for all 10 lawyers

The solution is built, tested, and ready to demonstrate.

---

## The Problem

| Current State | Impact |
|---------------|--------|
| 10 lawyers with 10 different prompts | Inconsistent quality, duplicated effort |
| No vetting or approval process | Risk of untested tools reaching client work |
| No shared knowledge | Wheel reinvented every time |
| No answer on data security | Priya can't approve without it |
| Manual term-sheet review | Hours spent on extraction that could be automated |

---

## The Solution

### Core Deliverable: Term-Sheet Review Skill

A Claude skill that:

- **Classifies** the instrument (SAFE / priced round / convertible note) from signals
- **Extracts** 11 key economic terms (valuation, liquidation preference, vesting, board, fees, etc.)
- **Flags** deviations from market standard with severity (🔴 Review / 🟡 Note / ⚪ Omission)
- **Maps** documents against Priya's fixed 28-item DD checklist
- **Reconciles** figures across documents (term sheet ↔ cap table ↔ articles)

**Design principles (per Priya's requirements):**
1. Use the fixed checklist verbatim — never invent categories
2. Never skip a step — every item gets an explicit status
3. Never fabricate — absent terms are "Not stated", not guessed

**Tested against:** All 4 sample term sheets (SAFE, Series A, convertible note, seed) with consistent output structure.

### Stretch Deliverables

| Deliverable | Status |
|-------------|--------|
| **Data Security Briefing** | Complete — 1-page partner-ready memo covering UK GDPR, SRA, Anthropic policies |
| **Approved Skills Pipeline** | Complete — versioning process, approval workflow, GitHub structure |
| **Lawyer Installation Guide** | Complete — step-by-step for non-technical users |
| **Professional Memo Template** | Complete — HTML template styled as H&V internal memo |

---

## Scope of Work

### What's Included

| Item | Description |
|------|-------------|
| Term-sheet review skill | Fully built, tested, documented |
| DD-room coverage feature | `--dd-room` flag for full checklist mapping |
| 4 worked examples | One per instrument type, for training/reference |
| Reference materials | Extraction fields, standard terms baseline, output template |
| Data security briefing | Partner-ready memo on compliance |
| Skills pipeline documentation | Approval process, versioning, changelog |
| Installation guide | For all 10 lawyers |
| Memo format template | HTML template for professional output |
| Live demonstration | Walkthrough with Tom + Priya |

### What's Not Included

- Ongoing maintenance (separate support agreement)
- Custom skills beyond term-sheet review (future engagement)
- SharePoint/365 integration (requires separate technical scoping)
- Training sessions beyond initial demo (available as add-on)

---

## Effort & Timeline

| Phase | Effort | Status |
|-------|--------|--------|
| Discovery & requirements | 4 hours | Complete |
| Core skill development | 8 hours | Complete |
| Testing across 4 formats | 4 hours | Complete |
| Stretch deliverables | 6 hours | Complete |
| Documentation | 4 hours | Complete |
| Demo preparation | 2 hours | Pending |
| **Total** | **28 hours** | |

**Delivery:** Ready for demo Wednesday 29 July 2026

---

## Investment

Based on the agreed budget range (£2,000–£5,000) and 28 hours of work:

| Option | Includes | Price |
|--------|----------|-------|
| **Core** | Term-sheet skill + demo | £2,500 |
| **Full** | Core + all stretch deliverables | £4,000 |
| **Full + Support** | Full + 3 months support (bug fixes, updates) | £4,800 |

**Recommendation:** Full package (£4,000) — the data security briefing alone is required for partner sign-off, and the skills pipeline eliminates the 10-different-prompts problem.

---

## Why This Approach

### What We Built vs. What We Didn't

| We Built | We Didn't Build |
|----------|-----------------|
| A skill that follows Priya's checklist exactly | A "smart" system that invents its own checks |
| Extraction with source references | Summaries that lose traceability |
| Flags that describe, not adjudicate | AI that gives legal opinions |
| Consistent output every time | Variable formats depending on input |

This is deliberately **conservative** — the skill does the grunt work and hands off to the lawyer for judgement. That's what makes it trustworthy enough for Priya to approve.

### Technical Choices

- **Claude Code skills** — portable, versionable, no infrastructure required
- **Markdown-based** — works with any document the firm already has
- **GitHub for skills repo** — firm already has light GitHub use; builds on existing tooling
- **No data leaves the firm** — with Claude Enterprise, no training on client data

---

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Lawyers don't adopt | Simple installation, clear guide, demo training |
| Skill produces errors | Human verification required; skill never used without lawyer review |
| Anthropic policy changes | Briefing based on current policies; recommend annual review |
| Edge case documents | Skill handles common formats; unusual cases flagged for manual review |

---

## Next Steps

1. **Demo** — We walk through the skill live with Tom + Priya (29 July)
2. **Sign-off** — Priya reviews data security briefing
3. **Deployment** — Push skill to firm's private repo
4. **Rollout** — Lawyers install using the guide; support available for 3 months

---

## Appendices

Available on request:
- A: Worked example outputs (all 4 formats)
- B: Full data security briefing
- C: Skills pipeline process document
- D: Lawyer installation guide

---

*Negative Zero · Consulting for AI-native workflows*
*Contact: emily.donovan@negativezero.com*
