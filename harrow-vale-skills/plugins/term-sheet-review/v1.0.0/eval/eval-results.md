<!-- Test-driven validation run: the SKILL.md procedure applied by hand against all 4 sample term sheets, before treating the skill as "generalised." Kept as a regression reference — any future SKILL.md wording change should be re-run against these 4 and produce equivalent flags. -->

# Eval Run — term-sheet-review skill vs. 4 sample term sheets

## Rubric

| Check | GreenGrid (priced) | Nimbus (SAFE) | Anchorline (conv. note) | Solace (bullet seed) |
|---|---|---|---|---|
| Output shape identical (6 sections, same order) | ✅ | ✅ | ✅ | ✅ |
| Instrument type correctly identified from content | ✅ | ✅ | ✅ | ✅ |
| SAFE-only fields (interest/maturity) marked N/A not "omitted" | n/a | ✅ | n/a | n/a |
| Known planted deviation caught | n/a (control — vanilla round) | ✅ MFN clause | ✅ 1.5x change-of-control premium | ✅ side-letter confirmation note |
| Reconciliation check run where data room supplied | ✅ pass | n/a (no data room) | n/a (no data room) | n/a (no data room) |
| Terse/bullet source formatting didn't leak into output structure | n/a | n/a | n/a | ✅ |

Result: **4/4 pass.** No SKILL.md wording changes needed after this round; kept as the regression baseline.

---

## Run 1 — GreenGrid Analytics Ltd (Series A, priced round + data room)

**Instrument:** Series A Preferred Share Financing — GreenGrid Analytics Ltd — Lead investor Northbridge Ventures LLP — 2 May 2026.

**Key Terms**

| Term | Detail |
|---|---|
| Instrument type | Priced equity round (Series A Preferred) |
| Amount raised | £3,200,000 |
| Pre-/Post-money valuation | £12,000,000 / £15,200,000 |
| Discount rate | N/A |
| Price per share | £1.50 |
| Interest rate | N/A |
| Maturity date | N/A |
| Liquidation preference | 1x non-participating |
| Anti-dilution | Broad-based weighted average |
| Board composition | 3 directors: 2 founder-appointed, 1 Series A-appointed |
| Protective provisions | Standard 4-item consent list (adverse Articles amendment, sale of company, senior/pari passu issuance, debt >£250k) |
| Information rights | ≥2% FD holders get quarterly accounts + annual budget |
| Pro-rata rights | Not stated |
| Conditions precedent | DD completion, clean disclosure letter, Investment Agreement, Amended Articles, Shareholders' Agreement |
| Exclusivity | 45 days |
| Governing law | England and Wales |

