# Chapter 14: Anti-Patterns and Failure Modes

Every technique in this book was born from a failure. The wave execution model exists because a developer tried to run 15 agents at once and got a merge conflict graveyard. The checkpoint discipline exists because someone skipped testing after wave 2 and spent three hours debugging a cascade that started in wave 1. The escalation protocol exists because an agent claimed a file was updated when it wasn't, and no one checked until the PR review.

This chapter documents 16 distinct ways AI-native development goes wrong, why each failure happens, which PROSE constraint it violates, and how to prevent or recover.

The uncomfortable truth: AI failures don't crash. They produce plausible wrong output. An agent that silently violates your architecture or ignores a security boundary produces code that compiles, might pass tests, and enters your codebase as technical debt you don't know you have. Learning to see these failures before they ship is the skill that separates effective AI-native development from expensive AI-assisted typing.

---

## The Taxonomy

Every anti-pattern maps to a PROSE constraint. This isn't a taxonomy imposed after the fact — it's why the constraints exist. Each constraint was articulated because a class of failures kept recurring, and ad-hoc fixes weren't enough.

| # | Anti-Pattern | Constraint Violated | Summary |
|---|---|---|---|
| 1 | Monolithic Prompt | Orchestrated Composition | All instructions in one block; small changes cause unpredictable cascades |
| 2 | Context Dumping | Progressive Disclosure | Everything loaded upfront; capacity wasted, attention diluted |
| 3 | Unbounded Agent | Safety Boundaries | No limits on tools or authority; non-determinism plus unlimited access |
| 4 | Flat Instructions | Explicit Hierarchy | Same rules everywhere; backend security rules load when editing CSS |
| 5 | Scope Creep | Reduced Scope | Task grows mid-execution; agent loses coherence as context degrades |
| 6 | The Solo Hero | Orchestrated Composition | One massive agent doing everything; no decomposition, no review |
| 7 | The Trust Fall | Safety Boundaries | Accepting agent output without verification |
| 8 | Same-File Parallel Edits | Orchestrated Composition | Two agents editing one file; second agent's changes fail silently |
| 9 | Skipping Checkpoints | Safety Boundaries | Committing multiple waves without validation between them |
| 10 | Not Fixing the Primitives | Explicit Hierarchy | Correcting symptoms manually instead of updating the instruction set |
| 11 | Context Window Exhaustion | Progressive Disclosure | Agent hits capacity mid-task and silently drops earlier instructions |
| 12 | Hallucinated Edits | Safety Boundaries | Agent reports success on changes it didn't persist |
| 13 | Stale Context Between Waves | Progressive Disclosure | Agent in wave N works against wave N-2 state of a file |
| 14 | Cost Runaway | Reduced Scope | Unbounded retries burn tokens without progress |
| 15 | The "Almost Done" Trap | Reduced Scope | Last 10% takes longer than starting over |
| 16 | Session State Loss | Safety Boundaries | Session crashes; no checkpoint means unrecoverable work |

Patterns 1-5 are the foundational anti-patterns from Chapter 1. Patterns 6-10 emerge from multi-agent execution mechanics. Patterns 11-16 were identified through systematic audit of what early documentation missed. All sixteen are real. All sixteen have cost teams real time, money, and trust.

---

## The Five Foundational Anti-Patterns

These are the patterns from Chapter 1's PROSE constraint table, expanded with worked scenarios.

### 1. The Monolithic Prompt

**Symptom.** One large instruction file containing every rule for your entire project. Adding a new rule breaks something unrelated. The agent ignores rules near the bottom or applies backend conventions to frontend code.

**Root cause.** Models interpret context probabilistically, not sequentially. Every instruction competes for attention. Adding content changes the probability distribution over all existing rules.

**Constraint violated.** Orchestrated Composition.

**Scenario.** A team's single 400-line instructions file covers Python style, security, APIs, database patterns, and tests. They add 30 lines of logging standards. Agents begin ignoring the database connection pooling rules that had worked for weeks — the new content shifted attention away from them.

