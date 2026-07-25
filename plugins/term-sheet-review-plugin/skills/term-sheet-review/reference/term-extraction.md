# Term Extraction — Fields by Instrument Type

For every field: record the **value** + a **short source quote or clause ref**.
If a field is not present in the document, record `Not stated`. Never infer.

## Common (all instruments)
- Company / issuer
- Investor / noteholder / lead investor
- Date
- Instrument type (and the signals that told you)
- Amount (purchase amount / principal / amount raised)
- Governing law
- Conditions to closing / conditions precedent (if any)
- Exclusivity period (if any)
- Confidentiality / binding-vs-non-binding note (if stated)
- Legal fees & expenses: who pays the round's legal costs, and is there a cap on investor legal fees the company must cover? (🟡 flag if no cap stated, or cap is high e.g. >£30k for early stage)
- Founder vesting schedule (if stated): duration, cliff, acceleration terms (single-trigger / double-trigger). Standard is 4 years with 1-year cliff — flag deviations.

## SAFE
- Valuation cap (state pre- or post-money)
- Discount rate
- Interest (should be none — flag if present, it may not be a true SAFE)
- Maturity date (should be none — flag if present)
- Conversion trigger (equity-financing threshold) and conversion mechanics (cap vs discount, which applies)
- Most-Favoured-Nation (MFN) clause — present? (🔴 flag if yes)
- Pro-rata rights
- Liquidity-event and dissolution-event treatment

## Priced equity round
- Pre-money valuation
- Post-money valuation
- Price per share
- New shares issued
- Fully-diluted shares post-round
- Investor ownership %
- Liquidation preference: multiple (1x/2x…) + participating vs non-participating
- Anti-dilution: none / broad-based WA / narrow-based WA / full ratchet
- Board composition (seats by class)
- Protective provisions / consent items (list them)
- Information rights (threshold + what)
- Option pool (created this round? size?) — note if absent
- Pro-rata rights

## Convertible loan note
- Principal amount
- Interest rate (and whether cash-pay or accruing/compounding, when paid)
- Maturity date / term
- Conversion discount
- Valuation cap (state pre- or post-money)
- Qualifying-financing threshold
- Conversion mechanics (lower of discount price vs cap price)
- Change-of-control treatment (repayment premium? conversion option?) — 🔴 flag any premium
- Events of default
- Security / ranking (secured vs unsecured, seniority)

## Notes on extraction discipline
- Percentages and share counts: report exactly as stated; do **not** recompute or "correct" them. If they look inconsistent, that is a **flag**, not something to fix.
- If the document gives both a value and a definition (e.g. "Discount Price means…"), quote the operative value and reference the definition.
- Keep quotes short (a clause number or ≤1 line). The lawyer has the full document.
