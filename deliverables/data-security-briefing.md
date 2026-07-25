# Data Security & Confidentiality Briefing
## Claude AI for Harrow & Vale LLP

**Prepared for:** Priya Vale, Managing Partner
**Date:** July 2026
**Classification:** Internal — Partner Review

---

## Executive Summary

This briefing addresses the data security, confidentiality, and regulatory compliance position for Harrow & Vale's use of Claude AI (Anthropic) for internal legal workflows. The key conclusions are:

1. **No training on client data** — Claude Enterprise/Team plans explicitly exclude customer content from model training
2. **UK GDPR compliant** — With appropriate deployment choices, the firm can maintain compliance
3. **SRA obligations preserved** — Existing confidentiality rules apply; no AI-specific regulations exist, but solicitor accountability remains absolute
4. **Data residency options available** — EU/UK processing achievable via AWS Bedrock or Google Vertex AI

**Recommendation:** Proceed with Claude Team or Enterprise under the firm's existing information governance framework, with the specific controls outlined below.

---

## 1. Data Training — Will Anthropic Train on Our Client Data?

**Answer: No.**

Anthropic's Commercial Terms (which govern Claude Team, Enterprise, and API access) explicitly state:

> "Anthropic may not train models on Customer Content from Services."

This applies to:
- Claude for Work/Team (Standard and Premium tiers)
- Claude Enterprise
- API usage under Commercial Terms

**Key distinction:** Consumer plans (Free/Pro/Max) have different policies — as of October 2025, consumer users are opted in to training by default. This does **not** apply to business/enterprise customers.

**Verification:** Anthropic's Trust Center confirms commercial customers are excluded from training provisions. The firm should retain a copy of the applicable Commercial Terms for audit purposes.

---

## 2. Data Retention — How Long Is Data Stored?

**API Usage (as of September 2025):**
- Standard retention: **7 days** (reduced from 30 days)
- Inputs and outputs automatically deleted after 7 days
- Never used for model training

**Zero Data Retention (ZDR) Option:**
- Available to qualifying enterprise API customers
- Inputs and outputs are **not stored** beyond real-time abuse screening
- Note: User Safety classifier results are retained for usage policy enforcement

**Recommendation:** For maximum protection, the firm should enquire about ZDR eligibility if processing highly sensitive matters.

---

## 3. Data Residency — Where Is Data Processed?

**Direct Anthropic API:**
- Processing occurs on Anthropic infrastructure (primarily US-based)
- Does not guarantee EU-only or UK-only processing

**EU/UK Residency Options:**
- **AWS Bedrock** — Available with EU region profiles
- **Google Vertex AI** — Available with EU regional endpoints

For matters where UK/EU data residency is required (e.g., particularly sensitive client instructions), the firm can route processing through these cloud providers while still using Claude models.

**Recommendation:** For routine internal use (term sheet review, DD mapping), direct API access is acceptable. For matters requiring strict UK/EU residency, configure AWS Bedrock (EU) or Vertex AI (EU).

---

## 4. SRA Compliance — Does This Breach Professional Obligations?

**Answer: No, provided appropriate controls are in place.**

### SRA Position on AI
The SRA has **not created AI-specific regulations**. The existing Code of Conduct applies in full:

- **Rule 6.3** — Keep affairs of current and former clients confidential unless disclosure is required/permitted by law or client consents
- **Rule 5.1** — Safeguard client confidentiality and legal professional privilege

### SRA Guidance (Risk Outlook Report)
The SRA advises firms to:
1. Take care to avoid confidentiality breaches when moving information between the firm and AI providers
2. Follow all data protection principles — normal rules apply
3. Distinguish between casual use of online AI (e.g., ChatGPT) and formally adopted systems
4. Ensure users understand how the system operates and can explain this to clients
5. Tell clients when AI will be used with their case and how it operates

### Solicitor Accountability
The solicitor's duty of competence, confidentiality, and accountability does **not** diminish with AI use. A solicitor remains personally responsible for:
- Verifying AI outputs
- Protecting client confidentiality
- Explaining the use of AI to clients where appropriate

**Case law note:** *Ayinde v Haringey LBC* and *Al-Haroun v Qatar National Bank* (June 2025) confirm that lawyers who rely on AI without verification face severe penalties.

### H&V Implementation
The term-sheet review skill is designed for **internal use only** — a first-pass review that a lawyer then verifies. This preserves:
- Human-in-the-loop accountability
- No client-facing AI interaction
- Solicitor sign-off on all outputs

---

## 5. UK GDPR Compliance

### Legal Basis for Processing
Where AI processes personal data (e.g., names in term sheets, cap tables), the firm needs a lawful basis under UK GDPR Article 6. Likely bases:
- **Legitimate interest** — The firm has a legitimate interest in efficient document review; this must be balanced against data subject rights (documented balancing test recommended)
- **Contractual necessity** — Where processing is necessary to perform the client engagement

### Data Protection Impact Assessment (DPIA)
Under UK GDPR, a DPIA is **mandatory** where processing includes automated decision-making. The firm should document:
- What personal data is processed
- How it flows to/from the AI system
- What safeguards are in place (encryption, access controls, retention limits)
- How data subject rights are preserved

### Data Minimisation
The skill should process only the data necessary for the task. Redaction of non-essential personal data before processing is best practice.

### Upcoming Regulation
The ICO is developing a statutory Code of Practice on AI and Automated Decision-Making (expected Summer 2026). The firm should monitor for updates.

---

## 6. Recommended Controls

| Control | Implementation |
|---------|----------------|
| **Use Claude Team or Enterprise only** | Ensures Commercial Terms (no training) apply |
| **Document data flows** | Map what data goes to Claude, when, and why |
| **Access control** | Limit access to approved users with appropriate training |
| **No client-facing use** | AI outputs are internal working documents only |
| **Human verification** | Every AI output is reviewed by a qualified solicitor |
| **Client disclosure** | Where appropriate, inform clients that AI tools assist (not replace) legal review |
| **DPIA completion** | Document the processing and safeguards |
| **Retain Commercial Terms** | Keep a copy of Anthropic's applicable terms for audit |
| **EU residency for sensitive matters** | Use AWS Bedrock (EU) or Vertex AI for matters requiring UK/EU-only processing |
| **Periodic review** | Review this position annually or when Anthropic/ICO policies change |

---

## 7. Summary Position

| Question | Answer |
|----------|--------|
| Will Anthropic train on our client data? | **No** — Commercial Terms prohibit it |
| How long is data retained? | **7 days** (standard) or **zero** (ZDR option) |
| Can we achieve UK/EU data residency? | **Yes** — via AWS Bedrock or Vertex AI |
| Does this breach SRA rules? | **No** — existing rules apply; we maintain compliance through controls |
| Is this UK GDPR compliant? | **Yes** — with documented lawful basis and DPIA |
| Is client data at risk? | **No more than with any cloud service** — apply standard information security |

---

## 8. Sources

- [Anthropic Trust Center](https://trust.anthropic.com) — Commercial Terms, data handling policies
- [SRA Risk Outlook: AI in the Legal Market](https://www.sra.org.uk/sra/research-publications/artificial-intelligence-legal-market/) — Regulatory guidance
- [ICO Guidance on AI and Data Protection](https://ico.org.uk/for-organisations/ai/) — UK GDPR compliance
- [Data (Use and Access) Act 2025](https://www.legislation.gov.uk) — UK automated decision-making framework

---

*This briefing is for internal planning purposes. It does not constitute legal advice on regulatory compliance. The firm should seek specialist data protection advice if required.*
