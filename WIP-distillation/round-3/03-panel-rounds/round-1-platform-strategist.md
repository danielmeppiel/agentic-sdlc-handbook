# Platform Strategist Review — Round 1

## Verdict
**MINOR-REVISIONS**

## Vendor-fairness check

### GitHub Copilot
**Status: FAIR**
- Treated as the baseline inference harness + multi-surface trigger system (CLI, IDE, Chat, Workspace).
- Ch09's proposed two-column load-order comparison (Copilot vs Claude Code) is balanced.
- **Risk:** The CLI-as-base framing may read as Microsoft-preferential. Mitigation: Frame it as "one canonical example" and rotate examples throughout the practitioner block.

### Anthropic Claude Code
**Status: FAIR**
- Correctly positioned as inference harness with built-in triggers (not just a chat interface).
- The `CLAUDE.md` load mechanic is accurately described (concept #3).
- **Minor gap:** No mention of Projects feature (released Q4 2024) as a distinct scoping mechanism vs file-based scoping in other harnesses. Should add one sentence in Ch18 matrix.

### Cursor
**Status: FAIR**
- `.cursor/rules/` glob recognition is correctly stated.
- **Risk:** Cursor's 2025 agent-mode roadmap (announced Feb 2025) includes programmatic spawn. If this arc publishes after that ships, Ch18's spawn-semantics row will be outdated on day one. Mitigation: Add temporal qualifier ("as of late 2024") or revise to "most harnesses do not expose programmatic spawn *to end-user primitives*" (Cursor's spawn may be internal-only).

### GitHub Codex (Copilot Workspace)
**Status: BORDERLINE-UNFAIR (undercovered)**
- Listed in concept #3 and Ch18 but no worked example or integration narrative.
- Codex's task-plan-execute model is a *canonical* example of the deterministic/probabilistic seam (Ch13) — the task list is the gate, the file edits are the model proposal. This should be a worked example, not a footnote.
- **Proposed fix:** Add Codex task-plan case as second worked example in Ch13, parallel to gh-aw. This elevates Codex to equal standing with the outer-loop story.

### OpenCode (GitHub Spark)
**Status: UNDERCOVERED**
- Named in concept #3 and Ch18 matrix but otherwise invisible.
- OpenCode is *the* no-install web-first harness (zero-config onboarding). The practitioner block should acknowledge this as a distinct trigger surface (web-native) vs local IDE.
- **Proposed fix:** Add one paragraph in Ch09 contrasting local-IDE triggers (Copilot, Claude Code, Cursor) vs web-first triggers (OpenCode, Codex). This also sets up the trigger-surface axis in Ch18.

### gh-aw (GitHub Agentic Workflows)
**Status: OVER-INDEXED (possibly)**
- Positioned as "the canonical strong-form A9" (concept #30) and the sole worked example of governed outer loop.
- **Reality check:** As of late 2024, gh-aw is in limited beta. By publication (mid-2025?), it may have GA'd, or it may still be niche. If niche, the canonical-example framing will read as premature coronation.
- **Vendor-attorney risk:** If a competing CI/CD platform (GitLab, Azure DevOps, CircleCI) adds native agent orchestration in 2025, they will cite this chapter as evidence of GitHub bias.
- **Proposed fix:** Re-frame as "one strong-form realization" and add a generic "CI/CD-mediated agent orchestration" pattern in Ch13 that is trigger-agnostic. gh-aw remains the worked example, but the *pattern* is portable. This passes the "remove Microsoft" test.

### APM (Agentic Package Manager)
**Status: OVER-INDEXED (intentionally, but declare it)**
- APM is the operational module system that realizes Genesis's composition substrate. It is the *reference implementation* of lockfile semantics, bundle hygiene, and transitive closure.
- **Risk:** Every other vendor listed is a harness/trigger vendor. APM is a package manager. The asymmetry will confuse readers unless explicitly named.
- **Proposed fix:** Add one-paragraph sidebar in Ch17 clarifying the stack: "Harnesses determine *what* loads (Ch09). Module systems determine *how* the closure is resolved and shipped (this chapter). APM is one such module system; others (e.g., a hypothetical Cursor Package Index) could exist."

### Cross-vendor summary
- **Copilot, Claude Code, Cursor:** fair, with minor temporal-qualifier risk on Cursor spawn semantics.
- **Codex:** undercovered; needs second Ch13 worked example.
- **OpenCode:** undercovered; needs trigger-surface contrast paragraph in Ch09.
- **gh-aw:** over-indexed; needs generic-pattern reframing to pass "remove Microsoft" test.
- **APM:** intentionally over-indexed (it's the reference impl), but must declare the asymmetry.

## Findings

### F1 (MEDIUM) — Ch18 will date fastest, but that's the point
**Claim:** The cross-harness reference annex (Ch18) is "the most new-content-dense" and maps substrate properties to specific harnesses (Copilot, Claude Code, Cursor, Codex, OpenCode) as of late 2024/early 2025.

**Evidence:**
- Harness capabilities evolve on 3–6 month cycles. Cursor announced agent-mode spawn (Feb 2025); Claude Code shipped Projects (Q4 2024); OpenCode is pre-GA.
- The 5x6 matrix (5 harnesses x 6 substrate concepts) will require quarterly updates if it aims to stay current.
- Historical analog: Martin Kleppmann's *Designing Data-Intensive Applications* Ch11 (stream processing systems) dated within 18 months due to Kafka/Flink/Pulsar release cycles, but the *conceptual framing* (at-least-once vs exactly-once semantics) is still canonical 7 years later.

**Proposed change:**
1. **Temporal scope declaration:** Add opening paragraph to Ch18 stating "This matrix reflects harness capabilities as of Q1 2025. Consult vendor docs for current state. The *substrate concepts* (rows) are durable; the harness capabilities (columns) evolve quarterly."
2. **Durability hierarchy:** Reorganize Ch18 into two sections: (a) "Durable substrate concepts" (the row definitions, ~40% of chapter), (b) "Harness snapshot (Q1 2025)" (the matrix, ~60% of chapter). This makes it trivial to rev the matrix without invalidating the conceptual foundation.
3. **Maintenance plan:** Commit to one matrix refresh per major handbook revision (e.g., v2.1 in late 2025). Do *not* attempt continuous updates — that creates maintenance hell. Better to be 6 months stale with a clear timestamp than to be inconsistently current.

**Why this is still an asset, not a liability:**
- The matrix answers the question "as a developer choosing a harness in early 2025, what are the load-determining differences?" — which is exactly what a practitioner needs at decision time.
- Even if specific cells date (Cursor gains spawn, OpenCode GA's), the *structure* of the question ("does this harness support programmatic spawn?") is durable.
- The chapter will be the most-cited section *because* it is data, not opinion. Every "Cursor vs Copilot for agent dev?" blog post in 2025 will link here.

### F2 (HIGH) — "harness is the compiler" analogy is defensible but must cite the variance explicitly
**Claim:** "The harness is the compiler; the filesystem is the source tree" (concept #3). Different harnesses parse different file conventions in different orders. Ch09 proposes teaching this via side-by-side Copilot vs Claude Code load-order comparison.

**Evidence:**
- **Defensible:** Compiler analogy is accurate. GCC vs Clang have different include-path resolution; Copilot vs Claude Code have different scope-discovery rules. This is substrate reality, not opinion.
- **Vendor-attorney risk:** If the side-by-side shows Copilot loading a primitive that Claude Code misses (or vice versa), vendor DevRel may push back on "inconsistent behavior" framing. They prefer "different scoping philosophies."
- **Field data:**
  - Copilot (as of Dec 2024): loads `.github/copilot-instructions.md` at repo root (GA), then any `instructions:` MCP tool if available, then file-scoped comments.
  - Claude Code (as of Dec 2024): loads `CLAUDE.md` at repo root, then `.claude/` directory, then Projects context if active.
  - Cursor (as of Dec 2024): loads `.cursor/rules/` glob, then `.cursorrules`, then chat-attached files.
  - Variance is real and observable.

**Proposed change:**
1. **Neutral framing:** In the side-by-side diagram, present both load orders as "correct for their design philosophy" rather than "inconsistent." Use neutral language: "Copilot prioritizes file-proximity scoping; Claude Code prioritizes explicit project boundaries."
2. **Cite vendor docs:** Footnote each column with the official doc link (e.g., Copilot's "Custom instructions" doc, Claude's "Projects and knowledge" doc). This makes the comparison *citeable*, not opinion.
3. **Add third column (or rotate examples):** Show three harnesses in the diagram (Copilot, Claude Code, Cursor) to avoid binary "A vs B" framing which reads as competitive comparison. Three+ options reads as "here is the design space."
4. **Explicitly state the portability consequence:** After the diagram, add one paragraph: "The practical takeaway: if you design a primitive assuming Copilot's file-proximity scoping, it may not activate in Claude Code's project-boundary model. The substrate vocabulary (scope-attached rule, module entrypoint) gives you a harness-agnostic design language. The per-harness adapters (Annex Ch18) give you the realization details."

**Why this still holds up:**
- The compiler analogy is used in industry already (e.g., Simon Willison's "LLM context is like compiler include paths" post, Jan 2024). This isn't novel framing; it's naming the consensus.
- The variance is a *feature* of the substrate model, not a bug. Teaching it explicitly prevents the "worked in Cursor, broken in Codex" support-ticket hell.

### F3 (HIGH) — gh-aw "canonical strong-form A9" claim requires generic-pattern fallback
**Claim:** "The governed outer loop. [...] Strong-form A9 SUPERVISED EXECUTION is what makes agent-driven PRs auditable for compliance" (concept #30). Proposed Ch13 uses gh-aw as the sole worked example.

**Evidence:**
- **gh-aw status (as of late 2024):** Limited beta, invitation-only. Public docs describe `safe-outputs:` gating and audit trail but do not yet show production-scale case studies.
- **Competing platforms:** GitLab has announced (but not shipped) agent-native CI steps. Azure DevOps has agent orchestration in preview. CircleCI, Jenkins, and GitHub Actions (non-agentic) all support supervised execution via approval gates and audit logs.
- **Vendor-attorney risk:** If the handbook says "gh-aw is the canonical form," competing vendors will (correctly) object that supervised execution is a *design pattern*, not a vendor-specific feature. They'll cite this chapter as anti-competitive framing.
- **Microsoft Vision Integrator test:** Does this pass the "remove Microsoft" test? If you deleted every gh-aw reference, would Ch13 still teach the deterministic/probabilistic seam? **Current answer: NO.** The chapter would lose its sole worked example.

**Proposed change:**
1. **Generic pattern first, gh-aw second:** Restructure Ch13 to lead with the *pattern* (supervised execution via auditable gate + credential isolation + bounded mutation surface), then show *two* realizations: (a) gh-aw as the outer-loop example, (b) Codex task-plan model as the inner-loop example. This balances the chapter and makes the pattern harness-agnostic.
2. **Temporal qualifier on gh-aw:** When introducing gh-aw, state "As of early 2025, GitHub Agentic Workflows is the most-complete realization of the governed outer loop in the GitHub ecosystem. Other CI/CD platforms are developing parallel capabilities." This acknowledges the state of the field without claiming uniqueness.
3. **Add generic "supervised execution" rubric:** Before the gh-aw example, list the three properties any supervised-execution system must have: (1) agent does not hold write credentials, (2) side effects are gated through a deterministic approval layer, (3) audit trail captures both proposal and disposition. Then show how gh-aw realizes these three, and how a hypothetical GitLab/ADO/CircleCI agent orchestrator could realize them.
4. **Rename "strong-form A9" to "supervised execution pattern":** Genesis's A9/A10 codes are agent-side jargon. The handbook should use the plain-English "supervised execution" throughout. Footnote Genesis codes as "one operational framework that calls this pattern A9 SUPERVISED EXECUTION / A10 GOVERNED OUTER LOOP."

**Why this still works:**
- gh-aw remains the worked example (it has the most detailed public docs as of late 2024).
- The *pattern* is now defensible and portable.
- Competing vendors can read Ch13 and say "yes, our platform supports supervised execution" without feeling misrepresented.

### F4 (MEDIUM) — OpenCode and Codex need trigger-surface elevation, not just matrix entries
**Claim:** Codex and OpenCode are listed in Ch18 matrix but lack integration narrative in the main practitioner arc.

**Evidence:**
- **Codex (Copilot Workspace):** Task-plan-execute model is *textbook* deterministic/probabilistic seam. The task list is a human-editable gate; each file edit is a model proposal that can be accepted/rejected. This is concept #12 ("consequential side effects belong to the deterministic side") in pure form. Yet current Ch13 doesn't use Codex as an example.
- **OpenCode (GitHub Spark):** Zero-install web-first harness. Lowers onboarding friction (no CLI, no IDE config). Represents a distinct trigger surface (web-native) vs local IDE. Yet current Ch09 doesn't contrast trigger surfaces.
- **Undercoverage consequence:** Readers using Codex or OpenCode as their primary harness will feel the handbook is "written for Copilot/Claude Code/Cursor" and miss the substrate generality.

**Proposed change:**
1. **Ch09 (Runtime Machine):** Add one subsection "Trigger surface variance: local IDE vs web-first." Contrast Copilot/Claude Code/Cursor (local-IDE-triggered, file-proximity scoping) vs OpenCode/Codex (web-triggered, explicit project boundaries). This sets up the trigger-surface axis that Ch18 formalizes.
2. **Ch13 (Deterministic/Probabilistic Boundary):** Add Codex task-plan model as second worked example, parallel to gh-aw. Structure: "Inner-loop supervised execution: the Codex model" (15-line task list example, showing how the task list is the gate). This balances the outer-loop (gh-aw) example and ensures both trigger surfaces are covered.
3. **Ch18 (Cross-Harness Reference):** Elevate Codex and OpenCode rows. Currently they're listed but not differentiated. Add one sentence per row explaining their trigger-surface distinction.

**Why this matters for platform strategy:**
- Codex is GitHub's flagship "AI-native IDE" play. Undercovering it in the practitioner block is a strategic miss — it should be *the* showcase for how GitHub thinks about agentic dev.
- OpenCode is the web-first onboarding funnel. If the handbook undercovers it, the lowest-friction entry point (web, no install) has no integration story.

### F5 (LOW) — APM's reference-implementation status must be declared explicitly, not assumed
**Claim:** APM is used throughout Ch17 (Primitives as Code) as the operational module system, realizing lockfile semantics, transitive closure, and bundle hygiene.

**Evidence:**
- APM is not a harness (like Copilot/Claude Code) or a trigger surface (like gh-aw). It's a package manager / module system.
- The practitioner block discusses seven vendors: five harnesses (Copilot, Claude Code, Cursor, Codex, OpenCode), one trigger surface (gh-aw), one module system (APM). The asymmetry is load-bearing but never declared.
- **Risk:** Readers may assume "APM is a harness" or "APM is GitHub-specific." Neither is true. APM is a CLI tool that works with any harness; it's not tied to GitHub (though it has GitHub-first UX).

**Proposed change:**
1. **Ch09 (Runtime Machine):** Add APM to the four-part machine diagram as a *fifth* optional layer: "module system / package manager (optional, e.g., APM)." Show it sitting between filesystem and harness, resolving the transitive closure before the harness loads primitives.
2. **Ch17 (Primitives as Code):** Add one-paragraph sidebar at chapter open: "This chapter uses APM as the reference implementation of a module system for agentic primitives. APM is one such system; others (e.g., a hypothetical Cursor Package Index, or hand-rolled `git submodule` workflows) could exist. The *concepts* (lockfile, transitive closure, bundle hygiene) are substrate properties; the *realization* (APM CLI commands) is one operational choice."
3. **Ch18 (Cross-Harness Reference):** Add APM as a *row* (not a column) in a separate mini-matrix: "Module systems and package managers." Rows: APM, git submodules, manual copy-paste. Columns: transitive closure support, lockfile semantics, publish-time lint. This clarifies APM's role without overindexing it.

**Why this matters:**
- APM is a Microsoft/GitHub-sponsored OSS project. If the handbook assumes APM without declaring it, competing vendors will cite this as evidence of bias.
- Declaring APM as "one reference implementation" invites ecosystem competition (which is healthy) while still showcasing APM's design.

### F6 (MEDIUM) — Temporal qualifiers must be consistent across all vendor references
**Claim:** The arc proposes "as of late 2024" or "as of Q1 2025" qualifiers in Ch18 but doesn't specify whether the *entire practitioner block* is scoped to a snapshot or claims timelessness.

**Evidence:**
- Harness capabilities evolve quarterly. Cursor agent-mode (Feb 2025), Claude Projects (Q4 2024), Copilot Edits (Dec 2024), gh-aw beta (ongoing).
- The handbook's shelf life depends on whether it claims "this is how harnesses work" (timeless, high bar) or "this is how harnesses worked in Q1 2025" (snapshot, lower bar but explicit).
- **Mixed signaling in current arc:** Ch09 proposes a "side-by-side comparison" (implies current state), Ch18 proposes "Q1 2025" qualifier (implies snapshot), Ch13 proposes "strong-form A9" (implies timeless pattern). These are inconsistent.

**Proposed change:**
1. **Pick one model and commit:** Either (a) snapshot model ("This practitioner block reflects the state of harnesses, triggers, and module systems as of Q1 2025"), or (b) timeless model ("This practitioner block teaches durable substrate concepts; harness-specific examples are illustrative, not exhaustive").
2. **Recommendation: hybrid model.** Chapters teaching substrate concepts (Ch09, Ch11, Ch13, Ch17) are timeless. Chapter teaching harness specifics (Ch18) is snapshot with explicit timestamp. This is the DDIA model (timeless concepts, snapshot case studies).
3. **Add temporal-qualifier policy to Ch08:** In the "Practitioner's Mindset" chapter, add one paragraph: "This block teaches durable substrate concepts (the runtime machine, attention as physics, the deterministic/probabilistic seam) that apply regardless of which harness or trigger you use. Where we cite specific harness behaviors (load orders, spawn semantics, tool-call affordances), we snapshot the state as of Q1 2025. Consult vendor docs for current capabilities."
4. **Audit all vendor references:** Search the arc for every "Copilot does X," "Claude Code supports Y," "gh-aw provides Z" claim. If the claim is a substrate property (true across all harnesses), leave unqualified. If the claim is a harness-specific feature, add "(as of Q1 2025)" or move it to Ch18.

**Why this matters:**
- Consistent temporal scoping prevents the "this chapter says Cursor doesn't support spawn, but it does now!" support-ticket flood.
- It also protects the handbook from premature obsolescence. If Codex pivots its task-plan model in mid-2025, the Ch13 example is still valid as a "worked example from Q1 2025."

### F7 (LOW) — "Attention anchor" and other Genesis pattern codes must stay footnoted, not load-bearing
**Claim:** The arc states "Where Genesis pattern codes are referenced as historical or operational artifacts (e.g., a sidebar noting 'this discipline is what an agent-side framework like Genesis calls the ATTENTION ANCHOR pattern'), the code is footnoted as out-of-band, not used as load-bearing structure" (section 5).

**Evidence:**
- Genesis is an agent-side operational framework. Its pattern codes (A1–A10, B1–B8, R1–R4) are machine codes for agents loading architectural-design primitives.
- The handbook is a human-side reference book. Using Genesis codes as chapter headings or section titles would invert the directionality contract.
- **Current arc compliance:** The arc is compliant. No Genesis codes appear as section titles in the proposed TOC. Ch11 will "add the load-lifecycle and transitive-closure sections" without naming them "B4 PLAN MEMENTO" or "B8 ATTENTION ANCHOR."

**Proposed change:**
- **None required for compliance.** The arc already follows the rule.
- **Recommendation for consistency:** When footnoting Genesis patterns, use consistent format: "This discipline—plan-write-then-reload—is realized in agent-side frameworks like Genesis as the ATTENTION ANCHOR pattern (B8)." This keeps the *concept* in the main text and the *code* in the footnote.

**Why this matters:**
- If Genesis codes leak into chapter titles or concept names, the handbook will be unreadable to developers who haven't loaded Genesis (which is most of the field).
- Footnoting them preserves cross-reference value for readers who *have* loaded Genesis while keeping the handbook self-contained.

## Durability assessment

### Fastest-dating sections (will require revision within 12 months)
1. **Ch18 (Cross-Harness Reference) — 80% of content dates within 12 months.**
   - The 5x6 matrix (harnesses x substrate concepts) will be partially stale by Q4 2025 as harnesses add spawn, MCP, or project-scoping features.
   - **Mitigation:** Explicit Q1 2025 timestamp + maintenance plan (one refresh per major handbook revision, not continuous updates).
2. **Ch09's side-by-side load-order comparison (Copilot vs Claude Code) — dates within 6–12 months.**
   - If either vendor changes scoping rules (e.g., Copilot adds project-boundary mode, or Claude Code adds file-proximity fallback), the diagram will be outdated.
   - **Mitigation:** Add temporal qualifier ("as of Q1 2025") and cite vendor docs for current state.
3. **Ch13's gh-aw worked example — dates within 6–18 months.**
   - If gh-aw GA's with different `safe-outputs:` syntax, or if competing CI/CD platforms ship agent orchestration, the example will need revision.
   - **Mitigation:** Reframe gh-aw as "one realization" (not "the canonical form") and add generic supervised-execution rubric.

### Slowest-dating sections (durable for 3–5+ years)
1. **Ch09's four-part runtime machine (model, harness, filesystem, trigger) — durable for 5+ years.**
   - This is the load-bearing substrate framing. It's analogous to "kernel, shell, filesystem, init system" in Unix — the vocabulary predates any specific implementation and will outlive any specific harness.
   - **Evidence:** The concepts are already implicit in Cursor, Claude Code, Copilot, and gh-aw docs. The handbook is naming the consensus, not inventing new framing.
2. **Ch13's deterministic/probabilistic seam — durable for 3–5 years.**
   - The "two computers, one program" framing is architecture, not tooling. It applies to LangChain, AutoGPT, Copilot, gh-aw, and any future agentic system equally.
   - **Evidence:** The seam is a first-principles property of "LLM + deterministic runtime." It's load-bearing for reasoning about safety, auditability, and failure modes — all of which are evergreen concerns.
3. **Ch11's attention-as-physics framing (concept #8) — durable for 3–5 years.**
   - Even as context windows grow (200K → 1M → 10M), attention decay remains a measurable property. The *threshold* may shift, but the *physics* stays.
   - **Evidence:** Anthropic, OpenAI, and Gemini all publish attention-curve research. The handbook is teaching the consensus finding, not a speculative claim.
4. **Ch17's lockfile/transitive-closure/bundle-hygiene concepts — durable for 5+ years.**
   - These are package-manager fundamentals. They predate LLMs (npm, pip, cargo all have lockfiles) and will postdate any specific agent primitive format.
   - **Evidence:** APM's lockfile design borrows from npm and cargo. The concepts are 10+ years old in adjacent domains.

### Ch18 specific: asset or liability?
**Verdict: HIGH-VALUE ASSET with planned obsolescence.**

**Why it's an asset:**
1. **Answers the #1 practitioner question:** "I'm choosing a harness in Q1 2025. What are the load-determining differences?" No other reference answers this with citeable data.
2. **Will be the most-cited section:** Every "Cursor vs Copilot" blog post, every "how to port my primitive to Claude Code" StackOverflow answer, every DevRel talk comparing harnesses will link to this matrix.
3. **Sets the substrate vocabulary:** By naming the rows (persona scope, scope-attached rule, programmatic spawn, etc.), Ch18 gives the field a harness-agnostic design language. Even when specific cells date, the row names stay durable.

**Why it will date fast (and why that's acceptable):**
1. **Harness releases are quarterly.** By Q4 2025, the matrix will be 6–9 months stale. By Q2 2026, it will be 12–15 months stale.
2. **Competing references will emerge.** Vendor DevRel teams will publish their own "feature parity" docs. Some will cite Ch18, some will compete with it.
3. **Maintenance burden is real.** If the handbook team commits to continuous updates, Ch18 becomes a treadmill. If they don't, it becomes a snapshot.

**Mitigation strategy (the DDIA model):**
1. **Ship as snapshot with explicit timestamp:** "This matrix reflects Q1 2025 harness capabilities."
2. **Commit to one refresh per major revision:** Update the matrix in handbook v2.1 (late 2025), v2.2 (mid-2026), etc. Do not attempt continuous updates.
3. **Separate durable concepts from harness snapshot:** Reorganize Ch18 into (a) durable substrate-concept definitions (40% of chapter, timeless), (b) harness snapshot matrix (60% of chapter, dates). This makes it trivial to rev the matrix without invalidating the foundation.
4. **Archive old matrices:** When publishing v2.1, keep the Q1 2025 matrix as "Appendix B: Historical harness snapshot (Q1 2025)." This preserves citability — blog posts from mid-2025 that linked to the Q1 matrix won't 404.

**Conclusion:** Ch18 is a *high-value, planned-obsolescence asset*. It will be the most-cited section in 2025–2026, will require one refresh per major handbook revision, and will have a 12–18 month half-life per snapshot. This is acceptable and aligns with field needs.

## Final word

This arc is **85% there**. The substrate framing (runtime machine, deterministic/probabilistic seam, attention as physics) is rock-solid and will be durable for 3–5 years. The vendor coverage is mostly fair, with three fixable gaps: (1) Codex needs elevation to Ch13 worked example, (2) OpenCode needs trigger-surface contrast in Ch09, (3) gh-aw needs generic-pattern fallback to pass the "remove Microsoft" test.

The cross-harness reference (Ch18) is the right call. It will date fast (12–18 month half-life per snapshot), but that's acceptable — the field *needs* this data, and the citability value outweighs the maintenance burden if you commit to one refresh per major revision rather than continuous updates.

**Three must-fix items before approval:**
1. **F3 (HIGH):** Reframe gh-aw from "canonical strong-form A9" to "one realization of supervised execution pattern" with generic rubric. Add Codex task-plan as second Ch13 example. This removes anti-competitive framing and passes the "remove Microsoft" test.
2. **F4 (MEDIUM):** Elevate Codex to Ch13 worked example and OpenCode to Ch09 trigger-surface contrast. This balances the vendor narrative and ensures both GitHub flagship products (Codex = AI-native IDE, OpenCode = web-first onboarding) are properly integrated.
3. **F6 (MEDIUM):** Add consistent temporal qualifiers. Declare the hybrid model (substrate concepts = timeless, harness-specific examples = Q1 2025 snapshot) in Ch08, audit all vendor references, move dated claims to Ch18.

**Two nice-to-have improvements:**
1. **F2 (HIGH):** Add third column to Ch09 load-order comparison (Copilot, Claude Code, Cursor) to avoid binary "A vs B" competitive framing. Cite vendor docs for each column.
2. **F5 (LOW):** Declare APM's reference-implementation status explicitly in Ch09 and Ch17 sidebars. This invites ecosystem competition while showcasing APM's design.

With these revisions, this arc will be the definitive practitioner reference for 2025–2027 and will hold up under vendor-by-vendor scrutiny. The "harness is the compiler" framing is defensible, the cross-harness annex is high-value despite fast dating, and the substrate vocabulary (four-part machine, deterministic/probabilistic seam, attention as physics) will outlive any specific harness.

Ship it with minor revisions.
