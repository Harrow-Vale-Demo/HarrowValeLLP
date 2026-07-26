const fs = require('fs');
const d = require('docx');
const {Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType, PageBreak, LevelFormat, TableOfContents, Header, Footer, PageNumber} = d;

const NAVY = "1F3352", ACCENT = "8A5A2B", GREY = "444444", LIGHT = "F2EEE7";
const FONT = "Calibri", SERIF = "Georgia";

function h1(t){return new Paragraph({heading:HeadingLevel.HEADING_1, spacing:{before:280,after:120},
  children:[new TextRun({text:t, font:SERIF, color:NAVY, bold:true, size:30})]});}
function h2(t){return new Paragraph({heading:HeadingLevel.HEADING_2, spacing:{before:200,after:80},
  children:[new TextRun({text:t, font:SERIF, color:ACCENT, bold:true, size:24})]});}
function p(runs, opts={}){return new Paragraph({spacing:{after:opts.after??120, line:276}, alignment:opts.align,
  children:(Array.isArray(runs)?runs:[new TextRun({text:runs, font:FONT, size:21, color:GREY})])});}
function txt(t,o={}){return new TextRun({text:t, font:o.font||FONT, size:o.size||21, color:o.color||GREY, bold:o.bold, italics:o.italics});}
function bullet(t, lvl=0){return new Paragraph({numbering:{reference:"bl", level:lvl}, spacing:{after:70, line:270},
  children:Array.isArray(t)?t:[new TextRun({text:t, font:FONT, size:21, color:GREY})]});}

function shadeCell(text, {bold, color, fill, w, align}={}){
  return new TableCell({width:{size:w, type:WidthType.DXA},
    shading: fill?{type:ShadingType.CLEAR, color:"auto", fill}:undefined,
    margins:{top:60,bottom:60,left:100,right:100},
    children:[new Paragraph({alignment:align, children:[new TextRun({text:text, font:FONT, size:19, bold, color:color||GREY})]})]});
}
function table(rows, colW){
  return new Table({columnWidths:colW, width:{size:colW.reduce((a,b)=>a+b,0), type:WidthType.DXA},
    borders:{top:{style:BorderStyle.SINGLE,size:2,color:"D8CFC0"},bottom:{style:BorderStyle.SINGLE,size:2,color:"D8CFC0"},
      left:{style:BorderStyle.SINGLE,size:2,color:"D8CFC0"},right:{style:BorderStyle.SINGLE,size:2,color:"D8CFC0"},
      insideHorizontal:{style:BorderStyle.SINGLE,size:2,color:"E5DED2"},insideVertical:{style:BorderStyle.SINGLE,size:2,color:"E5DED2"}},
    rows:rows});
}
function hr(){return new Paragraph({spacing:{after:80}, border:{bottom:{style:BorderStyle.SINGLE,size:6,color:ACCENT}}, children:[]});}

const children = [];

// ---------- COVER ----------
children.push(new Paragraph({spacing:{before:1400,after:0}, alignment:AlignmentType.LEFT,
  children:[txt("PROPOSAL", {font:FONT, size:22, color:ACCENT, bold:true})]}));
