# Term-Sheet Review Skill — Installation Guide
## For Harrow & Vale Lawyers

---

## What This Skill Does

The **term-sheet review** skill reads a venture term sheet and produces a structured first-pass review:

- **Extracts** key economic terms (valuation, liquidation preference, board composition, etc.)
- **Flags** deviations from market standard, unusual clauses, and omissions
- **Maps** documents against Priya's fixed DD checklist (when run with `--dd-room`)

The output is a consistent, plain-English memo you verify before use. The skill follows the same structure every time, regardless of whether the term sheet is a SAFE, priced round, or convertible note.

---

## Before You Start

You'll need:
- [ ] Claude Code installed on your machine
- [ ] Access to the firm's private GitHub repository (ask Tom if you don't have it)
- [ ] Your NZ/firm credentials for authentication

---

## Step 1: Install the Skill

Open Claude Code and run:

```
/install-plugin https://github.com/harrow-vale/approved-skills
```

You'll be prompted to authenticate with GitHub. Use your firm credentials.

Once installed, you'll see confirmation:
```
Installed: term-sheet-review v1.1.0
```

---

## Step 2: Using the Skill

### Basic Review (Single Term Sheet)

```
/term-sheet-review path/to/term-sheet.md
```

Or, if the file is on SharePoint/your desktop:
```
/term-sheet-review "C:\Users\YourName\Documents\NimbusRobotics-SAFE.pdf"
```

The skill will output:
- **Part A** — Key economic terms (table with values and source references)
- **Part B** — Flags for your attention (🔴 Review / 🟡 Note / ⚪ Omission)
- **Part C** — DD checklist coverage (all 28 items, with status)
- **Part D** — Summary for the lawyer (3-5 sentences, action-oriented)

### Full DD Coverage (With Data Room)

If you have a folder of DD documents (cap table, articles, contracts, etc.):

```
/term-sheet-review path/to/term-sheet.md --dd-room path/to/data-room-folder/
```

This additionally:
- Maps each checklist item to the document that satisfies it
- Flags missing documents
- Cross-checks figures between documents (e.g., term sheet vs cap table)

---

## Step 3: Understanding the Output

### Severity Flags

| Flag | Meaning |
|------|---------|
| 🔴 **Review** | Materially off-market or investor-favourable beyond standard. Look at this first. |
| 🟡 **Note** | Present and worth a glance, but not alarming. |
| ⚪ **Omission** | A term you'd normally expect that is absent. |

### What "Not stated" Means

If a term shows `Not stated`, it means the document doesn't include that information. The skill **never guesses** — if it's not in the document, it tells you it's missing.

### Checklist Statuses

| Status | Meaning |
|--------|---------|
| **PRESENT** | Document found that satisfies this item |
| **MISSING** | No document provided for this item |
| **N/A** | Item doesn't apply (e.g., no group structure for a single company) |

---

## Step 4: Verifying the Output

**Remember:** This is a first-pass review. You must:

1. **Check the extracted terms** against the source document
2. **Read the flagged items** and apply your judgement
3. **Add your own observations** before sending to the client/partner
4. **Sign off** as the reviewing solicitor

The skill saves you the grunt work of extraction. The legal analysis is yours.

---

## Step 5: Updating the Skill

When a new version is released, you'll receive a notification. To update:

```
/update-plugins
```

To check your current version:

```
/skill-info term-sheet-review
```

---

## Troubleshooting

### "Skill not found"

Run `/install-plugin` again. You may have been logged out of GitHub.

### "Permission denied"

Contact Tom Harrow to check your repository access.

### "File not found"

- Check the file path is correct
- Use quotes around paths with spaces: `"C:\My Documents\file.md"`
- The skill can read `.md`, `.txt`, and `.pdf` files

### Output looks wrong

- Check you're running the latest version (`/update-plugins`)
- If the term sheet is in an unusual format, the skill may struggle — raise with the technical team

---

## Getting Help

| Issue | Contact |
|-------|---------|
| How to use the skill | This guide, or ask a colleague |
| Skill not working | Marcus Ade (technical reviewer) |
| Access issues | Tom Harrow |
| Feature requests | Open a GitHub Issue |

---

## Quick Reference

```
# Basic review
/term-sheet-review path/to/file.md

# With DD room
/term-sheet-review path/to/file.md --dd-room path/to/folder/

# Check version
/skill-info term-sheet-review

# Update
/update-plugins
```

---

*Guide version 1.0 · July 2026 · Questions? Ask Tom or Marcus.*
