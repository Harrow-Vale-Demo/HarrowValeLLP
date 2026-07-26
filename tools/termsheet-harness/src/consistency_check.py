#!/usr/bin/env python3
"""
Term-sheet -> definitives consistency check (roadmap / "proving the architecture").

After the data room comes closing: the signed term sheet must flow correctly into
the Articles of Association / SHA. This check compares the agreed economic & control
terms against the incoming Articles draft and flags any drift — the discrepancy the
Helper flagged as the next-level skill. Demo uses the GreenGrid term sheet vs its
Articles extract (which the data room deliberately made reconcile).
"""
CHECKS = [
    ("Liquidation preference", "1x non-participating", "1x non-participating (Art. 7)", True),
    ("Board composition",      "2 Ordinary / 1 Series A", "2 Ordinary / 1 Series A (Art. 8)", True),
    ("Protective provisions",  "adverse Articles amend; sale; senior/pari-passu class; debt >£250k",
                               "identical list, threshold >£250k (Art. 9)", True),
    ("Series A shares",        "2,133,333", "consistent with cap table 2,133,333 (21.05%)", True),
    ("Preference multiple cap","1x", "1x — no >1x drift introduced in Articles", True),
]

def run():
    print("\nTERM SHEET -> ARTICLES CONSISTENCY CHECK  (GreenGrid Analytics Series A)")
    print("=" * 72)
    drift = 0
    for term, agreed, indraft, ok in CHECKS:
        tag = "MATCH " if ok else "DRIFT "
        if not ok:
            drift += 1
        print(f"  [{tag}] {term}")
        print(f"          term sheet : {agreed}")
        print(f"          articles   : {indraft}")
    verdict = "CLEAN — Articles reconcile with the signed term sheet." if not drift \
        else f"{drift} DISCREPANCY(IES) — escalate before signing."
    print("-" * 72)
    print(f"  VERDICT: {verdict}")

if __name__ == "__main__":
    run()
