# A4 gate — author decisions

> Decisions taken by orchestrator on the author's behalf per explicit
> "make good decisions and keep working" instruction. Each decision
> follows the synthesis recommendation. Author may override any of
> these at the A7 final gate before handbook PR opens.
>
> Source: `WIP/round-1/SYNTHESIS.md` §6 (14-item checklist).

## Canonical conflict resolutions

| # | Decision | Choice | Source |
|---|---|---|---|
| 1 | **C1 — Six vs seven primitives** | **Shape A**: publish six as canonical; Genesis names as Ch09 headers; current 7-block fig as appendix; "Industry terms: ..." lead-in to each section. | SYNTHESIS §4 C1 |
| 2 | **C3 — Ch15:23 governance vocabulary** | **Adopt**: name SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE; cite gh-aw safe-outputs as existing-today reference implementation. | SYNTHESIS §4 C3 |
| 3 | **C4 — Memory split** | **Two distinct primitives**: PLAN PERSISTENCE (active plan + checkpoints) + MEMORY (cross-session knowledge). | SYNTHESIS §4 C4 |
| 4 | **C5 — Ch14 anti-pattern absorption scope** | **Partial**: absorb practitioner-grade entries (R1–R4 verbs, Wave anti-patterns, Trust-Fall cross-link, TOKEN-LAUNDERING, INNER-LOOP-MISCAST); Genesis remains canonical for source-time + packaging detail. | SYNTHESIS §4 C5 |
| 5 | **C6 — PHANTOM DEPENDENCY / BUNDLE LEAKAGE** | **Shape C (split)**: BUNDLE LEAKAGE + DISPATCH CONTAMINATION as full Ch14 entry; other four as footnote until Round 2 evidence. | SYNTHESIS §4 C6 |
| 6 | **C7 — A1 PANEL vs Writer/Reviewer/Tester naming** | **Shape C**: keep handbook headers; second sentence reads "(architecturally: A1 PANEL — see Genesis)". | SYNTHESIS §4 C7 |
| 7 | **C8 — Voice rule** | **Adopt as house style**: named patterns ALL-CAPS verbatim; surrounding prose in handbook register; one verbatim definition box per pattern; no buzzword translation. | SYNTHESIS §4 C8 + TL §4a |
| 8 | **C9 — Bounded-rounds N** | **Adopt handbook wording in Genesis**: state as calibration not measurement; mirror `ch12:317`. | SYNTHESIS §4 C9 |

## Process scope

| # | Decision | Choice |
|---|---|---|
| 9 | 8-step design process | **Scope hard-rule "diagrams first" to cross-cutting redesigns and new SKILL/ORCHESTRATOR primitives only**. Exempt single-file `.instructions.md` and short scope-attached rule files. Handbook narrative: demote step list to appendix; surface outputs (handoff packet, plan persistence) in narrative. |

## Cleanup / verification

| # | Decision | Choice |
|---|---|---|
| 10 | PROSE citation cleanup (`primitives.md:230-231`) | **Replace blog cite with Ch10 cite**; keep blog as secondary provenance. 1-line edit. |
| 11 | APM URL verification (`apm.md:34`) | **Verify** `danielmeppiel.github.io/awd-cli/.../anatomy-of-an-apm-package/` is canonical OR update to microsoft/apm location. Deep-dive owner: ch09-primitives. |
| 12 | Mermaid conventions adoption | **Cross-link to Genesis, do not absorb as appendix**. Ship a `CONTRIBUTING-diagrams.md` (~200 words) with handbook-specific overlays (Quarto wrapper, 12-node ceiling, `pie/gantt/block-beta` carve-out, no emoji). |
| 13 | Hooks shape gap (IL §4d) | **Bidirectional fix**: propose trapezoid `[\..\]` for HOOK shape; disambiguate PROMPT vs ORCHESTRATION (currently both use `{..}`). One round-trip with Genesis maintainer (out of band). |
| 14 | Ch15 `ch15-squad` footnote forward-date | **Confirm publication or replace** with verifiable cite. Out-of-scope for this distillation; flagged for handbook side. |

## Doc-site IA decisions (B2 gate, taken in parallel)

| # | Question | Decision |
|---|---|---|
| B2.1 | Resources page for external corpus (handbook + agentskills.io + APM)? | **Yes** — `Resources / External corpus` page with cross-links + scope-of-each notes. |
| B2.2 | Per-harness setup — one page per harness or one matrix? | **One page per harness** (better Cmd+F, deep-link from blog posts, room for harness-specific quirks). Index page + 6 detail pages. |
| B2.3 | Examples gallery — 5 separate pages or one long page? | **5 separate pages** + index gallery. Each example is self-contained narrative. |
| B2.4 | Gemini per-harness file is missing in corpus | **Punt**: include Gemini in the harness index with a "coming soon" note. Track as a Genesis corpus issue separately; do not block site launch. |

## A7 final-gate review hooks

The author SHOULD revisit and may override:

- C1 Shape choice (highest blast radius — affects Ch09 spine).
- C5 absorption-scope (Ch14 length growth).
- C8 voice rule (positioning consequence; affects every Genesis-derived passage).
- B2.4 Gemini decision (corpus completeness signal).

If any of these reverse, the affected deep-dive draft re-runs. Other decisions are low-risk and unlikely to reverse.

## What this enables

- Round 2 chapter deep-dives (Ch09, Ch10, Ch11, Ch12, Ch13, Ch14) can dispatch in parallel.
- Doc-site B3 scaffold can dispatch.
- Ch15 deep-dive WAS gated on C3 — now unblocked under decision #2 (Adopt). NOTE: Ch15 was NOT in the original 6-chapter plan (plan listed Ch09/10/11/12/13/14). C3 affects Ch15:23 which is currently a one-paragraph touch — handle as a delta in the Ch14-or-Ch12 deep dive's "downstream" section, OR add a 7th deep dive. Decision: bundle the Ch15:23 paragraph into the Ch14 deep dive's scope (it's the governance-anti-patterns home) to avoid a 7th parallel agent.
