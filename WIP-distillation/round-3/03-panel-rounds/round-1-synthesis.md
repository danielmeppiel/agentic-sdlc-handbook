# Round 1 Synthesis — Chief Editor Verdict

**Date:** Round 1 of 3 (planned).
**Reviewers:** chief-editor, practitioner-authority, market-analyst, platform-strategist, dev-lead-proxy, illustrator, fact-ref-checker.

## Verdict aggregation

| Reviewer              | Verdict          | High-severity findings | Major contradictions |
|-----------------------|------------------|------------------------|----------------------|
| chief-editor          | MINOR-REVISIONS  | 1                      | none                 |
| practitioner-authority| MINOR-REVISIONS  | 3                      | none                 |
| market-analyst        | MINOR-REVISIONS  | 2                      | none                 |
| platform-strategist   | MINOR-REVISIONS  | 3 (must-fix)           | none                 |
| dev-lead-proxy        | MINOR-REVISIONS  | 2                      | none                 |
| illustrator           | MINOR-REVISIONS  | 0 (2 medium)           | none                 |
| fact-ref-checker      | MINOR-REVISIONS  | 1                      | none                 |

**Convergence test (structural).** Threshold is >= 6/7 APPROVE-or-MINOR-REVISIONS *and* no two reviewers in direct contradiction on a load-bearing element. Result: **7/7 MINOR-REVISIONS, zero contradictions on load-bearing elements**. Convergence achieved on Round 1. Proceed to final.

## Cross-reviewer agreement (the load-bearing findings)

Three findings recur across multiple reviewers; treat these as mandatory corrections in the final arc.

**A. Ch12 is overcrowded — split it.** Chief editor (F1, high) and dev-lead (F6) and illustrator (missing-diagram-1) converge on this. The current "Ch12 Context Engineering and Load Lifecycle" tries to teach the deterministic load mechanics *and* the probabilistic attention-economy disciplines in one chapter. Split into:
- **Ch12 — The Load Lifecycle.** Deterministic content: who-loads-what-when, transitive closure, binding modes, the `npm ls` analog for context.
- **Ch13 — Attention and Context Economy.** Probabilistic content: attention as physics, plan-write-then-reload, the bounded-scope rule for grounding.

This forces a renumbering: the deterministic/probabilistic boundary chapter becomes Ch14 (was Ch13), and downstream chapters shift +1.

