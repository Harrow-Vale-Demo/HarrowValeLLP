# Harrow & Vale — BVCA-aligned baseline (the "standard")
*The single source of truth the skill maps incoming terms against. Derived from
BVCA model documents and the firm's house norms. The skill must NOT invent its
own view — it flags deviations from this list.*

## Economics — standard positions
- **Valuation basis:** pre-money is standard. A **post-money** SAFE cap is more
  founder-dilutive and should be flagged (`aggressive`) if not clearly intended.
- **Liquidation preference:** **1x non-participating** is standard. Participating,
  or >1x, is `aggressive`.
- **Anti-dilution:** broad-based weighted average is standard. Full ratchet is
  `aggressive`.
- **Interest (convertibles):** 0–6% simple is typical. **8%+ or compounding** is `watch`.
- **Discount:** 15–20% is standard.
- **Option pool:** a pre-money option pool is common; **absence** on a priced
  round is worth noting (dilution/incentive impact).
- **Pro-rata rights:** expected for lead investors. Absence is a `missing_item`.
- **MFN:** common in early SAFEs but investor-favourable — record as `watch`.

## Control — standard positions
- **Board:** founder-majority at seed/Series A is standard (e.g. 2 founder / 1
  investor). Investor-majority early is `aggressive`.
- **Protective provisions:** a tight, standard list (adverse Articles amendment,
  sale of company, senior/pari-passu share class, debt above a threshold) is
  standard. A broad veto list is `watch`.
- **Drag-along:** a majority-threshold drag is standard; a low threshold is `watch`.
- **Change-of-control premium (convertibles):** 1x repayment is standard;
  **>1x premium** is `aggressive`.
- **Exclusivity:** 30 days standard; **45 days+** is `watch`.

## Expected terms (drive `missing_items`)
valuation, amount, liquidation_preference, anti_dilution, pro_rata_rights,
board_composition, protective_provisions, information_rights, governing_law.