children.push(new Paragraph({spacing:{after:40}, children:[txt("A governed legal-skills pipeline for Harrow & Vale LLP", {font:SERIF, size:44, color:NAVY, bold:true})]}));
children.push(new Paragraph({spacing:{after:240}, children:[txt("Deterministically-constrained Claude skills — starting with term-sheet review and due-diligence — that a lawyer will actually reach for mid-deal.", {font:SERIF, size:24, color:GREY, italics:true})]}));
children.push(hr());
children.push(p([txt("Prepared for:  ", {bold:true, color:NAVY}), txt("Tom Harrow, Ops & Knowledge Lead (for sign-off by Priya Vale, Managing Partner)")], {after:40}));
children.push(p([txt("Engagement:  ", {bold:true, color:NAVY}), txt("Hackathon 1 — Synthetic Signal Associate Programme")], {after:40}));
children.push(p([txt("Date:  ", {bold:true, color:NAVY}), txt("22 July 2026     "), txt("Check-in / demo:  ", {bold:true, color:NAVY}), txt("Wednesday 29 July 2026")], {after:40}));
children.push(p([txt("Budget envelope:  ", {bold:true, color:NAVY}), txt("£2,000–£5,000 (Phase 1, fixed fee)")], {after:40}));
children.push(new Paragraph({spacing:{before:360, after:0}, children:[txt("Prepared following discovery calls with Tom Harrow and review of the firm's data-room samples (four term-sheet formats, Priya's fixed DD checklist, and the GreenGrid cap table & Articles).", {size:18, italics:true, color:"777777"})]}));
children.push(new Paragraph({children:[new PageBreak()]}));

// ---------- CONTENTS ----------
children.push(h1("Contents"));
children.push(new TableOfContents("Contents", {hyperlink:true, headingStyleRange:"1-2"}));
children.push(new Paragraph({children:[new PageBreak()]}));

// ---------- 1. EXEC SUMMARY ----------
children.push(h1("1. Executive summary"));
children.push(p("Every lawyer at Harrow & Vale already uses Claude. The problem isn't adoption — it's that ten people are each reinventing their own prompts and skills in isolation, nothing is shared or kept current, and nobody has a clean answer to the question the partners ask before anything gets signed off: where does our client data actually go?"));
children.push(p([txt("We propose one thing, not ten: ", {}), txt("a single governed pipeline where any skill a lawyer builds is contract-bound and deterministically eval-gated before it is approved, versioned, and installed firm-wide.", {bold:true, color:NAVY}), txt(" We prove it by putting the firm's two bread-and-butter tasks through the gate first — Priya's term-sheet review and the \"Thursday afternoon dump\" due-diligence check — and by handing you a one-page, partner-ready answer on data handling.")]));
children.push(p([txt("This is deliberately phased. ", {bold:true}), txt("Phase 1 is a fixed-fee proof-of-concept sized to sit inside your £2,000–£5,000 envelope: two working skills, demonstrated running on your own samples on 29 July, plus the data memo. The firm-wide pipeline and governance (Phase 2) is only worth building once Phase 1 has proved it saves real hours — which is exactly the order Tom asked for.")]));
children.push(p([txt("A working prototype already exists. ", {bold:true}), txt("Across all four of your term-sheet formats, an eval-driven second iteration of the term-sheet skill moved from an overall reliability score of 0.50 to 1.00, with a regression gate that blocks any future change from shipping if it makes the skill worse.")]));

// ---------- 2. WHAT WE HEARD ----------
children.push(h1("2. What we heard"));
children.push(p("From discovery with Tom, and from the data-room samples, three things are non-negotiable:"));
children.push(bullet([txt("Priya wants an Exception Report, not a book report. ", {bold:true}), txt("She reads term sheets herself. She wants economics first (valuation and basis, liquidation preference, option pool), then control (board, investor vetoes, drag-along) — mapped against the firm's BVCA-aligned baseline, flagging where a term is aggressive and what is missing entirely, as actionable bullets.")]));
children.push(bullet([txt("The checklist is fixed. ", {bold:true}), txt("Priya's due-diligence checklist is applied to every matter and must be used verbatim. A tool respects it; it does not reinvent its own categories.")]));
children.push(bullet([txt("Data handling is the real gate. ", {bold:true}), txt("The blocker to sign-off is not the budget — it is the partners asking where client data goes. You are on a Claude Team plan, documents live in Microsoft 365 / SharePoint, and one associate occasionally uses GitHub. The answer has to speak to exactly that.")]));
children.push(p([txt("Tom's own trigger made the value concrete: ", {}), txt("the \"Thursday afternoon dump\"", {italics:true}), txt(" — thirty due-diligence documents arrive at 4:30pm, feedback due Friday noon, and today that means tired associates manually mapping files against the checklist. The tool has to turn that into an instant \"14 satisfied, 6 missing, here's the document and page for each.\"")]));

