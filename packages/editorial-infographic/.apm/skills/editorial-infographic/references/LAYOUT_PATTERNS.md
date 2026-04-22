# LAYOUT_PATTERNS — Section Recipes

A library of section internal layouts. Each pattern is a tested shape. The Illustrator panelist picks one per section based on content shape; consecutive sections must use **different patterns** (visual rhythm).

## Pattern A — Verdict Matrix

**Use when:** the content scores subjects across dimensions and produces an action verdict per column. Example: ASSESS readiness across CODEBASE / PROCESS / SKILL / CULTURE → NOT READY / PARTIAL / READY → onboarding wave.

```
                    NOT READY      PARTIAL        READY
                    ──────────────────────────────────────
  CODEBASE          ▪ verbatim     ▪ verbatim     ▪ verbatim
                      criterion      criterion      criterion
                    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
  PROCESS           ▪ ...          ▪ ...          ▪ ...
                    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
  SKILL             ▪ ...          ▪ ...          ▪ ...
                    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
  CULTURE           ▪ ...          ▪ ...          ▪ ...
                    ──────────────────────────────────────
  ONBOARDING WAVE   ONBOARD LAST   PREP, THEN     PILOT WAVE
                                   ONBOARD        FIRST
```

**Rules:** column headers in their accent color (RED / OCHRE / GREEN). Row labels in INK sans_bold. Cells in mono_reg, color-matched to column. Always end with an action-verdict legend strip — without it the matrix is reference, not decision-making.

## Pattern B — Two-Column Definition

**Use when:** introducing two parallel concepts that need equal weight (two roles, two failure modes, two metrics families). Example: DEFINE ROLES → CONTEXT ENGINEER | AGENT OPERATIONS SPECIALIST.

```
  KICKER (ochre, all-caps, full width)

  LABEL ONE                 LABEL TWO
  ──────────                ──────────
  definition wraps to       definition wraps to
  multiple lines, kept      multiple lines, kept
  parallel to right         parallel to left
  column                    column
```

**Rules:** labels in mono_bold, definitions in sans_reg. Column widths equal. If one definition is shorter, accept the asymmetry — do not pad. Optional qualifier line under one label (mono_reg, INK_FAINT) like "— emerges at Phase 4".

## Pattern C — Lifecycle Bar

**Use when:** content is a sequence of phases, each with entry/exit/rollback. Example: ROLL OUT → PILOT → EXPAND → SCALE.

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │ PILOT    │ ─→ │ EXPAND   │ ─→ │ SCALE    │
  │ 1–2 teams│    │ 3–5 teams│    │ all teams│
  └──────────┘    └──────────┘    └──────────┘
   EXIT: ...      EXIT: ...      EXIT: ...      ← green
   ROLLBACK: ...  ROLLBACK: ...  ROLLBACK: ...  ← red
```

**Rules:** equal-width boxes, arrows between (not just gaps). EXIT signals always green, ROLLBACK signals always red. Phase duration as a small mono_reg line under the title.

## Pattern D — Half-and-Half (qualitative + quantitative)

**Use when:** a section has two halves that contrast — leading indicators vs. lagging indicators, what-to-measure vs. what-not-to-measure. Example: MEASURE → leading | lagging.

```
  KICKER LEFT                       KICKER RIGHT
  ──────────────────────────────────────────────────
  body text or list             |  body text or list
  on the left half              |  on the right half
                                |
```

**Rules:** vertical rule (RULE color, 1px) divides the two halves. Each half gets its own kicker. Lists use small bullets (filled circles). Asymmetric content lengths are fine.

## Pattern E — Flat List with Inline Verdicts

**Use when:** a checklist or principles set where each item carries its own status marker. Example: ANTI-PATTERNS → checks/crosses inline.

```
  ✓  Principle / pattern that works (verbatim)
  ✓  Another verbatim principle
  ✗  Anti-pattern (verbatim)
  ✗  Another anti-pattern
```

**Rules:** check marker GREEN, cross marker RED. Items in sans_reg. No bullets — the verdict is the visual marker.

## Pattern F — Quote-as-Section

**Use when:** the source has a single passage so distilled it deserves its own visual moment, and breaking it into bullets would dilute it. Example: a foundational principle that anchors the methodology.

```
                                                  
                                                  
       Long-form pull quote in serif italic,      
       broken across 3–4 lines, centered,         
       maybe with the central phrase in INK       
       and the surrounding text in INK_SOFT.      
                                                  
       — ATTRIBUTION (mono_reg, small)            
                                                  
```

**Rules:** Use sparingly — at most one Pattern F per page (typically the leave-with). Consumes vertical space; earn it.

## Choosing a pattern (Illustrator's heuristic)

| Content shape | Pattern |
|---|---|
| Score subjects on dimensions, produce verdict | A — Verdict Matrix |
| Two parallel concepts of equal weight | B — Two-Column Definition |
| Sequence of phases with gates | C — Lifecycle Bar |
| Contrast (do / don't, leading / lagging) | D — Half-and-Half |
| Checklist of patterns + anti-patterns | E — Flat List |
| Single distilled principle | F — Quote-as-Section |

**Never use the same pattern twice in a row.** If two consecutive sections want Pattern A, the Illustrator must convert one to a different shape (often A → D works, or A → E if the columns collapse to a single dimension).
