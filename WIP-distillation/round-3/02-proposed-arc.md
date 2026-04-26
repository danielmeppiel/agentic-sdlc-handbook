# Proposed Arc — Practitioner Block v2 (Ch08–Ch15)

**Status:** Pre-panel draft. To be reviewed by the seven-agent panel and revised across up to three rounds.

**Author voice:** doc-writer. The arc is written as the *handbook's* internal restructuring memo — what we keep, what we restructure, what we add, what we cut — argued from the directionality contract.

---

## 1. Directionality contract (the load-bearing inversion)

The handbook is a reference book for *human developers* who are encountering a new kind of computer: the LLM-plus-harness-plus-filesystem substrate. The reader's job, after finishing the practitioner block, is to be able to:

1. Name the four parts of the runtime machine (model, harness, filesystem-as-loader, trigger surface) and know that they are independently composable.
2. Reason about how their primitives load, in what order, and what closure of files reaches the model at decision time.
3. Recognize attention as a physical property of the runtime, not a soft preference, and apply the disciplines that compensate for it.
4. Locate the deterministic / probabilistic seam in any agentic system they design and place consequential side effects on the deterministic side.
5. Diagnose silent semantic failures using the agent-equivalent of a stack trace.
6. Treat their primitives as code: lint, test, version, and ship them through CI like any other code class.
7. Translate a design from one harness to another using a substrate vocabulary.

These seven competencies are the *outcomes* the v2 arc must produce.

Genesis is one operational implementation that an agent loads. We borrow vocabulary from it where the vocabulary is durable and useful. We do not borrow its pattern codes (A1, B8, R1–R4, ATTENTION ANCHOR) as load-bearing handbook structure. The reader of this book is a human; the reader of Genesis is an agent.

## 2. Per-chapter changeset table

