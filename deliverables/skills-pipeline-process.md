# Approved Skills Pipeline
## Harrow & Vale LLP — Governance, Versioning & Distribution

---

## Overview

This document describes how a Claude skill gets from an idea to all ten lawyers' machines, and what stops a bad one getting there. It exists to answer four questions:

1. **Consistency** — do all ten lawyers use the same version?
2. **Quality** — has this version been tested, and can we see the result?
3. **Auditability** — six months on, can we show why we trusted it?
4. **Security** — who can change what reaches the firm?

The reusable asset is not any individual skill. It is the gate every skill passes through.

---

## 1. The shape of it

```
  Author a skill              Prove it                    Ship it
 ┌───────────────┐  golden   ┌──────────────┐  version   ┌────────────────────┐
 │ SKILL.md +    │──────────▶│ gate.py      │───────────▶│ marketplace +      │
 │ golden labels │  labels   │ threshold    │  on PASS   │ firm policy        │
 └───────────────┘           │ no-regression│   only     │ → ten lawyers      │
                             └──────────────┘            └────────────────────┘
                                    │ on FAIL
                                    └──▶ nothing is written
```

### Repository structure

```
HarrowValeLLP/
├── .claude-plugin/marketplace.json     # the shelf: HarrowVale Legal Skills
├── .claude/
│   ├── settings.json                   # marketplace + skills for repo contributors
│   └── skills/publish-hv-skill/        # the publishing workflow, as a skill
├── .github/workflows/skill-gate.yml    # CI: the enforcement
├── plugins/
│   ├── term-sheet-review-plugin/       # one directory per skill
│   └── cool-new-skill/
├── tools/
│   ├── skill-gate/                     # gate.py, publish.py, check_published.py
│   │   ├── fixtures/<skill>/           # golden labels + recorded runs, one dir per skill
│   │   └── scorers/                    # the graders the gate applies
│   ├── termsheet-harness/              # term-sheet contract, references, DD mapper, reports
│   └── org-policy/                     # the managed policy pushed to lawyers
└── releases/<skill>/
    ├── CHANGELOG.md
    └── v<version>/gate-report.json     # the evidence, per version
```

---

## 2. Roles

| Role | Person | Responsibility |
|---|---|---|
| **Skill author** | any associate | Writes the skill, the golden labels, and the recorded run |
| **Technical reviewer** | Marcus Ade | Reviews the skill and, critically, whether the golden labels are the right test |
| **Approving partner** | Priya Vale | Owns the standard — the DD checklist and the golden labels are hers |
| **Publisher / repository admin** | Tom Harrow | Runs the gate, publishes, manages the firm policy |

The important line: **Priya owns the labels, and the skill moves to meet them — never the reverse.** Retuning a golden label so a skill passes is the one change that would hollow out the whole pipeline, so it is called out explicitly in review.

---

## 3. What a skill must ship with

A skill is not "done" when it produces good output. It is done when it can be *graded*:

| Artefact | Where | Why |
|---|---|---|
| `SKILL.md` | `plugins/<skill>/skills/<skill>/` | the skill itself |
| Golden labels | `tools/skill-gate/fixtures/<skill>/golden.json` | the known-correct answers |
| A recorded run | `tools/skill-gate/fixtures/<skill>/runs/<version>.json` | what the skill actually produced |
| A registered metric | `tools/skill-gate/gate.py` | how the two are compared |

A skill with no registered gate cannot be published. That is enforced in code, not convention: `publish.py` refuses.

> **Current limitation, stated plainly.** Recorded runs are captured fixtures, not live model calls at gate time. This buys deterministic, zero-cost CI. The seam to make it live is a single function — `run_generator()` in `tools/skill-gate/generator_adapter.py` — pointed at `claude -p`. Until that is switched on, the gate proves *a recorded output* meets the standard, not that today's model call does.

---

## 4. Approval process

### 4.1 A new skill or a new version

