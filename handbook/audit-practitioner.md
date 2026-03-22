# Practitioner Block Audit — WIP Handbook Source Material

> **Auditor**: Practitioner Authority persona
> **Source**: `WIP/agentic-sdlc-for-practitioners-handbook.md` (15 sections, ~1,300 lines)
> **Supporting evidence**: `WIP/evangelism-playbook.md`, `WIP/11-march-strategy.md`, `WIP/20-march-strategy-update.md`
> **Reference case**: PR #394 — 70 files changed, +5,886/-1,030, 30 commits, 2,874 tests, ~90 min wall-clock
> **Target**: Block 2 (Chapters 8–14) of the new Agentic SDLC Handbook

---

## 1. Battle-Tested Gold

Techniques validated by the PR #394 execution, with evidence strength ratings.

### STRONG — Directly validated with measurable outcomes

| Technique | Evidence | Why it's gold |
|---|---|---|
| **Wave execution model** (§7) | 4 waves, 15 agents, 0 regressions. Specific timings reported per wave. | The core scheduling primitive. Dependency-ordered batches with parallel dispatch within each batch — proven at 70-file scale. |
| **One-file-one-agent rule** | Explicitly called out as a wave design rule; the string-matching conflict rationale is grounded in real Copilot CLI tool mechanics. | Prevents the most common parallel-edit failure mode. Simple, enforceable, immediately adoptable. |
| **Test-after-every-wave checkpoint** (§8) | 2,874 tests green across all waves. 30 commits = one per checkpoint. Zero regressions reported. | The "why you can trust agent output" argument. Non-negotiable gate that makes the entire system trustworthy. |
| **Two-team topology** (§6) | Architecture team + Domain Expert team structure used in PR #394. Named leads (python-architect, cli-logging-expert). | Right-sized for cross-cutting changes. Concrete enough to copy. |
| **Escalation protocol** (§10) | 3 human interventions reported: scope decision, agent recovery, test fix. Maps to L2 escalation. | Proves the human is a decision-maker, not a babysitter. The ratio (3 interventions / 15 agents dispatched) is the credibility data point. |
| **Feedback loop → primitive improvement** (§11) | Four specific failure-to-fix examples with before/after primitive changes. | The compounding mechanism. Each row is a real "I fixed this in markdown, not in code" story. |
| **Three-layer instrumentation** (§3) | Agents, Skills, Instructions — the cascade is the actual Copilot CLI architecture. Supported by `.github/` directory conventions. | Not theoretical — it's how the tool works. The cascade diagram is accurate. |
| **Foundation-before-migration wave ordering** | Wave 0 = protocol types + method moves. Wave 1+ = code that uses new APIs. Directly reflected in PR #394 timeline. | Prevents the "API doesn't exist yet" class of agent failures. |

### MODERATE — Validated but with caveats

| Technique | Evidence | Caveat |
|---|---|---|
| **Audit → Plan → Wave → Validate → Ship meta-process** (§4) | PR #394 followed this flow. Timeline in §15 matches. | The "ADAPT" loop (plan adaptation on escalation) is mentioned but the PR #394 account only shows one adaptation instance (Wave 2b recovery). Unclear how well this works under heavy adaptation pressure. |
| **Red teaming / panel discussions** (§5) | Described conceptually. The strategy docs (March 11, March 20) show adversarial review of *strategic* decisions. | The handbook claims agent-team panel reviews before execution, but the PR #394 account doesn't explicitly describe agents reviewing each other's plans. May have happened implicitly via the harness. |
| **The confidence argument** (§9) | "If tests pass, the code meets the spec" — the philosophical anchor. | True when test coverage is high. The handbook acknowledges this ("fix the tests, not the process") but doesn't quantify what "high enough" coverage means. PR #394 had 2,874 tests — but coverage percentage isn't reported. |
| **Scaling characteristics** (§14) | Performance numbers from PR #394 are precise. Safety argument is well-reasoned. | N=1. One project, one PR, one developer. No multi-developer or multi-project validation. |
| **Plan-carries-the-team spec format** (§5) | Example plan structure is concrete. Scope/Teams/Waves/Principles/Constraints format. | No evidence of how this performs with a team that *didn't* write the plan. Solo developer validated only. |

### WEAK — Conceptually sound but evidence is thin

