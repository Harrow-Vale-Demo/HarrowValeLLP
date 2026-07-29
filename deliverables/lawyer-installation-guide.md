# Term-Sheet Review Skill — User Guide
## For Harrow & Vale Lawyers

---

## What this skill does

The **term-sheet review** skill reads a venture term sheet and produces a structured first-pass review:

- **Extracts** the key economic terms (valuation or cap, discount, liquidation preference, board and consent rights, pro-rata, founder vesting, legal fees)
- **Flags** deviations from market standard, unusual clauses, and omissions
- **Checks** the document set against Priya's fixed due-diligence checklist — all 28 items, every time
- **Reconciles** figures across documents when you point it at a data room

The output is a consistent, plain-English memo that you verify before use. The structure is the same every time, whether the document is a SAFE, a priced round, a convertible loan note, or a terse seed summary.

---

## Getting the skill

### If the firm has set it up for you — nothing to do

Approved skills are pushed to your machine by firm policy. You do not need a GitHub account, a copy of any repository, or an install step. Open Claude Code and the skill is there.

To confirm:

```bash
claude plugin list
```

You should see `term-sheet-review` with a version number. If you do, skip to **Using the skill**.

### If you are setting it up yourself

Add the firm's skills marketplace once:

```bash
/plugin marketplace add f7-rage-gremlin/HarrowValeLLP
```

Install the skill:

```bash
/plugin install term-sheet-review@harrowvale-legal-skills
```

Activate it in the current session:

```bash
/reload-plugins
```

`/plugin` on its own opens a browser where you can see everything on the firm's shelf.

> If Claude tells you `/plugin` is not available in your environment, use the plugin browser in the Claude desktop app instead, or ask Tom to push the skill to you by policy.

---

## Using the skill

The simplest way is to ask for it in plain English. Claude selects the right skill from what you are asking for:

> Review this term sheet against our DD checklist: `NimbusRobotics-SAFE.pdf`

To invoke it explicitly, skills are named `plugin:skill`:

```bash
/term-sheet-review:term-sheet-review path/to/term-sheet.md
```

Paths with spaces need quotes:

```bash
/term-sheet-review:term-sheet-review "C:\Users\YourName\Documents\NimbusRobotics-SAFE.pdf"
```

### With a data room

If you have a folder of DD documents — cap table, articles, contracts, leases:

```bash
/term-sheet-review:term-sheet-review path/to/term-sheet.md --dd-room path/to/data-room/
```

This additionally maps each checklist item to the document that satisfies it, flags missing documents, and cross-checks figures between the term sheet and the cap table.

---

## Reading the output

The memo always has four parts:

| Part | Contents |
|---|---|
| **A** | Key economic terms — a table of values, each with its source in the document |
| **B** | Flags for your attention |
| **C** | DD checklist coverage — all 28 items, each with a status |
| **D** | Summary — 3 to 5 sentences, action-oriented |

### Severity flags

| Flag | Meaning |
|---|---|
| 🔴 **Review** | Materially off-market or investor-favourable beyond standard. Look here first. |
| 🟡 **Note** | Present and worth a glance, not alarming. |
| ⚪ **Omission** | A term you would normally expect, absent from the document. |

### Checklist statuses

| Status | Meaning |
|---|---|
| **PRESENT** | A document was found that satisfies this item |
| **MISSING** | No document provided for this item |
| **N/A** | The item does not apply — with the reason stated |

Every one of the 28 items appears with a status. None are ever silently dropped. When you run the skill against a single term sheet rather than a full data room, most items will read `N/A (not a DD document set)` — that is correct, not a failure.

### What "Not stated" means

If a term shows `Not stated`, the document does not contain it. The skill never guesses, never infers from comparable deals, and never fills a gap with a typical figure. An honest gap is the intended behaviour.

---

## Before you sign off

This is a first-pass review, not advice. You must:

1. **Check the extracted terms** against the source document — Part A gives you the clause reference for each
2. **Read the flagged items** and apply your judgement
3. **Add your own observations**
4. **Sign off** as the reviewing solicitor

The skill saves you the extraction. The legal analysis is yours.

---

## When a new version arrives

New versions are published only after passing the firm's evaluation gate, and reach you automatically — usually within a few minutes of a session starting. If a version arrives mid-session, Claude will prompt you to run:

```bash
/reload-plugins
```

To pull an update immediately rather than waiting:

```bash
/plugin marketplace update harrowvale-legal-skills
```

To see which version you are on:

```bash
claude plugin list
```

**Why the version matters.** If you are asked six months from now why a review said what it said, the version is the answer. Every approved version has a stored evaluation report in the firm's repository, so the firm can always show the evidence behind the skill you used.

---

## Other approved skills

The firm's shelf carries more than this one skill, and it grows. Anything approved appears the same way, with no action from you. To see everything available:

```bash
/plugin
```

---

## Troubleshooting

### "Skill not found" or the skill does not appear

Run `/reload-plugins`. If that does not fix it, check it is installed with `claude plugin list`. If it is missing entirely, contact Tom — it is a policy issue, not something you can fix locally.

### The version looks out of date

```bash
/plugin marketplace update harrowvale-legal-skills
```

then `/reload-plugins`.

### "File not found"

- Check the path
- Quote paths containing spaces: `"C:\My Documents\file.md"`
- The skill reads `.md`, `.txt`, and `.pdf`

### The output looks wrong

Check your version first (`claude plugin list`). If you are current and the output is still wrong, this matters — raise it with Marcus. A wrong output is a gap in the firm's test set, and the fix is to add your document as a test case so no future version can regress on it.

### Diagnosing configuration

```bash
claude doctor
```

Lists every setting in effect and where it came from. Useful to send to Tom if something is off.

---

## Getting help

| Issue | Contact |
|---|---|
| How to use the skill | This guide, or a colleague |
| Output looks wrong | Marcus Ade (technical reviewer) |
| Skill missing or not updating | Tom Harrow |
| Feature requests | Open a GitHub issue tagged `enhancement` |

---

## Quick reference

```bash
# Which version am I on?
claude plugin list

# Review a term sheet
/term-sheet-review:term-sheet-review path/to/file.md

# Review with a data room
/term-sheet-review:term-sheet-review path/to/file.md --dd-room path/to/folder/

# Pull updates now
/plugin marketplace update harrowvale-legal-skills

# Apply them to this session
/reload-plugins

# Browse the firm's approved skills
/plugin
```

---

*Guide version 2.0 · July 2026 · Questions? Ask Tom or Marcus.*
