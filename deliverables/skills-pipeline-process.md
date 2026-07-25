# Approved Skills Pipeline
## Harrow & Vale LLP — Governance & Versioning Process

---

## Overview

This document describes the approval, versioning, and distribution process for Claude skills used by Harrow & Vale LLP. The goal is to ensure:

1. **Consistency** — All 10 lawyers use the same vetted skills
2. **Quality** — Skills are tested and approved before deployment
3. **Auditability** — Changes are versioned and traceable
4. **Security** — Skills are stored in a private, access-controlled repository

---

## 1. Repository Structure

Skills are stored in a private GitHub repository:

```
harrow-vale-approved-skills/
├── .claude-plugin/
│   └── marketplace.json          # Plugin registry
├── plugins/
│   └── term-sheet-review-plugin/
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin manifest (name, version, author)
│       └── skills/
│           └── term-sheet-review/
│               ├── SKILL.md      # Skill definition
│               ├── reference/    # Supporting files
│               ├── templates/    # Output templates
│               └── examples/     # Worked examples
├── CHANGELOG.md                  # Version history
└── README.md                     # Installation instructions
```

---

## 2. Roles & Responsibilities

| Role | Person | Responsibility |
|------|--------|----------------|
| **Skill Author** | Any associate | Develops and tests new skills or updates |
| **Technical Reviewer** | Marcus Ade (or designated associate) | Reviews code/prompt quality, tests against samples |
| **Approving Partner** | Priya Vale | Final sign-off on any skill entering production |
| **Repository Admin** | Tom Harrow | Manages access, merges approved changes, tags releases |

---

## 3. Approval Process

### 3.1 New Skill Development

1. **Author creates skill** in a feature branch (`feature/skill-name`)
2. **Author tests** against at least 3 representative documents
3. **Author opens Pull Request** with:
   - Description of what the skill does
   - Test results (screenshots or output files)
   - Any dependencies or requirements
4. **Technical Reviewer** reviews within 2 working days:
   - Does it follow firm conventions?
   - Does it handle edge cases?
   - Are outputs consistent?
5. **Approving Partner** reviews within 3 working days:
   - Does it meet practice standards?
   - Is the output format appropriate?
   - Any confidentiality concerns?
6. **Repository Admin** merges to `main` and tags a release

### 3.2 Skill Updates

1. **Author creates update** in a feature branch (`update/skill-name-v1.1`)
2. **Author documents changes** in `CHANGELOG.md`
3. **Same review process** as new skills
4. **Version bump** in `plugin.json` (see versioning below)
5. **Release notification** sent to all users

### 3.3 Emergency Fixes

For critical bugs or security issues:
1. **Author fixes** in `hotfix/skill-name-issue`
2. **Technical Reviewer** expedites review (same day)
3. **Approving Partner** notified but can approve async
4. **Immediate release** with patch version bump

---

## 4. Versioning

Skills use **Semantic Versioning** (MAJOR.MINOR.PATCH):

| Version Change | When |
|----------------|------|
| **MAJOR** (2.0.0) | Breaking changes to output format or behaviour |
| **MINOR** (1.1.0) | New features, additional extractions, non-breaking |
| **PATCH** (1.0.1) | Bug fixes, typo corrections, clarifications |

**Version is recorded in:**
- `plugins/[skill]/. claude-plugin/plugin.json` → `"version": "1.0.0"`
- `.claude-plugin/marketplace.json` → `"version": "1.0.0"`
- Git tag → `v1.0.0`

---

## 5. Changelog

All changes are documented in `CHANGELOG.md` at the repository root:

```markdown
# Changelog

## [1.1.0] - 2026-08-01
### Added
- Founder vesting schedule extraction
- Legal fees & expenses extraction

### Changed
- Updated standard-terms baseline for new fields

## [1.0.0] - 2026-07-22
### Added
- Initial release of term-sheet-review skill
- Support for SAFE, priced round, convertible note
- DD-room coverage report with --dd-room flag
```

---

## 6. Installation & Updates

### First-Time Installation

Lawyers install the skill from the private repository:

1. Open Claude Code
2. Run: `/install-plugin https://github.com/harrow-vale/approved-skills`
3. Authenticate with GitHub (SSO if enabled)
4. Skill appears in available commands

### Receiving Updates

When a new version is released:

1. **Notification** sent via email/Slack by Repository Admin
2. Lawyer runs: `/update-plugins`
3. New version is active immediately

### Checking Current Version

Run: `/skill-info term-sheet-review`

Output:
```
term-sheet-review v1.1.0
Last updated: 2026-08-01
Author: Emily Donovan
Status: Approved (Priya Vale, 2026-07-29)
```

---

## 7. Retirement & Deprecation

If a skill is retired:

1. **Deprecation notice** added to skill (60-day warning)
2. **Skill remains functional** during deprecation period
3. **Removal** after 60 days, with final notification
4. **Archived** in `archive/` folder for reference

---

## 8. Audit & Compliance

For compliance and audit purposes:

- All changes are tracked in Git history
- Pull Requests record reviewer approvals
- Release tags mark production versions
- Repository access is logged by GitHub

**Retention:** All versions retained indefinitely in Git history.

---

## 9. Access Control

| Access Level | Who | Permissions |
|--------------|-----|-------------|
| **Read** | All 10 lawyers | View skills, install, use |
| **Write** | Authors (associates) | Create branches, open PRs |
| **Merge** | Repository Admin (Tom) | Merge to main, tag releases |
| **Admin** | Tom Harrow + Priya Vale | Manage access, settings |

---

## 10. Support

**Questions about skills:** Ask the author or technical reviewer
**Access issues:** Contact Tom Harrow
**Feature requests:** Open a GitHub Issue tagged `enhancement`
**Bug reports:** Open a GitHub Issue tagged `bug`

---

*Document version: 1.0 · Last updated: July 2026 · Owner: Tom Harrow*
