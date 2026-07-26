#!/usr/bin/env python3
"""
DD-checklist mapper demo — the 'Thursday afternoon dump' in action.

Parses Priya's fixed checklist (reference/dd-checklist.md) verbatim, then maps a
manifest of dumped documents (data-room mock set) against it, emitting a
satisfied/partial/missing report with citations. In production the manifest is
built by the skill reading the actual dumped folder; here we use the mock
GreenGrid data-room set so the demo is reproducible.
"""
import re, os, json, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# What landed in the "dump" and which checklist items each doc evidences.
MANIFEST = [
    {"doc": "articles-of-association-greengrid.md",
     "satisfies": {"Articles of Association (current, as amended)":
                   ("partial", "Extract only — Arts. 3,7,8,9; full instrument in DMS")}},
    {"doc": "cap-table-greengrid.md",
     "satisfies": {"Register of members / cap table":
                   ("satisfied", "Cap table, post-Series-A-close"),
                   "Full capitalisation table, fully diluted":
                   ("satisfied", "Reconciled to term sheet: 10,133,333 FD shares")}},
]

def parse_checklist(path):
    items, section = [], None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip()
        m = re.match(r"^##\s+\d+\.\s+(.*)", line)
        if m:
            section = m.group(1).strip(); continue
        m = re.match(r"^-\s+(.*)", line)
        if m and section:
            items.append((section, m.group(1).strip()))
    return items

def run():
    items = parse_checklist(os.path.join(BASE, "reference", "dd-checklist.md"))
    ev = {}
    for d in MANIFEST:
        for item, (status, cite) in d["satisfies"].items():
            ev[item] = (status, d["doc"], cite)
    rows, sat, part, miss = [], 0, 0, 0
    for section, item in items:
        if item in ev:
            status, doc, cite = ev[item]
            rows.append((section, item, status, f"{doc} — {cite}"))
            sat += status == "satisfied"; part += status == "partial"
        else:
            rows.append((section, item, "missing", ""))
            miss += 1
    total = len(items)
    print(f"\nDD CHECKLIST REVIEW — {sat} satisfied, {part} partial, {miss} missing "
          f"(of {total})\n" + "=" * 68)
    cur = None
    for section, item, status, cite in rows:
        if section != cur:
            print(f"\n[{section}]"); cur = section
        tag = {"satisfied": "✔ ", "partial": "~ ", "missing": "x "}[status]
        print(f"  {tag}{item}")
        if cite:
            print(f"       ↳ {cite}")
    missing = [f"{s}: {i}" for s, i, st, _ in rows if st == "missing"]
    print("\nCHASE LIST (missing):")
    for m in missing:
        print(f"  - {m}")
    json.dump({"satisfied": sat, "partial": part, "missing": miss, "total": total,
               "rows": [{"section": s, "item": i, "status": st, "citation": c} for s,i,st,c in rows]},
              open(os.path.join(BASE, "reports", "dd_report.json"), "w", encoding="utf-8"), indent=2)

if __name__ == "__main__":
    run()