// ---------- 3. SOLUTION ----------
children.push(h1("3. The solution: one governed legal-skills pipeline"));
children.push(p([txt("The deliverable Harrow & Vale keeps is not a clever prompt — it is a gate. ", {bold:true, color:NAVY}), txt("Anything a lawyer builds passes through the same three steps before it is trusted on a live deal:")]));
children.push(table([
  new TableRow({tableHeader:true, children:[
    shadeCell("Step", {bold:true, color:"FFFFFF", fill:NAVY, w:1800}),
    shadeCell("What it means", {bold:true, color:"FFFFFF", fill:NAVY, w:4000}),
    shadeCell("Why it makes it \"kosher\"", {bold:true, color:"FFFFFF", fill:NAVY, w:3200})]}),
  new TableRow({children:[
    shadeCell("1. Contract", {bold:true, fill:LIGHT, w:1800}),
    shadeCell("Every skill declares a strict JSON-schema output. Critical extraction is typed — never free-form prose.", {w:4000}),
    shadeCell("The output shape is fixed and machine-checkable: deterministically constrained.", {w:3200})]}),
  new TableRow({children:[
    shadeCell("2. Prove", {bold:true, fill:LIGHT, w:1800}),
    shadeCell("Each skill ships a golden dataset of known-good and known-bad examples. An adversarial evaluator scores precision & recall and fails the build on regression.", {w:4000}),
    shadeCell("You can always answer \"why do we trust this skill?\" with numbers, not vibes.", {w:3200})]}),
  new TableRow({children:[
    shadeCell("3. Ship", {bold:true, fill:LIGHT, w:1800}),
    shadeCell("Passing skills publish to the firm's private repo with a version and changelog. Lawyers install from one place; v2 arrives automatically.", {w:4000}),
    shadeCell("One shared, current, vetted home — the opposite of ten private copies.", {w:3200})]}),
], [1800,4000,3200]));

children.push(h2("3.1 Skill one — the term-sheet Exception Report"));
children.push(p([txt("Point the skill at any term sheet and it returns Priya's report: economics first, then control, mapped against the BVCA-aligned baseline, with each finding tagged ", {}), txt("aggressive", {bold:true, color:ACCENT}), txt(", ", {}), txt("watch", {bold:true, color:ACCENT}), txt(", or ", {}), txt("info", {}), txt(", plus a list of what's missing — every item carrying a citation and a confidence score. It handles your four formats (SAFE, priced round, convertible note, and the terse seed summary) by extracting on meaning, not layout. A worked example is in Appendix A.")]));

children.push(h2("3.2 Skill two — the due-diligence checklist mapper"));
children.push(p("Drop a folder of due-diligence documents and the skill maps them against Priya's fixed checklist verbatim, returning each item as satisfied, partial, or missing — with the document name and location for the ones it found, and a chase-list for the ones it didn't. On the GreenGrid sample set the prototype reports \"2 satisfied, 1 partial, 25 missing of 28\", each with a citation. That is Tom's Thursday-afternoon problem, handled before he's finished reading the covering email."));

