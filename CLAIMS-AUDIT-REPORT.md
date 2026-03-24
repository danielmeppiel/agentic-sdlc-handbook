# Full Manuscript Claims Audit Report

**Document:** The Agentic SDLC Handbook  
**Scope:** 15 chapters + 4 case studies + index (~78,140 raw words)  
**Audit date:** Current HEAD (694c6af)  
**Auditor:** Fact & Reference Checker — full manuscript pass  
**Prior audit:** FACT-CHECK-SYNTHESIS.md (pre-remediation)  
**Remediation commits reviewed:** e6e4913 ("remediation sweep"), 046e7e4 ("footnotes to practitioner block"), cf77ff4 ("replace fabricated pricing"), 6e06691 ("replace hallucinated annotated session")

---

## Summary Statistics

| Category | Count | % of Total |
|----------|-------|-----------|
| **Total factual claims audited** | ~215 | 100% |
| ✅ Verified (cited source or reproducible) | ~72 | 33% |
| ✅ Qualified (honestly hedged, author attribution) | ~68 | 32% |
| 🟡 Qualified-but-weak (hedge present, insufficient) | ~42 | 20% |
| 🟠 Unverified (no source, no qualification) | ~18 | 8% |
| 🔴 Verifiably wrong or self-contradictory | ~4 | 2% |
| 🔴 Critical — must fix before publication | ~8 | 4% |
| **Cross-chapter inconsistencies** | **6** | — |
| **Missing citations** | **3** | — |

**Improvement since prior audit:** The remediation sweep fixed the most critical items — word count updated to ~68,000 (from 62,500), "authored entirely" softened, Liu et al. citation added, Baumeister citation added, practitioner block received footnotes (ch07–ch12 now have citations), pricing updated. However, **several medium-severity issues remain** and **two new inconsistencies have been introduced** by the fixes themselves.

---

## 1. CRITICAL ISSUES (Must-Fix Before Publication)

### 🔴 #1. WAVE COUNT INCONSISTENCY — "5 waves" vs "9 waves" vs "4 waves + 1 recovery"

This is the most serious cross-chapter inconsistency remaining in the manuscript.

| Source | What it says |
|--------|-------------|
| **Case study** (line 104) | "nine waves" across "five phases" |
| **Case study** (line 275) | "~25 [dispatches] across 9 waves in 5 phases" |
| **Ch12** (line 212) | "four waves plus one recovery wave" (= 5 waves) |
| **Ch13** (line 235) | "5 checkpoints (4 waves + final validation)" |
| **Ch13** (line 285) | "75 files and ~25 agents across 5 waves (including one recovery wave)" |
| **Case study wave table** | Lists 5 named phases: Foundation, Auth wiring, Logger wiring, Tests, Ship |

**The problem:** The case study says 9 waves in 5 phases. Ch12 and Ch13 say 4-5 waves. These are different numbers for the same execution. Presumably, the "5 phases" contained sub-waves totaling 9, but this is never reconciled. A reader comparing the case study to Ch12/Ch13 will see "9 waves" vs "5 waves" and assume one is wrong.

**Damage level:** 🔴 CRITICAL. The wave count is a core structural metric of the book's primary evidence.

**Recommendation:** Add a note to the case study canonical metrics reconciling the count: "9 waves organized into 5 phases. Chapters 12 and 13 reference the 5 phases; the case study details all 9 waves." Or update Ch12/Ch13 to say "5 phases comprising 9 waves."

---

### 🔴 #2. SESSION COUNT CONTRADICTION — "single session" vs "2 sessions"

| Source | What it says |
|--------|-------------|
| **Ch09** (line 654) | "Duration: 207 turns, **single session**" |
| **Case study** (line 7) | "~16 hours wall-clock across **2 sessions**" |
| **Case study** (line 282) | "2 sessions including planning, monitoring, breaks" |

**The problem:** Ch09 describes the PR #394 execution as a "single session" of "207 turns." The case study says it was "2 sessions." These cannot both be true.

**Damage level:** 🔴 CRITICAL. A reader who checks both sources will find a flat contradiction.

**Recommendation:** Determine the ground truth. If there were 2 sessions, Ch09 should say "207 turns across 2 sessions." If 207 turns was one session with a separate planning session, clarify: "207 turns in the execution session (planning was a separate session)."

