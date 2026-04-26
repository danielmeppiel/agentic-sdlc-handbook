# Concepts Extracted — Practitioner Block (Ch08–Ch15)

**Purpose.** This document is the upstream input to the proposed arc. It enumerates the durable concepts that a *human developer* needs to understand in order to build, ship, and operate agentic systems — with each concept argued from first principles, mapped to its source in the field (Genesis skill, current handbook drafts, third-party harness docs), and tagged for handbook coverage status.

**Directionality contract.** The handbook is the canonical reference book for the *human* engineer encountering a new computer (the LLM + harness + filesystem substrate). Genesis is one operational *agent-side* implementation that an agent may load to perform architectural design tasks. We borrow vocabulary where it earns its place, but Genesis pattern codes (A1, B8, R1–R4, ATTENTION ANCHOR, etc.) are agent-side machine codes and MUST NOT be load-bearing structure in the handbook.

**Coverage tags.**
- **NO** — the concept is absent from current Ch08–Ch15.
- **PARTIAL** — the concept is touched but not named, not depth-ed, or not connected to its consequences.
- **WRONG-FRAME** — the handbook teaches a related artifact but in the wrong direction (reads as agent ops manual rather than developer reference).
- **YES** — the concept is well-covered and only needs cross-reference fixes.

**Gap categories.** The user named 8 gap categories. Through extraction we surface 4 more, for 12 total. Each concept below is mapped to one or more gap categories.

---

## Gap categories

| ID  | Name                                                | Origin               |
|-----|-----------------------------------------------------|----------------------|
| G1  | The runtime machine                                 | user-named           |
| G2  | Load lifecycle / the "compiler" model               | user-named           |
| G3  | Token economy and attention as a design constraint  | user-named           |
| G4  | Deterministic / probabilistic boundary              | user-named           |
| G5  | Failure model and debugging discipline              | user-named           |
| G6  | State separation (filesystem vs conversation)       | user-named           |
| G7  | DevEx for markdown-as-code                          | user-named           |
| G8  | Cross-harness reference matrix                      | user-named           |
| G9  | Distribution-surface hygiene (bundle leakage)       | extracted (Genesis)  |
| G10 | Substrate vs adapter separation                     | extracted (Genesis)  |
| G11 | Trigger-surface vs inference-harness orthogonality  | extracted (Genesis)  |
| G12 | Tool-call affordance as runtime property            | extracted (Genesis)  |

---

## The concepts

Each entry: *name (plain English)*, *why a human needs it*, *classical analog*, *source pointer*, *current handbook status*, *gap category*.

### Foundational: the runtime machine

**1. The agent runtime is a four-part machine.** Every agentic system is the composition of (a) an inference model, (b) a harness/runtime that drives it, (c) a filesystem layout the harness consults to assemble context, and (d) one or more trigger surfaces that decide *when* the harness runs. A human developer who cannot name these four parts cannot reason about why their setup behaves differently in Cursor vs Codex vs gh-aw.
*Classical analog:* the kernel-plus-shell-plus-filesystem-plus-init-system stack of a Unix box.
*Source:* Genesis `runtime-affordances/common.md` defines the substrate as the union of these parts; per-harness adapters demonstrate the variance.
*Status:* **NO.** Ch04 names "agentic computing stack" abstractly; Ch08–Ch15 do not separate harness from model from filesystem-as-loader.
*Gap:* G1.

**2. Markdown that steers an LLM is code.** The `.md` files committed to the repo are not documentation — they are programs that load into a context window and direct inference. They have a parser (the harness), a linker (the loader), a runtime (the model), and failure modes (attention decay, missing dependency). Treating them as docs is the single largest category error in the field.
*Classical analog:* config-as-code (Terraform, k8s manifests) — declarative artifacts that *execute* through a runtime.
*Source:* implicit throughout Genesis (every primitive is a markdown file with binding semantics); explicit in `primitives.md` "MODULE ENTRYPOINT" definition.
*Status:* **PARTIAL.** Ch09 calls primitives "atomic units of agentic behavior" but the meta-thesis is never stated. Ch11 ("context engineering") is the closest the handbook gets to admitting these files are code.
*Gap:* G1, G7.

