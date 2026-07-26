"""
Adversarial evaluator for the term-sheet-review skill.

Scores a candidate structured review (the Generator's output) against a golden
label set, per the Helper's recommended legal build loop:
  Contract (schema)  ->  Generator (skill)  ->  Evaluator (this file).

Metrics per case and aggregate:
  - instrument detection accuracy
  - exception precision / recall / F1   (matched on normalised key + severity)
  - missing-item precision / recall / F1
It intentionally penalises BOTH misses (recall) and over-flagging (precision),
because a lawyer who gets false alarms stops trusting the tool.
"""
from __future__ import annotations
import json, glob, os
from dataclasses import dataclass, field


def _prf(tp: int, fp: int, fn: int):
    p = tp / (tp + fp) if (tp + fp) else 1.0
    r = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0
    return round(p, 3), round(r, 3), round(f1, 3)


def _match(candidate, golden, severity_key=None):
    """Set-match by 'key'; a candidate item is correct only if its key is in
    golden AND (if severity is graded) its severity matches golden's."""
    gold_by_key = {g["key"]: g for g in golden}
    tp = fp = 0
    matched = set()
    sev_correct = 0
    for c in candidate:
        k = c.get("key")
        if k in gold_by_key:
            tp += 1
            matched.add(k)
            if severity_key and c.get("severity") == gold_by_key[k].get("severity"):
                sev_correct += 1
        else:
            fp += 1
    fn = len(gold_by_key) - len(matched)
    return tp, fp, fn, sev_correct


@dataclass
class CaseResult:
    case: str
    instrument_ok: bool
    exc: tuple
    miss: tuple
    severity_accuracy: float


def evaluate_case(candidate: dict, golden: dict) -> CaseResult:
    instrument_ok = candidate.get("instrument") == golden.get("instrument")

    tp, fp, fn, sev_ok = _match(candidate.get("exceptions", []),
                                golden.get("expected_exceptions", []),
                                severity_key=True)
    exc = _prf(tp, fp, fn)
    sev_acc = round(sev_ok / tp, 3) if tp else 1.0

    mtp, mfp, mfn, _ = _match(candidate.get("missing", []),
                              golden.get("expected_missing", []))
    miss = _prf(mtp, mfp, mfn)

    return CaseResult(golden["case"], instrument_ok, exc, miss, sev_acc)


def aggregate(results):
    n = len(results)
    inst = sum(r.instrument_ok for r in results) / n
    exc_f1 = sum(r.exc[2] for r in results) / n
    miss_f1 = sum(r.miss[2] for r in results) / n
    sev = sum(r.severity_accuracy for r in results) / n
    # Overall reliability score: weighted toward exception detection.
    overall = round(0.5 * exc_f1 + 0.2 * miss_f1 + 0.2 * inst + 0.1 * sev, 3)
    return {
        "instrument_accuracy": round(inst, 3),
        "exception_f1": round(exc_f1, 3),
        "missing_f1": round(miss_f1, 3),
        "severity_accuracy": round(sev, 3),
        "overall_reliability": overall,
    }


def run_version(version: str, base: str = "."):
    golden = {}
    for f in glob.glob(os.path.join(base, "golden", "*.json")):
        g = json.load(open(f, encoding="utf-8"))
        golden[g["case"]] = g
    results = []
    for case, g in sorted(golden.items()):
        cand_path = os.path.join(base, "runs", version, case + ".json")
        cand = json.load(open(cand_path, encoding="utf-8"))
        results.append(evaluate_case(cand, g))
    return results, aggregate(results)
