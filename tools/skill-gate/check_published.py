#!/usr/bin/env python3
"""
check_published.py — closes the loophole.

gate.py proves a recorded run is good enough. publish.py writes that version
everywhere. Neither stops an author from simply hand-editing a version number
and pushing: the marketplace pins updates to the version string, so a hand-bump
would disseminate an ungraded skill to all ten lawyers.

This check refuses that. For every skill on the shelf it asserts:

  1. plugin.json and the marketplace entry agree on the version;
  2. that version has stored gate evidence, or is a recorded run that passes;
  3. the skill text reports the same version a lawyer is installing.

Run in CI as a required status check. An author cannot then get an ungraded
version onto master, and master is the only ref the marketplace serves.

Exit code 0 = consistent, 1 = a published version is not backed by the gate.
"""
from __future__ import annotations
import glob
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate as gatelib  # noqa: E402

REPO = gatelib.REPO
MARKETPLACE = os.path.join(REPO, ".claude-plugin", "marketplace.json")

# Versions approved under the firm's earlier, pre-gate review process. Their
# evidence is a written evaluation rather than a gate report. Nothing may be
# added here: every new version goes through tools/skill-gate/publish.py.
PRE_GATE_APPROVED = {
    ("term-sheet-review", "1.1.0"): "releases/term-sheet-review/v1.1.0/eval/eval-results.md",
}


def fail(msg: str, problems: list):
    problems.append(msg)
    print(f"  FAIL  {msg}")


def check_entry(entry: dict, problems: list):
    skill = entry["name"]
    print(f"\n{skill}")
    listed = entry.get("version")
    source = entry.get("source", "")
    if not isinstance(source, str) or not source.startswith("./"):
        print(f"  skip  non-local source ({source!r})")
        return

    plugin_path = os.path.join(REPO, source[2:].replace("/", os.sep))
    manifest_path = os.path.join(plugin_path, ".claude-plugin", "plugin.json")
    if not os.path.exists(manifest_path):
        fail(f"{skill}: no plugin.json at {os.path.relpath(manifest_path, REPO)}", problems)
        return

    pinned = json.load(open(manifest_path, encoding="utf-8")).get("version")

    # 1. the shelf and the plugin must agree. plugin.json wins at install time,
    #    so a mismatch means the shelf advertises a version nobody receives.
    if pinned != listed:
        fail(f"{skill}: marketplace says {listed}, plugin.json says {pinned}. "
             f"plugin.json wins at install time, so the shelf is lying.", problems)
    else:
        print(f"  ok    version {pinned} agrees across plugin.json and the shelf")

    # 2. that version must be backed by the gate.
    evidence = os.path.join(REPO, "releases", skill, f"v{pinned}", "gate-report.json")
    if os.path.exists(evidence):
        report = json.load(open(evidence, encoding="utf-8"))
        if report.get("passed"):
            print(f"  ok    gate evidence {os.path.relpath(evidence, REPO)} "
                  f"({report['metric']}={report['candidate_score']})")
        else:
            fail(f"{skill}: stored gate report for v{pinned} records a FAIL.", problems)
    elif (skill, pinned) in PRE_GATE_APPROVED:
        print(f"  ok    pre-gate approval on file: {PRE_GATE_APPROVED[(skill, pinned)]}")
    else:
        result = gatelib.run_gate(skill, candidate=pinned, quiet=True)
        if result and result["passed"]:
            print(f"  ok    recorded run {pinned} passes the gate "
                  f"({result['metric']}={result['candidate_score']})")
        else:
            fail(f"{skill}: v{pinned} is published but has no passing gate result. "
                 f"Publish through tools/skill-gate/publish.py.", problems)

    # 3. the skill must not claim to be a version other than the one shipped.
    for skill_md in glob.glob(os.path.join(plugin_path, "skills", "*", "SKILL.md")):
        text = open(skill_md, encoding="utf-8").read()
        found = re.search(r"\*\*Skill version:\*\*\s*(\d+\.\d+\.\d+)", text)
        rel = os.path.relpath(skill_md, REPO)
        if not found:
            continue
        if found.group(1) != pinned:
            fail(f"{rel} reports v{found.group(1)} but ships as v{pinned}.", problems)
        else:
            print(f"  ok    {rel} reports v{pinned}")


def main():
    mkt = json.load(open(MARKETPLACE, encoding="utf-8"))
    print(f"Shelf: {mkt['name']}  ({len(mkt['plugins'])} skills)")
    problems: list = []
    for entry in mkt["plugins"]:
        check_entry(entry, problems)

    print()
    if problems:
        print(f"{len(problems)} problem(s). A published version is not backed by the gate.")
        sys.exit(1)
    print("Every published version is backed by the gate.")


if __name__ == "__main__":
    main()
