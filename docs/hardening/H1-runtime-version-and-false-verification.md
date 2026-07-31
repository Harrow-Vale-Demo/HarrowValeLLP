# H1 — Out-of-date runtime, plus an install check that confirmed itself

**Found:** 2026-07-29 to 2026-07-30
**Class:** Verification integrity
**Status:** Closed
**Severity:** Was high — it cost most of two sessions and produced a wrong change to a client-facing deliverable.

> Backfilled for completeness. Full narrative lives in `docs/cowork/cowork-session-notes.md`
> and `PROGRESS.md`; this is the hardening summary.

---

## Symptom

Plugins appeared to be simultaneously installed and not installed. `/term-sheet-review` never
appeared under `/`, so the install was assumed broken and repeatedly redone.

## Two independent causes

### 1. The runtime was ~170 releases behind

`claude --version` reported **2.0.51**; current was ~2.1.218. On that build `/reload-plugins`
and `claude plugin list` did not exist, and plugin skills were not registering. Updating to
**2.1.140** resolved it, and `/term-sheet-review:term-sheet-review` then fired.

The machine runs NixOS, so the update had to go through the nix configuration — `nixos-rebuild
switch` alone was insufficient, because the version is pinned in nixpkgs and the pin had to move
first.

### 2. The install check read the shelf and reported it as the machine

`.claude/settings.local.json` carried a pre-approved shell command that reads
`.claude-plugin/marketplace.json` and prints its contents. Asked to check installed plugins, an
agent that could not run `claude plugin list` ran that instead, and printed the result under the
heading **"Installed plugins:"**.

That file is the *shelf*. It prints identically on a machine with nothing installed. Because it
sat in the allow-list it ran with no prompt, so the substitution was invisible.

The tell, in hindsight: `mock-skill v1.0.0` appeared as "installed" the moment it was committed
to the shelf.

## The compounding error

While diagnosing, a plausible-sounding explanation was adopted without checking it: *these
plugins ship no `commands/` directory, therefore they have no slash-command invocation.*

**That is false.** Skills in a `skills/` directory are exposed as `/plugin-name:skill-name`;
`commands/` is only the older flat-file form of the same mechanism.

The false claim was written into five files — including
`deliverables/lawyer-installation-guide.md`, which is client-facing — before anyone checked it
against the documentation. Undone in commit `df64f1a`.

## Fixes applied

- [x] Runtime updated to 2.1.140 via the nix configuration
- [x] The self-confirming command removed from `.claude/settings.local.json`
- [x] The false claim undone in all five files, each now carrying a
      `Verified against Claude Code 2.1.140, 2026-07-30` stamp
- [x] Verification guidance corrected to the `/plugin` panel — **Installed** vs **Discover**
- [ ] Add the `/plugin` panel method alongside the `claude plugin list` line in
      `.claude/skills/publish-hv-skill/SKILL.md` (the CLI command is valid on 2.1.140 and worth
      keeping; the panel should sit beside it)

## Lessons

1. **A verification that can pass on a broken machine is not a verification.** Ask what the
   check would print if the thing were absent. If the answer is "the same", it is not a check.
2. **Never accept an agent's summary of system state as evidence.** Read the surface that owns
   the state — here, the `/plugin` panel.
3. **No invocation syntax goes into a document until someone has typed it and watched it work.**
   Adopted as a standing rule for the repo.
4. **Record the version you verified against.** A stamp in the text is what lets the next reader
   know when it went stale, and it is cheap.
5. **A confident wrong explanation is more expensive than no explanation.** The version gap was
   discoverable in one command; the plausible theory delayed finding it and did collateral damage
   to a deliverable on the way.
