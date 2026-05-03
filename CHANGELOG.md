# Changelog

All notable changes to The Agentic SDLC Handbook are recorded here. Format follows the spirit of Keep a Changelog; the handbook is prose, so entries describe edits to chapters and primitives rather than software diffs.

## 0.10.1 - May 2026 edition

### Reference architecture (Ch04)

- New Ch04 ("The Reference Architecture") presents a 5-layer stacked supply-chain landscape: Platform -> Context & Capabilities -> Governance and Distribution -> Agent Harness -> SDLC phases. Bottom-to-top hero diagram with per-edge labels (hosts / authored as / resolves and ships / executes as).
- Recursion diagram: the {Skill, Persona, Context} triplet repeats at every depth; eval-and-plan conventions make the recursion governable.
- APM-as-supply-chain table maps `apm.yml`, `apm.lock.yaml`, `apm_modules/`, `apm install`, `apm publish` to their npm analogues.
- Frameworks-as-libraries sidebar names Spec-Kit, Squad, Superpowers, and BMAD as primitive-supplying libraries at the Context & Capabilities layer (with URLs).
- Microsoft-stack sidebar maps Foundry Agent Service, GitHub Agentic Workflows, Copilot Studio, M365 Graph, Fabric, Entra Agent ID, and Purview for agents against the 5 layers; APM lockfile sits underneath identity and policy.
- Closing thesis: the SDLC is one instance of the pattern; legal review, M&A diligence, financial close, marketing campaigns, and book authoring all generalise the same way. This handbook itself was authored using the editorial-pipeline `Skill` (forward-pointer to `case-study-handbook-writing.qmd` in Part IV).

### Part III restructure (Ch08-Ch21)

- Reorganized Part II Ch04 ("The Reference Architecture") as a leader-grade chapter: surface 5-layer landscape, decision matrix, build/buy/compose framing — without the deep recursion mechanics, panel walkthrough, or three-concern triplet that previously lived alongside the executive material.
- Promoted the practitioner-grade material into a new **Ch08 ("The Practitioner's Reference Architecture")** at the head of Part III: deep mechanics of the five-layer model, end-to-end Panel walkthrough (Section 4), recursion bound, Microsoft-stack mapping, and the start-anywhere pattern generalisation — all with `-mechanics`-suffixed labels (e.g. `@sec-five-layers-mechanics`, `@fig-recursion-mechanics`) so they do not collide with the leader-grade Ch04 anchors.
- Renumbered the remaining Part III chapters by +1: Ch08 Mindset -> Ch09, Ch09 Runtime -> Ch10, Ch10 Instrumented -> Ch11, Ch11 PROSE -> Ch12, Ch12 Load Lifecycle -> Ch13, Ch13 Attention -> Ch14, Ch14 Det/Prob Boundary -> Ch15, Ch15 Multi-Agent -> Ch16, Ch16 Execution Meta-Process -> Ch17, Ch17 Rosetta -> Ch18, Ch18 Anti-Patterns -> Ch19, Ch19 Primitives-as-Code -> Ch20, Ch20 What Comes Next -> Ch21.
- Updated `_quarto.yml` Part III chapter list and Closing block to reflect the new ordering.
- Swept all `Chapter N` and `ChNN` prose mentions across every chapter to point at the new numbering. Refs to deep mechanics (Panel deep treatment, recursion bound, three-concern triplet, npm-mapping) re-pointed from old Ch04 to new Ch08; refs to surface-level material (5-layer landscape mental model, surface starter shape) stayed at Ch04. Rewrote the Part III opener forward-pointer in Ch07 to reflect that Ch08 now leads with the practitioner-grade reference architecture (not the mindset chapter, which moved to Ch09).

### Roles and team structures (Ch06)

- Three role concerns named: `Domain Specialist` (procedure), `Agentic Workflow Engineer` (composition), `Agent Operations Specialist` (operations). The BPM workflow-engineer collision is named once and dispensed with. `SME` and `Domain Owner` are recognised passing synonyms for `Domain Specialist`.
- 5-layer ownership swimlane shows who builds and operates what at each layer.
- New subsection "How developers work in the agentic SDLC" treats the developer day-to-day: authoring `Skills`, `Personas`, and `Context` bundles in the same repo as the code; CODEOWNERS extends to `apm.yml`; inner-loop / outer-loop split.

### Cross-cutting

- Compounding and cost-curve claims throughout the book carry `hypothesis` or `early signal` register.
- All chapter diagrams use the centralised `_quarto.yml` mermaid CSS variables (lines 76-100). Per-diagram colour skinning is not used.
- 8 sibling chapters (Ch03, Ch05, Ch13, Ch15, Ch17, Ch19, Ch20) refreshed for cross-link fidelity and 5-layer vocabulary alignment.
- Ch20 closing thread: "the SDLC is just one example of what these patterns and harnesses can agentify."
- Split Part III opening: a short preface (vocabulary + 5-layer map + composition-pattern names, ~1,600 words) opens Part III as the new Ch08 ("A Map for Part III"), giving the leader a five-minute exit ramp and the practitioner the vocabulary the substrate chapters operate in. The capstone "The Reference Architecture, Earned" (Ch21) closes Part III with the Panel worked example, the APM-to-npm mapping table, the Microsoft-stack landing sidebar, the Monday decision frame, and the "the proof is this book" close — landing as earned recognition after the substrate chapters rather than as an asserted preview before them. Synthesis-grade material moved from the opener to the capstone; vocabulary-introduction material stayed at the opener. Ch07's Part-III forward pointer, Ch09's opening callback, and the four substantive Ch08 cross-references in Ch14, Ch16, and Ch20 were re-pointed accordingly. Closing chapter "What Comes Next" renumbered from Ch21 to Ch22. Two legacy footnote names in Ch09 (`^ch8-n1`, `^ch8-cognitive`) renamed to `^ch9-n1`, `^ch9-cognitive`.