---

### 🔴 #3. MERMAID DIAGRAM COUNT — "25" claims vs 37 actual

The prior audit flagged "15 Mermaid diagrams" as verifiably wrong. The remediation updated this to "25 Mermaid diagrams." However:

| Claimed | Actual count |
|---------|-------------|
| "25 Mermaid diagrams" (case-study-handbook-writing lines 181, 284) | **25 in handbook chapters** (correct at time of writing) |
| "25 Mermaid diagrams confirmed" (case-study-publishing-pipeline line 47) | **Now 25 in chapters** — this was correct |
| "all 24 blocks" (case-study-publishing-pipeline line 86) | **Now 25** — off by 1 |
| "37 Mermaid diagrams rendered" (case-study-publishing-pipeline line 169) | **Actual total: 37** — this is the final count including case studies |

**The problem:** The publishing-pipeline case study has *both* "24 blocks" (line 86, referring to the sed conversion) and "37 Mermaid diagrams rendered" (line 169, the summary). Meanwhile the handbook-writing case study claims "25 Mermaid diagrams." The "24 blocks" reference is a historical artifact from the conversion — it may have been accurate at that point. But the summary line (37) contradicts the body (24/25).

**Damage level:** 🟠 HIGH. The numbers are internally inconsistent within the same case study.

**Recommendation:** The publishing-pipeline case study needs to reconcile: "A bulk `sed` conversion fixed all 25 chapter blocks [update from 24]; the total across all files including case studies grew to 37." The summary line (37) is correct for the total.

---

### 🔴 #4. N=1 GENERALIZATION — "15–20% starting hypothesis" (Ch12)

**Location:** `handbook/ch12-multi-agent-orchestration.qmd` line 317

**Current text:** "We use 15–20% as a starting hypothesis for well-planned work, though this has not been validated across multiple teams."

**Assessment:** The remediation improved this from "is typical" to "starting hypothesis...not validated across multiple teams." This is substantially better hedging. However, the same paragraph then says: "Rates significantly above 20% may indicate underspecified plans. Rates below 5% warrant scrutiny." These prescriptive thresholds (20%, 5%) are derived from the same N=1 observation and create diagnostic benchmarks from insufficient evidence.

**Damage level:** 🟡 MODERATE (improved from 🔴 CRITICAL). The qualification helps. The prescriptive thresholds still overreach.

**Recommendation:** Add to the prescriptive sentences: "These thresholds are initial calibration points from our reference case study, not validated benchmarks." Or soften to: "In our experience, rates significantly above 20% correlated with underspecified plans."

---

### 🔴 #5. Ch12 TIME INCONSISTENCY — "24 minutes" vs "~90 minutes"

Ch12 presents two different time figures for the same execution:

| Location | Metric | Value |
|----------|--------|-------|
| Ch12 line 212 | "wave execution time" | "roughly 24 minutes" |
| Ch12 line 360 | "agent execution" | "24 minutes of agent execution" |
| Ch12 line 360 | "total elapsed time" | "roughly 90 minutes" |
| Case study line 281 | "wave execution time" | "~90 minutes" |
| Ch01, Ch04, Ch08, Ch13 | "wave execution time" | "~90 minutes" |

**The problem:** Ch12 line 212 says "four waves plus one recovery wave handled 75 files in roughly **24 minutes of wave execution time**." Every other chapter and the canonical metrics say "~90 minutes" of wave execution time. The ~90 minutes appears in Ch12 line 360 as "total elapsed time" — but that contradicts the case study which defines ~90 minutes as "wave execution time" and ~16 hours as "total elapsed time."

Ch12 appears to use "wave execution time" to mean "pure agent computation time" (24 min), while every other chapter uses it to mean "active agent + human review time during the execution phase" (90 min). This redefinition within a single chapter is confusing.

**Damage level:** 🔴 CRITICAL. The 24-minute figure appears only in Ch12 and seems to represent a different measurement than every other chapter's ~90 minutes. A reader will see "24 minutes" in Ch12 and "90 minutes" in Ch13 for the same PR and assume error.

