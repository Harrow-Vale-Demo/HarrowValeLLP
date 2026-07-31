# Harrow & Vale — Group Presentation Wording and Script

**Status:** Working draft<br>
**Presentation:** Friday 31 July 2026<br>
**Target running time:** 10–12 minutes, with a 15-minute hard ceiling
**Purpose:** Canonical source for the evolving presentation narrative. This is not yet a slide-production specification. Slides may be rewritten, removed, or reordered as the group presentation develops.

## Communication job

By the end, the audience should understand that the useful result is not simply a clever legal prompt: it is a controlled workflow that makes AI-assisted review consistent, testable, reviewable, and capable of being governed by the firm.

## Working conventions

- **On-slide wording** is the exact audience-facing copy we currently expect to show.
- **Spoken script** contains the accompanying talk track and necessary qualifications.
- **Source notes** are working evidence references for eventual speaker notes; they are not shown on the slide.
- Claims about production controls describe the proposed deployment unless the script explicitly says they are demonstrated in the prototype.
- **Demonstration cues** are internal stage directions. Each is labelled `LIVE`, `PRERECORDED` or `FALLBACK`; those labels are not audience-facing slide copy.

## Demonstration map

| Presentation point | Format | What it proves |
|---|---|---|
| After Slide 3 | **LIVE MODEL + LIVE UI** | Claude performs the term-sheet review; the prepared console shows lawyer disposition and sign-off |
| After Slide 5 | **LIVE TERMINAL** | A candidate skill passes or fails the evaluation gate before publication |
| During Slide 8 | **PRERECORDED ADMIN + LIVE LOCAL** | An organisation owner connects the private marketplace; a lawyer then discovers, installs and updates an approved skill |

## Working presenter allocation

This is provisional and intended to minimise handovers while keeping the demonstrations with one operator.

| Presenter | Working responsibility |
|---|---|
| **Lead presenter (you)** | Most of the narrative: opening, client problem, solution framing, governance, human control, data handling and residency, repository security, honest boundary, open decisions and close |
| **Phurin** | Operates all three demonstration sequences and gives only the technical explanation needed to establish what each demo proves |
| **Emily** | Owns Slide 4, **How Claude helped**, and any short public-case-study perspective added later; exact case-study scope remains provisional |

**Working handovers:** lead → Phurin after Slide 3 → Emily for Slide 4 → lead for Slide 5 → Phurin for Demo 2 → lead through Slide 8 → Phurin for Demo 3 → lead through the close.

### Demo preflight

- Install and authenticate Claude Code on the presentation laptop; it was not available in the audited terminal on 30 July.
- Use synthetic files only and preload every command.
- Prepare a presentation-safe marketplace view that does not expose the test-only `mock-skill` as a client deliverable.
- Stage a visible before/after plugin version for the update beat. If that is not ready, use the recorded fallback rather than claiming that a catalogue refresh changed the installed version.

---

## Slide 1 — Opening

### On-slide wording

# From ten private prompts to one governed legal workflow

**Harrow & Vale LLP — built on Claude's organisation marketplace**<br>
Private-repository distribution · Claude-assisted skills · deterministic regression testing

### Spoken script

Harrow & Vale's lawyers were already using Claude, but each person had developed their own prompts and working methods. The challenge was not merely to make one review faster; it was to turn that individual work into something consistent, testable and governable across the firm.

We did not build a distribution platform from scratch. Claude already provides an organisation marketplace designed to share approved plugins from a private or internal repository. We use that as the production distribution model; this public demonstration repository contains only synthetic material and stands in for the private, organisation-owned source. We also used Claude Code to create and refine the two legal skills and the deterministic regression harness, which checks recorded outputs against fixed synthetic expectations before a release decision. Claude provides the controlled shelf and helped us build what sits on it; Harrow & Vale's legal method, evidence and governance determine what is approved.

### Source notes