**3. The harness is the compiler; the filesystem is the source tree.** Different harnesses (Copilot, Claude Code, Cursor, Codex, OpenCode) parse different file conventions in different orders. A `.cursor/rules/` glob does not exist for Codex. A `CLAUDE.md` is silent in Cursor. The harness — not the model — determines what gets loaded.
*Classical analog:* the relationship between a C compiler's include-path resolution and the source tree layout. Different compilers, same headers, different reach.
*Source:* `runtime-affordances/per-harness/{claude-code,copilot,cursor,codex,opencode}.md` — five concrete adapter specs.
*Status:* **NO.** Ch09 has a tool-support table (mid-2025) but presents it as feature parity rather than the load-determining substrate property it actually is.
*Gap:* G1, G2, G8.

**4. Inference is per-thread; the filesystem is shared.** A conversation is a finite stream of tokens local to one model invocation. Files on disk are durable, mutable, and visible to all threads. This split — conversation-state vs filesystem-state — is the single most important structural property of agentic systems and dictates almost every design pattern that follows.
*Classical analog:* process memory vs the filesystem on a Unix box. Any senior engineer has the intuition; what is missing is the realization that this partition applies one tier higher in the stack.
*Source:* Genesis `architectural-patterns.md` A4 SIBLING THREADS / A5 DELEGATED WORKER define how spawned threads have independent context but shared FS; `composition-substrate.md` "PORTABILITY MODE" depends on this split.
*Status:* **NO.** Ch12 (multi-agent) discusses session isolation but never frames the thread-vs-FS separation as a first-class property.
*Gap:* G1, G6.

### Foundational: the load lifecycle

**5. Primitives have binding modes.** Some primitives bind because the *agent* (the inference loop) decides to load them based on a description match — these are agent-invoked. Others bind because the *substrate* (the trigger surface) decides to load them based on event match — these are substrate-invoked. A skill is agent-invoked. A workflow file is substrate-invoked. Confusing the two is how operators ship a "skill" that never activates.
*Classical analog:* lazy import (agent-invoked) vs entrypoint registration (substrate-invoked).
*Source:* Genesis `primitives.md`, "Primitive vs module" and "Binding modes" sections.
*Status:* **NO.** Ch09 lists primitives but never explains binding semantics.
*Gap:* G2.

**6. Load order is observable and matters.** The harness loads in a defined order: persona scoping files first, then scope-attached rules matching the active file, then on-demand modules whose descriptions match the request, then any child threads spawned from the parent. This order is not flat — later layers can refine but cannot blindly override earlier ones.
*Classical analog:* CSS specificity and `@import` cascades; or Git's `.gitignore` resolution from root to leaf.
*Source:* Genesis `runtime-affordances/common.md` "What the substrate guarantees"; `composition-substrate.md` "INLINE / LOCAL SIBLING / EXTERNAL MODULE" composition modes.
*Status:* **PARTIAL.** Ch10's "Explicit Hierarchy" constraint and Ch11's "Instruction Hierarchy" describe the *result* but not the load-time *mechanism*.
*Gap:* G2, G3.

**7. The transitive-closure question.** When a primitive declares an external dependency, the loader must resolve that reference, fetch the target, and recurse — exactly like a package manager building a dep tree. The handbook needs to teach the developer to ask: *what is the closure of files that load when my agent runs?* This question is the equivalent of `npm ls` or `pip freeze` for agent context.
*Classical analog:* dependency resolution and lockfiles in any package manager.
*Source:* Genesis `composition-substrate.md` defines TRANSITIVE CLOSURE and VERSION PINNING as substrate concepts; `module-system-adapters/apm.md` maps them to APM realization.
*Status:* **NO.** Ch09 hints at sharing context files via `apm install` in a footnote but never frames closure as a debugging tool.
*Gap:* G2, G7, G9.

### Token economy and attention

