# Fact & Reference Check — Block 0 + Block 1 (Chapters 1–7)

**Auditor**: Fact & Reference Checker — Claims Auditor
**Scope**: Chapters 1–7 (The Agentic SDLC Thesis through Planning the Transition)
**Date**: 2025-07-15
**Methodology**: Every factual claim, statistic, comparison, prediction, vendor claim, attribution, and causal statement was extracted and classified per the three-tier system (Verified / Qualified / Unverified). Cross-chapter consistency was checked against the Ch1 case study reference numbers.

---

## Executive Summary

| Chapter | Verified | Qualified | ⚠️ Unverified | Highest Risk |
|---------|----------|-----------|----------------|--------------|
| Ch 1 | 3 | 5 | 6 | "Context windows have grown 100×" — false precision |
| Ch 2 | 16 | 8 | 10 | "Code generation is the solved phase" — overstatement |
| Ch 3 | 4 | 16 | 11 | 30–60% rework rate — flagship number, no citation |
| Ch 4 | 6 | 10 | 8 | Milestone gate thresholds — presented as calibrated, unsourced |
| Ch 5 | 11 | 6 | 7 | ISO 27001 edition ambiguity; phase-number inconsistency |
| Ch 6 | 4 | 6 | 9 | 🔴 Source misattribution (SO 2024/Octoverse) |
| Ch 7 | 3 | 6 | 10 | Kill criteria and ratio thresholds — consequential, unsourced |
| **Total** | **47** | **57** | **61** | |

**Top 5 most vulnerable claims across the block** (a skeptical CTO or journalist would attack these first):

1. **Ch6 §Time-allocation table** — Cites "2024 Stack Overflow Developer Survey" and "Octoverse report" as sources, but neither contains the activity-level breakdown shown. **Falsifiable by checking the sources.** 🔴 Critical.
2. **Ch3 §30–60% rework rate** — Flagship number used in both Ch1 and Ch3. Ch1 hedges ("Teams report…"); Ch3 escalates to "Industry data consistently shows…" — no citation in either. Most quotable and most challengeable.
3. **Ch2 §"Code generation is the solved phase"** — Bold overstatement. Hallucinations, architectural coherence remain unsolved. Quotable out of context.
4. **Ch7 §Kill criteria (40%) and ratio thresholds (1.5:1, 3:1, 5:1)** — Teams will make consequential decisions based on these numbers. No sourcing or methodology.
5. **Ch5 §Phase numbering in board template** — Contradicts the book's own phase model from Ch2. Internal factual error.

---

## Chapter 1: The Agentic SDLC Thesis

### ✅ Verified Claims

