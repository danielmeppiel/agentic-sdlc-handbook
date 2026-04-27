# Fact / Reference Checker Review — Round 1

## Verdict
**MINOR-REVISIONS**

The proposed arc makes strong, specific claims that advance the handbook's clarity. Most concepts trace to Genesis assets or existing handbook material. However, several load-bearing assertions lack verifiable citations — particularly vendor-specific capabilities, academic cognitive-load claims, and the "2x2 of quality gates." The arc needs 6-8 specific citations added and 3-4 vendor claims verified against current documentation.

## Citation audit (per concept in the proposed arc)

| Concept | Source claimed | Verifiable? | Risk of staleness |
|---------|---------------|-------------|-------------------|
| Four-part runtime machine | Genesis `runtime-affordances/common.md` | ✓ Internal | Low |
| Markdown-as-code thesis | Genesis `primitives.md`, implicit throughout | ✓ Internal | Low |
| Harness as compiler | Genesis per-harness adapters (5 files) | ✓ Internal | **HIGH** — harness APIs change quarterly |
| Thread-vs-FS separation | Genesis `architectural-patterns.md` A4/A5 | ✓ Internal | Low |
| Binding modes (agent vs substrate) | Genesis `primitives.md` | ✓ Internal | Low |
| Load order observable/matters | Genesis `runtime-affordances/common.md` | ✓ Internal | Medium |
| Transitive closure question | Genesis `composition-substrate.md` | ✓ Internal | Low |
| Context finite, attention degrades | Genesis `pattern-tradeoffs.md` truth #1 | **Partial** — physics claim needs academic source | Medium |
| Plan-write-then-reload | Genesis B4/B8 patterns | ✓ Internal | Low |
| Bounded-scope rule (grounding) | Genesis `pattern-tradeoffs.md` | ✓ Internal | Low |
| Two computers, one program | Genesis S7/A9 patterns | ✓ Internal | Low |
| Consequential side effects → deterministic side | Genesis A9 + gh-aw `safe-outputs` | **Needs vendor doc** — gh-aw capability | **HIGH** |
| Hallucination as system property | Genesis truth #4 + C2/C6/A7 | ✓ Internal | Low |
| Agent stack trace protocol | Ch09 Turn 23 + Genesis A8 | ✓ Internal | Low |
| Silent semantic failure dominant | Genesis A7 + Ch09 Turn 5 EMU example | ✓ Internal | Low |
| Four kinds of quality gate (2x2) | Genesis `pattern-tradeoffs.md` section 2 | **❌ NO SOURCE** — 2x2 needs citation | High |
| Plan persistence durable | Genesis primitives + Copilot session-state SQLite | **Needs vendor verification** | **HIGH** |
| Child-thread spawn variance | Genesis per-harness adapters | **Needs current vendor docs** (Cursor, Codex) | **HIGH** |
| Lint-test-CI for primitives | Genesis composition + APM toolchain | ✓ Internal (APM) | Low |
| Lockfile semantics | Genesis `composition-substrate.md` + APM | ✓ Internal (APM) | Low |
| Cross-harness matrix | Genesis 5 per-harness adapters (~580 lines) | ✓ Internal | **HIGH** — harness updates |
| Bundle leakage / phantom dep | Genesis `composition-substrate.md` + APM rules | ✓ Internal (APM) | Low |
| Architect stays portable | Genesis `portability-rules.md` | ✓ Internal | Low |
| Trigger vs inference orthogonality | Genesis `per-trigger-surface/gh-aw.md` + per-harness | ✓ Internal | Medium |
| MCP as runtime property | Genesis `primitives.md` anti-pattern flag | ✓ Internal | Low |
| Attention anchor pattern | Genesis B8 `design-patterns.md` lines 617-684 | ✓ Internal | Low |
| Refactor patterns (SPLIT/FUSE/EXTRACT/INLINE) | Genesis `refactor-patterns.md` R1-R4 | ✓ Internal | Low |
| Pattern selection on tradeoff axes | Genesis `pattern-tradeoffs.md` (entire file) | ✓ Internal | Low |
| Threading topology 2x2 | Genesis `pattern-tradeoffs.md` section 4 | **Partial** — missing classical source | Medium |
| Governed outer loop (A9/A10) | Genesis A10 + gh-aw adapter SANDBOXING fields | **Needs vendor doc** — gh-aw audit trail | **HIGH** |
| PR #394 case study (70 files, 2,874 tests, 90 min) | Existing Ch13, author's work | ✓ Internal (case study) | Low — but **consistency risk** |

## Findings

### F1 (HIGH) — Attention-decay physics claim lacks academic grounding

