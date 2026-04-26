# Ch13 — Integration draft (architect's 8-step process scoped + plan-persistence anchor)

> Scope: round-2 deep-dive for `handbook/ch13-the-execution-meta-process.qmd`.
> Binding decisions: AUTHOR-DECISIONS.md #9 (8-step scope), C4 (PLAN
> PERSISTENCE primitive), C8 (voice rule — pattern names verbatim ALL-CAPS).
> Source: `genesis-skill/skills/genesis/SKILL.md`,
> `assets/primitives.md`, `assets/refactor-patterns.md`.

---

## 1. Integration thesis

Ch13 today describes a five-phase **execution loop** for code change:
AUDIT → PLAN → WAVE → VALIDATE → SHIP, with an ADAPT loop folded back
to PLAN. This is the right shape, and the chapter does not need a
re-architecture. What it needs is to seat itself correctly relative to
the layer immediately above it.

Genesis's 8-step process is **the design layer for primitives** —
SKILLs, ORCHESTRATORs, persona scoping files, scope-attached rule
files — which are themselves the inputs Ch13's loop consumes. Ch13's
agents do not invent their own personas mid-wave; they load primitives
that were designed earlier. When those primitives were designed
casually (no diagrams, no SoC pass, no compliance check), the
execution loop pays the cost in escalations, ADAPT loop fires, and
mid-wave context exhaustion.

The boundary between the two layers is the **handoff packet** — the
artifact Genesis emits at step 6 ("DESIGN ENDS HERE. Stop."). The
handoff packet is persisted via PLAN PERSISTENCE and reloaded by the
caller thread that draft modules at step 7b. That same persistence
discipline is what Ch13's checkpoint discipline already uses
implicitly between waves; naming the primitive (PLAN PERSISTENCE,
per AUTHOR-DECISIONS C4) lets Ch13 cite a primitive instead of
re-deriving the discipline.

The integration move, then, is two-part and surgical:

1. Add a short **layering frame** at the top of Ch13 explaining the
   design / execution split and naming the handoff packet as the
   boundary artifact. This stops readers from mis-reading the 8-step
   process as a competing methodology.
2. Anchor Ch13's existing **Checkpoint Discipline** section on the
   PLAN PERSISTENCE primitive (Ch09), with the reload-before-each-
   spawn rule (G21 from SYNTHESIS, `SKILL.md:300-307, 331-336`).

The 8-step process itself does **not** belong in the main narrative.
Per AUTHOR-DECISIONS #9 and SYNTHESIS T22, the step list demotes to
an appendix; the **outputs** (handoff packet, plan persistence) are
what surface in the prose.

---

## 2. Scoping rule (when 8-step applies)

State this explicitly in the new layering frame so readers do not
over-engineer one-line rule files into design-doc productions:

**Hard rule "diagrams first" applies to:**

- Cross-cutting redesigns spanning multiple primitive modules.
- New SKILL primitives (the kind Ch09 catalogs).
- New ORCHESTRATOR primitives (gh-aw workflows, panel skills).

**Hard rule does NOT apply to:**

- Single-file `.instructions.md` (one path, one lens, one rule set).
- Short scope-attached rule files (one trigger, one constraint).
- One-paragraph PROSE clarifications that ride on existing primitives.

The proportionality argument matches Ch13's existing "Adapting the
Meta-Process" section (small / large change calibration at lines
275-297). The same frame applies one layer up: the cost of the
8-step process should pay for itself in the avoided ADAPT-loop fires
during execution. On a one-line rule, it cannot. On a new SKILL the
whole team will load on every dispatch hit, it does — many times
over.

The footnote can cite Practitioner Authority's observation that
Genesis itself does not run the 8-step process on every commit to
Genesis (`SYNTHESIS.md:416`); the discipline is for the modules that
warrant it.

---

## 3. Section-by-section edit plan