| Location | Claim | Basis |
|----------|-------|-------|
| L51 | "In 2000, Roy Fielding… published a dissertation that defined constraints — statelessness, uniform interface, layered system" | Fielding, R. T. (2000). *Architectural Styles and the Design of Network-Based Software Architectures.* UC Irvine doctoral dissertation. |
| L103 | "Anthropic publishes guidelines for structuring agent interactions" | Anthropic's public documentation includes agent design guidelines. |
| L69 | "70 files changed, 2,874 tests passing, 3 human interventions, roughly 90 minutes" | Internal case study (PR #394). Canonical reference numbers for cross-chapter consistency. |

### ✅ Qualified Claims (Acceptable)

| Location | Claim | Hedge |
|----------|-------|-------|
| L23 | "Teams report that 30–60% of agent-generated code requires rework when applied to complex tasks" | "Teams report" — attributed to pattern observation, not a study |
| L23 | "not because the models are weak, but because the context is" | Analytical claim following from the chapter's own argument; presented as a conclusion, not external data |
| L25 | "Name any experienced engineering team… They've hit this cliff" | Rhetorical challenge, not factual assertion |
| L101 | "PROSE articulates constraints that any reliable AI-native development approach will need to address" | Framed as "the appropriate claim is…" — explicit positioning |
| L29 | "Some retreat… Others push forward with brute force" | Pattern observation, not empirical claim |

### ⚠️ Unverified Claims

**1. Context window growth — "100×"**
- **Line/section**: L47
- **Claim**: *"Context windows have grown 100× in two years"*
- **Issue**: GPT-3 (2020): 4K tokens. GPT-4 (2023): 32K (8×) or 128K (32×). Gemini 1.5 (2024): 1M (250× over GPT-3, but over 4 years, not 2). Claude 3 (2024): 200K (50× over GPT-3). No straightforward "100× in two years" measurement is citable. False precision for a claim that's directionally correct.
- **Recommendation**: Replace with *"Context windows have grown by orders of magnitude in recent years"* or cite specific models and dates.

**2. "Satisfaction… has not kept pace"**
- **Line/section**: L47
- **Claim**: *"satisfaction with AI on complex engineering tasks has not kept pace"*
- **Issue**: No survey cited. The 2024 Stack Overflow survey actually shows increasing satisfaction with AI tools, though it doesn't break down by task complexity. The claim is plausible but unsupported as stated.
- **Recommendation**: Add qualification → *"anecdotally, satisfaction with AI on complex tasks has not grown proportionally"* or cite specific survey data showing the complexity gap.

**3. REST didn't "eliminate" SOAP or RPC**
- **Line/section**: L53
- **Claim**: *"REST didn't eliminate SOAP or RPC."*
- **Issue**: Minor factual quibble — REST effectively did eliminate SOAP for most new development. SOAP persists in legacy enterprise systems but new adoption is negligible. The rhetorical point (REST didn't replace everything overnight) is sound, but "didn't eliminate" overstates SOAP's current relevance.
- **Recommendation**: Consider *"REST didn't immediately replace SOAP or RPC"* — the word "immediately" preserves the point while being more accurate.

**4. "LangChain and LangGraph define patterns for composing LLM workflows"**
- **Line/section**: L103
- **Claim**: Lists LangChain, LangGraph, AutoGen as alternatives
- **Issue**: Accurate as of mid-2025, but these tools evolve rapidly. LangGraph is relatively new and its pattern-definition role may be overstated. Minor — but vendor claims need extra scrutiny per the audit persona.
- **Recommendation**: Add temporal qualifier → *"As of 2025, LangChain and LangGraph…"*

**5. "More confident wrong answers, faster"**
- **Line/section**: L47
- **Claim**: *"A more powerful model working with unstructured, incomplete, or noisy context doesn't produce better results. It produces more confident wrong answers, faster."*
- **Issue**: Strong causal claim. While plausible (larger models can be more confidently wrong), no citation. Some research suggests larger models are *better* at self-correction and uncertainty calibration. The claim conflates model power with context quality in a way a researcher could challenge.
- **Recommendation**: Qualify → *"can produce more confident wrong answers"* (replace "doesn't… It produces" with conditional framing).

**6. "The failure mode of a strong model with poor context is insidious"**
- **Line/section**: L47
- **Claim**: *"it produces plausible output that looks correct and silently violates your system's invariants"*
- **Issue**: Analytical claim presented as universal law. True in many cases, but strong models with poor context also sometimes refuse to act or flag uncertainty. The framing as an inevitable outcome overreaches.
- **Recommendation**: Add *"often"* → *"it often produces plausible output…"*

---

## Chapter 2: The AI-Native Landscape

### ✅ Verified Claims

| Location | Claim | Basis |
|----------|-------|-------|
| L11 | "2024 Stack Overflow Developer Survey found 76% of developers are using or plan to use AI coding tools" | 2024 SO Developer Survey (publicly available) |
| L11 | "up from 44% in 2023" | 2023 SO Developer Survey |
| L11 | "GitHub's 2024 Octoverse report placed the figure higher: 97%" | GitHub Octoverse 2024 |
| L13 | "In 2021, GitHub Copilot launched as a technical preview" | Copilot technical preview: June 29, 2021 |
| L13 | "an autocomplete tool powered by OpenAI Codex" | Accurate at launch |
| L15 | "Gartner estimated in 2024 that by 2028, 75% of enterprise software engineers will use AI code assistants — up from fewer than 10% in early 2023" | Gartner press release August 2024 |
| L31 | "Amazon CodeWhisperer (now Q Developer)" | Rebranded April 2024 |
| L33 | "ChatGPT's launch in late 2022" | November 30, 2022 |
| L35 | "GitHub Copilot's agent mode, Claude Code, Cursor's Composer, and Windsurf's Cascade" | All shipping products as of mid-2025 |
| L37 | "GitHub's Coding Agent assigns issues to an AI that works in a cloud environment, submits pull requests, and responds to review feedback" | Announced May 2025 |
| L37 | "Several startups — Devin, Factory, Codegen — are building similar workflows" | All real, funded companies |
| L97 | "GitHub Copilot uses custom instructions and `.github/copilot-instructions.md`" | Documented in GitHub Copilot docs |
| L97 | "Cursor uses `.cursor/rules`" | Documented in Cursor docs |
| L97 | "Claude Code uses `CLAUDE.md`" | Documented in Anthropic docs |
| L105 | Microsoft disclosure: "the author works at Microsoft and discloses this" | Explicit self-disclosure |
| L166 | "A 2024 GitHub survey found that 92% of U.S.-based developers report using AI coding tools at work" | GitHub-commissioned survey (Wakefield Research, 2024) |

### ✅ Qualified Claims (Acceptable)

| Location | Claim | Hedge |
|----------|-------|-------|
| L11 | Octoverse 97% caveat | "Even accounting for sampling bias" |
| L13 | Cursor ARR | "reportedly reached hundreds of millions in ARR faster than almost any developer tool" — double-hedged |
| L13 | Revenue figures generally | "reported or credibly estimated numbers from mid-2025" |
| L9 | Market velocity | "the figures will be outdated by the time you read this" |
| L79 | Capability matrix | "an honest snapshot" and "attempts something different" |
| L105 | Microsoft breadth | "factual observation" + "Whether breadth matters more than depth… is a decision each organization makes" |
| L156 | Gains prediction | "next 12–18 months" — time-bounded, inherently uncertain |
| L119 | Shadow IT scenario | Uses "may have" — conditional framing |

### ⚠️ Unverified Claims

**1. "Only viable option" in 2022**
- **Line/section**: L19
- **Claim**: *"In 2022, OpenAI's models were the only viable option for code generation at production quality."*
- **Issue**: Overstated. Salesforce CodeGen, BigCode/StarCoder predecessors, and Tabnine's own models existed. "Dominant" is defensible; "only viable" is not.
- **Recommendation**: Replace with *"the dominant option"* or *"the only option most developers had practical access to."*

**2. "Speed is unprecedented"**
- **Line/section**: L21
- **Claim**: *"the speed is unprecedented because the tools produce immediate, visible productivity gains"*
- **Issue**: "Unprecedented" is an unsupported superlative. Slack and other tools had comparable adoption velocity.
- **Recommendation**: *"the speed appears to exceed prior developer tool adoption curves"*

**3. Anthropic API revenue composition**
- **Line/section**: L13
- **Claim**: *"Anthropic's API revenue — much of it code-generation workloads — followed the same curve."*
- **Issue**: Anthropic has not disclosed revenue breakdown by use case. Unverifiable.
- **Recommendation**: Remove parenthetical or change to *"a significant portion of which is believed to come from code-generation workloads."*

**4. "At least a dozen well-funded products"**
- **Line/section**: L13
- **Claim**: *"the market includes at least a dozen well-funded products"*
- **Issue**: Only ~8 are named in the chapter. Vague count without enumeration.
- **Recommendation**: Either enumerate or change to *"more than ten."*

**5. "No organization has fully automated an end-to-end SDLC"**
- **Line/section**: L37
- **Claim**: *"No organization has fully automated an end-to-end SDLC with agents"*
- **Issue**: Unfalsifiable negative stated as absolute fact. Small teams using Devin for full cycles might dispute this.
- **Recommendation**: *"No organization has publicly demonstrated a fully automated end-to-end SDLC at production scale"* or *"To the author's knowledge…"*

**6. Enterprise tier pricing multiplier**
- **Line/section**: L111
- **Claim**: *"Enterprise tiers… typically run 2–3× the individual price."*
- **Issue**: Copilot Individual ($10) → Enterprise ($39) = 3.9×. Range is roughly correct but "typically" overgeneralizes.
- **Recommendation**: *"typically run 2–4× the individual price, depending on the vendor"*

**7. "92% of U.S.-based developers" — missing bias caveat**
- **Line/section**: L166
- **Claim**: GitHub survey "92%" figure
- **Issue**: Unlike the 97% Octoverse figure (which gets a sampling bias caveat on L11), this commissioned survey (n=1,000) gets no methodology note. Inconsistent treatment.
- **Recommendation**: Note it's a commissioned survey: *"A 2024 GitHub-commissioned survey (Wakefield Research, n=1,000) found…"*

**8. Capability matrix ratings — no methodology**
- **Line/section**: L81–93
- **Claim**: Every maturity cell (e.g., "Amazon Q Developer: Emerging for multi-file editing")
- **Issue**: Editorial assessments with no disclosed rating methodology. Any vendor could dispute any cell.
- **Recommendation**: Add methodology note: *"Ratings reflect publicly available features and documentation as of [month] 2025. 'Emerging' indicates a feature in public preview or limited availability."*

**9. "Code generation is the solved phase"**
- **Line/section**: L137
- **Claim**: *"code generation is the solved phase"*
- **Issue**: Overstatement. Code generation is mature but not "solved" — hallucinations, architectural coherence, complex refactoring remain hard. Most quotable, most challengeable.
- **Recommendation**: *"code generation is the most mature phase"* or *"the phase where current tools deliver the most reliable value."*

**10. "Eight of twelve developers" shadow IT**
- **Line/section**: L119
- **Claim**: *"a team of twelve engineers may have eight people using different AI tools, none approved by IT"*
- **Issue**: Reads like a specific data point despite using "may have." Borderline — the conditional framing helps but the specificity implies a measurement.
- **Recommendation**: Minor. Consider *"it's common for a majority of a team to be using unapproved tools."*

---

## Chapter 3: The Business Case

### ✅ Verified Claims

| Location | Claim | Basis |
|----------|-------|-------|
| L9 | "developers report writing code 55% faster" | GitHub Copilot research (Peng et al., 2023): 55.8% faster task completion |
| L9 | "tool X generates 46% of accepted code" | GitHub blog (Feb 2023): "46% of code is now written by AI" |
| L84 | Cycle time as a DORA metric | Lead time for changes is a canonical DORA metric |
| L107 | "Vibe Coding Cliff" concept | Defined in Ch1 L7/15 — internally consistent |

### ✅ Qualified Claims (Acceptable)

| Location | Claim | Hedge |
|----------|-------|-------|
| L11 | "coding is 20–35% of a developer's working time" | Range given, no false precision |
| L13 | "30–60% of AI-generated code on complex tasks requires meaningful rework" | "Industry data consistently shows" + range |
| L34 | "the other 70–80% of your actual investment" | Analogy framing |
| L40 | "$10–40/month per developer" | Realistic range for 2024–25 |
| L46 | "2–4 weeks of engineering time for initial context architecture" | Scoped to "team of 10–15 developers" |
| L50 | "token costs can reach $50–200 per developer per month" | "can reach" — appropriately hedged |
| L54 | "1–2 weeks of reduced productivity during learning curve" | Reasonable estimate |
| L62 | "first 60–90 days, your team will be slower" | Standard change management pattern |
| L66–74 | TCO table ranges | All given as ranges; called "estimates" |
| L84 | "reduce cycle time by 30–50%" | "within the agent's reliable capability range" |
| L86 | "Teams with mature context engineering report fewer convention-violation defects" | "Teams… report" — observation |
| L90 | "Teams that adopt agentic development well report higher job satisfaction" | "Teams… report" |
| L94 | "20–40% reduction on agent-suitable tasks" | Range; qualified to task type |
| L111 | "15–25%" improvement at inflection | Moderate range |
| L259 | "expect 20–40% improvements in cycle time" | Bounded to "well-scoped tasks with mature context" |
| L190 | "fully loaded cost $200,000/year each" | Used in worked example (plausible for US senior engineers) |

### ⚠️ Unverified Claims

**1. "Coding is 20–35% of a developer's working time"**
- **Line/section**: L11
- **Claim**: Stated as settled fact with no source.
- **Issue**: Plausible (consistent with MS Research time studies, Stripe survey) but the specific range needs attribution.
- **Recommendation**: Add citation: *"Studies of developer time allocation (Microsoft Research 2019, Stripe 2018) consistently find…"*

**2. "30–60% rework rate" — escalated framing**
- **Line/section**: L13
- **Claim**: *"Industry data consistently shows that 30–60% of AI-generated code on complex tasks requires meaningful rework"*
- **Issue**: **Framing inconsistency with Ch1.** Ch1 L23 says "Teams report that 30–60%…" (hedged). Ch3 escalates to "Industry data consistently shows" — a stronger epistemological claim for the same number. No citation in either chapter. This is the book's flagship number and its most weaponizable.
- **Recommendation**: Add specific citation(s) (GitClear 2024, Uplevel 2024, or similar). At minimum, align framing to Ch1's weaker hedge: *"Surveys and internal reports consistently suggest…"*

**3. "$200–600 per developer per year" — arithmetic gap**
- **Line/section**: L40
- **Claim**: Range stated for tooling costs.
- **Issue**: $10–40/mo × 12 = $120–480/yr individual. Enterprise at "2–3× higher" = $240–1,440/yr. The $200–600 range is awkwardly narrow for enterprise. A CFO would notice.
- **Recommendation**: Clarify: *"$200–600 per developer per year for team tiers; enterprise agreements with SSO, audit, and data-residency controls typically run $500–1,500."*

**4. "2–4 weeks for initial context architecture" — no provenance**
- **Line/section**: L46
- **Claim**: Presented as factual expectation.
- **Issue**: No basis given. Is this from the authors' experience? Case studies? Surveys?
- **Recommendation**: *"In our experience with teams adopting this methodology, expect 2–4 weeks…"*

**5. TCO table — no methodology**
- **Line/section**: L66–74
- **Claim**: Specific dollar ranges summing to "$77,000–229,000" for year 1 for a team of 10. The "8–13% of total for licenses" ratio is derived from these self-generated estimates.
- **Issue**: No methodology or source. The precision implies empirical grounding.
- **Recommendation**: Either cite sources or explicitly label as *"illustrative model"* rather than *"typical range."*

**6. "Reduce cycle time by 30–50%" — core value proposition**
- **Line/section**: L84
- **Claim**: No empirical source.
- **Issue**: This is the chapter's central value proposition. A CTO will demand: "whose cycle time? measured how?"
- **Recommendation**: Add citation or provenance. Even *"Early adopters with mature context report…"* is stronger.

**7. "Onboarding takes two weeks instead of two months"**
- **Line/section**: L88
- **Claim**: Specific durations: 75% reduction in onboarding time, no source.
- **Issue**: Extraordinary claim stated as fact.
- **Recommendation**: *"…takes weeks instead of months"* or present as hypothetical.

**8. Value driver timeline table — unsourced**
- **Line/section**: L94–97
- **Claim**: Specific timelines ("Months 4–6" for cycle time, "Months 6–9" for defect reduction) and percentages ("20–40%", "15–30%").
- **Issue**: Professional table format implies empirical backing. No source given.
- **Recommendation**: Add note: *"These timelines reflect patterns observed across early-adoption teams; your experience will vary."*

**9. "Technology change management research" — gestures without citing**
- **Line/section**: L103
- **Claim**: *"a pattern that technology change management research has documented repeatedly"*
- **Issue**: Invokes "research" without citing any.
- **Recommendation**: Add one citation (Rogers 1962; Moore 1991).

**10. "$1.5–2.5M in forgone throughput" — circular reasoning**
- **Line/section**: L249
- **Claim**: Cost-of-delay figure derived from the chapter's own worked example.
- **Issue**: Estimate derived from estimates, presented as a business argument. The conditionality is buried.
- **Recommendation**: Explicitly frame: *"Using the moderate scenario modeled above, a 12-month delay could represent $1.5–2.5M in forgone throughput — acknowledging that this depends entirely on the model's assumptions."*

**11. Fully loaded cost geography**
- **Line/section**: L190
- **Claim**: *"fully loaded cost $200,000/year each"*
- **Issue**: Not flagged as US-specific. Varies dramatically by geography.
- **Recommendation**: Add *"(US market, senior engineers)"* or *"adjust for your market."*

---

## Chapter 4: The Reference Architecture

### ✅ Verified Claims

| Location | Claim | Basis |
|----------|-------|-------|
| L13 | "The PROSE framework from Chapter 1 defines those constraints" | Internal cross-reference, consistent |
| L96 | "Production-ready across GitHub Copilot, Cursor, Claude Code, Windsurf" | Shipping products with public code-gen features |
| L95 | "Early implementations exist (GitHub Copilot, Claude)" for plan-phase ADR drafting | Both tools can draft structured documents |
| L99 | "Shipping in GitHub Copilot, Amazon Q" for automated code review | Both GA products |
| L180 | "70 files, 2,874 tests, roughly 90 minutes with three human interventions" | **Consistent with Ch1 L69** ✔️ |
| L229 | "custom instructions in GitHub Copilot, rule files in Cursor, `CLAUDE.md` in Claude Code" | Verifiable vendor documentation |

### ✅ Qualified Claims (Acceptable)

| Location | Claim | Hedge |
|----------|-------|-------|
| L11 | "No current AI system replaces these functions" | "current" scopes temporally |
| L80 | "these exist in early forms, but no tool reliably automates the judgment calls" | Explicit uncertainty |
| L95 | "accuracy varies significantly" | Acknowledged variance |
| L98 | "Generation works; strategic test design still requires human judgment" | Split claim with qualification |
| L101 | "no vendor ships reliable autonomous incident response" | "reliable autonomous" scopes the claim |
| L119 | "This is not a temporary state" | Grounded in Ch1's structural argument |
| L131–133 | Team A vs. Team B thought experiment | Clearly hypothetical |
| L178 | "two years of compounding context" | Logical argument, not empirical |
| L231 | "No single vendor covers all three context domains comprehensively today" | "today" scopes temporally |
| L129 | Model commoditization narrative | Analytical framing |

### ⚠️ Unverified Claims

**1. Market adoption distribution**
- **Line/section**: L86
- **Claim**: *"most organizations in mid-2025 have invested in the Build bucket, have minimal coverage in Intent, and almost none in Operate"*
- **Issue**: "Most organizations" with no survey or source.
- **Recommendation**: *"Based on vendor maturity and published adoption patterns, most organizations appear to have concentrated investment in Build…"*

**2. "One model family dominated" in 2022**
- **Line/section**: L129
- **Claim**: *"In 2022, one model family dominated code generation."*
- **Issue**: Unnamed model, no citation. Code Llama, AlphaCode existed.
- **Recommendation**: *"In 2022, OpenAI's Codex was the dominant commercial code-generation offering."*

**3. "At least five model families compete credibly"**
- **Line/section**: L129
- **Claim**: No enumeration or source.
- **Recommendation**: Enumerate in parenthetical or soften to *"several model families."*

**4. "Pricing falls as competition increases"**
- **Line/section**: L129
- **Claim**: General economic claim applied to AI models, no pricing data cited.
- **Recommendation**: Add concrete example (GPT-4 API price drops) or qualify as *"Pricing trends downward."*

**5. "Documenting conventions takes two days; payback in two weeks"**
- **Line/section**: L184
- **Claim**: Specific ROI numbers with no source.
- **Issue**: Reads as data-backed but appears illustrative.
- **Recommendation**: Frame as illustrative: *"In a representative scenario, documenting conventions might take two days…"*

**6. "Three to five convention violations per PR"**
- **Line/section**: L184
- **Claim**: Stated as fact, highly context-dependent.
- **Recommendation**: *"In teams we observed, pull request reviews frequently caught three to five convention violations…"*

**7. "Isolated tools" for Operate phase**
- **Line/section**: L84
- **Claim**: *"capabilities exist in isolated tools but not yet in integrated workflows"*
- **Issue**: PagerDuty, Datadog have shipped AI-assisted incident features that could be called "integrated."
- **Recommendation**: Name 1–2 tools and clarify what "integrated" means.

**8. Milestone gate thresholds — all seven unsourced**
- **Line/section**: L239–247
- **Claims**: ≥70% first-attempt linting pass rate; ≥15% review turnaround decrease; ≥10pp coverage increase; <30% rework rate; ≥20% intervention decline; ≥80% runbook coverage; ≥90% alert correlation accuracy
- **Issue**: Seven specific numeric thresholds presented as recommended gates. None sourced. Teams will use these as benchmarks.
- **Recommendation**: Add framing: *"The following thresholds are starting points based on patterns observed across early-adopter teams; calibrate them to your baseline."*

---

## Chapter 5: Governance for AI-Assisted Delivery

### ✅ Verified Claims

| Location | Claim | Basis |
|----------|-------|-------|
| L9 | Compliance frameworks require demonstrating authorized humans made deliberate choices | SOC 2 CC8.1, ISO 27001 A.14.2, PCI DSS Req. 6 |
| L52–57 | All SOC 2, ISO 27001, PCI DSS, HIPAA, EU AI Act control references | Control numbers verified ✔️ (see note on ISO edition below) |
| L73 | "This is an unsettled area of law" (AI-generated code IP/copyright) | Multiple active litigations (Andersen v. Stability AI, NYT v. OpenAI). No settled precedent. |
| L105 | "Model API pricing has changed frequently" | OpenAI, Anthropic, Google have all revised pricing multiple times |
| L116 | Airline autopilot skill degradation | FAA SAFO 13002 (2013); NTSB reports; Ebbatson et al. (2010) |
| L141 | "EU AI Act's human oversight requirements (Article 14)" | Art. 14 mandates human oversight for high-risk AI systems |
| L152 | "prompt injection is… a documented attack vector" | OWASP Top 10 for LLM Applications (2023): #1 risk |
| L173 | "EU AI Act entered into force in August 2024 with phased enforcement through 2027" | Official Journal July 12, 2024; in force August 1, 2024. Phased to 2027. |
| L173 | "Code-generating agents are not, by default, classified as high-risk" | Not in Annex III high-risk categories |
| L13 | Linters/compilers produce deterministic output | Well-established CS characterization |
| L185 | "Most major providers offer regional deployment options at enterprise tiers" | Azure, AWS, GCP — accurate |

### ✅ Qualified Claims (Acceptable)

| Location | Claim | Hedge |
|----------|-------|-------|
| L40 | "Most organizations… will find themselves in 'None' or 'Basic' for at least four of six areas" | "Most" — editorial judgment, acceptable |
| L65 | "risks that organizations… are encountering now" | Category description, not statistical claim |
| L71 | "Most major providers offer data retention and training opt-out guarantees" | "Most" — accurate for enterprise tiers |
| L101 | "Teams may find unassisted velocity is lower than before adoption" | "may find" — conditional |
| L116 | Financial analysts and model reliance | Supported by automation bias literature, though uncited |
| L185 | Regional deployment at enterprise tiers | "Most" and "enterprise tiers" — accurate |

### ⚠️ Unverified Claims

**1. "12–24 months out" for tooling maturity**
- **Line/section**: L42
- **Claim**: *"others depend on tooling maturity that is 12–24 months out"*
- **Issue**: Specific timeline prediction with no source. Will age poorly.
- **Recommendation**: *"…tooling maturity that, as of mid-2025, remains ahead of generally available products."*

**2. Compliance frameworks and "authorized humans"**
- **Line/section**: L9
- **Claim**: *"require demonstrating that authorized humans made deliberate choices"*
- **Issue**: Slightly overstated. Frameworks say "authorized individuals" or "personnel." Human-centricity is implicit, not explicit in all.
- **Recommendation**: *"authorized individuals"* or add *"(implicitly assuming human actors)"*

**3. "Every prior automation wave"**
- **Line/section**: L116
- **Claim**: *"It follows the same pattern observed in every prior automation wave"*
- **Issue**: "Every" is unfalsifiable.
- **Recommendation**: *"patterns well-documented in prior automation contexts, notably aviation and financial analysis."*

**4. ⚠️ Phase number inconsistency in board template**
- **Line/section**: L209
- **Claim**: Example shows "Phase 2 (agentic)" as current state, "Phase 3 by year-end" as target.
- **Issue**: **Cross-chapter inconsistency.** Ch2 defines Phase 2 as "Conversational assistance" and Phase 3 as "Agentic coding." The board template labels Phase 2 as "(agentic)" — contradicting the book's own model.
- **Recommendation**: Fix to either *"Phase 2 (conversational)" → "Phase 3 (agentic) by year-end"* or *"Phase 3 (agentic)" → "Phase 4 by year-end."*

**5. ISO 27001 edition ambiguity**
- **Line/section**: L52–57
- **Claim**: ISO control numbers A.12.4, A.9.2, A.9.4, A.14.2, A.13.2, A.12.1, A.18.2
- **Issue**: These are **ISO 27001:2013** Annex A numbering. The current standard is **ISO 27001:2022**, which renumbered all controls (e.g., A.12.4 → A.8.15). Organizations certified under 2022 won't recognize these.
- **Recommendation**: Specify *"ISO 27001:2013"* or add 2022 equivalents in parentheses.

**6. "Optimizes for plausibility" — technical imprecision**
- **Line/section**: L19
- **Claim**: *"Agent code is the output of a statistical process that optimizes for plausibility"*
- **Issue**: LLMs optimize for next-token prediction (cross-entropy loss), not "plausibility" directly. Acceptable shorthand for CTOs, but ML practitioners could challenge.
- **Recommendation**: *"optimizes for statistically likely token sequences — which correlates with plausibility but does not guarantee correctness."*

**7. "Thousands of instruction files"**
- **Line/section**: L103
- **Claim**: *"An organization with thousands of instruction files"*
- **Issue**: Most organizations have dozens to hundreds, not thousands. Scale may not yet exist.
- **Recommendation**: *"hundreds or thousands of instruction files"*

---

## Chapter 6: Team Structures

### ✅ Verified Claims

| Location | Claim | Basis |
|----------|-------|-------|
| L102 | "Team Topologies, the framework by Matthew Skelton and Manuel Pais" | *Team Topologies* (2019, IT Revolution) |
| L37 | "'10x developer' myth has persisted for decades" | Traces to Sackman, Erikson & Grant (1968); popularized by McConnell |
| L27 | "'10x faster coding' does not translate to '10x faster delivery'" | Analytical claim following from the chapter's own time-allocation premise |
| L108 | Cross-references to Ch1, Ch4, Ch5 | Internal — verifiable within the book |

### ✅ Qualified Claims (Acceptable)

| Location | Claim | Hedge |
|----------|-------|-------|
| L13 | Time-allocation table | "represents typical patterns, not universal truths — your distribution will vary" |
| L126 | Junior pipeline models (A/B/C) | "informed hypotheses, not proven patterns. No organization has run any of these for a full cycle…" — exemplary honesty |
| L134 | Whether new models produce capable engineers | "The honest answer is: we don't know yet." |
| L176 | Smaller, more-senior teams | "directional, not prescriptive" (L187) |
| L186–189 | Staffing table ratios | Two explicit caveats follow. |
| L228 | "The most common pattern in early assessments…" | Observational framing |

### ⚠️ Unverified Claims

**1. 🔴 CRITICAL: Misattributed sources for time-allocation table**
- **Line/section**: L13
- **Claim**: *"draws on industry data from the 2024 Stack Overflow Developer Survey, GitHub's Octoverse report"*
- **Issue**: **Neither source contains activity-level time-allocation data.** The 2024 SO survey covers tool adoption and productivity frictions — not the "30–35% writing new code" breakdown shown. The 2024 Octoverse covers language trends and global developer growth — zero time-allocation data. These are falsifiable claims about named sources. A journalist checking them would find the handbook wrong.
- **Recommendation**: **Replace the source attribution immediately.** Options: (a) Cite actual sources (GitHub 2022 developer productivity research, MS Research SPACE framework), (b) remove named sources and say *"synthesized from industry surveys and early adopter reports,"* (c) footnote distinguishing verifiable data from projections.

**2. Pre-agentic percentage breakdowns — no single source**
- **Line/section**: L15–23
- **Claim**: "Writing new code 30–35%", "Reading code 20–25%", "Code review 10–15%", etc.
- **Issue**: No study produces these exact breakdowns. The ~30% writing figure is loosely supported, but other rows lack citations.
- **Recommendation**: Add footnote: *"Pre-agentic ranges are composites from multiple industry surveys (2019–2023); no single source produces this exact breakdown."*

**3. Agentic-era percentages presented as data**
- **Line/section**: L15–23 ("With Agentic Tools" column)
- **Claim**: "Writing new code 10–15%", "Context engineering 10–15%", etc.
- **Issue**: No agentic-era time-allocation study exists. These are projections in a data-formatted table.
- **Recommendation**: Split into "Measured (Pre-Agentic)" and "Projected (Agentic)" or add column header.

**4. Staffing model numbers — pre-agentic uncited, agentic projected**
- **Line/section**: L178–183
- **Claim**: "6–10 engineers" → "4–7"; "Senior-to-junior ratio 1:2–1:3" → "1:1–2:1"
- **Issue**: Pre-agentic norms uncited; agentic numbers are pure projections.
- **Recommendation**: *"Pre-agentic ranges reflect common industry patterns (cf. Forsgren et al., Accelerate). Agentic ranges are projected from early adopter reports."*

**5. Mentorship investment percentage**
- **Line/section**: L197
- **Claim**: *"requires real mentorship investment from seniors (10–15% of their time)"*
- **Issue**: Specific percentage, no source.
- **Recommendation**: *"typically around 10–15% of their time, based on early adopter estimates."*

**6. Transition timeframes**
- **Line/section**: L195, L199
- **Claim**: "Over 12–18 months" (Path A); "Over 12–24 months" (Path C)
- **Issue**: Specific timeframes with no evidence. No organization has published data on this.
- **Recommendation**: Add *"roughly"* and parenthetical: *"(depending on attrition and hiring pace)"*

**7. "Most common pattern" in assessments — no sample**
- **Line/section**: L228
- **Claim**: *"The most common pattern in early assessments: high marks on senior presence and psychological safety, low marks on knowledge explicitness and context ownership."*
- **Issue**: "Early assessments" implies data collection. No sample size or methodology.
- **Recommendation**: *"A pattern we frequently observe…"* or cite the source.

**8. "10x developer myth" framing**
- **Line/section**: L37
- **Claim**: *"myth"* and *"Agentic development makes it obsolete."*
- **Issue**: Labeling 10x as a "myth" is editorial. The original research showed large variance; interpretation is debated. "Obsolete" is even stronger.
- **Recommendation**: Consider *"The '10x developer' idea"* instead of *"myth."*

**9. "Reviewing agent output is qualitatively harder"**
- **Line/section**: L19, L29
- **Claim**: No study cited comparing review difficulty of AI-generated vs. human-generated code.
- **Recommendation**: *"Early adopter teams report that reviewing agent output is qualitatively harder…"*

---

## Chapter 7: Planning the Transition

### ✅ Verified Claims

| Location | Claim | Basis |
|----------|-------|-------|
| L172 | DORA metrics: "deployment frequency, lead time, change failure rate, MTTR" | Canonical DORA definition (Forsgren, Humble, Kim) |
| L174 | DORA metrics "well-understood, widely adopted" | Industry standard, 9+ years of State of DevOps reports |
| L18 | "Lines of code, PR volume, and per-task cycle time all inflate apparent value" | Goodhart's Law applied to dev metrics — well-established |

### ✅ Qualified Claims (Acceptable)

| Location | Claim | Hedge |
|----------|-------|-------|
| L3–5 | Opening composite narrative | Reads as archetype, not specific case |
| L7 | "most common adoption trajectory" | Experiential observation (borderline — see Flag 1) |
| L63 | Phase timeline ranges | "ranges, not fixed schedules" with calibration guidance |
| L95 | "coaching model breaks at roughly a 1:3 ratio" | "roughly" provides hedging |
| L122 | "Phase 3… at least 12 months" for 400+ engineers | Prescriptive guidance, not empirical claim |
| L188 | "generation-to-review ratio around 1:1" early in adoption | Framed as expectation |

### ⚠️ Unverified Claims

**1. "Most common adoption trajectory"**
- **Line/section**: L7
- **Claim**: Stated as fact about the industry with no qualification.
- **Issue**: Agentic tools too new for large-scale adoption studies.
- **Recommendation**: *"a common adoption trajectory we see repeatedly"*

**2. Coaching capacity ratio — 1:3**
- **Line/section**: L95
- **Claim**: *"The coaching model breaks at roughly a 1:3 ratio"*
- **Issue**: Specific ratio, no citation. Where does 1:3 come from?
- **Recommendation**: *"in our experience, the model becomes strained beyond a 1:3 ratio."*

**3. Review rejection rate threshold — 60%**
- **Line/section**: L83
- **Claim**: *"Review rejection rate exceeds 60%"* as rollback trigger.
- **Issue**: Why 60%? No justification.
- **Recommendation**: Add rationale or acknowledge as starting point.

**4. "By week four, intervention should be trending down"**
- **Line/section**: L84
- **Claim**: Week-four inflection point asserted without evidence.
- **Recommendation**: *"In our experience, teams on well-scoped pilots see declining intervention by weeks 3–5."*

**5. Kill criteria — 40% threshold**
- **Line/section**: L138
- **Claim**: *"fewer than 40% of participating teams show measurable improvement… the transition is not producing organizational value."*
- **Issue**: High-stakes threshold (program termination) with no justification. Arbitrary number presented as principled.
- **Recommendation**: Provide basis or frame as suggested starting point.

**6. Generation-to-review ratios: 1.5:1, 3:1, 5:1**
- **Line/section**: L188
- **Claim**: Three thresholds presented as calibrated benchmarks.
- **Issue**: Most operationally consequential claim in the chapter. No source, no sample size. Teams will use these numbers.
- **Recommendation**: *"Based on our observation of early adopters, we suggest the following as starting benchmarks, to be calibrated against your own baselines."*

**7. Coach burnout threshold — 30%**
- **Line/section**: L112
- **Claim**: *"more than 30% of their time coaching"*
- **Issue**: Specific threshold with no justification.
- **Recommendation**: Soften → *"more than roughly a quarter to a third of their time"*

**8. "4–6 week" context layer build time**
- **Line/section**: L69
- **Claim**: *"4–6 week effort for a team starting from zero documentation"*
- **Issue**: Specific duration, highly variable, no justification.
- **Recommendation**: *"Based on early adopter experience, expect 4–6 weeks."*

**9. "Every week saved costs a month of remediation"**
- **Line/section**: L196
- **Claim**: Specific 1:4 ratio, no evidence.
- **Issue**: Rhetorically effective but empirically ungrounded.
- **Recommendation**: *"premature acceleration typically costs multiples of the time saved in later remediation."*

**10. "Negative data points spread faster than positive ones"**
- **Line/section**: L116
- **Claim**: Alludes to negativity bias without attribution.
- **Issue**: Low risk. Defensible as general psychology.
- **Recommendation**: Minor — consider *"as organizational research consistently shows"* for grounding.

---

## Cross-Chapter Consistency Audit

### Case Study Numbers (PR #394)

| Metric | Ch1 (L69) | Ch4 (L180) | Other Chapters | Status |
|--------|-----------|------------|----------------|--------|
| Files changed | 70 | 70 | Not referenced | ✅ Consistent |
| Tests passing | 2,874 | 2,874 | Not referenced | ✅ Consistent |
| Human interventions | 3 | 3 ("three") | Not referenced | ✅ Consistent |
| Wall-clock time | "roughly 90 minutes" | "roughly 90 minutes" | Not referenced | ✅ Consistent |

### 30–60% Rework Rate

| Chapter | Framing | Status |
|---------|---------|--------|
| Ch1 L23 | "Teams report that 30–60%…" | Hedged (observation) |
| Ch3 L13 | "Industry data consistently shows that 30–60%…" | Stronger claim (data) |
| **Assessment** | ⚠️ **Inconsistent framing.** Same number, different epistemic strength. Align to weaker (more honest) hedge. |

### Phase Model Numbering

| Source | Phase 2 | Phase 3 | Status |
|--------|---------|---------|--------|
| Ch2 | Conversational assistance | Agentic coding | Canonical definition |
| Ch5 L209 (board template) | "(agentic)" | Target | ⚠️ **Contradicts Ch2** |

### PROSE Constraint Naming

All five constraints (Progressive Disclosure, Reduced Scope, Orchestrated Composition, Safety Boundaries, Explicit Hierarchy) are named consistently across Ch1, Ch4, Ch5, and Ch6. ✅

---

## Recommendations Summary

### 🔴 Critical (fix before publication)

| # | Chapter | Issue |
|---|---------|-------|
| 1 | Ch6 | **Misattributed sources** — 2024 SO Survey and Octoverse cited for data they don't contain |
| 2 | Ch5 | **Phase number inconsistency** — board template contradicts Ch2's phase model |
| 3 | Ch3/Ch1 | **30–60% rework rate** — flagship number, no citation, inconsistent framing between chapters |

### 🟡 High Priority (a skeptical CTO would challenge)

| # | Chapter | Issue |
|---|---------|-------|
| 4 | Ch2 | "Code generation is the solved phase" — overstatement |
| 5 | Ch7 | Kill criteria (40%) and ratio thresholds — consequential numbers, unsourced |
| 6 | Ch3 | TCO table and "cost of delay" figure — circular reasoning risk |
| 7 | Ch1 | "Context windows have grown 100×" — false precision |
| 8 | Ch2 | "Only viable option" in 2022 — factually incorrect |
| 9 | Ch5 | ISO 27001 edition ambiguity (2013 vs. 2022 numbering) |
| 10 | Ch3 | "Onboarding takes two weeks instead of two months" — extraordinary claim, no source |

### 🟢 Low Priority (qualify with a word or two)

| # | Pattern | Fix |
|---|---------|-----|
| 11 | Multiple chapters | Add "roughly", "in our experience", or "early adopters report" to specific thresholds |
| 12 | Ch1, Ch2 | Add temporal qualifiers ("as of 2025") to vendor landscape claims |
| 13 | Ch3, Ch4, Ch7 | Frame illustrative numbers as illustrative ("in a representative scenario…") |
| 14 | Ch7 | Add brief rationale for operational thresholds (60% rejection, 40% kill, 1:3 coaching) |

---

*Total claims audited: ~165. Of these, 47 verified, 57 qualified, 61 flagged. The manuscript is directionally honest and generally well-hedged for an opinionated practitioner handbook. The 3 critical flags and 7 high-priority flags represent the claims most likely to undermine credibility if challenged by a skeptical reader.*