| Technique | Evidence | Gap |
|---|---|---|
| **Autonomous CI/CD workflows** (§12) | Described as scheduled drift detection, dependency audits, auto-fix loops. | Zero execution evidence. Entirely aspirational. No "we ran this and caught X" story. |
| **Ring 2 (Acceptance) and Ring 3 (Integration/E2E) tests** (§9) | Described in the pipeline model. | PR #394 metrics report unit tests only (2,874). No acceptance or E2E test execution mentioned. The ring model is sound but only Ring 1 was validated. |
| **Scenario B/C/D** (§15) | Three additional scenarios beyond the reference case. | Hypothetical. Structured correctly but never executed. They read as "how I would do it" not "how I did it." |
| **Dashboard POC** (Appendix D) | Detailed architecture, hook event model, server code. | Not executed. It's a design doc for a visualization layer, not a battle-tested tool. Interesting but unproven. |

---

## 2. Theory Without Evidence

Applying the "battle-tested or cut" principle ruthlessly:

### Cut candidates

| Claim | Section | Problem |
|---|---|---|
| **"Zero regressions"** | §14 | Extraordinary claim. More precisely: zero regressions *detected by the test suite*. The distinction matters. |
| **"You might speak to terminals using voice input"** | §1 | Mentioned twice. No evidence this was used during PR #394. Aspirational lifestyle claim that weakens credibility. |
| **"You do not write production code"** | §1 | Overstated. PR #394 involved 3 human interventions including a test fix — that's writing code. The reality is "you write very little code." |
| **Autonomous CI/CD auto-merge** | §12 | "If CI is green, auto-merge" for low-risk fixes. Zero evidence of an autonomous fix loop running. No project actually does this safely without significant guardrails not described. |
| **"What would be 2-3 days of manual work"** | §1, §15 | The ~90min vs 2-3 days comparison. No baseline measurement. This is a guess, not a metric. Scenario A even contradicts: it says ~35 minutes, not ~90 minutes. |
| **Code Review + Security as parallel agents** (§5) | Described as automatic gates. | No evidence from PR #394 that dedicated review/security agents ran as described. |
| **Dashboard interactive control plane** | Appendix D | Pre-tool-use hook returning deny decisions via HTTP — interesting concept, completely unbuilt. |

### Downgrade candidates (keep but mark as emerging)

| Claim | Recommendation |
|---|---|
| Red teaming between agents | Move from "established pattern" to "promising technique" until multi-agent adversarial review is demonstrated on a real PR |
| Ring 2/3 test pipeline | Keep the model but note only Ring 1 is validated; Rings 2-3 are architectural guidance |
| Scaling beyond 70 files | Acknowledge the scaling analysis is extrapolation, not observation |

---

## 3. "Can I Use This Monday?" Test

For each major technique: could a senior developer adopt this on their next PR without extensive setup?

| Technique | Monday-ready? | Setup cost | Verdict |
|---|---|---|---|
| **Meta-process** (Audit→Plan→Wave→Validate→Ship) | ✅ Yes | Zero — it's a mental model | Any developer can run an explore agent to audit, write a plan, then execute in waves. Works with any AI coding tool. |
| **Wave execution** | ✅ Yes | Zero — just sequence your prompts | The concept of "batch independent tasks, run them, test, commit, repeat" requires no infrastructure. The specific Copilot CLI dispatch mechanism is optional. |
| **Checkpoint discipline** | ✅ Yes | Zero | "Test and commit after each batch" is universally applicable. |
| **One-file-one-agent rule** | ✅ Yes | Zero | Simple constraint. Works with any tool that dispatches agents. |
| **Three-layer instrumentation** | ⚠️ Partial | Medium — 2-4 hours for initial agents + skills + instructions setup | The *concept* is Monday-ready. Writing good agent personas and skill rules takes iteration. First attempt will be rough. The handbook should include a "minimal viable instrumentation" starter. |
| **Test rings** | ⚠️ Partial | Depends on existing test suite | If you already have tests, Ring 1 is free. If you don't, the entire system's trust model collapses. Handbook should address the "no tests yet" starting point. |
| **Escalation protocol** | ✅ Yes | Zero — it's a decision framework | The four levels are immediately useful as a mental model for "when do I intervene?" |
| **Feedback loop** | ✅ Yes | Low — just edit the markdown | After any agent mistake, update the persona/skill/instruction. Requires the mindset shift, not infrastructure. |
| **Team topology** | ⚠️ Partial | Medium — need agent files written | Two-team structure is clear but requires agent persona files that encode real domain knowledge. Generic personas won't perform. |
| **Autonomous CI/CD** | ❌ No | High — requires workflow authoring, trust calibration | Not Monday-ready. Requires significant CI/CD infrastructure, careful scope definition, and organizational trust. |

