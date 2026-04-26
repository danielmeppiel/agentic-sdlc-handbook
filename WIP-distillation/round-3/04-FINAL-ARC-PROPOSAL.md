# Final Arc Proposal — Practitioner Block v2 (Ch08–Ch20 + Appendix A) — v1.1

**Status:** v1.1 (post author-review). Converged after one panel round; two structural additions applied per maintainer.
**Scope:** Plan-only. No `.qmd` files modified by the orchestrator. No git operations performed by the orchestrator. No branches created by the orchestrator. (Maintainer subsequently created `feat/practitioner-block-v2` to begin Wave A.)
**Audience:** the chief editor, the implementation team, and the maintainer.

**v1.1 deltas from v1.0 (maintainer instructions, 2026-04-26):**

1. **Ch08 strategic Genesis surfacing.** The practitioner's-mindset chapter now opens with an explicit recommendation to install the `danielmeppiel/genesis` skill as the agent-side companion that operationalizes the entire block. Genesis is the single skill that illustrates all the disciplines this Part III teaches — readers who run it as they read get a working reference. Genesis is named in Ch08, used as a worked-example source throughout, and named again in Ch20 (What Comes Next) as the canonical first install for teams entering the practice. The directionality contract is preserved: the handbook teaches the human, Genesis is named as one implementation, not promoted to load-bearing structure.
2. **New Ch17 — Architectural Patterns: A Rosetta Stone.** A standalone chapter for architects that catalogues the recurring agentic-design patterns and maps them to classical Gang-of-Four pattern names where the analogy holds. Treats the runtime as a layered system (model / harness / filesystem / triggers / threading / persistence) and presents pattern decisions per layer. This is the architects' chapter; it sits between Ch16 (Execution Meta-Process) and the renumbered Ch18 (Anti-Patterns). All chapters from old Ch17 onward shift by one (Anti-Patterns is now Ch18; Primitives as Code is now Ch19; What Comes Next is now Ch20). Total Part III chapter count: 13.

---

## 1. Executive summary

The Practitioner Block of *The Agentic SDLC Handbook* (currently Ch08–Ch15 in `_quarto.yml`) teaches *what to build* (the seven primitives, the PROSE constraints, the wave protocol) extremely well. It does not teach the *underlying machine* — the LLM, the harness, the filesystem-as-loader, the trigger surface, the threading model, and the persistence boundary that together constitute the substrate every agentic workflow runs on. A reader finishing the current Part III knows the artifacts but cannot reason about why a primitive that worked in Cursor stops binding in Codex, why a 6,000-token instruction file degrades agent quality despite a 200K context window, or where exactly the deterministic gate sits in their `gh-aw safe-outputs:` block. The corrective is structural, not editorial.