1. **Author** works on a branch (`feature/<skill>-<change>`)
2. **Author** writes or extends the golden labels, and records a run named for the version they intend to ship
3. **Author** runs the gate:
   ```bash
   python tools/skill-gate/gate.py <skill>
   ```
   Or, inside a Claude Code session in the repository, uses the wrapper skill:
   ```bash
   /publish-hv-skill <skill>
   ```
4. **On FAIL** — nothing is published. The author fixes the skill, not the test.
5. **On PASS** — publish:
   ```bash
   python tools/skill-gate/publish.py <skill>
   ```
6. **Author** opens a pull request. CI re-runs the gate independently.
7. **Technical reviewer** within 2 working days: is the skill sound, and are the labels the right test?
8. **Approving partner** within 3 working days: does this meet practice standards?
9. **Publisher** merges to `master` and tags the release.

### 4.2 Emergency fixes

For a skill producing materially wrong output on live matters:

1. Author fixes on `hotfix/<skill>-<issue>`
2. The gate still runs. There is no bypass, and none should be added — a hotfix that regresses something else is not a fix.
3. Technical reviewer expedites, same day
4. Approving partner notified, may approve asynchronously
5. Patch version published

If a skill must be stopped immediately, the fast path is to disable it by policy rather than to rush an ungated version.

### 4.3 What is not allowed

- Publishing on a gate FAIL, for any reason
- Editing a stored `gate-report.json`, or hand-editing a version number
- Adjusting golden labels so a skill passes
- Pushing directly to `master`

The first three are refused by `check_published.py`. The fourth is prevented by branch protection.

---

## 5. Versioning

Semantic versioning: MAJOR.MINOR.PATCH.

| Change | When |
|---|---|
| **MAJOR** | Breaking change to output format or behaviour |
| **MINOR** | New extraction fields or coverage, non-breaking |
| **PATCH** | Bug fixes, wording, clarifications |

**The version published is the version graded.** The author names the recorded run for the version they intend to ship; the gate grades that run; `publish.py` writes that same version everywhere. There is no separate bump step that can be got wrong.

A version lives in five places, all written by `publish.py` in one action:

| Location | Purpose |
|---|---|
| `plugins/<skill>/.claude-plugin/plugin.json` | **the pin users update against** |
| `.claude-plugin/marketplace.json` | the shelf listing |
| `SKILL.md` version marker | so the skill reports its own version in output |
| `releases/<skill>/CHANGELOG.md` | the human record |
| `releases/<skill>/v<version>/gate-report.json` | the evidence |

Two mechanics worth knowing:

- **`plugin.json` wins.** If the version is set in both `plugin.json` and the marketplace entry, `plugin.json` is authoritative at install time. A mismatch means the shelf advertises a version nobody receives.
- **The version string is the update trigger.** Lawyers receive a new version only when that string changes. This is also why a hand-edited version is dangerous: it disseminates without evidence, which is exactly what `check_published.py` refuses.

Release folders under `releases/` are immutable. `publish.py` will not overwrite one.

---

## 6. Enforcement

Four layers. Only the last two are enforcement rather than good practice:

| Layer | Stops | Bypassable by |
|---|---|---|
| `publish.py` as the only sanctioned publisher | honest mistakes | editing a version by hand |
| `check_published.py` | hand-edited versions | not running it |
| **CI on every pull request** | both of the above | pushing straight to `master` |
| **Branch protection on `master`** | that too | nobody |

The marketplace serves whatever is on `master`. So the question is never "did the author run the gate?" — it is **"can anything reach `master` without the gate passing?"** With `skill-gate` as a required status check and direct pushes disallowed, the answer is no, and the author's discipline stops being part of the security model.

CI's blocking check is deliberately narrow: *is every version on the shelf backed by a passing gate result?* It is **not** "does every recorded run pass" — an author mid-iteration has a failing run by definition, and that must not block everyone else.

For the strongest form, point the marketplace at a `release` branch that only CI can move:

```json
"source": { "source": "github", "repo": "<org>/<repo>", "ref": "release" }
```

A direct push to `master` then reaches nobody.

---

## 7. Distribution

