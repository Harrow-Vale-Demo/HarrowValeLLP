# Org Policy — Distributing Approved Skills to the Firm

Two ways a lawyer gets the firm's skills. They are not alternatives to argue
about; they answer different questions.

| Route | Who it fits | Where it lives |
|---|---|---|
| **Project settings** | anyone working *in this repository* | `.claude/settings.json` (committed) |
| **Managed policy** | the ten lawyers, who never clone anything | this folder, applied per machine |

For the demo you want the **managed policy**. Lawyers don't clone repositories,
and "the firm decided you have this skill" is the actual client story.

---

## Why managed settings and not project settings

Managed settings sit at the top of Claude Code's precedence order — above local,
project, and user settings — and cannot be overridden by the user. That is the
whole point: the firm decides which skills its lawyers use, and a lawyer cannot
quietly switch to their own fork mid-deal. It also reaches the nine lawyers who
will never clone this repository, which project settings cannot.

The **shape is the same in every scope**, per the published settings schema — an
object keyed by name, not an array. Getting this wrong is silent: Claude Code
strips invalid entries and carries on with the rest, so a mis-shaped policy looks
applied and does nothing.

```jsonc
"extraKnownMarketplaces": {
  "harrowvale-legal-skills": {
    "source": { "source": "github", "repo": "f7-rage-gremlin/HarrowValeLLP" },
    "autoUpdate": true
  }
}
"enabledPlugins": { "term-sheet-review@harrowvale-legal-skills": true }
```

`extraKnownMarketplaces` entries accept exactly `source`, `installLocation`,
`autoUpdate`, and `lastUpdated`. A `github` source accepts `repo`, plus optional
`ref`, `path`, and `skipLfs`.

Two of those are worth knowing about:

- **`ref`** pins the shelf to a branch or tag. Point it at a `release` branch that
  only CI can move and a direct push to `master` no longer reaches anyone — the
  strongest form of the enforcement story.
- **`path`** points at a `marketplace.json` elsewhere in the repo, defaulting to
  `.claude-plugin/marketplace.json`. So a marketplace *can* live in a
  subdirectory when named this way, even though the `/plugin marketplace add
  owner/repo` shorthand only ever looks at the root.

---

## Apply it

[`managed-settings.json`](managed-settings.json) is the policy.
[`install-org-policy.ps1`](install-org-policy.ps1) applies it to the Windows
policy registry key Claude Code reads.

Default target is **HKCU** — current user only, no administrator rights, trivially
reversible. That is the same mechanism a real IT department drives through Group
Policy or Intune, just scoped to one user, which is what makes it demoable on
three ordinary laptops.

Inspect first:

```bash
powershell -File tools/org-policy/install-org-policy.ps1 -Show
```

Apply, then restart Claude Code:

```bash
powershell -File tools/org-policy/install-org-policy.ps1
```

Remove it again:

```bash
powershell -File tools/org-policy/install-org-policy.ps1 -Uninstall
```

Add `-Machine` to cover all users on the box; that needs an elevated shell.

The script validates the JSON and refuses to apply an empty or malformed policy,
because a broken policy is worse than none.

### Other delivery mechanisms

The same JSON, unchanged, deploys through any of these — worth naming in the
proposal, because it is how the firm would really do it:

| Mechanism | Target |
|---|---|
| claude.ai admin console | server-managed, all org members at sign-in |
| Intune / Group Policy | `HKLM\SOFTWARE\Policies\ClaudeCode`, value `Settings` |
| Jamf / Kandji (macOS) | `com.anthropic.claudecode` managed preferences |
| File-based | `C:\Program Files\ClaudeCode\managed-settings.json` |

---

## How a skill actually arrives on nine other machines

"It just shows up" is six links in a chain. Five are settled; one you must test.

