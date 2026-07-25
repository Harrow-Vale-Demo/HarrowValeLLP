# Harrow & Vale — Approved Skills

Private, versioned home for Claude skills vetted for firm-wide use. See `CONTRIBUTING.md` for the full approval and versioning process.

## Install

```
/plugin marketplace add harrow-vale/harrow-vale-skills
/plugin install term-sheet-review@harrow-vale-skills
```

## Update to the latest approved version

```
/plugin marketplace update harrow-vale-skills
/plugin update term-sheet-review
```

## What's available

| Skill | Version | Description |
|---|---|---|
| `term-sheet-review` | 1.0.0 | Reviews a term sheet against the firm's DD checklist, flags deviations/unusual clauses, produces a plain-English summary. |

## Governance

Every skill here is approved by Tom Harrow (process) and Priya Vale (substantive due-diligence accuracy) before it's published or updated — see `CONTRIBUTING.md`. Firm-wide conventions all skills must follow live in `.claude/rules/`.
