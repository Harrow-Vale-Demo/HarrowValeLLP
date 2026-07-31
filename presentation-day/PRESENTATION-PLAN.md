# Presentation Working Plan — Friday 31 July 2026

> Emily's continuation plan. Written 2026-07-31 so work can resume from a known state.
> Pick up at **"Next actions"** — everything above it is context you already have.

---

## Where things stand

**Presentation:** Friday 31 July 2026 (**today**), 10–12 minutes, 15-minute hard ceiling.
**Emily owns:** Slide 4, "How Claude helped" — ~60–75 seconds, immediately after Live Demo 1.
**Presenters:** Lea leads (written as "you" in Lee's Claude's drafts) · Phurin runs all three
demos · Emily takes Slide 4.

### Decision already made

**Keep the wording honest.** No more coding before the presentation. Claims are pegged to what
is actually merged, using the status tags below. This was a deliberate choice, not a fallback.

### The status gradient — do not upgrade these on stage

| Artefact | Reality | Safe verb |
|---|---|---|
| Held-out test (Vantor Health) | ✅ real, on disk | "we wrote", "we tested against" |
| Hardening records H1–H5 | ✅ real, in `docs/hardening/` | "we documented" |
| Packaging check (the silent failure) | 🟡 written, **unmerged** | "we've written" — never "our gate blocks this" |
| Verbatim checklist check | 📄 spec only | "we've specified" |
| `situate` skill | ⬜ **does not appear as an available skill** | say nothing; treat as unverified |

---

## Files that matter

| File | What it's for |
|---|---|
| `slide-04-emily-pack.md` | **Emily's script.** Spoken tracks (60s and 75s variants), the silent-failure wording, Q&A defences, do-not-say list |
| `governance-and-testing-story.md` | The full hardening narrative — Phurin → Emily relay, why testing was necessary, future testing, Priya/Tom mapping |
| `group-presentation-wording-and-script.md` | The whole-group script and demo map (not Emily's to edit) |
| `harrow-vale-presentation.html` | The deck itself |

---

## Next actions

### Before presenting

- [ ] Read `slide-04-emily-pack.md` end to end once, out loud, with a timer.
- [ ] **Choose the spoken track:** primary (~60s, no hardening) or the variant (~75s, includes
      the reliability beat). If not certain, take the primary — Slide 5 needs its air.
- [ ] Decide whether the silent-failure beat goes in at all. It is the strongest 15 seconds
      available *if delivered briskly*; it is a wobble if delivered hesitantly.
- [ ] **Two free wins, currently unclaimed** — both true, both in the brief, both cost nothing:
      say **"four formats"** (the brief only asked for three), and say **"test-driven from the
      start"**.
- [ ] Demo prep: `git status` against origin **first**. A stale checkout serves an old catalogue
      and looks exactly like a broken install.

### After presenting

- [ ] Merge the presentation branch to master (see below).
- [ ] Then, in order of value: merge `feature/gate-packaging-check`, then
      `feature/handover-02-artefacts`, then decide on `feature/merge-dd-checklist` and
      `feature/situate-skill`.
- [ ] Investigate why `situate` doesn't register as a skill before claiming it anywhere.

---

## The branch plan

**Problem:** five branches carry unmerged work. Presentation material must reach master without
dragging any of it along.

**Why this is easy:** every presentation file already on master is **byte-identical** to the
current branch. Only two files are new or changed, and only one of them is presentation
material.

| File | State |
|---|---|
| `presentation-day/slide-04-emily-pack.md` | untracked — **new, wanted** |
| `presentation-day/governance-and-testing-story.md` | untracked — **new, wanted** |
| `presentation-day/PRESENTATION-PLAN.md` | untracked — **new, wanted** (this file) |
| `docs/cowork/cowork-session-notes.md` | modified — **not presentation material, leave behind** |

**The plan:**

1. Branch from `origin/master` directly — not from the current branch.
2. Add only the three `presentation-day/` files above.
3. Commit, push, PR into master.

That merges cleanly with zero risk of pulling in unmerged work, because it contains nothing but
three new files in a directory that already exists on master.

**Leave behind:** the `docs/cowork/cowork-session-notes.md` modification stays on
`feature/handover-02-artefacts` and can be dealt with after the presentation.

---

## Unmerged branch register — for after today

| Branch | Ahead | Contains | Risk if merged blind |
|---|---|---|---|
| `feature/gate-packaging-check` | 8 | Packaging check, slash-command drift fix | Low — most valuable to land |
| `feature/situate-skill` | 4 | `situate` v0.1.0, H4/H5 docs | Medium — skill doesn't register; diagnose first |
| `feature/merge-dd-checklist` | 3 | Phurin's dd-checklist plugin | Medium — deliberately off-shelf |
| `feature/handover-02-artefacts` | 2 | Hardening docs, held-out fixture | Low |
| `dd-checklist-marketplace-plugin-and-fixed-json` | 1 | Phurin's original manifest fix | Superseded by Lee's refactor |

**The lesson this register exists to prevent:** unmerged work is indistinguishable from work
never done. Phurin fixed H5 correctly on 29 July; it was rediscovered from scratch on 31 July
because the branch never landed.

---

## If someone asks a hard question

**"Is the packaging check live?"**
> "It's written, not yet merged. What's merged is the diagnosis and the held-out test. We'd
> rather tell you where the line is than blur it."

**"Did Claude get anything wrong?"**
> "Yes, and that's the part worth telling you about." → then H2 or H3 from
> `slide-04-emily-pack.md`.

**"Is this just a prompt?"**
> "A prompt lives on one lawyer's machine and nobody knows which version anyone is using. This
> is a versioned skill with a fixed checklist, a scored gate before release, and one approved
> shelf all ten lawyers install from."
