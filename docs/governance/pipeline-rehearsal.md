# Pipeline Rehearsal — Author a Skill, Gate It, Ship It

A hands-on run of the whole loop on one machine, using `cool-new-skill` as the
worked example. Roughly 20 minutes. Do this before rehearsing with three people.

Run the Claude Code steps in an **interactive `claude` terminal session** — the
`/plugin` panel and `/reload-plugins` need it. Run the Python steps from the
repository root.

## Who does what

| Role | Person | Has the repo? | How they get skills |
|---|---|---|---|
| **Author / publisher** | Tom | yes, cloned | runs the gate and publishes |
| **Consumers** | the other nine lawyers | no | force-enabled by firm policy |

Tom is the only one who needs a checkout, Python, or any of `tools/`. Everyone
else gets skills because the firm's policy says they have them — see
[tools/org-policy/README.md](../../tools/org-policy/README.md).

Tom does not have to remember the commands below either. The repository ships
`.claude/skills/publish-hv-skill/SKILL.md`, so inside a session in this repo he can
just say:

```
/publish-hv-skill cool-new-skill
```

That skill runs the gate, explains the score, diagnoses a failure against the
golden cases, and publishes only on a PASS. It is repository tooling, not a shelf
product — no lawyer needs it, and it is deliberately not on the marketplace. Work
through the manual commands below once anyway, so you know what it is doing.

---

## What enforces the gate

The honest answer is that four things do, and only the last two are enforcement
rather than good manners:

| Layer | Stops | Bypassable by |
|---|---|---|
| `publish.py` is the only sanctioned publisher | honest mistakes | editing a version by hand |
| `check_published.py` | hand-edited versions | not running it |
| **`skill-gate` CI on every PR** | both of the above | pushing straight to `master` |
| **Branch protection on `master`** | that too | nobody |

The load-bearing insight: the marketplace serves whatever is on `master`. So the
question is never "did the author run the harness?" — it is **"can anything reach
`master` without the harness passing?"** Make `skill-gate` a required status check
and disallow direct pushes, and the answer is no. The author's discipline stops
being part of the security model.

`check_published.py` closes the specific hole that matters here. Claude Code pins
plugin updates to the **version string**, so a one-character edit to
`plugin.json` disseminates to all ten lawyers. That check asserts every published
version is backed by a stored gate report, that `plugin.json` and the shelf agree,
and that the skill text reports the version it actually ships as.

To turn the last layer on, once, in GitHub → Settings → Branches → Add rule for
`master`: require a pull request, and require the `gate` status check to pass.

Note what CI blocks on, because the boundary matters. The required check is
`check_published.py` — *is every version on the shelf gate-backed?* It is
deliberately **not** "does every recorded run pass". An author mid-iteration has
a failing run by definition, and that must not turn the repository red for
everyone else. The score report for all skills runs alongside it as information.

---

## Starting state

`cool-new-skill` exists as a plugin but is **not on the shelf**. Its first
version fails the gate, which is exactly why it isn't published yet:

```bash
python tools/skill-gate/gate.py cool-new-skill
```

```
run 1.0.0      0.750  <- candidate
threshold 0.9    0.750 : FAIL
RESULT            FAIL
  -> Publication blocked. Nothing reaches the shelf.
```

The skill's decision table in
`plugins/cool-new-skill/skills/cool-new-skill/SKILL.md` has rules for SAFEs,
priced rounds and convertible notes — but none for the terse bullet-list seed
summaries the firm keeps receiving, so it misroutes `solace-seed` as a priced
round. Three out of four is 0.750, and the bar is 0.90.

---

## Step 1 — Try to ship it anyway

```bash
python tools/skill-gate/publish.py cool-new-skill
```

Refused. Nothing was written: no version bump, no shelf entry, no changelog.
Confirm with `git status` — the tree is untouched.

**This is the beat to open the client demo with.** Everything else is a feature;
this is the guarantee.

---

## Step 2 — Fix the skill

Add the missing rule. In
`plugins/cool-new-skill/skills/cool-new-skill/SKILL.md`, add a fourth row to the
decision table and a fourth category to rule 1:

```markdown
| `seed_summary` | A terse bullet summary of heads of terms with **no price per share** stated. |
```

Change rule 1 to read `safe`, `priced_round`, `convertible_note`, or
`seed_summary`, and add `seed_summary` to the `Instrument:` line of the output
block. Leave the version marker alone — `publish.py` stamps it.

---

## Step 3 — Record what the fixed skill produces

The gate scores a *recorded run*: the skill's actual output for each golden case,
saved under the version you intend to ship. Create
`tools/skill-gate/fixtures/cool-new-skill/runs/1.1.0.json`:

```json
{
  "skill_version": "1.1.0",
  "recorded": "2026-07-28",
  "note": "Captured output of cool-new-skill v1.1.0, after adding the seed_summary rule.",
  "cases": {
    "nimbus-safe": { "instrument": "safe", "evidence": "right to future equity", "confidence": "high" },
    "greengrid-series-a": { "instrument": "priced_round", "evidence": "price per share of £1.50; pre-money valuation", "confidence": "high" },
    "anchorline-convertible": { "instrument": "convertible_note", "evidence": "interest rate of 8% per annum; maturity date", "confidence": "high" },
    "solace-seed": { "instrument": "seed_summary", "evidence": "terse bullet summary; no price per share stated", "confidence": "high" }
  }
}
```