The firm's shelf is a marketplace named **`harrowvale-legal-skills`**, catalogued in `.claude-plugin/marketplace.json` at the repository root.

### Reaching the ten lawyers

Skills are pushed by **managed settings** — organisation policy that sits above user, project, and local settings and cannot be overridden by the user. The firm decides which skills its lawyers use; a lawyer cannot quietly switch to their own fork mid-deal.

```json
{
  "extraKnownMarketplaces": {
    "harrowvale-legal-skills": {
      "source": { "source": "github", "repo": "<org>/<repo>" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": {
    "term-sheet-review@harrowvale-legal-skills": true
  }
}
```

The same JSON deploys through any standard channel: the claude.ai admin console, Intune or Group Policy, Jamf or Kandji on macOS, or a file on disk. See `tools/org-policy/` for the policy and an apply script.

`autoUpdate` is what makes a new version — and a newly published skill — actually arrive. Third-party marketplaces default to auto-update off; without this flag a lawyer's catalogue never refreshes and a new skill stays invisible to them.

### What a lawyer does

Nothing, to receive a skill. To check what they have: the `/plugin` panel, which separates plugins that are installed on the machine from those merely sitting on the shelf. To pull an update immediately rather than waiting: `/plugin marketplace update harrowvale-legal-skills`, then `/reload-plugins`.

A skill can be invoked either in plain language — Claude picks the right skill from its description — or with a namespaced slash command in the form `/plugin-name:skill-name <args>`. Both routes reach the same skill.

Updates are checked shortly after a session starts, and the running session keeps the versions it launched with — so a review never shifts under a lawyer mid-document.

### Adding a skill firm-wide

A skill on the shelf is available; a skill named in the policy is *deployed*. Adding one firm-wide is a one-line policy change. That line is deliberate: it is the written record of a human decision that the firm's lawyers should have this skill.

---

## 8. Pinning for live matters

A matter that must not shift can pin a known-good version. Because plugin sources accept an exact commit SHA, a review run today can be reproduced exactly months later — which is what makes the audit answer defensible rather than approximate.

---

## 9. Retirement

1. **Deprecation notice** added to the skill (60-day warning)
2. **Skill remains functional** during the period
3. **Removed** from the policy, then from the shelf, with final notification
4. **History retained** — `releases/` and Git history are never pruned, so a review produced by a retired skill can still be explained

---

## 10. Audit and compliance

For any approved version the firm can produce:

| Question | Answer lives in |
|---|---|
| What did this version do? | `releases/<skill>/v<version>/` and the Git tag |
| Was it tested, and how did it score? | `releases/<skill>/v<version>/gate-report.json` |
| Against what standard? | `tools/skill-gate/fixtures/<skill>/golden.json` — Priya's labels |
| Who approved it? | the pull request, and `releases/<skill>/CHANGELOG.md` |
| Which version produced a given review? | the version marker in the skill's own output |
| Who could have changed it? | branch protection and repository access logs |

**Retention:** all versions retained indefinitely in Git history.

---

## 11. Access control

| Level | Who | Permissions |
|---|---|---|
| **Policy-managed** | all ten lawyers | receive and use approved skills; no repository access needed |
| **Read** | associates | view the repository |
| **Write** | authors | branches and pull requests |
| **Merge** | Tom | merge to `master`, tag releases |
| **Admin** | Tom, Priya | repository settings, branch protection, firm policy |

Most lawyers need no repository access at all, which is the point: the distribution channel is policy, not a code checkout.

---

## 12. Current state versus production

Honest accounting of what is built and what is a deployment decision:

| Item | Now | For production |
|---|---|---|
| Gate, publisher, consistency check | working | as-is |
| CI workflow | written | make `gate` a required status check |
| Branch protection | not enabled | enable on `master` |
| Repository visibility | public, for demonstration | private, firm read access — policy JSON unchanged |
| Recorded runs | captured fixtures | switch `run_generator()` to live calls |
| `strictKnownMarketplaces` | not set | set, to restrict lawyers to the firm's shelf |

---

*Document version 2.0 · July 2026 · Owner: Tom Harrow*