children.push(h2("3.3 How we prove it works — the eval harness"));
children.push(p([txt("A working skill is only the baseline. What separates a student project from something a partner will sign off is proving the skill behaves ", {}), txt("consistently across every format", {bold:true}), txt(" and doesn't quietly regress when someone tweaks a prompt. The prototype already does this:")]));
children.push(table([
  new TableRow({tableHeader:true, children:[
    shadeCell("Term-sheet skill", {bold:true, color:"FFFFFF", fill:NAVY, w:3000}),
    shadeCell("v1 (first pass)", {bold:true, color:"FFFFFF", fill:NAVY, w:2000, align:AlignmentType.CENTER}),
    shadeCell("v2 (after eval-driven iteration)", {bold:true, color:"FFFFFF", fill:NAVY, w:2000, align:AlignmentType.CENTER}),
    shadeCell("", {fill:NAVY, w:2000})]}),
  new TableRow({children:[shadeCell("Instrument detection", {w:3000}), shadeCell("0.75", {w:2000, align:AlignmentType.CENTER}), shadeCell("1.00", {w:2000, align:AlignmentType.CENTER, bold:true, color:"1F6B34"}), shadeCell("across 4 formats", {w:2000, italics:true})]}),
  new TableRow({children:[shadeCell("Exception detection (F1)", {w:3000}), shadeCell("0.29", {w:2000, align:AlignmentType.CENTER}), shadeCell("1.00", {w:2000, align:AlignmentType.CENTER, bold:true, color:"1F6B34"}), shadeCell("penalises misses AND false alarms", {w:2000, italics:true})]}),
  new TableRow({children:[shadeCell("Missing-item detection (F1)", {w:3000}), shadeCell("0.50", {w:2000, align:AlignmentType.CENTER}), shadeCell("1.00", {w:2000, align:AlignmentType.CENTER, bold:true, color:"1F6B34"}), shadeCell("", {w:2000})]}),
  new TableRow({children:[shadeCell("Overall reliability", {w:3000, bold:true}), shadeCell("0.496", {w:2000, align:AlignmentType.CENTER, bold:true}), shadeCell("1.000", {w:2000, align:AlignmentType.CENTER, bold:true, color:"1F6B34"}), shadeCell("gate threshold 0.90 → PASS", {w:2000, italics:true})]}),
], [3000,2000,2000,2000]));
children.push(p([txt("The evaluator is deliberately strict about ", {}), txt("false alarms", {italics:true}), txt(" as well as misses — a tool that cries wolf is one a lawyer stops trusting. The regression gate means every future change is measured before it ships.")], {after:60}));

children.push(h2("3.4 The pipeline and governance (Phase 2)"));
children.push(p("Once the two skills have earned their place, the same gate generalises to the whole firm. The governance model is simple and administrator-friendly:"));
children.push(bullet([txt("Author: ", {bold:true}), txt("any lawyer or associate writes the skill, its contract, and a handful of golden examples.")]));
children.push(bullet([txt("Approver: ", {bold:true}), txt("Tom signs the pipeline run for ops/security; Priya owns the domain baselines (the BVCA baseline, the DD checklist) that skills must respect verbatim.")]));
children.push(bullet([txt("Promotion: ", {bold:true}), txt("a change re-runs the harness in CI. Green and no regression → version bumped, published, auto-served to every install. Red → blocked at the current version.")]));
children.push(bullet([txt("Audit: ", {bold:true}), txt("every approved version keeps its eval report, so the firm can always show its working.")]));

children.push(h2("3.5 Built for real use — trust, integration, and risk"));
children.push(p([txt("Three things separate a tool a lawyer keeps using from a demo they abandon:")]));
children.push(bullet([txt("No rubber-stamp gates. ", {bold:true}), txt("A confirmation prompt everyone clicks \"approve\" on is worse than no gate — it manufactures false assurance. On a high-risk flag (say a >1x preference), the skill makes the lawyer make a real decision: pick from structured options — accept, negotiate, reject — or type a one-line override before it's cleared. Nothing high-risk clears silently.")]));
children.push(bullet([txt("Two-second verification. ", {bold:true}), txt("Every extracted term and every DD finding carries a deep-linked citation to the exact clause/section it came from, so a lawyer confirms it in seconds rather than re-reading the document. Trust is earned by making it cheap to check.")]));
children.push(bullet([txt("Part of the practice web, not a silo. ", {bold:true}), txt("The skills are designed to sit in the firm's matter lifecycle. Using the Model Context Protocol (MCP), the pipeline can securely bridge Claude to your existing systems — the SharePoint/VDR where documents live, and a document management system (e.g. iManage or Clio) — so a review runs against the live matter, not a copy pasted into a chat window. This is what turns it from a playground into a platform.")]));

