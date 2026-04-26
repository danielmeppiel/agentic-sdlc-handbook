# Dev Lead Proxy Review — Round 1

## Verdict
**MINOR-REVISIONS**

## Would I buy this for my team? Why?

Yes, budget approved. v2 closes the gap between "fun demo" and "production-grade workflow" that I've been stuck on for six months. Ch13 (deterministic/probabilistic boundary) is the first thing I've read that explains *why* I need a gh-aw workflow instead of just letting Claude Code push to main. Ch09 (runtime machine) finally gives me vocabulary to debug "this works in Cursor but not in Codex." Ch17 (primitives as code) is how I'd onboard someone who ships backend APIs — they already think in lint/test/deploy cycles, so framing markdown instructions the same way clicks immediately. The anti-pattern catalogue in Ch16 maps directly to postmortems my team has already written. This is the missing ops manual.

## What gets used vs what gets skipped

| Chapter | Likely use frequency | Why |
|---------|---------------------|-----|
| Ch09 (Runtime Machine) | Weekly | Reference when debugging cross-harness issues; required onboarding reading |
| Ch10 (Instrumented Codebase) | Weekly | Template for structuring new projects; binding-mode table gets printed and taped to monitors |
| Ch11 (PROSE Specification) | Once per project setup | Read once, apply forever — like PEP 8 or Google's style guide |
| Ch12 (Context Engineering) | Monthly | Onboarding new hires; debugging attention-decay failures |
| Ch13 (Deterministic/Probabilistic Boundary) | **Daily** | The chapter I wish existed 8 months ago. Required reading before anyone ships agent-generated code to prod |
| Ch14 (Multi-Agent Orchestration) | Monthly | Only when scaling past single-agent workflows; most teams stay single-agent for 6+ months |
| Ch15 (Execution Meta-Process) | Weekly | PR #394 case study is gold for understanding what "done" looks like |
| Ch16 (Anti-Patterns + Stack Trace) | **Daily** | My new postmortem template. "Bundle leakage" entry will save us from a class of failure we didn't have a name for |
| Ch17 (Primitives as Code) | Weekly | Onboarding backend engineers; establishing CI gates for agentic repos |
| Ch18 (Cross-Harness Reference) | Monthly | Lookup table when evaluating new tools or migrating harnesses |
| Ch19 (What Comes Next) | Skipped | Unless I'm planning a conference talk |

Ch13 and Ch16 get used most because they directly address the "can we ship this?" question. Ch14 (multi-agent) gets skipped by most teams until they hit scale — single-agent workflows handle 80% of use cases.

## Findings

### F1 (MAJOR) — Ch13 needs a runnable example in the first 500 words

**Claim:** Ch13 is the most critical chapter for production adoption, but if the opening is abstract theory ("two computers, one program"), engineers will skim past it before reaching the gh-aw `safe-outputs:` example that makes it click.

**Evidence:** From proposed arc section 4, Ch13 teaching plan lists concept #11 (two computers) first, then concept #12 (consequential side effects belong to deterministic side). The seam diagram comes before the runnable example. This is backwards for a dev-lead audience.

**Proposed change:** Open Ch13 with a 30-line gh-aw workflow file showing `safe-outputs:` in action, annotated inline. Reader sees the gate *before* they read the theory. Then section 2 explains "this is the deterministic/probabilistic seam" and the diagram makes sense. Pattern: show-then-explain, not explain-then-show.

### F2 (MAJOR) — "Agent stack trace" protocol must be a numbered checklist, not prose

**Claim:** Ch16's "agent stack trace" (concept #14) is described in proposed arc as "the failure-model-and-debugging unifying protocol" but the current handbook has it as "the list you read." For postmortems, I need a checklist I can hand to a junior who just hit their first silent semantic failure.

**Evidence:** Concept #14 lists four items: (a) loaded primitive set, (b) plan-memento file, (c) verbose tool-call log, (d) diff between expected/actual. This is gold, but only if it's formatted as a protocol, not buried in a paragraph.

**Proposed change:** Ch16 section 1 must be titled "The Agent Stack Trace Protocol" with a numbered checklist:
```
1. Check: What primitives loaded at decision time?
   Command: [harness-specific command here]
2. Check: Does a plan-memento file exist? Is it stale?
   Location: [scope-specific path]
3. Check: What did the agent *try* to do?
   Command: [verbose tool-call log]
4. Check: What *actually* happened?
   Command: [diff command]
```