**Checklist Review** (data room supplied: cap table, Articles extract, customer MSA, office lease)
- *1. Corporate Structure:* Articles of Association — Present (extract reviewed, Art. 7/8/9 match term sheet). Cap table/register of members — Present, reconciles (see below). Certificate of incorporation, register of directors, group structure chart — **Omitted**, not found in reviewed set.
- *2. Share Capital & Instruments:* Full cap table — Present. Outstanding SAFEs/convertibles/options — **Omitted**, not confirmed either way (cap table notes "no option pool created" but doesn't confirm absence of other instruments). Option scheme rules — **Omitted**. Side letters — **Omitted**, unconfirmed.
- *3. Material Contracts:* Customer contract >£50k — Present (Halloway Utilities MSA, £182,000 ACV). Lease — Present (Riverside Business Park). Supplier/vendor exclusivity agreements, loan agreements — **Omitted**, not found.
- *4–9 (IP, Employment, Litigation/Compliance, Financials/Tax, Insurance, Related-Party):* **Omitted** — not part of the reviewed document set; note explicitly that "omitted" here means not supplied, not confirmed non-existent.

**Unusual Clauses:** None identified — all terms sit within the market-standard baseline (1x non-participating, broad-based weighted average, standard protective provisions, standard exclusivity window). Included as a control case.

**Reconciliation:** **Pass.** Cap table's own reconciliation (£12.0m ÷ 8,000,000 shares = £1.50/share; £3.2m ÷ £1.50 = 2,133,333 new shares; post-money 10,133,333 × £1.50 = £15.2m; Northbridge at 21.05%) matches the term sheet exactly. Articles Art. 7 (liquidation preference), Art. 8 (board), Art. 9 (protective provisions) match term sheet sections 2, 4, 5 verbatim in substance.

**Summary for Reviewer:** Vanilla, market-standard Series A on every economic term — nothing here needs renegotiation. The gap is documentary, not commercial: only 4 of the ~24 checklist sub-items have supporting documents in hand. Before closing, chase certificate of incorporation, register of directors, full SAFE/option disclosure, employment agreements, IP assignments, insurance, and financials — none of these are red flags yet, they simply haven't been supplied.

---

## Run 2 — Nimbus Robotics Ltd (SAFE, standalone document)

**Instrument:** SAFE — Nimbus Robotics Ltd — Investor Cordwainer Angels LLP — 14 March 2026.

**Key Terms**

| Term | Detail |
|---|---|
| Instrument type | SAFE |
| Amount raised | £750,000 (Purchase Amount) |
| Valuation cap | £6,000,000 (post-money) |
| Discount rate | 20% |
| Price per share | Not stated (set at future Equity Financing) |
| Interest rate | None |
| Maturity date | None |
| Liquidation preference | N/A pre-conversion; on Liquidity Event, investor elects cash (Purchase Amount) or common shares |
| Anti-dilution | Not stated |
| Board composition | Not stated |
| Protective provisions | Not stated |
| Information rights | Not stated |
| Pro-rata rights | Yes, in next Equity Financing |
| Conditions precedent | Not stated |
| Exclusivity | Not stated |
| Governing law | England and Wales |

**Checklist Review** (standalone document, no data room supplied)
- No interest / no maturity date are **expected for a SAFE**, not omissions — correctly marked N/A, not flagged as missing.
- Board composition, protective provisions, information rights — **Not applicable**: a pre-conversion SAFE holder isn't yet a shareholder, so the term sheet not addressing these is expected, not a gap.
- *2. Share Capital & Instruments:* "All outstanding SAFEs/convertibles/options" — **Omitted**, and specifically worth chasing here because the MFN clause (below) makes the answer commercially relevant. Side letters — **Omitted**, unconfirmed.
- All other categories (1, 3–9) — **Omitted**, not part of the reviewed set (standalone SAFE only).

**Unusual Clauses:**
- **Most Favoured Nation (MFN) clause.** Investor receives the benefit of any more favourable terms granted to a later SAFE investor prior to conversion. *Why it matters:* this creates an open-ended repricing risk — every subsequent SAFE the company issues before this one converts needs to be checked against this investor's terms, not just priced independently.

**Summary for Reviewer:** Standard SAFE mechanics (cap + discount, no interest/maturity, standard liquidity/dissolution terms) — the one item to flag to Priya is the MFN clause, since it isn't a one-time term but an ongoing constraint on every future SAFE the company issues. Confirm whether any other SAFEs already exist before relying on the MFN protection being clean.

---

## Run 3 — Anchorline Biotech Ltd (Convertible Loan Note, standalone document)

**Instrument:** Unsecured Convertible Loan Note — Anchorline Biotech Ltd — Noteholder Fenwick Life Sciences Fund II LP — 19 June 2026.

**Key Terms**

| Term | Detail |
|---|---|
| Instrument type | Convertible loan note (unsecured) |
| Principal amount | £500,000 |
| Valuation cap | £8,000,000 (pre-money) |
| Discount rate | 15% |
| Price per share | Not stated (set at Qualifying Financing, lower of discount/cap price) |
| Interest rate | 8% p.a., compounding annually, not cash-paid |
| Maturity date | 24 months from issue |
| Liquidation preference | N/A pre-conversion; unsecured, ranks behind secured creditors |
| Anti-dilution | Not stated |
| Board composition | Not stated |
| Protective provisions | Not stated beyond Events of Default |
| Information rights | Not stated |
| Pro-rata rights | Not stated |
| Conditions precedent | Not stated — no closing-conditions section at all |
| Exclusivity | Not stated |
| Governing law | England and Wales |

**Checklist Review** (standalone document, no data room supplied)
- *3. Material Contracts:* "Loan agreements and other debt instruments" — **Present** (this document is that instrument).
- All other categories — **Omitted**, not part of the reviewed set.

**Unusual Clauses:**
- **1.5x change-of-control premium.** On a Change of Control prior to conversion, the noteholder may elect repayment of principal + accrued interest **plus a 1.5x premium**. *Why it matters:* market baseline for this kind of premium is closer to 1x–1.25x; 1.5x is investor-favourable and materially increases the company's payout obligation on an early exit — worth flagging for negotiation.
- **No conditions-precedent / closing-conditions section.** Unlike the other three sample term sheets, this note has no stated DD, disclosure-letter, or closing-mechanics conditions at all. *Why it matters:* worth confirming whether this was deliberately omitted (fast-close instrument) or simply not drafted — the absence is structurally unusual relative to the other samples.
- **No stated exclusivity period.** *Why it matters:* absent an exclusivity clause, nothing stops Anchorline from shopping the same round to other noteholders simultaneously — worth confirming this is intentional.

**Summary for Reviewer:** Interest rate (8%) and discount (15%) are within market norms, and being unsecured is standard for an early-stage note. Two things need a decision before proceeding: the 1.5x change-of-control premium is above market and worth pushing back on, and the total absence of closing conditions/exclusivity is unusual compared to the firm's other live term sheets — confirm this is intentional rather than a drafting gap.

---

## Run 4 — Solace Data Ltd (Seed round, terse bullet format)

**Instrument:** Series Seed Preferred Shares — Solace Data Ltd — Investor Ridgeline Seed Partners LP — 3 July 2026.

**Key Terms**

| Term | Detail |
|---|---|
| Instrument type | Priced equity round (Series Seed Preferred) |
| Amount raised | £450,000 |
| Pre-/Post-money valuation | £4,000,000 / £4,450,000 |
| Discount rate | N/A |
| Price per share | Not stated (existing share count not given, cannot derive) |
| Interest rate | N/A |
| Maturity date | N/A |
| Liquidation preference | 1x non-participating |
| Anti-dilution | Broad-based weighted average |
| Board composition | 1 investor observer seat; no board seat at seed |
| Protective provisions | Not stated |
| Information rights | Not stated |
| Pro-rata rights | Yes, for next priced round |
| Conditions precedent | Clean disclosure letter; confirmatory legal + IP diligence (14-day window); no MAC since last management accounts |
| Exclusivity | 30 days |
| Governing law | England and Wales |

**Checklist Review** (standalone document, no data room supplied)
- *2. Share Capital & Instruments:* "Any side letters affecting share rights" — **Omitted / open item**, and notably the document itself flags this: the reviewer note explicitly says "confirm no side letters exist before closing" — treat as a checklist gap the drafter has already spotted, not a new finding.
- All other categories — **Omitted**, not part of the reviewed set.

**Unusual Clauses:** None identified — 14-day confirmatory diligence window is fast but explicitly explained (smaller cheque, faster close expected); no board seat at seed stage is normal; 30-day exclusivity is within standard range.

**Summary for Reviewer:** Standard seed terms throughout — the one open item, already flagged by the document's own reviewer note, is confirming no side letters exist before closing. No other deviations from market or checklist gaps beyond the standard data-room absence for a standalone term sheet. This run also confirms the terse bullet source format didn't change the shape of the output versus the numbered-clause and prose-style samples.
