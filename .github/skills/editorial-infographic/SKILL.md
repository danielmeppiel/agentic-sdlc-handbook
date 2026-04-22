---
name: editorial-infographic
description: "Single-page, longform infographic for thought leadership posts. Multi-agent panel pipeline: Architect (structure) + Illustrator (visual) + Skeptic (fidelity), arbitrated by an Editor. Source-verbatim (no invented vocabulary), branded (dark masthead + dark CTA footer bookending cream content), and conversion-optimized (the URL is the artifact's loudest element). Use when shipping a 1-pager derived from authored long-form content (book chapter, research paper, methodology spec) for LinkedIn, X, blog hero, or conference handout. Triggers: editorial infographic, longform infographic, 1-pager, one pager, chapter infographic, book chapter visual, thought leadership chart, panel-reviewed visual, methodology infographic, framework infographic, visual essay, LinkedIn long image."
license: CC-BY-NC-4.0
metadata:
  author: "Daniel Meppiel"
  source: "Distilled from The Agentic SDLC Handbook Ch.7 LinkedIn pipeline"
  prose-style: "Designed against PROSE — danielmeppiel.github.io/awesome-ai-native/docs/prose/"
---

# Editorial Infographic — Multi-Agent Panel Pipeline

A 1-pager that earns its space. Not a slide deck flattened to a poster, not a carousel collapsed to a wall of text. **Source-grounded, panel-reviewed, brand-consistent.**

This skill is **PROSE-shaped**: instructions are progressively disclosed, work is decomposed into right-sized phases, primitives compose, three hard rules bound the failure modes, and specificity increases as you move from this file into `references/` and the agent personas.

## When to use this

- You have **already-authored long-form content** (book chapter, paper, methodology) you want to compress into one shareable image.
- The audience is **practitioners or leaders who already read a lot of BS** on this topic — generic frameworks won't land. Specificity will.
- The goal is **thought leadership + conversion** (drive readers back to the source). Not pure aesthetics; not pure data viz.

If the source is short, a tweet/text post is better. If the source needs swiping, use `social-media-carousel`. If the goal is pure visual art, use `canvas-design`.

## Agent panel roster

The skill orchestrates four specialized agents. **Persona detail lives in the linked `.agent.md` files — read them before invoking.** This skill orchestrates only.

| Agent | Persona | Owns |
|-------|---------|------|
| [Infographic Architect](../../agents/infographic-architect.agent.md) | Information structure reviewer | Section count, section names (action verbs), reading order, what to cut |
| [Infographic Illustrator](../../agents/infographic-illustrator.agent.md) | Visual editor | Brand chrome enforcement, color discipline, layout pattern per section, visual rhythm |
| [Infographic Skeptic](../../agents/infographic-skeptic.agent.md) | Domain authority (calibrated at runtime) | Source fidelity (line-by-line), taxonomy match, bullshit detection, leave-with quote uniqueness |
| [Infographic Editor](../../agents/infographic-editor.agent.md) | Orchestrator & arbiter | Convening the panel, resolving conflicts, holding the human approval gate, final ship call |

### Routing topology

```
                    ┌──────────────────────┐
                    │  source extracts +   │
                    │  brief + audience    │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │  ARCHITECT  │  │ ILLUSTRATOR │  │   SKEPTIC   │
       │  structure  │  │   visual    │  │  fidelity   │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │ proposals      │ spec           │ flags
              └────────────────┼────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │       EDITOR         │
                    │  synthesize · resolve │
                    │  conflicts · arbitrate│
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │  ASCII MOCKUP →      │
                    │  HUMAN APPROVAL GATE │
                    └──────────┬───────────┘
                               ▼
                          render → review
```

- **Specialists raise findings independently** — no implicit consensus.
- **Editor arbitrates.** When the Skeptic vetoes on source fidelity, the Skeptic wins. When the Architect and Illustrator disagree on section count vs visual rhythm, the Editor decides and documents why.
- **The human is the gate** between mockup and render. The Editor cannot bypass it.

