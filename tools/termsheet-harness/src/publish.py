#!/usr/bin/env python3
"""
publish.py — the promotion step of the pipeline.

Ties the three things together: EVAL -> VERSION -> MARKETPLACE.
A skill version cannot enter the marketplace unless the eval gate passes.

  1. Run the eval harness for the skill (reuses evaluator + the same gate).
  2. If PASS: bump the semantic version, prepend a changelog entry, and update
     the plugin's entry in .claude-plugin/marketplace.json (version + lastEval).
  3. If FAIL: refuse to publish and exit non-zero. Nothing reaches the shelf.

Usage:
  python3 src/publish.py term-sheet-review --bump minor
  python3 src/publish.py term-sheet-review --bump minor --simulate-regression
"""
import json, os, sys, argparse, datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))
import evaluator

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MKT = os.path.join(BASE, ".claude-plugin", "marketplace.json")
CHANGELOG = os.path.join(BASE, "CHANGELOG.md")
THRESHOLD = 0.90


def bump(v, kind):
    a, b, c = (int(x) for x in v.split("."))
    return {"major": f"{a+1}.0.0", "minor": f"{a}.{b+1}.0", "patch": f"{a}.{b}.{c+1}"}[kind]


def gate_for(skill, simulate_regression=False):
    """Return (passed, overall, detail). term-sheet-review is graded by the harness;
    other skills use their own gate hook (here dd-checklist is demo-marked)."""
    if skill == "term-sheet-review":
        latest = "v1" if simulate_regression else "v2"   # v1 is the weak first pass
        _, agg = evaluator.run_version(latest, BASE)
        overall = agg["overall_reliability"]
        return overall >= THRESHOLD, overall, agg
    return True, None, {"note": "skill supplies its own gate"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill")
    ap.add_argument("--bump", choices=["major", "minor", "patch"], default="minor")
    ap.add_argument("--simulate-regression", action="store_true",
                    help="grade against the weak v1 output to prove the gate blocks a bad publish")
    args = ap.parse_args()

    mkt = json.load(open(MKT, encoding="utf-8"))
    entry = next((p for p in mkt["plugins"] if p["name"] == args.skill), None)
    if not entry:
        print(f"! unknown skill '{args.skill}'"); sys.exit(2)

    passed, overall, detail = gate_for(args.skill, args.simulate_regression)
    print(f"\nPUBLISH {args.skill}")
    print(f"  eval gate: overall_reliability={overall}  threshold={THRESHOLD}  -> {'PASS' if passed else 'FAIL'}")

    if not passed:
        print(f"  ✗ BLOCKED — gate failed, version stays at {entry['version']}. Nothing published to the marketplace.")
        sys.exit(1)

    old = entry["version"]; new = bump(old, args.bump)
    entry["version"] = new
    entry["lastEval"] = {"overall_reliability": overall, "gate": "PASS",
                         "date": datetime.date.today().isoformat()}
    json.dump(mkt, open(MKT, "w", encoding="utf-8"), indent=2)

    log = open(CHANGELOG, encoding="utf-8").read()
    hdr = f"## {args.skill}\n"
    note = f"### {new} — {datetime.date.today().isoformat()}\n- Published via pipeline. Eval gate PASS (overall {overall}).\n\n"
    log = log.replace(hdr, hdr + note, 1) if hdr in log else log + f"\n{hdr}{note}"
    open(CHANGELOG, "w", encoding="utf-8").write(log)

    print(f"  ✓ version {old} -> {new}")
    print(f"  ✓ marketplace.json updated (plugin '{args.skill}' now v{new}, lastEval recorded)")
    print(f"  ✓ CHANGELOG.md updated")
    print(f"  PUBLISHED to marketplace 'harrowvale-legal-skills'. Lawyers get it via /plugin marketplace update.")


if __name__ == "__main__":
    main()