| Location in `ch13-the-execution-meta-process.qmd` | Edit type | Summary |
|---|---|---|
| Top of file (after the chapter intro, before "The Five Phases" at line 13) | NEW SUBSECTION | Add `## Two layers, one artifact: design vs execution`. Frames the 8-step process as the design layer; names the handoff packet as the boundary; states the scoping rule. ~25 lines. |
| Line 9 ("five-phase meta-process. It works regardless of which AI coding tool you use") | EDIT | Add half-sentence: "...above any specific tool's mechanics, and below the design layer that produces the primitives the loop consumes (see appendix)." |
| `## Checkpoint Discipline` (line 215-260) | EDIT | Anchor on the PLAN PERSISTENCE primitive by name (forward reference to Ch09 §PLAN PERSISTENCE). Add the reload-before-each-spawn rule from `SKILL.md:331-336`. Cross-link Ch11 ATTENTION ANCHOR. Use ALL-CAPS verbatim per C8. |
| `### What Happens at a Checkpoint` (line 227-237) | EDIT | Add a fifth component: **Reload**. The plan store is read at the top of every new spawn so re-grounding is mechanical, not recall-based. |
| `## Wave Decomposition` (line 137 onward) | LIGHT EDIT | One-sentence cross-link to Ch14's R1 SPLIT triggers — the wave that fails on a 58-call-site `install.py` (line 199) is the same shape as a primitive that fails R1 BODY-OVER-BUDGET. The refactor-pattern verbs are how you fix the underlying primitive after the ADAPT loop fires. |
| `## The ADAPT Loop` (line 239-260) | EDIT | One-sentence note that ADAPT echoes Genesis A8 ALIGNMENT LOOP; bound it with N=3 calibration per Ch12 (C9 / dev-lead-proxy R6 alignment). |
| End of chapter (after line 321) | NEW APPENDIX | Add `## Appendix: The Genesis 8-Step Design Process`. Verbatim lift from `SKILL.md:52-83` (the ASCII process diagram and the per-step sketches), with `(adapted from genesis-skill/SKILL.md)` attribution and a forward-link to Ch09. |

The chapter's existing five-phase mermaid diagram (line 17-30), the
worked-example case study (line 183-211), the wave-sizing table (line
166-171), and the Adapting-the-Meta-Process section (line 275-297) all
stay as-is. None of them are wrong; the integration only adds a
layering frame above and a primitive anchor inside. No restructuring.

---

## 4. Full draft of changed sections

### 4.1 NEW SUBSECTION — top of chapter, after line 11

```markdown
## Two layers, one artifact: design vs execution

The five-phase loop in this chapter is the **execution layer**. It
moves code: 75 files, four waves, one merged PR. Above it sits a
**design layer** that produces the primitives — the SKILLs, the
ORCHESTRATORs, the persona scoping files, the scope-attached rule
files — that Ch13's agents load when they execute. The two layers
operate on different artifacts, on different cadences, with different
gates. Conflating them is a category error that produces either
under-designed primitives (which then fail mid-wave) or over-engineered
one-line rule files (which then ship with five diagrams and a
compliance matrix nobody reads).

The design layer is documented in full in [the Genesis architect's
8-step process](https://github.com/danielmeppiel/genesis-skill). In
this book it appears in two places: as a forward reference from Ch09
(where the primitives the design layer produces are catalogued) and
as the appendix to this chapter (where the steps themselves are
listed verbatim for reference). What matters for the execution loop
is not the steps. It is the **output**: the handoff packet.

A handoff packet is a single artifact carrying the component diagram,
the thread/sequence diagram, the dependency graph, an interface
sketch per module, the composition table, the declared targets, and
the open compliance findings. The design layer ends — explicitly,
with the words "DESIGN ENDS HERE" — when the packet is persisted to
the plan store. The execution layer begins by reading the packet
back. The packet is the only thing that crosses the boundary; no
tacit context survives.

This produces a clean rule. **When you start a Ch13 wave on a new
primitive, the handoff packet for that primitive should already
exist.** If it does not, you are doing two things at once: designing
and executing. That is the configuration in which agents go off-
script, scope drifts, and ADAPT-loop fires multiply.

**When the design layer is mandatory.** The hard rule — diagrams
first, packet before drafting — applies to:

- Cross-cutting redesigns spanning multiple primitive modules.
- New SKILL primitives (the modules cataloged in Ch09).
- New ORCHESTRATOR primitives (gh-aw workflows, panel skills).

**When it is exempt.** Single-file `.instructions.md`, short
scope-attached rule files, and one-paragraph PROSE clarifications do
not need the full ceremony. The cost of an 8-step process should pay
for itself in avoided ADAPT-loop fires during execution. On a
one-line rule that ships once and never recomposes, it cannot. On a
new SKILL the whole team loads on every dispatch hit, it does — many
times over.[^ch13-design-cost]

The proportionality argument echoes the small / large calibration in
"Adapting the Meta-Process" later in this chapter: the structure is
the same, the formality is what scales.

[^ch13-design-cost]: The Genesis maintainer notes that the 8-step
process is not run on every commit to Genesis itself; it is reserved
for new primitives and cross-cutting refactors. The exemption is
load-bearing — without it, the discipline collapses under its own
overhead.
```

### 4.2 EDIT — `## Checkpoint Discipline` opening (replaces line 215-225)