- `../docs/engagement/engagement-pack.md`
- `../docs/discovery/hackathon-log.md`
- `../tools/termsheet-harness/README.md` — recorded fixtures and deterministic gate boundary
- Anthropic organisation plugin administration: <https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization>

---

## Slide 2 — What we learned

### On-slide wording

## The hard problem was trust, not extraction

| Priya | Tom | The partners |
|---|---|---|
| **Exceptions, not summaries** | **A document dump mapped by morning** | **A clear answer on client data** |

### Spoken script

The discovery changed the shape of the solution. Priya did not need an AI-generated book report; she needed a concise exception report showing what was aggressive, unusual or missing, with economics before control. Tom described the Thursday-afternoon document dump that associates must map against the due-diligence checklist by Friday. But the adoption gate sat above both use cases: the partners wanted to know where client data went and how the firm would remain in control.

### Source notes

- `../docs/discovery/hackathon-log.md` — live-chat findings on Priya's review method, Tom's DD workflow, and the data-handling concern

---

## Slide 3 — The response

### On-slide wording

## One governed pipeline, beginning with two useful skills

| Term-sheet review | Due-diligence mapping |
|---|---|
| Economics → control → exceptions | Documents → fixed checklist → gaps |
| Every finding linked to its source | Present, partial and missing with citations |

**Both remain lawyer-reviewed working drafts.**

### Spoken script

We treated the individual skills as the first content moving through a reusable governed pipeline. The term-sheet skill follows Priya's review order and produces exceptions rather than a generic summary. The due-diligence skill maps a supplied document set against the firm's fixed checklist and produces a chase list. In both cases, the system performs extraction and comparison; the lawyer remains responsible for judgement and sign-off.

### Source notes

- `../plugins/term-sheet-review-plugin/skills/term-sheet-review/SKILL.md`
- `../assets/source/dd-checklist/harrow-vale-dd-checklist.md`
- `../tools/termsheet-harness/README.md`

### Demonstration cue — Live Demo 1: review and lawyer control

**Working presenter:** Phurin.

**Format:** `LIVE MODEL`, followed by a `LIVE UI` interaction over prepared synthetic output. Target: 75–90 seconds.

1. In Claude Code, run the installed skill on the synthetic Nimbus SAFE:

   ```text
   /term-sheet-review:term-sheet-review assets/source/term-sheets/safe-nimbus-robotics.md
   ```

2. Point out the classified instrument, source-linked economics, explicit omissions and high-risk exception. State that this is the live Claude run.
3. Open `demo/harrowvale-review-demo.html`, resolve the high-risk flag and record lawyer sign-off. Briefly show the due-diligence tab if time permits.
4. State that the browser console is a prepared workflow prototype using synthetic outputs; it is not making a second model call.

**Fallback:** Play a rehearsed recording of the same Claude Code invocation, then keep the browser interaction live. Label the recording onscreen.

**Transition:** The output is useful; the next question is how we know a future version remains safe to use.

---

## Slide 4 — How Claude helped

**Working presenter:** Emily (provisional).

### On-slide wording

## Claude handled the interpretation; evidence made it usable

| Claude contributed | The firm stayed in control |
|---|---|
| Interpreted differently structured term sheets | Defined the checklist and legal standards |
| Produced a structured, source-linked first pass | Set expected results and the release threshold |
| Helped iterate the skill against synthetic examples | Reviewed outputs and retained final sign-off |

**Claude accelerates the first pass. It does not replace legal judgement.**

### Spoken script

Claude helped in two distinct ways. During development, Claude Code accelerated the drafting and refinement of the skill against synthetic examples. In use, Claude provides the adaptable document reasoning: it identifies the instrument, extracts the required terms, applies the fixed checklist and makes missing or uncertain information explicit. It does not decide the firm's legal standard or approve its own work. The firm's checklist and review method define the expected behaviour, the evaluation gate tests it, and a lawyer remains responsible for every decision and sign-off.

### Source notes