The v2 arc inserts five new chapters and one reference appendix into the practitioner block. The new chapters (Runtime Machine, Load Lifecycle, Attention and Context Economy, the Deterministic/Probabilistic Boundary, Primitives as Code) close the eight named gap categories the maintainer enumerated; the reference appendix (the Cross-Harness Reference) replaces the current mid-2025 tool-support table with a dated, citable substrate-property matrix. All eight existing chapters are preserved — some renumbered, two restructured — and the strongest existing material (the annotated Copilot session in current Ch09, the PR #394 case study in current Ch13, the seven-primitives catalogue in current Ch09) is kept intact.

The directionality contract this arc enforces: the handbook is the canonical reference for *human developers* encountering a new computer. Vocabulary is borrowed from the agent-side Genesis skill where it earns its place — substrate concepts like "scope-attached rule" and "transitive closure" carry across — but Genesis pattern codes (A1, B8, R1–R4, ATTENTION ANCHOR) are agent-side machine codes and do not appear as load-bearing handbook structure. They may surface in footnotes or sidebars marked as out-of-band.

The panel review converged on Round 1. All seven reviewers (chief editor, practitioner authority, market analyst, platform strategist, dev-lead proxy, illustrator, fact/reference checker) returned MINOR-REVISIONS. Three findings recurred across multiple reviewers and are baked into this final arc: split the load-lifecycle chapter from the attention-economy chapter; demote the cross-harness reference from teaching chapter to appendix; open every new chapter with a concrete Monday-morning failure before introducing substrate vocabulary.

If approved, implementation decomposes cleanly into five waves over an estimated seven to ten working days, with two human checkpoints. Wave A authors the two largest new chapters in parallel; Wave B restructures two existing chapters; Wave C authors the remaining new content; Wave D polishes and cross-references; Wave E ships.

## 2. Directionality contract

The handbook reader is a human developer. The Genesis reader is an agent. The two have different needs, and the v1 practitioner block tacitly inverted them — borrowing agent-side scaffolding (named patterns, design steps, rule files about rule files) into chapters meant for humans. The v2 arc reverses this: it teaches the *runtime as a computer the human is learning to program*, with patterns and disciplines introduced as solutions to problems the human will recognize, not as a catalogue inherited from the agent's design substrate.

Concretely, after finishing the v2 practitioner block, a reader should be able to:

1. **Name the four parts of the runtime machine** (model, harness, filesystem-as-loader, trigger surface) and recognize that they are independently composable. The same primitives can run under Copilot or Claude Code; the load behavior differs because the harness — not the model — is the compiler.
2. **Reason about load lifecycle and transitive closure.** When their agent misbehaves, they can ask: "what is the closure of files that loaded into context at decision time?" and reach for the substrate-level tools that answer this (`apm compile --dry-run`, the harness's verbose mode, a `plan.md` snapshot).
3. **Recognize attention as a physical property of the substrate.** Not a soft preference. They apply the disciplines (progressive disclosure, plan-write-then-reload, the bounded-scope rule for grounding) because they understand the failure mode they prevent, not because the handbook told them to.
4. **Locate the deterministic/probabilistic seam in any agentic system.** They can draw a line on a system diagram between the deterministic computer (file I/O, tool calls, the test runner, the lockfile, the gh-aw audit trail) and the probabilistic one (the model). They place consequential side effects on the deterministic side.
5. **Diagnose silent semantic failures.** They have a stack-trace equivalent: the loaded primitive set, the plan memento, the verbose tool log, the diff. They run it after every postmortem.
6. **Treat their primitives as code.** Lint, test, version, lockfile, CI. The tooling is real, not aspirational; one open-source toolchain is named.
7. **Translate a design from one harness to another.** Using substrate vocabulary, they can state a design in portable terms and adapt it to whichever harness the team standardizes on next quarter.

These seven outcomes are testable. A reviewer of the drafted v2 prose should be able to point to passages that develop each.

Genesis appears in this book as: (a) the source of borrowed vocabulary (named in footnotes when first introduced); (b) the named example of an agent-side framework that operationalizes these ideas (in the closing chapter and in one Ch10 callout); (c) never as the load-bearing structure of any chapter.

## 3. Final TOC

The v2 practitioner block:

```
Part III — For Practitioners

  Ch08  The Practitioner's Mindset                       [KEEP+sidebar+Genesis]
  Ch09  The Runtime Machine                              [NEW; ~3500 words]
  Ch10  The Instrumented Codebase                        [RESTRUCTURE]
  Ch11  The PROSE Specification                          [KEEP]
  Ch12  The Load Lifecycle                               [NEW; ~2500 words]
  Ch13  Attention and Context Economy                    [NEW; ~2500 words]
  Ch14  The Deterministic / Probabilistic Boundary       [NEW; ~3000 words]
  Ch15  Multi-Agent Orchestration                        [KEEP+ADD]
  Ch16  The Execution Meta-Process                       [KEEP]
  Ch17  Architectural Patterns: A Rosetta Stone          [NEW; ~3000 words]
  Ch18  Anti-Patterns and the Agent Stack Trace          [KEEP+EXTEND]
  Ch19  Primitives as Code                               [NEW; ~2500 words]
  Ch20  What Comes Next                                  [KEEP]

Appendix A  The Cross-Harness Reference                  [NEW; dated snapshot]
```

**Total chapters:** 13 (was 8). **New chapters:** 6. **Restructured chapters:** 2 (Ch10 instrumented codebase, current Ch11 context engineering split). **Preserved chapters:** 8 (Ch08 with Genesis insert; Ch11, Ch15-Ch16, Ch18, Ch20 light edits; the rest fully preserved). **Appendices:** 1 new.

**Estimated word-count delta:** +17,000 words across new chapters, +3,000 from appendix, -1,500 from material moved out of restructured chapters. Net: roughly +18,500 words. Current Part III is approximately 27,000 words; v2 lands at approximately 45,500 words.

## 4. Per-chapter changeset

| Chapter | Title (v2)                                       | Action       | Word-count delta | Notes                                                                               |
|---------|--------------------------------------------------|--------------|------------------|-------------------------------------------------------------------------------------|
| Ch08    | The Practitioner's Mindset                       | KEEP+sidebar+Genesis | +700     | Add a one-page sidebar previewing the four-part runtime machine and a "Your First Week" pathway. **Open the chapter with the strategic Genesis surfacing**: name `danielmeppiel/genesis` as the agent-side companion that operationalizes the entire Part III, with install instructions and a one-paragraph "what it gives you as you read." |
| Ch09    | The Runtime Machine                              | NEW          | +3500            | The substrate chapter. Opens with a concrete cross-harness failure.                |
| Ch10    | The Instrumented Codebase                        | RESTRUCTURE  | +200             | Add binding-mode column to primitives table. Move tool-support matrix to Appendix A. Re-frame primitives as substrate-typed artifacts. |
| Ch11    | The PROSE Specification                          | KEEP         | +200             | Add forward-references to Ch12 and Ch13 explaining the substrate origin of each constraint. |
| Ch12    | The Load Lifecycle                               | NEW          | +2500            | Deterministic mechanics: who loads what when, transitive closure, binding modes.    |
| Ch13    | Attention and Context Economy                    | NEW          | +2500            | Probabilistic disciplines: attention as physics, plan-write-then-reload, bounded-scope grounding. |
| Ch14    | The Deterministic / Probabilistic Boundary       | NEW          | +3000            | The seam. Two computers, one program. Opens with a concrete failure.               |
| Ch15    | Multi-Agent Orchestration                        | KEEP+ADD     | +600             | Add the threading-topology 2x2 as the chapter's spine. Surface harness-spawn variance. Note current Ch12 stays intact. |
| Ch16    | The Execution Meta-Process                       | KEEP         | +300             | Add a short subsection on plan-write-then-reload as cross-wave attention discipline. |
| Ch17    | Architectural Patterns: A Rosetta Stone          | NEW          | +3000            | The architects' chapter. Layered model of the agentic runtime; catalogue of recurring patterns mapped to GoF names where the analogy holds; per-layer pattern decisions. |
| Ch18    | Anti-Patterns and the Agent Stack Trace          | KEEP+EXTEND  | +700             | Add the agent-stack-trace checklist (one printed page) at chapter open. Add bundle-leakage and phantom-dependency entries. |
| Ch19    | Primitives as Code                               | NEW          | +2500            | DevEx for markdown-as-code. Opens with a concrete failure (silent broken primitive caught by lint). |
| Ch20    | What Comes Next                                  | KEEP         | +300             | Add forward reference to Appendix A's refresh cadence; name `danielmeppiel/genesis` again as the canonical first install for teams entering the practice. Light update for v2 numbering. |
| Appx. A | The Cross-Harness Reference                      | NEW          | +2500            | Dated snapshot. Substrate-question matrix replacing the current Ch09 tool-support table. |

## 5. New chapters in detail

### Ch09 — The Runtime Machine

**Thesis.** Every agentic system is the composition of four independently-replaceable parts: an inference model, a harness/runtime that drives it, a filesystem layout the harness consults, and one or more trigger surfaces that decide when the harness runs. A developer who cannot name these four parts cannot reason about why their setup behaves differently across vendors.

**Opening (the Monday failure).** A senior engineer ports a working APM project from Copilot to Claude Code. The same primitive files. The same model family. The skills bind in Copilot; in Claude Code they go silent. Without the runtime-machine vocabulary, this is a mystery. With it, it is one of three diagnoses (the harness's load order, the file naming convention it parses, the binding mode of the primitive) — each one falsifiable with a one-minute test.

**Sections.**

1. *The four-part machine.* One paragraph each on the model, the harness, the filesystem-as-loader, the trigger surface. A stacked-block diagram showing data flow at session start.
2. *Markdown that steers an LLM is code.* The meta-thesis. A 30-line `.instructions.md` is parsed (frontmatter), linked (referenced files), loaded (read into context), and executed (steers inference). It has all four properties of a code artifact and the failure modes that follow.
3. *The harness is the compiler.* Why `.cursor/rules/` does not exist for Codex, why `CLAUDE.md` is silent in Cursor, why Copilot's `.instructions.md` with `applyTo:` is the most expressive of the five. A concrete table comparing two harnesses on the same primitive.
4. *Inference is per-thread; the filesystem is shared.* The single most consequential structural property. Set up here so Ch12 (load lifecycle) and Ch15 (multi-agent topology) can build on it.
5. *What this chapter unlocks.* A forward map: Ch10 will teach what to build knowing the runtime is in your head; Ch12 will teach load mechanics; Ch14 will teach where the deterministic seam lives.

**Diagrams.**

- Stacked-block diagram of the four-part machine (mermaid block-beta).
- Two-column comparison: Copilot's load order vs Claude Code's load order, same project (mermaid sequence or table; illustrator review recommended sequence).

**Citations.** Genesis `runtime-affordances/common.md` for the substrate definition (footnoted as out-of-band agent-side reference). Vendor docs for each harness's load behavior, dated. Author's synthesis where the four-part decomposition is original prose.

### Ch12 — The Load Lifecycle

**Thesis.** When the agent runs, the harness loads files in a defined order, recursing through declared dependencies until the closure is built and the model sees it. This is observable, debuggable, and the key to diagnosing "why did my primitive not bind?"

**Opening (the Monday failure).** A team adds a new skill that should activate on database migrations. It does not. The skill file is correctly placed; the description matches. The verbose harness output reveals the cause: a parent instruction file is overflowing the context budget, and the on-demand skill never gets pulled because the dispatcher has already closed the load window. Without load-lifecycle vocabulary the team retypes the description for an hour. With it the diagnosis is one minute.

**Sections.**

1. *Load order is observable.* What the harness logs and how to read it. The sequence diagram showing persona-scope → scope-attached rules → on-demand modules → child threads.
2. *Binding modes.* Agent-invoked (a skill matches a description) vs substrate-invoked (a workflow file matches an event). Confusing the two is the most common cause of "my primitive does not run."
3. *The transitive-closure question.* When a primitive declares an external dependency, the loader recurses. What is the closure of files that load when *my* primitive activates? Tools to answer it: `apm compile --dry-run`, `--verbose` flags, manual trace.
4. *Inline vs local-sibling vs external module.* The three composition modes from the substrate. When to inline; when to extract; when to depend.
5. *What this chapter does NOT cover.* The probabilistic side of context — token economy, attention decay, signal-to-noise ratio — is Ch13. This chapter is purely about the deterministic mechanics.

**Diagrams.**

- Sequence diagram of load order, harness side (illustrator-recommended addition).
- A worked transitive-closure example, expanded inline.

**Citations.** Genesis `composition-substrate.md` for transitive-closure semantics; `primitives.md` for binding modes (out-of-band footnote). APM docs for the toolchain commands, dated.

### Ch13 — Attention and Context Economy

**Thesis.** Context is finite. Attention degrades non-linearly under load. Doubling input length does not halve output quality; it crosses a threshold past which the model loses the thread. This is *physics*, not preference, and the disciplines that compensate are not optional polish.

**Opening (the Monday failure).** A team's reliable code-review prompt starts producing inconsistent results. No one changed the prompt. They added a "useful" 800-line context file two weeks ago. The model's context window can fit the new content; the model's *attention* cannot. The cure is not a bigger model; it is progressive disclosure of the new content.

**Sections.**

1. *Why context is not a budget; it is a working set.* The CPU-cache analog. Past a threshold, performance does not degrade gracefully — it collapses.
2. *Plan-write-then-reload.* Long sessions drift because earlier turns push out of effective attention. Writing the plan to a file *during* the session and reloading at decision points is the cure. (One worked example from PR #394.)
3. *The bounded-scope rule for external grounding.* When the agent reaches outside its corpus (web fetch, repo read, MCP tool call), the design must specify what the external source is *authoritative for*. Authority overreach is a high-severity silent failure.
4. *Signal-to-noise as a design metric.* How to measure what counts as signal vs noise per task type. Concrete heuristics.
5. *The PROSE constraints, revisited.* P (Progressive Disclosure), R (Reduced Scope), O (Orchestrated Composition) all derive from this chapter's physics. Forward-reference Ch11's normative spec.

**Diagrams.**

- A working-set vs context-length curve (table or simple chart).
- A plan-memento timeline showing decay and reload points.

**Citations.** Anthropic and OpenAI papers on attention/context length where applicable (fact-checker: vendor and academic). Author's synthesis where the working-set framing is original.

### Ch14 — The Deterministic / Probabilistic Boundary

**Thesis.** Every agentic system is the composition of two computers — a deterministic one (the harness, file I/O, tool calls, the test runner, the lockfile, the gh-aw audit trail) and a probabilistic one (the model). The single most important architectural decision in any agentic design is *where the seam between them sits and what crosses it*.

**Opening (the Monday failure).** A team ships an agent that creates GitHub issues from incoming bug reports. It works for two weeks. Then it fabricates a customer name and creates an issue tagged with the wrong account. The model hallucinated; the system carried the hallucination through to a side effect because there was no deterministic gate between the model's output and the GitHub API call. The cure is to redraw the seam: the model proposes the issue body; a deterministic schema-checked transformer (the gh-aw `safe-outputs` block, or its equivalent) executes the API call against a controlled allowlist.

**Sections.**

1. *Two computers, one program.* The seam table (deterministic side | probabilistic side | what crosses each direction).
2. *Consequential side effects belong on the deterministic side.* The model proposes; the gate disposes. Worked example: a gh-aw workflow as one realization of supervised execution. (Per platform-strategist finding D: gh-aw is *one realization*, not *the canonical* form. Other realizations are sketched: a CI lambda, a Buildkite job-level secret, an Argo workflow.)
3. *Hallucination as a system property.* Pretraining is frozen; the model fabricates plausibly when asked about thin regions. The cure is grounding (Ch13's bounded-scope rule) plus verification (the gates below), not "use a better model."
4. *The four kinds of quality gate.* The closed 2x2: programmatic-internal (test/lint), judgement-internal (goal-steward review), programmatic-external (cold-reader-with-rubric), judgement-external (human checkpoint). Picking the wrong cell for the failure mode is a design mistake.
5. *Strong-form supervised execution.* What it takes to ship agent-driven side effects to production: the agent never holds the write token; the substrate does. This unblocks compliance review for agent-driven PRs.

**Diagrams.**

- The seam table (per illustrator: a table, not a flowchart).
- The 2x2 of gate types with one named example per cell (table).

**Citations.** Genesis A9 SUPERVISED EXECUTION and `pattern-tradeoffs.md` gate-types section as out-of-band agent-side references. GitHub Actions docs for `safe-outputs:` semantics, dated. Author's synthesis where the two-computers framing is original prose.

### Ch18 — Primitives as Code

**Thesis.** If markdown that steers an LLM is code (Ch09), then the discipline of shipping it must look like the discipline of shipping any other code: lint, test, version, distribute, audit. This chapter operationalizes the meta-thesis.

**Opening (the Monday failure).** A team merges a PR that updates a skill file. The PR diff looks fine; the skill renders correctly in the file viewer. The next day, agent quality on that skill's domain drops by half. Cause: the PR introduced a markdown link to a moved file; the broken link was invisible in review because no one ran a primitive linter. The handbook's previous chapters described primitives as files. This chapter treats them as code, with all the tooling that implies.

**Sections.**

1. *The five-command discipline.* Lint, test, lockfile-resolve, package, audit. One CLI invocation each. (Per chief editor F3 and market analyst F1: this is the entry-point operational proof of the meta-thesis.)
2. *Lint-test-CI for primitives.* Frontmatter schema validation, link integrity, scope coverage, activation tests (does this skill activate on its trigger description?). What goes in `.github/workflows/`.
3. *Lockfile semantics for context.* When primitives reference external modules, the resolved dep tree must be pinned. Otherwise next week's `apm install` produces different agent behavior with no code change visible. The same problem npm faced; the same cure.
4. *Bundle leakage and phantom dependency.* The dual failures from the substrate. Phantom: a primitive references context that is not declared. Leakage: a primitive ships maintainer-only files that the consumer's loader picks up. Worked example from APM publish-time rules.
5. *Refactor patterns for primitives.* Split, fuse, extract, inline. When to use which. (Genesis R1–R4 vocabulary, footnoted as agent-side; the chapter's prose uses Fowler's classical refactoring catalogue as the load-bearing analog.)
6. *The architect stays portable; the coder reaches for vendor syntax.* The discipline that closes the chapter: design conversations use substrate vocabulary; vendor-specific syntax appears only in onboarding sections of a primitive. This is the rule that makes Ch09's portability claim operational.

**Diagrams.**

- The publish-vs-load distinction: ship-time scope (what the publisher emits) vs run-time scope (what the consumer's harness loads). The bundle-leakage anti-pattern.
- A primitive lifecycle: author → lint → test → publish → resolve → load → execute → audit, with the deterministic/probabilistic boundary marked (per illustrator addition).

**Citations.** APM docs for the toolchain. Genesis `composition-substrate.md` and `module-system-adapters/apm.md` (out-of-band). Fowler refactoring catalogue (academic).

### Appendix A — The Cross-Harness Reference

**Thesis.** The substrate question is not "does Cursor support skills?" — it is "in which harness, at which load-lifecycle point, attached to which scope, does this primitive type bind?" The answer is data, not opinion, and the data is concrete and citable. This appendix is the dated snapshot.

**Maintenance model.** Snapshot date: at publication. Refresh cadence: annually, or on major harness release. Each row carries a *verified-on* date. Ch10, Ch12, and Ch14 forward-reference Appendix A explicitly; readers know to check the date.

**Sections.**

1. *The substrate-question matrix.* Five harnesses (Copilot, Claude Code, Cursor, Codex, OpenCode) by six substrate properties (persona scoping, scope-attached rules, on-demand modules, programmatic spawn, plan persistence, tool-call affordance). One cell per intersection, with citation.
2. *Trigger surface vs inference harness.* The orthogonality grid. gh-aw is a trigger surface that pairs with any inference harness; Claude Code is an inference harness with built-in triggers; Copilot can be either. Example cells: gh-aw + Claude Code, Copilot trigger + Copilot inference, Argo Workflow + OpenAI inference.
3. *Tool-call affordance per harness.* MCP support, deterministic tool list, sandbox properties.
4. *Child-thread spawn semantics.* Programmatic spawn vs cooperative-only. The harnesses that have it; the harnesses that do not.
5. *Plan persistence.* How each harness implements (or fails to implement) durable plans across sessions.

**Format.** Tables. Not flowcharts. Per illustrator review.

**Citations.** Vendor documentation for each cell, dated. Genesis `runtime-affordances/per-harness/*.md` as out-of-band cross-references.

## 6. Concept-source traceability

Every new section traces back to one of three source families:

- **Genesis source files.** `primitives.md`, `composition-substrate.md`, `architectural-patterns.md`, `design-patterns.md`, `refactor-patterns.md`, `pattern-tradeoffs.md`, `runtime-affordances/common.md`, `runtime-affordances/portability-rules.md`, the five per-harness adapters, and `runtime-affordances/per-trigger-surface/gh-aw.md`. Borrowed concepts are footnoted on first use as agent-side references and never relied upon as load-bearing structure.
- **Existing handbook material.** The annotated Copilot session in current Ch09, the PR #394 case study in current Ch13, the seven-primitives catalogue, the PROSE constraints, the wave protocol, the anti-patterns taxonomy. All preserved; cross-referenced explicitly.
- **External sources.** Vendor documentation (Copilot, Claude Code, Cursor, Codex, OpenCode, gh-aw, GitHub Actions), dated; academic literature where applicable (cognitive load theory in Ch08; attention/context length papers in Ch13); industry references (Fowler refactoring catalogue in Ch18; Flyvbjerg case-study methodology in Ch08).

The fact-checker's audit (round 1) flagged seven categories of claims requiring verification before final draft: vendor session-state behavior (Copilot SQLite), spawn-capability claims (Cursor, Codex), gh-aw safe-outputs (GitHub Actions docs), attention-as-physics (academic citation needed), the 2x2 of quality gates (author's synthesis label needed), threading-topology 2x2 (classical concurrency citation), PR #394 numbers (consistency audit). Each is a drafting requirement, not an arc-level question.

## 7. Open questions and explicit non-decisions

These items were surfaced in panel review but deliberately not resolved at the arc level; the chief editor and authors will decide during drafting:

1. **Chapter-title polish.** "Runtime Machine," "Load Lifecycle," "Deterministic / Probabilistic Boundary" are all working titles. The words "runtime," "lifecycle," and "boundary" are overloaded in software. Final titles will be set during drafting after the prose voice settles.
2. **The "Your First Week" sidebar in Ch08.** Dev-lead F5 recommends an explicit one-week onboarding pathway in Ch08. The arc says yes; the exact day-by-day mapping is a drafting decision.
3. **Where the case-study material in current Ch09 (the annotated Copilot session) lives in v2.** Stay in Ch10 as the worked example, or move to Ch16 (execution meta-process) alongside PR #394, or promote to Part IV. Recommendation: stay in Ch10. Final call to chief editor.
4. **Splitting Part III into IIIa and IIIb.** A 12-chapter Part III is large. A divider after Ch14 (the seam chapter) is defensible. Decision deferred to chief editor after first full draft.
5. **The Ch08 sidebar previewing the four-part machine.** Recommended by chief editor; depth and length deferred to drafting.
6. **Whether Genesis is named as one realization in Ch19 (What Comes Next).** A short paragraph naming Genesis (and Squad, and Spec-Kit, and Claude plugins) as agent-side frameworks that operationalize the disciplines this book teaches. Recommendation: yes, but only in Ch19. Final wording deferred.

## 8. Panel verdicts (consolidated)

| Reviewer              | Round 1 Verdict   | High findings (resolved in this final arc?)               |
|-----------------------|-------------------|-----------------------------------------------------------|
| chief-editor          | MINOR-REVISIONS   | Split Ch12 — RESOLVED (Ch12 + Ch13 split)                |
| practitioner-authority| MINOR-REVISIONS   | Demote Ch18 to appendix — RESOLVED; concrete failures opening — RESOLVED |
| market-analyst        | MINOR-REVISIONS   | Prove markdown-as-code with tooling — RESOLVED in Ch18.1 |
| platform-strategist   | MINOR-REVISIONS   | gh-aw as one realization, not canonical — RESOLVED in Ch14.2 |
| dev-lead-proxy        | MINOR-REVISIONS   | Ch14 runnable example — RESOLVED in Ch14 opening; agent stack trace as checklist — RESOLVED in Ch17 |
| illustrator           | MINOR-REVISIONS   | Tables not flowcharts — RESOLVED in Ch14 + Appx A; missing sequence diagram — RESOLVED in Ch12 |
| fact-ref-checker      | MINOR-REVISIONS   | Vendor and academic citations — DEFERRED to drafting (per section 6) |

**Convergence.** 7/7 reviewers minor revisions. Zero contradictions on load-bearing elements. Threshold (>= 6/7 + zero contradictions) cleared on Round 1. No Round 2 was run.

## 9. Implementation decomposition

**Tooling contract (role separation).** Authoring and review are distinct skills; do not collapse them.

| Activity                          | Skill                                                          | Notes                                                                                                  |
|-----------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Chapter authoring (prose generation) | `editorial-pipeline` (`.github/skills/editorial-pipeline/`) | 6-agent pipeline (Chief Editor, Thought Leadership, Practitioner Authority, Publishing Advisor, Copywriter, Fact-Ref Checker). Three hard rules: brief-is-binding, panel-before-draft, source-fidelity. Two human gates: outline approval, ship. Each new chapter and each restructured chapter goes through one full pipeline run. |
| Surgical edits (cross-refs, lint, polish, footnote demotion) | direct edit                                          | No prose generation needed; bypass `editorial-pipeline`.                                               |
| Review gate at end of Wave B and Wave D | `handbook-panel` (`.github/skills/handbook-panel/`)         | 11-agent review panel (chief-editor synthesizes). No content authored here — it produces verdicts only. Convergence criterion: 6 of 7 reviewers APPROVE or MINOR-REVISIONS, no two reviewers contradict on a load-bearing element. |

If approved, drafting decomposes into five waves over an estimated seven to ten working days:

- **Wave A (parallel, 2 `editorial-pipeline` runs, 2-3 days).** Author Ch09 (Runtime Machine) and Ch14 (Deterministic / Probabilistic Boundary). The two largest new chapters; they share a diagram (the seam) and benefit from being co-authored. Each pipeline run loads the full Genesis substrate vocabulary and the existing handbook chapters they extend. Both pipelines emit chapter outlines first; Chief Editor approves both outlines before either pipeline drafts prose.
- **Wave B (parallel, 2 `editorial-pipeline` runs, 1-2 days).** Restructure Ch10 (Instrumented Codebase) — add binding-mode column, move tool-support matrix to appendix — and split current Ch11 into Ch12 (Load Lifecycle) and Ch13 (Attention and Context Economy). Restructure work uses `editorial-pipeline` because new prose is generated; pure cross-ref renumbering does not. Both pipelines pull forward concepts established in Wave A.
- **Wave C (parallel, 2 `editorial-pipeline` runs, 1-2 days).** Author Ch18 (Primitives as Code) and Appendix A (Cross-Harness Reference). Both reference forward into earlier chapters and benefit from being last.
- **Wave D (sequential, direct edit, 1-2 days).** Polish Ch08, Ch11, Ch15, Ch16, Ch17, Ch19. Add cross-references. Verify TOC and footnotes. Run primitive lint on the handbook itself (where applicable). Apply the fact-checker's verification list (section 6 of this arc). No `editorial-pipeline` invocation here — the work is mechanical.
- **Wave E (sequential, 1 reviewer + chief editor, 1 day).** Final read-through. Back-cover and abstract update. Verify the seven outcome competencies (section 2 of this arc) are testable against the new prose. Sign-off.

**Human checkpoints (gated by `handbook-panel` review).**

1. **End of Wave B — first review gate.** Run `handbook-panel` against the contiguous Ch08–Ch15 v2 draft. The panel verifies directionality inversion holds (handbook canonical, Genesis cited as one implementation), no Genesis ALL-CAPS pattern codes are load-bearing, and the five new chapters integrate with preserved originals. Maintainer reads the synthesis verdict and decides fix-then-continue or rework.
2. **End of Wave D — second review gate.** Run `handbook-panel` against the full Part III plus Appendix A. Verdict gates publication-ready approval. Fix-then-ship or final round.

**Estimated total effort.** Ten agent-days plus three human-day checkpoints. Calendar time: seven to ten working days assuming parallel waves run end-to-end without delay.

**Risks and mitigations.**

- **Risk:** The five new chapters drift in voice. **Mitigation:** Wave A authors a style-and-voice exemplar (Ch09 first 1500 words) before Wave B starts; subsequent waves match.
- **Risk:** Cross-references fall out of sync as chapters renumber. **Mitigation:** Ch10–Ch19 use Quarto's symbolic cross-reference syntax (e.g., `@sec-runtime-machine`) instead of literal numbers; Wave D performs a final pass.
- **Risk:** Appendix A dates faster than the rest of the book. **Mitigation:** Per chief editor F2, the appendix carries an explicit snapshot date and refresh cadence; Ch10/Ch12/Ch14 forward-references say "as of <date>."
- **Risk:** Genesis vocabulary leaks into load-bearing prose. **Mitigation:** Wave D includes a grep pass for ALL-CAPS pattern codes in the new chapters; any occurrence requires either footnote demotion or removal.

---

**End of final arc proposal.** Awaiting maintainer sign-off to begin Wave A.
