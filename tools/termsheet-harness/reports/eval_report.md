# Term-Sheet-Review — Eval Report

```
=== Skill version v1 ===
  anchorline-convertible   instrument=OK  | exc P/R/F1=1.00/0.50/0.67 | missing F1=0.00 | severity=1.00
  greengrid-series-a       instrument=OK  | exc P/R/F1=0.00/0.00/0.00 | missing F1=0.00 | severity=1.00
  nimbus-safe              instrument=OK  | exc P/R/F1=0.50/0.50/0.50 | missing F1=1.00 | severity=1.00
  solace-seed              instrument=MISS | exc P/R/F1=0.00/1.00/0.00 | missing F1=1.00 | severity=1.00
  AGG  instrument=0.75 exc_F1=0.29 miss_F1=0.50 severity=1.00 OVERALL=0.496

=== Skill version v2 ===
  anchorline-convertible   instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00 | severity=1.00
  greengrid-series-a       instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00 | severity=1.00
  nimbus-safe              instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00 | severity=1.00
  solace-seed              instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00 | severity=1.00
  AGG  instrument=1.00 exc_F1=1.00 miss_F1=1.00 severity=1.00 OVERALL=1.000

=== REGRESSION GATE ===
  v1 overall = 0.496  ->  v2 overall = 1.000
  no-regression: PASS | threshold 0.9: PASS
  RESULT: PASS ✅
```