**Overall Monday-readiness: 6/10 techniques are immediately usable.** The meta-process, wave execution, checkpoints, and escalation protocol can be adopted by anyone with an AI coding tool. The three-layer instrumentation and team topology need initial investment. Autonomous CI/CD is a future-state aspiration.

---

## 4. Failure Modes — Documented vs. Missing

### Documented (§13) — Quality assessment

The handbook documents 7 anti-patterns. Rating each:

| Anti-pattern | Quality | Notes |
|---|---|---|
| The Solo Hero | ✅ Good | Clear problem, clear fix. |
| The Context Bomb | ✅ Good | Actionable — "precise instructions, not entire codebase." |
| The Trust Fall | ✅ Good | Directly supported by the "agent claimed success but file wasn't persisted" evidence from §11. |
| The Scope Creep Agent | ✅ Good | "Do NOT modify" constraints are concrete. |
| Same-File Parallel Edits | ✅ Good | Grounded in Copilot CLI's string-matching mechanics. |
| Skipping Checkpoints | ✅ Good | The bisection argument is compelling. |
| Not Fixing the Primitives | ✅ Good | Core to the feedback loop philosophy. |

### Missing failure modes that SHOULD be documented

These are failure modes that likely occurred during PR #394 or would occur in practice, but the handbook doesn't cover:

| Failure mode | Why it's missing | Impact |
|---|---|---|
| **Context window exhaustion** | The handbook doesn't discuss what happens when a wave has so many tasks that the harness's context fills up. At 70 files and 15 agents, context pressure is real. | Agents get degraded instructions. Harness loses track of state. The developer doesn't realize quality is dropping. |
| **Agent hallucination in edits** | The handbook focuses on agents *not doing enough* but doesn't address agents generating plausible-looking but incorrect code (e.g., calling APIs that don't exist, fabricating test assertions). | Test rings catch *some* of this, but semantic correctness bugs slip through. |
| **Stale context between waves** | When Wave 2 depends on Wave 1's output, the harness must re-read files. If it relies on cached context from the plan phase, agents operate on stale code. | The handbook mentions "context" for wave dependencies but doesn't flag this as a failure mode. |
| **Prompt injection via code** | An agent reading existing code could encounter patterns that mislead its behavior. Adversarial or accidentally confusing code is a risk. | Not a theoretical concern — complex codebases have misleading comments, dead code, and conflicting patterns. |
| **Cost runaway** | No mention of token/cost tracking. 15 agent dispatches across premium models adds up. A failed wave with retries can 3-4x the cost. | Practitioners need guidance on cost monitoring and budget guardrails. |
| **The "almost done" trap** | An agent completes 90% of its task, reports success, but misses edge cases. The harness marks the task done. You discover the gap 2 waves later. | The spot-check protocol helps but doesn't systematically prevent this. Need structured verification commands in agent prompts. |
| **Merge conflict with parallel development** | The handbook assumes a single developer on a branch. What happens when another developer's PR lands mid-wave and your branch needs rebasing? | Wave commits can conflict with upstream changes. No guidance on rebase-during-execution. |
| **Agent persona drift** | Over time, as you add rules to personas, they become bloated and contradictory. The feedback loop creates ever-growing instruction sets. | The handbook's "fix the primitive" advice doesn't address primitive maintenance and pruning. |
| **Session state loss** | Copilot CLI sessions can disconnect. What happens to the wave state, the SQL tables, the partial progress? | The handbook doesn't cover recovery from session crashes. PR #394 mentions "recovered a stuck agent" but not session loss. |

---

## 5. Tool Dependency Assessment

### Portability matrix

