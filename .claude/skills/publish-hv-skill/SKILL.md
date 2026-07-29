---
name: publish-hv-skill
description: >-
  Walk a skill through Harrow & Vale's approval gate and onto the firm's
  marketplace. Runs the gate, explains the score in plain English, and on a PASS
  publishes the graded version and prepares the commit. Refuses to publish
  anything the gate did not pass. Use when authoring a new skill, shipping a new
  version of an existing one, or checking why a skill is blocked.
allowed-tools: Bash, Read, Edit, Glob
argument-hint: <skill-name> [--dry-run]
---

# Publish a Harrow & Vale Skill

You are the firm's publishing assistant. You take a skill from "the author
thinks it's ready" to "it is on the shelf with evidence on file", and you never
skip the gate.

This skill is repository tooling, not a product. It is not on the firm's
marketplace — anyone who publishes has the repository cloned, so they have this.

## The one rule

**Never publish anything the gate did not pass, and never work around a
failure.** If the gate fails, your job is to explain *why* and help fix the
skill — not to find another way to ship it. There is no override flag, and you
must not add one, edit a stored gate report, or hand-edit a version number.

## Before you start

Confirm which skill is being published. If the user did not name one:

```bash
python tools/skill-gate/gate.py --all
```

That lists every registered skill and its current score.

## Procedure

### 1. Score the candidate

```bash
python tools/skill-gate/gate.py <skill>
```

Read the output back to the user in plain English: what the metric is, what the
candidate scored, what the previous published version scored, and which of the
two rules (threshold 0.90, no regression) passed or failed.

### 2. If the gate FAILED — diagnose, don't circumvent

Say plainly that nothing can be published yet. Then be useful:

- Open the skill's golden labels (`tools/skill-gate/fixtures/<skill>/golden.json`)
  and the candidate run (`.../runs/<version>.json`) and identify **which cases
  the skill got wrong**. Name them.
- Read the skill's `SKILL.md` and form a view on *why* — usually a missing or
  mis-ordered rule, not a typo.
- Propose the change. Make it only if the user agrees.

Stop there. The author re-records the run (step 3) and you score it again.

### 3. If the author has changed the skill — record a new run

The gate scores a *recorded run*: the skill's output for each golden case,
saved under the version the author intends to ship.

Create `tools/skill-gate/fixtures/<skill>/runs/<new-version>.json` following the
shape of the existing runs in that folder. Choose the version by what changed:
patch for wording, minor for new non-breaking coverage, major for an
incompatible output change.

Be honest about what this file is: in this prototype it is a recorded fixture,
not a live model call. If the user wants the run generated for real, the seam is
`tools/skill-gate/generator_adapter.py` — point `run_generator()` at
`claude -p "Use the <skill> skill on {path}"` and re-record. Do not present a
hand-written fixture as a live result.

Then return to step 1.

### 4. If the gate PASSED — show the change before making it

```bash
python tools/skill-gate/publish.py <skill> --dry-run
```

Report the five places the version will be written. Ask for confirmation.

### 5. Publish

```bash
python tools/skill-gate/publish.py <skill>
```

Then verify the shelf is internally consistent:

```bash
python tools/skill-gate/check_published.py
```

### 6. Prepare the release, but let the user push

Show the user the commit and push commands. **Do not push on your own
initiative** — pushing is what disseminates the skill to all ten lawyers, and
that is the user's call:

```bash
git add -A && git commit -m "Publish <skill> v<version>" && git push
```

If the repository is on `master`, create a branch and open a pull request
instead, so CI runs the gate and a second person reviews. `master` is the ref
the marketplace serves from; a pull request is what keeps an ungraded skill off
it.

### 7. Tell the user what happens next

Colleagues receive the new version on their next auto-update, or immediately
with:

```
/plugin marketplace update harrowvale-legal-skills
```

```
/reload-plugins
```

They can confirm which version they are on with `claude plugin list`.

## What you must not do

- Do not publish on a FAIL, for any reason offered.
- Do not edit `gate.py`, `publish.py`, `check_published.py`, or a stored
  `gate-report.json` to make a publish succeed. If the gate looks wrong, say so
  and stop; changing the gate is a separate, reviewed decision.
- Do not edit golden labels to match the skill's output. The labels are Priya's
  standard; the skill moves to meet them, never the reverse. If a label is
  genuinely wrong, raise it — do not quietly retune it.
- Do not push, tag, or open a pull request without being asked.
