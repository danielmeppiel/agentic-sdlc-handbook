# Fact & Reference Check — Block 2 + Closing (Chapters 8–15)

**Auditor:** Fact & Reference Checker — Claims Auditor
**Scope:** Chapters 8–15 (Block 2 practitioner content + closing)
**Date:** 2025-07-24

---

## Chapter 8: The Practitioner's Mindset

### Verified claims (no action needed)
- "An agent is not predicting your next line. An agent is attempting to execute a task — reading files, making decisions about structure, writing code across multiple locations, running tests, interpreting failures." — Verifiable from public agent tool documentation (Copilot, Cursor, Claude Code).
- "It has no persistent memory of your codebase. It cannot learn from last week's code review. Every time you dispatch it, it starts from zero." — Verifiable structural property of current LLM-based agents (stateless sessions).
- PR #394 forward-reference: "70 files changed, 90 minutes, 3 human interventions" — Consistent with Ch13's detailed accounting (see cross-chapter audit below).

### Qualified claims (acceptable as-is)
- "Most developers first encounter AI coding tools as autocomplete." — Qualified by "most"; widely observed pattern.
- "Most failures in agentic development trace back to the planning phase, not the execution phase." — Author's observation based on experience; framed as a generalization, not a statistic.
- "If you are making non-trivial corrections to more than 20–30% of an agent's output on a given task, the specification was wrong or the task was wrong for an agent." — Framed as a heuristic ("the discipline is to recognize"), not a researched threshold.

### ⚠️ Unverified claims (action required)

#### Flag 8.1 — Intervention characterization must match Ch13
- **Line/section:** ~Line 71 (Three roles paragraph)
- **Claim:** "The third was test triage: a test failed after wave completion, and the practitioner traced the cause to an ordering issue in the migration and directed a targeted fix. That was the Reviewer."
- **Issue:** Ch13 (line 216) describes Intervention 3 as occurring "during Wave 2b" after replacement agents completed. The Ch8 description says "after wave completion" which is vague — it could mean after Wave 2 or after Wave 2b. This is borderline but could confuse a reader cross-referencing.
- **Recommendation:** Tighten to match Ch13: "after the recovery wave (Wave 2b)" for precision.

---

## Chapter 9: The Instrumented Codebase

### Verified claims (no action needed)
- "Six categories of primitives cover the full range of knowledge an agent needs." — Author's framework definition; internally consistent across the chapter (Instructions, Agents, Skills, Prompts, Memory, Orchestration).
- Tool compatibility table (line 276): GitHub Copilot supports `.instructions.md` with `applyTo`, Cursor uses `.cursor/rules/*.mdc`, Claude Code uses `CLAUDE.md`, Windsurf uses `.windsurfrules`. — Verifiable from public documentation; qualified with "as of mid-2025."
- "Most tools natively support two of six." — Derivable from the compatibility table.
- "Agent configurations are the least portable." — Derivable from the compatibility table.

### Qualified claims (acceptable as-is)
- "You'll typically get 30-60 items" (conventions list during audit) — Qualified with "typically"; presented as practitioner experience.
- "Most projects need 8-12 instruction files." — Qualified with "most"; author's observation.
- "If your instruction file exceeds 40-50 lines, it's trying to do too much." — Framed as guidance, not a researched limit.

### ⚠️ Unverified claims (action required)