| Concept | Copilot CLI specific? | Works with Cursor? | Works with Claude Code? | Works with future tools? | Portability rating |
|---|---|---|---|---|---|
| Meta-process (Audit→Plan→Wave→Ship) | ❌ Universal | ✅ | ✅ | ✅ | 🟢 Fully portable |
| Wave execution model | ❌ Universal | ✅ | ✅ | ✅ | 🟢 Fully portable |
| One-file-one-agent rule | ❌ Universal | ✅ | ✅ | ✅ | 🟢 Fully portable |
| Checkpoint discipline | ❌ Universal | ✅ | ✅ | ✅ | 🟢 Fully portable |
| Escalation protocol | ❌ Universal | ✅ | ✅ | ✅ | 🟢 Fully portable |
| Feedback loop | ❌ Universal | ✅ | ✅ | ✅ | 🟢 Fully portable |
| Test ring model | ❌ Universal | ✅ | ✅ | ✅ | 🟢 Fully portable |
| Three-layer instrumentation | ⚠️ Partially | ⚠️ Different format | ⚠️ Different format | ⚠️ Unknown | 🟡 Concept portable, format varies |
| Agent persona files (.agent.md) | ✅ Copilot-specific format | Cursor uses .cursorrules | Claude uses CLAUDE.md | Unknown | 🟡 Concept portable, format tool-specific |
| Skills (SKILL.md) | ✅ Copilot-specific | No direct equivalent | No direct equivalent | Unknown | 🔴 Tool-specific |
| Instructions (.instructions.md) | ✅ Copilot-specific | Cursor has .cursor-rules | Claude has settings | Unknown | 🟡 Concept exists, format varies |
| Harness internals (SQL, session state) | ✅ Copilot CLI only | ❌ Not applicable | ❌ Not applicable | ❌ | 🔴 Tool-specific |
| Sub-agent dispatch (task tool) | ✅ Copilot CLI only | Cursor has multi-file edit | Claude Code has sub-tasks | Varies | 🟡 Concept portable, API tool-specific |
| Dashboard POC (hooks) | ✅ Copilot CLI hooks only | ❌ | ❌ | ❌ | 🔴 Tool-specific |

### Overall portability verdict

**The high-level methodology is fully portable.** The meta-process, wave execution, checkpoints, escalation, and feedback loops are tool-agnostic patterns that work with any AI coding assistant capable of dispatching multiple tasks.

**The implementation details are Copilot CLI-specific.** Agent files, skill activation, instruction scoping, SQL-based task tracking, and hook-based dashboards are tied to Copilot CLI's architecture.

**For the new handbook**: Present the methodology as universal. Use Copilot CLI as the reference implementation but include "translation notes" showing how the same concept maps to Cursor, Claude Code, and generic tool X. The WIP handbook is too tightly coupled to Copilot CLI — roughly 40% of the content is implementation detail that won't transfer.

---

## 6. What's Missing for the New Handbook

Topics the WIP handbook does NOT cover that Block 2 needs:

### Critical gaps

