# Affinity Matrix: Genesis Skill Corpus × Agentic SDLC Handbook (Ch08–Ch15)

Scope: maps every Genesis asset (skills/genesis/**) to the eight Part-III handbook chapters. Cells are graded DIRECT / RELATED / MARGINAL / NONE. Conflicts are listed verbatim with file:line. Persona reading lists are at the end.

Repos:
- Genesis: `/Users/danielmeppiel/Repos/genesis-skill/skills/genesis/`
- Handbook: `/Users/danielmeppiel/Repos/apm-handbook/handbook/`

Cell grades:
- **DIRECT** — same concept, both texts make load-bearing claims about it; one can be read as a normative gloss on the other.
- **RELATED** — adjacent topic; one text touches it, the other develops it in detail; useful cross-reference but not the same claim.
- **MARGINAL** — passing mention only; useful for a sidebar or footnote.
- **NONE** — no meaningful overlap.

---

## 1. Asset × Chapter Affinity

Chapters: 08 Practitioner's Mindset · 09 Instrumented Codebase · 10 PROSE Specification · 11 Context Engineering · 12 Multi-Agent Orchestration · 13 Execution Meta-Process · 14 Anti-Patterns · 15 What Comes Next.

| Genesis asset | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| `SKILL.md` (8-step design process) | RELATED [^1] | DIRECT [^2] | DIRECT [^3] | DIRECT [^4] | RELATED [^5] | DIRECT [^6] | RELATED [^7] | MARGINAL |
| `agents/genesis-architect.agent.md` | DIRECT [^8] | DIRECT [^9] | RELATED [^10] | RELATED [^11] | RELATED [^12] | RELATED [^13] | DIRECT [^14] | MARGINAL |
| `assets/primitives.md` (TIER 0) | MARGINAL | DIRECT [^15] **CANONICAL CONFLICT** | DIRECT [^16] | DIRECT [^17] | RELATED [^18] | RELATED [^19] | RELATED [^20] | RELATED [^21] |
| `assets/composition-substrate.md` | NONE | DIRECT [^22] | RELATED [^23] | RELATED [^24] | MARGINAL | NONE | DIRECT [^25] | MARGINAL |
| `assets/architectural-patterns.md` (Tier-3 A1–A10) | RELATED [^26] | RELATED [^27] | RELATED [^28] | RELATED [^29] | DIRECT [^30] | DIRECT [^31] | DIRECT [^32] | RELATED [^33] |
| `assets/design-patterns.md` (Tier-2 C/S/B) | MARGINAL | RELATED [^34] | DIRECT [^35] | DIRECT [^36] | DIRECT [^37] | RELATED [^38] | DIRECT [^39] | NONE |
| `assets/refactor-patterns.md` (R1–R4) | NONE | DIRECT [^40] | RELATED [^41] | RELATED [^42] | MARGINAL | MARGINAL | DIRECT [^43] | NONE |
| `assets/pattern-tradeoffs.md` (matrices) | RELATED [^44] | RELATED [^45] | DIRECT [^46] | RELATED [^47] | DIRECT [^48] | DIRECT [^49] | DIRECT [^50] | NONE |
| `assets/mermaid-conventions.md` | NONE | RELATED [^51] | NONE | RELATED [^52] | DIRECT [^53] | DIRECT [^54] | MARGINAL | NONE |
| `assets/runtime-affordances/common.md` (+ portability-rules) | NONE | DIRECT [^55] | RELATED [^56] | DIRECT [^57] | RELATED [^58] | NONE | RELATED [^59] | RELATED [^60] |
| `assets/runtime-affordances/per-harness/*` | NONE | DIRECT [^61] | NONE | RELATED [^62] | NONE | NONE | NONE | RELATED [^63] |
| `assets/runtime-affordances/per-trigger-surface/gh-aw.md` | NONE | RELATED [^64] | DIRECT [^65] | NONE | RELATED [^66] | RELATED [^67] | DIRECT [^68] | RELATED [^69] |
| `assets/module-system-adapters/apm.md` | NONE | DIRECT [^70] | MARGINAL | RELATED [^71] | NONE | NONE | RELATED [^72] | RELATED [^73] |
| `examples/01-readme-iteration.md` | RELATED [^74] | NONE | RELATED [^75] | NONE | DIRECT [^76] | DIRECT [^77] | DIRECT [^78] | NONE |
| `examples/02-review-panel-architecture.md` | RELATED [^74] | NONE | RELATED [^75] | NONE | DIRECT [^76] | DIRECT [^77] | DIRECT [^78] | NONE |
| `examples/03-release-notes-single-skill.md` | RELATED [^79] | RELATED [^79] | RELATED [^79] | NONE | MARGINAL | MARGINAL | MARGINAL | NONE |
| `examples/04-pr-review-advisory.md` + `05-pr-review-verdict.md` | RELATED [^80] | RELATED [^80] | DIRECT [^80] | NONE | DIRECT [^80] | RELATED [^80] | DIRECT [^80] | RELATED [^80] |

### Footnotes

[^1]: SKILL.md frames the architect persona's "non-negotiable design discipline" — same posture as Ch08 §"Your Three Roles" (Architect / Reviewer / Escalation Handler) at `ch08-the-practitioners-mindset.qmd:55`.
[^2]: SKILL.md step 2 ("component diagram") and step 3.5 ("composition substrate") output the same artifact category Ch09 calls primitives — `ch09-the-instrumented-codebase.qmd:23 ## The Seven Primitive Types`. Direct mapping but rival taxonomy (see conflict §C1).
[^3]: SKILL.md asset table maps every primitive to a PROSE axis: `assets/primitives.md:230-239`. Ch10 owns the PROSE chapter; this is a downstream gloss.
[^4]: SKILL.md mandates PROGRESSIVE DISCLOSURE / LAZY ASSET loading at every step — same constraint Ch11 develops as the Five-Layer Hierarchy (`ch11-context-engineering.qmd:52 ## The Instruction Hierarchy`).
[^5]: SKILL.md step 3 (sequence diagram of thread spawn / fan-in) is the canonical Tier-3 pattern selection step where multi-agent topology lands. Ch12 covers Writer/Reviewer/Tester and Domain Teams (`ch12-multi-agent-orchestration.qmd:45 ## Agent Specialization Patterns`).
[^6]: SKILL.md is itself an 8-step meta-process; Ch13 owns the 5-phase AUDIT→PLAN→WAVE→VALIDATE→SHIP meta-process (`ch13-the-execution-meta-process.qmd:13 ## The Five Phases`). Both are normative meta-processes; cite each other.
[^7]: SKILL.md step 7's portability declaration (`per-harness reach is justified` ↔ NOT) generates the kind of "tool-coupling-as-anti-pattern" check Ch14 catalogues.
[^8]: `genesis-architect.agent.md:285 ## Classic architecture principles you apply` and `:300 ## The non-negotiable design discipline` are the same Architect-role posture Ch08 §"Your Three Roles" defines.
[^9]: `genesis-architect.agent.md:198 ## Disambiguation you enforce in every review` and `:213` ("agentskills.io ... narrowest scope ... MODULE ENTRYPOINT vs PERSONA, RULE, CHILD-THREAD SPAWN, ORCHESTRATOR, ASSET") is the architect's binding to the 6-primitive taxonomy — collides with Ch09's 7-type list (see §C1).
[^10]: Architect agent says (line 354) "Four tiers of pattern thinking" — same disciplined-constraint stance as PROSE; PROSE itself is not the architect's vocabulary.
[^11]: `genesis-architect.agent.md:236 ## Skill dispatch (the layer above the thread)` is a description of context-routing identical in spirit to Ch11's hierarchy/dispatcher discussion.
[^12]: `genesis-architect.agent.md:354 ## Four tiers of pattern thinking` includes Tier-3 A1 PANEL / A4 STAFFED PLAN — the multi-agent surface Ch12 covers prose-side.
[^13]: Architect agent's review posture aligns with Ch13 ADAPT loop, but the agent does not own the meta-process.
[^14]: `genesis-architect.agent.md:437 ## Anti-patterns you flag (named in classic terms)` and `:474 ## Severity rubric for findings` are a sibling taxonomy to Ch14's 19 anti-patterns; many entries are isomorphic, several are name-divergent (e.g. "GOD MODULE" vs Ch14 "context-overload"). Strong cross-cite candidate; mild taxonomy conflict.
[^15]: **CANONICAL CONFLICT.** `assets/primitives.md:1 # TIER 0 -- Substrate primitives` / `:3 The six concepts every agent harness implements` enumerates SIX primitives by RUNTIME ROLE (PERSONA / MODULE ENTRYPOINT / RULE / CHILD-THREAD SPAWN / TRIGGER ORCHESTRATOR / PLAN PERSISTENCE). Handbook `ch09-the-instrumented-codebase.qmd:23 ## The Seven Primitive Types` / `:7` ("It defines seven primitive types") enumerates SEVEN by FILE-EXTENSION + USE-CASE (Instructions / Agents / Skills / Prompts / Memory / Orchestration / Hooks). Different taxonomies, not mergeable by addition. See §2 below.
[^16]: `assets/primitives.md:230-239` maps each primitive to a PROSE axis — direct gloss on Ch10.
[^17]: `assets/primitives.md` SCOPE-ATTACHED RULE FILE = directory-scoped instructions; Ch11 §The Instruction Hierarchy at `ch11-context-engineering.qmd:56` is the same five-layer cascade. Naming differs.
[^18]: TRIGGER ORCHESTRATOR + CHILD-THREAD SPAWN are the substrate Ch12's writer/reviewer/tester topologies sit on.
[^19]: PLAN PERSISTENCE is the substrate of Ch13's checkpoint discipline (`ch13-the-execution-meta-process.qmd:215 ## Checkpoint Discipline`). Naming differs ("plan.md / checkpoints" both).
[^20]: `primitives.md` enumerates several anti-patterns inline (PHANTOM DEPENDENCY, BUNDLE LEAKAGE) that Ch14 does not include but should cross-reference.
[^21]: Final paragraph of `primitives.md` argues vocabulary outlives any one tool — same thesis as Ch15 line 5 ("the methodology survives tool change. The primitives survive model change.").
[^22]: `composition-substrate.md` defines MODULE / DEPENDENCY / DISTRIBUTION BOUNDARY / TRANSITIVE CLOSURE / VERSION PINNING / PORTABILITY MODE — durable concepts Ch09 does not have. Adds a missing layer to Ch09's taxonomy.
[^23]: Composition-mode rules (INLINE / LOCAL SIBLING / EXTERNAL MODULE) implement Reduced Scope + Orchestrated Composition (PROSE).
[^24]: TRANSITIVE CLOSURE + PORTABILITY MODE bear directly on context-budget reasoning at Ch11's hierarchy edges.
[^25]: `composition-substrate.md:111-150` enumerates DUPLICATED LEAF / HIDDEN EXTERNAL / UNPINNED CRITICAL DEP / TRANSITIVE BLOAT / BOUNDARY VIOLATION / TOOL LEAK / BUNDLE LEAKAGE — a packaging-anti-pattern set absent from Ch14. Direct candidate for cross-reference / merge.
[^26]: A1 PANEL is the architectural realization of Ch08's "Three Roles" applied to deliberation.
[^27]: Several Tier-3 patterns name primitives by Genesis's vocabulary, not Ch09's; reading the catalogue exposes the naming gap.
[^28]: A6/A9/A10 wave/sandbox/capability discussion is the operational realization of Safety Boundaries (PROSE §S, `ch10-the-prose-specification.qmd:221`).
[^29]: A1/A2/A4/A5 selection assumes a Plan Memento + dispatcher hierarchy, which is what Ch11 builds.
[^30]: A1 PANEL, A2 PIPELINE, A3 ORCHESTRATOR-SAGA, A4 STAFFED PLAN, A7 ADVERSARIAL REVIEW are direct cognates of Ch12's Writer/Reviewer/Tester, Domain Teams, Audit-Execute-Validate sequences (`ch12-multi-agent-orchestration.qmd:45`).
[^31]: A5 WAVE EXECUTION (`architectural-patterns.md:200`) maps to Ch13 §Wave Decomposition (`ch13-the-execution-meta-process.qmd:137 ## Wave Decomposition`). Both teach the same discipline; Genesis adds explicit gates and re-plan rules.
[^32]: Each Tier-3 pattern carries an ANTI-PATTERNS subsection (e.g. WAVE-WITHOUT-GATE, COSMETIC DISSENT, PLAN-AND-PRAY, TOKEN-LAUNDERING, IMPLICIT-TRUST OUTER LOOP) — a sibling catalogue to Ch14's 19. Direct merge / cross-reference target.
[^33]: A10 GOVERNED OUTER LOOP is the substrate-level realization of Ch15's "agent governance becomes a first-class engineering discipline" prediction.
[^34]: C1 LAZY ASSET / C2 PERSONA PRELOAD / C6 EXTERNAL CORPUS GROUNDING are primitive-loading shapes Ch09 names obliquely (Memory, Skill, Agent) but does not pattern-name.
[^35]: Tier-2 catalogue is a per-axis (Creational/Structural/Behavioral) library of PROSE-realizing patterns; B8 ATTENTION ANCHOR is the LLM-physics-native cure absent from PROSE's prose-only vocabulary.
[^36]: B4 PLAN MEMENTO + B8 ATTENTION ANCHOR are the operational heart of Ch11 context engineering at long-session scale; `design-patterns.md:617 ## B8. ATTENTION ANCHOR` is the load-bearing cell.
[^37]: B1 FAN-OUT + SYNTHESIZER, B3 SUPERVISOR, B7 TODO COMMAND are the patterns Ch12 describes prose-only.
[^38]: B5 ACCEPTANCE OBSERVER, B7 TODO COMMAND, B9 GOAL STEWARD, B10 HUMAN CHECKPOINT operationalize Ch13 phase boundaries.
[^39]: Each design pattern carries an ANTI-PATTERN named in classical idiom (EAGER BLOAT, MID-SESSION PERSONA SWAP, PLAN-AND-PRAY, NAMED-NOT-GROUNDED EXPERT, MOVING-GOALPOST STEWARD, etc.). Strong overlap with Ch14 §Five Foundational Anti-Patterns + §Execution Anti-Patterns.
[^40]: R1 SPLIT / R2 FUSE / R3 EXTRACT / R4 INLINE are the source-time refactor verbs Ch09 lacks. They name the operations that move primitives across files / between layers.
[^41]: R3 EXTRACT enforces Reduced Scope (PROSE §R) at module granularity; R1 SPLIT enforces Progressive Disclosure when one entrypoint is overloaded.
[^42]: SPLIT/FUSE arbitrate dispatcher-collision tradeoffs that Ch11 surfaces only at the dispatcher hierarchy level.
[^43]: GOD MODULE / DUPLICATED INLINE CONTENT / WRONG-LENS INLINE / PHANTOM DEPENDENCY / RUSHED INLINE / PROMOTION-WITHOUT-NEED are the source-time anti-pattern set; Ch14 covers run-time anti-patterns. Adjacent and complementary; no overlap.
[^44]: Matrix #2 (Gate types: INTERNAL/EXTERNAL × PROGRAMMATIC/JUDGEMENT) is the decision tool an Architect uses; Ch08 names the role but not the matrix.
[^45]: Matrix #1 (Hallucination countermeasures) maps "TRUTHS" (#1 finite context, #4 hallucination is inherent, etc.) to patterns. Ch09 is the artifact catalogue but does not pair them with truths.
[^46]: Every matrix in the file maps named patterns to PROSE truths or PROSE axes; matrix #1 row "(architectural) PLAN BEFORE EXECUTION" reads as a PROSE-supplement.
[^47]: Matrix #3 grounding doctrine (Internal × Eager, External × Lazy) sharpens the C6 EXTERNAL CORPUS rule that sits beneath Ch11's hierarchy.
[^48]: Matrix #4 threading topology (parallel/sequential × shared state) is the coordination-tax decision tool Ch12 describes prose-only at `:356 ## The Coordination Tax: Honest Numbers`.
[^49]: Matrix #5 (synthesis style — implied by SKILL.md and architect agent) is the same arbitration discipline Ch13 §Checkpoint Discipline depends on.
[^50]: The whole file is structured as "when you see failure mode X, the missing pattern is Y" — same shape as Ch14's anti-pattern → recovery mapping.
[^51]: Component-diagram conventions (node-shape per primitive type) standardize visualization of Ch09's primitives.
[^52]: Dependency-graph diagrams (step 3.5) make Ch11's hierarchy visualizable at module granularity.
[^53]: Sequence diagram + thread spawn / fan-in conventions are the visual specification language for every Ch12 topology. Direct mandatory reading for any handbook illustrator.
[^54]: A8 ALIGNMENT LOOP / A9 SUPERVISED EXECUTION / B10 HUMAN CHECKPOINT diagram conventions (round counter, double-line tool-call edges) are the visual grammar Ch13's wave/checkpoint discussion lacks.
[^55]: Defines the SIX primitive concepts harness-agnostic — same scope as Ch09 §Tool Support and Portability table at `ch09-the-instrumented-codebase.qmd:313`.
[^56]: PROSE's Explicit Hierarchy is realized by SCOPE-ATTACHED RULE FILE cascade documented here.
[^57]: SCOPE-ATTACHED RULE FILE = the cascading-instructions layer that drives Ch11's Five-Layer Hierarchy.
[^58]: TRIGGER ORCHESTRATOR + CHILD-THREAD SPAWN substrate is the foundation under Ch12 topologies.
[^59]: Portability-rules.md "When a per-harness reach is justified / NOT justified" enumerates anti-patterns of harness-coupling Ch14 lacks.
[^60]: Portability-rules.md is the operational realization of Ch15's "stack crystallizes through independent convergence" thesis (ch15:17).
[^61]: Per-harness adapters (claude-code / codex / copilot / cursor / opencode) ARE the "Tool Support and Portability" table at Ch09:313 — at adapter granularity. Direct.
[^62]: Per-harness file paths and dispatch rules show how Ch11's hierarchy LOADS in each harness.
[^63]: Per-harness adapters illustrate the convergence Ch15:17 names.
[^64]: gh-aw is one of the workflow-trigger surfaces a "Hooks" entry in Ch09 abstracts over.
[^65]: gh-aw's `safe-outputs:` subsystem is the canonical realization of Safety Boundaries (PROSE §S, `ch10-the-prose-specification.qmd:221`) under capability-gating semantics.
[^66]: Trigger surface is the substrate under any A6 EVENT-DRIVEN / A10 GOVERNED OUTER LOOP multi-agent topology.
[^67]: gh-aw runs Ch13's wave / phase patterns under runtime supervision — useful concrete example.
[^68]: TOKEN-LAUNDERING / IMPLICIT-TRUST OUTER LOOP / OVER-BROAD TRIGGERS / WEAK-FORM A9 INSIDE STRONG-FORM SURFACE — runtime anti-patterns Ch14 does not catalogue.
[^69]: gh-aw is the cited convergence point of "agentic computing stack crystallizes" (ch15:17).
[^70]: APM's mapping from substrate concepts to manifest / lockfile / dependency-spec syntax. The package-manager realization Ch09 §Tool Support gestures at.
[^71]: APM's publish-time rules drive what loads at every layer of Ch11's hierarchy.
[^72]: APM publish-time rules enforce BUNDLE LEAKAGE / PHANTOM DEPENDENCY mitigations.
[^73]: Cited as the manifest-based dependency-resolution case in Ch15:17 ("manifest-based primitive distribution... open-source tools already provide manifest-based dependency resolution and security scanning at the primitive layer").
[^74]: Worked examples render the Architect-Reviewer-Escalation triple Ch08 abstracts.
[^75]: Examples 01 and 02 carry PROSE-axis citations on their own findings.
[^76]: Example 02 is the canonical A1 PANEL realization the handbook-panel skill itself runs on; example 01 is the canonical A8 ALIGNMENT LOOP + A7 ADVERSARIAL REVIEW realization. Both are direct illustrations of Ch12's Writer/Reviewer/Tester pattern.
[^77]: Both examples surface a wave-style decomposition with explicit gates between rounds, illustrating Ch13.
[^78]: Both examples enumerate the anti-patterns the panel caught (cosmetic dissent, warm-context cold reader, etc.) — direct overlay on Ch14.
[^79]: Example 03 demonstrates a single-skill release-notes flow — directly relevant to Ch08-10 (single-thread practitioner working with constraints) but only marginally to multi-agent / wave / anti-pattern chapters.
[^80]: Examples 04+05 are two PR-review modes: advisory (no verdict) vs verdict (GO/REFINE). Together they instantiate PROSE Safety Boundaries (10), Writer/Reviewer/Tester topology (12), and surface review anti-patterns (14). 04 vs 05 also illustrates a strong/weak A9 form choice (15 governance trajectory).

---

## 2. Canonical Conflicts (verbatim)

Each entry: severity (CANONICAL = irreconcilable taxonomy / vocabulary; EMPHASIS = same idea, different scope; TERMINOLOGY = same idea, different name; OMISSION = one corpus has it, the other doesn't).

### C1. Six substrate primitives vs Seven primitive types — **CANONICAL**

Genesis, `assets/primitives.md:1-3`:

> # TIER 0 -- Substrate primitives
>
> The six concepts every agent harness implements under different folder
> names and frontmatter dialects. Genesis names them once so the
> vocabulary outlives any one tool.

The six (per `assets/primitives.md` section headers): **PERSONA SCOPING FILE**, **MODULE ENTRYPOINT**, **SCOPE-ATTACHED RULE FILE**, **CHILD-THREAD SPAWN**, **TRIGGER ORCHESTRATOR**, **PLAN PERSISTENCE**.

Handbook, `ch09-the-instrumented-codebase.qmd:7`:

> This chapter catalogs those files. It defines seven primitive types, shows what each looks like, explains how they compose, and walks through the transformation of an uninstrumented repository into one that's ready for agentic development.

And `ch09-the-instrumented-codebase.qmd:23-25`:

> ## The Seven Primitive Types
>
> Seven categories cover the full range of knowledge an agent needs.

The seven (per Ch09 section headers `:43, :75, :121, :174, :217, :256, :294`): **Instructions**, **Agents**, **Skills**, **Prompts**, **Memory**, **Orchestration**, **Hooks**.

Why irreconcilable: the cuts run on **different axes**. Genesis cuts by RUNTIME ROLE (file-loaded-into-thread vs spawn-affordance vs orchestrator-above-the-thread vs persistence-store). Handbook cuts by FILE-EXTENSION × USE-CASE. The two sets are not trivially mergeable: e.g. Genesis's "MODULE ENTRYPOINT" is a single role realized as Ch09's "Skills" OR "Agents" OR "Prompts" depending on use-case; Genesis's "PLAN PERSISTENCE" is closest to but strictly narrower than Ch09's "Memory" (active plan/todos/checkpoints vs cross-session knowledge); Genesis's "TRIGGER ORCHESTRATOR" maps to Ch09's "Hooks" but is also the substrate under Ch09's "Orchestration" (`.spec.md`). Picking one cut means deprecating the other as the **public** vocabulary; both can survive as internal references. **Decision required by the panel.**

### C2. agentskills.io as authority on "skill" — **TERMINOLOGY / CANONICAL**

Genesis, `assets/primitives.md:48-58`:

> What agentskills.io does NOT own (genesis is authoritative):
> the broader primitive taxonomy. The agentskills.io corpus uses
> "skill" as the unit, conflating the container surface with the
> agent's whole behavior. Genesis treats MODULE ENTRYPOINT as ONE
> primitive type among PERSONA SCOPING, SCOPE-ATTACHED RULE,
> CHILD-THREAD SPAWN, ORCHESTRATOR, ASSET. Do not let the spec's
> unit framing erase the other primitive types when designing.

Handbook, `ch09-the-instrumented-codebase.qmd:121` (§Skills) and `:172`:

> Skills differ from instructions in an important way: they provide *decision frameworks*, not just rules.

The handbook treats "Skills" as one of seven primitives (a class of files). Genesis treats "skill" as a CONTAINER that BUNDLES one or more primitives plus dependencies (the MODULE concept in `composition-substrate.md:18-26`). The handbook's framing is the framing Genesis explicitly warns against. **Severity = CANONICAL** because it surfaces in every reference to "Skills"; downstream reviewers will read the handbook through one lens and Genesis through the other unless arbitrated.

### C3. Hooks vs TRIGGER ORCHESTRATOR — **CANONICAL (scope mismatch)**

Handbook, `ch09-the-instrumented-codebase.qmd:294-298`:

> ### Hooks
>
> **Purpose:** Define automated actions triggered by development events. Hooks bridge the gap between passive context (instructions, memory) and active behavior, making the instrumented codebase reactive rather than waiting to be queried.
>
> **File format:** Configured via tool-specific hook mechanisms (e.g., VS Code tasks, GitHub Actions triggers, copilot hooks configuration) rather than a single portable file format.

Genesis, `assets/primitives.md` §5 (around line 174):

> ## 5. TRIGGER ORCHESTRATOR
>
> A declarative pipeline that spawns sessions in response to events
> (schedule, push, comment, label, manual). Lives ABOVE the thread,
> deciding when work begins and what initial context it carries.
>
> INDUSTRY TERMS: "workflow", "hook", "automation", "trigger".

Same general object (event → run), but Genesis's TRIGGER ORCHESTRATOR is the load-bearing substrate under all of A6 EVENT-DRIVEN, A9 SUPERVISED EXECUTION (strong form), and A10 GOVERNED OUTER LOOP, with optional fields SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE (`assets/runtime-affordances/common.md` and `architectural-patterns.md:530-635`). The handbook's "Hooks" reduces this to "automation on dev events" without naming the substrate fields the architectural patterns rely on. **Decision required: does Ch09 absorb Genesis's substrate-field model, or does Genesis collapse "TRIGGER ORCHESTRATOR" into "Hooks"?** Note: Ch15:17 already cites GitHub Agentic Workflows positively, which is the trigger-surface Genesis treats as A10 canonical.

### C4. Memory vs PLAN PERSISTENCE — **EMPHASIS**

Handbook, `ch09-the-instrumented-codebase.qmd:217-247`:

> ### Memory
>
> **Purpose:** Preserve knowledge across sessions. Agents are stateless; every conversation starts from zero. Memory files give them access to accumulated decisions, resolved trade-offs, and project history that would otherwise vanish between sessions.
>
> ... Memory files capture the knowledge that doesn't fit in instructions because it isn't a rule; it's context.

Genesis, `assets/primitives.md` §6:

> ## 6. PLAN PERSISTENCE
>
> A stable artifact (file or structured store) holding the active plan,
> todos, and checkpoints across turns and across spawns. The cure for
> attention decay over long sessions.
>
> INDUSTRY TERMS: "plan.md", "TODO state", "checkpoints", "session store".

These are adjacent but **not coextensive**: Memory = cross-session knowledge accumulation; PLAN PERSISTENCE = active-plan state across turns / spawns within and between sessions. Genesis treats long-running PLAN as a primitive in its own right because B4 PLAN MEMENTO + B8 ATTENTION ANCHOR depend on it (`design-patterns.md:520, :617`); the handbook collapses both into one bin labeled "Memory". **Severity = EMPHASIS.** Recommendation: split or formally annotate.

### C5. PROSE — **NO CONFLICT (alignment confirmed)**

Genesis, `assets/primitives.md:230-234`:

> Each primitive earns its keep against PROSE
> ([danielmeppiel.github.io/awesome-ai-native](https://danielmeppiel.github.io/awesome-ai-native/)):

Genesis maps each substrate primitive to one PROSE axis (P/R/O/S/E). Handbook Ch10 owns the canonical PROSE chapter. Both texts agree on the five letters, the five names, and that PROSE is constraint-shaped. **No conflict.** Note for review panel: the cite goes from Genesis → external blog (danielmeppiel.github.io); the handbook owns the canonical exposition. Genesis should cite Ch10 instead.

### C6. Run-time anti-patterns vs source-time anti-patterns — **OMISSION (both directions)**

Handbook Ch14 (`ch14-anti-patterns-and-failure-modes.qmd:13`) and `:47 ## The Five Foundational Anti-Patterns` plus `:117 ## Execution Anti-Patterns` enumerate run-time-observable failures (silent failures, file-presence-is-execution, context overload).

Genesis distributes a sibling anti-pattern set across SEVEN files:
- `composition-substrate.md:111-150` (DUPLICATED LEAF / HIDDEN EXTERNAL / UNPINNED CRITICAL DEP / TRANSITIVE BLOAT / BOUNDARY VIOLATION / TOOL LEAK / BUNDLE LEAKAGE)
- `refactor-patterns.md` PREMATURE SPLIT / FORCED FUSION / PROMOTION-WITHOUT-NEED / RUSHED INLINE
- `design-patterns.md` EAGER BLOAT / MID-SESSION PERSONA SWAP / NAMED-NOT-GROUNDED EXPERT / MOVING-GOALPOST STEWARD (and ~15 more)
- `architectural-patterns.md` WAVE-WITHOUT-GATE / COSMETIC DISSENT / RED TEAM WITHOUT TEETH / WARM-CONTEXT COLD READER / PLAN-AND-PRAY / VERIFY-WITH-LLM-ONLY / TOKEN-LAUNDERING / IMPLICIT-TRUST OUTER LOOP / OVER-BROAD TRIGGERS / HARNESS-PORTABILITY THEATRE / WEAK-FORM A9 INSIDE STRONG-FORM SURFACE
- `genesis-architect.agent.md:437`
- `runtime-affordances/portability-rules.md:45-48`
- `pattern-tradeoffs.md` Matrix #1 (countermeasure rows)

Estimated total: 35-50 named anti-patterns spread across Genesis. The two sets are **largely disjoint** — Genesis's are source-time / module-graph / multi-agent-orchestration failures; Ch14's 19 are run-time / single-agent / team-process failures. **Severity = OMISSION (mutual).** This is the largest cross-corpus integration opportunity.

### C7. PHANTOM DEPENDENCY / BUNDLE LEAKAGE — **OMISSION**

Genesis, `composition-substrate.md:128-150`:

> - BUNDLE LEAKAGE: non-runtime files colocated INSIDE the module's
>   distribution boundary (eval scenarios, contributor scripts, dev
>   notes, scratch fixtures). The symmetric counterpart of PHANTOM
>   DEPENDENCY (referenced-but-not-bundled): bundled-but-not-
>   consumed-at-runtime.

These two named failures (and DISPATCH CONTAMINATION as the more serious sub-case of BUNDLE LEAKAGE) have no Ch14 entry. They are real, named, observed in production (Genesis cites APM's local-content scanner). **Severity = OMISSION** in Ch14.

### C8. A1 PANEL vs Domain Teams — **TERMINOLOGY (no canonical conflict)**

Genesis A1 PANEL (`architectural-patterns.md:33-76`) and Handbook §Agent Specialization Patterns at `ch12-multi-agent-orchestration.qmd:45` describe the **same shape** (specialist threads + synthesis decision) under different names. **Severity = TERMINOLOGY.** Recommendation: pick one canonical name in the published artifact; note the other in cross-reference.

### C9. Wave Execution — **NO CONFLICT (alignment confirmed)**

Genesis A5 WAVE EXECUTION (`architectural-patterns.md:200-241`) and Handbook §Wave Decomposition (`ch13-the-execution-meta-process.qmd:137`) teach the same discipline: topologically sort the DAG, group same-depth tasks into a wave, gate between waves, re-plan from failed wave on gate failure. Genesis adds the explicit anti-patterns (WAVE-WITHOUT-GATE, EVERY-TASK-IS-A-WAVE) which Ch13 should cite.

### C10. Architect-Reviewer-Escalation roles — **ALIGNMENT**

Handbook Ch08 §Your Three Roles (`ch08-the-practitioners-mindset.qmd:55`) and Genesis architect agent persona (`genesis-architect.agent.md:285, :300`) describe the same posture. **No conflict;** Genesis is a worked specialization of one of the three roles.

---

## 3. Persona Reading Lists (review panel)

Each persona gets 1-3 high-signal Genesis reads. Allocations are non-redundant where possible.

### Practitioner Authority
**Reads:** `skills/genesis/SKILL.md` + `skills/genesis/assets/architectural-patterns.md`
**Why:** SKILL.md is the disciplined 8-step process the persona's "battle-tested" lens needs to validate. architectural-patterns.md is the tier-3 pattern catalogue with explicit ANTI-PATTERNS sections — the operational test of "does this pattern actually survive contact with a multi-agent runtime?". Both files are normative-by-construction and demand evidence-grounded review.

### Chief Editor (voice / structure / bloat)
**Reads:** `skills/genesis/assets/primitives.md` + `skills/genesis/assets/composition-substrate.md`
**Why:** These two are the load-bearing taxonomy files. Chief Editor must arbitrate the 6-vs-7 conflict (§C1) at the **prose** level — what taxonomy ships in the published handbook, what hyphens / capitalizations / parallel structures are used. composition-substrate.md adds a layer (MODULE / DEPENDENCY / DISTRIBUTION BOUNDARY / TRANSITIVE CLOSURE / VERSION PINNING / PORTABILITY MODE) the handbook doesn't have; editorial decision: absorb, footnote, or ignore.

### Dev Lead Proxy ("can I use this Monday?")
**Reads:** `skills/genesis/examples/` (especially 01-readme-iteration.md and 02-review-panel-architecture.md) + `skills/genesis/assets/refactor-patterns.md`
**Why:** Examples are the only Monday-runnable artifacts. refactor-patterns.md (R1 SPLIT / R2 FUSE / R3 EXTRACT / R4 INLINE) gives the Dev Lead a verb-set for the source-time decisions Ch09 leaves implicit ("when do I split this skill?"). If a Dev Lead can't apply these on Monday, the handbook chapter has a gap.

### CTO Proxy ("so what?", "prove it")
**Reads:** `skills/genesis/assets/pattern-tradeoffs.md` + `skills/genesis/assets/architectural-patterns.md` (sections A9-A10 in particular, lines 411-645)
**Why:** pattern-tradeoffs.md is six matrices that close decision spaces (gate types, grounding doctrine, threading topology, synthesis style, hallucination countermeasures × truths). The CTO lens demands "show me the decision matrix, not the pattern list". A9 + A10 carry the strong-form-vs-weak-form supervision argument and the substrate-cost argument — directly answers "why pay for governance?" and grounds Ch15's governance prediction.

### Illustrator (mermaid / visual specs)
**Reads:** `skills/genesis/assets/mermaid-conventions.md` + `skills/genesis/assets/design-patterns.md`
**Why:** mermaid-conventions.md is a complete visual-grammar specification (diagram-per-step mapping, node-shape conventions, double-line edges for tool-call results crossing into LLM, A8 round-counter conventions, A9 cylinder for tool nodes). It has no sibling in the handbook. design-patterns.md gives the canonical Tier-2 patterns the diagrams illustrate. Read together they form the visual style guide for any handbook chapter that draws topology.

### Fact & Ref Checker
**Reads:** `skills/genesis/assets/primitives.md` + `skills/genesis/assets/module-system-adapters/apm.md` (+ skim `skills/genesis/agents/genesis-architect.agent.md:198-220`)
**Why:** primitives.md cites agentskills.io as a corpus and reserves authority over taxonomy — Fact Checker must verify (a) the agentskills.io citation is accurate and (b) the taxonomy claim does not silently borrow handbook framing. apm.md is the case Ch15:17 cites for "manifest-based primitive distribution" — verify the convergence claim. The genesis-architect.agent.md disambiguation block enumerates the exact authority-boundary each external corpus owns.

### Thought Leadership (voice / positioning / authenticity)
**Reads:** `skills/genesis/SKILL.md` + `skills/genesis/agents/genesis-architect.agent.md` + `skills/genesis/assets/runtime-affordances/portability-rules.md`
**Why:** SKILL.md and the architect agent together carry Genesis's voice — disciplined, anti-buzzword, specifies-its-own-anti-patterns. portability-rules.md is the pure positioning artifact: it argues the methodology survives tool change (the same thesis as Ch15:5 — "the methodology survives tool change. The primitives survive model change."). Read together they let Thought Leadership judge whether the handbook's voice matches or drifts from the corpus that informed it.

---

## 4. Open Questions for the Panel

1. **Which primitive taxonomy ships?** The handbook's seven (file-extension × use-case) is more accessible to a first-time reader; Genesis's six (runtime role) is more durable across tool change. Picking neither leaves a permanent vocabulary fork. Picking both leaves cross-references confusing. Recommend the panel arbitrate at the CEO / Chief Editor level and pick one as the **public** vocabulary, the other as **internal architect-reference**.

2. **Should Hooks absorb TRIGGER ORCHESTRATOR's substrate fields (SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE), or stay scoped to "actions on dev events"?** Ch15:17 already commits to gh-aw being canonical; the substrate-field model is what makes A10 GOVERNED OUTER LOOP buildable. If Hooks stays narrow, Ch09 needs a new primitive or a pointer to the architectural-patterns layer.

3. **Does Ch09's "Skills = decision frameworks" framing replace, or layer on top of, Genesis's MODULE ENTRYPOINT?** Genesis treats "skill" as a container; the handbook treats it as a content-shape. These can coexist if labeled distinctly, but right now they share the word.

4. **Is Memory split into PLAN PERSISTENCE (active plan / checkpoints) and CROSS-SESSION KNOWLEDGE (the current `.memory.md` use case)?** The B8 ATTENTION ANCHOR pattern needs the former named separately; the latter is what `.memory.md` currently is. Two-bin split is cheap.

5. **Does Ch14 absorb Genesis's source-time anti-pattern catalogue (composition-substrate, refactor-patterns, design-patterns, architectural-patterns ANTI-PATTERN sections)?** Estimated 35-50 named entries. If yes, Ch14 roughly doubles in length. If no, Genesis becomes the canonical anti-pattern reference and Ch14 cites it.

6. **Is the agentskills.io citation in `assets/primitives.md:230-234` (PROSE → external blog) replaced by a citation to Ch10?** Genesis exists inside the handbook's broader corpus; PROSE has a canonical chapter now. The blog-cite is a leftover.

7. **Does the handbook adopt Genesis's mermaid conventions wholesale (`assets/mermaid-conventions.md`)?** It is a complete visual-grammar specification with no sibling. Adopting it standardizes every diagram; not adopting it leaves the handbook's diagrams stylistically inconsistent with the canonical patterns they illustrate.

---

End of artifact.