Make it copy-pasteable. The theory comes after.

### F3 (MINOR) — Ch18 should be an appendix, not a chapter

**Claim:** Cross-harness reference is lookup material, not teaching material. Putting it in Part III inflates the practitioner block and forces a linear read of reference data that's better skimmed on-demand.

**Evidence:** My own behavior pattern — I read teaching chapters linearly (Ch08-Ch15), then use reference material as a lookup table. Ch18's proposed content (5x6 matrix, trigger-surface vs inference-harness axes) is exactly what an appendix is for.

**Proposed change:** Move Ch18 to Appendix B. Part III closes at Ch17 (Primitives as Code), which ends on the "architect stays portable" discipline — a better narrative endpoint. Ch17 says "here's how to ship primitives"; Appendix B says "here's where they bind in each harness."

### F4 (MAJOR) — Ch10 binding-mode column needs worked examples, not just table entries

**Claim:** The proposed restructure adds a "binding-mode column" to the primitives table (agent-invoked vs substrate-invoked). This distinction is critical — it's why skills sometimes don't activate — but without a worked "before/after" example showing a skill that *should* have bound but didn't, the table entry is just more vocabulary.

**Evidence:** Concept #5 explains the distinction well in theory ("skill is agent-invoked, workflow is substrate-invoked") but the proposed arc doesn't say *how* Ch10 will teach it beyond "add binding-mode column."

**Proposed change:** Ch10 section 2 needs a two-column worked example:
- **Left column:** "I wrote a skill with description 'Handle authentication errors'. It didn't load when the agent hit a 401."
- **Right column:** "Skills are agent-invoked (description-match at runtime). For trigger-on-error, use a workflow file (substrate-invoked, event-match). Here's the corrected YAML."

One failure-mode example per binding mode. This is how backend engineers already think about event-driven systems.

### F5 (MINOR) — Onboarding pathway needs an explicit "first week" section in Ch08

**Claim:** The arc assumes readers will discover the onboarding pathway by reading linearly, but dev leads don't onboard new hires that way — they assign specific chapters in a specific order with checkpoints. Ch08 (Practitioner's Mindset) should end with a one-page "Your First Week" section.

**Evidence:** Proposed arc says Ch08 gets "tighten the three-roles section; add a one-page sidebar on the four-part runtime machine." The sidebar is conceptual scaffolding, not an onboarding path.

**Proposed change:** Ch08 closing section titled "Your First Week with Agentic Workflows":
```
Day 1-2: Read Ch09 (Runtime Machine), Ch10 (Instrumented Codebase), Ch11 (PROSE).
         Goal: Understand the substrate and basic primitives.
Day 3:   Read Ch13 (Deterministic/Probabilistic Boundary).
         Goal: Internalize where the safety gate sits.
Day 4:   Read Ch16 (Anti-Patterns + Stack Trace).
         Goal: Know how to debug before you break production.
Day 5:   Read Ch17 (Primitives as Code), run `apm compile` on our team's repo.
         Goal: Understand our CI gates.
Week 2:  Ship your first agent-assisted PR with a senior reviewing both the code *and* the primitives you used.
```

This is what I'd hand to a new senior on Monday morning.

### F6 (MINOR) — Ch12 transitive-closure section needs the `npm ls` analog made explicit

**Claim:** Concept #7 (the transitive-closure question) is framed as "the equivalent of `npm ls` or `pip freeze` for agent context" but the proposed arc says Ch12 will "add the load-lifecycle and transitive-closure sections" without saying *how* a developer would actually run the equivalent command.

**Evidence:** Proposed arc section 2 says Ch12 gets "restructure" with load-lifecycle and transitive-closure added, but doesn't specify the runnable example.

**Proposed change:** Ch12 must include a side-by-side comparison table:

| Classical tool | Agent equivalent | What it shows |
|---------------|------------------|---------------|
| `npm ls` | `apm compile --dry-run` | Closure of primitives that load |
| `pip freeze` | `apm.lock` inspection | Pinned versions of external modules |
| `git log` | Plan-memento file + verbose tool log | History of agent decisions |

Developers already know `npm ls`. Tell them the agent analog in the first paragraph, *then* explain why closure matters.