| Topic | Why it matters | New handbook chapter |
|---|---|---|
| **Context engineering** | The WIP handbook treats context as "give agents precise instructions" but doesn't cover: context window budgeting, retrieval-augmented generation for large codebases, how to structure knowledge for agent consumption, long-term context vs. session context. This is the #1 skill gap for practitioners. | Ch 8: Context Engineering |
| **Agent primitive design** | The WIP handbook shows finished primitives (personas, skills, instructions) but doesn't teach how to *design* them. What makes a good persona vs. a bad one? How do you test a skill rule? What's the iteration cycle? | Ch 9: Agent Primitives |
| **Delegation patterns** | When to use one agent vs. many. When to parallelize vs. serialize. How to scope a task so an agent can complete it autonomously. The WIP handbook implies these decisions but doesn't formalize them. | Ch 11: Delegation & Orchestration |
| **Team adoption** | How does this scale from one practitioner to a team? What changes when 5 developers share agent primitives? How do you onboard someone who's never used agents? Code review processes for agent-generated code? | Ch 13: Team Scale |
| **Cost and token economics** | Zero mention in the WIP handbook. Real practitioners need to understand model selection, token budgets, cost per wave, ROI calculations at the task level. | Ch 12: Tooling & Distribution |
| **Security model for agent-generated code** | The WIP handbook has a security principle (#1 priority) but no security *practices*. How do you audit agent-generated code for vulnerabilities? What's the threat model when agents have filesystem access? | Ch 14: Anti-Patterns & Failure Modes |
| **Incremental adoption path** | The WIP handbook goes from 0 to "full fleet deployment" with no intermediate steps. "Just try it on a single file change" → "Use it for a refactor" → "Scale to cross-cutting changes" → "Full agentic SDLC." | Ch 10 or Ch 13 |

### Nice-to-have gaps

| Topic | Notes |
|---|---|
| **Metrics and measurement** | How do you know the agentic process is actually faster? What to measure, how to baseline, how to track improvement. |
| **Model selection per task type** | When to use Opus vs. Sonnet vs. Haiku. The WIP handbook mentions `claude-opus-4.6` for the architect but doesn't explain the selection logic. |
| **Multi-repository orchestration** | The WIP handbook is single-repo. Real projects span multiple repos. How do wave dependencies work across repo boundaries? |
| **Regulatory and compliance considerations** | For practitioners in regulated industries: audit trails, reproducibility requirements, approval workflows for agent-generated changes. |

---

## 7. Chapter Mapping Recommendation

Mapping WIP handbook sections (§1–§15) to new Block 2 chapters (Ch 8–14):

### Chapter 8: The Practice — Context Engineering

| Source | Action | Notes |
|---|---|---|
| §3 (Repository Instrumentation) | **Merge in** — restructure as "context engineering via markdown" | The three-layer cascade is context engineering. Frame it that way. |
| NEW | **Add** — context window management, retrieval patterns, knowledge structuring | The WIP handbook's biggest gap. Must be original content. |
| NEW | **Add** — "minimal viable context" starter template | Monday-readiness requirement. |

### Chapter 9: Agent Primitives

| Source | Action | Notes |
|---|---|---|
| §3 (Agents layer) | **Extract** — agent persona design principles | Promote from "here's a persona" to "here's how to design one." |
| §3 (Skills layer) | **Extract** — skill rule design patterns | Same: teach design, not just show examples. |
| §3 (Instructions layer) | **Extract** — instruction scoping patterns | |
| §11 (Feedback Loop) | **Merge in** — primitive improvement cycle | The feedback loop IS primitive iteration. They belong together. |
| NEW | **Add** — testing and validating primitives, primitive maintenance and pruning | |

### Chapter 10: Execution — The Meta-Process

| Source | Action | Notes |
|---|---|---|
| §4 (The Meta-Process) | **Keep largely intact** — this is gold | Core content. Proven. Well-structured. |
| §5 (Planning Discipline) | **Merge in** — planning is part of the meta-process | Don't give planning its own chapter; it's one phase. |
| §7 (Wave Execution) | **Merge in** — waves are the execution phase | Same: this is the meta-process in action. |
| §8 (Checkpoint Discipline) | **Merge in** — checkpoints are the validation phase | |
| §15 Scenario A | **Keep** as the worked example | Only the battle-tested scenario. |
| §15 Scenarios B/C/D | **Cut or demote** to sidebar "thought exercises" | Unvalidated. |

### Chapter 11: Delegation & Orchestration

| Source | Action | Notes |
|---|---|---|
| §6 (Team Topology) | **Merge in** — team composition is a delegation decision | |
| §10 (Escalation Protocol) | **Merge in** — escalation is the boundary of delegation | |
| §2 (The Thesis) — partial | **Extract** — "parallelize planning, not coding" | The core delegation principle. |
| NEW | **Add** — task scoping for agents, parallelization decision framework, when to intervene vs. let run | |

### Chapter 12: Tooling & Distribution

| Source | Action | Notes |
|---|---|---|
| §1 (Three Actors) — partial | **Extract** — the harness concept (tool-agnostic) | Present as "your orchestration tool" not "Copilot CLI specifically." |
| Appendix C (Harness Internals) | **Cut or heavily condense** | Too Copilot CLI-specific. Keep only the concept of "the tool tracks state for you." |
| Appendix D (Dashboard POC) | **Cut entirely** | Unvalidated, tool-specific, speculative. Doesn't belong in a practitioner handbook. |
| NEW | **Add** — tool comparison matrix, APM for agent config distribution, cost/token economics, model selection guidance | |
| Strategy docs | **Reference** — the cross-tool governance argument from March strategy updates is relevant context | Don't copy strategy docs, but the multi-tool reality informs tooling guidance. |

### Chapter 13: Team Scale

| Source | Action | Notes |
|---|---|---|
| §14 (Scaling Characteristics) | **Merge in** — partial, the "what scales" analysis | Keep the scaling tables. Cut the "safety argument" (it's in Ch 10 as part of the meta-process value prop). |
| §6 (Team Topology) — scaling section | **Merge in** — the "scaling up/down" guidance | |
| NEW | **Add** — onboarding new practitioners, shared primitive libraries, code review for agent-generated code, organizational adoption path | This is the biggest new-content need after context engineering. |
| §12 (Autonomous CI/CD) | **Move here** — with heavy "emerging practice" caveat | Autonomous workflows are a team-scale concern, not a solo-practitioner topic. Clearly mark as aspirational. |

### Chapter 14: Anti-Patterns & Failure Modes

| Source | Action | Notes |
|---|---|---|
| §13 (Anti-Patterns) | **Keep all 7** — they're solid | |
| §9 (Test Ring Pipeline) | **Merge in** — test rings are the primary failure-prevention mechanism | Frame as "the safety net that catches failures." |
| NEW | **Add** — the 9 missing failure modes from Section 4 of this audit | Context exhaustion, hallucination, stale context, cost runaway, the "almost done" trap, session state loss, persona drift, merge conflicts, prompt injection. |

### What gets cut entirely

| Source | Reason |
|---|---|
| §1 first paragraph ("You might speak to terminals…") | Aspirational fluff. Undermines credibility. |
| §2 (The Thesis) as standalone section | Distribute the useful parts. The philosophical framing belongs in Block 0, Ch 1. The practitioner-relevant principles embed in Ch 10/11. |
| Appendix A (Repository Setup Checklist) | Collapse into Ch 8 as a "getting started" sidebar. |
| Appendix B (Prompt Examples) | Distribute examples into their relevant chapters (audit prompts in Ch 10, wave prompts in Ch 10, recovery in Ch 11). |
| Appendix C (Harness Internals) | Too tool-specific. Condense to 2 paragraphs in Ch 12. |
| Appendix D (Dashboard POC) | Unvalidated. Not practitioner content. Could live in a separate "experiments" repo. |

### Summary transformation

```
WIP (15 sections + 4 appendices)
     │
     ├─ §3 ──────────────────────→ Ch 8 (Context Engineering) [expand]
     ├─ §3 + §11 ────────────────→ Ch 9 (Agent Primitives) [expand]
     ├─ §4 + §5 + §7 + §8 + §15A → Ch 10 (Meta-Process) [consolidate]
     ├─ §2 + §6 + §10 ──────────→ Ch 11 (Delegation) [expand]
     ├─ §1(partial) + NEW ───────→ Ch 12 (Tooling) [mostly new]
     ├─ §12 + §14 + NEW ────────→ Ch 13 (Team Scale) [mostly new]
     ├─ §9 + §13 + NEW ─────────→ Ch 14 (Anti-Patterns) [expand]
     │
     ├─ §2(thesis) ─────────────→ Block 0, Ch 1 [redirect]
     └─ §15 B/C/D, App C/D ────→ CUT
```

**Content reuse estimate**: ~50% of WIP content carries forward (the battle-tested gold). ~20% needs heavy rewriting for tool-neutrality. ~30% is cut or replaced with new content addressing the gaps identified in this audit.

---

## Final Verdict

The WIP handbook is the strongest source of *proven methodology* for the new handbook's practitioner block. The meta-process, wave execution, checkpoint discipline, and feedback loop are genuine contributions to the field — not because they're theoretically elegant, but because they shipped a 70-file, 2,874-test PR with zero regressions.

**Three things to preserve at all costs:**
1. The PR #394 evidence. Specific numbers, specific timings, specific failure-and-fix stories. This is the credibility anchor.
2. The feedback loop → primitive improvement cycle. This is the insight that separates "using AI tools" from "engineering an AI-native process."
3. The escalation protocol. The 4-level framework (self-heal → harness → you decide → scope change) is immediately useful and tool-agnostic.

**Three things to fix:**
1. Tool coupling. Decouple methodology from Copilot CLI implementation details. The handbook should teach principles that work with any tool.
2. Missing practitioner topics. Context engineering, delegation patterns, team adoption, and cost economics are critical gaps.
3. Intellectual honesty. Remove "zero regressions" absolute claims, voice input lifestyle claims, and unvalidated scenarios. The real evidence is strong enough — don't dilute it with speculation.