**8. Context is finite, attention degrades non-linearly.** Doubling input length does not halve output quality; it crosses a threshold past which the model loses the thread entirely. A human developer needs to internalize attention as a *physical* property of the runtime, not as a soft preference.
*Classical analog:* CPU cache pressure and memory bandwidth — past a working-set threshold, performance does not degrade gracefully, it collapses.
*Source:* Genesis `pattern-tradeoffs.md` truth #1 ("CONTEXT IS FINITE AND FRAGILE"); B4 PLAN MEMENTO and B8 ATTENTION ANCHOR are direct countermeasures.
*Status:* **PARTIAL.** Ch10 (Progressive Disclosure) and Ch11 (Context Budget) name the symptom but never make the physics explicit. Ch08 mentions context window once.
*Gap:* G3.

**9. Plan-write-then-reload is the cure for attention decay.** Long sessions drift because earlier turns get pushed out of effective attention. The discipline is to write the plan to a file *during* the session and reload it at decision points. The plan becomes external memory the harness can re-cite into context.
*Classical analog:* checkpoint files in long-running batch jobs; journaling filesystems.
*Source:* Genesis B4 PLAN MEMENTO and B8 ATTENTION ANCHOR (`design-patterns.md`).
*Status:* **PARTIAL.** Ch11 mentions memory files and Ch13 references plan persistence in waves; the *anti-decay* framing is missing.
*Gap:* G3, G6.

**10. The bounded-scope rule for external grounding.** Whenever the agent reaches outside its corpus (web fetch, repo read, MCP call), the design must specify what the external source is *authoritative for*. Authority overreach — letting the fetched corpus dictate the framing of questions it does not own — is one of the most common silent-quality failures.
*Classical analog:* dependency injection with explicit interfaces; "depend on abstractions, not concretions."
*Source:* Genesis `pattern-tradeoffs.md` "Grounding doctrine"; primitives.md taxonomy example.
*Status:* **NO.** Ch10 and Ch11 discuss progressive disclosure but never the authority-scope rule.
*Gap:* G3, G4.

### The deterministic / probabilistic boundary

**11. Two computers, one program.** An agentic system is the *composition* of a deterministic computer (the harness, the file I/O, the tool calls, the test runner, the gh-aw lockfile) and a probabilistic one (the model). Treating the whole thing as probabilistic produces shrugs in the face of failures. Treating the whole thing as deterministic produces unsupervised outages.
*Classical analog:* the CPU/GPU split in a graphics program — both are computers, they have different correctness models, your code must respect the seam.
*Source:* Genesis S7 DETERMINISTIC TOOL BRIDGE (`design-patterns.md` lines 319–435) names this seam as a first-class pattern; A9 SUPERVISED EXECUTION captures the strong-form realization (gh-aw safe-outputs).
*Status:* **NO.** Ch10 and Ch11 talk about safety boundaries but never name the boundary as a deterministic/probabilistic seam.
*Gap:* G4.

**12. Consequential side effects belong to the deterministic side.** Anything that mutates external state — git push, file write outside the workspace, API call with side effects, GitHub issue creation — should pass through a deterministic gate that the model *requests* but does not *execute*. The model proposes; the gate disposes.
*Classical analog:* the system-call boundary in Unix — userspace cannot directly write to disk; it asks the kernel.
*Source:* Genesis A9 SUPERVISED EXECUTION (`architectural-patterns.md`); `runtime-affordances/per-trigger-surface/gh-aw.md` "CAPABILITY_GATING via safe-outputs".
*Status:* **PARTIAL.** Ch10 has "Safety Boundaries" but the framing is "what the agent must not do" rather than "where the deterministic gate sits."
*Gap:* G4, G5.

**13. Hallucination is a system property, not a model bug.** Pretraining is frozen; the model fabricates plausibly when asked about thin regions of its training. The cure is not "use a better model" — it is to architect grounding (lazy external corpus, explicit cutoff awareness) and verification (cold-reader review, programmatic check) into the design.
*Classical analog:* network unreliability in distributed systems — you do not "fix" it, you design retry and idempotency around it.
*Source:* Genesis truth #4 (`pattern-tradeoffs.md`) plus C2/C6/A7 countermeasures.
*Status:* **PARTIAL.** Ch14 has a "Hallucinated Edits" anti-pattern entry; the *system property* framing is missing.
*Gap:* G4, G5.