#### Flag 9.1 — Before/after metrics lack sourcing
- **Line/section:** ~Line 537–547 (metrics table)
- **Claim:** "Convention-violating outputs: 40-60% uninstrumented → Under 10% instrumented. Agent-generated code requiring rewrite: 30-50% → Under 15%. Time from agent output to merge: Hours → Minutes."
- **Issue:** The text says "Based on projects that have undergone this transformation, including the reference case documented throughout this book." This is qualified but the ranges are suspiciously precise. Multiple "projects" are referenced but only one (PR #394) is documented. The 40-60% / 30-50% ranges and the "Under 10%" / "Under 15%" figures read as estimates, not measurements.
- **Recommendation:** Either (a) add "In the author's experience" qualifier to make the source explicit, or (b) tighten the attribution to the specific reference case: "In the reference case, convention-violating outputs dropped from roughly half to under 10%." The current phrasing implies a broader evidence base than one documented case study.

#### Flag 9.2 — "150 lines of markdown distributed across 8 files"
- **Line/section:** ~Line 534
- **Claim:** "The difference is not the model. The difference is 150 lines of markdown distributed across 8 files."
- **Issue:** This is specific and measurable — but only for the example shown. If the before/after is based on the reference case (PR #394 codebase), this is verifiable. If it's a constructed example, it should say so.
- **Recommendation:** Clarify whether this is from the reference case or a representative example. Both are fine; the distinction matters for credibility.

---

## Chapter 10: The PROSE Specification

### Verified claims (no action needed)
- PROSE acronym expands to: Progressive Disclosure, Reduced Scope, Orchestrated Composition, Safety Boundaries, Explicit Hierarchy. — Author's framework definition; consistent with Ch1 (line 60-65).
- "PROSE defines five constraints." — Consistent count across Ch1, Ch10, Ch14, Ch15.
- Constraint-to-property mappings match Ch1's table exactly.
- Anti-pattern names (Monolithic Prompt, Context Dumping, Unbounded Agent, Flat Instructions, Scope Creep) match Ch1 (lines 91-95) and Ch14 (patterns 1-5) exactly.

### Qualified claims (acceptable as-is)
- Three failure stories (fintech with hierarchy but no disclosure, platform team with scope but no composition, enterprise team with boundaries but no scope) — Presented as team experiences; anonymized but specific enough to be credible anecdotes. Not verifiable but appropriately framed.
- "1,400 words of OWASP token reference, 900 words of session management spec, 600 words of rate-limiting policy" — Specific word counts in a scenario. Plausible but unverifiable; acceptable as illustration.

### ⚠️ Unverified claims (action required)

*No unverified claims requiring action.* This chapter is primarily a framework specification with worked examples. Claims are definitional (the author's framework) or qualified anecdotes.

---

## Chapter 11: Context Engineering

### Verified claims (no action needed)
- "Information at the beginning and end gets more weight; content in the middle degrades." — Well-documented LLM property (the "lost in the middle" phenomenon, documented in Liu et al. 2023 and widely replicated). Could benefit from a citation but is a verified property.
- Context budget diagram segments and percentages are presented as approximations (~5-10%, ~15-25%, etc.), clearly labeled as "roughly."

### Qualified claims (acceptable as-is)
- "A 40-line instruction file outperforms a 400-line one that covers the same material with less focus." — Qualified as a consequence of the attention model; framed as a practical observation.
- "Shorter sessions produce better results than longer ones." — Qualified as a consequence of context budget mechanics.
- "after 20+ turns" / "roughly 30-40 turns" session reset heuristics — Framed as practitioner guidance.

### ⚠️ Unverified claims (action required)

#### Flag 11.1 — 128K context window attribution
- **Line/section:** ~Line 36
- **Claim:** "On a 128K-token window — common for models like Claude Sonnet or GPT-4"
- **Issue:** As of mid-2025, Claude Sonnet models support 200K tokens (not 128K). GPT-4 Turbo supports 128K. The claim groups these models together under "128K" which is inaccurate for Claude Sonnet.
- **Recommendation:** Either (a) change to "On a 128K-to-200K-token window — common in current frontier models" or (b) remove specific model names and say "On a 128K-token window — a common baseline for current models" since the budget math is illustrative.

#### Flag 11.2 — Token-to-lines conversion
- **Line/section:** ~Line 46
- **Claim:** "Those 20K instruction tokens are roughly 800 lines of markdown."
- **Issue:** At ~25 tokens/line for markdown, 20K / 25 = 800. The math is reasonable for English markdown prose, but varies significantly by content density. Code-heavy markdown can run 30-40 tokens/line. This is an approximation presented as a fact.
- **Recommendation:** Add "approximately" or "for typical prose" — the current phrasing implies precision that depends on content type.

---

## Chapter 12: Multi-Agent Orchestration

### Verified claims (no action needed)
- "The boundary between 10 and 15 files is not arbitrary" — Justified by the reasoning about conversation history consumption. Presented as a practical heuristic with the appropriate caveat "Your mileage will vary."
- One-file-one-agent rule — well-reasoned from string-matching edit mechanics; verifiable in current agent tooling.
- Wave-based parallelism with commit-and-test checkpoints — described as a methodology, not an external claim.
- Four-level escalation protocol (L1-L4) — author's framework definition.

### Qualified claims (acceptable as-is)
- "A wave with 2-3 agents completes in the time it takes the slowest agent to finish — typically 3-5 minutes. A wave with 8 agents still takes 8-10 minutes." — Qualified with "typically"; presented as practitioner observation.
- "40-60% of total human time spent on coordination" — Qualified as "for a well-planned execution."

### ⚠️ Unverified claims (action required)

#### Flag 12.1 — ⚠️ CRITICAL: Intervention characterization contradicts Ch8 and Ch13
- **Line/section:** ~Line 295
- **Claim:** "In the PR #394 execution, 3 human interventions were needed across 15 agent dispatches. Two of those were design conflicts that the priority ordering did not fully resolve."
- **Issue:** This directly contradicts Ch8 (line 71) and Ch13 (lines 210-218), which describe the 3 interventions as: (1) a **scope decision** during planning — the Architect role; (2) an **agent stall/recovery** during Wave 2 — the Escalation Handler role; (3) a **test triage** after Wave 2b — the Reviewer role. **None** of these are described as "design conflicts" in Ch8 or Ch13. A design conflict (per Ch12's own definition at line 291) is when "two agents produce output that reflects genuinely different design philosophies." The three interventions described in Ch13 involve a scoping judgment, a recovery decision, and a bug fix — not design philosophy disagreements between agents.
- **Recommendation:** Fix this sentence. Options: (a) Revise to match Ch13's categorization: "One was a scope decision, one was an agent recovery, and one was test triage — none resolvable by the priority ordering alone." (b) If the author intends a different interpretation, reconcile across all three chapters. This is the most significant cross-chapter inconsistency in Block 2.

#### Flag 12.2 — Escalation distribution math doesn't add up
- **Line/section:** ~Line 326
- **Claim:** "The distribution was roughly 80% autonomous (L1), 13% automated retry (L2), and 7% human decision (L3/L4)."
- **Issue:** 7% of 15 dispatches = ~1 human decision. But the same case study documents 3 human interventions. Either (a) the percentage base is not "dispatches" (it could be total decision points, including sub-tasks), or (b) the percentages don't match the PR #394 data. 3/15 = 20% human intervention rate, not 7%.
- **Recommendation:** Clarify the denominator. If the base is "total decision points" (which includes sub-decisions within agent sessions), state that explicitly. If it's dispatches, the numbers are wrong and should be corrected to roughly 67% L1, 13% L2, 20% L3/L4.

#### Flag 12.3 — Agent count in timeline doesn't sum to 15
- **Line/section:** ~Lines 226, 334
- **Claim:** "15 agents dispatched" (also in Ch13 line 183)
- **Issue:** The Ch13 timeline accounts for: 2 (audit) + 2 (Wave 0) + 5 (Waves 1&2 combined) + 2 (Wave 2b) + 1 (Wave 3) = **12 agents**. Three agents are unaccounted for. The "Waves 1 and 2" description (Ch13 line 200) is ambiguous: "Five parallel agents covering verbose logging coverage (Wave 1) and CommandLogger migration (Wave 2)" — but these waves were sequential. It's unclear whether "Five" is per-wave or total across both.
- **Recommendation:** Expand the Waves 1 and 2 description in Ch13 to clarify the per-wave agent count. If the total is truly 15, show where each agent was dispatched. If the timeline is a summary that omits some dispatches (e.g., retry agents), note that.

#### Flag 12.4 — "Parallelism saved approximately 21 minutes"
- **Line/section:** ~Line 226
- **Claim:** "The parallelism saved approximately 21 minutes compared to sequential execution."
- **Issue:** This implies a comparison between the observed 24-minute parallel execution and an estimated 45-minute sequential execution (24 + 21 = 45). The sequential estimate is not shown or justified in Ch12. Ch12 line 336 estimates sequential single-agent time at "60-75 minutes of agent time" — but that's a different comparison (single-agent vs. multi-agent, not parallel vs. sequential multi-agent). The "21 minutes" figure is unanchored.
- **Recommendation:** Show the math: state the sequential estimate and how 21 minutes of savings was calculated.

#### Flag 12.5 — Human time breakdown percentages
- **Line/section:** ~Line 334
- **Claim:** "Planning and partitioning (~30% of human time), monitoring execution (~20%), handling interventions (~25%), and post-execution review (~25%)."
- **Issue:** These are presented as findings from the PR #394 case but have the precision of rounded estimates. They sum to 100% correctly. Applied to the stated "roughly 45 minutes" of human time: 13.5 min planning, 9 min monitoring, 11.25 min interventions, 11.25 min review. These are plausible but unverifiable.
- **Recommendation:** Qualify as "approximately" or "in our experience" — currently presented as measured data from a single case.

#### Flag 12.6 — Single-agent comparison is estimated, not measured
- **Line/section:** ~Line 336
- **Claim:** "The same 70-file change executed sequentially by a single agent would take an estimated 60-75 minutes of agent time... expect 2-3 additional rework cycles... Total single-agent elapsed time: roughly 90-120 minutes with lower output quality."
- **Issue:** The word "estimated" is present, and "Based on similar single-agent attempts on changes of this scale" provides qualification. However, the "2-3 additional rework cycles" and the total time range are estimates of a counterfactual. The qualification is adequate but the comparison should not be mistaken for a controlled experiment.
- **Recommendation:** Acceptable as-is with the "estimated" and "Based on similar attempts" qualifiers. No change needed, but flagging for awareness.

---

## Chapter 13: The Execution Meta-Process

### Verified claims (no action needed)
- PR #394 metrics table (lines 177-187): 70 files, +5,886/−1,030, 30 commits, 2,874 tests, 15 agents dispatched, 3 human interventions, ~90 minutes. — Internal case study data; self-consistent within Ch13.
- "Zero regressions detected by the test suite" with the honest caveat: "not proof of correctness — it is proof that no tested behavior changed." — Appropriately qualified.
- Five-phase meta-process (Audit → Plan → Wave → Validate → Ship) — author's methodology definition.
- Three interventions map to Ch8's three roles (Architect, Escalation Handler, Reviewer) — consistent with Ch8 line 71.

### Qualified claims (acceptable as-is)
- "Your first time through this process will take roughly 3×" — Qualified as "roughly"; framed as guidance.
- "2,874 tests taking approximately 2 minutes per run, across 5 checkpoints — roughly 10 minutes of testing total." — Math checks: 5 × 2 = 10. Consistent.
- "A 70-file change took 90 minutes regardless of whether the codebase has 10,000 lines or 10 million." — Framed as a property of the methodology ("proportional to the change, not the codebase").

### ⚠️ Unverified claims (action required)

#### Flag 13.1 — 30 commits for a 70-file change
- **Line/section:** ~Line 181
- **Claim:** "Commits: 30"
- **Issue:** The chapter describes roughly 5 wave executions (Wave 0, Wave 1, Wave 2, Wave 2b, Wave 3). Even with one commit per agent per wave, the timeline accounts for ~13 execution agents. With checkpoint commits, you'd expect ~5-15 commits, not 30. The 30-commit figure implies granularity not explained in the timeline (e.g., per-file commits, intermediate commits during waves, or multiple commit rounds).
- **Recommendation:** Either (a) explain the commit granularity that produces 30 commits (e.g., "one commit per agent task plus wave-level checkpoint commits") or (b) verify the number matches the actual PR.

#### Flag 13.2 — Audit completed in 3 minutes
- **Line/section:** ~Line 194
- **Claim:** "Audit (3 minutes). Two explore agents dispatched in parallel... produced severity-ranked findings with file-and-line citations."
- **Issue:** Producing severity-ranked, citation-level audit findings across a codebase that spans 70 files in 3 minutes is remarkably fast. This is plausible for an expert with mature agent configurations on a familiar codebase, but the timeline reads as a best-case run. The later caveat (line 190) about first-timers expecting 3× partially addresses this.
- **Recommendation:** The 3× caveat at line 190 is adequate, but consider moving it **before** the timeline rather than after, so readers encounter the expectation calibration before the impressive-sounding numbers.

#### Flag 13.3 — Wave 2b "7 minutes" includes diagnosis
- **Line/section:** ~Line 259
- **Claim:** "Total cost of the adaptation: 7 minutes, including diagnosis, plan adjustment, agent dispatch, and re-validation."
- **Issue:** The Wave 2b section (line 202) says "Recovery (7 minutes)" and describes: diagnosing a stall, inspecting partial work, deciding to split across 2 agents, dispatching them, and re-validating. Seven minutes for all of this is very tight. Plausible for an experienced practitioner but impressively fast.
- **Recommendation:** Acceptable as-is given the 3× first-timer caveat. Flagging for awareness.

---

## Chapter 14: Anti-Patterns and Failure Modes

### Verified claims (no action needed)
- "19 distinct ways" — The taxonomy table lists exactly 19 numbered anti-patterns. Consistent with the claim.
- "Patterns 1–5 are the foundational anti-patterns from Chapter 1." — Verified: Ch1 lines 91-95 list exactly these 5 anti-patterns (Monolithic Prompt, Context Dumping, Unbounded Agent, Flat Instructions, Scope Creep) with matching constraint violations.
- Anti-pattern-to-constraint mappings match Ch1 and Ch10 consistently:
  - Monolithic Prompt → Orchestrated Composition ✓
  - Context Dumping → Progressive Disclosure ✓
  - Unbounded Agent → Safety Boundaries ✓
  - Flat Instructions → Explicit Hierarchy ✓
  - Scope Creep → Reduced Scope ✓
- "All nineteen are real. All nineteen have cost teams real time, money, and trust." — Author's assertion based on experience; framed as such.

### Qualified claims (acceptable as-is)
- "An agent generating 70 files in 90 minutes produces more review surface area than a human in the same timeframe." — Reasonable inference from the PR #394 case study; not a comparative measurement but a logical observation.
- "Token cost trending — flag any week-over-week spike >25%" — Presented as a team-level checklist recommendation, not a researched threshold.
- Failure scenario descriptions (400-line instructions file, SQL injection from conflicting rules, etc.) — Presented as illustrative scenarios, not documented incidents.

### ⚠️ Unverified claims (action required)

#### Flag 14.1 — Opening vignettes presented as specific incidents
- **Line/section:** Lines 3-4
- **Claim:** "The wave execution model exists because a developer tried to run 15 agents at once and got a merge conflict graveyard. The checkpoint discipline exists because someone skipped testing after wave 2 and spent three hours debugging a cascade that started in wave 1."
- **Issue:** These are presented as specific historical incidents ("a developer," "someone") but are unattributed. They could be the author's experience, a colleague's experience, or composite examples. The specificity ("15 agents," "three hours") creates an expectation of a real incident.
- **Recommendation:** Either (a) attribute: "In our early experiments..." or (b) qualify: "Teams have reported..." The current phrasing implies documented incidents without providing documentation.

---

## Chapter 15: What Comes Next

### Verified claims (no action needed)
- "REST did not make HTTP better. It gave engineers constraints to reason about distributed systems. Twenty-five years later, the constraints still hold." — REST was defined in Roy Fielding's 2000 doctoral dissertation. 25 years from 2000 = 2025. Factually accurate.
- Three-tier honesty framework (Available now / Emerging / Directional) self-assessment table — Author's framework applied to the author's own claims; transparently structured.

### Qualified claims (acceptable as-is)
- "Everything in this book will be partially obsolete within eighteen months." — Clearly labeled as the author's prediction; framed with appropriate confidence hedging.
- "Tool-using agents become the default interaction mode" — Classified as "Available now" with "High" confidence. Verifiable from public product announcements (GitHub Copilot agent mode, Cursor agent mode, Claude Code).
- "Multi-agent orchestration enters mainstream tooling" — Classified as "Available now" with "High" confidence. Verifiable from early production tooling.
- "Full lifecycle agent coverage becomes operational" — Classified as "Directional" with "Low-to-medium" confidence. Appropriately hedged.
- "15–20% rather than the 2–3x some claim" — The "2–3x" reference is to vendor productivity claims (e.g., GitHub's developer survey data, various industry reports). The "some claim" qualifier is accurate. The "15-20%" figure is the author's more conservative estimate — clearly positioned as the author's opinion.

### ⚠️ Unverified claims (action required)

#### Flag 15.1 — "The way CI/CD became a category a decade ago"
- **Line/section:** ~Line 19
- **Claim:** "Agent governance platforms will be a category — the way CI/CD became a category a decade ago."
- **Issue:** CI/CD as a category has roots going back further than "a decade." Jenkins (2011), Travis CI (2011), CircleCI (2011) are ~14 years old. The "decade" is an approximation but could be tightened.
- **Recommendation:** Minor — change to "the way CI/CD became a category over the past decade" or remove the timeframe. Not a significant issue.

#### Flag 15.2 — Orchestrated Composition in the "What Will Not Change" section
- **Line/section:** ~Line 49
- **Claim:** All five PROSE constraints are mapped to structural properties in the "What Will Not Change" section.
- **Issue:** This was flagged by a prior review as missing Orchestrated Composition. However, **the current text does include it** (line 49): "Orchestrated Composition addresses the complexity that emerges when multiple agents interact." The prior review's concern has been addressed.
- **Recommendation:** No action needed. Noting for the record.

---

## Cross-Chapter Consistency Audit

### PR #394 Numbers

| Metric | Ch8 | Ch12 | Ch13 | Ch14 | Consistent? |
|---|---|---|---|---|---|
| Files changed | 70 | 70 | 70 | 70 (implied) | ✅ Yes |
| Wall-clock time | 90 min | ~90 min | ~90 min | 90 min (implied) | ✅ Yes |
| Human interventions | 3 | 3 | 3 | — | ✅ Yes |
| Agents dispatched | — | 15 | 15 | 15 (opening) | ✅ Yes |
| Tests passing | — | — | 2,874 | — | ✅ (single source) |
| Lines +/- | — | — | +5,886/−1,030 | — | ✅ (single source) |
| Commits | — | — | 30 | — | ✅ (single source) |
| Concerns | — | 5 | 5 | — | ✅ Yes |
| Waves | — | 4 (+1 recovery) | 4 (+1 recovery) | — | ✅ Yes |
| Agent execution time | — | 24 min | 24 min (derivable) | — | ✅ Yes |
| Human time | — | ~45 min | — | — | ✅ (single source) |

### ⚠️ PR #394 Intervention Characterization — INCONSISTENT

| Chapter | Intervention 1 | Intervention 2 | Intervention 3 |
|---|---|---|---|
| **Ch8** (line 71) | Scope decision (Architect) | Agent recovery (Escalation Handler) | Test triage (Reviewer) |
| **Ch12** (line 295) | — | — | — |
| **Ch12 claim** | "Two of those were **design conflicts** that the priority ordering did not fully resolve" |
| **Ch13** (lines 212-216) | Scope decision (Architect) | Agent recovery (Escalation Handler) | Test triage (Reviewer) |

**Ch8 and Ch13 agree.** Ch12 contradicts both by characterizing 2 of 3 interventions as "design conflicts." This must be reconciled — see Flag 12.1.

### ⚠️ PR #394 Escalation Distribution — INCONSISTENT

| Source | L3/L4 Rate | Implied count (of 15) |
|---|---|---|
| Ch12 line 326 | 7% | ~1 |
| Ch8, Ch13 | 3 interventions | 3/15 = 20% |

**3 human interventions out of 15 dispatches = 20%, not 7%.** See Flag 12.2.

### PROSE Constraint Names — CONSISTENT ✅

| Constraint | Ch1 | Ch8 | Ch9 | Ch10 | Ch11 | Ch12 | Ch13 | Ch14 | Ch15 |
|---|---|---|---|---|---|---|---|---|---|
| Progressive Disclosure | ✅ | — | ✅ | ✅ | ✅ | — | — | ✅ | ✅ |
| Reduced Scope | ✅ | — | — | ✅ | — | — | — | ✅ | ✅ |
| Orchestrated Composition | ✅ | — | — | ✅ | — | — | — | ✅ | ✅ |
| Safety Boundaries | ✅ | — | — | ✅ | — | — | — | ✅ | ✅ |
| Explicit Hierarchy | ✅ | — | — | ✅ | ✅ | — | — | ✅ | ✅ |

All five constraint names are used consistently across every chapter that references them. No drift in naming.

### Anti-Pattern Names — CONSISTENT ✅

The five foundational anti-patterns (Monolithic Prompt, Context Dumping, Unbounded Agent, Flat Instructions, Scope Creep) use identical names in Ch1 (lines 91-95), Ch10 (anti-pattern sections), and Ch14 (patterns 1-5 with expanded scenarios).

### Primitive Count — CONSISTENT ✅

"Six primitive types" is stated consistently in Ch9 (lines 5, 274, 316, 586) and referenced in Ch11. The six are: Instructions, Agents, Skills, Prompts, Memory, Orchestration — consistent throughout.

### Anti-Pattern Count — CONSISTENT ✅

"19 distinct ways" (Ch14 line 5) matches the taxonomy table (19 numbered entries) and the closing line (line 452: "These 19 patterns").

---

## Summary of Action Items

### Critical (must fix before publication)

| Flag | Chapter | Issue | Action |
|---|---|---|---|
| **12.1** | Ch12 | "Two of those were design conflicts" contradicts Ch8 and Ch13's intervention descriptions | Revise Ch12 line 295 to match Ch8/Ch13 characterization |
| **12.2** | Ch12 | 7% L3/L4 rate implies ~1 intervention; case study has 3 (=20%) | Fix the percentages or clarify the denominator |

### High (should fix)

| Flag | Chapter | Issue | Action |
|---|---|---|---|
| **12.3** | Ch12/Ch13 | Timeline accounts for ~12 agents, not 15 | Expand Waves 1 and 2 description to show per-wave agent count |
| **13.1** | Ch13 | 30 commits unexplained by the timeline structure | Explain the commit granularity |
| **11.1** | Ch11 | 128K attributed to "Claude Sonnet or GPT-4" — Claude Sonnet is 200K | Fix model-to-window-size attribution |

### Medium (recommended)

| Flag | Chapter | Issue | Action |
|---|---|---|---|
| **9.1** | Ch9 | Before/after metrics imply broader evidence than one case study | Add "In the author's experience" or tighten attribution |
| **12.4** | Ch12 | "21 minutes saved" is unanchored | Show the sequential estimate math |
| **14.1** | Ch14 | Opening vignettes sound like specific incidents but are unattributed | Add "In our early experiments" or similar |
| **12.5** | Ch12 | Human time breakdown percentages are estimates presented as findings | Qualify with "approximately" |

### Low (optional polish)

| Flag | Chapter | Issue | Action |
|---|---|---|---|
| **8.1** | Ch8 | Intervention 3 description slightly vaguer than Ch13 | Tighten wording to match |
| **9.2** | Ch9 | "150 lines across 8 files" — unclear if reference case or example | Clarify provenance |
| **11.2** | Ch11 | Token-to-lines conversion presented without margin | Add "approximately" |
| **15.1** | Ch15 | "CI/CD became a category a decade ago" — slightly imprecise | Minor wording adjustment |

---

## Auditor's Notes

**Overall assessment:** Block 2 is technically rigorous and honest in its hedging. The three-tier honesty framework in Ch15 demonstrates self-awareness about claim strength. The PR #394 case study is the credibility anchor for the entire block, and its numbers are internally consistent **except** for the intervention characterization (Ch12 vs. Ch8/Ch13) and the escalation distribution math (Ch12). These two issues in Ch12 are the only critical findings — they create contradictions that a careful reader cross-referencing chapters will catch.

**Strongest chapters for factual integrity:** Ch10 (pure framework specification), Ch14 (explicit about experience-based claims), Ch15 (transparent about uncertainty).

**Chapter requiring most attention:** Ch12, due to the two critical inconsistencies in PR #394 characterization and the escalation math.