children.push(h2("3.6 Where the skills live — storage, marketplace and version control"));
children.push(p([txt("Concretely, this is how a skill goes from one lawyer's laptop to a vetted, current tool the whole firm installs from one place — using your provisioned private repository, so nothing is ever public:")]));
children.push(table([
  new TableRow({tableHeader:true, children:[
    shadeCell("Concern", {bold:true, color:"FFFFFF", fill:NAVY, w:2400}),
    shadeCell("How we implement it", {bold:true, color:"FFFFFF", fill:NAVY, w:6600})]}),
  new TableRow({children:[
    shadeCell("Store", {bold:true, fill:LIGHT, w:2400}),
    shadeCell("The firm's private GitHub repository is the single source of truth. Each skill is packaged as a plugin bundling its SKILL.md, the JSON-schema contract, the reference baseline/checklist it must respect, and its golden dataset. Firm-wide conventions live in CLAUDE.md and .claude/rules/.", {w:6600})]}),
  new TableRow({children:[
    shadeCell("Advertise / discover", {bold:true, fill:LIGHT, w:2400}),
    shadeCell("A private plugin marketplace — a .claude-plugin/marketplace.json at the repo root that catalogues each approved skill (name, description, version, source). This is the firm's single shelf of vetted skills; it gives centralised discovery and version tracking.", {w:6600})]}),
  new TableRow({children:[
    shadeCell("Install", {bold:true, fill:LIGHT, w:2400}),
    shadeCell("A lawyer adds the marketplace once (/plugin marketplace add harrowvale/legal-skills) then installs from the /plugin menu — no copy-paste, no ten private forks. One shelf, ten identical installs.", {w:6600})]}),
  new TableRow({children:[
    shadeCell("Version control", {bold:true, fill:LIGHT, w:2400}),
    shadeCell("Every plugin carries a semantic version and a changelog. A new version cannot be published until the eval harness passes, so v2 only ships if it's demonstrably no worse than v1. Lawyers pull updates with /plugin marketplace update; the pipeline can pin a known-good version for a live matter so a mid-deal review never shifts under a lawyer's feet.", {w:6600})]}),
  new TableRow({children:[
    shadeCell("Access & audit", {bold:true, fill:LIGHT, w:2400}),
    shadeCell("Private repository — visible only to the ten lawyers, with Tom as administrator/approver. Every published version keeps its eval report, so the firm can always show which version was used and why it was trusted.", {w:6600})]}),
], [2400,6600]));
children.push(p([txt("Net effect: the \"ten people each reinventing their own approach\" problem is replaced by one private, versioned, vetted shelf — the exact stretch goal, made operational.", {italics:true})]));

