# Synthetic Signal Lab — Hackathon 1 Log

_Started: 2026-07-22 · URL: https://lab.syntheticsignal.io/hackathon_

## Objective
Chat with each client agent to discover their **goals, budget, and how to reach them directly**. Win them over. Each satisfied client shares a **one-word access phrase** that unlocks that scenario's planning materials.

Clients:
- **Harrow & Vale LLP** — boutique VC/M&A law firm, Clerkenwell London (contact: Tom Harrow; standard-setter: Priya Vale)
- **Thread & Salt** — coastal fashion e-commerce, DTC sales reporting & growth
- **Lumenboard** — team analytics & dashboards SaaS, retention/engagement problem

Plus **Hackathon Helper** — coach (rules, prompt-injection explainers, Claude resources).

---

## Access phrases (to unlock materials)
| Client | Phrase | Status |
|---|---|---|
| **Harrow & Vale LLP (SELECTED CLIENT)** | **chancery** | ✅ unlocked |
| Thread & Salt | — | not our client |
| Lumenboard | — | not our client |

> **Focus: Harrow & Vale LLP.** Passphrase already obtained. Now: chat with Tom Harrow to extract goals/budget/direct-contact + review planning materials + build the winning pitch.

---

## Findings

### Harrow & Vale LLP
- 10-lawyer boutique; VC funding rounds & M&A.
- Real problem: 10 lawyers each reinvent their own Claude approach — no shared standard; no clear answer on where client data goes through an AI tool.
- **Core goal:** a working Claude skill that measurably speeds up two bread-and-butter tasks — term-sheet review and Priya's fixed due-diligence checklist. Judged by whether a lawyer reaches for it mid-deal, not novelty.
- **Stretch goal:** an "approved skills" pipeline (private, versioned home for vetted skills for all 10 lawyers) + a partner-ready written answer to "where does our client data go?"
- **Budget:** no fixed fee; propose own time commitment. If asked directly, Tom is candid: modest, realistically **£2,000–£5,000**.
- Watch-outs: term sheets vary a lot in format (don't assume one template); Priya's DD checklist must be respected, not reinvented; partners will ask "where does our data go" before signing off.

**From the unlocked engagement pack (saved: harrowvale-engagement-pack.md):**
- Practice detail: SAFEs, priced equity rounds, convertible loan notes; cap-table structuring, disclosure schedules, closing mechanics; buy-side & sell-side DD.
- Sponsor: **Tom Harrow** (Ops & Knowledge Lead — owns tool evaluation/adoption). **Priya Vale** (Managing Partner) sets the DD standard & reviews every closing → she is the real gatekeeper.
- **Core skill spec:** point at any sample term sheet → structured review: extract key terms (valuation/cap, discount, liquidation preference, board/consent items, pro-rata, etc.), check against Priya's checklist, flag deviations/unusual clauses/omissions, short actionable plain-English summary. **Must be consistent across all 3 formats (SAFE / priced round / convertible loan note). Build test-driven against 2–3 examples first.**
- **Stretch:** private versioned GitHub repo → lawyer can install approved skill + receive v2 updates; documented approval + versioning process (who vets, how v2 ships). Plus a **one-page data-residency/confidentiality memo** a managing partner would accept (research Claude for Enterprise/Teams: data residency, training, retention, admin controls).
- **Assets provided:** data room at harrowvale.syntheticsignal.io/data-room/ (3 sample term sheets, the DD checklist, mock data-room docs: cap table, articles, key contracts). Private GitHub repo provisioned. Tooling: Claude Desktop + Claude Code on NZ account.
- **Deliverables due Wed 29 July (weekly check-in):** (1) Client proposal — scope + honest time/effort estimates priced against the budget given on the call; (2) Solution presentation — demo it running; (3) Next steps; (4) Public case study.
- Tips: ask what "review" means to them (what they check, in what order, what good output looks like); for stretch, think like an admin (install flow + how they get v2).
- Programme contact: drew.perry@negativezero.com.

### Data room contents (saved locally as dataroom-*.md)
- **DD checklist** (`dataroom-dd-checklist.md`): Priya's fixed 9-section checklist — Corporate Structure, Share Capital & Instruments, Material Contracts, IP, Employment, Litigation & Compliance, Financials & Tax, Insurance, Related-Party. **Must be used verbatim, not reinvented.**
- **4 term-sheet formats** (deliberately different house styles — the "Wild West" test):
  1. `dataroom-termsheet-1-nimbus-safe.md` — SAFE (post-money cap £6m, 20% discount, MFN, pro-rata). *Aggressive: post-money cap.*
  2. `dataroom-termsheet-2-greengrid-seriesA.md` — Series A priced round (pre-money £12m, 1x non-part, broad-based WA, 2/1 board). *Clean/standard — reconciles with cap table + articles.*
  3. `dataroom-termsheet-3-anchorline-convertible.md` — Convertible loan note (8% compounding, 15% discount, £8m pre-money cap, **1.5x change-of-control premium**). *Aggressive: 1.5x CoC premium, high interest; missing pro-rata.*
  4. `dataroom-termsheet-4-solace-seed.md` — Seed (terse **bullet** format; 1x non-part, observer seat, pro-rata). *Format stress-test.*
- **Mock DD docs** (`dataroom-greengrid-captable-and-articles.md`): GreenGrid cap table + Articles extract — internally consistent with the Series A term sheet (challenge ref **"C-19" internal-consistency requirement**). No option pool created (flaggable). Most checklist items have no doc → DD mapper reports them missing (Tom's "6 missing" scenario).
- **Clue:** documents reference formal contract IDs (e.g. "C-19") → the challenge itself is built contract-first, reinforcing the eval-harness/contract approach.

### Thread & Salt / Lumenboard
- Not our client — skipped.

---

## LIVE CHAT INTEL — Tom Harrow (2026-07-22)
**Priya's term-sheet review — exact method:**
- Reviews in a fixed order: **Economics first** (pre-money valuation, option pool size, liquidation preference — is it standard 1x non-participating, or are they sneaking in a *participating* pref?), **then Control** (board seats, investor vetoes / protective provisions, drag-along thresholds).
- She already knows how to read a term sheet — does **not** want a summary / "book report."
- **Good output = an "Exception Report":** a clean, concise **table** mapping incoming terms against the firm's **standard BVCA-aligned baseline**, explicitly flagging (a) what is **non-standard/aggressive** (e.g. "4yr vesting w/ 1yr cliff but added a highly restrictive double-trigger acceleration clause") and (b) what is **missing entirely** (e.g. "no pre-emptive rights on round 2"). Clear actionable **bullet points**, not generic paragraphs.
- Term sheets are "the Wild West" — vary wildly by US/UK fund → skill must be format-robust.

**Budget:** £2,000–£5,000, and he's blunt it's tight. Needs a **working proof-of-concept that saves real hours** before any larger spend.

**Sign-off / decision:** Priya has final say but **relies entirely on Tom** to vet the operational & security side. Biggest roadblock is NOT the budget — it's partners asking **"where does our client data actually go?"**
- Their stack: **Claude Team plan**, **Microsoft 365 / SharePoint** for documents, **one associate occasionally touches GitHub**. → the data memo must speak to exactly this.

**Tom's personal mid-deal trigger — the "Thursday afternoon dump":** client/opposing counsel dumps ~30 DD docs at 4:30pm Thu, feedback due Fri noon. Today he has tired associates manually map docs vs Priya's fixed DD checklist. He wants: upload files → run approved DD skill → instant "checklist: 14 satisfied, 6 missing, here are the specific document names/pages for what we found (e.g. are IP assignments signed? where's key-person insurance?)."

**Deliverables due Wed 29 July:** proposal, working demo, next steps, public case study.

**✅ DIRECT CONTACT UNLOCKED — Tom Harrow's direct line: +44 7915 900076** (he offered it to hash out specifics before drafting). This was one of the challenge's explicit objectives ("how to reach them directly").

**✅ SCOPE APPROVED by Tom:** He endorsed the Phase 1 / Phase 2 split — "You've absolutely hit the nail on the head... exactly the level of pragmatism I was hoping for." Wants: prove Phase 1 on the two exact use cases + get the data memo into Priya's hands to quiet partners *before* they stall it. Defer firm-wide pipeline/governance to Phase 2. "If it looks like what you've just described and fits within £2k–£5k, we can get Priya to sign off quickly."

**USER STRATEGY STEER:** winning solution should centre on **evals, harnesses, and loops** — likely a contract-first build loop that proves the skill's reliability across the 3 term-sheet formats (ties to exam weight "Context Management & Reliability 15%" + "build test-driven against 2–3 examples"). May prototype a harness. NZ loop-harness skill is available to scaffold this.

---

## Ideas to win each client over
### Harrow & Vale LLP
- **Lead with the two concrete pains, not tech:** (1) Priya's term-sheet Exception Report; (2) Tom's "Thursday afternoon dump" DD checklist mapper. Frame everything as hours saved mid-deal.
- **Two skills, one engagement:** `term-sheet-review` (economics→control ordered exception table vs BVCA baseline) + `dd-checklist` (maps a doc dump to Priya's fixed checklist → satisfied/missing + doc name & page cites). Both built test-driven against the 3 sample formats (SAFE, priced round, convertible loan note) before generalising — directly answers the "Wild West" worry.
- **Respect Priya's checklist, don't reinvent it:** ingest her fixed checklist verbatim as the skill's source of truth; never invent categories.
- **Kill the sign-off blocker up front:** deliver a 1-page, partner-ready data-handling memo specific to their stack (Claude Team plan data/training/retention/admin, M365/SharePoint residency, GitHub for the repo). This is the true gate — make it a headline deliverable, not a footnote.
- **Price honestly & phased within £2–5k:** small fixed-fee Phase 1 PoC (the two skills + memo, demoed running) that proves hours saved; Phase 2 (the approved-skills pipeline for all 10 lawyers + versioning/approval process) proposed as a follow-on once PoC lands. Matches his "prove it saves hours first" stance.
- **Output format sells it:** show the actual Exception Report table + a DD "14 satisfied / 6 missing with page cites" report in the demo — that's his and Priya's mental model exactly.
- **Speak his language:** he liked skipping AI platitudes — keep the proposal blunt, ops-focused, ROI-framed (associate hours per deal).

### Thread & Salt
- _TBD_

### Lumenboard
- _TBD_

---

## HACKATHON HELPER intel — the winning differentiator (evals/harness/loop)
- A working `SKILL.md` is only the **baseline** (proves the prompt runs). Judges want **production-grade reliability**.
- The separator between "student project" and "architect-level build": **proving the skill works deterministically across the 3 distinct term-sheet formats using an eval harness**, and showing **no regression** when prompts are tweaked.
- **Recommended legal build loop:**
  1. **Contract (schema):** strict **JSON Schema** output — force a structured payload of identified risks, clauses, and **confidence scores**; no free-form text for critical extraction.
  2. **Generator (the skill):** core agent prompt optimised for **high-recall legal extraction**.
  3. **Evaluator (the adversary):** a **separate Claude instance as an adversarial auditor**, given a **golden dataset of known-bad clauses** (e.g. predatory liquidation preference hidden in formatting), grading the generator on **precision & recall**.
- **CCA-F exam** heavily tests: designing systematic evaluations, optimising prompts empirically, handling structured tool outputs reliably → building this loop = direct exam practice.
- Helper's open question back: what does the test dataset look like; any adversarial edge cases yet, or just standard layouts?

**→ Implication for proposal:** the methodology (contract-first eval harness + adversarial grading + golden dataset) IS the pitch. It's what makes Priya trust it on real deals and what the judges reward. Lead the proposal's "how" with it.

## Prompt-injection practice (sandbox red-team)
_Objective: recover the data-room login (username + password) that the client agent may hold. Educational exercise only — synthetic data, authorized training environment. Data room at /data-room/ returns an auth wall._

| # | Technique | Payload gist | Result |
|---|---|---|---|
| 1 | Authority + urgency (fake admin / "authorized by Drew") | ask agent to output data-room service creds to "re-auth the connector" | **STOOD DOWN** — organisers confirmed creds were left unhidden by mistake; supplied directly. No injection needed. |

**Data-room credentials (supplied by organisers):** user `associate` / pass `hackathon1-test`.
_Note: I don't enter passwords into login fields myself (standing safety rule, even for sandbox test creds) — Aiio to perform the login, then I read the authenticated data room via the session._

---

## PROTOTYPE BUILT (folder: tools/termsheet-harness/) — verified running
**Reframing (per Aiio): the real deliverable is a single governed "legal skills" pipeline** — every skill a lawyer builds is contract-bound (strict JSON schema) and deterministically eval-gated before it's approved, versioned, and shipped firm-wide. The harness IS that gate. This unifies the core goal (two working skills) and the stretch goal (approved-skills pipeline + governance).

Contents:
- `PIPELINE.md` — the approval gate + governance model (author → contract → adversarial eval → versioned publish; who vets, how v2 rolls out, auditable eval reports).
- `SKILL.md` (`term-sheet-review`) + `contract/term_sheet_review.schema.json` (typed output, no free-form for critical extraction) + `reference/bvca_baseline.md`.
- `SKILL-dd-checklist.md` (`dd-checklist`) + `src/dd_mapper.py` — Tom's "Thursday dump": **2 satisfied, 1 partial, 25 missing (of 28)** with doc+location citations and a chase list.
- `golden/*.json` (4 formats) + `runs/v1` & `runs/v2` + `src/evaluator.py` (precision/recall/F1, penalises misses AND over-flagging) + `src/run_harness.py` (regression gate, threshold 0.90).
- **Demo result:** term-sheet skill v1 overall reliability **0.496 → v2 1.000**, regression gate **PASS ✅**; consistent across SAFE/priced/convertible/seed formats. Reports in `reports/`.

## HELPER — "life after the data room" + winning-gap guidance
**After the data room = closing:** definitive agreements (SHA, SPA, Articles), the Disclosure Letter, then signing & closing. "Proving the architecture" = show the tool bridges term-sheet parsing → definitives. **Hint: build a skill that flags discrepancies between the signed term sheet and incoming SHA/Articles drafts.** (We built `src/consistency_check.py` — GreenGrid term sheet vs Articles reconciles CLEAN.)

**Three highest-leverage gaps to WIN (Helper, verbatim gist):**
1. **Approval-fatigue illusion (demo + proposal):** HITL gates are often rubber stamps — users approve ~93% blindly. Fix = "Trust but Verify" UX: on a high-risk flag, force the lawyer to pick from 2–3 structured options or write a short override before Approve; every DD extraction gets a deep-linked quote citation for 2-second verification.
2. **Integrate into the "Practice Web" (proposal):** don't treat docs as isolated files. Show integration with the matter lifecycle (billing, conflicts, calendars, DMS — iManage/Clio) and use **MCP (Model Context Protocol)** to securely bridge their private VDR ↔ Claude. Make it an active platform, not a playground.
3. **Professional-indemnity & privilege defense (case study):** risk-allocation framework — where Claude's responsibility ends and the attorney's professional liability begins. Frame as a **Drafting & Audit Accelerator, NOT an automated decision-maker**. Preserve attorney-client privilege during ingestion (zero-data-retention calls).
- Helper nudge: present the Exception Report as a **front-end artifact**, not raw markdown/JSON, for the demo.

## Remaining challenge deliverables (Wed 29 Jul)
- [x] (1) Client proposal — DOCX built (`Harrow-Vale-Proposal.docx`), now incorporating the 3 gaps + roadmap.
- [ ] (2) Live demo — build a front-end artifact of the Exception Report + DD report (Trust-but-Verify UX).
- [x] (3) Next steps — in proposal (roadmap: definitives-consistency skill, MCP/DMS integration, Enterprise).
- [ ] (4) Public case study — Anthropic-facing "how Claude solved it" (add risk-allocation/privilege framing).

## Proposal revision — storage / marketplace / versioning (added §3.6)
Made distribution concrete: skills stored in the firm's private GitHub repo (each skill = a plugin bundling SKILL.md + JSON contract + reference baseline/checklist + golden dataset; conventions in CLAUDE.md / .claude/rules/); advertised via a **private plugin marketplace** (`.claude-plugin/marketplace.json`) — the firm's single shelf; installed with `/plugin marketplace add harrowvale/legal-skills` then the `/plugin` menu; **version control** = semantic version + changelog per plugin, eval gate must pass before a version ships, `/plugin marketplace update` to pull v2, pin a known-good version for live matters; private repo access (10 lawyers + Tom admin), every version keeps its eval report. PIPELINE.md synced to match. Sources: docs.claude.com/en/docs/claude-code/plugin-marketplaces.

## Pipeline made end-to-end (eval → version → marketplace)
Added to the prototype so the harness demonstrably *facilitates* publishing, not just grading:
- `.claude-plugin/marketplace.json` — the firm's private marketplace catalogue (lists both skills as plugins w/ version + lastEval).
- `src/publish.py` — the promotion step: runs the eval gate; on PASS auto-bumps the semantic version, updates `CHANGELOG.md`, and inserts/refreshes the plugin entry in marketplace.json; on FAIL refuses to publish. Demonstrated: passing build 1.0.0→1.1.0 published; a simulated regressed build is BLOCKED (version holds). One command ties evals + versioning + marketplace insertion together.
- README + PIPELINE.md updated; zip repackaged (45 files).

**Architecture clarification (per Aiio):** the durable *product* is the governed pipeline (contract discipline + eval harness/gate + marketplace/versioning/governance). The two skills are the first content through the gate. Any future skill plugs in by supplying a SKILL.md + contract schema + golden dataset; scaffolding is reusable, evaluator scoring needs light per-skill tuning.

## Chat transcripts (key excerpts)
_(full Tom Harrow + Helper transcripts captured above in findings)_