**Prevention.** Decompose into composable primitives: agent personas for domain expertise, skills for cross-cutting concerns, file-scoped instructions for local conventions. When you add logging standards, they live in a logging skill, not alongside database rules.

**Recovery.** Extract the most volatile section into its own primitive. Validate for a week. Extract the next. Work outward from the pain.

### 2. Context Dumping

**Symptom.** You include your entire codebase in every agent context. Responses slow. Quality degrades. The agent fixates on irrelevant details from unrelated files.

**Root cause.** Context windows have limited attention, not just limited capacity. Flooding the window with irrelevant content gives the agent noise that competes with signal. A developer working on auth includes 50 files; the agent borrows error-handling patterns from CLI rendering code because that happened to be in context.

**Constraint violated.** Progressive Disclosure.

**Prevention.** Context budgeting. For each task, include only the target file, direct dependencies, and relevant primitives. The meta-process's planning phase does this naturally — each wave's task assignment specifies exactly which files each agent receives.

**Recovery.** Subtract files from context one at a time, re-running the task. You will likely find that removing irrelevant files *improves* quality.

### 3. The Unbounded Agent

**Symptom.** The agent has access to every tool and file with no restrictions. It makes changes you didn't ask for — refactors imports, renames methods, modifies test files to match its changes. Some changes are useful; most are harmful, and they're tangled into the same diff.

**Root cause.** Non-deterministic systems with unlimited authority produce variance not just in quality but in *scope*. Constraints reduce the surface area over which variance manifests.

**Constraint violated.** Safety Boundaries.

**Prevention.** The plan specifies which files each agent may modify. Instructions include "Do NOT modify" clauses. The harness enforces one file, one agent per wave.

**Recovery.** Revert to the last checkpoint. Rewrite the task with explicit scope constraints. Re-dispatch. Re-execution costs less than surgical extraction from a tangled diff.

### 4. Flat Instructions

**Symptom.** Every session loads the same instructions regardless of context. Domain-specific rules contradict each other because they were never meant to coexist. The agent resolves ambiguity unpredictably.

**Root cause.** Instructions that don't vary by scope are either too general to be useful or contain domain-specific rules that conflict across contexts.

**Constraint violated.** Explicit Hierarchy.

**Scenario.** A project's instructions include both "always use parameterized queries for database access" and "prefer simple string formatting for readability." An agent building a database query follows the formatting rule, producing a SQL injection vulnerability. The conflict existed for months without incident.

**Prevention.** Layer instructions global to local. Database patterns scope to `**/db/**`. Frontend patterns scope to `**/components/**`. Contradictions between domains never coexist in the same context.

**Recovery.** Audit instructions for cross-domain contradictions. Move domain-specific rules into scoped primitives, starting with the contradiction that caused the most recent failure.

### 5. Scope Creep

**Symptom.** A task that started as "add error handling to three functions" has grown to include refactoring, tests, logging, and a deprecation fix. Early output is solid; later output is inconsistent. The agent seems to "forget" constraints it followed earlier.

**Root cause.** Context is finite. As a session grows, earlier instructions compete with hundreds of lines of generated code for attention. The agent hasn't gotten worse; the effective context has degraded.

**Constraint violated.** Reduced Scope.

**Prevention.** Right-size tasks to context capacity. When scope expansion is discovered mid-task, the correct response is escalation (create a follow-up task), not absorption (add it to the current session).

**Recovery.** Stop. Commit what works. Create a new task for the expanded scope in a fresh session. Sunk cost of the current session is less than the debugging cost of degraded output.

---

## Execution Anti-Patterns

Five patterns that emerge from multi-agent execution mechanics.

### 6. The Solo Hero

One agent handles an entire feature. It produces a large, unreviewed diff — some parts excellent, others violating patterns it was never told about. No decomposition, no isolation of regressions.

**Fix.** One file, one agent per wave. Checkpoint discipline provides the review gate a solo agent lacks.

### 7. The Trust Fall

The agent says "Done. All changes applied." You commit without checking. Later: a file wasn't modified, tests weren't actually run, or an edge case the agent claimed to handle is missing from the code.