## The Three Hard Rules

These are non-negotiable. They exist because every previous failure mode of this format violated one of them.

### Rule 1 — Verbatim from source

Every claim, definition, criterion, and section name must be **traceable to a line in the source document**. The Skeptic enforces this line-by-line. Invented vocabulary is the most common cause of this format failing — practitioners detect it instantly.

### Rule 2 — Panel before render

You **MUST** run the panel pipeline and produce an **ASCII mockup** for human approval *before* writing render code. The Editor holds this gate.

*Why:* Pixels are expensive to iterate. Layout decisions made in ASCII cost minutes; the same decisions made in PIL cost hours.

### Rule 3 — Brand chrome bookends only

Dark (INK) backgrounds appear in **exactly two places**: the masthead band and the CTA footer band. Body sections are always cream-on-INK-text. The Illustrator enforces this. *No "look at me" dark slabs in the body.*

## The Pipeline (5 phases)

The Editor orchestrates these. Each phase has a fresh, focused scope.

| Phase | Owner | Output |
|-------|-------|--------|
| 1. Source extraction | You (the orchestrator) | Verbatim extracts with line citations, audience brief |
| 2. Panel synthesis | Editor invokes Architect + Illustrator + Skeptic in parallel | Three independent proposals |
| 3. ASCII mockup + human gate | Editor synthesizes; you present to user | Approved single-design mockup |
| 4. Render | You (or a subagent) using `assets/starter_template.py` | PNG at ~2400 × ~5500 supersampled |
| 5. Review | Editor runs `references/REVIEW_CHECKLIST.md` | Ship verdict; failures route back to Phase 2 |

For phase-by-phase invocation prompts and conflict-resolution rules, see [`references/PIPELINE.md`](references/PIPELINE.md).

## Composing with other skills

- After shipping the image, draft the LinkedIn post body separately. The image's role is the **payoff**; the post's role is the **hook**.
- For a swipeable variant, slice the same content into a PDF carousel via `social-media-carousel`. Same content, different layout — never share both.
- For a printed handout, export the same PNG at 300dpi and add to a PDF cover sheet.

## Outputs

- A single PNG at the source's native long-portrait ratio (typically ~2400 × 5500 px after SCALE=2 supersampling).
- Save to `~/Desktop/<source-slug>-<topic-slug>.png`.
- Optionally: a copy at `<source-repo>/assets/<chapter>-<topic>.png` for use as a chapter `image:` social card (see [Distribution after ship](references/REVIEW_CHECKLIST.md#distribution-after-ship)).

## File map

- [`references/PIPELINE.md`](references/PIPELINE.md) — phase recipes, invocation prompts, conflict-resolution rules
- [`references/BRAND_SYSTEM.md`](references/BRAND_SYSTEM.md) — colors, fonts, chrome recipe, SCALE pattern (Illustrator's operating manual)
- [`references/LAYOUT_PATTERNS.md`](references/LAYOUT_PATTERNS.md) — six tested patterns (A–F) and when to use which
- [`references/REVIEW_CHECKLIST.md`](references/REVIEW_CHECKLIST.md) — Phase 5 ship gate + Tier 1/2/3 distribution playbook
- [`assets/starter_template.py`](assets/starter_template.py) — the renderer with helpers, brand tokens, masthead + 4-section + CTA footer skeleton
- [`assets/ascii_mockup_template.md`](assets/ascii_mockup_template.md) — Phase 3 fill-in-the-blanks scaffold

Agent personas live one level up:

- [`../../agents/infographic-architect.agent.md`](../../agents/infographic-architect.agent.md)
- [`../../agents/infographic-illustrator.agent.md`](../../agents/infographic-illustrator.agent.md)
- [`../../agents/infographic-skeptic.agent.md`](../../agents/infographic-skeptic.agent.md)
- [`../../agents/infographic-editor.agent.md`](../../agents/infographic-editor.agent.md)
