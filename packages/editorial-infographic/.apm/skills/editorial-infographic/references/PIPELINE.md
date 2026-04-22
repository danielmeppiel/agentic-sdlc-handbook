# PIPELINE — Phase Recipes & Conflict Resolution

This file is loaded by the [Infographic Editor](../../../agents/infographic-editor.agent.md) when orchestrating the 5-phase pipeline. Persona detail lives in the agent files; this file is the **routing recipe**.

## Phase 1 — Source extraction (you, the orchestrator)

Before the panel can convene, you need the raw material. Do this yourself.

1. Read the entire source chapter / document.
2. Extract candidate material with **line citations**:
   - Candidate section topics (3–8 — the panel will cut to 4)
   - Verbatim taglines / lede sentences
   - Verbatim criteria, lists, role definitions, framework names
   - 5–10 candidate leave-with quotes (verbatim)
3. Draft a one-paragraph **audience brief**: who is the practitioner the page is for? What do they read? What have they seen too many times?

**Output:** A working notes block you'll pass to all four agents.

## Phase 2 — Convene the panel (Editor)

The [Infographic Editor](../../../agents/infographic-editor.agent.md) invokes three panelists **in parallel** using the Task tool with `mode: sync`:

### Invocation 1 — Architect

```
Task: infographic-architect (or general-purpose with the agent file as context)
Prompt:
  You are the Infographic Architect (load .github/agents/infographic-architect.agent.md
  and follow it as your operating manual).

  Source extracts (verbatim, with line numbers):
    <paste Phase 1 extracts>

  Audience brief:
    <paste Phase 1 brief>

  Goal of the post:
    <e.g., "drive engineering leaders back to Ch7 of the free book">

  Produce your output in the format your agent file specifies (THESIS, LEAVE-WITH,
  SECTIONS, PAGE TITLE, THESIS LINES).
```

### Invocation 2 — Illustrator

```
Task: infographic-illustrator
Prompt:
  You are the Infographic Illustrator (load .github/agents/infographic-illustrator.agent.md
  and follow it as your operating manual).

  Read references/BRAND_SYSTEM.md and references/LAYOUT_PATTERNS.md before
  responding.

  Source extracts and audience brief:
    <same as Architect>

  Goal:
    <same>

  Important: you may not yet have the Architect's section list (parallel invocation).
  Propose layout patterns based on the source extracts' content shape, and produce
  the visual rhythm map. The Editor will reconcile with the Architect's section
  count in synthesis.

  Produce your output in the format your agent file specifies.
```

### Invocation 3 — Skeptic (calibrated)

```
Task: infographic-skeptic
Prompt:
  You are the Infographic Skeptic (load .github/agents/infographic-skeptic.agent.md
  and follow it as your operating manual).

  CALIBRATION:
    Professional role: <e.g., "VP of Engineering at a Series-B SaaS, leads 80
                       engineers across 12 teams">
    Daily reading: <e.g., "HN front page, Anthropic + OpenAI engineering blogs,
                   simonw, Latent Space, Cursor / Codex / Claude Code commentary">
    Already seen 50 times this year: <e.g., "AI hype decks, generic 'culture
                                     eats strategy' frameworks, vendor pitches
                                     dressed as methodology">
    Would actually pay for: <e.g., "concrete role definitions, real metrics,
                            rollback criteria written by someone who shipped
                            this in production">

  Source document path: <path or paste of the full source chapter>

  Proposed infographic content: <on first pass: source extracts as the candidate
                                   set; on second pass after Architect: the
                                   architect's actual proposal>

  Produce your output in the format your agent file specifies (LINE-BY-LINE
  FIDELITY REVIEW, LEAVE-WITH VERDICT, TAXONOMY DRIFT, etc.).
```

**The Editor MUST set the calibration.** A generic skeptic produces generic feedback. If the calibration block is empty or vague, the Skeptic will refuse and ask for it (per its agent file).

## Phase 3 — Synthesize (Editor) and present mockup (you)

The Editor reconciles the three outputs into a single ASCII mockup. Common conflicts and their default resolutions:

| Conflict | Default resolution | Override conditions |
|---|---|---|
| Architect: 4 sections / Illustrator: 5 (fifth is a quote) | Fold the 5th into the leave-with | Keep 5 only if the quote isn't from the source |
| Architect: 4 / Illustrator: 5 (fifth is content) | Default to 4; ask Architect to merge two | Keep 5 only if the page would lose a critical answer |
| Illustrator wants a dark slab on body section "for emphasis" | Reject (Hard Rule #3) | None |
| Skeptic: 3 invented sentences flagged | Swap for verbatim quotes; re-show to Skeptic for ratification | None — fidelity is the ceiling |
| Architect proposes a noun-named section | Bounce back to Architect with the rule cited | None — verb hard rule |
| Illustrator chose two consecutive grids | Bounce back to Illustrator: convert one to a different pattern | None — rhythm hard rule |
| Skeptic and Architect disagree on whether a sentence is "in source" | Editor reads the source line themselves and decides | None |
| Skeptic flags the leave-with as topic-generic | Replace with a Skeptic-proposed alternative | Keep only if the user has a specific reason |

After resolution, the Editor produces the mockup using [`../assets/ascii_mockup_template.md`](../assets/ascii_mockup_template.md), then **you (the orchestrator) present it to the human user** with the structure specified in the Editor's agent file.

**Wait for explicit "render" / "go" / "ship".** No exceptions.

## Phase 4 — Render

Once approved:

1. Copy `assets/starter_template.py` to a working location (or edit in place if iterating).
2. Update the CONFIG block (publication, chapter, title, URL).
3. Replace each section block with the panel-approved content.
4. Run `python3 starter_template.py`.
5. Inspect the PNG.

The renderer uses `SCALE=2` supersampling — final image is ~2400 × ~5500 px.

## Phase 5 — Review

The Editor runs [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md) top to bottom. Any unchecked item routes the failing region back to Phase 2 — **only that region**, with the appropriate panelist re-invoked with the user's specific feedback as a constraint.

Do **not** patch issues in isolation without panel re-review. Patches without panel re-review are how the wall-of-text failure mode reappears: each individual fix looks fine, the page as a whole gets denser.

## Iteration discipline

If the user rejects a section after rendering:

1. Editor re-convenes the **specific** failing panelist (Architect for structure issues, Illustrator for visual issues, Skeptic for fidelity issues).
2. Pass the user's specific feedback as a constraint.
3. Editor re-synthesizes the affected region.
4. Re-render only the affected section if possible (or the whole page if the change cascades).
5. Re-show ASCII mockup of the changed region to user before re-rendering.

## Composing this skill with others

This skill ends when the PNG ships. Everything after — LinkedIn post body, distribution sequence, repurposing — is composed with other skills:

- LinkedIn post body: a separate composition step (no skill yet — manual).
- PDF carousel variant: `social-media-carousel` skill, fed the same source material.
- Distribution playbook: see [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md#distribution-after-ship).
