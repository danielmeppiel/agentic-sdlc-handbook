# ASCII Mockup Template — Phase 3 Gate

Fill this in **after** Phase 2 (panel synthesis) and **before** Phase 4 (render).
Show the completed mockup to the user. Wait for explicit approval. Do not render
until approved.

This is a fixed-width preview of the entire page, masthead through footer.
Width below is ~76 chars to fit comfortably in chat. The actual render is
1200 × ~2700 logical px (2400 × ~5400 supersampled).

```
┌────────────────────────────────────────────────────────────────────────────┐
│  THE  PUBLICATION  NAME                                  CHAPTER  N        │
│  ────────────────────────────────────────────────────────────────────────  │
│  PIECE TITLE                                  FREE ONLINE · PDF · EPUB     │
└────────────────────────────────────────────────────────────────────────────┘

                          Page Title Line 1
                          Subtitle (italic)

           One- to two-sentence thesis. Sets the frame for the
                  four sections below. Centered, serif.
   ─────────────────────────────────────────────────────────────────────

   01  VERB ONE                            italic kicker that names subject
   ═════════════════════════════════════════════════════════════════════
   <inner layout — pick from LAYOUT_PATTERNS.md and SKETCH IT HERE>
   <e.g., 4-row matrix with column verdicts, OR two-column definition,
   OR lifecycle bar, OR half-and-half list>


   02  VERB TWO                            italic kicker that names subject
   ═════════════════════════════════════════════════════════════════════
   <DIFFERENT layout pattern than section 01>


   03  VERB THREE                          italic kicker that names subject
   ═════════════════════════════════════════════════════════════════════
   <yet another layout — visual rhythm matters>


   04  VERB FOUR                           italic kicker that names subject
   ═════════════════════════════════════════════════════════════════════
   <last layout pattern>

   ─────────────────────────────────────────────────────────────────────
            <leave-with quote — verbatim from source —
              broken into rhythmic lines, italic serif,
                centered, with one phrase optionally
                  emphasized in INK vs INK_SOFT>
   ─────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────────────────────┐
│        READ THE FULL CHAPTER — AND THE REST. (ochre kicker)                │
│                                                                            │
│                       The Book Title (display)                             │
│                          by Author Name                                    │
│                                                                            │
│                  Read free online  ·  PDF  ·  EPUB                         │
│                  url-goes-here-underlined-in-mono                          │
└────────────────────────────────────────────────────────────────────────────┘
```

## Pre-approval checklist (orchestrator runs before showing user)

- [ ] Section names are action verbs (not nouns).
- [ ] Each section has its italic kicker line.
- [ ] No two consecutive sections use the same layout pattern.
- [ ] Leave-with quote is verbatim from source AND topic-unique.
- [ ] CTA footer has the full stack: kicker → book title → byline → format → URL.
- [ ] Masthead has chapter label (signals "there's more").
- [ ] Page title + thesis combine to give a complete pitch in 4 seconds.

## Asking for approval

Present the mockup to the user with this format:

> Here is the proposed layout for `<topic>`. Before I render:
> - Section structure: `<list>`
> - Layout patterns: `<section1: pattern, section2: pattern, ...>`
> - Leave-with quote: `<verbatim quote>` (source line `<N>`)
>
> Approve, or which sections to revise?

Do **not** start rendering on a "looks good" — wait for an explicit "render" or "go".