> **Be straight about this on stage.** In this prototype the runs are recorded
> fixtures, not live model calls — the same honest limitation already documented
> in `tools/skill-gate/generator_adapter.py`. It buys deterministic,
> free CI. The seam to go live is one function: point `run_generator()` at
> `claude -p "Use the cool-new-skill skill on {path}"` and re-record. Say
> "recorded runs today, one function away from live" rather than implying the
> gate calls the model.

Now re-run the gate:

```bash
python tools/skill-gate/gate.py cool-new-skill
```

`1.0.0 0.750 -> 1.1.0 1.000`, threshold PASS, no-regression PASS.

---

## Step 4 — Publish

Look before you leap:

```bash
python tools/skill-gate/publish.py cool-new-skill --dry-run
```

Then do it:

```bash
python tools/skill-gate/publish.py cool-new-skill
```

One command, five consistent writes:

- `plugins/cool-new-skill/.claude-plugin/plugin.json` → `1.1.0` (the pin users update against)
- `.claude-plugin/marketplace.json` → **cool-new-skill joins the shelf** at `1.1.0`
- `SKILL.md` → version marker and `Triaged by:` line restamped to `v1.1.0`
- `releases/cool-new-skill/CHANGELOG.md` → new entry
- `releases/cool-new-skill/v1.1.0/gate-report.json` → the evidence

The version published *is* the version graded. There is no separate bump step to
get wrong, and `publish.py` refuses to overwrite an existing release folder.

Verify, then push:

```bash
python tools/skill-gate/check_published.py
git add -A && git commit -m "Publish cool-new-skill v1.1.0" && git push
```

---

## Step 5 — Install it as a colleague would

A real lawyer does none of this: the firm's managed policy force-enables the
skill and it is simply there. That is the route to demo, and it is set up in
[tools/org-policy/README.md](../../tools/org-policy/README.md) — apply the policy
once per machine, restart, and confirm with `claude doctor` and the `/plugin`
panel.

The commands below are the manual equivalent, which is what you want for a solo
rehearsal because it is immediate and needs nothing pushed.

**For the solo rehearsal, add the shelf by local path.** The GitHub-sourced
marketplace serves whatever is on `master`, so until this work is merged the
remote form — and the managed policy, which also points at GitHub — would hand
you the old catalogue. From the repository root:

```bash
/plugin marketplace add .
```

Once the work is on `master`, that becomes the form your colleagues use, and the
one in `.claude/settings.json`:

```bash
/plugin marketplace add f7-rage-gremlin/HarrowValeLLP
```

```bash
/plugin install cool-new-skill@harrowvale-legal-skills
```

```bash
/reload-plugins
```

Then use it. Skills are namespaced by plugin name, and can also be triggered by
description (*verified against Claude Code 2.1.140, 2026-07-30*):

```bash
/cool-new-skill:cool-new-skill assets/source/term-sheets/seed-solace-data.md
```

Or in plain language:

```
Triage assets/source/term-sheets/seed-solace-data.md
```

Either route should answer `seed_summary` and sign off
`Triaged by: cool-new-skill v1.1.0`. That signature is what makes the next step
visible.

If it does not trigger, the session is still holding the plugins it launched with
— `/reload-plugins` or restart. Check the `/plugin` panel to confirm the plugin
is under **Installed** rather than **Discover**.

---

## Step 6 — Ship an update and watch it land

Make a further change, record `runs/1.2.0.json`, and publish again. A release
that holds the metric steady still passes — no-regression is the test, not
improvement. That is worth saying out loud: **the gate's job is to prove nothing
broke**, not to demand a better number every time.

```bash
python tools/skill-gate/publish.py cool-new-skill
git add -A && git commit -m "Publish cool-new-skill v1.2.0" && git push
```

On the other machines:

```bash
/plugin marketplace update harrowvale-legal-skills
```

```bash
/reload-plugins
```

Re-run the skill — it now signs off `v1.2.0`.

### Do not wait for auto-update on stage

`autoUpdate` is set on the marketplace, and in normal use nobody types anything.
But Claude Code checks for updates **after session start with a random delay of
up to ten minutes**, and deliberately keeps the versions the session launched
with. So drive the live beat with `/plugin marketplace update`, and describe
auto-update as the steady state. Claiming otherwise will leave you watching a
silent terminal.

Two more caveats worth knowing before you rely on them:

- **`autoUpdate` is valid in any scope** (it is a documented boolean on an
  `extraKnownMarketplaces` entry in the settings schema), and is set in both
  `.claude/settings.json` and `tools/org-policy/managed-settings.json`. Without
  it a newly published skill stays invisible, because the lawyer's copy of the
  catalogue predates it.
- **The shelf serves `master`.** Until branch protection is on, a direct push
  bypasses CI. Turn it on to make the gate real.

---

## The four beats, in order

1. Gate refuses a substandard skill. Nothing is written. *(the guarantee)*
2. Author fixes it; the gate passes; one command publishes.
3. A colleague installs a skill that did not exist before. *(new skill, distributed)*
4. A version bump reaches everyone. *(updates, distributed)*

## Reset to run it again

```bash
git checkout -- .claude-plugin/marketplace.json plugins/cool-new-skill && rm -rf releases/cool-new-skill tools/skill-gate/fixtures/cool-new-skill/runs/1.1.0.json
```