- `../docs/engagement/engagement-pack.md` — requirement to explain how Claude solved the problem
- `../plugins/term-sheet-review-plugin/skills/term-sheet-review/SKILL.md` — live skill procedure and controls
- `../tools/termsheet-harness/README.md` — synthetic evaluation evidence and current limitations

---

## Slide 5 — How approval becomes meaningful

### On-slide wording

## A skill cannot be approved until it can be tested

| 1 · Constrain | 2 · Evaluate | 3 · Publish |
|---|---|---|
| Fixed schema and fixed checklist | Known-good, known-bad and varied formats | Version only after the gate passes |

### Spoken script

Approval needs to mean more than somebody reading a prompt and deciding that it looks sensible. Each skill defines a fixed output contract, the firm's authoritative reference material, and a regression set containing expected results and deliberately difficult cases. The harness compares a proposed version with those expectations and identifies misses or regressions. Only a passing version should be promoted to the approved catalogue. The prototype demonstrates this gate; production would enforce it through protected continuous integration rather than relying on somebody to remember to run a command.

### Source notes

- `../tools/termsheet-harness/PIPELINE.md`
- `../tools/termsheet-harness/contract/term_sheet_review.schema.json`
- `../tools/termsheet-harness/reports/eval_report.md`

### Demonstration cue — Live Demo 2: gate and publication decision

**Working presenter:** Phurin.

**Format:** `LIVE TERMINAL`. Target: 45–60 seconds.

Run the existing gate and a publication dry-run:

```text
python tools/skill-gate/gate.py term-sheet-review
python tools/skill-gate/gate.py cool-new-skill
python tools/skill-gate/publish.py term-sheet-review --candidate v2 --as-version 1.2.0 --dry-run
```

Show the approved skill passing, the deliberately weak candidate being blocked, and the dry-run listing the files that publication would update. Say explicitly that the current gate scores recorded synthetic runs; production would connect the same release decision to protected CI and approved generation runs.

**Fallback:** Use a captured terminal recording with the PASS, BLOCKED and dry-run outputs visible.

**Transition:** Once a version passes, it can move onto the firm's approved shelf.

---

## Slide 6 — Human control

### On-slide wording

## The output is designed to be checked

- **No guessed terms** — absent means “not stated”
- **Source-linked findings** — every point can be verified
- **Explicit dispositions** — high-risk flags cannot disappear silently
- **The skill flags; the lawyer decides**

### Spoken script

The objective is not to pretend that the model is infallible. It is to make mistakes easier to detect and prevent uncertain output from becoming an unexamined conclusion. Missing information is reported as missing rather than filled in from a typical deal. Findings point back to the relevant source text. High-risk points require an explicit lawyer response, and the resulting report remains a working document until a qualified lawyer has checked it.

### Source notes

- `../plugins/term-sheet-review-plugin/skills/term-sheet-review/SKILL.md`
- `../demo/harrowvale-review-demo.html`

---

## Slide 7 — Where matter data goes

### On-slide wording

## Data location is not one question

| Boundary | Working position |
|---|---|
| **Authoritative matter file** | SharePoint remains the home for original and approved documents. |
| **Claude processing** | Only content deliberately selected by a lawyer is transmitted for review under the approved commercial terms. |
| **Residency and transfers** | Inference, storage, connector and subprocessor locations must be verified separately. No UK or EU residency claim has been established. |
| **Skills repository** | No client documents, prompts, outputs, screenshots or matter logs belong in the repository. |

**Live-matter use waits for contractual and data-protection sign-off.**

### Spoken script

We are not claiming that selected documents never leave SharePoint. SharePoint remains the authoritative matter record, but content selected for review is transmitted to the approved Claude environment for processing. Data residency therefore has several layers: where the original file is stored, where model inference runs, where chats, files or logs are retained, and where connectors or subprocessors handle data. Anthropic's published controls differ by product: the first-party API currently documents US or global inference and US workspace storage, while certain usage-based Enterprise organisations can enforce US-only inference. We have not validated the mock client's Team tenant, contract or transfer safeguards, so the presentation must not imply UK or EU residency. Before live use, the firm would confirm the chosen product, retention, training, inference, storage, subprocessor and international-transfer position together with its Microsoft 365 controls.