### Failure model and debugging

**14. The stack-trace equivalent for agentic failures.** When a traditional program fails, you read a stack trace. When an agent fails, you read (a) the loaded primitive set at decision time, (b) the plan-memento file if one exists, (c) the verbose tool-call log, and (d) the diff between expected and actual output. Knowing this list is the diagnostic skill that distinguishes a practitioner.
*Classical analog:* the `pstack` / `strace` / `lsof` triad on Unix.
*Source:* Ch09's annotated session (Turn 23) demonstrates the pattern in practice; Genesis `architectural-patterns.md` A8 ALIGNMENT LOOP describes the discipline.
*Status:* **PARTIAL.** Ch14 has a long failure-mode list but no unified diagnostic protocol.
*Gap:* G5.

**15. Silent semantic failure is the dominant failure shape.** Agent-generated code that compiles, passes shallow review, and encodes the wrong assumption is the failure that hurts most. Linters cannot catch it; tests cannot catch it unless the author already knows the answer. The cure is grounding (correct context loaded) plus adversarial review (a fresh-context thread reads the artifact).
*Classical analog:* off-by-one bugs and type-confusion errors in C — they compile, they sometimes pass tests, they ship and corrupt data.
*Source:* Genesis A7 ADVERSARIAL REVIEW; Ch09's Turn 5 EMU/ghu example is the canonical worked instance.
*Status:* **YES** in Ch14 (anti-pattern #6); but never connected to its architectural cure (A7-style cold reader).
*Gap:* G5.

**16. The four kinds of quality gate.** Quality gates split on two axes: who renders the verdict (the agent itself vs an outside source) and how it is rendered (programmatic vs judgement). The 2x2 is closed: (programmatic+internal) = test/lint, (judgement+internal) = goal-steward, (programmatic+external) = cold-reader-with-rubric, (judgement+external) = human checkpoint. Picking the wrong cell for the failure mode you are guarding against is a common design mistake.
*Classical analog:* CI's lint/test/integration tiers, but with two new cells (cold-reader-rubric, human-checkpoint) that classical CI lacks because classical code does not have probabilistic output.
*Source:* Genesis `pattern-tradeoffs.md` section 2 "Gate types".
*Status:* **NO.** Ch10's "Validation Gate" mentions one cell.
*Gap:* G4, G5.

### State separation

**17. Plan persistence is durable; conversation memory is not.** A plan written to `plan.md` survives a session crash, a context-window overflow, and a hand-off to a new thread. A plan held only in conversation does not. Designing for persistence is a substrate-level decision, not a polish step.
*Classical analog:* writing intermediate state to disk in a long-running ETL job.
*Source:* Genesis `primitives.md` "PLAN PERSISTENCE" primitive; `runtime-affordances/per-harness/copilot.md` notes Copilot's session-state SQLite plus `plan.md`.
*Status:* **PARTIAL.** Ch11 covers memory; Ch13 covers waves with checkpoints; the unifying primitive is missing.
*Gap:* G6.

**18. Child-thread spawn semantics differ across harnesses.** Claude Code's Task tool, Copilot's `task` agent dispatch, OpenCode's subagents — these are programmatic spawn primitives. Cursor and Codex (as of late 2025) lack programmatic spawn. The choice of harness determines what multi-agent topologies you can build.
*Classical analog:* `fork()` vs cooperative-only coroutine systems.
*Source:* Genesis `runtime-affordances/per-harness/{claude-code,copilot,cursor,codex,opencode}.md`.
*Status:* **NO.** Ch12 (multi-agent orchestration) treats spawn as universally available.
*Gap:* G6, G8.

### DevEx: markdown-as-code

**19. Lint-test-CI for primitives.** If markdown files are code, they can be linted (frontmatter schema, link integrity, scope coverage), tested (does this skill activate on its trigger description?), and gated in CI. Primitive lint catches drift before it ships.
*Classical analog:* `eslint`/`pyflakes`/`shellcheck` plus integration tests for any other code class.
*Source:* implicit; Genesis `composition-substrate.md` discusses VERSION PINNING and lockfile semantics; APM provides `apm compile` / `apm pack` as the toolchain.
*Status:* **NO.** No chapter teaches primitive linting.
*Gap:* G7.

**20. Lockfile semantics for context.** When primitives reference external modules, the resolved dep tree must be pinned. Otherwise next week's `apm install` produces different agent behavior with no code change visible in the diff. This is exactly the dependency-confusion problem npm faced; the cure is the same.
*Classical analog:* `package-lock.json` / `Cargo.lock` / `go.sum`.
*Source:* Genesis `composition-substrate.md` "VERSION PINNING"; `module-system-adapters/apm.md` mapping.
*Status:* **NO.** Ch09 mentions APM in a closing footnote.
*Gap:* G7, G9.

### Cross-harness reference matrix

**21. The matrix is data, not opinion.** Ch09 has a tool-support table that reads as a marketing comparison. The substrate-level matrix that practitioners need answers different questions: which harness loads which primitive type at which scope at which point in the session lifecycle? The data is concrete and citable.
*Source:* Genesis 5 per-harness adapters; ~580 lines of structured matrix data.
*Status:* **PARTIAL.** Ch09's table covers feature presence at a high level; the substrate-question answers are missing.
*Gap:* G8.

### Distribution-surface hygiene

**22. Bundle leakage and phantom dependency are dual failures.** *Phantom dependency:* a primitive references context that is not declared as a dependency, so consumers do not load it — agent fails silently. *Bundle leakage:* a primitive ships maintainer-only files that the consumer's loader picks up unintentionally — agent runs the wrong context. Both come from confusing distribution-surface (what you publish) with run-time scope (what the consumer's harness loads).
*Classical analog:* `__init__.py` over-exports in Python or PUBLIC vs INTERNAL APIs in any module system.
*Source:* Genesis `composition-substrate.md` and `module-system-adapters/apm.md` "APM publish-time rules" — the bundle-leakage failure shape (PAYLOAD BLOAT + DISPATCH CONTAMINATION) is named and cited.
*Status:* **NO.** No coverage.
*Gap:* G9.