Agent self-reports are generated text, not system logs. An agent can "believe" it made a change that wasn't persisted. **This is the most dangerous pattern in the chapter** — it exploits the tendency to treat confident prose as authoritative.

**Fix.** Never rely on self-reports. Run the test suite. Verify file state with `git diff`. Spot-check critical changes. One line of diff output is worth a thousand words of agent narrative.

### 8. Same-File Parallel Edits

Two agents edit different sections of the same file in the same wave. The first completes; the second's edits fail because string matches no longer apply. In some tools, this fails silently.

**Fix.** One file, one agent per wave. Sequence cross-domain changes to the same file across waves.

### 9. Skipping Checkpoints

"Wave 1 worked, wave 2 is similar, let me batch them." Wave 3 fails. The root cause was wave 2, but without a checkpoint between them, you can't bisect. You debug three waves simultaneously.

**Fix.** Test after every wave. Commit after every wave. The two-minute checkpoint cost is insurance against three-hour debugging cascades.

### 10. Not Fixing the Primitives

An agent keeps making the same mistake across sessions — deprecated API, wrong pattern, invented method. Each time you correct the output manually. Next session, same mistake.

The correction happened in the code, not the instruction set. Manual corrections are patches on output; primitive updates are fixes to the system.

**Fix.** Every recurring failure triggers the feedback loop: identify the root primitive and add the missing rule. The system should learn, not repeat.

---

## The Nine Missing Failure Modes

Identified through systematic audit of early agentic practice. These represent gaps in original documentation — patterns that kept occurring but weren't formally catalogued.

### 11. Context Window Exhaustion

| | |
|---|---|
| **Symptom** | Output quality degrades partway through a task. Early functions are well-structured; later ones are sloppy or ignore constraints followed earlier. No error — just quietly worse output. |
| **Root cause** | The session exceeded effective context capacity. Earlier instructions are technically "in" context but the model no longer attends to them. |
| **Constraint violated** | Progressive Disclosure + Reduced Scope |
| **Severity** | High |
| **Prevention** | Right-size tasks. If the agent followed a convention in its first three functions but ignores it in the fifth, the context is exhausted. End session, checkpoint, start fresh. |
| **Recovery** | Revert degraded output. Split remaining work into a new task with fresh context. |

### 12. Hallucinated Edits

| | |
|---|---|
| **Symptom** | Agent reports specific changes to a file. The file on disk doesn't reflect them — the edit wasn't persisted, or the agent described planned changes it never executed. |
| **Root cause** | Self-reports are generated text. When an edit fails silently (string match not found, file locked), the agent may not register the failure and still report success. |
| **Constraint violated** | Safety Boundaries |
| **Severity** | Critical |
| **Prevention** | Verify file state after completion. `git diff` is ground truth. The checkpoint discipline catches functional regressions; spot-checks catch non-functional missing edits. |
| **Recovery** | Compare agent's reported changes against actual diff. Re-dispatch focused tasks for just the missing edits. |

### 13. Stale Context Between Waves

| | |
|---|---|
| **Symptom** | Agent in wave 3 references an old version of a function modified in wave 2. Code compiles (the function still exists) but uses the old calling convention or misses a new parameter. |
| **Root cause** | Context was assembled from cached file state. If the harness doesn't re-read files after each checkpoint, agents work against stale information. |
| **Constraint violated** | Progressive Disclosure |
| **Severity** | High |
| **Prevention** | Re-read file state after each wave before assembling next wave's context. Include explicit references to interface changes: "Note: `resolve()` now takes a `strict` parameter (added in wave 2)." |
| **Recovery** | Run integration tests that exercise cross-module interactions. Revert affected output and re-dispatch with current file content. |

### 14. Cost Runaway