**Recommendation:** Ch12 should define its terms explicitly: "24 minutes of pure agent computation time (the time agents spent actively generating code), versus ~90 minutes of wave execution time (including human review between waves)." Make the "roughly 90 minutes" in Ch12 line 360 explicitly match the case study's canonical definition.

---

### 🟠 #6. PRICING CLAIMS — Need "as of [date]" disclaimers

**Location:** `handbook/ch03-the-business-case.qmd` lines 46–50

The pricing table cites specific prices:
- GitHub Copilot: Free / $10 Pro / $39 Pro+; $19/user/mo Business; $39/user/mo Enterprise
- Cursor: Free / $20 Pro / $60 Pro+; $40/user/mo Business
- Claude: Free / $20 Pro / $100+ Max; $25/seat/mo Team; $20/seat + usage Enterprise

The text also claims: "GitHub Copilot Enterprise includes 1,000 premium requests per user per month" and "a single request to a frontier model like Claude Opus 4.6 consumes multiple premium requests."

**Assessment:** These prices are approximately correct as of mid-2025 but will become stale. The "Claude Opus 4.6" model name reference embeds a specific model version that dates the content.

**Damage level:** 🟠 HIGH. Pricing changes quarterly. A reader in 6 months will find these numbers wrong.

**Recommendation:** Add "Pricing as of Q2 2025; verify current rates at each vendor's site" to the table footer. The case study already uses "~68,000 words" with the tilde convention — apply the same approach here. Consider referencing "Claude Opus" without the version number, or "a frontier model" generically.

---

### 🟠 #7. SQUAD CITATION DATE — "March 2026" (future-dated)

**Location:** Ch04 line 303, Ch09 line 795, Ch15 line 187

The Squad citation reads: `Brady Gaster, "How Squad Runs Coordinated AI Agents Inside Your Repository," GitHub Blog, March 2026.`

**Assessment:** If this book is being published before March 2026, this citation refers to a future publication. If it's already been published, the date needs verification.

**Damage level:** 🟡 MODERATE. A future-dated citation is unusual but not necessarily wrong if the content is scheduled. However, citing an unpublished source as evidence undermines the claim that relies on it.

**Recommendation:** Verify the publication date. If the blog post hasn't been published yet, either (a) note "forthcoming" or (b) remove the citation and describe Squad based on the public repository only.

---

### 🟠 #8. CONVENTION VIOLATION NUMBERS STILL UNRECONCILED (Ch03 vs Ch09)

| Source | Claim |
|--------|-------|
| Ch03 line 113 | "15–30% reduction in convention violations" |
| Ch09 line 602 | "Convention-violating outputs: 40-60% → Under 10%" |

The footnote in Ch03 (line 326) now explains: "Chapter 9 reports a wider range (40–60% dropping to under 10%) for teams with mature instrumentation. The difference reflects adoption stage."

**Assessment:** The reconciliation footnote is a significant improvement. However, the Ch03 claim says "15–30% *reduction*" (a relative change) while Ch09 says "40–60% → under 10%" (absolute levels, implying ~75-83% relative reduction). The footnote's explanation doesn't fully resolve this mathematical inconsistency: a 15–30% reduction from a 40–60% base would produce 28–51%, not "under 10%."

**Damage level:** 🟡 MODERATE. The footnote helps but the math doesn't add up.

**Recommendation:** Clarify that Ch03's "15-30% reduction" means a different thing than Ch09's absolute rate change. Perhaps: "15-30% fewer convention violations caught in review" (Ch03) vs "convention violation rate in generated code drops from 40-60% to under 10% with mature instrumentation" (Ch09). These can coexist if Ch03 is measuring review catches and Ch09 is measuring generation-time violations.

---

## 2. CROSS-CHAPTER INCONSISTENCIES (Complete List)