### Substrate vs adapter

**23. The architect stays portable; the coder reaches for vendor syntax.** A design discussion expressed in vendor-specific syntax (e.g., a paragraph that uses `applyTo:` glob conventions) is locked to one harness. A design discussion expressed in substrate vocabulary (scope-attached rule, persona scoping file) ports across harnesses. The handbook's prose should be the substrate vocabulary; vendor syntax should appear only in worked examples and onboarding sections.
*Classical analog:* writing portable C against POSIX vs writing C against Linux-only `epoll`.
*Source:* Genesis `runtime-affordances/portability-rules.md`.
*Status:* **WRONG-FRAME.** Ch09 mixes substrate concepts with vendor syntax in adjacent paragraphs.
*Gap:* G10.

### Trigger surface vs inference harness

**24. Two orthogonal axes operators conflate.** The trigger surface (what causes the agent to run: a pull request, a `/skill` invocation, a workflow event, a webhook) is independent of the inference harness (which model and runtime executes once triggered). Different combinations have different audit and capability profiles. gh-aw is a trigger surface that pairs with any inference harness; Claude Code is an inference harness with its own built-in triggers; Copilot can be either.
*Classical analog:* cron (trigger) vs the executable it launches (runtime); the two are independently composable.
*Source:* Genesis `runtime-affordances/per-trigger-surface/gh-aw.md`; per-harness adapters discuss inference-harness side.
*Status:* **NO.** Ch12 and Ch13 treat triggers and harnesses as a single axis.
*Gap:* G11.

### Tool-call affordance

**25. MCP and tool calls are runtime properties, not primitive types.** A skill does not "have" an MCP — the runtime in which the skill executes does. Some harnesses expose rich tool-call affordances; others expose only file I/O. Designing a skill that assumes a specific tool exists couples the design to a runtime; designing against the substrate concept ("the agent must be able to read a remote spec") leaves the realization to the runtime adapter.
*Classical analog:* a Python script that assumes `subprocess` exists vs one that abstracts I/O behind an interface.
*Source:* Genesis `primitives.md` "Tool-call affordance is a runtime property, not a primitive type" (explicit anti-pattern flag).
*Status:* **NO.** Ch09 lists "Hooks" as a primitive without separating the trigger surface from the action.
*Gap:* G12.