- **Claim (line 88-91 of concepts doc, repeated in arc Ch09):** "Doubling input length does not halve output quality; it crosses a threshold past which the model loses the thread entirely. A human developer needs to internalize attention as a *physical* property of the runtime, not as a soft preference." + Classical analog: "CPU cache pressure and memory bandwidth — past a working-set threshold, performance does not degrade gracefully, it collapses."
- **Evidence:** Genesis `pattern-tradeoffs.md` truth #1 (internal assertion). No citation to transformer attention-mechanism papers or empirical LLM context-window studies.
- **Issue:** The claim about non-linear degradation is presented as established fact but lacks external verification. The cache-pressure analogy is evocative but needs a source showing the parallel holds.
- **Proposed change:** Add footnote citing either (a) transformer attention mechanism papers (Vaswani et al 2017 "Attention Is All You Need" + empirical follow-up on attention head saturation) or (b) LLM context-window benchmarks (Anthropic's long-context evals, OpenAI's "lost in the middle" research). If no direct source exists, qualify: "Practitioners report..." or "Empirically observed in sessions exceeding..."

### F2 (HIGH) — "Four kinds of quality gate" 2x2 presented without source

- **Claim (concept #16, arc Ch13):** "Quality gates split on two axes: who renders the verdict (the agent itself vs an outside source) and how it is rendered (programmatic vs judgement). The 2x2 is closed: (programmatic+internal) = test/lint, (judgement+internal) = goal-steward, (programmatic+external) = cold-reader-with-rubric, (judgement+external) = human checkpoint."
- **Evidence:** Genesis `pattern-tradeoffs.md` section 2 (internal framework). No citation to software testing literature, CI/CD patterns, or formal verification.
- **Issue:** The 2x2 is presented as a discovered taxonomy ("the 2x2 is closed") but appears to be original work by the author. This is acceptable IF explicitly labeled as the author's synthesis. If it draws on prior art (e.g., test pyramids, Humble/Farley's CI book, ISTQB testing types), that should be cited.
- **Proposed change:** Either (a) add citation if prior art exists, or (b) qualify: "We propose a 2x2 taxonomy..." / "In our operational experience, quality gates fall into four types..." Make clear this is the author's framework, not an industry-standard classification.

### F3 (HIGH) — Copilot session-state SQLite claim needs vendor verification

- **Claim (concept #17, line 150):** "Genesis `runtime-affordances/per-harness/copilot.md` notes Copilot's session-state SQLite plus `plan.md`."
- **Evidence:** Internal Genesis file referencing a Copilot feature.
- **Issue:** This is a specific vendor capability claim ("Copilot has session-state SQLite"). As of the fact-checker's knowledge cutoff, GitHub Copilot in VSCode does not expose a documented SQLite-backed session-state API to agent authors. This may be: (a) a feature added after cutoff, (b) an internal implementation detail not part of the public API, or (c) a misattribution (confusion with Cursor's `.cursorrules` or another harness).
- **Risk of staleness:** **Very high** — vendor APIs change without notice.
- **Proposed change:** Verify against current GitHub Copilot documentation. If the feature exists, add "(as of [date])" qualifier and link to vendor docs. If the feature is internal/undocumented, qualify: "Copilot internally persists session state (observed via...)" If it doesn't exist or is misattributed, correct the claim.

### F4 (HIGH) — Cursor and Codex spawn-capability claims need current vendor docs