| | |
|---|---|
| **Symptom** | A task that should have taken 3 dispatches has consumed 15. Each retry makes marginal or no progress. Token costs climb. |
| **Root cause** | Unbounded retry loops combined with scope absorption. Retrying without changing input is expecting different results from a non-deterministic system. |
| **Constraint violated** | Reduced Scope |
| **Severity** | Medium |
| **Prevention** | Set a retry budget. After two failed dispatches for the same task, change the approach: decompose further, add context, or escalate. Don't loop at the same level. |
| **Recovery** | Stop. Review what's been attempted. Often the agent is stuck because the task is underspecified. One specific constraint added to context is worth more than ten retries with the same input. |

### 15. The "Almost Done" Trap

| | |
|---|---|
| **Symptom** | Agent completed 90% of the task. The remaining 10% — an edge case, a subtle interaction — resists every attempt. Hours pass refining prompts. |
| **Root cause** | Some tasks are flat for 90% and vertical for the last 10%. The easy parts follow common patterns; the hard part requires novel reasoning about your specific system's constraints. Sunk cost makes starting over feel irrational, but closing the gap exceeds the cost of the complete task done differently. |
| **Constraint violated** | Reduced Scope |
| **Severity** | Medium |
| **Prevention** | Identify the hard part during planning. Consider doing it manually or as a separate, tightly-scoped agent task with maximum context. |
| **Recovery** | Accept the 90%. Commit it. Handle the rest manually or in a fresh session focused exclusively on the hard part. |

### 16. Session State Loss

| | |
|---|---|
| **Symptom** | Mid-task, the session crashes. Plan state, partial edits, task tracking — gone. Some files are partially edited, leaving the codebase inconsistent. |
| **Root cause** | Agent sessions are stateful but not durable. State lives in context and memory, not persistent storage. |
| **Constraint violated** | Safety Boundaries |
| **Severity** | High |
| **Prevention** | Commit after every wave. Externalize state that matters (plan file, task status) to persistent storage. Smaller waves mean smaller blast radius. |
| **Recovery** | Revert to last committed checkpoint. Re-read the plan. Re-dispatch from the last completed wave. Cost is one wave's re-execution, not the entire session. |

---

## The Silent Failure Problem

The failure modes above share a property that distinguishes them from traditional bugs: they don't announce themselves. A compiler error stops the build. An AI failure produces output that compiles, might pass tests, and reads well in review.

Three categories require different detection:

**Convention violations.** Code works but doesn't follow established patterns. Detection: primitive rules that encode conventions, code review agents, grep-based pattern audits.

**Semantic drift.** Code does approximately the right thing but misses a subtle constraint — handles the happy path but not the edge case your system depends on. Detection: boundary-condition tests, property-based testing, human review of business-critical logic.

**Architectural erosion.** Code introduces a coupling or boundary violation that won't fail immediately but degrades maintainability. Detection: architecture tests in CI, module boundary enforcement, periodic dependency graph review.

The common thread: silent failures are caught by *structure*, not by vigilance. If you rely on careful reading of agent-generated diffs to catch quality issues, you're already behind.

---

## Team-Level Anti-Patterns

Technical anti-patterns happen in code. Organizational anti-patterns amplify every technical failure in this chapter.

**Over-trust.** The team ships agent-generated code with minimal review. Agent code has different failure signatures than human code — locally correct but globally inconsistent. Each function works; the functions don't work together the way a human would have designed them.

**Under-specification.** No primitives. Each developer prompts ad-hoc, in their own style. Output quality varies wildly between team members — not because of skill differences, but context differences. The team blames the tool instead of the context.

**No feedback loop.** Failures happen, developers fix them manually, no one updates the primitives. The same mistake recurs weekly. The team experiences AI as unreliable because their system doesn't learn.

**Cargo-culting complexity.** The team implements full multi-agent orchestration for a 10-file repository with two developers. The overhead exceeds the benefit. The disciplines in this book scale *down* — a solo developer on a small change needs right-sized tasks and good primitives, not a four-wave plan with parallel review agents.

**Abandoned governance.** No one audits what agents modify outside stated scope. No one tracks token costs against value. AI usage grows organically without the structures that catch these patterns before they become expensive.

