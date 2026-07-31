# Using Claude for Governance — the hardening and testing story

> Prepared 2026-07-31 for the Friday presentation.
> Source material for Slide 4 ("How Claude helped"), the Q&A, and the public case study.
> Companion to `slide-04-emily-pack.md`, which holds the actual spoken wording.
>
> **Status discipline:** every claim below is tagged. Do not upgrade a tag on stage.
> ✅ merged and real · 🟡 built but not merged · 📄 specified only · ⬜ not started

---

## The one-sentence version

We did not only use Claude to *write* the skill. We used Claude to **test the skill, find its
own failure modes, and turn each one into a mechanical check** — which is the part that makes
it governable by a law firm rather than merely impressive in a demo.

---

## 1. The arc: hardening was iterative, and it was a relay

This matters because it is honest, and because it shows the process works when more than one
person touches it.

### Phurin started it — 2026-07-29

| What | Detail |
|---|---|
| Found the orphaned `marketplace.json` | A second manifest under `tools/termsheet-harness/.claude-plugin/` pointing at a directory that was not a plugin, referenced by nothing |
| Fixed it and packaged `dd-checklist` properly | Commit `903368f` |
| Added `mock-skill` as a skill-gate smoke test | Gave the gate CI coverage — a deliberately known-bad skill the gate must refuse |

Phurin's instinct was the right one: **prove the gate can say no.** A gate that has only ever
said yes is untested.

### Emily continued it — 2026-07-30 / 31

| # | Issue | Class | Status |
|---|---|---|---|
| H1 | Out-of-date runtime, plus an install check that confirmed itself | Verification integrity | ✅ Closed |
| H2 | Desktop upload shipped `SKILL.md` without its `reference/` files | Packaging integrity | ✅ Diagnosed · 🟡 check written, unmerged |
| H3 | Skill ships worked answers for its own test documents | Evaluation integrity | ✅ Held-out test exists · 📄 verbatim check specified |
| H4 | Two parallel term-sheet systems, two same-named skills | Source-of-truth integrity | ⬜ Open |
| H5 | Second marketplace manifest + version pinning against a stale checkout | Distribution integrity | ✅ Orphan gone · 🟡 Phurin's branch unmerged |

### The honest complication in the relay

Phurin diagnosed and fixed H5 correctly on 29 July. **The branch never merged**, so two days
later the same problem was being rediscovered from scratch.

> **Unmerged work is indistinguishable from work never done.**

That is a genuine process lesson, not a personal one, and it is worth saying out loud. It is
also the single most actionable thing for the next engagement.

---

## 2. Why testing was necessary — the pattern under all five

Every incident was the same failure wearing different clothes:

> **Something was verified somewhere other than where it is used.**

- **H1** — the check read the shelf manifest instead of the machine's install state
- **H2** — the gate scored a recording; the package that reached the machine was never checked
- **H3** — the test scored a document whose answer shipped inside the skill
- **H4** — five copies of the checklist, and no assertion that the one in use is the one approved
- **H5** — a manifest pointing at a non-plugin directory, served from a stale checkout

**None of these announced themselves.** Not one produced an error. In every case the system
kept working and kept looking confident. That is the property that makes them dangerous in a
legal setting, and it is why "it works when we try it" was never going to be sufficient evidence.

### The improvement this pattern points to

Naming a pattern is only half the work. The pattern has **two** properties, and a good fix has
to address both:

| Property | What it means | What fixes it |
|---|---|---|
| **Displaced verification** | Checked in one place, used in another | Move the check to the point of use |
| **Silent divergence** | Nothing signals when the two differ | Refuse, don't degrade |

**Level 1 — the artefact checks itself at the point of use.**
The skill asserts it can read `reference/dd-checklist.md` before doing anything, and refuses to
produce a review if it cannot. Cheap, local, and it fixes both properties in one change: the
check happens where the work happens, and silence becomes a refusal. This is the highest-value
outstanding item in `docs/hardening/H2`, because it defends against every future variant rather
than the one instance we found.

