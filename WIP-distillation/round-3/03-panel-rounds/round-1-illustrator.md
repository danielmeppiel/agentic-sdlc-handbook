# Illustrator Review — Round 1

## Verdict
MINOR-REVISIONS

## Diagram inventory feasibility

### Ch09 — The Runtime Machine
1. **Four-part stacked-block diagram** (data flow at session start): **EASY**
   - Simple flowchart LR: user request → harness → file load → context assembly → model → tool calls → trigger surface → side effect
   - 8 boxes, linear flow, no branching
   - Fits mermaid conventions perfectly (under 25 nodes, single concept)

2. **Two-column comparison (Copilot vs Claude Code load order)**: **MEDIUM**
   - Not actually a diagram — this is a side-by-side markdown table or two parallel flowcharts
   - Risk: if rendered as two parallel flowcharts in one mermaid block, GitHub rendering can struggle with horizontal layout on mobile
   - Recommendation: structured markdown table with "Load Step", "Copilot", "Claude Code" columns. Clearer and more scannable than dual flowcharts.

### Ch13 — The Deterministic / Probabilistic Boundary
3. **The seam diagram** (deterministic | probabilistic | what crosses): **HARD**
   - Conceptually: two-column with bidirectional arrows showing what crosses the boundary
   - Mermaid pain point: representing "what crosses" cleanly requires either:
     - Two subgraphs (left=deterministic, right=probabilistic) with labeled edges crossing between them, OR
     - A three-column layout (deterministic | interface | probabilistic) — but this makes it a table, not a flow diagram
   - Risk: too many edges if we show all crossing points (file I/O, tool calls, results, grounding, gates, verifications)
   - Recommendation: **Use a table** with three columns: "Deterministic Side", "Crosses Seam As", "Probabilistic Side". Example rows: "test runner" | "verification result →" | "plan generator", "lockfile" | "← tool invocation" | "agent thread". This is the "faster than prose" test winner — a flowchart with 12+ crossing arrows becomes spaghetti.

4. **2x2 of gate types** (programmatic vs judgment × internal vs external): **EASY**
   - This is a classic quadrant chart, mermaid-friendly
   - Use `flowchart` with four positioned boxes and annotations, or just a markdown table
   - Table is cleaner: headers = "Internal Source" / "External Source", rows = "Programmatic" / "Judgment", cells = examples
   - Passes the "one idea per visual" test

### Ch17 — Primitives as Code
5. **Publish-vs-load distinction** (ship-time scope vs run-time scope): **MEDIUM**
   - Two-phase diagram: author-side scope (what gets bundled) vs consumer-side scope (what gets loaded)
   - Mermaid option: two subgraphs with a dashed boundary between them
   - Risk: if we add the "bundle leakage" anti-pattern as a visual element, it clutters
   - Recommendation: Two-panel flowchart (one subgraph per phase) with a single arrow labeled "lockfile pins" crossing the boundary. Keep bundle-leakage as a prose callout, not a diagram overlay.

6. **Primitive lifecycle** (author → lint → test → publish → resolve → load → execute → audit): **EASY**
   - Linear flowchart, 8 nodes, no branches
   - Textbook mermaid use case
   - Possible enhancement: mark deterministic vs probabilistic phases (lint/test/publish/resolve are deterministic; load/execute may involve LLM)

### Ch18 — The Cross-Harness Reference
7. **5×6 substrate-question matrix**: **NOT-ACTUALLY-A-DIAGRAM**
   - This is a data table (5 harnesses × 6 substrate concepts = 30 cells)
   - Attempting to render this as a mermaid flowchart would produce a kitchen-sink diagram (30+ nodes)
   - The right format is a **markdown table** with sortable/filterable columns if rendered in Quarto
   - Passes the reference-material test; does not pass the "diagram" test

8. **Trigger-surface vs inference-harness axes** (2D grid with example cells): **MEDIUM**
   - Conceptually: a 2D grid showing orthogonality (trigger on one axis, harness on the other, cells = pairings)
   - Mermaid option: flowchart with positioned nodes, but it will look forced
   - Better: a **table** with trigger surfaces as rows, inference harnesses as columns, cells = "yes/no/native"
   - If the goal is to show *which pairings exist*, a table beats a graph

## Missing diagrams

1. **Ch12 (Context Engineering / Load Lifecycle) — sequence diagram**: The proposed arc adds "load lifecycle and transitive-closure sections" but names no diagram. A **sequence diagram** showing harness → persona files → rules → on-demand modules → child threads (with time progressing downward) would make load order observable. Complexity: medium (5-7 participants, linear cascade).

2. **Ch13 (Deterministic/Probabilistic Boundary) — supervised execution example**: The arc mentions "strong-form supervised execution" but doesn't diagram it. A **flowchart** showing LLM plan → gate checkpoint → tool invocation → deterministic verifier → gate decision would concretize the seam. Complexity: easy (6 nodes, one decision diamond). This is the Genesis "A9 SUPERVISED EXECUTION" pattern; mermaid-conventions.md already has a canonical fragment for it.