Each organizational pattern amplifies a technical one. Over-trust amplifies the Trust Fall. Under-specification causes Context Dumping. No feedback loop perpetuates Not Fixing the Primitives. The fix is organizational: team agreements, review processes, and treating primitives as shared infrastructure.

---

## The Recovery Playbook

When you've hit an anti-pattern and need to get back on track:

1. **Stop and assess.** Identify which anti-pattern from the taxonomy table. The symptom tells you where to look; the constraint tells you what's structurally wrong.

2. **Checkpoint what works.** Commit all passing code. Working code on a branch is preserved progress; code in an agent session is ephemeral.

3. **Revert what doesn't.** If agent output has contaminated files beyond the task's scope, revert to the last known-good state. Don't salvage sprawling changes.

4. **Decompose.** The most common recovery action. Whatever task was too large, too broad, or too underspecified — break it down. Write sub-tasks explicitly. Assign scope boundaries.

5. **Fix the primitive.** Before re-dispatching, add whatever instruction was missing or insufficient. This prevents recurrence in re-execution and every future session.

6. **Re-dispatch with constraints.** Fresh session, clean context, updated primitives, explicit scope boundaries. Re-execution costs less than debugging a contaminated session.

The hardest part is step 1 — not because identifying anti-patterns is difficult, but because it requires admitting the current approach isn't working. The sunk cost of a long session creates pressure to push forward. The playbook works only if you're willing to stop.

---

## The Failure Mode Decision Tree

When something goes wrong, the first question is what kind of wrong:

```
Something went wrong with agent output
    |
    +-- Is the code syntactically wrong?
    |       YES --> Model capability issue. Stronger model, better
    |               examples, or do it manually.
    |       NO  -->
    |
    +-- Do tests fail?
    |       YES --> Agent's code or pre-existing?
    |       |         Agent's --> Check: task too broad? (Scope Creep)
    |       |                    Check: context stale? (Stale Context)
    |       |                    Check: constraint dropped? (Exhaustion)
    |       |         Pre-existing --> Separate issue.
    |       NO  -->
    |
    +-- Does the code follow your conventions?
    |       NO  --> Primitive issue.
    |               Check: is the rule in the instruction set?
    |               Check: was the right primitive activated?
    |               Check: too much noise in context?
    |       YES -->
    |
    +-- Does it integrate correctly with the system?
            NO  --> Architectural issue.
                    Check: did the agent see the right interfaces?
                    Check: did it respect module boundaries?
            YES --> Probably fine. Verify edge cases.
```

---

## Security Practices for Agent-Generated Code

Agents have filesystem access, can execute commands, and generate code for your production environment. Three risks deserve specific attention.

**Prompt injection via code.** Files from external sources — dependencies, configuration from registries — can contain instructions the model interprets as commands. A malicious comment in a dependency is absurd to a human and a real attack vector for a model. Treat all external content in agent context as untrusted input.

**Scope escalation through side effects.** An agent modifying application code might also touch CI pipelines, deployment scripts, or configuration files if they're within filesystem access. A subtle workflow modification is easy to miss in a large diff. Restrict filesystem access to relevant directories. Review diffs for out-of-scope file changes.

**Credential exposure.** Agents reading environment files or test fixtures may echo sensitive values in output or embed them in generated code. Exclude credential files from context. Use secret scanning in CI.

These risks aren't unique to AI-generated code — they're amplified by volume. An agent generating 70 files in 90 minutes produces more review surface area than a human in the same timeframe. Review discipline must scale with generation speed.

---

## What This Chapter Is Not

This is not exhaustive. New failure modes will emerge as agent capabilities evolve. What this chapter provides is a framework — the PROSE constraint mapping, symptom-first identification, and structural prevention approach — that applies to failures we haven't seen yet.

If you encounter a failure not in this chapter, add it using the same format: symptom, root cause, constraint violated, prevention, recovery. The taxonomy is a living document.

These 16 patterns represent the collective scar tissue of early agentic development practice — the failures that wasted the most time, burned the most tokens, and eroded the most trust. Learn from them, and you skip the most expensive part of the learning curve.