**Level 2 — gate-stamped provenance, which closes the entire class.**
The gate already stores a report of what it graded. Extend it to record the **exact file list
and a hash of each file**, ship that manifest inside the package, and verify it at install time
and at run time. Anything that differs from what was graded refuses loudly.

One mechanism, all five incidents:

| Incident | How provenance catches it |
|---|---|
| H1 | Compares the machine's actual install state against what was graded, not the shelf's claim |
| H2 | Missing `reference/` files break the file list immediately |
| H3 | Exposes that a test document's answer also ships inside the skill |
| H4 | Asserts the checklist in use is the approved copy, not one of five |
| H5 | Asserts the manifest resolves and matches what was graded |

**Level 3 — the principle worth stating once:**

> **Verify where it runs, not where it's convenient. Make absence refuse, not degrade.**

### Framing it for a law firm: chain of custody

Priya and Tom already think in these terms, so use them:

- The **gate** proves the skill was correct **when we examined it**.
- What it never proved is **chain of custody** — that the artefact on a lawyer's machine is
  that same examined thing, unaltered.
- Every one of the five was a **break in the chain**, and **none of the breaks were logged**.
- The fix is the ordinary professional one: stamp the package with what was approved, verify it
  where it is used, and make a mismatch refuse rather than quietly carry on.

This reframes five awkward-sounding bugs as **one well-understood problem with a standard
answer** — which is a considerably better impression than five unrelated mistakes.

**Status honesty:** Levels 1 and 2 are **design, not build**. Neither exists. Present them as
"the design we'd take into the next phase", never as something running today.

### The sharpest single example — H2, for the stage

The skill shipped to a second surface **without its checklist file**. It still ran. It still
produced a clean, structured, confident review. It had simply stopped using Priya's checklist
and started using its own idea of one. **Nothing in the output revealed the difference.**

The evaluation gate could not catch it, because the gate scores the *output* of a recorded run —
it never looked at what was in the *package*.

---

## 3. What "using Claude for governance" actually meant

Three distinct uses, and only the first is the obvious one.

| Use | What it looked like |
|---|---|
| **Generation** | Drafting the skill, the reference files, the extraction logic |
| **Adversarial self-testing** | Being asked to attack its own output — "how could this be wrong and still look right?" — which is how H2 and H3 surfaced |
| **Governance authoring** | Writing the gate, the scorers, the fixtures, the packaging check, and the hardening records themselves |

The second is the one worth talking about. Most AI demos show generation. **The reliability
story comes from making the model prosecute its own work**, then converting whatever it finds
into a check that runs without a human remembering to care.

### The principle we kept landing on

> Stop asking the model to be careful. Make it a check that fails the build.

An instruction in a prompt is a request. A gate check is a guarantee. Every hardening item
above is an attempt to move one rule from the first category to the second.

---

## 4. What has actually been done

**✅ Merged and real**

- The evaluation gate: threshold 0.90 **and** a no-regression rule, enforced by exit code
- `publish.py` as the only sanctioned publisher — writes nothing on a FAIL, and stamps the
  *same version the gate graded* into `plugin.json`, the marketplace, the skill text, the
  changelog and a stored gate report
- `check_published.py` — asserts every published version is backed by a gate report
- `mock-skill` — a deliberately known-bad skill proving the gate refuses (Phurin)
- A held-out test document (Vantor Health) the skill has never seen, with its own labels
- Five hardening records in `docs/hardening/`, written to be blunt rather than flattering

**🟡 Built, not merged** *(say "we've written", never "our gate blocks this")*

- The packaging check — scans `SKILL.md` for every `reference/`, `templates/` or `examples/`
  path and blocks publication if any is absent from the shipped tree. Runs *before* scoring.

**📄 Specified only**

- The verbatim-checklist check — compares the checklist in any output against the source file
  character for character, so a paraphrase fails rather than passing quietly
  (`docs/governance/verbatim-checklist-check-spec.md`)

**⬜ Known open**

- A skill self-check that **refuses to produce a review** if it cannot read
  `reference/dd-checklist.md`. Highest-value outstanding item: it defends against every future
  variant of H2, not just the instance we found.
