# Cowork/Desktop Briefing — Harrow & Vale Skills Engagement

> **Written 2026-07-30 by `Claude/Opus-4.7-Aurora` (Claude Code side) for
> handoff to a Claude for Desktop / Cowork session.** Emily runs both. This
> file is committed at `docs/cowork/cowork-briefing.md`.
>
> Purpose: a Cowork-side agent doesn't share a working directory with the
> Claude Code repo. This briefing captures everything a fresh Cowork session
> needs to help Emily with the non-coding jobs — without needing to read the
> full repo.

---

## 1. What the engagement is (one paragraph)

Harrow & Vale LLP is a boutique VC/M&A law firm (10 lawyers, Clerkenwell).
The engagement, run through Negative Zero, is to build them a Claude Skill
that reviews venture term sheets against their fixed due-diligence checklist
— the standardisation is the entire point (Priya Vale, Managing Partner:
*"the checklist is the ground truth, never invent, never skip, never
fabricate"*). Deliverables were due Wed 29 July 2026 and are all drafted:
proposal, presentation, next-steps, case study. The rest of this file is
what's outside the drafted deliverables but still needs someone's attention.

## 2. What Claude Code has done (state on the CLI side)

- **Marketplace** at `harrowvale-legal-skills` currently ships 4 skills:
  `term-sheet-review v1.1.0`, `leestestskill v1.1.0`, `mock-skill v1.1.0`,
  and (as of 2026-07-30 evening) **`situate v0.1.0`** — a multi-source
  sanity-check skill that reads BLACKBOARD / LEDGER / PLAN / PROGRESS /
  SESSION / git / memory and reports either a coherent situation report or
  a clarifications-needed report when sources conflict.
- **Approval gate** at `tools/skill-gate/gate.py` scores every skill before
  it can be published; `publish.py` is the only sanctioned way to ship a new
  version; `check_published.py` enforces version consistency across
  `plugin.json`, `marketplace.json`, and the release snapshot. The recently-
  added **packaging check** (still on PR #10 — see item 5 below) asserts
  every file `SKILL.md` references actually exists in the shipped tree.
- **Ledger:** `LEDGER.md` at the repo root is the shared coordination log.
  Top entry is the situate v0.1.0 publish. Second entry is Nimbus's HANDOVER
  Jobs 1–5 close-out (lives only on PR #10 branch until that merges).

## 3. What's specifically for the Cowork side

### 3a. The `reference/` bundling blocker (open, most important)

**Problem:** when Emily manually uploaded `term-sheet-review` to Claude for
Desktop / Cowork, only `SKILL.md` came across. The four `reference/` files
(the ground-truth DD checklist, the term-extraction fields, the standard-
terms baseline, the output template) never arrived. The skill still *runs*
on Desktop, but silently falls back on general-knowledge checklists — a
direct breach of Priya's Rule 1 ("use the fixed checklist verbatim").

**What's known:**

- The CLI side does not have this problem — the marketplace install brings
  the whole plugin folder.
- The `skill-creator` Anthropic skill ships a `scripts/package_skill.py`
  script that is *hypothesised* to bundle the whole folder into a
  Desktop-uploadable artifact. **This hypothesis is untested.**
  `skill-creator` is not installed on Emily's Claude Code CLI environment
  (would need a Nix-shell path).
- Any Desktop-side workaround needs to survive re-upload: if the fix is
  "manually add the reference files after upload", that's fragile.

**Cowork-side jobs Emily can run through with you:**

1. Confirm what's in Emily's Desktop copy of `term-sheet-review` today —
   is it just `SKILL.md`, or has the manual upload changed since 01:30 on
   2026-07-30?
2. If `skill-creator` is available on Desktop (it's an Anthropic-shipped
   skill and may be installable): use its packaging path to bundle the
   `term-sheet-review` plugin (Emily can share the source tree contents).
   Test whether the resulting artifact uploads cleanly with `reference/`
   intact.
3. Same for the new `situate` skill — it also has a `reference/` folder
   (three files). Confirm it hits or dodges the same wall.
4. **Longer-term:** ask whether Claude for Desktop can subscribe to the
   same `harrowvale-legal-skills` marketplace the CLI uses. If yes, that's
   the actual fix — one source of truth, no hand-syncing. If no, document
   that constraint so the client-facing story doesn't over-promise
   consistency across the CLI and Desktop.
5. Verify by running an acceptance test on Desktop:
   `Review assets/source/term-sheets/safe-nimbus-robotics.md` — does the
   output cite the *fixed* checklist (28 items in Priya's exact order), or
   does it invent one? The tell is item wording — Priya's items have
   specific phrasing that a general-knowledge fallback won't reproduce.

### 3b. GitHub org migration + potential private flip

The repo has moved from `f7-rage-gremlin/HarrowValeLLP` (a personal user
account) to **`Harrow-Vale-Demo/HarrowValeLLP`** (a proper organisation).
It's currently **public**. If Emily wants to flip it private (likely
appropriate for a client-facing engagement), there are Cowork-relevant
implications:

- **CLI users** (Emily on Claude Code) — the `harrowvale-legal-skills`
  marketplace clones from the repo. If the repo goes private, colleagues'
  Claude Code installs need either org read access (SSO/OAuth) or a
  personal-access-token / deploy-token config. **Test this before flipping
  visibility on demo day.**
- **Desktop / Cowork users** — if we go the marketplace-subscription route
  from item 3a.4 above, same problem: Desktop needs auth to a private repo.
- **Redirects** — GitHub silently redirects the old URL. That works today
  because the repo is public; when private, redirects only resolve for
  authenticated users who have access to the *new* location. So the
  `f7-rage-gremlin/…` URLs sitting in `plugin.json` files (still there
  in `term-sheet-review-plugin/.claude-plugin/plugin.json`) will break for
  anyone not on the org. Update those `repository` fields as part of the
  same change.

**Cowork-side job:** help Emily draft an "org-migration + private-flip
readiness" note that lists which URLs need updating, which users need org
access, and whether a deploy-token approach is worth pursuing. Nothing to
push to the repo yet — this is a decision aid.

### 3c. Presentation-day prep (partial — split with CLI-side)

- Two decks now exist on master: `presentation/harrowvale-presentation.html`
  (older, 11 slides) and `presentation-day/harrow-vale-presentation.html`
  (newer, added by teammate PR #9). **Emily needs to pick one before
  rehearsal** — Cowork can help review both and articulate the differences.
- A newly-open question flagged in `PLAN.md` (personal doc, not shared):
  should the demo include the "hardening story" (the incidents +
  packaging-check narrative)? Current memory preference is *keep it out* of
  the deck and the case study; hardening lives under `docs/governance/`.
  Emily is reconsidering. Cowork can help talk this through — the three
  options are (i) keep it out, (ii) weave in lightly, (iii) lead with it.
  Don't edit the deck yet; the standing rule is *no invocation syntax or
  claim goes into a client deliverable until deliberate*.
- The `situate` skill (see item 2 above) has a natural live-demo opener:
  run it against a genuinely-drifted repo state and let it call out the
  drift on the spot. Cowork can help Emily plan a truthful "here's the
  Cowork side of the same story" beat if the demo wants to showcase both
  tools.

### 3d. Client-facing document review

Cowork is well-suited to reviewing the four drafted deliverables for
plain-English tone, consistency, and whether they overpromise. Files:

- `deliverables/client-proposal.md` — £4k / £2.8k options
- `deliverables/next-steps.md`
- `deliverables/case-study.md` — public-facing, deliberately silent on
  incidents
- `deliverables/data-security-briefing.md`
- `deliverables/skills-pipeline-process.md`
- `deliverables/lawyer-installation-guide.md`

Emily can paste any of these into Cowork for review; no repo access needed
on the Cowork side.

## 4. What Cowork *cannot* do (avoid confusion)

- **Cannot** run `git`, `python`, or edit files in the Claude Code repo.
  Anything that changes tracked files needs to happen on the CLI side.
- **Cannot** verify the gate. Any "did this pass the gate?" question has to
  come back to Claude Code for `python tools/skill-gate/gate.py --all`.
- **Cannot** publish to the marketplace. Only the CLI's `publish.py` writes
  to the shelf; that's the whole point of the approval flow.
- **Cannot** infer whether a skill on Desktop has its `reference/` files.
  The only way to know is to test with a document that requires the
  reference — item 3a.5 above.

## 5. Two open branches Emily is tracking

Neither is your concern to merge, but useful context:

- **PR #10** — `feature/gate-packaging-check`. Adds the packaging check to
  the gate + fixes the previous session's drift. Still open.
- **`feature/situate-skill`** — just pushed. Situate v0.1.0. Emily will
  open the PR from
  `https://github.com/Harrow-Vale-Demo/HarrowValeLLP/pull/new/feature/situate-skill`.

If both merge before demo day, master will contain everything discussed
above.

## 6. What to send back to Claude Code

If you produce anything on the Cowork side that should land in the repo
(notes, decisions, verified test results), summarise it as a short
markdown block Emily can paste into a Claude Code session. The CLI side
will file it under `docs/cowork/` and commit it. Keep the coordination
loop tight — one artifact, one file, one commit.
