# Round 1 — Panel Synthesis (A4 gate document)

> Aggregated from 7 R1 cold reads: Practitioner Authority, Chief Editor, Dev
> Lead Proxy, CTO Proxy, Illustrator, Fact & Ref Checker, Thought Leadership.
> Grounded in `WIP/affinity-matrix.md` (10 conflicts C1-C10 + 7 open
> questions). Synthesis only — no new findings (those go in §7).

---

## Executive headline

The panel is **unanimous** on five things: (1) Genesis is a positioning multiplier and a Monday-yield multiplier for the handbook, not just companion material; (2) the four-verb refactor catalogue (R1 SPLIT / R2 FUSE / R3 EXTRACT / R4 INLINE) and the substrate composition vocabulary (MODULE / DEPENDENCY / DISTRIBUTION BOUNDARY) are gaps in the handbook the corpus closes cheaply; (3) **C1 (six vs seven primitives) is the load-bearing conflict that gates every Ch09 / Ch12 / Ch14 deep-dive** and must be resolved before round 2 dispatches; (4) Ch14's run-time anti-pattern catalogue and Genesis's source-time / governance / packaging anti-pattern set are largely disjoint and the integration is the single largest cross-corpus opportunity; (5) Ch15's governance prediction silently borrows Genesis's substrate-field model (SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE) without naming it — falsifiability is on the table.

The panel **disagrees** on three things the author has to call: (a) whether the **PHANTOM DEPENDENCY / BUNDLE LEAKAGE** entries are Gold (Chief Editor, Dev Lead, Practitioner Authority) or "wrong audience for handbook narrative" (Thought Leadership); (b) whether to **absorb Genesis vocabulary verbatim** (Thought Leadership: yes, names are signature artifacts) or **soften into handbook register** (Chief Editor: only the names verbatim, prose in handbook voice — these reconcile if rule §4a from Thought Leadership becomes house style); (c) whether the **8-step design discipline** survives unmodified in the handbook (Practitioner Authority and Dev Lead say scope it to cross-cutting redesigns; Thought Leadership says ship the *outputs*, demote the steps).

The author's A4 gate work-list (full version in §6): pick a C1 shape, pick a C3 / C4 scope split, pick a voice rule (verbatim names), pick whether Ch14 doubles or Genesis becomes the canonical anti-pattern reference, pick whether Ch15:17 commits to substrate-field vocabulary or footnotes it.

---

## Section 1 — Battle-Tested Gold (consolidated)

De-duplicated. Strength = **UNANIMOUS** (≥4 personas), **STRONG** (2-3), **MODERATE** (1 with strong evidence). Personas: PA = Practitioner Authority, CE = Chief Editor, DL = Dev Lead, CTO, IL = Illustrator, FR = Fact & Ref Checker, TL = Thought Leadership.

### G-UNANIMOUS

| ID | Topic | Source (Genesis file:line) | Recommended chapter | Why it elevates | Personas |
|---|---|---|---|---|---|
| G1 | **A10 GOVERNED OUTER LOOP** + substrate fields (SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE) + 6 anti-patterns (TOKEN-LAUNDERING, IMPLICIT-TRUST OUTER LOOP, OVER-BROAD TRIGGERS, HARNESS-PORTABILITY THEATRE, INNER-LOOP MISCAST AS OUTER, WEAK-FORM A9 INSIDE STRONG-FORM SURFACE) | `architectural-patterns.md:530-645` | **Ch15** primary, **Ch5/Ch12** secondary, **Ch14** for the 6 anti-patterns | Gives Ch15's "governance becomes a category" prediction three named, falsifiable fields and one canonical realization (gh-aw safe-outputs). Converts hand-waving into procurement language. | PA, CTO, TL, FR (M3) |
| G2 | **R1 SPLIT / R2 FUSE / R3 EXTRACT / R4 INLINE** — the four refactor verbs with triggers + procedure + per-verb anti-patterns | `assets/refactor-patterns.md:1-217` | **Ch14 §"Not Fixing the Primitives"** + **Ch09 §Instructions / §Skills** | Ch14 says "fix the primitive"; Genesis names *which* fix. R3 EXTRACT's step-4 phantom-dep check is a correctness gap in Ch14's current "Extract" recovery — readers following Ch14 alone will ship a broken bundle. | DL (G1), PA, CE (1f), IL (taxonomy) |
| G3 | **A1 PANEL** + 3 anti-patterns (PANEL-WITHOUT-SYNTHESIS, PANEL-IN-ONE-CONTEXT, IMBALANCED PANEL) with cited realization (`apm-review-panel`) | `architectural-patterns.md:33-76` | **Ch12 §Pattern 1 Writer/Reviewer/Tester** | Lifts Ch12's "specialization is good" prose into a falsifiable rubric. PANEL-IN-ONE-CONTEXT names the failure Ch12 implies but never names. Tied to TL's "rejection-with-WHEN-clause" discipline. | PA, TL (1d), DL (G2), CTO (gate-types) |
| G4 | **A5 WAVE EXECUTION** + WAVE-WITHOUT-GATE + EVERY-TASK-IS-A-WAVE | `architectural-patterns.md:200-241` | **Ch14** (cite-and-import) + **Ch13 §Wave Decomposition** (cross-link) | Closes the gap where Ch14 lists 19 run-time anti-patterns but no wave-shape failure modes. Already aligned with handbook discipline (C9). | PA, DL, IL |

### G-STRONG

