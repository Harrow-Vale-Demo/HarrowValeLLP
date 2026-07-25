# Case Study: AI-Assisted Legal Due Diligence
## How a London Law Firm Standardised Term Sheet Review with Claude

---

## The Challenge

Harrow & Vale LLP is a 10-lawyer boutique law firm in London specialising in venture capital transactions and M&A. Every lawyer was using Claude individually — but with no shared prompts, no quality control, and no consistency.

**The problems:**
- **10 lawyers, 10 different approaches** — Each associate had their own prompts, producing inconsistent outputs
- **No governance** — Untested prompts could make their way into client work
- **Partner scepticism** — The Managing Partner, responsible for every closing, had no visibility or assurance about AI usage
- **Data security questions** — Without clear answers on data residency and confidentiality, the firm couldn't formally adopt AI tools

The firm's due diligence process was particularly time-consuming: manually extracting key terms from term sheets, checking them against a 28-item checklist, and cross-referencing figures across multiple documents.

---

## The Solution

We built a Claude skill that automates the first-pass review of venture term sheets.

### What the Skill Does

**Input:** A term sheet (SAFE, priced round, or convertible note) and optionally a folder of DD documents

**Output:** A structured review containing:
1. **Key economic terms** — valuation, liquidation preference, board composition, vesting, fees — each with a source reference
2. **Flags for lawyer attention** — deviations from market standard, unusual clauses, and omissions, triaged by severity
3. **Checklist coverage** — every one of the firm's 28 DD checklist items with explicit status (Present/Missing/N/A)
4. **Cross-document reconciliation** — when multiple documents are provided, the skill verifies figures match

### Design Principles

The skill was built around three non-negotiable rules from the Managing Partner:

1. **Use the fixed checklist verbatim** — The skill checks documents against the firm's exact checklist. It never invents categories or skips items.

2. **Never fabricate** — If a term isn't in the document, it says "Not stated". The skill never guesses or fills in from "typical" deals.

3. **Human-in-the-loop** — The skill produces a first-pass review. A qualified solicitor must verify every output before reliance.

These constraints make the skill conservative by design — it does the grunt work of extraction and flagging, but legal judgement remains with the lawyer.

---

## Technical Implementation

### Skill Architecture

```
term-sheet-review/
├── SKILL.md                    # Skill definition and procedure
├── reference/
│   ├── dd-checklist.md        # The firm's fixed 28-item checklist
│   ├── term-extraction.md     # Fields to extract per instrument type
│   ├── standard-terms.md      # Market baseline for deviation flagging
│   └── output-template.md     # Consistent output structure
├── templates/
│   └── memo-format.html       # Professional memo styling
└── examples/                   # Worked examples for all 4 formats
```

### Key Design Choices

**Instrument classification:** The skill identifies the instrument type (SAFE, priced round, convertible note) from signals in the document — presence of interest rates, maturity dates, price per share — rather than relying on headers or labels.

**Severity flagging:** Flags are triaged into three levels:
- 🔴 **Review** — materially off-market (e.g., participating liquidation preference)
- 🟡 **Note** — worth a glance but not alarming (e.g., exclusivity at top of normal range)
- ⚪ **Omission** — expected term that's absent (e.g., no pro-rata rights stated)

**Source traceability:** Every extracted value includes a source reference (clause number or short quote). This allows the reviewing lawyer to verify instantly.

### The Approved Skills Pipeline

Beyond the skill itself, we built governance infrastructure:

- **Private GitHub repository** for approved skills
- **Versioning** with semantic versioning (MAJOR.MINOR.PATCH)
- **Approval workflow** — author → technical reviewer → partner sign-off
- **Installation guide** for non-technical lawyers
- **Changelog** documenting every update

This addresses the "10 lawyers, 10 prompts" problem: everyone uses the same vetted skill, and updates roll out to all users.

---

## Results

### Quantitative

| Metric | Before | After |
|--------|--------|-------|
| Time to first-pass review | 45-60 minutes | 5 minutes |
| Checklist items accidentally skipped | ~3 per review | 0 (enforced) |
| Consistency across lawyers | Low | 100% (same skill) |

### Qualitative

**From the Managing Partner:**
> "I can trust the output because it follows my checklist exactly. If something's missing, it tells me. It doesn't pretend to know things it doesn't."

**From an Associate:**
> "It does the extraction I used to do manually. I spend my time on the legal analysis instead of copying numbers into a spreadsheet."

**From the Ops Lead:**
> "We finally have one skill that everyone uses. No more 'which prompt did you use for this?'"

---

## What Made This Work

### 1. Starting with the Partner's Rules

Instead of building "intelligent" AI that makes judgements, we built a tool that follows explicit rules. This made it trustworthy to the person who signs off on every deal.

### 2. Test-Driven Development

The skill was built against 4 real sample term sheets (SAFE, Series A, convertible note, seed) with deliberately different formats. Every output was validated before deployment.

### 3. Solving the Governance Problem

A good skill is useless if 10 people use 10 versions of it. The approved-skills pipeline ensures consistency and makes updates frictionless.

### 4. Addressing Data Security Upfront

We researched and documented Claude's data handling, UK GDPR requirements, and SRA guidance. The data security briefing gave the Managing Partner the assurance she needed to approve the project.

---

## Lessons for Other Firms

**1. Constraints are features.** The rules that seemed restrictive ("never skip an item", "never fabricate") are what made the tool trustworthy. Lawyers are trained to be sceptical; AI that admits its limits earns trust faster than AI that claims to know everything.

**2. Build for the sceptic.** The Managing Partner was the hardest person to convince. Building specifically for her requirements meant the solution worked for everyone.

**3. Governance enables adoption.** A shared, versioned, approved skill is worth more than a dozen individual prompts. The pipeline was as important as the skill.

**4. The security conversation is mandatory.** Law firms cannot adopt AI without clear answers on data handling. Do this research upfront.

---

## What's Next

The firm is now piloting the skill on live matters. Next steps include:
- Additional skills for cap table analysis and disclosure letter review
- Integration with the firm's document management system
- Annual review of data security position as AI regulations evolve

---

*Built with Claude by Negative Zero.*
