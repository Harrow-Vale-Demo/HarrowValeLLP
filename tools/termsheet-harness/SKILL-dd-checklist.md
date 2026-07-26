---
name: dd-checklist
description: >-
  Map a pile of due-diligence documents against Priya Vale's FIXED due-diligence
  checklist (reference/dd-checklist.md) and return, per checklist item, whether it
  is satisfied — with the document name and location — or missing. Built for the
  "Thursday afternoon dump": drop 30 files, get an instant satisfied/missing report.
  Uses the firm's checklist verbatim; never invents its own categories.
allowed-tools: [Read, Grep, Glob]
argument-hint: <folder-of-dd-documents>
---

# DD Checklist Mapper (Harrow & Vale house method)

Tom's trigger: opposing counsel dumps ~30 documents at 4:30pm; feedback due by
Friday noon. This skill replaces the manual associate scramble.

## Rules
1. **Use Priya's checklist verbatim.** Load `reference/dd-checklist.md`. Every
   item you report against must be one of its items — do not add, rename, merge
   or invent categories.
2. **For each checklist item, decide: satisfied / partial / missing**, and when
   satisfied cite the **document name and the section/page** that satisfies it.
3. **Output is a report, not prose:** a section-by-section table plus a headline
   count — "N of M satisfied, K missing" — and the missing items listed so a
   lawyer can chase them.
4. **Never mark satisfied on a guess.** If a document only partially covers an
   item (e.g. an extract), mark `partial` and say what's still needed.