- **Claim (concept #18, line 154-157):** "Claude Code's Task tool, Copilot's `task` agent dispatch, OpenCode's subagents — these are programmatic spawn primitives. Cursor and Codex (as of late 2025) lack programmatic spawn."
- **Evidence:** Genesis per-harness adapter files (internal).
- **Issue:** This is a dated, vendor-specific negative claim ("Cursor lacks X as of late 2025"). Negative claims are fragile — a vendor can add the feature in the next release. The "(as of late 2025)" qualifier helps but is not sufficient for handbook prose that may be read in 2026.
- **Risk of staleness:** **Very high** — Cursor and Anthropic update monthly.
- **Proposed change:** 
  1. Verify against current Cursor and Codex documentation (December 2025 or later).
  2. If still accurate, keep the date qualifier and add a footnote: "Verified as of [date]. Check vendor docs for updates."
  3. If capability has been added, update the claim.
  4. Consider rephrasing to make staleness explicit: "At time of writing, Cursor and Codex do not expose programmatic spawn APIs; check vendor roadmaps for changes."

### F5 (MEDIUM) — gh-aw `safe-outputs` and audit-trail claims need vendor verification

- **Claim (multiple locations — concept #12, #30, arc Ch13):** gh-aw provides "CAPABILITY_GATING via safe-outputs" and "provides the audit trail" for supervised execution and governed outer loop.
- **Evidence:** Genesis `runtime-affordances/per-trigger-surface/gh-aw.md` (internal) + worked examples.
- **Issue:** This is a specific claim about GitHub Actions Workflows' capability. The handbook should link to the official GitHub Actions documentation sections on:
  - Job outputs and step gating
  - Audit logs for workflow runs
  - Environment protection rules (if that's what "safe-outputs" maps to)
- **Risk of staleness:** Medium — GitHub Actions is stable but adds features regularly.
- **Proposed change:** Add footnotes to Ch13 linking to:
  1. GitHub Actions docs on `outputs:` and conditional steps
  2. GitHub audit log documentation
  3. If "safe-outputs" is a Genesis/APM-specific convention rather than a GitHub-native keyword, clarify: "`safe-outputs:` (our convention for gating mutations in workflow YAML)..."

### F6 (MEDIUM) — Threading topology 2x2 needs classical source or qualification

- **Claim (concept #29):** "Multi-agent design is a 2x2: parallel threads on shared state (race), parallel threads on isolated state (map-reduce), sequential threads on shared state (pipeline), sequential threads on isolated state (relay)."
- **Evidence:** Genesis `pattern-tradeoffs.md` section 4 (internal).
- **Issue:** The 2x2 reads like established concurrency theory (parallel/sequential x shared/isolated is the standard way to taxonomize threading models) but lacks a citation. This is teachable from first principles, but if it's drawn from classical concurrency literature (e.g., Andrews & Schneider, Herlihy & Shavit's "Art of Multiprocessor Programming"), it should cite them.
- **Proposed change:** Either (a) add citation to concurrency textbook, or (b) present as "we adapt the classical concurrency 2x2..." with a pointer to where the classical version appears.

### F7 (LOW) — PR #394 consistency audit required

- **Claim (multiple chapters):** The case study references "70 files," "2,874 tests," "90 minutes," and specific intervention counts.
- **Evidence:** Author's case study, cited in existing Ch13.
- **Issue:** The concepts doc and arc both reference PR #394 but do not verify internal consistency. The fact-checker's mandate includes checking that the same statistic is quoted the same way in all chapters.
- **Proposed change:** Before final publication, run a consistency audit:
  1. Grep the entire handbook for "PR #394" and extract all numeric claims.
  2. Verify they match. If "70 files" appears in one chapter and "72 files" in another, reconcile.
  3. This is a **pre-publication blocker**, not an arc-approval blocker, but flag it now.

## Sources to add

1. **Attention mechanism non-linear degradation:**
   - Vaswani et al (2017), "Attention Is All You Need" (foundational transformer paper)
   - Liu et al (2023), "Lost in the Middle: How Language Models Use Long Contexts" (arXiv:2307.03172) — empirical study showing degradation
   - Alternative: Anthropic's long-context evaluation blog posts (if more accessible to practitioners)

2. **Quality gate taxonomy (if prior art exists):**
   - Humble & Farley (2010), *Continuous Delivery* (CI/CD gate types)
   - Fowler, "TestPyramid" pattern (if the 2x2 maps onto it)
   - If no direct mapping, explicitly label as author's synthesis

3. **Threading topology 2x2:**
   - Andrews & Schneider (1983), "Concepts and Notations for Concurrent Programming" (classical concurrency taxonomy)
   - Herlihy & Shavit (2008), *The Art of Multiprocessor Programming* (shared-state vs message-passing)

4. **Vendor documentation (all HIGH-risk-of-staleness claims):**
   - GitHub Copilot API documentation (session state, task dispatch)
   - Cursor documentation (spawn capabilities, rules loading)
   - Anthropic Claude Code documentation (Task tool)
   - GitHub Actions documentation (outputs, audit logs, environment protection)

5. **Cognitive load theory (if the handbook references it elsewhere):**
   - Sweller (1988), "Cognitive Load During Problem Solving" — if the "attention as physical property" framing draws on this
   - The arc does not explicitly invoke Sweller, but if Ch11's "Progressive Disclosure" does, cross-reference it in Ch09's attention section

6. **Dependency confusion / supply-chain security:**
   - The lockfile-semantics section (concept #20) invokes "the dependency-confusion problem npm faced" without citation
   - Add: Birsan (2021), "Dependency Confusion" blog post (the original disclosure), or NIST guidance on software supply-chain attacks

## Final word

The proposed arc is **factually sound at the conceptual level** — the substrate model it teaches is internally consistent, well-argued, and clearly sourced to Genesis where Genesis is the authoritative internal reference. The issues are:

1. **Vendor-specific claims risk staleness.** The arc correctly dates them ("as of late 2025") but the handbook will be read in 2026+. Solution: add verification dates and "check vendor docs" disclaimers.

2. **Academic/theoretical claims need external grounding.** The attention-decay physics, the 2x2 taxonomies, and the threading-topology model are presented as established truths but lack citations. Solution: either cite prior art or explicitly label as the author's synthesis.

3. **Case-study consistency is a publication blocker.** PR #394 numbers must be audited across all chapters. Solution: defer to pre-publication pass but flag now.

The arc can proceed to the next panel round with these revisions:
- Add 6-8 citations (attention, quality gates, threading, dependency confusion)
- Verify 3-4 vendor claims (Copilot SQLite, Cursor/Codex spawn, gh-aw safe-outputs)
- Add "as of [date]" + "check vendor docs" disclaimers to all harness-capability claims
- Mark PR #394 consistency audit as a pre-publication task

**Recommendation: MINOR-REVISIONS** — the arc is strong, the gaps are fixable, and none of the missing citations invalidate the structural argument.