### F7 (MAJOR) — Ch17 must address "who reviews primitive changes" in CI

**Claim:** Ch17 teaches "lint-test-CI for primitives" but doesn't answer the org-process question: in a code review, does the reviewer need to review the `.instructions.md` change the same way they review a `.py` file change? Or is it a different review discipline?

**Evidence:** Concept #19 says primitives can be "linted, tested, and gated in CI" but the proposed Ch17 content list doesn't include "review protocol."

**Proposed change:** Ch17 needs a subsection titled "Reviewing Primitive Changes" that addresses:
- **Diff review:** Changes to primitives *are* code changes. Same approval gates as code.
- **Activation testing:** Did you verify this skill actually loads when its description matches? (The primitive-lint equivalent of a smoke test.)
- **Attention-budget check:** Does this change increase the context load? If yes, what did you cut to compensate?

This is the conversation I'd have in a PR review. Make it explicit.

## Onboarding pathway

If a new senior joins my team Monday, here's their reading order for week 1:

**Monday morning:**
1. Ch08 (Practitioner's Mindset) — 20 minutes. Skim to the "Your First Week" section (proposed F5), read that first, then loop back to the three-roles framing.
2. Ch09 (Runtime Machine) — 45 minutes. This is the conceptual foundation. Don't skip the two-column Copilot-vs-Claude-Code comparison.

**Monday afternoon:**
3. Ch10 (Instrumented Codebase) — 60 minutes. Read the binding-mode worked examples (proposed F4) twice. Print the primitives table and tape it next to your monitor.

**Tuesday:**
4. Ch11 (PROSE Specification) — 30 minutes. Read once, apply forever. Like a style guide.
5. Ch13 (Deterministic/Probabilistic Boundary) — 90 minutes. **Most important chapter.** Start with the `safe-outputs:` example (proposed F1), then read the theory. Re-read section 2 (consequential side effects) before bed.

**Wednesday:**
6. Ch16 (Anti-Patterns + Stack Trace) — 60 minutes. Read the agent-stack-trace checklist (proposed F2) first. Then read the anti-pattern catalogue. Flag the entries that match failures you've already seen in other teams' postmortems.

**Thursday:**
7. Ch17 (Primitives as Code) — 45 minutes. Read section on lint-test-CI. Then go to our team repo, run `apm compile --dry-run`, and inspect the output.
8. Ch12 (Context Engineering) — 30 minutes. Skim the transitive-closure section. You already understand dependency resolution from npm/pip; this is the agent analog.

**Friday:**
9. Ch15 (Execution Meta-Process) — 30 minutes. Read the PR #394 case study. This is what "done" looks like.
10. Appendix B (Cross-Harness Reference, formerly Ch18 per F3) — 15 minutes. Skim the matrix. Bookmark for later.

**Week 1 checkpoint:** Senior can ship an agent-assisted PR with primitives that load correctly, side effects behind deterministic gates, and a plan-memento file for session continuity. They know how to debug using the agent stack trace protocol.

**Week 2:** Pair with a senior on their team. First PR they open gets reviewed both for code *and* for the primitives they used.

Ch14 (Multi-Agent Orchestration) is deferred to month 2 — most teams stay single-agent for the first 6 months.

## Final word

This is the handbook I've been waiting for. v2 closes the production-readiness gap that kept me from rolling out agentic workflows beyond my own team. Ch13 (deterministic/probabilistic boundary) and Ch16 (agent stack trace) are the two chapters I'll re-read every time someone on my team asks "can we ship this?" The binding-mode distinction in Ch10, the transitive-closure protocol in Ch12, and the lint-test-ship discipline in Ch17 are all concepts my backend engineers already understand in a different context — reframing them for agentic systems is the right teaching strategy.

The revisions I'm calling for (F1-F7) are about execution, not direction. The arc is sound. Make the examples runnable, make the protocols copy-pasteable, and move the reference material to an appendix. Approve pending those changes.

If I had to cut scope to ship faster: keep Ch09, Ch13, Ch16, Ch17. Defer Ch14 (multi-agent) and Ch18 (cross-harness reference) to v2.1. Most teams can operate for 6+ months on single-agent workflows with one harness. The deterministic gate, the agent stack trace, and the primitive DevEx are the unlock.