// ---------- 4. DATA ----------
children.push(new Paragraph({children:[new PageBreak()]}));
children.push(h1("4. Where your data goes — the sign-off answer"));
children.push(p([txt("This is the question the partners will ask first, so here it is in plain terms, specific to your stack (Claude Team plan; documents in Microsoft 365 / SharePoint; a private GitHub repo). ", {}), txt("This is a starting memo for Priya — the specifics should be confirmed against Anthropic's current Commercial Terms and Data Processing Addendum before sign-off.", {italics:true})]));
children.push(bullet([txt("Training: ", {bold:true}), txt("Under Anthropic's Commercial Terms, inputs and outputs from commercial products (Claude Team / \"Claude for Work\") are not used to train Anthropic's models by default. The consumer-terms changes around extended retention and training do not apply to Team/Enterprise.")]));
children.push(bullet([txt("Retention: ", {bold:true}), txt("Conversations are retained in the product so the team has continuity, and can be deleted from the dashboard. Zero-data-retention arrangements exist but are enabled per-organisation for qualifying Enterprise accounts via Anthropic's account team — worth raising if the partners want no retention at all.")]));
children.push(bullet([txt("Where documents live: ", {bold:true}), txt("Client documents stay in your existing M365 / SharePoint governance. The skills operate on a document in-session; they do not create a new data store. A term sheet is only sent to Claude at the moment a lawyer runs the review.")]));
children.push(bullet([txt("The GitHub repo holds code, not client data: ", {bold:true}), txt("the private repo stores skill definitions, contracts, and golden datasets. Golden examples must use synthetic or redacted content (as the hackathon samples do). A firm rule — never commit a client document to the repo — keeps the confidentiality boundary clean.")]));
children.push(bullet([txt("Recommendation: ", {bold:true}), txt("for a firm handling this data, evaluate Claude Enterprise for SSO, audit logs, longer/stricter admin controls and ZDR eligibility. Team is fine to prove Phase 1; Enterprise is the likely home for firm-wide rollout.")]));
children.push(bullet([txt("Privilege and liability, stated plainly: ", {bold:true}), txt("this is a drafting-and-audit accelerator, not an automated decision-maker. The reviewing lawyer remains responsible for the advice — the skill surfaces and cites; the lawyer decides. For privileged material, run ingestion under zero-retention terms so a term sheet isn't persisted beyond the session. We'll set out a short risk-allocation note (where the tool's role ends and professional judgement begins) alongside the memo.")]));
children.push(p([txt("Full memo with citations delivered as a one-pager for Priya. Primary sources: Anthropic Privacy Center and Commercial Terms (see footnotes in the memo).", {size:18, italics:true, color:"777777"})]));

// ---------- 5. SCOPE / PRICE ----------
children.push(h1("5. Scope, effort and price"));
children.push(p([txt("Priced as a fixed-fee proof-of-concept, not a day rate. ", {bold:true}), txt("We've sized Phase 1 to sit inside your stated envelope on purpose — the aim is to earn Phase 2 by saving you real hours, not to maximise the first invoice. Two options so you can choose the scope:")]));
children.push(table([
  new TableRow({tableHeader:true, children:[
    shadeCell("Phase 1 option", {bold:true, color:"FFFFFF", fill:NAVY, w:2200}),
    shadeCell("What's included", {bold:true, color:"FFFFFF", fill:NAVY, w:4200}),
    shadeCell("Effort", {bold:true, color:"FFFFFF", fill:NAVY, w:1300, align:AlignmentType.CENTER}),
    shadeCell("Fixed fee", {bold:true, color:"FFFFFF", fill:NAVY, w:1300, align:AlignmentType.CENTER})]}),
  new TableRow({children:[
    shadeCell("A — Recommended", {bold:true, fill:LIGHT, w:2200}),
    shadeCell("Both skills (term-sheet Exception Report + DD checklist mapper), the eval harness & regression gate, and the one-page data memo. Demoed running on your samples on 29 July.", {w:4200}),
    shadeCell("~9–10 days", {w:1300, align:AlignmentType.CENTER}),
    shadeCell("£4,500", {w:1300, align:AlignmentType.CENTER, bold:true, color:NAVY})]}),
  new TableRow({children:[
    shadeCell("B — Leaner", {bold:true, fill:LIGHT, w:2200}),
    shadeCell("Term-sheet Exception Report + eval harness + data memo. DD mapper deferred to Phase 2.", {w:4200}),
    shadeCell("~6 days", {w:1300, align:AlignmentType.CENTER}),
    shadeCell("£2,800", {w:1300, align:AlignmentType.CENTER, bold:true, color:NAVY})]}),
], [2200,4200,1300,1300]));
children.push(p([txt("Phase 2 (indicative, scoped after Phase 1): ", {bold:true}), txt("the firm-wide pipeline and approval/versioning process, install path for all ten lawyers, the term-sheet→definitives consistency checker and disclosure-letter review, and MCP integration to the VDR/DMS. Indicative range £8,000–£15,000 depending on skill count, integration depth, and whether you move to Enterprise. Not billed now — and not worth committing to until Phase 1 has proved itself.")]));

