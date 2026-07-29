#!/usr/bin/env python3
"""
gate.py — the firm's single approval gate.

Every skill on the HarrowVale Legal Skills shelf is scored by this one gate
before it can be published. A skill declares:

  * golden labels  — the known-correct answers (Priya owns these)
  * a candidate run — the skill's actual output for each golden case
  * a metric        — how the two are compared

The gate applies two rules to the resulting score:

  1. it must meet the threshold (0.90), and
  2. it must not regress against the previously published version.

Exit code 0 = PASS, 1 = FAIL. That exit code is the whole enforcement story:
publish.py refuses to publish on a non-zero exit, and CI refuses to merge.

Usage:
  python gate.py cool-new-skill
  python gate.py cool-new-skill --candidate 1.0.0     # grade an older run
  python gate.py term-sheet-review
  python gate.py --all
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
FIXTURES = os.path.join(HERE, "fixtures")
THRESHOLD = 0.90

sys.path.insert(0, os.path.join(HERE, "scorers"))

# Registry of every skill the gate knows how to score. Every skill's fixtures
# live at fixtures/<skill>/, so a new one is a line here plus that directory.
# Until it appears, a skill has no gate and therefore cannot be published.
SKILLS = {
    "term-sheet-review": {"scorer": "termsheet", "base": os.path.join(FIXTURES, "term-sheet-review")},
    "cool-new-skill": {"scorer": "triage", "base": os.path.join(FIXTURES, "cool-new-skill")},
    "leestestskill": {"scorer": "triage", "base": os.path.join(FIXTURES, "leestestskill")},
}


def semver(v: str):
    return tuple(int(x) for x in v.split("."))


# --------------------------------------------------------------------------
# Scorers. Each returns {version: score} for every recorded run of the skill.
# --------------------------------------------------------------------------

def score_termsheet(base: str):
    """Precision/recall/F1 over exceptions and omissions (scorers/termsheet.py)."""
    import termsheet
    scores = {}
    for path in sorted(glob.glob(os.path.join(base, "runs", "v*"))):
        version = os.path.basename(path)
        _, agg = termsheet.run_version(version, base)
        scores[version] = agg["overall_reliability"]
    return scores, "overall_reliability"


def score_triage(base: str):
    """Fraction of cases where the skill put the document in the right category.

    Reusable across any single-label classifier. The golden file names the field
    being compared via "field" (default "instrument"), so a new skill of this
    shape needs fixtures and one line in SKILLS -- no new scorer.
    """
    golden = json.load(open(os.path.join(base, "golden.json"), encoding="utf-8"))
    field = golden.get("field", "instrument")
    expected = {c["case"]: c[field] for c in golden["cases"]}
    scores = {}
    for path in sorted(glob.glob(os.path.join(base, "runs", "*.json"))):
        run = json.load(open(path, encoding="utf-8"))
        cases = run["cases"]
        correct = sum(1 for case, want in expected.items()
                      if cases.get(case, {}).get(field) == want)
        version = os.path.splitext(os.path.basename(path))[0]
        scores[version] = round(correct / len(expected), 3)
    return scores, golden.get("metric", "accuracy")


SCORERS = {"termsheet": score_termsheet, "triage": score_triage}


# --------------------------------------------------------------------------
# The gate itself
# --------------------------------------------------------------------------

def run_gate(skill: str, candidate: str | None = None, quiet: bool = False):
    spec = SKILLS.get(skill)
    if not spec:
        print(f"! '{skill}' has no registered gate. Skills without a gate cannot be published.")
        print(f"  Registered: {', '.join(sorted(SKILLS))}")
        return None

    scores, metric = SCORERS[spec["scorer"]](spec["base"])
    if not scores:
        print(f"! no recorded runs found for '{skill}' under {spec['base']}/runs/")
        return None

    ordered = sorted(scores, key=lambda v: semver(v.lstrip("v")) if v.lstrip("v")[:1].isdigit() else (0,))
    cand = candidate or ordered[-1]
    if cand not in scores:
        print(f"! no recorded run '{cand}' for '{skill}'. Have: {', '.join(ordered)}")
        return None

    idx = ordered.index(cand)
    prev = ordered[idx - 1] if idx > 0 else None
    cand_score = scores[cand]
    prev_score = scores[prev] if prev else None

    no_regression = prev_score is None or cand_score >= prev_score
    meets_threshold = cand_score >= THRESHOLD
    passed = no_regression and meets_threshold

    result = {
        "skill": skill,
        "metric": metric,
        "candidate": cand,
        "candidate_score": cand_score,
        "previous": prev,
        "previous_score": prev_score,
        "threshold": THRESHOLD,
        "meets_threshold": meets_threshold,
        "no_regression": no_regression,
        "gate": "PASS" if passed else "FAIL",
        "passed": passed,
    }

    if not quiet:
        print(f"\nGATE  {skill}")
        print(f"  metric            {metric}")
        for v in ordered:
            marker = "  <- candidate" if v == cand else ""
            print(f"  run {v:<10} {scores[v]:.3f}{marker}")
        if prev:
            print(f"  no-regression     {prev} {prev_score:.3f} -> {cand} {cand_score:.3f} : "
                  f"{'PASS' if no_regression else 'FAIL'}")
        else:
            print("  no-regression     n/a (first version)")
        print(f"  threshold {THRESHOLD}    {cand_score:.3f} : {'PASS' if meets_threshold else 'FAIL'}")
        print(f"  RESULT            {'PASS' if passed else 'FAIL'}")
        if not passed:
            print("  -> Publication blocked. Nothing reaches the shelf.")

    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill", nargs="?", help="skill name, or use --all")
    ap.add_argument("--candidate", help="grade a specific recorded run instead of the newest")
    ap.add_argument("--all", action="store_true", help="gate every registered skill")
    args = ap.parse_args()

    if args.all:
        results = [run_gate(s) for s in sorted(SKILLS)]
    elif args.skill:
        results = [run_gate(args.skill, args.candidate)]
    else:
        ap.error("give a skill name or --all")

    if any(r is None for r in results):
        sys.exit(2)
    sys.exit(0 if all(r["passed"] for r in results) else 1)


if __name__ == "__main__":
    main()