- One source of truth across Claude Code and Desktop, rather than two hand-synced copies.
- `situate` — a multi-source sanity-check skill exists in the repo and passed the gate, but it
  **does not currently appear as an available skill**, so it is unverified and must not be
  presented as working.

---

## 5. Future testing before client handover

Ordered by value per hour, which is roughly inverse to how interesting they are.

| Priority | Test | Why |
|---|---|---|
| 1 | **Skill refuses without its checklist** | Converts the entire H2 class from silent to loud |
| 2 | **Merge-status sweep in demo prep** | `git branch -r` + a merge check takes seconds and would have prevented H4 and H5 both |
| 3 | **Assert exactly one `marketplace.json`**, at the repo root | Two lines. Catches the next orphan immediately |
| 4 | **Assert every `source` path resolves** to a dir containing `.claude-plugin/plugin.json` | The orphan's actual fault; nothing tests it today |
| 5 | **Verbatim-checklist check** | Implement the existing spec; closes the paraphrase hole |
| 6 | **More held-out documents** | One is enough to break the open-book problem; a handful is enough to trust the score |
| 7 | **Cross-surface consistency test** | Same document, Claude Code and Desktop, assert identical structure |
| 8 | **Install-verification on the machine** | H1's class: check the install state where it is used, not where it is convenient |

### A caveat to state plainly at handover

The gate is good at what it does, and what it does is **score recorded fixtures**. Every
incident so far has lived in the gap between *"the artefact is correct"* and *"the thing running
on a lawyer's machine is correct."*

That gap is not a defect in the gate — it is the **boundary** of the gate. The right response is
to name the boundary and add cheap deterministic checks on the other side of it, rather than to
imply the gate covers ground it does not.

---

## 6. Mapping to what the client actually asked for

### Priya Vale — Managing Partner, sets the standard

> Does not want Claude hallucinating new checklist items or skipping steps. The checklist is a
> fixed, standardised process.

| Priya's concern | What answers it | Status |
|---|---|---|
| Don't invent checklist items | The checklist is a **file the skill reads**, not knowledge in the model | ✅ |
| Don't skip steps | Every item appears in every review with an explicit status; silence is not permitted | ✅ |
| Don't fabricate values | Absent terms read `Not stated`; every value carries its source clause | ✅ |
| *How would we know if it stopped following the checklist?* | This is H2 — and the honest answer is that until the packaging check merges, you would not know from the output alone | 🟡 |
| Paraphrasing the checklist | Verbatim check | 📄 |

**The line for Priya:** *the checklist is not in the model's head, it is a file — and we are
making it mechanically impossible to ship a version that cannot read it.*

### Tom Harrow — Ops & Knowledge Lead, owns adoption

> Wants data security & governance, efficiency & standardisation, and one approved shelf so all
> ten lawyers use the same version.

| Tom's concern | What answers it | Status |
|---|---|---|
| Ten lawyers, ten private prompts | One marketplace; everyone installs from the same shelf | ✅ |
| How does a lawyer get v2? | `autoUpdate`, or `/plugin marketplace update` | ✅ |
| Who vets, and on what evidence? | The gate: 0.90 threshold + no regression, with a stored gate report per version | ✅ |
| Can a bad version reach the shelf? | `publish.py` writes nothing on FAIL; `mock-skill` proves the refusal | ✅ |
| Could a *correct* skill still ship broken? | Yes — that was H2, and it is the honest edge of the story | 🟡 |
| Where does client data go? | `deliverables/data-security-briefing.md`; be careful not to imply UK/EU residency | ✅ |

**The line for Tom:** *the version on the shelf is provably the version the gate graded — there
is no separate bump step that can be got wrong.*

---

## 7. The framing that makes this a strength

The temptation is to hide the incidents. The better story:

> The firm's own process caught all five before a lawyer relied on any of them, and each one
> produced a permanent mechanical check rather than a promise to be careful.
>
> **A governance system that has never found anything is not evidence of quality. It is
> evidence of not having looked.**

Delivered briskly and without apology, this is the strongest material available. Delivered
hesitantly, it reads as instability. If in doubt, use the shorter version in
`slide-04-emily-pack.md` and keep the detail for Q&A.