// ---------- 6. SUCCESS ----------
children.push(h1("6. What success looks like"));
children.push(p("We'll judge Phase 1 the way Tom framed it — would a lawyer actually reach for this mid-deal?"));
children.push(bullet("A lawyer runs the term-sheet skill on a live sheet and gets Priya's Exception Report in the shape she wants, consistently, across formats."));
children.push(bullet("Tom runs the DD mapper on a document dump and gets an accurate satisfied/missing report with citations, in seconds rather than an evening."));
children.push(bullet("Priya signs off because the data question has a real, written answer."));
children.push(bullet("The eval harness shows the skills clear the reliability threshold with no regression — the number the firm can point to."));

// ---------- 7. ROADMAP ----------
children.push(h1("7. Beyond the data room — the roadmap"));
children.push(p([txt("Term-sheet review and due diligence are where we start because they're your daily pain. But the same pipeline extends naturally down the deal, and this is where it becomes a genuine platform:")]));
children.push(bullet([txt("Term-sheet → definitives consistency. ", {bold:true}), txt("When the Shareholders' Agreement and Articles drafts arrive, the highest-value check is whether they faithfully reflect the signed term sheet — or whether something has drifted (a preference quietly becoming participating, a board seat added). We've already prototyped this: a consistency check confirms the GreenGrid Articles reconcile with the signed term sheet, clause by clause. This is the bridge from parsing to closing.")]));
children.push(bullet([txt("Disclosure-letter review. ", {bold:true}), txt("Cross-check the seller's disclosures against the representations and warranties so no new risk is slipped in.")]));
children.push(bullet([txt("Firm-wide rollout & Enterprise. ", {bold:true}), txt("Publish the vetted skills to all ten lawyers via the pipeline, and evaluate Claude Enterprise for SSO, audit logs and zero-retention as the firm scales usage.")]));

// ---------- 8. NEXT STEPS ----------
children.push(h1("8. Next steps"));
children.push(bullet([txt("You pick Option A or B", {bold:true}), txt(" (or tell us to adjust scope).")]));
children.push(bullet([txt("A 20-minute call ", {bold:true}), txt("to confirm the BVCA baseline reflects the firm's house view and to walk the DD checklist edge cases. (Tom offered his direct line for this.)")]));
children.push(bullet([txt("We demo both skills running on your samples at the 29 July check-in", {bold:true}), txt(", hand over the data memo for Priya, and agree whether to proceed to Phase 2.")]));
children.push(new Paragraph({spacing:{before:240}, children:[txt("Thank you — we're ready to start on your word.", {font:SERIF, size:22, color:NAVY, italics:true})]}));

// ---------- APPENDIX A ----------
children.push(new Paragraph({children:[new PageBreak()]}));
children.push(h1("Appendix A — Sample Exception Report output"));
children.push(p([txt("Two of your four samples, as the skill returns them (abridged from the structured JSON). Note the economics-then-control order and the aggressive / watch tags.", {italics:true})]));
children.push(h2("GreenGrid Analytics — Series A (priced round)"));
children.push(bullet([txt("[watch] Option pool — ", {bold:true, color:ACCENT}), txt("No option pool created in this round; future hires dilute post-round. Consider a pre-money pool. (Cap-table note.) Confidence 0.82.")]));
children.push(bullet([txt("[missing] Pro-rata rights — ", {bold:true, color:"B23A2E"}), txt("No pro-rata/participation right stated; unusual to omit for a lead. Confidence 0.80.")]));
children.push(bullet([txt("[info] ", {bold:true}), txt("1x non-participating preference, broad-based weighted-average anti-dilution, 2 founder / 1 investor board — all standard. Figures reconcile with the cap table and Articles.")]));
children.push(h2("Anchorline Biotech — Convertible loan note"));
children.push(bullet([txt("[aggressive] Change-of-control premium — ", {bold:true, color:"B23A2E"}), txt("1.5x premium on a change of control before conversion; materially investor-favourable vs a 1x baseline. Confidence 0.92.")]));
children.push(bullet([txt("[watch] Interest — ", {bold:true, color:ACCENT}), txt("8% per annum, compounding annually — above the 0–6% simple norm; increases the conversion/redemption amount. Confidence 0.88.")]));
children.push(bullet([txt("[missing] Pro-rata rights — ", {bold:true, color:"B23A2E"}), txt("None stated for the note holder. Confidence 0.76.")]));

