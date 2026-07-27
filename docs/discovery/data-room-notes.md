# Data Room — Contents & Analysis Notes

*Source: Harrow & Vale data room, added by Emily. Originals in `assets/legacy-raw-import/`, working
copies in `assets/source/`. All documents are synthetic/mock (fictional companies).*

---

## ⭐ The Due Diligence Checklist (the anchor of the whole build)

**File:** [`assets/source/dd-checklist/harrow-vale-dd-checklist.md`](../../assets/source/dd-checklist/harrow-vale-dd-checklist.md)

Priya Vale's **fixed, standardised** DD checklist — applied to *every* funding-round/M&A
matter **regardless of instrument type**. The doc itself states the constraint we heard on
the call, verbatim:

> "Any skill built to speed up DD review must check documents against **this exact list, not
> invent its own categories.**"

**9 sections, 30 checklist items:**

| # | Section | Items |
|---|---|---|
| 1 | Corporate Structure | Cert of incorporation; Articles (as amended); Register of members/cap table; Register of directors & secretaries; Group structure chart (if applicable) |
| 2 | Share Capital & Instruments | Fully-diluted cap table; all SAFEs/convertibles/option grants; option scheme rules & grant letters; side letters affecting share rights |
| 3 | Material Contracts | Customer contracts >£50k/yr; supplier agreements w/ exclusivity or min-spend; leases; loan agreements & debt instruments |
| 4 | Intellectual Property | IP assignments from founders & contractors; registered TM/patents; open-source licence usage |
| 5 | Employment | Employment agreements (all staff); contractor/consultancy agreements; tribunal claims/disputes |
| 6 | Litigation & Compliance | Outstanding/threatened litigation; regulatory correspondence/investigations; GDPR/data-protection summary (incl. DPIA) |
| 7 | Financials & Tax | Last 2 yrs accounts (audited or mgmt); tax filings & HMRC correspondence; R&D tax credit claims |
| 8 | Insurance | D&O liability insurance; professional indemnity (if applicable) |
| 9 | Related-Party Transactions | Any company↔director/major-shareholder transactions |

**Design implication for the skill:** load this checklist as ground truth, walk it
item-by-item, and for each item report one of `PRESENT / MISSING / N/A` with the supporting
document cited. Never generate a checklist item that isn't here; never silently skip one.
This is how we satisfy Priya's "no hallucination, no skipped steps" requirement — and how we
make coverage **auditable** (all 30 items accounted for, every time).

---

## The three term-sheet formats (core deliverable test set)

The brief demands the skill work across **3 deliberately different formats**. We actually
have **4** term sheets — even better for test-driven development (2–3 to build against, the
rest to validate generalisation).

