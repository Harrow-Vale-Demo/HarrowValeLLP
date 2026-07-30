# situate

A Claude Skill for Harrow & Vale LLP that answers **where is this project
right now?** by reading every coordination source (BLACKBOARD, LEDGER, PLAN,
PROGRESS, HANDOVER-*, git state, memory) and reporting either a coherent
situation report or a clarifications-needed report when sources conflict.

## What it does

- Reads every coordination file, git state, and memory index — no skipping.
- Cross-checks doc claims against git (git wins by default).
- Reports every divergence explicitly; never invents a coherent story.
- Self-diagnoses the caller: on the Focus Board? holds a lock? handle valid?
- In `--conflicts` mode, produces a severity-ordered diagnostic pass.

## Design principle (Priya-style rules — see `reference/rules.md`)

1. Never fabricate agreement.
2. Zoom out — absence is a fact.
3. Prefer git-verifiable facts over doc claims.
4. Ask when ambiguous.
5. Self-diagnose the caller.

## Usage

Ask in plain English:

> Situate this repo — where are we right now?
> Run situate in conflicts mode

Or invoke it explicitly (plugin skills are namespaced `plugin:skill`):

```
/situate:situate
/situate:situate --conflicts
```

*Verified against Claude Code 2.1.140, 2026-07-30.*

## When to run it

- **At the start of every session** — the opening question of every session
  is "where are we?". Situate answers that.
- **Before a handoff** — surfaces anything the next agent will need to know.
- **When you suspect drift** — coordination docs and git have diverged.
- **After a merge** — sanity-check that BLACKBOARD, LEDGER, and git tell the
  same story.

## Files

- `SKILL.md` — the skill definition, procedure, and self-check.
- `reference/sources.md` — every source situate reads, in order.
- `reference/rules.md` — the five Priya-style rules and why each exists.
- `reference/output-templates.md` — the three output shapes verbatim.
- `examples/` — worked runs against known tree states:
  - `example-clean-tree.md` — an all-clear situation report.
  - `example-drifted-tree.md` — a clarifications-needed report against a
    deliberately drifted tree.

## Validation

Built against two golden tree states — one clean, one deliberately drifted with
known divergences. The gate scores situate on whether it correctly classifies
which of those two states it's looking at (`triage` scorer on the `tree_state`
field). A future version will score full report correctness (source coverage +
divergence detection).