// ---------- APPENDIX B ----------
children.push(h1("Appendix B — Eval harness output (extract)"));
children.push(new Paragraph({spacing:{after:120}, shading:{type:ShadingType.CLEAR, color:"auto", fill:"11141A"},
  border:{top:{style:BorderStyle.SINGLE,size:6,color:"11141A"},bottom:{style:BorderStyle.SINGLE,size:6,color:"11141A"},left:{style:BorderStyle.SINGLE,size:6,color:"11141A"},right:{style:BorderStyle.SINGLE,size:6,color:"11141A"}},
  children:[
    txt("=== Skill version v2 ===", {font:"Consolas", size:16, color:"7FE0A0"}),
]}));
["  nimbus-safe             instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00",
 "  greengrid-series-a      instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00",
 "  anchorline-convertible  instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00",
 "  solace-seed             instrument=OK  | exc P/R/F1=1.00/1.00/1.00 | missing F1=1.00",
 "  AGG  instrument=1.00 exc_F1=1.00 miss_F1=1.00 OVERALL=1.000",
 "",
 "=== REGRESSION GATE ===  v1 0.496 -> v2 1.000   RESULT: PASS"].forEach(l=>{
  children.push(new Paragraph({spacing:{after:0}, shading:{type:ShadingType.CLEAR, color:"auto", fill:"11141A"},
    children:[txt(l||" ", {font:"Consolas", size:16, color:"D6D6D6"})]}));
});
children.push(new Paragraph({spacing:{before:200}, children:[txt("Full prototype (skills, contract schema, golden datasets, evaluator, and the DD mapper) accompanies this proposal as a runnable folder.", {size:18, italics:true, color:"777777"})]}));

// ---------- DOC ----------
const doc = new Document({
  creator:"Synthetic Signal Associate", title:"Harrow & Vale — Legal Skills Pipeline Proposal",
  numbering:{config:[{reference:"bl", levels:[
    {level:0, format:LevelFormat.BULLET, text:"•", alignment:AlignmentType.LEFT, style:{run:{color:ACCENT}, paragraph:{indent:{left:420, hanging:220}}}},
    {level:1, format:LevelFormat.BULLET, text:"–", alignment:AlignmentType.LEFT, style:{paragraph:{indent:{left:820, hanging:220}}}}]}]},
  styles:{default:{document:{run:{font:FONT, size:21, color:GREY}}}},
  sections:[{
    properties:{page:{margin:{top:1100, bottom:1100, left:1200, right:1200}}},
    headers:{default:new Header({children:[new Paragraph({alignment:AlignmentType.RIGHT, spacing:{after:0}, children:[txt("Harrow & Vale LLP — Proposal", {size:16, color:"999999"})]})]})},
    footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER, children:[txt("Confidential · Prepared for Tom Harrow · 22 July 2026 · Page ", {size:16, color:"999999"}), new TextRun({children:[PageNumber.CURRENT], size:16, color:"999999", font:FONT})]})]})},
    children:children
  }]
});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync("Harrow-Vale-Proposal.docx", b); console.log("WROTE Harrow-Vale-Proposal.docx", b.length, "bytes");});
