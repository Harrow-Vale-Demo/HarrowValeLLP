# Scenario 1 — Harrow & Vale LLP
**Unlocked engagement pack · Hackathon 1 · Synthetic Signal Associate Program · Negative Zero**

## The client
Harrow & Vale LLP is a boutique law firm in Clerkenwell, London, advising founders and investors through venture funding rounds and mergers & acquisitions. Ten lawyers work from first institutional round through to exit, with a particular focus on term-sheet negotiation and due-diligence discipline. Every lawyer already uses Claude — but each has built their own prompts and skills in isolation: nothing is shared, approved, or kept up to date.

- **Website:** harrowvale.syntheticsignal.io
- **Your sponsor:** Tom Harrow, Ops & Knowledge Lead (runs how the firm evaluates and adopts tools). Managing Partner Priya Vale sets the firm's due-diligence standard and reviews every closing.
- **Practice:** SAFEs, priced equity rounds and convertible loan notes; cap-table structuring, disclosure schedules, closing mechanics; buy-side and sell-side due diligence.

## The ask
- **Core —** a working Claude skill that speeds up term-sheet review and the firm's due-diligence checklist. Given a term sheet, it should extract the key economic terms, check them against Priya's checklist, and flag deviations, unusual clauses and omissions in a consistent, plain-English review.
- **Stretch —** a proper "approved skills" pipeline for the whole firm: a private, versioned home for vetted skills that all ten lawyers can install from and that stays current — plus a written, partner-ready answer to their data-residency and confidentiality question.

## What's been built for you (tech setup)
- **Public site —** harrowvale.syntheticsignal.io (practice areas, the team).
- **Data room —** harrowvale.syntheticsignal.io/data-room/ — sign in with your Negative Zero identity. It holds the sample term sheets (a SAFE, a priced round, and a convertible loan note — deliberately different formats), the firm's due-diligence checklist, and a small mock data-room document set (cap table, articles, key contracts). If you can't reach it, ask Drew on the night.
- **Approved-skills repository —** a private GitHub repository is provisioned for the stretch goal; your team is sent an invite. Publish your vetted skill there with a version and an install path.
- **Your own tooling —** Claude Desktop + Claude Code, signed in with your NZ account.

## Requirements — what "done" looks like
- **Core:** point the skill at any of the sample term sheets and it produces a structured review — key terms extracted (valuation/cap, discount, liquidation preference, board/consent items, pro-rata, etc.), deviations and omissions flagged against the checklist, and a short summary a lawyer could act on. It must stay consistent across the three different term-sheet formats — build test-driven against 2–3 examples before generalising.
- **Stretch:** a lawyer can install the approved skill from the private repo, receive updates when a new version ships, and there is a documented approval + versioning process (who vets, how v2 rolls out). Plus a one-page data-residency / confidentiality memo a managing partner would accept.

## How to build it with Claude
- **Agent Skills —** a `SKILL.md` with clear frontmatter (name, description, allowed-tools, argument-hint). Iterate against real term sheets, not vibes.
- **Distribution & versioning —** a private plugin / marketplace via the GitHub repo; consider `CLAUDE.md` and `.claude/rules/` for firm-wide conventions.
- **The memo —** research Claude for Enterprise / Teams data-handling (data residency, training, retention, admin controls). This is a consulting deliverable, not code — enterprise clients ask it every time.
- **Exam alignment:** Claude Code Configuration & Workflows (20%), Context Management & Reliability (15%).

## Deliverables — due at the weekly check-in, Wednesday 29 July
1. **Client proposal** — how you'll solve the challenge, scope of work, and honest time & effort estimates, priced against the budget the client gave you on the call.
2. **Solution presentation** — demonstrate the working solution to the client. Show it running.
3. **Next steps** — how the client takes it further, or the next engagement you'd propose.
4. **Public case study** — Anthropic / public-facing: how Claude solved the problem. Format is your call.

## Tips
- Ask the client what "review" means to them — what they check, in what order, and what a good output looks like.
- For the stretch, think like an administrator: how does a lawyer install an approved skill, and how do they get version 2?

## Support
Stuck on the *how*? Ask the **Hackathon Helper** in the Lab. Programme contacts: Drew, Alba & Daley, or drew.perry@negativezero.com. All client data is synthetic practice data.