```markdown
## Checkpoint Discipline

A checkpoint is the pause between waves. It is the mechanism that
makes the meta-process safe. It is also where the **PLAN
PERSISTENCE** primitive (Ch09) earns its keep.

PLAN PERSISTENCE is a stable artifact — a `plan.md` file, a
structured store, a session note — holding the active plan, the
todo list, and the checkpoint history across turns and across spawns.
It is the cure for attention decay over long sessions. The discipline
is not write-once. It is **write-then-reload**: the plan must be read
back at every re-grounding boundary (start of a wave, return from a
spawn, after a tool failure). A written-once-never-read plan is dead
weight.

Reload cadence in this chapter mirrors the **ATTENTION ANCHOR**
cadence from Ch11. The checkpoint is the cadence event for the
orchestrating session; the spawn boundary is the cadence event for
the wave agent. Both read the same persisted plan. Neither relies on
recall.

### Why Test After Every Wave

[existing prose continues unchanged from line 219 onward]
```

### 4.3 EDIT — `### What Happens at a Checkpoint` (extends line 227-237)

Add a fifth component after **Plan review**:

```markdown
**Reload.** Before the next wave's agents spawn, the orchestrating
session re-reads the persisted plan. Any wave-2 adjustment, any
escalation note added during the previous checkpoint, becomes part
of the plan that wave 3's agents load at startup. This is the
write-then-reload discipline named in PLAN PERSISTENCE: the plan is
not a static document the orchestrator carries in its head; it is a
file the orchestrator and every spawn it produces reads from. The
reload step takes seconds. It is the difference between a wave
launching from the plan as it currently exists and a wave launching
from the plan as the orchestrator remembers it.
```

### 4.4 EDIT — ADAPT loop alignment note (insert at line 241, before the mermaid)

```markdown
The ADAPT loop is the execution-layer realization of Genesis's
**ALIGNMENT LOOP** pattern. Both share the same shape (detect →
diagnose → adjust → re-execute) and the same calibration: bounded
rounds, typically N≈3, treated as a rule of thumb rather than a
measured optimum. The same N=3 calibration appears in Ch12's
multi-agent orchestration discussion. When the ADAPT loop has fired
three times on the same wave, the failure is not a wave-execution
problem; it is usually a primitive-design problem one layer up. At
that point, returning to the design layer and re-running the
relevant 8-step process for the primitive that keeps failing is
cheaper than continuing to ADAPT around it.
```

### 4.5 NEW MERMAID — slot in immediately after the new "Two layers, one artifact" subsection

```{mermaid}
%%| fig-cap: "The design layer (8-step process) emits a handoff packet, persisted via PLAN PERSISTENCE; the execution loop reads the same packet back and operates the five-phase loop. The boundary is the persisted artifact, not a tacit handoff."
%%| fig-alt: "Top-to-bottom diagram. Top region labeled DESIGN LAYER contains a vertical chain of eight nodes representing the Genesis 8-step process from intent and scope through validate. The chain emits a parallelogram labeled HANDOFF PACKET that crosses into a cylinder labeled PLAN PERSISTENCE. From PLAN PERSISTENCE, an arrow leads down into the EXECUTION LAYER region containing the existing five-phase loop AUDIT, PLAN, WAVE, VALIDATE, SHIP with the ADAPT loop folded back to PLAN. A dashed reload arrow runs from PLAN PERSISTENCE to each phase in the execution layer, indicating the read-back discipline."
%%| label: fig-design-execution-layers
flowchart TB
    subgraph DESIGN["DESIGN LAYER (8-step, scoped)"]
        S1["1. intent + scope"] --> S2["2. component diagram"]
        S2 --> S3["3. thread / sequence"]
        S3 --> S35["3.5 composition decision"]
        S35 --> S4["4. SoC pass"]
        S4 --> S5["5. compliance check"]
        S5 --> S6["6. handoff packet"]
    end
    S6 ==> PKT[/"HANDOFF PACKET"/]
    PKT ==> PP[("PLAN PERSISTENCE")]
    subgraph EXEC["EXECUTION LAYER (Ch13 five-phase loop)"]
        AUDIT["AUDIT"] --> PLAN["PLAN"]
        PLAN --> WAVE["WAVE"]
        WAVE --> VAL["VALIDATE"]
        VAL -->|done| SHIP["SHIP"]
        VAL -->|next| WAVE
        VAL -->|fail| ADAPT["ADAPT"]
        ADAPT --> PLAN
    end
    PP -.->|reload| PLAN
    PP -.->|reload| WAVE
    PP -.->|reload| ADAPT
```