### Behavioral patterns

**26. The attention anchor pattern.** Re-stating goal, scope, and acceptance criteria at decision points inside a long session is not redundancy — it is the cure for the physics of attention decay (concept #8). It has no exact classical analog because no traditional program has attention as a runtime property. This is a new pattern with no old name.
*Source:* Genesis B8 ATTENTION ANCHOR (`design-patterns.md` lines 617–684).
*Status:* **NO.** Ch11 hints at it via "instruction hierarchy"; the pattern as a behavioral discipline is not named.
*Gap:* G3.

**27. Refactor patterns for primitives.** Just as code is refactored, primitives are refactored. The four basic moves are: SPLIT a too-large primitive into focused siblings; FUSE small siblings that always co-load; EXTRACT a shared sub-primitive; INLINE a single-consumer reference. Knowing the moves prevents accidental architectural drift.
*Classical analog:* Fowler's refactoring catalog, mapped to a different artifact class.
*Source:* Genesis `refactor-patterns.md` (R1–R4).
*Status:* **NO.** No coverage.
*Gap:* G7.

**28. Pattern selection on tradeoff axes, not check-off lists.** Two patterns can fit the same slot. The discipline is to pick on axes — gate type, grounding doctrine, threading topology — not by enumeration. A naked pattern recommendation ("use a reviewer agent") is harder to remember than a pattern paired with the system property it serves ("hallucination is inherent → cold-reader review with programmatic rubric").
*Source:* Genesis `pattern-tradeoffs.md` (entire file).
*Status:* **NO.** Ch12 and Ch13 list patterns; none teach selection on axes.
*Gap:* G4, G5.

### Threading topology

**29. Parallel-vs-sequential threads x shared-vs-isolated state.** Multi-agent design is a 2x2: parallel threads on shared state (race), parallel threads on isolated state (map-reduce), sequential threads on shared state (pipeline), sequential threads on isolated state (relay). Each cell has different correctness obligations. Ch12 implicitly inhabits one cell ("one-file-one-agent" = parallel + isolated by file partition) without naming the design space.
*Source:* Genesis `pattern-tradeoffs.md` section 4 "Threading topology".
*Status:* **PARTIAL.** Ch12 covers wave-based parallelism well but does not name the closed 2x2.
*Gap:* G6, G11.

### Outer-loop governance

**30. The governed outer loop.** Wrapping the agent in a substrate (gh-aw, a CI workflow) that holds the credentials, gates the side effects, and provides the audit trail is the production-grade realization of the "agent never holds the GitHub write token" principle. Strong-form A9 SUPERVISED EXECUTION is what makes agent-driven PRs auditable for compliance.
*Classical analog:* sudoers + auditd; or in cloud terms, the IAM-mediated step-function that calls the lambda but holds the role.
*Source:* Genesis A10 GOVERNED OUTER LOOP; `runtime-affordances/per-trigger-surface/gh-aw.md` SANDBOXING + CAPABILITY_GATING + AUDIT_SURFACE fields.
*Status:* **NO.** Ch12/Ch13 discuss orchestration; gh-aw governance is unmentioned.
*Gap:* G4, G11.

---

## Coverage summary

Of the 30 concepts:
- **NO** coverage in current handbook: 18
- **PARTIAL** coverage: 9
- **WRONG-FRAME** coverage: 1
- **YES** coverage: 1

This is the corrective signal: the *practitioner block* in its current form teaches the *artifacts* (the seven primitives, the PROSE constraints, the wave protocol) extremely well, but does not teach the underlying *machine*. A reader finishing Ch08–Ch15 today knows what to build but cannot reason about why a primitive that worked in Cursor stops working in Codex, or why a 6,000-token instruction file degrades agent quality despite the model's 200K context window, or where exactly the deterministic gate sits in their `safe-outputs:` block. Those are the gaps the v2 arc must close.