### 1. SAFE — Nimbus Robotics Ltd
**File:** [`assets/source/term-sheets/safe-nimbus-robotics.md`](../../assets/source/term-sheets/safe-nimbus-robotics.md) · Investor: Cordwainer Angels · 14 Mar 2026
- Purchase amount £750k; **valuation cap £6m post-money**; **discount 20%**; no interest, no maturity (it's a SAFE).
- **MFN clause = yes** (unusual/notable — worth flagging). Pro-rata = yes.
- Converts on Equity Financing ≥ £1m, at lower of cap price or discount price.
- Format: prose + a terms table.

### 2. Priced round (Series A) — GreenGrid Analytics Ltd
**File:** [`assets/source/term-sheets/series-a-greengrid-analytics.md`](../../assets/source/term-sheets/series-a-greengrid-analytics.md) · Lead: Northbridge Ventures · 2 May 2026
- £3.2m at **£12m pre / £15.2m post**; £1.50/share; 2,133,333 new shares; investor **21.05%**.
- **1x non-participating** liquidation preference; broad-based weighted-average anti-dilution.
- Board: 3 seats (2 founders / 1 Series A). Protective provisions (4 consent items).
- Info rights for holders ≥2%. **45-day exclusivity.**
- Format: numbered clauses + terms table. **Figures reconcile with the GreenGrid cap table (file 5).**

### 3. Convertible loan note — Anchorline Biotech Ltd
**File:** [`assets/source/term-sheets/convertible-note-anchorline-biotech.md`](../../assets/source/term-sheets/convertible-note-anchorline-biotech.md) · Noteholder: Fenwick Life Sciences · 19 Jun 2026
- £500k principal; **8% interest** (compounding annually, paid on conversion/redemption/maturity).
- **24-month maturity**; **15% conversion discount**; **£8m pre-money cap**.
- Qualifying financing ≥ £2m. Change-of-control: repay + **1.5x premium** OR convert at cap.
- **Unsecured** (ranks behind secured creditors). Events of default listed.
- Format: bolded label + prose per term. It IS a debt instrument (interest + maturity) — contrast with the SAFE.

### 4. Seed round (terse bullets) — Solace Data Ltd
**File:** [`assets/source/term-sheets/seed-solace-data.md`](../../assets/source/term-sheets/seed-solace-data.md) · Investor: Ridgeline Seed Partners · 3 Jul 2026
- £450k at £4m pre / £4.45m post; investor **10.11%**; 1x non-participating.
- **Observer seat only** (no board seat at seed). Pro-rata = yes; broad-based WA anti-dilution.
- 30-day exclusivity; CPs incl. clean disclosure letter, 14-day IP diligence, no MAC.
- Format: **condensed bullet list** (deliberately different "house style"). Note: "confirm no side letters."

**Format-variety takeaway:** table+prose (SAFE), numbered clauses (Series A), labelled prose
(note), and terse bullets (seed). If the skill handles all four → it's genuinely robust. Good
test matrix.

---

## Mock data-room document set (supports the DD checklist)

These map to specific checklist items — useful for a **worked DD demo** on GreenGrid (the one
company with a full set: term sheet + cap table + articles + contracts).

| File | Maps to checklist |
|---|---|
| [`assets/source/data-room/cap-table-greengrid.md`](../../assets/source/data-room/cap-table-greengrid.md) | §1 Register of members / §2 fully-diluted cap table. Founders 2×39.47%, Northbridge 21.05%. **No option pool** created this round (notable). Figures reconcile with the Series A term sheet. |
| [`assets/source/data-room/articles-greengrid.md`](../../assets/source/data-room/articles-greengrid.md) | §1 Articles (as amended). Company no. 14829371. Liquidation pref (Art 7), board (Art 8), protective provisions (Art 9) — **consistent with the term sheet**. |
| [`assets/source/data-room/lease-greengrid.md`](../../assets/source/data-room/lease-greengrid.md) | §3 Material Contracts → leases. Reading office, 5yr term, break at m36, £68k/yr. |
| [`assets/source/data-room/msa-greengrid-halloway.md`](../../assets/source/data-room/msa-greengrid-halloway.md) | §3 Material Contracts → customer contracts >£50k. Halloway Utilities, £182k ACV. UK data residency + DPA (relevant to §6 GDPR). |

**GreenGrid coverage gaps (illustrative for a DD demo):** present = cap table, articles, 2
material contracts. Missing vs. the 30-item checklist = cert of incorporation, register of
directors, option scheme docs, IP assignments, employment agreements, litigation/regulatory,
accounts/tax, insurance, related-party. → A DD-coverage report on GreenGrid would flag ~24
items as MISSING / not-yet-provided — a compelling, honest demo of the skill's value.

---

## How this shapes the proposal

- **Core skill** = term-sheet reviewer. Extract economic terms → check against the 30-item
  checklist → plain-English review flagging deviations, unusual clauses (e.g. Nimbus MFN,
  Anchorline 1.5x CoC premium), and omissions. Test-driven against these 4 sheets.
- **Deviation-flagging** needs a notion of "standard" — from the corpus, "standard" ≈ 1x
  non-participating pref, broad-based WA anti-dilution, board proportional to ownership,
  pro-rata yes. Anything off that baseline gets flagged for a lawyer's eye (not auto-judged).
- **Reconciliation checks** (Series A ↔ cap table ↔ articles all agree) are a strong,
  demonstrable feature and directly serve "due-diligence discipline."
- **Governance/anti-hallucination** is the headline: checklist-as-ground-truth, item-by-item
  coverage, cite-the-source, PRESENT/MISSING/N/A. Directly answers Priya + the "data security
  & governance" want.