| ID | Topic | Source | Recommended chapter | Why | Personas |
|---|---|---|---|---|---|
| G5 | **A9 SUPERVISED EXECUTION** + 4 anti-patterns (PLAN-AND-PRAY, VERIFY-WITH-LLM-ONLY, UNCHECKPOINTED IRRECOVERABLE, TOOLLESS PRECONDITION) and the **STRONG vs WEAK FORM** distinction | `architectural-patterns.md:411-528` | **Ch14 §Trust Fall + Hallucinated Edits** (cross-link); STRONG-vs-WEAK as new Ch14 entry | VERIFY-WITH-LLM-ONLY is the architectural cause; Ch14's Trust Fall (`ch14:127-131`) is the symptom. Cross-linking gives readers both layers. STRONG-vs-WEAK is a board-readable security-review item ("are we leaving safety on the table?"). | PA, CTO, TL |
| G6 | **A7 ADVERSARIAL REVIEW** + **COLD READER** sub-pattern + WARM-CONTEXT COLD READER anti-pattern | `architectural-patterns.md:290-356`; `examples/01-readme-iteration.md:64-70, 144-150` | **Ch12 §Pattern 1**, optional **Ch14** entry | Promotes "no warm-context handoff" from a half-sentence (`ch12:70`) to a load-bearing constraint with a named failure mode. Concept-Monday-ready as a review-discipline rule even without fan-out harness. | PA, DL (G3), IL (subgraph) |
| G7 | **B8 ATTENTION ANCHOR** + 5 re-injection boundaries + 3 anti-patterns (ANCHOR DRIFT, OVER-ANCHORING, IMPLICIT-ANCHOR) — "CLASSICAL ANALOG: NONE" | `assets/design-patterns.md:617-683` | **Ch11 Context Engineering** as the chapter spine | TL's strongest signature-move candidate. Single most under-named concept in public agentic-dev conversation. Ch11 currently talks around it. | TL (1a), IL (round counter), PA (implicit) |
| G8 | **Substrate composition vocabulary** — MODULE, DEPENDENCY, DISTRIBUTION BOUNDARY, TRANSITIVE CLOSURE, VERSION PINNING, PORTABILITY MODE; plus the 3 composition modes (INLINE / LOCAL SIBLING / EXTERNAL MODULE) and the 4-clause "should this be its own module?" rubric (RULE OF THREE / INDEPENDENT RELEASE / DIFFERENT OWNER / PINNING-WORTHY) | `assets/composition-substrate.md:18-105`; `primitives.md:245-273` | **Ch09 new sub-section "Composition and reuse"** (ABSORB MODULE / DEPENDENCY / DISTRIBUTION BOUNDARY); **Ch09 footnote** (TRANSITIVE CLOSURE, VERSION PINNING); **Ch09 merge** (PORTABILITY MODE) | Closes Ch09's "Start with three to five agent configurations" → "but how do I share / version them?" gap. Gives APM-shaped distribution a vocabulary. | CE (1f, 4b), DL (G4), FR |
| G9 | **PROSE-axis mapping table** — each substrate primitive ↔ one PROSE axis | `primitives.md:233-239` | **Ch10 closing** (`ch10:562`) or **Ch11 opening** | Ch10 introduces the five constraints; Ch09 enumerates the files; nothing currently connects them. This 5-row table does. Letter-for-letter aligned with Ch10 (FR confirmed). | CE (1d), FR (M1) |
| G10 | **Mermaid conventions wholesale** — node-shape vocabulary (PERSONA `((..))`, SKILL `[..]`, RULE `[/../]`, ORCHESTRATOR `{..}`, ASSET `[(..)]`); double-line `==>` for tool-call → LLM; cylinder for S7 DETERMINISTIC TOOL BRIDGE; A8 round-counter diamond `RC{round<max?}`; B10 HUMAN CHECKPOINT diamond; `:::new` dashed class | `assets/mermaid-conventions.md` | **Handbook style guide** (cross-link to Genesis, layered approach); apply across **Ch08-Ch15** | The handbook today has *seven* simultaneous micro-styles; Genesis collapses these to one. Three handbook diagrams currently render UNBOUNDED LOOPs by construction (`ch12:445`, `ch13:17`, `ch14:454`); round-counter diamond fixes them. | IL |
| G11 | **Rejection-with-WHEN-clause discipline** — every pattern carries WHEN clause; selection produces audit trail of patterns *considered and rejected* | `examples/05-pr-review-verdict.md:8, 151-157`; `README.md:144` | **Ch10** (structural counterpart to PROSE) or **Ch13**, recurring callout in Ch12-Ch14 | TL signature move #2. Most under-marketed differentiator. Takes Daniel from "guy with frameworks" to "guy with engineering discipline". | TL (1b) |
| G12 | **"Markdown that steers an LLM is code"** one-liner | `SKILL.md:21-22` | **Ch08 opening** + **Ch15 closing** (bookend) | Already public anchor. Job is to *protect* from softening, not elevate. Note PA flags this aphoristic without cost-accounting evidence — see §7. | TL (1c), PA (downgrade) |
| G13 | **MODULE ENTRYPOINT description spec** (4 rules: imperative / intent-first / indirect-triggers / ≤1024 char hard cap) + **EVALS PLAN** (with_skill vs without_skill A/B; 20-trigger 60/40 split, ≥0.5 / <0.5) + **REAL-TASK REFINEMENT** | `SKILL.md:97-111, 288-298, 418-428` | **Ch09 §Skills** | Closes "what makes a good skill description?" (currently absent in Ch09). EVALS provides the "battle-tested or cut" gate Ch09-Ch14 don't ship. | PA, FR (G1) |
| G14 | **Primitive vs Module disambiguation block** — "PRIMITIVE: file the runtime loads. MODULE: unit of distribution + deps + version." | `primitives.md:245-252` | **Ch09 callout** | Two definitions, six lines, zero hand-waving. Independent of C1; helps either taxonomy. | CE (1b), FR |
| G15 | **Tool-call affordance is NOT a primitive type** + MCP correctly bounded as protocol surface only | `primitives.md:267-305` | **Ch09 callout** | Ends category-confusion any MCP-adjacent reader will hit. Prevents next reader's "is MCP a primitive?" question. | CE (1e), FR (G2) |
| G16 | **Four-tier pattern hierarchy** (Tier 0 substrate / Tier 1 affordances / Tier 2 design / Tier 3 architectural) — "Tier-1 loaded LAST" rule | `agents/genesis-architect.agent.md:354-402` | **Ch10 or Ch12 structural figure** + **Ch15** | Inherits credibility from GoF / POSA literature. Mechanism behind "primitives survive model change". Conference-talk diagram. | TL (1e) |
| G17 | **Persona vs thread (subagent) disambiguation** | `genesis-architect.agent.md:200-208` | **Ch09 callout** or **Ch12** | Central conceptual cleanup; handbook does not address it explicitly anywhere. Genesis owns it cleanly. | FR (G5) |

### G-MODERATE (one persona, but evidence supports)

| ID | Topic | Source | Chapter | Personas |
|---|---|---|---|---|
| G18 | **A2 PIPELINE** + STAGE COLLAPSE / INFINITE PLANNING / TASKS WITHOUT PLAN | `architectural-patterns.md:79-114` | Ch12 / Ch13 cross-link | PA |
| G19 | **A4 STAFFED PLAN** + GOD-PERSONA / INLINE-PERSONA | `architectural-patterns.md:158-197` | Ch12 | PA |
| G20 | **A9 step-7b PROBE** before manifest emission (PHANTOM DEPENDENCY at agent layer) | `SKILL.md:345-369` | Ch14 entry adjacent to Prompt Injection via Dependencies | PA |
| G21 | **PERSIST-and-RELOAD handoff packet** rule | `SKILL.md:300-307, 331-336` | Ch13 §Checkpoint Discipline | PA |
| G22 | **Synthesis-style table** (CONSENSUS / MAJORITY / DISSENT-WEIGHTED / CEO-ARBITRATED / FALL-THROUGH) | `pattern-tradeoffs.md:148-161` | Ch12 (names the fan-in shape Ch12 leaves unnamed) | CTO |
| G23 | **Gate-types 2x2** (internal/external × programmatic/judgement) | `pattern-tradeoffs.md:57-86` | Ch12 + Ch5 | CTO |
| G24 | **INLINE / LOCAL SIBLING / EXTERNAL MODULE** as Monday-runnable composition decision | `composition-substrate.md:84-105` | Ch09 (covered in G8 above; called out here as Monday-pickup item) | CE, DL |
| G25 | **"WHEN NOT TO APPLY" section convention** (every example carries one) | `examples/01-readme-iteration.md:210-219` and similar | Adopt as handbook-wide convention | DL (G5) |
| G26 | **BUNDLE LEAKAGE + DISPATCH CONTAMINATION** (carries its own evidence — APM scanner) | `composition-substrate.md:128-150` | Ch14 | CE (promotes 1 of 4 from §2 of own report); FR. Conflicts with TL — see §7. |
| G27 | **APM adapter delegates rather than duplicates** (substrate vs apm-usage) | `module-system-adapters/apm.md:13-20, 81-86` | Ch10 "Try It" callout cross-link | FR (G4, M2) |
| G28 | **agentskills.io citations URL-precise and bounded** (5 URLs, each scoped to surface) | `primitives.md:67-88` | N/A — Genesis-internal discipline; cite as model in handbook style guide | FR (G1) |