(Mermaid conventions per the repo style guide: `flowchart TB`, no
emoji, ASCII labels, double-line `==>` for the artifact boundary,
cylinder `[(..)]` for the persisted store, dashed `-.->` for reload
edges. Fits the 12-node ceiling decided at AUTHOR-DECISIONS #12.)

---

## 5. Appendix — full 8-step process reference

> Slot at the end of the chapter, after line 321 and the existing
> footnotes. Verbatim lift from `genesis-skill/skills/genesis/SKILL.md`
> with attribution. The body of the chapter does not depend on this
> appendix; it is here for the reader who wants the full design-layer
> reference without leaving the book.

```markdown
## Appendix: The Genesis 8-Step Design Process

The execution loop in this chapter consumes primitives — SKILLs,
ORCHESTRATORs, persona scoping files, scope-attached rule files —
that were produced by an upstream design process. This appendix lists
that process in full for reference. The hard rule "diagrams first"
applies only to cross-cutting redesigns and new SKILL or ORCHESTRATOR
primitives; single-file `.instructions.md` and short scope-attached
rule files are exempt (see "Two layers, one artifact" at the top of
this chapter).

(adapted from `genesis-skill/skills/genesis/SKILL.md`)

```
   1 intent + scope
        v
   2 component diagram   <-- load primitives, design patterns,
        v                    architectural patterns, refactor
        v                    patterns, mermaid conventions
   3 thread / sequence diagram
        v
 3.5 composition decision  <-- per box: inline | sibling | external
        v
   4 SoC pass against existing modules
        v
   5 classic + PROSE + LLM-physics compliance check
        v
   6 handoff packet (diagrams + interface sketch + declared targets
                     + module composition table + todos)
        v             [PERSIST PACKET to plan store]
        v                                      [DESIGN ENDS HERE]
   ----- caller / coder thread takes over -----
   7a portability check
        v
   7b draft natural-language module(s)
        v             RELOAD plan before each module / spawn
   8 validate against diagrams + lint (PROSE 5-axis, size budget,
     ASCII, coherent unit, portability honored)
```

The eight steps in summary:

1. **Intent + scope.** One paragraph: capability, trigger, boundary.
   Single Responsibility check (no "and" connecting two capabilities).
   Draft the dispatch description that becomes the module's
   frontmatter `description`.
2. **Component diagram.** A `flowchart` showing every primitive the
   design uses, marked PERSONA / SKILL / RULE / ORCHESTRATOR / ASSET,
   existing vs new.
3. **Thread / sequence diagram.** A `sequenceDiagram` showing
   spawns, fan-in, and any one-writer interlocks. Pattern selection
   runs in tier order (refactor patterns first, then architectural
   patterns, then design patterns).
4. **Composition decision (3.5).** Per box: INLINE asset, LOCAL
   SIBLING primitive, or EXTERNAL MODULE pulled via the project's
   module system. External modules require a declared dependency at
   the distribution surface.
5. **SoC pass.** Apply R1 SPLIT, R2 FUSE, R3 EXTRACT, R4 INLINE
   triggers across the existing module graph (see Ch14 §Refactor
   Patterns). Restructure before re-picking architectural patterns.
6. **Compliance check.** PROSE 5-axis, MODULE ENTRYPOINT canonical
   spec (name regex, description ≤ 1024 chars, body ≤ 500 lines),
   classic principles. BLOCKER findings stop the design.
7. **Handoff packet.** Diagrams + interface sketches + composition
   table + declared targets + open findings + todos + an evals plan.
   Persisted to the plan store. Design ends here.
8. **Draft + validate (caller-side).** Portability check (7a) loads
   the common substrate; only flagged per-harness needs load a
   harness adapter. Module bodies (7b) draft against the persisted
   packet, reloaded before each spawn. Validation (8) lints against
   the packet's interface sketches.

The reload-before-each-spawn rule at step 7b is the same write-then-
reload discipline named in the PLAN PERSISTENCE primitive (Ch09)
and applied at every checkpoint of this chapter's execution loop.
The discipline is not duplicated; it is one rule, applied at two
layers.
```

---

## 6. Cross-link audit

The integration creates four cross-link edges Ch13 currently lacks
or under-states. All four point at primitives or patterns named
elsewhere in the handbook; none of them require new prose in the
target chapter.

| Edge | Target | Anchor in target | Purpose |
|---|---|---|---|
| Ch13 §Checkpoint Discipline → Ch09 §PLAN PERSISTENCE | Ch09 (primitives catalog under AUTHOR-DECISIONS C1 / C4) | The PLAN PERSISTENCE primitive entry — write-then-reload, plan store, reload at re-grounding boundaries | Names the primitive Ch13 has been using implicitly. |
| Ch13 §Checkpoint Discipline → Ch11 §ATTENTION ANCHOR cadence | Ch11 (context engineering) | ATTENTION ANCHOR cadence — the mechanism that decides when to re-ground | The cadence the checkpoint inherits is the same cadence Ch11 already names. |
| Ch13 §Wave Decomposition → Ch14 §Refactor Patterns | Ch14 (anti-patterns + refactor pattern absorption per AUTHOR-DECISIONS C5) | R1 SPLIT, R2 FUSE, R3 EXTRACT, R4 INLINE | When ADAPT fires repeatedly, the wave-shape problem is usually an underlying primitive-shape problem; R1-R4 are the in-loop refactor verbs. |
| Ch13 §ADAPT loop → Ch12 §Bounded rounds | Ch12 (multi-agent orchestration; C9 calibration wording) | N≈3 rule of thumb, taught discipline | Aligns ADAPT iteration ceiling with the same calibration Ch12 documents. |

One edge from Ch13 outward already exists (the Conway's Law footnote
at line 321 forward-references Ch12's team-as-decomposition framing).
That edge does not need to change.

---

## 7. Impact summary

**Net change to Ch13 length:** +~150 lines.

- New "Two layers, one artifact" subsection: ~80 lines including
  the new mermaid.
- Checkpoint Discipline edits: ~15 lines net (a paragraph added at
  the opening, a fifth component added to "What Happens at a
  Checkpoint", an ADAPT-loop alignment note).
- Appendix (verbatim 8-step lift with attribution): ~75 lines.
- Body deletions: zero. The existing five-phase narrative, the
  worked example, the wave-sizing table, and the small/large
  calibration are all kept.

**Decisions honored.**

- AUTHOR-DECISIONS #9 (8-step scope): step list demoted to appendix;
  outputs (handoff packet, PLAN PERSISTENCE) surfaced in main
  narrative; scoping rule (cross-cutting + new SKILL/ORCHESTRATOR
  only; single rule files exempt) stated explicitly in the new
  layering subsection.
- AUTHOR-DECISIONS C4 (PLAN PERSISTENCE primitive): named verbatim
  at the opening of Checkpoint Discipline; reload-before-each-spawn
  rule added; ATTENTION ANCHOR cadence cross-link added.
- AUTHOR-DECISIONS C8 (voice rule): pattern names ALL-CAPS verbatim
  throughout — PLAN PERSISTENCE, ATTENTION ANCHOR, ALIGNMENT LOOP,
  R1 SPLIT, R2 FUSE, R3 EXTRACT, R4 INLINE, MODULE ENTRYPOINT,
  CHILD-THREAD SPAWN, ADAPT, AUDIT, PLAN, WAVE, VALIDATE, SHIP.

**Risks the integration does NOT take.**

- Does not rename phases. AUDIT / PLAN / WAVE / VALIDATE / SHIP stay.
- Does not absorb the 8-step process into the body. It stays in the
  appendix per AUTHOR-DECISIONS #9.
- Does not duplicate the refactor-pattern catalogue. R1-R4 stay in
  Ch14 per AUTHOR-DECISIONS C5; Ch13 cross-links only.
- Does not introduce per-harness syntax. The handoff-packet boundary
  is harness-agnostic.

**Downstream chapter touchpoints.**

- Ch09: needs the PLAN PERSISTENCE primitive entry to exist before
  this Ch13 cross-link lands. Per the Ch09 deep-dive, this is in
  scope under C4. Sequencing: Ch09 lands first, then Ch13.
- Ch14: needs R1-R4 entries to exist as named refactor patterns.
  Per C5 absorption decision, this is in scope. Sequencing: Ch14
  refactor-pattern absorption lands before Ch13's wave-decomposition
  cross-link goes hot.
- Ch12: no change required; the bounded-rounds wording at
  `ch12:317` already says "rule of thumb, not measurement", which
  is what the new ADAPT-loop note cites.

**Verification before this chapter ships.**

1. The new mermaid renders under the handbook's Quarto pipeline
   without breaking the 12-node ceiling.
2. All ALL-CAPS pattern names in the new prose match the names
   used in Ch09, Ch11, Ch12, and Ch14 (no drift).
3. The appendix attribution line matches the canonical path
   (`genesis-skill/skills/genesis/SKILL.md`).
4. The "DESIGN ENDS HERE" quote in the new subsection is verbatim
   from `SKILL.md:309`.

No reversal request. The integration sits cleanly under the binding
decisions and produces a chapter that reads as one of two layers
rather than as a stand-alone methodology.
