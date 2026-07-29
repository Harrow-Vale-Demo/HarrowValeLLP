#!/usr/bin/env python3
"""
Term-sheet-review eval harness.

Runs the evaluator over every sample format for one or more skill versions,
prints a per-case + aggregate report, writes reports/eval_report.{md,json},
and applies a REGRESSION GATE:
  - overall_reliability must be >= THRESHOLD, and
  - the latest version must not regress vs the previous version.
Exit code 0 = pass, 1 = fail (wire into CI / pre-publish hook).
"""
import json, sys, os, datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)                              # tools/termsheet-harness
GATE = os.path.join(os.path.dirname(BASE), "skill-gate")   # tools/skill-gate
FIXTURES = os.path.join(GATE, "fixtures", "term-sheet-review")

# The gate owns the scorer and the fixtures; this script only formats a report
# from them. Reports stay here, beside the other term-sheet prototype output.
sys.path.insert(0, os.path.join(GATE, "scorers"))
import termsheet  # noqa: E402

THRESHOLD = 0.90
VERSIONS = ["v1", "v2"]  # chronological


def fmt_case(r):
    return (f"  {r.case:<24} instrument={'OK ' if r.instrument_ok else 'MISS'} "
            f"| exc P/R/F1={r.exc[0]:.2f}/{r.exc[1]:.2f}/{r.exc[2]:.2f} "
            f"| missing F1={r.miss[2]:.2f} | severity={r.severity_accuracy:.2f}")


def main():
    lines, report = [], {"generated": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
                         "threshold": THRESHOLD, "versions": {}}
    for v in VERSIONS:
        results, agg = termsheet.run_version(v, FIXTURES)
        report["versions"][v] = {"aggregate": agg,
                                 "cases": {r.case: {"instrument_ok": r.instrument_ok,
                                                    "exception_prf": r.exc,
                                                    "missing_prf": r.miss,
                                                    "severity_accuracy": r.severity_accuracy}
                                           for r in results}}
        lines.append(f"\n=== Skill version {v} ===")
        for r in results:
            lines.append(fmt_case(r))
        lines.append(f"  AGG  instrument={agg['instrument_accuracy']:.2f} "
                     f"exc_F1={agg['exception_f1']:.2f} miss_F1={agg['missing_f1']:.2f} "
                     f"severity={agg['severity_accuracy']:.2f} "
                     f"OVERALL={agg['overall_reliability']:.3f}")

    latest, prev = VERSIONS[-1], VERSIONS[-2]
    latest_score = report["versions"][latest]["aggregate"]["overall_reliability"]
    prev_score = report["versions"][prev]["aggregate"]["overall_reliability"]
    improved = latest_score >= prev_score
    passed = latest_score >= THRESHOLD and improved
    report["gate"] = {"latest": latest, "latest_score": latest_score,
                      "prev": prev, "prev_score": prev_score,
                      "no_regression": improved, "meets_threshold": latest_score >= THRESHOLD,
                      "passed": passed}

    lines.append("\n=== REGRESSION GATE ===")
    lines.append(f"  {prev} overall = {prev_score:.3f}  ->  {latest} overall = {latest_score:.3f}")
    lines.append(f"  no-regression: {'PASS' if improved else 'FAIL'} | "
                 f"threshold {THRESHOLD}: {'PASS' if latest_score>=THRESHOLD else 'FAIL'}")
    lines.append(f"  RESULT: {'PASS ✅' if passed else 'FAIL ❌'}")

    out = "\n".join(lines)
    print(out)

    os.makedirs(os.path.join(BASE, "reports"), exist_ok=True)
    with open(os.path.join(BASE, "reports", "eval_report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    with open(os.path.join(BASE, "reports", "eval_report.md"), "w", encoding="utf-8") as fh:
        fh.write("# Term-Sheet-Review — Eval Report\n\n```" + out + "\n```\n")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