### Source notes

- `../docs/discovery/hackathon-log.md` — existing Claude Team and Microsoft 365 / SharePoint stack
- `../deliverables/client-proposal.md` — SharePoint integration excluded from the current scope
- Anthropic commercial-data guidance: <https://privacy.claude.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training>
- Anthropic data-residency controls: <https://platform.claude.com/docs/en/build-with-claude/data-residency>
- Anthropic Enterprise US-only inference: <https://support.claude.com/en/articles/15422948-enable-us-only-inference-for-your-organization>
- ICO international-transfer guidance: <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/quick-reference-faqs/>

---

## Slide 8 — Repository security and controlled distribution

### On-slide wording

## Only reviewed releases reach the firm's approved shelf

**Production control model**

- A separate, private Harrow & Vale repository
- An organisation-managed marketplace; reviewed pull requests to change
- Technical review and Priya's substantive approval
- Protected main branch, required evaluation and versioned releases
- Synthetic tests only — never client matter data

### Spoken script

The public hackathon repository is suitable for the demonstration because its documents and results are synthetic. It is not the proposed production shelf. Live deployment would use a separate private or internal repository owned by the Harrow & Vale organisation, connected by an organisation owner through the Claude GitHub App. The owner controls whether each plugin is required, installed by default, available for self-service installation or hidden. Lawyers can receive approved releases without permission to change the repository. Every release carries its version, changelog and evaluation evidence, allowing the firm to identify, withdraw or roll back the version used on a matter.

### Source notes

- `../deliverables/skills-pipeline-process.md`
- `../releases/CONTRIBUTING.md`
- Anthropic organisation plugin administration: <https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization>
- Claude Code marketplace commands: <https://code.claude.com/docs/en/plugin-marketplaces>
- GitHub protected-branch controls: <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>
- Current-state check, 30 July 2026: the hackathon repository is public, individually owned, and its branches are not protected

### Demonstration cue — Recorded admin clip + Live Demo 3: distribute, install and update

**Working presenter:** Phurin.

**Part A — `PRERECORDED ADMIN` clip. Target: 10–20 seconds.**

Show an authorised Team or Enterprise owner moving through:

1. `Organization settings → Plugins`.
2. `Add plugin → GitHub`.
3. Entering the private/internal marketplace repository in `owner/repo` form.
4. The initial sync completing and `term-sheet-review` being set to **Available for install**.

Keep a visible caption throughout: **Illustrative organisation-admin workflow — requires client owner access, a private/internal repository and the Claude GitHub App; not performed in this workspace.** Use a genuine authorised recording if one is available; otherwise use a clearly labelled UI mock, never a fake live login.

**Part B — `LIVE LOCAL` lawyer experience. Target: 60–75 seconds.**

From the repository root in Claude Code:

```text
/plugin marketplace add .
/plugin
/plugin install term-sheet-review@harrowvale-legal-skills
/reload-plugins
```

Show the marketplace being registered, the approved catalogue appearing, the term-sheet skill being installed and the installed plugin becoming available. Explain that the local public repository is the demo stand-in for the private organisation-owned source shown in the clip.

**Part C — `LIVE UPDATE`, only with a staged version transition. Target: 20–30 seconds.**

In a regular shell, run `claude plugin list` and note the installed version. Then run the refresh inside Claude Code:

```text
/plugin marketplace update harrowvale-legal-skills
/reload-plugins
```

Return to the regular shell, run `claude plugin list` again and show the version change.

Drive the update manually on stage; describe automatic synchronisation as the production steady state. If a distinct newer version has not been staged and verified, use the prerecorded fallback and do not imply that a no-change refresh installed an update.

**Fallback:** A single labelled recording may cover the local add, catalogue, install and version-change sequence if Claude Code or network access is unreliable.