| # | Metric | Ch/Location A | Ch/Location B | Issue |
|---|--------|--------------|--------------|-------|
| 1 | Wave count | Case study: "9 waves in 5 phases" | Ch12/13: "4-5 waves" | Unreconciled (Critical #1 above) |
| 2 | Session count | Ch09: "single session" | Case study: "2 sessions" | Flat contradiction (Critical #2 above) |
| 3 | Wave execution time | Ch12 line 212: "24 minutes" | All others: "~90 minutes" | Different definitions (Critical #5 above) |
| 4 | Mermaid count | Publishing case study line 86: "24 blocks" | Publishing summary line 169: "37 diagrams" | Internal inconsistency (Critical #3 above) |
| 5 | Convention violations | Ch03: "15-30% reduction" | Ch09: "40-60% → under 10%" | Math doesn't reconcile (Issue #8 above) |
| 6 | Test count mid-execution | Ch13 line 235: "~2,850 tests" | Case study: counts are 2,829→2,839→2,846→2,874→2,897 | ~2,850 is reasonable approximation of mid-point — ✅ acceptable |

---

## 3. WHAT WAS FIXED SINCE PRIOR AUDIT (FACT-CHECK-SYNTHESIS.md)

The remediation sweep (commits e6e4913, 046e7e4, cf77ff4, 6e06691) addressed:

| Prior Issue | Status | Assessment |
|-------------|--------|-----------|
| #1 Word count "62,500" | ✅ **FIXED** — Updated to "~68,000" | Actual wc -w: 78,140 total / ~69,000 handbook chapters. "~68,000" is close enough with YAML/code exclusion. |
| #2 "15 Mermaid diagrams" | 🟡 **PARTIALLY FIXED** — Updated to "25" | 25 in chapters is correct. But "24 blocks" still appears in publishing case study line 86, and "37" in line 169. Internal inconsistency remains. |
| #5 "Research consistently shows" (Ch07) | ✅ **FIXED** — Baumeister citation added | footnote [^ch7-bad] now cites Baumeister et al. 2001. |
| #6 Context budget false precision (Ch11) | 🟡 **PARTIALLY ADDRESSED** — Liu et al. citation added | The "lost in the middle" effect now has a citation. The "40-line outperforms 400-line" claim now reads "In our experience" — improved. Budget percentages still lack derivation methodology. |
| #10 Lost-in-the-middle citation (Ch11) | ✅ **FIXED** — Liu et al. 2023 added | footnote [^ch11-middle] |
| "Authored entirely" contradiction | ✅ **FIXED** — No longer in text | Removed from case study. |
| Block 2 citation desert | ✅ **FIXED** — 14 footnotes added to Ch08-Ch15 | Ch08: 2 footnotes (Flyvbjerg, Sweller). Ch09: 4 footnotes. Ch10: 2 footnotes. Ch11: 1 footnote. Ch12: 2 footnotes (Brooks, SAE). Ch13: 2 footnotes (Brooks, Conway). Ch14: 1 footnote (Perez). Ch15: 5 footnotes. |
| PR #394 time disambiguation | ✅ **FIXED** in Ch01, Ch04, Ch08 — now say "wave execution time" | All main-chapter references now specify "wave execution time." But Ch12 introduced a new inconsistency (24 min vs 90 min — see Critical #5). |
| Intervention count | ✅ **FIXED** in Ch01, Ch04 | Ch01 now says "3 execution-phase interventions (5 total including verification)." Ch08 provides the full reconciliation. |
| Fabricated pricing | ✅ **FIXED** — Real vendor data | Commit cf77ff4 replaced fabricated pricing with real vendor data. Still needs "as of" date. |
| "3-5 days manually" counterfactual | ✅ **FIXED** — Qualified | Case study line 287 now reads: "This estimate has not been formally benchmarked." |
| Ch09 annotated session | ✅ **FIXED** — Replaced hallucinated data | Commit 6e06691 replaced fabricated session with real PR #394 data. |

---

## 4. REMAINING UNVERIFIED CLAIMS (Priority Order)

### Tier 1 — Claims presented as fact without source or qualification

| # | Chapter | Line | Claim | Issue | Recommendation |
|---|---------|------|-------|-------|---------------|
| 1 | Ch02 | 17 | "Gartner estimated in 2024 that by 2028, 75% of enterprise software engineers will use AI code assistants — up from fewer than 10% in early 2023" | No specific Gartner report ID cited. "Gartner estimated" is attributed but unverifiable without the report reference. | Add footnote with Gartner report title/ID, or note "widely reported Gartner estimate" |
| 2 | Ch03 | 62 | "token costs can reach $50–200 per developer per month" | No source. Author's observation? Industry data? | Add "based on our observation of teams using agentic workflows" or cite a source |
| 3 | Ch03 | 82-88 | TCO table ($95K–$249K for 10-person team) | Derived from unsourced component estimates. The "context engineering: $20,000–60,000" and "training: $15,000–40,000" ranges have no derivation methodology. | Add footnote: "Ranges based on the author's advisory work with early-adopter teams. Your costs will vary by region, seniority, and tooling maturity." |
| 4 | Ch06 | 158 | "60–70% of their first year" reviewing agent-generated code | False precision for a training recommendation. | Change to "most of their first year" or add "in our suggested model" |
| 5 | Ch09 | 602 | "Convention-violating outputs: 40-60% → Under 10%" in table | Table format implies data. Footnote [^ch9-lint] addresses linting but not the specific numbers. | Add table note: "Observed in the APM project. Your baseline will vary by codebase maturity." |
| 6 | Ch12 | 352 | "67% autonomous (L1), 13% automated retry (L2), and 20% human decision (L3/L4)" | Derived from N=1 execution. Presented with false precision to two significant figures. | Round to "roughly two-thirds / one-eighth / one-fifth" or explicitly note "in our reference case" |
| 7 | Ch12 | 362 | Sequential estimate: "60-75 minutes of agent time" + "2-3 additional rework cycles" | Counterfactual comparison — estimated, not measured | Already qualified ("Based on similar single-agent attempts") — acceptable as-is |
| 8 | Ch13 | 321 | "regardless of whether the codebase has 10,000 lines or 10 million" | Scaling claim from one data point | Already qualified ("though we have verified this only at the scale documented") — acceptable |

### Tier 2 — Claims with weak but present hedging

| # | Chapter | Line | Claim | Assessment |
|---|---------|------|-------|-----------|
| 1 | Ch01 | 25 | "30–60% of agent-generated code on complex tasks requires significant rework" | ✅ Well-cited (Stack Overflow + GitClear) with honest qualifier "no controlled study has established a definitive figure." |
| 2 | Ch03 | 100 | "25–55% task completion time compression" | ✅ Well-cited (Peng 55.8%, Cui 26%, DORA qualifier). Range is honest. |
| 3 | Ch03 | 289 | "$1.5–2.5M in forgone throughput improvement" | 🟡 Qualifier exists but dollar amount dominates. "Illustrative, not predictive" helps. |
| 4 | Ch07 | lines ~195-249 | Generation-to-review ratios (1:1, 3:1, 1.5:1, 5:1) | 🟡 Labeled "starting benchmarks" — adequate but 4 specific ratios from unspecified observations creates false precision |
| 5 | Ch07 | ~195 | "fewer than 40%" kill criterion | 🟡 Labeled "suggested threshold" — acceptable with strengthened context |
| 6 | Ch11 | 30 | "40-line instruction file produces more consistent output than a sprawling 400-line one" | 🟡 Now prefaced with "In our experience" — improved from prior audit |

---

## 5. RESEARCH CITATIONS AUDIT

### ✅ Properly cited research claims

| Claim | Citation | Chapter |
|-------|----------|---------|
| Copilot 55.8% task completion | Peng et al. 2023, arXiv:2302.06590 | Ch03 |
| 26% increase in completed tasks | Cui et al. 2024, Microsoft Research | Ch03 |
| DORA 21% flow efficiency | DORA 2025 report | Ch03 |
| Stack Overflow 76% adoption, 45% "bad" at complex | 2024 SO Survey | Ch01 |
| 66% "almost right but not quite" | 2025 SO Survey | Ch01, Ch03 |
| GitClear code churn | GitClear 2025/2026 analyses | Ch01, Ch03 |
| Lost-in-the-middle effect | Liu et al. 2023 (NeurIPS 2024) | Ch11 |
| Negativity bias | Baumeister et al. 2001 | Ch07 |
| Case study methodology | Flyvbjerg 2006 | Ch08 |
| Cognitive load theory | Sweller 1988 | Ch08 |
| Sycophantic behavior | Perez et al. 2022 | Ch14 |
| Conway's Law | Conway (via Brooks) | Ch13 |
| Brooks's Mythical Man-Month | Brooks 1975 | Ch12, Ch13 |
| SAE driving automation levels | SAE J3016 | Ch12 |
| Constraints & creativity | Stokes 2005 | Ch10 |
| ISO 27001, SOC 2, PCI DSS | Standard references | Ch05 |

### 🟡 Attributed but unverifiable

| Claim | Attribution | Issue |
|-------|------------|-------|
| Gartner 75% by 2028 | "Gartner estimated in 2024" | No report ID. Widely reported but reader can't verify specific source. |
| Cursor ARR $100M+ | Footnote cites "Sacra, 2024" | Third-party estimate — footnote appropriately notes "Anysphere has not confirmed." |
| GitHub Copilot revenue | "Microsoft has cited...in quarterly earnings calls" | No specific earnings call date. |

### ⚠️ Remaining gaps

| Claim | Location | Issue |
|-------|----------|-------|
| "adoption surveys consistently show the same split" | Ch01 line 25 | Vague — which surveys beyond SO? The footnote cites SO and GitClear but "surveys" (plural) implies more. |
| "two-pizza teams" concept | Ch06 | ✅ Already cited (AWS whitepaper link present) |

---

## 6. CROSS-REFERENCE INTEGRITY

All cross-chapter references were verified:

| Reference | Source | Target | Status |
|-----------|--------|--------|--------|
| "Chapter 14" for anti-patterns | Ch01 line 120 | Ch14 exists, covers anti-patterns | ✅ |
| "Chapter 13 traces a real pull request" | Ch08 line 75 | Ch13 §PR #394 exists | ✅ |
| "Chapter 8 described" role shift | Ch09 line 748 | Ch08 covers role shift | ✅ |
| "Chapter 11 provides the methodology" | Ch04 line 193 | Ch11 covers context engineering | ✅ |
| "Chapter 2" for maturity phases | Ch05 line 46, Ch06 line 124 | Ch02 covers phases | ✅ |
| "Chapter 9, under the constraints from Chapter 10" | Ch15 line 127 | Both chapters exist with correct content | ✅ |
| "Chapters 10 through 12" | Ch13 line 7 | All three exist with stated topics | ✅ |
| Case study links (../case-study-apm-overhaul.qmd) | Ch08, Ch12, Ch13, Ch14 | File exists | ✅ |
| PR #394 URL (github.com/microsoft/apm/pull/394) | Multiple chapters | External link — verifiable | ✅ (reader-verifiable) |

**No broken cross-references found.** All chapter references point to content that matches the description.

---

## 7. CASE STUDY INTERNAL CONSISTENCY

### PR #394 Canonical Metrics (Case Study) vs. Chapter References

| Metric | Case Study (canonical) | Ch01 | Ch04 | Ch08 | Ch09 | Ch12 | Ch13 | Status |
|--------|----------------------|------|------|------|------|------|------|--------|
| Files changed | 75 | 75 | 75 | 75 | 75 | 75 | 75 | ✅ Consistent |
| Tests start | 2,829 | — | 2,829 | — | 2,829 | — | 2,829 | ✅ Consistent |
| Tests end | 2,897 | 2,897 | 2,897 | — | 2,897 | — | 2,897 | ✅ Consistent |
| Test net change | +68 (115 written, 47 consolidated) | — | — | — | — | — | +68 | ✅ Consistent |
| Agent dispatches | ~25 | — | — | — | — | ~25 | ~25 | ✅ Consistent |
| Execution interventions | 3 | 3 | 3 | 3 | — | 3 | — | ✅ Consistent |
| Total escalations | 5 | "5 total including verification" | "5 total including verification" | "+2 additional" = 5 | — | — | 5 | ✅ Consistent |
| Wave execution time | ~90 min | ~90 min | ~90 min | ~90 min | — | **24 min** / **~90 min** | ~90 min | 🔴 INCONSISTENT (see #5) |
| Wall-clock time | ~16 hours | — | — | "~16-hour" | — | — | — | ✅ Consistent where mentioned |
| Sessions | 2 sessions | — | — | — | "single session" | — | — | 🔴 INCONSISTENT (see #2) |
| Waves | 9 waves in 5 phases | — | — | — | — | "4+1" = 5 | "5 waves" | 🔴 INCONSISTENT (see #1) |
| Plan iterations | 8 (v1-v8) | — | — | — | — | — | 8 | ✅ Consistent |
| Planned files | 47 | — | — | — | — | — | — | Case study explains expansion: "additional 28 were test files, configuration updates, and documentation changes" ✅ |

### Handbook-Writing Case Study

| Metric | Claim | Verification | Status |
|--------|-------|-------------|--------|
| Word count | ~68,000 | `wc -w handbook/*.qmd` = 69,062 | ✅ Close enough with tilde |
| Chapters | 15 | Count of ch*.qmd files = 15 | ✅ |
| Personas | 11 (8 + 3 dynamic) | Described in case study | ✅ Self-consistent |
| Mermaid diagrams | 25 | Handbook `grep -c`: 25 | ✅ |
| Fact-check flags | 75 (5 critical) | Self-referential — this audit is the evidence | ✅ Self-consistent |

### Publishing-Pipeline Case Study

| Metric | Claim | Verification | Status |
|--------|-------|-------------|--------|
| "37 Mermaid diagrams rendered" (line 169) | 37 | Actual count: 37 (25 handbook + 12 case studies) | ✅ |
| "all 24 blocks" (line 86) | 24 | Current count: 25 in chapters | 🟡 Off-by-one (may have been accurate at time of that conversion) |
| "3 output formats" | HTML, PDF, EPUB | Described in case study | ✅ |
| "49-second CI deploy" | 49 seconds | Self-reported, plausible | ✅ Qualified |

---

## 8. ASSERTIONS PRESENTED AS UNIVERSAL TRUTHS

Claims that are opinions or single-observation generalizations presented without adequate qualification:

| # | Location | Assertion | Issue | Severity |
|---|----------|----------|-------|----------|
| 1 | Ch12:317 | "Rates significantly above 20% may indicate underspecified plans" | N=1 → diagnostic threshold | 🟡 Moderate |
| 2 | Ch12:317 | "Rates below 5% warrant scrutiny" | N=1 → diagnostic threshold | 🟡 Moderate |
| 3 | Ch13:321 | "time spent scales with the change scope, not the full codebase size" | N=1 scaling law | 🟡 Qualified ("we have verified this only at the scale documented") |
| 4 | Ch11:30 | "Context is not free" | Truism — uncontroversial | ✅ Fine |
| 5 | Ch15:13 | "Within a year, tool-using agents will be the default interaction mode" | Predictive claim | ✅ Proper three-tier framework used |
| 6 | Ch04:164 | "highest-ROI starting investment for any team" | Superlative claim | 🟡 "Any team" is too broad — should be "most teams" |
| 7 | Ch06:78 | "A team of solid engineers with a well-maintained context layer will outperform a team of exceptional engineers working in a knowledge vacuum" | Comparative claim with no evidence | 🟡 Reads as principle, not tested hypothesis |

---

## 9. TOOL/TECHNOLOGY CAPABILITY CLAIMS

| Claim | Location | Assessment |
|-------|----------|-----------|
| `.github/copilot-instructions.md` file format | Ch09 | ✅ Correct — documented by GitHub |
| `.cursorrules` / `.cursor/rules/` | Ch09 | ✅ Correct — documented by Cursor |
| `.claude/` directory / `CLAUDE.md` | Ch09 | ✅ Correct — documented by Anthropic |
| Model Context Protocol (MCP) | Ch09, Ch15 | ✅ Correct — publicly documented standard |
| `plugin.json` manifest for Claude | Ch09, Ch15 | ✅ Correct — documented by Anthropic |
| Squad / Spec-Kit references | Ch04, Ch09, Ch15 | 🟡 Squad citation is future-dated (March 2026) — see Issue #7 |
| "GitHub Copilot Enterprise includes 1,000 premium requests" | Ch03 | 🟡 Approximately correct as of mid-2025. Subject to change. |
| "Claude Opus 4.6 consumes multiple premium requests" | Ch03 | 🟡 Correct as of current pricing. Model version will become stale. |

---

## 10. TOP 10 CLAIMS NEEDING IMMEDIATE ATTENTION

Ranked by credibility damage × fix difficulty:

| # | Issue | Location | Severity | Fix Effort |
|---|-------|----------|----------|-----------|
| 1 | **Wave count: "9 waves" vs "5 waves"** | Case study vs Ch12/Ch13 | 🔴 Critical | Low — add reconciliation note |
| 2 | **Session count: "single session" vs "2 sessions"** | Ch09 vs Case study | 🔴 Critical | Low — update Ch09 |
| 3 | **Ch12 time: "24 minutes" vs "~90 minutes"** | Ch12 vs all others | 🔴 Critical | Low — clarify definitions |
| 4 | **Mermaid "24 blocks" vs 25 actual** | Publishing case study line 86 | 🟠 High | Low — update number |
| 5 | **Pricing needs "as of" date** | Ch03 pricing table | 🟠 High | Low — add footnote |
| 6 | **Squad citation future-dated "March 2026"** | Ch04, Ch09, Ch15 | 🟡 Moderate | Low — verify or update |
| 7 | **N=1 diagnostic thresholds (5%, 20%)** | Ch12 line 317 | 🟡 Moderate | Low — add qualification |
| 8 | **Convention violation math (15-30% vs 75-83%)** | Ch03 vs Ch09 | 🟡 Moderate | Medium — clarify what each measures |
| 9 | **TCO table lacks derivation** | Ch03 lines 82-88 | 🟡 Moderate | Medium — add footnote |
| 10 | **"Any team" superlative** | Ch04 line 164 | 🟡 Low | Low — change to "most teams" |

---

## 11. STRUCTURAL OBSERVATIONS

### Citation Density (Post-Remediation)

| Block | Chapters | Footnotes | Assessment |
|-------|----------|-----------|-----------|
| Part I (C-suite) | Ch01–Ch03 | ~17 | ✅ Well-cited |
| Part II (Architecture) | Ch04–Ch07 | ~8 | ✅ Adequate (improved) |
| Part III (Practitioner) | Ch08–Ch15 | ~16 | ✅ Adequate (dramatically improved from 0) |
| Part IV (Case Studies) | 4 case studies | 0 | 🟡 No external citations, but case studies are primary evidence — acceptable |

The "citation desert" problem has been substantially addressed. Ch08–Ch15 now average ~2 footnotes per chapter. The practitioner block's disclaimer (Ch08 line 7) about experiential evidence is excellent — it establishes the evidentiary basis for the entire block.

### PROSE Framework Consistency

- "Five constraints" count: ✅ Consistent across Ch10, Ch04, case studies
- Constraint names (P-R-O-S-E): ✅ Consistent everywhere
- Primitive types listed in Ch09: ✅ Self-consistent

### Hedging Quality (Best and Worst)

**Best hedging in the manuscript:**
1. Ch15 three-tier honesty framework (Available / Emerging / Directional)
2. Ch08 line 7 practitioner block disclaimer
3. Ch12 line 212 "estimated, not measured" parallelism comparison
4. Ch03 line 100 "within the agent's reliable capability range" qualifier
5. Case study line 287 "This estimate has not been formally benchmarked"

**Worst remaining hedging:**
1. Ch12 line 317 prescriptive thresholds (5%, 20%) from N=1
2. Ch09 line 602 table format implies data for N=1 observation
3. Ch04 line 164 "highest-ROI starting investment for any team"
4. Ch12 line 352 false-precision percentages (67%, 13%, 20%) from N=1

---

## 12. CONCLUSION

The manuscript's credibility profile has improved substantially since the prior audit. The remediation sweep addressed the most damaging issues — word count, pricing, citation desert, authorship claims. The remaining critical items are primarily **cross-chapter consistency failures** (wave count, session count, time metrics) that are easy to fix but high-damage if left unfixed.

**Bottom line:** The book's evidentiary standard is honest for a practitioner guide. It does not overclaim research backing it doesn't have. The Ch08 disclaimer inoculates the practitioner block. The remaining fixes are mechanical (reconcile numbers) rather than philosophical (change the claims). Fix the 3 cross-chapter contradictions (#1, #2, #3 above) and this manuscript's credibility stands up to skeptical scrutiny.

---

*End of claims audit report. Generated from full-manuscript review of all 20 .qmd files.*