---

## Section 2 — Theory Without Evidence (consolidated)

| ID | Topic | Source | Verdict | Personas |
|---|---|---|---|---|
| T1 | **A3 ORCHESTRATOR-SAGA** with ANEMIC SAGA / IMPLICIT TRIGGER COUPLING | `architectural-patterns.md:117-154` | DOWNGRADE — "promising; no cited realization". Mark as architectural guidance only until a real saga ships. | PA |
| T2 | **A6 EVENT-DRIVEN as standalone pattern** | `architectural-patterns.md:244-287` | COLLAPSE INTO A10 — every cited realization is actually A10. Reference A6 only as parent shape. | PA |
| T3 | **A8 ALIGNMENT LOOP "typically 2-3 max" / N=3 empirical** | `architectural-patterns.md:373-374`; `examples/01-readme-iteration.md:124-141` | DOWNGRADE — call it calibration, not measurement. Mirror `ch12:317`'s honesty model ("15-20% as a starting hypothesis"). Reconcile with Ch14:216 retry-budget framing. | PA, DL (T2) |
| T4 | **A9 STRONG-FORM "use it whenever the trigger surface offers it"** | `architectural-patterns.md:445-451` | KEEP, FOOTNOTE — substrate-cost argument from `:596-603` belongs ABOVE the preference rule. | PA |
| T5 | **"Markdown that steers an LLM is code"** as discipline claim (slogan vs cost evidence) | `SKILL.md:21-24` | RETAIN-AS-POSITIONING (TL); DEMAND-EVIDENCE for cost-accounting (PA). See §7 — these are reconcilable: keep the slogan, add a cost-accounting sentence. | TL (Gold), PA (theory) |
| T6 | **"Diagrams before any natural-language module body"** as HARD RULE | `SKILL.md:38-39` | DOWNGRADE TO STRONG DEFAULT — exempt small primitives (single-file `.instructions.md`). Apply Genesis's own calibrate-per-scope wisdom upstream. | PA |
| T7 | **EVALS GATE 0.5 threshold** | `SKILL.md:296-298, 422-424` | KEEP, FLAG as untested threshold (structure is gold, the specific number is not derived). | PA |
| T8 | **BINDING MODES block** (AGENT-INVOKED vs SUBSTRATE-INVOKED) | `primitives.md:98-128` | DEMAND-EVIDENCE — dense theory, no worked example. Promote to Gold once example added. | CE (2a) |
| T9 | **4 composition anti-patterns** (DUPLICATED LEAF / HIDDEN EXTERNAL / UNPINNED CRITICAL DEP / TRANSITIVE BLOAT) — names crisp, war stories absent | `composition-substrate.md:111-117` | DEMAND-EVIDENCE — Ch14's voice runs on observed-in-the-wild incidents; ship as named-but-evidence-pending or wait for receipts. (BUNDLE LEAKAGE excepted — promoted to G26.) | CE (2b) |
| T10 | **agentskills.io authority block** (meta-citation discipline) | `primitives.md:42-58` | RETAIN-AS-INTERNAL; do NOT lift to handbook (it is editorial scaffolding, not chapter prose). | CE (2c) |
| T11 | **"Tool-agnostic substrate" framing** without cross-tool concordance | `composition-substrate.md:2-6` | DEMAND-EVIDENCE — needs a cross-tool concordance table (npm package.json ↔ APM apm.yml ↔ plugin.json ↔ Genesis vocabulary), or scope the claim. | CE (2d) |
| T12 | **Pattern-tradeoffs.md as a whole** — every matrix is normative-only, zero measurements | `pattern-tradeoffs.md` (file-wide) | DEMAND-EVIDENCE before any matrix becomes a normative handbook claim. Borrow PR #394 numbers from Ch12 where applicable. | CTO |
| T13 | **A10 itself ships without an incident-reduction or measured portability case** | `architectural-patterns.md:530-645` | DEMAND-EVIDENCE — at minimum one named incident strong-form A9 inside A10 would have prevented; alternatively, ship as "directional" in Ch15's three-tier honesty table. | CTO |
| T14 | **"Harness orthogonality" claim** | `architectural-patterns.md:592-594, 622-627` | DEMAND-EVIDENCE — needs a worked port across two harnesses with measured engineering cost; otherwise HARNESS-PORTABILITY THEATRE risks afflicting the doc itself. | CTO |
| T15 | **Examples 04 + 05 marketed as Monday-runnable bundles** | `examples/04-pr-review-advisory.md`, `05-pr-review-verdict.md` | REFRAME — these are reference *designs*, not reference *implementations*. Multi-day on fan-out harness; multi-week otherwise. | DL (T1) |
| T16 | **"Skill stops at step 6" as guaranteed property** | `examples/03/04/05` (each has variant) | DOWNGRADE — it is a *taught* property (skill prose), not enforced (no tool gate). Don't present as guarantee. | DL (T3) |
| T17 | **C6 EXTERNAL CORPUS GROUNDING with bounded scope** as discipline alone | `examples/01-readme-iteration.md:166-178` | DEMAND-EVIDENCE — needs an AUTHORITY-OVERREACH reviewer in the panel for mechanical enforcement. | DL (T4) |
| T18 | **PROSE citation goes to personal blog, not Ch10** | `primitives.md:230-231` | CUT-AND-REPLACE — replace with citation to Ch10 (canonical now). Keep blog URL only as secondary provenance marker. | FR (T1) |
| T19 | **APM canonical anatomy URL** points to `danielmeppiel.github.io/awd-cli/...` while text says "ships in microsoft/apm" | `module-system-adapters/apm.md:32-38` | DEMAND-VERIFICATION — confirm or update URL to microsoft/apm canonical location. | FR (T2) |
| T20 | **Second-order claim about agentskills.io** ("conflates container surface with agent's whole behavior") asserted without quote | `primitives.md:53-58`; `genesis-architect.agent.md:213-216` | DEMAND-EVIDENCE — quote one URL, or soften to omission claim. | FR (T3) |
| T21 | **Ch15 footnote `ch15-squad`** dated March 2026 (forward-dated) | `ch15:187` | HANDBOOK-SIDE FACT-CHECK — out of Genesis scope but flagged because Genesis depends on the convergence story. | FR (T4) |
| T22 | **Full 8-step process diagram in handbook narrative** | `SKILL.md:52-83` | DEMOTE-TO-APPENDIX — use the *outputs* (handoff packet, plan persistence) as narrative; demote step list to reference sidebar. | TL |
| T23 | **Module-system-adapter discussion in handbook** | `genesis-architect.agent.md:418-435` | RETAIN-AS-CONCEPT, DROP THE HANDLE — would read as APM marketing-by-proxy and undermine "platform without being platformed" stance. | TL |

