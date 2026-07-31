# H2 — Desktop upload shipped `SKILL.md` without its `reference/` files

**Found:** 2026-07-30
**Class:** Packaging integrity
**Status:** Closed on the affected copy; the preventive check is still outstanding
**Severity:** High. A silent breach of Rule 1, invisible in the output.

> Backfilled for completeness. Full narrative in `PLAN.md` and
> `docs/cowork/cowork-session-notes.md`; this is the hardening summary.

---

## Symptom

The hand-uploaded Claude for Desktop copy of `term-sheet-review` contained **only `SKILL.md`**.
Its four reference files never arrived:

- `reference/dd-checklist.md` ← Priya's ground-truth checklist
- `reference/term-extraction.md`
- `reference/standard-terms.md`
- `reference/output-template.md`

`SKILL.md` points at `reference/dd-checklist.md` in five separate places.

## Why it mattered more than it looked

The skill still ran. It still produced a confident, well-formatted review. Without the checklist
file it fell back on general knowledge of what a DD checklist contains — inventing categories,
which is exactly what Rule 1 forbids.

**Nothing in the output distinguished that from a correct run.** No error, no warning, no missing
section. This is the failure mode that matters most in this project: not a crash, but a
plausible answer produced without the ground truth.

Evidence at the time, from file counts by `creatorType` in one session bundle:

| creatorType | Skills | Supporting files |
|---|---|---|
| `anthropic` | docx (61), pptx (56), xlsx (53), skill-creator (18), pdf (12) | full trees |
| `user` | **term-sheet-review (1)**, nix-purity (1) | `SKILL.md` only |

So the mechanism *can* carry folders. The fault was specific to the hand-upload route.

## Fix

`skill-creator`'s `scripts/package_skill.py` zips a whole skill folder into a `.skill` archive
that installs in one click. Packaged and installed successfully: all 11 files present on disk,
`reference/`, `examples/` and `templates/` intact, verified by directory listing rather than by
asking the model.

### A divergence found on the way

The first packaging attempt **failed validation**:

```
Unexpected key(s) in SKILL.md frontmatter: argument-hint.
Allowed: allowed-tools, compatibility, description, license, metadata, name
```

`argument-hint` is valid for a Claude Code **plugin** skill and rejected by the Desktop
**personal** skill schema. So byte-identical `SKILL.md` cannot ship to both surfaces. It was
stripped from the packaged copy only; the repo source is unchanged.

That divergence is worth knowing before promising cross-surface consistency to the client.

## Outstanding

- [ ] **Packaging check in the gate** — assert every file referenced by `SKILL.md` exists in the
      shipped tree. Partially addressed on PR #10; confirm it covers this case.
- [ ] **Frontmatter check against the Desktop schema** — otherwise a skill can pass the gate and
      still be unpackageable for Desktop, discovered at upload time.
- [ ] **Self-check in the skill** — have it confirm it can read `reference/dd-checklist.md` and
      **refuse to produce a review if it cannot**, rather than falling back on general knowledge.
      A loud refusal is worth more to a partner than a plausible answer. This is the single
      highest-value item, because it protects against every future variant of this failure rather
      than this one instance.
- [ ] **One source of truth for both surfaces**, rather than two hand-synced copies. Whether
      Desktop can subscribe to the marketplace directly is still unanswered.

## Lessons

1. **Silent degradation is the dangerous failure.** A skill that stops working announces itself;
   a skill that keeps working without its ground truth does not.
2. **A skill that depends on a file should verify the file is there.** Cheap, local, and turns an
   invisible failure into an obvious one.
3. **Verify packaging on disk, not by asking.** The directory listing is evidence; model output
   about its own configuration is not.
4. **The gate scored a recording, and the packaging never reached it.** Same boundary as H1 and
   H3 — see [INDEX.md](INDEX.md).