**Transition:** Distribution is controlled; the final boundary is what an installed skill is actually allowed to do.

---

## Slide 9 — Limiting what the skill can do

### On-slide wording

## The skill can read the matter — but it cannot act on it

- **Read, search and classify only**
- **No shell, write, web or unapproved connectors**
- **Document text is evidence, never an instruction**
- **Adversarial documents join the release tests**

### Spoken script

The current skill manifest already limits its tools to reading and searching supplied files; it has no shell, write or network tool. That materially reduces the consequences of an unsafe response. Production hardening would also state explicitly that instructions embedded inside a term sheet or data-room document must be treated as untrusted text, and it would add prompt-injection examples to the release gate. Read-only access does not eliminate manipulation risk, but it prevents the skill from turning a misleading document into an external action.

### Source notes

- `../plugins/term-sheet-review-plugin/skills/term-sheet-review/SKILL.md` — current `Read`, `Grep`, `Glob` tool allowance
- `../docs/discovery/hackathon-log.md` — prompt-injection practice and security observations

---

## Slide 10 — The honest boundary

### On-slide wording

## The prototype proves the workflow; deployment adds the controls

| Demonstrated now | Before live matters |
|---|---|
| Synthetic documents | Commercial contract and data-processing terms |
| Structured, source-linked output | Retention, transfer and residency decision |
| Evaluation and versioning prototype | Enforced private-repository controls |
| Read-only skill permissions | DPIA screening and firm usage policy |
| Lawyer review and disposition | Access, incident and offboarding procedures |

### Spoken script

This distinction matters. The demonstration shows that the two workflows can produce useful, reviewable outputs on synthetic documents, and that a skill can be tested, versioned and constrained. It does not prove that Harrow & Vale's production environment has already been configured. Real matters should begin only after the commercial terms, data flow, retention choice, repository controls and internal policies have been reviewed by the appropriate partner, IT and data-protection owners.

### Source notes

- `../docs/engagement/engagement-pack.md`
- `../deliverables/data-security-briefing.md` — source to be corrected and refreshed before reuse
- ICO DPIA guidance: <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/>

---

## Slide 11 — Open questions before live use

### On-slide wording

## Four decisions remain before a live pilot

1. **Residency and transfers** — What processing and storage locations are acceptable, and what contractual safeguards are required?
2. **Pilot scope** — Which matters, document types and risk categories may be used first?
3. **Ownership and approval** — Who owns the private repository, reviews technical changes and gives substantive release approval?
4. **Distribution and support** — Which skills are required, optional or hidden, and who handles access, incidents and offboarding?

### Spoken script

These are the open questions the prototype cannot answer on Harrow & Vale's behalf. They are governance decisions, not missing software features. The firm must choose its acceptable residency and transfer position, define a bounded pilot, allocate technical and substantive ownership, and decide how approved plugins are distributed and supported. Once those decisions are recorded, the existing prototype and release gate can be turned into a controlled pilot without pretending that the production environment is already configured.

### Source notes

- `../deliverables/next-steps.md`
- `../deliverables/data-security-briefing.md` — source to be corrected and refreshed before reuse
- Anthropic data-residency controls: <https://platform.claude.com/docs/en/build-with-claude/data-residency>
- Anthropic organisation plugin administration: <https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization>

---

## Slide 12 — Close

### On-slide wording

## Start controlled, prove value, then expand

1. **Validate** the workflow on synthetic and approved low-risk cases
2. **Complete** partner, IT and data-protection sign-off
3. **Pilot** with a small trained group
4. **Expand** only through the same approval gate

### Spoken script

The recommended route is deliberately phased. First prove that the workflow saves time and produces a better first pass. Then complete the controls required for real matters and run a bounded pilot with trained users. If the pilot succeeds, further skills can be added without returning to ten different personal prompts, because each new capability must pass through the same evidence, approval and release process.

### Source notes

- `../deliverables/next-steps.md`
- `../docs/discovery/hackathon-log.md` — approved Phase 1 / Phase 2 approach