3. **Ch14 (Multi-Agent Orchestration) — threading topology 2×2**: The arc says "add the threading-topology 2x2 as the chapter's spine" but doesn't inventory it. Needed: a **2×2 quadrant** showing (sequential vs parallel) × (stateless vs stateful). Complexity: easy (table or positioned flowchart boxes).

4. **Ch16 (Anti-Patterns / Stack Trace) — agent stack trace example**: The arc adds "the agent stack trace" as the unifying protocol but no visual. A **before/after comparison** (prose error message vs structured stack trace with load path, binding point, transitive deps) would be powerful. Complexity: medium (two side-by-side text blocks, not a true diagram, but high pedagogical value).

## Findings

### F1 (MEDIUM) — Ch13 seam diagram is not a diagram
- **Claim**: The "seam diagram" as described ("deterministic computer | probabilistic computer | what crosses each direction") will produce a spaghetti flowchart if rendered in mermaid with labeled edges for every crossing point (file I/O, tool calls, results, grounding, gates, verifications, spawn signals).
- **Evidence**: Mermaid-conventions.md warns against diagrams with more than 7 relationship edges; the seam has at least 6 distinct crossing types, each bidirectional. GitHub rendering struggles with dense edge layouts on mobile. The Genesis tool-call convention uses double-line edges for deterministic→probabilistic crossings, but stacking 6+ such edges in one diagram violates the "one idea per visual" principle.
- **Proposed change**: Replace the seam diagram with a **three-column table**: "Deterministic Side" | "Interface/Seam" | "Probabilistic Side". Each row is one crossing type (e.g., "test runner" | "pass/fail signal →" | "plan revision"). Add a **simple two-box diagram** above the table showing just the high-level split (one box = deterministic computer, one box = probabilistic computer, one bidirectional arrow = "interface"). The table carries the detail; the diagram carries the concept.

### F2 (LOW) — Ch18 matrix is reference data, not a diagram
- **Claim**: The 5×6 substrate-question matrix (5 harnesses × 6 substrate concepts = 30 cells) is being inventoried as a "diagram" but is actually tabular reference data.
- **Evidence**: Mermaid-conventions.md: "Keep each diagram under 25 nodes." A 30-cell matrix would require 30 nodes plus edges. The visual strategist principle: "If a 3-element diagram conveys the same insight as a 12-element diagram, use 3." The insight here is "different harnesses have different substrate properties" — the *lookup* is the value, not the *shape*.
- **Proposed change**: Render the 5×6 matrix as a **markdown table** (sortable in Quarto). Add a **small 2-box flowchart** showing the "substrate question" pattern: one box = "your design (substrate concepts)", one box = "harness adapter (per-vendor realization)", arrow = "portability boundary". The flowchart establishes the mental model; the table is the reference.

### F3 (MEDIUM) — Ch09 load-order comparison will fail on mobile if dual-flowchart
- **Claim**: The "two-column comparison: Copilot's load order vs Claude Code's load order" is at risk of rendering poorly in narrow viewports if implemented as two side-by-side mermaid flowcharts in one code block.
- **Evidence**: Mermaid LR (left-right) flowcharts do not reflow on mobile; GitHub renders them at fixed width. Two parallel flowcharts in one block will force horizontal scroll. The alternative — two separate mermaid blocks stacked vertically — loses the side-by-side comparison value.
- **Proposed change**: Use a **markdown table** with three columns: "Load Step" (numbered 1-N), "Copilot", "Claude Code". Each cell describes what loads at that step. This format is mobile-safe, version-control-friendly, and faster to scan than dual flowcharts. If a visual is still desired, add a single **flowchart** showing the *generic* load order (persona → rules → on-demand modules → children) and use the table to show *variance*.

### F4 (HIGH) — Ch12 load-lifecycle needs a sequence diagram, currently unlisted
- **Claim**: Ch12 (Context Engineering / Load Lifecycle) is being restructured to "add the load-lifecycle and transitive-closure sections" but the diagram inventory is empty. Load order is sequential and time-sensitive; this is a textbook use case for a sequence diagram.
- **Evidence**: Mermaid-conventions.md: "Step 3 | sequenceDiagram | thread spawn / fan-in / interlock points." The proposed concepts (persona files load first, then rules, then modules, then children) are a cascade — sequence diagrams make cascades observable. Genesis defines this in `runtime-affordances/common.md` "What the substrate guarantees" but the handbook has no visual.
- **Proposed change**: Add to Ch12's diagram inventory: **Sequence diagram** with participants = harness, persona-scope, rule-scope, module-registry, child-threads. Vertical flow shows load order. Annotate with "Note over" blocks for key guarantees (e.g., "rules cannot override persona"). Complexity: medium (5 participants, 8-10 messages, no branches).

