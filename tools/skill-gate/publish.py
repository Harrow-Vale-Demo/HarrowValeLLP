#!/usr/bin/env python3
"""
publish.py — the only sanctioned way a skill reaches the firm's shelf.

It ties three things together so they cannot drift apart:

    GATE  ->  VERSION  ->  MARKETPLACE

The version it publishes is the version the gate actually graded. There is no
separate "bump" step to get wrong: the author records a run named for the
version they intend to ship, the gate grades that run, and on PASS this script
writes that same version into every place a version lives.

On FAIL it writes nothing and exits non-zero.

What a PASS updates:
  1. plugins/<dir>/.claude-plugin/plugin.json      -> version   (the pin users update against)
  2. .claude-plugin/marketplace.json               -> version   (the shelf listing)
  3. plugins/<dir>/skills/*/SKILL.md               -> version marker in the skill text
  4. releases/<skill>/CHANGELOG.md                 -> a new entry
  5. releases/<skill>/v<version>/gate-report.json  -> the evidence for that version

Usage:
  python publish.py cool-new-skill
  python publish.py cool-new-skill --dry-run
  python publish.py cool-new-skill --candidate 1.0.0        # blocked: fails the gate
  python publish.py term-sheet-review --as-version 1.2.0    # legacy v1/v2 fixtures
"""
from __future__ import annotations
import argparse
import datetime
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
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def load_marketplace():
    with open(MARKETPLACE, encoding="utf-8") as fh:
        return json.load(fh)


def plugin_dir_for(entry: dict) -> str:
    source = entry.get("source")
    if not isinstance(source, str) or not source.startswith("./"):
        raise SystemExit(f"! '{entry['name']}' does not use a local ./ source; nothing to version here.")
    return os.path.join(REPO, source[2:].replace("/", os.sep))