| # | Link | What makes it happen | Silently fails if |
|---|---|---|---|
| 1 | The skill is good enough | gate PASS | blocked — nothing is published, by design |
| 2 | It is on the shelf | `publish.py` writes `marketplace.json` | never pushed to `master` |
| 3 | The shelf is registered on their machine | `extraKnownMarketplaces` in the policy | policy not applied, or mis-shaped |
| 4 | Their copy of the catalogue is current | `autoUpdate: true` on the entry | auto-update off — **a new skill is invisible, because their catalogue predates it** |
| 5 | The plugin is installed | `enabledPlugins` | see below |
| 6 | It is loaded in the session | `/reload-plugins`, or next launch | the running session keeps the versions it started with |

**Link 4 is the one people miss.** A newly published skill is a change to
`marketplace.json`. Until a lawyer's local copy of the catalogue refreshes, the
new skill does not exist as far as their Claude Code is concerned — no amount of
`enabledPlugins` will conjure it. That is what `autoUpdate: true` is for, and why
third-party marketplaces defaulting to auto-update **off** would quietly break
this.

**Link 5 needs testing, not trusting.** Anthropic's documentation is not
consistent on whether a managed `enabledPlugins` entry installs a plugin with no
user action at all:

- the settings reference describes `enabledPlugins` as pre-installing and
  force-enabling for all users, and the plugin guide says managed-scope plugins
  "are installed by administrators via managed settings";
- but the plugin guide also says a plugin from an external source that is only
  *enabled* by settings "doesn't load until the team member installs it", and the
  suggestions page states flatly that "Claude Code never installs a plugin
  automatically. The user always confirms."

So budget for **one confirmation per person, once**, the first time. Test it:

```bash
powershell -File tools/org-policy/install-org-policy.ps1
```

Restart Claude Code, then:

```bash
claude plugin list
```

If `term-sheet-review` is listed, link 5 is automatic. If it reports the plugin
as not installed and offers a `claude plugin install` command, run it once — and
know that a genuinely new skill will need the same one-time confirmation.

Either way the demo is safe, because **the impressive beat does not depend on
link 5**. Get everyone installed during setup; then the *update* — the version
moving on all three machines after Tom publishes — flows through links 4 and 6
with nobody typing anything.

### The honest limit

A skill the policy does not name will not appear, however good it is. It sits on
the shelf, visible under `/plugin` → Discover, uninstalled. That is governance
working as intended: the shelf is what passed the gate, the policy is what the
firm decided its lawyers get. Adding a skill firm-wide is a one-line policy change
pushed the same way as any other IT policy — and that line is the record of a
human decision, which is exactly what Priya would want to be able to point at.

## The command check

After applying the policy and restarting, each person confirms what they have:

```bash
claude doctor
```

Lists every loaded setting, which scope it came from, and any validation errors —
so you can point at the screen and show the policy is in force rather than
asserting it.

```bash
claude plugin list
```

Lists installed plugins with their versions. This is the check that makes an
update visible: run it before and after a publish and the version moves.

For a belt-and-braces check that does not depend on any tooling, run the skill
itself — `cool-new-skill` signs every answer `Triaged by: cool-new-skill v<x.y.z>`.
A lawyer can therefore always tell which approved version produced a given
answer, which is the auditability point Priya cares about.

---

## Two things to verify before you present

1. **`autoUpdate` timing.** Claude Code checks for updates after session start
   with a random delay of up to ten minutes, and the running session keeps the
   versions it launched with. Do not wait for it on stage — drive the live beat
   with `/plugin marketplace update harrowvale-legal-skills` then
   `/reload-plugins`, and describe auto-update as the steady state.
2. **The repo is public.** `f7-rage-gremlin/HarrowValeLLP` is a public GitHub
   repository, so no authentication is needed and the demo is frictionless. It
   also contradicts the private, access-controlled repository described in the
   security briefing. Say so once, plainly, and note that the only change for
   production is making the repo private and granting the firm read access — the
   policy JSON is identical.

## Deliberately not set

`strictKnownMarketplaces` would lock users to this marketplace alone. It is the
right production hardening for a law firm and worth describing in the proposal,
but **do not set it on your own machines for the demo** — it would cut off every
other marketplace you use, including the Negative Zero one.