| Chapter | Current form (1-line)                                       | Verdict      | Action                                                                                                                                                                          |
|---------|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ch08    | The practitioner's mindset (autocomplete trap, three roles) | KEEP+POLISH  | Tighten the three-roles section; add a one-page sidebar on the four-part runtime machine to anchor everything that follows.                                                     |
| Ch08.5  | (new) **The Runtime Machine**                               | NEW          | Insert as Ch09 in the new numbering. The substrate chapter the block currently lacks. ~3500 words. See section 4.                                                               |
| Ch09    | The instrumented codebase (seven primitives)                | RESTRUCTURE  | Renumber to Ch10. Re-frame: primitives are *binding-mode-typed* artifacts in the substrate. Add binding-mode column to the master table. Move tool-support matrix to new Ch15.  |
| Ch10    | The PROSE specification                                     | KEEP         | Renumber to Ch11. No structural change. Add a short forward-reference to the runtime-machine chapter explaining why each constraint exists.                                     |
| Ch11    | Context engineering                                         | RESTRUCTURE  | Renumber to Ch12. Add the load-lifecycle and transitive-closure sections (currently absent). Re-cast "context budget" in attention-as-physics terms.                            |
| Ch11.5  | (new) **The Deterministic / Probabilistic Boundary**        | NEW          | Insert as Ch13. ~3000 words. Two computers, one program. Where the gate sits. Strong-form supervised execution. See section 4.                                                  |
| Ch12    | Multi-agent orchestration                                   | KEEP+ADD     | Renumber to Ch14. Add the threading-topology 2x2 as the chapter's spine. Surface harness-spawn-capability variance.                                                             |
| Ch13    | The execution meta-process (waves, PR #394 case)            | KEEP         | Renumber to Ch15. The case-study material is gold and stays. Add a short subsection on plan-write-then-reload as the cross-wave attention discipline.                           |
| Ch14    | Anti-patterns and failure modes                             | KEEP+EXTEND  | Renumber to Ch16. Add the failure-model-and-debugging unifying protocol (the "agent stack trace") as the chapter's opening framework. Add bundle-leakage and phantom-dep entries. |
| Ch14.5  | (new) **Primitives as Code: Lint, Test, Ship**              | NEW          | Insert as Ch17. ~2500 words. DevEx for markdown-as-code, lockfile semantics, distribution-surface hygiene. See section 4.                                                       |
| Ch14.7  | (new) **The Cross-Harness Reference**                       | NEW (annex) | Insert as Ch18 (closing reference). ~2500 words. The substrate-question matrix: who loads what at which scope at which lifecycle point. See section 4.                          |
| Ch15    | What comes next                                             | KEEP         | Renumber to Ch19. No change.                                                                                                                                                    |

**Net:** 8 existing chapters preserved (some renumbered), 4 new chapters inserted, 1 reference annex added. Total practitioner block grows from 8 chapters (~3,500 lines) to 13 chapters (~5,800 lines estimated).

## 3. Final TOC (proposed)

```
Part III — For Practitioners
  Ch08  The Practitioner's Mindset                  [KEEP]
  Ch09  The Runtime Machine                          [NEW]
  Ch10  The Instrumented Codebase                   [RESTRUCTURE]
  Ch11  The PROSE Specification                     [KEEP]
  Ch12  Context Engineering and Load Lifecycle      [RESTRUCTURE]
  Ch13  The Deterministic / Probabilistic Boundary  [NEW]
  Ch14  Multi-Agent Orchestration                   [KEEP+ADD]
  Ch15  The Execution Meta-Process                  [KEEP]
  Ch16  Anti-Patterns and the Agent Stack Trace     [KEEP+EXTEND]
  Ch17  Primitives as Code                          [NEW]
  Ch18  The Cross-Harness Reference                 [NEW annex]
  Ch19  What Comes Next                             [KEEP]
```

## 4. New chapters in detail

### Ch09 — The Runtime Machine (new, ~3500 words)

**Thesis.** Every agentic system is the composition of four independently-replaceable parts: an inference model, a harness/runtime that drives it, a filesystem layout the harness consults, and one or more trigger surfaces. A developer who cannot name these four parts cannot reason about their setup.

**Key concepts taught.**

- The four-part machine (concept #1). One paragraph each on model, harness, filesystem-as-loader, trigger surface — illustrated against a single concrete example (an APM project running under Copilot vs the same project running under Claude Code).
- Markdown-that-steers-an-LLM is code (concept #2). The meta-thesis. Argued via a worked example: a 30-line `.instructions.md` file is parsed, linked, loaded, and executed in a way that has all four properties of a code artifact (parser, linker, runtime, failure modes).
- The harness is the compiler (concept #3). The variance across harnesses (Copilot, Claude Code, Cursor, Codex, OpenCode) is not a feature comparison — it is the substrate choice that determines what loads.
- Inference is per-thread; the filesystem is shared (concept #4). The single most consequential structural property. Set up here so that Ch12's load lifecycle and Ch14's multi-agent topology can build on it without re-explaining.

**Diagram inventory.**

- A stacked-block diagram of the four-part machine, with arrows showing the data flow at session start (user request → harness → file load → context assembly → model → tool calls → trigger surface → side effect).
- A two-column comparison: Copilot's load order vs Claude Code's load order on the same repo, highlighting the differences.

**Anchors forward.** Ch10 will list primitives knowing the reader has the runtime machine in their head. Ch11 will state the PROSE constraints knowing the reader understands attention as a physical property of the substrate. Ch13 will draw the deterministic / probabilistic seam onto the four-part diagram.

### Ch13 — The Deterministic / Probabilistic Boundary (new, ~3000 words)

**Thesis.** An agentic system is the composition of two computers — a deterministic one (the harness, file I/O, tool calls, the test runner, gh-aw lockfile) and a probabilistic one (the model). The most important architectural decision in any agentic design is where the seam between them sits and what crosses it.

**Key concepts taught.**

- Two computers, one program (concept #11). The seam diagram. What goes on each side.
- Consequential side effects belong to the deterministic side (concept #12). The model proposes; the gate disposes. Worked example: a gh-aw workflow with `safe-outputs:` translating model intent into bounded, auditable mutations.
- Hallucination as a system property (concept #13). The cure is grounding plus verification, not "use a better model."
- The four kinds of quality gate (concept #16). The closed 2x2 (programmatic vs judgement) x (internal vs external).
- The bounded-scope rule for external grounding (concept #10). Whenever you reach outside the corpus, declare what the source is authoritative for.

**Diagram inventory.**

- The seam diagram (deterministic computer | probabilistic computer | what crosses each direction).
- The 2x2 of gate types with one named example per cell (test/lint, goal-steward review, cold-reader-with-rubric, human checkpoint).

**Anchors back.** Pulls from Ch10's safety-boundaries paragraph and elevates it into a chapter-length treatment. Pulls from Ch14's hallucinated-edits anti-pattern and re-presents it as a system property with structural cures.

### Ch17 — Primitives as Code (new, ~2500 words)

**Thesis.** If markdown that steers an LLM is code, then the discipline of shipping it must look like the discipline of shipping any other code: lint, test, version, distribute, audit.

**Key concepts taught.**

- The transitive-closure question (concept #7). What is the closure of files that loads when this primitive activates? Tools to answer it (`apm compile --dry-run`, harness verbose mode).
- Lint-test-CI for primitives (concept #19). Frontmatter schema, link integrity, scope coverage, activation tests.
- Lockfile semantics for context (concept #20). Why pinning matters; how it differs from code lockfiles (the "code" is prose, the resolution is description-match).
- Bundle leakage and phantom dependency (concept #22). The dual failures. Worked example from the APM publish-time rules.
- Refactor patterns for primitives (concept #27). Split, fuse, extract, inline — when to use which.
- The architect stays portable; the coder reaches for vendor syntax (concept #23). The chapter ends by establishing the discipline: design conversations use substrate vocabulary; vendor-specific syntax appears only in onboarding sections of a primitive.

**Diagram inventory.**

- The publish-vs-load distinction: ship-time scope (what the publisher emits) vs run-time scope (what the consumer's harness loads). The bundle-leakage anti-pattern.
- A primitive lifecycle: author → lint → test → publish → resolve → load → execute → audit.

### Ch18 — The Cross-Harness Reference (new annex, ~2500 words)

**Thesis.** The substrate question is not "does Cursor support skills?" — it is "in which harness, at which load-lifecycle point, attached to which scope, does this primitive type bind?" The answer is data, not opinion, and the data is concrete and citable.

**Key concepts taught.**

- The matrix is data, not opinion (concept #21). The chapter is a structured reference, organized by primitive type, with one row per harness.
- Trigger surface vs inference harness orthogonality (concept #24). The two-axis grid. gh-aw is a trigger surface that pairs with any inference harness; Claude Code is an inference harness with built-in triggers; Copilot can be either.
- Tool-call affordance as runtime property (concept #25). MCP and tool calls are not primitives; they are runtime properties that the harness exposes.
- Child-thread spawn semantics differ across harnesses (concept #18). Some harnesses have programmatic spawn; some do not. Multi-agent topology choice depends on this.
- Plan persistence is durable; conversation memory is not (concept #17). How each harness implements (or fails to implement) plan persistence.

**Diagram inventory.**

- The 5x6 substrate-question matrix (5 harnesses x 6 substrate concepts: persona scope, scope-attached rule, on-demand module, programmatic spawn, plan persistence, tool-call affordance).
- The trigger-surface vs inference-harness axes, with example cells (gh-aw + Claude Code, Copilot trigger + Copilot inference, etc.).

**Anchors back.** Replaces Ch10's mid-2025 tool-support table (which was a feature comparison) with a substrate-property reference (which is a load-determining property reference).

## 5. Concept-source traceability

Every new and restructured section traces its concepts back to:

- Genesis files: `primitives.md`, `composition-substrate.md`, `architectural-patterns.md`, `design-patterns.md`, `refactor-patterns.md`, `pattern-tradeoffs.md`, `runtime-affordances/common.md`, `runtime-affordances/portability-rules.md`, the five per-harness adapters, and `runtime-affordances/per-trigger-surface/gh-aw.md`.
- Existing handbook coverage: forward and back references are explicit, not borrowed implicitly.
- Field evidence: PR #394 case study, the annotated Copilot session in current Ch09, vendor docs.

Where Genesis vocabulary is borrowed (e.g., "scope-attached rule," "module entrypoint," "transitive closure"), the term is given a plain-English gloss on first use and never relies on the reader having read Genesis. Where Genesis pattern codes are referenced as historical or operational artifacts (e.g., a sidebar noting "this discipline is what an agent-side framework like Genesis calls the ATTENTION ANCHOR pattern"), the code is footnoted as out-of-band, not used as load-bearing structure.

## 6. Open questions for the panel

1. **Should Ch18 be a chapter or an appendix?** The cross-harness reference is reference material. It might fit better as an appendix that the rest of the book points to, freeing Part III to be teaching prose.
2. **Is the Ch13 split clean?** The deterministic/probabilistic chapter pulls material from current Ch10 (Safety Boundaries), Ch12 (orchestration), and Ch14 (hallucinated edits). The risk is fragmentation; the benefit is a single load-bearing chapter that names the seam.
3. **How do we name Ch09 without using "runtime"?** The word is overloaded in software (runtime library, runtime environment, ML runtime). Alternatives: "The Substrate," "The Agent Computer," "The Four-Part Machine."
4. **Where does the case-study material in current Ch09 (the annotated Copilot session) live in v2?** Options: stay in Ch10 (the new Instrumented Codebase chapter) as the worked example; move to Ch15 (Execution Meta-Process) alongside PR #394; promote to Part IV alongside the existing case studies.
5. **Do we ship one block in v2, or split it?** The 13-chapter Part III is large. We could split into IIIa (substrate + primitives + PROSE) and IIIb (orchestration + execution + ops), with a part divider.
6. **What about the existing footnotes and bibliography?** Sweller, Flyvbjerg, etc. carry over; new chapters need new citations (especially Ch13's deterministic/probabilistic framing — there is good academic prior art).

## 7. Implementation decomposition (out-of-scope teaser)

If this arc is approved, the implementation work splits cleanly:

- **Wave A** (parallel, 2 agents): write Ch09 (Runtime Machine) and Ch13 (Deterministic/Probabilistic Boundary). These are the two largest new chapters, share a diagram (the seam), and benefit from being co-authored.
- **Wave B** (parallel, 2 agents): restructure Ch10 (Instrumented Codebase) and Ch12 (Context Engineering). Both touch existing prose; both pull binding-mode and load-lifecycle concepts forward.
- **Wave C** (parallel, 2 agents): write Ch17 (Primitives as Code) and Ch18 (Cross-Harness Reference). These are the most new-content-dense; they can ship after Wave A/B because they reference forward into them.
- **Wave D** (sequential, 1 agent): polish Ch08, Ch11, Ch14, Ch15, Ch16; add cross-references; verify TOC and footnotes; run the full handbook lint.
- **Wave E** (sequential, 1 agent + chief editor): final read-through; back-cover and abstract update; ensure the seven outcome competencies named in the directionality contract are testable against the new prose.

Total estimated effort: 5 waves over 7–10 working days, with two human checkpoints (end of Wave B for arc validation, end of Wave D for final approval).

---

**End of proposed arc.** Ready for panel review.
