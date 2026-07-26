"""
Generator adapter — the seam where the live skill plugs in.

In production, run_generator() invokes the `term-sheet-review` SKILL.md against a
term sheet and returns JSON validated against contract/term_sheet_review.schema.json.
Two supported wirings:

  1. Claude Code (headless):
       claude -p "Use the term-sheet-review skill on {path}" --output-format json
  2. Messages API: load SKILL.md as the system prompt, attach the term sheet, and
     require a tool/response_format matching the contract schema.

For deterministic CI, this prototype reads recorded run fixtures from runs/<version>/,
i.e. captured outputs of real skill runs. Re-record them with --refresh once the
live model wiring is enabled. Keeping fixtures in-repo lets the harness gate every
prompt change on precision/recall without spending tokens on unchanged cases.
"""
import json
import os


def run_generator(case: str, version: str = "v2", base: str = ".") -> dict:
    path = os.path.join(base, "runs", version, case + ".json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)