### F5 (MEDIUM) — Ch14 threading-topology 2×2 is named but not inventoried
- **Claim**: The arc says Ch14 will "add the threading-topology 2x2 as the chapter's spine" but the diagram inventory for Ch14 is absent from section 4.
- **Evidence**: The changeset table (section 2) says Ch14 = "KEEP+ADD" with threading topology as the structural addition, but section 4 only details the four *new* chapters (Ch09, Ch13, Ch17, Ch18). The threading 2×2 is load-bearing for the chapter but not specified.
- **Proposed change**: Add to the arc (or flag for Wave B): Ch14 diagram inventory should include a **2×2 quadrant chart** with axes = (sequential vs parallel) × (stateless vs stateful). Each cell = one threading pattern with a one-line description and a pointer to the Genesis pattern code (e.g., A4 SIBLING THREADS in the "parallel + stateless" cell). Render as either a mermaid flowchart with four positioned boxes or a markdown table. Complexity: easy.

### F6 (LOW) — Ch17 primitive-lifecycle diagram should mark deterministic/probabilistic phases
- **Claim**: The primitive lifecycle diagram (author → lint → test → publish → resolve → load → execute → audit) is listed as linear, but it crosses the deterministic/probabilistic boundary and should mark that seam visually.
- **Evidence**: Ch13 is the "deterministic / probabilistic boundary" chapter; Ch17 is "primitives as code." The lifecycle phases split cleanly: author/lint/test/publish/resolve are deterministic (file I/O, CI, lockfile resolution); load/execute are probabilistic (agent decides whether to activate the module). The diagram should reinforce the seam.
- **Proposed change**: Render the lifecycle as a **flowchart** with two background colors or subgraphs: one for deterministic phases (left), one for probabilistic phases (right). The "load" step is the crossing point. This connects Ch17 back to Ch13's thesis without duplicating content.

### F7 (LOW) — Ch16 agent-stack-trace example is prose, not diagram, but high pedagogical value
- **Claim**: The arc adds "the agent stack trace" as Ch16's unifying framework but inventories no visual. A before/after comparison of error output would have high teaching value even though it's not a traditional diagram.
- **Evidence**: The visual strategist principle: "Visuals earn their space" via the "faster than prose" test. Showing a traditional error message ("the agent hallucinated an edit") vs a structured stack trace (load path → binding point → transitive deps → attention budget at decision time) is a **worked example**, not a diagram, but it concretizes the debugging discipline faster than prose alone.
- **Proposed change**: Add to Ch16's inventory: **Before/after comparison** rendered as two fenced code blocks (not mermaid). Label: "Traditional error report" vs "Agent stack trace." This is the equivalent of showing a segfault vs a full gdb backtrace. Not a flowchart, but a visual nonetheless.

## Final word

The proposed arc is **diagram-feasible with two structural fixes** and three additions.

**Fixes required** (MINOR-REVISIONS):
1. Ch13 seam diagram → two-box concept diagram + three-column crossing table
2. Ch18 matrix → two-box portability diagram + markdown reference table

**Additions recommended**:
3. Ch12 load-lifecycle → sequence diagram (medium complexity)
4. Ch14 threading topology → 2×2 quadrant (easy)
5. Ch17 lifecycle → mark deterministic/probabilistic phases (trivial style change)

**Anti-patterns avoided**: No kitchen-sink diagrams, no decorative visuals, no unlabeled arrows. The arc respects the "one idea per visual" and "elegantly simple" principles. The two high-risk diagrams (seam, matrix) are correctly identified as concepts that belong in tables, not flowcharts.

**Visual density**: The final block will have 8-10 load-bearing visuals spread across 13 chapters (~0.7 visuals/chapter). This is appropriate for practitioner material — denser than executive summary, sparser than API reference. The proposed visuals are all "faster than prose" — they teach substrate concepts (four-part machine, load order, seam, lifecycle) that spatial language cannot convey efficiently in linear text.

**Mermaid compliance**: All flowcharts stay under 25 nodes. All diagrams use ASCII arrows and avoid Unicode. The sequence diagram for Ch12 follows mermaid-conventions.md step-3 guidance. The supervised-execution fragment (if added to Ch13) can lift the canonical form from mermaid-conventions.md lines 188-196 directly.

**Cross-chapter visual language**: The "deterministic | probabilistic" split introduced in Ch13 is reinforced in Ch17's lifecycle. The "four-part machine" from Ch09 is referenced (not redrawn) in Ch13's seam discussion. The "transitive closure" concept in Ch12 is visually echoed in Ch17's publish-vs-load diagram. This is good visual architecture — motifs recur without redundancy.

**Chapter-as-appendix question** (from section 6, open question #1): Ch18 should be an **Appendix**, not a chapter. It is reference data (the 5×6 matrix) that the teaching chapters point to, but it does not advance the narrative arc. Appendices are where tables with 30 cells belong. This also answers the visual question: appendices can have dense tables; chapters should have sparse, concept-forward diagrams.

**Mobile and dark-mode safety**: All proposed changes favor markdown tables and simple flowcharts over complex layouts. Tables reflow; flowcharts with <10 nodes render acceptably on mobile. No reliance on color for semantics (the deterministic/probabilistic split can use subgraph labels, not just background tint).

**Verdict rationale**: MINOR-REVISIONS rather than APPROVE because two inventoried diagrams (Ch13 seam, Ch18 matrix) are mis-classified and need format changes. The arc is strong; the fixes are surgical. With the two changes and three additions, the visual layer will be production-ready.