**B. Ch18 is a reference, not a chapter — demote to appendix.** Practitioner-authority (F1, high), dev-lead (F3), and illustrator (it's a table not a diagram) all flag this. The cross-harness substrate matrix is the highest-utility reference material in the book but is not teaching prose. Move to Appendix A; have Ch10, Ch12, and Ch14 forward-reference it explicitly.

**C. Open the new chapters with a concrete failure, not theory.** Practitioner-authority (F2, high), dev-lead (F1, high), and market-analyst (F1) converge: Ch09 (Runtime Machine), the new Ch14 (Deterministic/Probabilistic Boundary), and Ch17 (Primitives as Code) must each begin with a recognizable Monday-morning failure that the chapter then resolves. The substrate vocabulary follows the failure; it does not lead. This is a *pedagogical* requirement, not just stylistic.

## Single-reviewer findings worth incorporating

**D. (Platform strategist F4) gh-aw is *one realization* of supervised execution, not the canonical strong form.** Reframe in Ch14 to "the gh-aw realization" with a sentence acknowledging that other substrates (CI lambdas, Buildkite job-level secrets, Argo Workflows) implement the same pattern. This is a vendor-fairness fix and removes a potential point of contention.

**E. (Market analyst F1, F3) Prove markdown-as-code with tooling examples.** The thesis "markdown that steers an LLM is code" needs at least one concrete worked example showing primitive lint, primitive test, and primitive lockfile in action. Without this, the meta-thesis reads as slogan, not architecture. Place this in Ch17 as the chapter's opening worked example.

**F. (Dev lead F2, illustrator missing-diagram-2) The agent stack trace is a checklist, not prose.** In Ch16 (renumbered to Ch17 after the Ch12 split), the "diagnostic protocol" must be a numbered, tickable checklist that fits on one printed page. This is a usability requirement: it gets used during postmortems, not during reading.

**G. (Fact checker F1, F3) Vendor claims and academic claims need explicit sourcing.** Add a "Sources and verification dates" footnote convention: every vendor-specific claim in Ch10, Ch12, Ch14, and Appendix A is dated; every academic-flavor claim (attention as physics, the 2x2 of quality gates) is either cited or explicitly labeled "author's synthesis."

**H. (Illustrator F2) Replace "diagram" with "table" where appropriate.** Ch14's seam diagram and Appendix A's substrate-question matrix are tables. Mermaid would produce spaghetti. The `Ch12 load lifecycle` chapter, by contrast, *should* gain a sequence diagram (currently absent).

**I. (Chief editor F2) Cross-harness reference needs an explicit maintenance model.** Appendix A states a snapshot date and a refresh cadence. Without this, the appendix dates the entire book.

## Findings deferred to implementation phase

These are quality multipliers, not arc-level decisions — surface them when authoring:

- Concrete-example inventory per chapter before drafting (practitioner F4).
- Bidirectional linking protocol between chapters (chief editor F4).
- Ch08 sidebar on the four-part runtime machine (chief editor's amendment to F0).
- Onboarding pathway sidebar in Ch08 ("Your First Week") (dev-lead F5).
- Title polishing — the words "lifecycle" and "boundary" and "machine" are all overloaded; check during drafting.

## Decisions for the final arc

Adopting findings A through I, the final arc's TOC becomes:

```
Part III — For Practitioners
  Ch08  The Practitioner's Mindset                       [KEEP+sidebar]
  Ch09  The Runtime Machine                              [NEW; opens with failure]
  Ch10  The Instrumented Codebase                        [RESTRUCTURE]
  Ch11  The PROSE Specification                          [KEEP]
  Ch12  The Load Lifecycle                               [NEW; deterministic mechanics]
  Ch13  Attention and Context Economy                    [NEW; probabilistic disciplines]
  Ch14  The Deterministic / Probabilistic Boundary       [NEW; opens with failure]
  Ch15  Multi-Agent Orchestration                        [KEEP+ADD; threading 2x2]
  Ch16  The Execution Meta-Process                       [KEEP]
  Ch17  Anti-Patterns and the Agent Stack Trace          [KEEP+EXTEND; checklist]
  Ch18  Primitives as Code                               [NEW; opens with failure]
  Ch19  What Comes Next                                  [KEEP]

Appendix A  The Cross-Harness Reference                  [NEW; dated snapshot]
```

Net change vs original Ch08-Ch15: 4 new chapters inserted (Ch09 Runtime Machine, Ch12 Load Lifecycle, Ch13 Attention Economy, Ch14 Deterministic/Probabilistic Boundary, Ch18 Primitives as Code — five new chapters total counting the Ch12 split), one reference appendix added, all original chapters preserved (some renumbered, some restructured). Total practitioner block grows from 8 chapters to 13 chapters plus one appendix.

## No Round 2 needed

Convergence was achieved on Round 1 (7/7 minor revisions, zero contradictions). The findings are concrete and non-conflicting. Proceed to `04-FINAL-ARC-PROPOSAL.md` incorporating findings A through I.

## Decision log (chief editor's prerogative)

- Keep the Ch12 split (finding A) — load-bearing.
- Demote Ch18 to Appendix A (finding B) — load-bearing.
- Open three new chapters with concrete failures (finding C) — load-bearing.
- Adopt findings D through I as drafting requirements baked into the per-chapter sections of the final arc.
- Defer chapter-title polishing to drafting; current names are working titles.
- Defer the implementation Wave plan refinement to the final arc's section 9 (decomposition).

End of synthesis. Proceeding to final arc.