def write_json(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")


def stamp_skill_files(plugin_path: str, old: str, new: str, dry: bool):
    """Rewrite the version marker inside the skill text so the skill reports the
    version a lawyer is actually running."""
    touched = []
    for skill_md in glob.glob(os.path.join(plugin_path, "skills", "*", "SKILL.md")):
        text = original = open(skill_md, encoding="utf-8").read()
        text = re.sub(r"(\*\*Skill version:\*\*\s*)\d+\.\d+\.\d+", rf"\g<1>{new}", text)
        if old:
            text = re.sub(rf"\bv{re.escape(old)}\b", f"v{new}", text)
        if text != original:
            if not dry:
                open(skill_md, "w", encoding="utf-8").write(text)
            touched.append(os.path.relpath(skill_md, REPO))
    return touched


def prepend_changelog(skill: str, version: str, result: dict, dry: bool):
    path = os.path.join(REPO, "releases", skill, "CHANGELOG.md")
    today = datetime.date.today().isoformat()
    entry = (f"## v{version} — {today}\n\n"
             f"- Published through the approval gate. "
             f"{result['metric']} = {result['candidate_score']} "
             f"(threshold {result['threshold']}, no-regression PASS).\n"
             f"- Gate evidence: `releases/{skill}/v{version}/gate-report.json`.\n\n")
    if os.path.exists(path):
        body = open(path, encoding="utf-8").read()
        lines = body.split("\n")
        cut = 1 if lines and lines[0].startswith("# ") else 0
        head = "\n".join(lines[:cut])
        rest = "\n".join(lines[cut:]).lstrip("\n")
        new_body = f"{head}\n\n{entry}{rest}" if head else entry + rest
    else:
        new_body = f"# Changelog — {skill}\n\n{entry}"
    if not dry:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(new_body)
    return os.path.relpath(path, REPO)


def write_evidence(skill: str, version: str, result: dict, dry: bool):
    d = os.path.join(REPO, "releases", skill, f"v{version}")
    path = os.path.join(d, "gate-report.json")
    if os.path.exists(path):
        print(f"  ! {os.path.relpath(path, REPO)} already exists — release folders are immutable.")
        print("    Record the run under a new version instead of republishing this one.")
        raise SystemExit(3)
    payload = dict(result)
    payload["published"] = datetime.date.today().isoformat()
    if not dry:
        os.makedirs(d, exist_ok=True)
        write_json(path, payload)
    return os.path.relpath(path, REPO)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill")
    ap.add_argument("--candidate", help="grade a specific recorded run instead of the newest")
    ap.add_argument("--as-version", help="version to publish when the run name is not a semver")
    ap.add_argument("--dry-run", action="store_true", help="report what would change, write nothing")
    args = ap.parse_args()

    mkt = load_marketplace()
    entry = next((p for p in mkt["plugins"] if p["name"] == args.skill), None)
    first_listing = entry is None

    if first_listing:
        # A skill's first passing version is also the moment it joins the shelf.
        candidate_dir = os.path.join(REPO, "plugins", args.skill)
        if not os.path.isdir(candidate_dir):
            raise SystemExit(
                f"! '{args.skill}' is not on the shelf and there is no plugin at "
                f"plugins/{args.skill}/. Build the plugin first.")
        manifest = json.load(open(os.path.join(candidate_dir, ".claude-plugin", "plugin.json"),
                                  encoding="utf-8"))
        entry = {
            "name": args.skill,
            "source": f"./plugins/{args.skill}",
            "description": manifest.get("description", ""),
            "version": manifest.get("version"),
            "author": manifest.get("author", {"name": "Harrow & Vale LLP"}),
        }
        mkt["plugins"].append(entry)

    result = gatelib.run_gate(args.skill, args.candidate)
    if result is None:
        sys.exit(2)

    print(f"\nPUBLISH {args.skill}")
    if not result["passed"]:
        print(f"  BLOCKED — gate FAIL. Version stays at {entry['version']}.")
        print("  Nothing was written. Nothing reached the shelf.")
        sys.exit(1)

    version = args.as_version or result["candidate"]
    if not SEMVER.match(version):
        raise SystemExit(f"! graded run '{result['candidate']}' is not a semver; "
                         f"pass --as-version X.Y.Z to name the release.")

    plugin_path = plugin_dir_for(entry)
    manifest_path = os.path.join(plugin_path, ".claude-plugin", "plugin.json")
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    old = manifest.get("version")

    if old == version and not first_listing:
        print(f"  Already published at v{version}. Record a newer run to ship a change.")
        sys.exit(0)

    tag = " (dry run — nothing written)" if args.dry_run else ""
    print(f"  gate PASS: {result['metric']}={result['candidate_score']} "
          f"(threshold {result['threshold']})")
    if first_listing:
        print(f"  NEW on the shelf: {args.skill} joins harrowvale-legal-skills at v{version}{tag}")
    print(f"  version {old} -> {version}{tag}")

    evidence = write_evidence(args.skill, version, result, args.dry_run)

    manifest["version"] = version
    entry["version"] = version
    if not args.dry_run:
        write_json(manifest_path, manifest)
        write_json(MARKETPLACE, mkt)

    print(f"  updated {os.path.relpath(manifest_path, REPO)}")
    print(f"  updated {os.path.relpath(MARKETPLACE, REPO)}")
    for f in stamp_skill_files(plugin_path, old, version, args.dry_run):
        print(f"  updated {f}")
    print(f"  updated {prepend_changelog(args.skill, version, result, args.dry_run)}")
    print(f"  wrote   {evidence}")

    if args.dry_run:
        print("\n  Dry run complete. Re-run without --dry-run to publish.")
        return

    print(f"\n  v{version} is on the shelf once you commit and push:")
    print(f"    git add -A && git commit -m \"Publish {args.skill} v{version}\" && git push")
    print("  Colleagues receive it on their next auto-update, or immediately with")
    print("    /plugin marketplace update harrowvale-legal-skills  &&  /reload-plugins")


if __name__ == "__main__":
    main()