---

## Section 3 — Monday-ready (consolidated)

| Technique | Endorsing personas | Best target chapter | Monday verdict | Setup cost | Note |
|---|---|---|---|---|---|
| R1-R4 refactor verbs (audit `.github/instructions/*.md`, every `SKILL.md`) | DL, PA, CE | Ch14, Ch09 | **Y** | 30 min read + 2 hr first-pass | Highest Monday yield in corpus. Ch14 #10 currently lacks the verbs. |
| 4-rule MODULE ENTRYPOINT description checklist | PA, FR | Ch09 §Skills | **Y** | 5 min/skill | Pure checklist. Falsifiable. |
| A1 PANEL anti-pattern audit (3 checks against any review primitive) | PA, TL | Ch12 | **Y** | 0 — re-read your last review skill | Likely catches at least one. |
| A5 WAVE gating discipline (named anti-patterns checklist) | PA, DL | Ch14 | **Y** | 0 — formalizes existing intuition | Already partially in Ch13. |
| A7 COLD READER as review discipline (fresh session, artifact-only) | PA, DL, IL | Ch12 / Ch14 | **Y** | 15 min team decision | No tooling. Mandatory for cold-traffic surfaces. |
| EVALS PLAN trigger split (16-20 queries, 60/40) | PA, FR | Ch09 | **Y** | 30-60 min/skill | Zero infra beyond harness. |
| EVALS PLAN with/without_skill A/B | PA | Ch09 | **Partial** | 1-2 hr/skill | Wiring is harness-dependent. |
| A9 PROBE before manifest emission | PA | Ch14 | **Y** | 0 — add one tool-call step | Stops PHANTOM DEPENDENCY at zero cost. |
| PERSIST-and-RELOAD handoff packet | PA | Ch13 | **Y** | 0 | Reload-before-each-spawn is the only addition. |
| REAL-TASK REFINEMENT (run skill on real task; revise from trace) | PA | Ch09 / Ch13 | **Y** | 1 task cycle | Universal. |
| INLINE / LOCAL SIBLING / EXTERNAL MODULE composition decision (audit each `.skills/*`) | DL, CE | Ch09 | **Y** | 1-2 hr | APM users get manifest assist; non-APM users discover phantom-dep set in afternoon. |
| Example 03 single-skill release-notes draft | DL | Ch09 | **Y** | 1/2 day | Lone "no harness required" full worked example. `git`+`jq`+`bash`. |
| Examples 01/02/04/05 (multi-agent worked) | DL | Ch12 | **Concept-Y / Impl-N** | 2-4 hr on fan-out harness; blocked otherwise | Needs CHILD-THREAD SPAWN harness; otherwise reproduces PANEL-IN-ONE-CONTEXT. |
| W6 facts-and-side-effects table (per-skill audit) | DL | Ch09 / Ch13 | **Y** | 1 hr/skill | Universal. No harness gate. |
| "WHEN NOT TO APPLY" section convention | DL | Style guide | **Y** | Free | Prevents most common consultant-grade misapplication. |
| 6 CTO slides (governance substrate / weak-vs-strong / vendor cost / governance-washing / synthesis modes / gate-types 2x2) | CTO | Ch5 / Ch12 / Ch15 | **Y** | 1-2 hr deck assembly | Two slides (substrate property + vendor cost) carry the deck. |
| Mermaid Monday list — replace `\n` with `<br/>` (ch08), `graph TD`→`flowchart TD` (ch10:392), strip emoji (ch11:64-68), add round-counter to ch12:445 + ch13:17, B10 diamonds at ch12:142+461, cylinder + `==>` pass across ch12+ch13 | IL | Ch08-Ch15 | **Y** | 5 min - 30 min/diagram | One-day sweep delivers cross-chapter consistency. |
| Drop-in callouts: Primitive-vs-Module / PROSE-axis table / "tool-call affordance not a primitive" / 3 composition modes / BUNDLE LEAKAGE entry | CE, FR | Ch09 / Ch10 | **Y** | 5-15 min each | Five copy-paste insertions. Trivial editorial risk. |
| ATTENTION ANCHOR as conference-talk concept | TL | Ch11 | **Y** | 0 | Plant-the-flag window is open. |
| Bounded-rounds N=3 as **rule of thumb** (not empirical claim) | DL | Ch12 / Ch13 | **Y** | 0 | Use it; flag as taught discipline. |

---

## Section 4 — Reconciliation Required (canonical conflicts)

The author's longest stop. Lead conflict first; subsequent ordered by downstream blast radius.

### **C1 — Six runtime-role primitives vs Seven file-extension primitives** [LEAD; CANONICAL]

**Genesis** (`assets/primitives.md:1-3`):
> "# TIER 0 -- Substrate primitives. The six concepts every agent harness implements under different folder names and frontmatter dialects. Genesis names them once so the vocabulary outlives any one tool."
> Six: PERSONA SCOPING FILE, MODULE ENTRYPOINT, SCOPE-ATTACHED RULE FILE, CHILD-THREAD SPAWN, TRIGGER ORCHESTRATOR, PLAN PERSISTENCE.

**Handbook** (`ch09-the-instrumented-codebase.qmd:7, :23-25`):
> "It defines seven primitive types... Seven categories cover the full range of knowledge an agent needs."
> Seven: Instructions, Agents, Skills, Prompts, Memory, Orchestration, Hooks.

**Severity:** CANONICAL. The cuts run on different axes (runtime role vs file-extension × use-case); 6+7 ≠ 13 (most would be aliases).

**Persona positions:**
- **PA:** "the **handbook vocabulary wins** because (a) the handbook is the user-facing artifact, (b) Genesis vocabulary is internal-architect language that adds learning tax, (c) [the audit-practitioner concluded] handbook is too tightly coupled to Copilot CLI — solution is universal in handbook vocabulary." Genesis keeps the 6 internally; published artifacts translate.
- **CE:** "Real pick is between Shape A and Shape B. Shape C is the worst from a Chief Editor seat (highest bloat, weakest voice) and I would advise against it. Depends on how much commercial positioning depends on the 'seven' framing — that is a CEO + Publishing Advisor call, not mine."
- **TL:** "published narrative cannot use both numbers without the reader concluding the author has not made up his mind. Whichever the canonical answer is, the *other one* must be silently retired in published material... pick one, stick to it across all surfaces, and update LinkedIn / README / handbook in the same release."
- **FR:** "not logically contradictory — same SKILL.md file can host a Ch09 'decision framework' while being a Genesis 'MODULE ENTRYPOINT.' But taxonomically incompatible — each side claims a complete enumeration." Whichever ships, the cross-reference seam needs an explicit one-line mapping.
- **IL:** From a visual angle, Genesis names 5 shapes; the handbook adds Hooks (no shape) and conflates Prompts/Orchestration. Adopting Genesis surfaces a real gap in Genesis's own catalogue — bidirectional fix.
- **DL, CTO:** No explicit position; both rely on the resolution.

**Decision shapes** (CE's framing, panel-endorsed):
- **Shape A — Publish six as canonical; footnote seven as the file-shape view.** Ch09 retitled "The Six Substrate Primitives", Genesis names as headers, "Industry terms: instruction file, rule, AGENTS.md, skill, plugin..." opens each. Current seven-block fig becomes appendix. **Cost:** rewrite headers + intro; preserve body content. **Voice cost:** loses one-word friendliness; gains runtime-role coherence.
- **Shape B — Publish seven as canonical; footnote six as the runtime-role view.** Ch09 stays structurally; new section "An architect's view: six runtime roles" introduces Genesis taxonomy as internal reference. Mapping table supplied. **Cost:** ~50 lines added; permanent two-vocabulary world.
- **Shape C — Hybrid merged list (~7-8 entries, both names per entry).** Highest editorial cost, highest bloat, weakest voice. **Panel consensus: avoid.**

**Editorial recommendation:** **Shape A**. Rationale: PA, TL, IL, CE all converge that one vocabulary must win publicly; PA's "handbook wins because user-facing" *and* TL's "Genesis is the positioning multiplier" reconcile under Shape A *if* Genesis names are kept verbatim (TL §4a voice rule) — the handbook absorbs Genesis's vocabulary into Ch09 and gets the runtime-role coherence. Shape A also resolves C3 and C4 cleanly (see below). The tradeoff is the one-word friendliness; mitigated by opening every section with "Industry terms: ..." Defer final pick to author given commercial-positioning weight.

**Downstream impact:**
- **Shape A:** Ch09 (rewrite headers, preserve body, add 7-block fig as appendix); Ch12 anti-pattern names align with Genesis A1-A10; Ch14 absorbs source-time anti-patterns under Genesis vocabulary; Ch15:17 commits to substrate-field vocabulary. C3, C4, C7, C8 cascade-resolve. Genesis assets ship without translation footnotes.
- **Shape B:** Ch09 unchanged + 50-line section; every Genesis-derived passage in Ch12-Ch15 carries a translation footnote; C3 / C4 stay open as separate decisions; affinity matrix's 7 open questions stay live longer.

**Hard constraint regardless of shape:** the Memory ↔ PLAN PERSISTENCE scope mismatch (C4) MUST be addressed (CE: "both names refer to non-coextensive concepts; whichever taxonomy ships, both bins need to exist or one needs an explicit footnote").

---

### **C2 — agentskills.io / "skill = container" vs Ch09 "skills = decision frameworks"** [CANONICAL, downstream of C1]

**Genesis** (`primitives.md:32-44`): "MODULE ENTRYPOINT... INDUSTRY TERMS: 'skill' (agentskills.io), 'plugin', 'command bundle'." — skill is a *container*.

**Handbook** (`ch09:121-123`): "Skills... package reusable decision frameworks... A skill is more than a set of rules; it teaches an agent how to think about a specific domain." — skill is a *content shape*.

**Severity:** CANONICAL (FR: "not logically contradictory but taxonomically incompatible"). Surfaces in every reference to "Skills".

**Persona positions:**
- **FR (R2):** Compatible-reading: Ch09's Skill is *content* authored *inside* Genesis's MODULE ENTRYPOINT *container*. Recommend explicit one-line mapping at every cross-reference seam.
- **PA (R5):** Recommend Ch09 absorbs the four-rule + 1024-cap description spec; OR Genesis stops claiming agentskills.io is "load-bearing authority" and surfaces the rules itself. From practitioner lens, the four rules belong in Ch09.
- **CE:** Implicit in C1 framing — under Shape A this resolves; under Shape B it stays a one-sentence cross-reference.

**Decision shapes:**
- **Shape A:** (Auto-resolved by C1 Shape A) Ch09 §MODULE ENTRYPOINT replaces §Skills; "skill" becomes an industry term.
- **Shape B:** Ch09 §Skills adds one-line note: "the SKILL.md file is the canonical container surface for any reusable, dispatcher-discoverable capability — see Genesis primitives.md:32-58 for container-vs-content distinction. Decision-framework framing here describes one common kind of *content* an instrumented codebase puts inside that container." (FR M4, exact wording.)
- **Shape C:** Drop "Skills" as a primitive type entirely; introduce as a concept under MODULE ENTRYPOINT. (Tied to Shape A of C1.)

**Editorial recommendation:** Shape A if C1 lands as A; Shape B otherwise.

---

### **C3 — Hooks vs TRIGGER ORCHESTRATOR (substrate fields)** [CANONICAL, downstream of C1, gates Ch15]

**Handbook** (`ch09:294-298`): "Hooks... bridge the gap between passive context and active behavior."

**Genesis** (`primitives.md` §5): "TRIGGER ORCHESTRATOR... A declarative pipeline that spawns sessions in response to events... Lives ABOVE the thread, deciding when work begins and what initial context it carries." With substrate fields SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE that A9 / A10 depend on.

**Severity:** CANONICAL (scope mismatch). Ch15:17 already cites gh-aw positively (Genesis's A10 canonical realization).

**Persona positions:**
- **CE (4c):** Under Shape A of C1, Hooks → TRIGGER ORCHESTRATOR with substrate fields as sub-list. Under Shape B, ch09 §Hooks needs +1 paragraph.
- **CTO (4.1):** This is the *central gap*. Ch15 predicts governance as a future category and says "tooling barely exists" but A10 names one canonical realization shipping today. **Either Ch15's "barely exists" is correct and A10's CANONICAL REALIZATION is overstated, OR A10 is correct and Ch15 should commit to substrate-field vocabulary.** "Without that vocabulary the prediction is unfalsifiable."
- **IL (4d):** Hooks has no Genesis shape; bidirectional fix needed (propose trapezoid `[\..\]` for HOOK shape).

**Decision shapes:**
- **Shape A — Adopt substrate-fields vocabulary in Ch15:23.** Rewrite to name SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE as the three properties the predicted category will be measured against; cite gh-aw safe-outputs as existing-today reference implementation. Cost: Ch15 commits to vocabulary owned by external corpus. Benefit: prediction becomes falsifiable.
- **Shape B — Ch15 stays vendor-neutral and category-only.** Add a footnote that Genesis's substrate-field model is one candidate vocabulary the category may consolidate around. Lower commitment; weaker prediction.
- **Shape C — Defer Ch15 governance prediction entirely** until receipts arrive. (Not endorsed by any persona.)

**Editorial recommendation:** **Shape A**. CTO's verdict: "the prediction is too vague to act on; either ship the vocabulary or footnote it" — and the panel has converged on the vocabulary's quality (G1 is unanimous Gold).

**Downstream impact:** Ch15 deep-dive cannot dispatch until this is resolved. Ch14 absorbs the 6 A10-tier governance anti-patterns (G1).

---

### **C4 — Memory vs PLAN PERSISTENCE** [EMPHASIS, must resolve as part of C1]

**Handbook** (`ch09:217-247`): Memory = cross-session knowledge accumulation.
**Genesis** (`primitives.md` §6): PLAN PERSISTENCE = active plan + todos + checkpoints across turns and spawns.

**Severity:** EMPHASIS but **non-coextensive**.

**Persona positions:**
- **CE:** Hard constraint — both bins must exist or one needs explicit footnote that it includes the other.
- **PA, DL:** Implicit — both rely on PLAN PERSISTENCE for persist-and-reload (G21).

**Decision shapes:**
- **Shape A — Two distinct primitives** (PLAN PERSISTENCE + MEMORY/cross-session). Cleanest under C1 Shape A.
- **Shape B — One Memory primitive with two sub-types** explicitly named (active-plan vs cross-session). Compatible with C1 Shape B.
- **Shape C — Treat PLAN PERSISTENCE as runtime affordance, not primitive type.** (Reduces from 6 to 5 in Genesis; rejected by Genesis itself.)

**Editorial recommendation:** Shape A. Two-bin split is cheap (matrix open question #4).

---

### **C5 — Run-time vs source-time anti-pattern catalogues** [OMISSION, mutual; largest integration opportunity]

**Severity:** OMISSION (mutual). Affinity-matrix C6.

**Persona positions:**
- **PA, DL (R5), CTO (4.2):** Genesis distributes 35-50 named anti-patterns across 7 files; Ch14 has 19 run-time entries. Sets are largely disjoint. DL: "Ch14 currently presents itself as the *complete* anti-pattern catalogue for AI-native development, and a Monday dev lead will treat it as such."
- **TL:** Cautions against bloating Ch14 narrative with packaging anti-patterns aimed at agent-platform-authors (wrong audience).

**Decision shapes:**
- **Shape A — Ch14 absorbs the source-time set wholesale** (~doubles in length). Genesis becomes secondary reference.
- **Shape B — Ch14 absorbs only practitioner-grade entries** (R1-R4 verbs as sidebar, BUNDLE LEAKAGE, A5 wave anti-patterns, Trust-Fall ↔ VERIFY-WITH-LLM-ONLY cross-link, Token-Laundering, Inner-Loop-Miscast); Genesis remains canonical for source-time / packaging. Ch14 grows ~30%, not 100%.
- **Shape C — Split Ch14 into Ch14a (run-time) / Ch14b (source-time and packaging).**

**Editorial recommendation:** **Shape B**. Reconciles DL's "treats Ch14 as complete" concern with TL's "wrong audience for packaging anti-patterns" concern. R1-R4 verbs are non-negotiable (G2). 6 governance anti-patterns also in (G1). PHANTOM DEPENDENCY / BUNDLE LEAKAGE depends on §7 disagreement.

---

### **C6 — PHANTOM DEPENDENCY / BUNDLE LEAKAGE in Ch14** [OMISSION; panel disagreement — see §7]

**Source:** `composition-substrate.md:128-150`. Affinity matrix C7.

**Persona positions:**
- **CE (1f, promoting from §2):** BUNDLE LEAKAGE *does* carry its evidence (cites APM scanner; names DISPATCH CONTAMINATION). Closer to Gold. Promote.
- **DL (R2, R5), PA, FR (G4):** Operational, real, observed. Belongs in Ch14.
- **TL (§2):** "Excellent operational material. Wrong audience for narrative space — these speak to the agent-platform-author, not the practitioner reading the handbook." Reference in footnotes.

**Decision shapes:**
- **Shape A — Full Ch14 entries** (CE, DL, PA, FR position).
- **Shape B — Footnotes / appendix entries** (TL position).
- **Shape C — Split: BUNDLE LEAKAGE + DISPATCH CONTAMINATION as Ch14 entry (war-storied via APM scanner); the four un-evidenced ones (DUPLICATED LEAF / HIDDEN EXTERNAL / UNPINNED CRITICAL DEP / TRANSITIVE BLOAT) as footnote until evidence ships.**

**Editorial recommendation:** **Shape C**. Reconciles all positions: TL's "wrong audience" applies to the un-evidenced four; CE's "carries its evidence" applies to BUNDLE LEAKAGE; T9 from §2 already DEMAND-EVIDENCE on the un-evidenced four.

---

### **C7 — A1 PANEL vs Domain Teams / Writer-Reviewer-Tester** [TERMINOLOGY]

Genesis A1 PANEL (`architectural-patterns.md:33-76`) ↔ Handbook §Pattern 1 / §Pattern 2 (`ch12:53-130`). Affinity matrix C8.

**Persona positions:**
- **PA:** Handbook names carry more semantic content; keep handbook names, Genesis cites them as A1 realizations.
- **TL §4a:** Names verbatim — A1 PANEL stays A1 PANEL.
- **CE, IL:** Implicit — cross-reference in either direction works.

**Decision shapes:**
- **Shape A — Keep handbook names; Genesis cites as A1 realization.** PA position.
- **Shape B — Adopt A1 PANEL as canonical; Writer-Reviewer-Tester as one realization.** TL position.
- **Shape C — Both, side by side, with explicit mapping.** CE prose-shape.

**Editorial recommendation:** **Shape C** with TL's verbatim-name rule. Ch12 §Pattern 1 retains "Writer/Reviewer/Tester" header but introduces "(architecturally: the A1 PANEL pattern — see Genesis architectural-patterns.md)" as the second sentence. Reconciles signature-naming with semantic clarity.

---

### **C8 — Voice register: Genesis is brutal, handbook is bookish** [EMPHASIS, house-style]

**Persona position (TL §4a):** "Names verbatim, surrounding prose in handbook register." Four-rule integration policy:
1. Named patterns keep Genesis-register names verbatim (ALL CAPS, two-three words, no smoothing).
2. Surrounding prose is handbook register, not Genesis.
3. Each named pattern gets one verbatim Genesis-style definition box (callout, monospace).
4. No buzzword translation (HAND-ROLLED HALLUCINATION stays HAND-ROLLED HALLUCINATION).

**Cross-validation:** CE implicitly endorses (1b, 1f Gold items keep Genesis vocabulary); PA neutral; DL neutral.

**Decision shape:** Adopt as house style. **Editorial recommendation:** ADOPT. This is the load-bearing constraint that lets Shape A of C1 and C2 land without diluting the positioning multiplier.

---

### **C9 — Bounded rounds N=3 (calibration vocabulary)** [TERMINOLOGY / EMPHASIS]

Genesis (`architectural-patterns.md:373`; `examples/01:130-132`): N=3 max, "empirically".
Handbook (`ch14:216`): "After two failed dispatches... change the approach."

**Persona positions:** PA, DL, TL all flag — same operational rule, different anchor; "empirically" not cited.

**Decision shapes:**
- **Shape A — Adopt handbook's "two failed dispatches" wording in Genesis;** state honestly as calibration not measurement (`ch12:317` honesty model).
- **Shape B — Genesis keeps N=3 with footnote "calibration based on observed runs; not measured benchmark";** handbook cross-references.

**Editorial recommendation:** Shape A. PA: "either way, state honestly that the threshold is calibration, not measurement."

---

### **C10 — Ch15:17 four-vendor convergence claim** [FACT-CHECK, handbook-side]

Forward-dated `ch15-squad` footnote (March 2026) per FR (T4 / T21). Out of Genesis scope but flagged because Genesis's apm.md is the case-study evidence under the convergence claim.

**Editorial recommendation:** Hand to handbook fact-check pass. Genesis should not anchor architectural claims on the four-way convergence until Ch15's footnote firms up.

---

### Conflicts ALIGNMENT-CONFIRMED (no action)

- **C5 (PROSE):** Letter-for-letter aligned. Single fix: T18 (replace blog cite with Ch10 cite).
- **C9 affinity (Wave Execution):** Aligned; absorb Genesis's two anti-patterns into Ch14 (G4).
- **C10 affinity (Architect-Reviewer-Escalation roles):** Aligned. No action.

---

## Section 5 — Per-chapter integration proposals

| Chapter | Items routed | Estimated impact | C-conflict dependencies | Round-2 deep-dive? |
|---|---|---|---|---|
| **Ch08 Practitioner's Mindset** | G12 (markdown-is-code as opener bookend) | Light edit | None | No — bookend only |
| **Ch09 Instrumented Codebase** | G2 (R1-R4 sidebar), G8 (composition vocabulary new sub-section), G13 (description spec + EVALS), G14 (Primitive vs Module callout), G15 (tool-call affordance callout), G17 (persona vs thread), G24 (composition decision Monday item), G27 (APM adapter cross-link), the seven-block fig becomes appendix or chapter spine becomes Genesis names | **Chapter-spine rewrite under C1 Shape A; new sub-section + 5 callouts under Shape B** | **C1 (gates everything), C2, C3, C4** | **YES — primary deep-dive candidate** |
| **Ch10 PROSE Specification** | G9 (PROSE-axis mapping), G11 (rejection-with-WHEN as structural counterpart), G16 (four-tier hierarchy figure), T18 (replace blog cite) | New sub-section + table + figure | None (PROSE alignment confirmed) | YES — for G11 absorption |
| **Ch11 Context Engineering** | G7 (ATTENTION ANCHOR as chapter spine), G9 (PROSE-axis bridge alternative), IL Monday items (emoji strip, font fixes) | **Chapter-spine candidate for G7** | None | **YES — G7 deep-dive** |
| **Ch12 Multi-Agent Orchestration** | G3 (A1 PANEL + 3 anti-patterns), G6 (A7 COLD READER), G18 (A2 PIPELINE), G19 (A4 STAFFED PLAN), G22 (synthesis-style table), G23 (gate-types 2x2), Mermaid round-counter + cylinder + `==>` pass | New sub-section + table + diagram redraws | **C7 (PANEL naming)** | YES — for new sub-section + diagrams |
| **Ch13 Execution Meta-Process** | G4 (Wave anti-patterns cross-link), G21 (PERSIST-and-RELOAD), G11 (recurring callout), G6 (A7 in checkpoint discipline), Mermaid round-counter on five-phase loop | Light edits + cross-links | C9 (mild) | No — light edits only |
| **Ch14 Anti-Patterns** | G2 (R1-R4 as primary), G4 (Wave anti-patterns), G5 (PLAN-AND-PRAY/VERIFY-WITH-LLM-ONLY cross-linked from #7 Trust Fall), G20 (PHANTOM DEPENDENCY / A9 PROBE entry), G26 (BUNDLE LEAKAGE + DISPATCH CONTAMINATION entry), 6 A10 governance anti-patterns from G1 (TOKEN-LAUNDERING etc.), AUTHORITY-OVERREACH (T17 → new entry), Genesis's GOD MODULE / HIDDEN COUPLING / STUB ORCHESTRATION cross-references | **Chapter ~30-50% growth under C5 Shape B; ~100% under Shape A** | **C5 (governs growth), C6 (governs which packaging anti-patterns enter), C1 (governs vocabulary)** | **YES — primary deep-dive candidate** |
| **Ch15 What Comes Next** | G1 (A10 substrate-cost argument), G16 (four-tier hierarchy), TL §4e (cite Genesis as mechanism behind "survives tool change" thesis), FR M3 (footnote A10 as architecture under convergence claim), G12 (markdown-is-code closing bookend), C10 fact-check on `ch15-squad` | New paragraph(s) under §:23 governance prediction; closing bookend | **C3 (substrate-field vocabulary commit gates the rewrite)** | **YES — gated by C3 resolution** |

---

## Section 6 — Author A4 gate checklist

Tight numbered decisions. Each: question, recommended answer, downstream consequence.

1. **C1 — Six-vs-seven primitive taxonomy. Pick Shape A, Shape B, or Shape C.**
   - Recommended: **Shape A** (publish six as canonical; Genesis names as Ch09 headers; current seven-block fig as appendix; "Industry terms:" lead-in to each section).
   - Downstream: Ch09 spine rewrite; Ch12-Ch15 use Genesis vocabulary; C2/C3/C4 cascade-resolve. Without this decision, Ch09, Ch12, Ch14, Ch15 deep-dives cannot dispatch.

2. **C3 — Ch15:23 governance prediction. Adopt SANDBOXING/CAPABILITY_GATING/AUDIT_SURFACE vocabulary, footnote it, or defer?**
   - Recommended: **Adopt** (Shape A). Cite gh-aw safe-outputs as existing-today reference implementation.
   - Downstream: Ch15 prediction becomes falsifiable; commits the handbook to a vocabulary owned by Genesis. If deferred, Ch15 deep-dive blocked.

3. **C4 — Memory vs PLAN PERSISTENCE. Two primitives, one with sub-types, or a footnote?**
   - Recommended: **Two distinct primitives** (Shape A). Cheap split.
   - Downstream: Ch09 §Memory bifurcates; B8 ATTENTION ANCHOR in G7 has a named home; Ch13's checkpoint discipline has a primitive to anchor on.

4. **C5 — Ch14 anti-pattern absorption. Wholesale, partial, or split chapter?**
   - Recommended: **Shape B (partial)** — absorb practitioner-grade entries (R1-R4 verbs, Wave anti-patterns, Trust-Fall cross-link, Token-Laundering, Inner-Loop-Miscast); Genesis remains canonical for source-time / packaging detail.
   - Downstream: Ch14 grows ~30%; Genesis assets ship as referenced authority for the rest.

5. **C6 — PHANTOM DEPENDENCY / BUNDLE LEAKAGE entry. Full Ch14 entries, footnotes, or split?**
   - Recommended: **Shape C (split)** — BUNDLE LEAKAGE + DISPATCH CONTAMINATION as full entry (war-storied); other four as footnote until evidence ships (T9).
   - Downstream: Ch14 absorbs one entry now; four entries pending Round 2 evidence collection.

6. **C7 — A1 PANEL vs Writer/Reviewer/Tester naming.**
   - Recommended: **Shape C** — keep handbook names as headers, introduce "(architecturally: A1 PANEL — see Genesis)" as second sentence.
   - Downstream: TL voice rule §4a satisfied; PA's semantic-content concern satisfied.

7. **C8 — Voice rule (TL §4a). Adopt as house style?**
   - Recommended: **Adopt** (named patterns verbatim ALL CAPS; surrounding prose in handbook register; one verbatim definition box per pattern; no buzzword translation).
   - Downstream: Every Genesis-derived passage in Ch08-Ch15 follows this rule. Without this rule, Shape A of C1/C2 risks diluting positioning into bookish prose.

8. **C9 — Bounded-rounds N. Adopt handbook's "two failed dispatches" or keep N=3?**
   - Recommended: **Adopt handbook wording in Genesis**; state as calibration not measurement (mirror `ch12:317`).
   - Downstream: T3 closes; reader sees one consistent threshold across both corpora.

9. **8-step design process scope (T6 from Practitioner / T22 from TL).**
   - Recommended: **Scope hard-rule "diagrams first" to cross-cutting redesigns and new SKILL/ORCHESTRATOR primitives only**; exempt single-file `.instructions.md` and short scope-attached rule files. In handbook narrative, demote step list to appendix; surface outputs (handoff packet, plan persistence) in narrative.
   - Downstream: Ch13 covers the discipline at code layer; Ch09 references Genesis for primitive-design layer with the exemption noted.

10. **PROSE citation cleanup (T18).**
    - Recommended: **Replace** `primitives.md:230-231` blog cite with Ch10 cite (keep blog as secondary provenance).
    - Downstream: 1-line edit. Resolves C5 cleanly.

11. **APM URL verification (T19).**
    - Recommended: **Verify** `danielmeppiel.github.io/awd-cli/.../anatomy-of-an-apm-package/` is still canonical, or update to microsoft/apm location.
    - Downstream: 30-second check; potential 1-line edit.

12. **Mermaid conventions adoption.**
    - Recommended: **Cross-link to Genesis spec; do not absorb as appendix.** Ship a 200-word `CONTRIBUTING-diagrams.md` with handbook-specific overlays (Quarto wrapper, 12-node ceiling, `pie/gantt/block-beta` permitted for chart types, no emoji).
    - Downstream: One-day mermaid sweep across Ch08-Ch15 applies §3 Monday-ready diagram items; ongoing diagrams inherit consistency.

13. **Hooks shape gap (IL §4d).**
    - Recommended: **Bidirectional fix** — propose trapezoid `[\..\]` for HOOK shape; disambiguate PROMPT vs ORCHESTRATION (currently both use `{..}`).
    - Downstream: Update Genesis `mermaid-conventions.md` § (one round-trip with Genesis maintainer); handbook gets full coverage.

14. **Ch15 `ch15-squad` footnote forward-date (T21).**
    - Recommended: **Confirm publication or replace** with verifiable cite.
    - Downstream: Strengthens four-vendor convergence claim. Out of Genesis scope strictly but Genesis's apm.md depends on it.

---

## Section 7 — New things only synthesis surfaces

Items only visible from cross-persona reading; no single persona caught these.

- **PHANTOM DEPENDENCY / BUNDLE LEAKAGE conflict between CE/PA/DL Gold and TL Theory.** Three personas (CE 1f, FR G4, DL R2) treat these as Gold for Ch14; TL §2 explicitly demotes them as "wrong audience for narrative space". The split runs along audience lines (operator-engineer vs trade-book reader). **Resolution shape C in C6** above bridges this. Surface for the author: this is the *only* Gold/Theory conflict in the corpus; the rest of the panel converges.

- **The "markdown is code" slogan vs cost evidence tension.** TL ranks G12 as Daniel's strongest one-liner ("must protect from softening"). PA ranks the same line as Theory ("aphoristic; no measurement of cost/benefit"). These reconcile if the line keeps its position as an aphoristic positioning anchor while the *handbook prose around it* adds one cost-accounting sentence (echo Ch13:225's "~10 minutes vs hours" model). Author A4 task: don't pick one persona; deliver both.

- **Genesis vs handbook on `examples/04` and `examples/05` framing.** DL says reference *designs* not *implementations* (T15). TL §1 ranks the examples as evidence-led positioning. Reconciliation: TL is correct that the examples are *evidence of the discipline* (shows the cold-load runs producing different justified architectures); DL is correct that they are not Monday-shippable bundles. Frame in handbook as "exemplars of cold-load runs", not as templates to deploy.

- **Genesis's 8-step process never measures itself with its own EVALS gate (PA §1 MODERATE).** PA observes that Genesis demands a `with_skill` vs `without_skill` delta of every primitive but does not run that gate on Genesis itself. This is a self-applied-evidence gap that strengthens the recommendation in checklist item #9 (scope the discipline; exempt small primitives; demonstrate cost-pays-for-itself on cross-cutting redesigns).

- **"Hooks lacks a mermaid shape" + "TRIGGER ORCHESTRATOR is the substrate" combine to a bidirectional Genesis improvement.** IL surfaced the shape gap; CE/CTO/PA surfaced the substrate-fields gap. Together: Genesis should add (a) a HOOK shape and (b) a PROMPT vs ORCHESTRATION disambiguation; handbook should adopt both. This is round-trip work with Genesis maintainer, not a one-way absorption.

- **PA's R1 (vocabulary canonical conflict — affects every Tier-3 pattern row) and CE's C1 framing converge on Shape A's *editorial cost* being lower than the panel realizes.** Both note the body content of Ch09 already describes the same things under file-extension headers; only the headers + intro need rewriting to land Shape A. This is the cheapest path the panel did not explicitly state.

- **The R1-R4 refactor verbs are the highest-Monday-yield item AND the cheapest Ch14 absorption.** DL's G1 is a chapter-changing finding; PA endorses it; CE 1f gives the supporting composition vocabulary. No persona objects. This is the safest first-deliverable for Round 2.

- **Ch15:17 already cites gh-aw positively but does not reuse it under :23 governance prediction (CTO's central gap).** This is the silent borrowing FR worries about, surfaced from a different angle. The prediction looks vendor-neutral but the substrate it implies is named in only one corpus. Decision #2 in §6 closes this.

---

End of synthesis.

/Users/danielmeppiel/Repos/genesis-skill/WIP/round-1/SYNTHESIS.md
