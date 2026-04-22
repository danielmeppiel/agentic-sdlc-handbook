# BRAND_SYSTEM — Tokens, Chrome, Scale

The visual system. **Do not deviate without panel approval.** Consistency across infographics is what builds the recognizable visual brand.

## Canvas

| Property | Value | Why |
|---|---|---|
| Logical width | 1200 px | LinkedIn render width sweet spot |
| Logical height | variable, ~2700–3000 typical | Long portrait, content-driven |
| **Render scale** | **`SCALE = 2`** | Supersampled to 2400 × ~5500. Crisp on retina + zoom. **Non-negotiable.** |
| Background | `CREAM = (245, 240, 230)` | Editorial paper feel, not pure white |
| Margins | `ML = MR = 80` | Logical px |
| DPI on save | `(440, 440)` | Print-quality metadata |

## Color palette (4 colors only)

| Token | RGB | Role |
|---|---|---|
| `INK` | `(20, 25, 35)` | Body text, all section numbers, masthead band, CTA footer band |
| `INK_SOFT` | `(70, 75, 90)` | Section taglines (italic ledes), de-emphasized text |
| `INK_FAINT` | `(130, 135, 150)` | Captions, qualifiers (e.g., "— emerges at Phase 4") |
| `RED` | `(170, 60, 50)` | Warnings, NOT READY column, ROLLBACK markers, anti-patterns |
| `GREEN` | `(40, 130, 90)` | Readiness, EXIT signals, leading indicators, positive outcomes |
| `OCHRE` | `(190, 140, 50)` | Kickers ("TWO NEW ROLES", "TEAM TOPOLOGY"), small all-caps emphasis |
| `RULE` | `(180, 175, 165)` | Hairline dividers in body |
| `RULE_SOFT` | `(210, 205, 195)` | Inner-grid dividers |

**Color discipline rules** (panel-enforced):

1. **Every accent color must map to meaning, never aesthetics.** Red is danger; green is good; ochre is "look here." If you can't justify the color in one sentence, use INK.
2. **Section numbers (01/02/03/04) are always INK.** No rainbow.
3. **Body never uses dark backgrounds.** The chrome bookends own that treatment.
4. **OCHRE on dark masthead/footer** uses the lighter variant `(232, 198, 120)` for legibility on INK.

## Typography

Three families. Roles are strict.

| Family | When to use |
|---|---|
| **Serif display** (CrimsonPro Bold) | Page title, leave-with quote, CTA book title — anywhere the voice is *editorial* |
| **Sans bold** (WorkSans Bold; or Inter / IBM Plex Sans if available) | Section verbs (ASSESS / DEFINE ROLES / ROLL OUT / MEASURE), table column headers |
| **Mono regular & bold** (IBM Plex Mono) | Section numbers (01/02/03), kickers (small all-caps), masthead text, URL, criteria labels |

**Italic serif** (e.g., Source Serif Italic) is used for:
- Section taglines / ledes (the one-line italic under each section header)
- The leave-with quote
- Author byline ("by Daniel Meppiel")
- Disclaimers ("Create the role when the work exists, not when the job title sounds innovative.")

**Sizes (logical pt, before SCALE multiplication):**

| Use | Size |
|---|---|
| Page title (display serif) | 82 |
| Thesis lines (serif regular) | 23 |
| Section verb (sans bold) | 20 |
| Section tagline (serif italic) | 17 |
| Section number (mono bold) | 15 |
| Body text (sans regular) | 13–14 |
| Kicker (mono bold, all caps) | 11 |
| Leave-with quote (serif italic) | 38 (broken across lines) |
| CTA book title (serif display) | 34 |
| URL (mono bold) | 17 |
| Masthead text (mono regular) | 14 |
| Captions / disclaimers (mono regular) | 11 |

## The chrome bookends

The page has **exactly two dark bands.** Top and bottom. They are mirror images in function.

### Masthead band (top)

```
┌──────────────────────────────────────────────┐
│  THE  PUBLICATION  NAME       CHAPTER  VII   │  ← mono_reg(14), OCHRE-on-INK
│  ─────────────────────────────────────────   │  ← cream hairline
│  PIECE TITLE                FORMAT AFFORD.   │  ← mono_reg(11), light-cream-on-INK
└──────────────────────────────────────────────┘
                                                  ← height: ~116 px logical
```

- **Top-left:** publication / book identity (always)
- **Top-right:** chapter or piece number (signals depth, "there's more")
- **Bottom-left:** this piece's title
- **Bottom-right:** format/access affordance ("FREE ONLINE · PDF · EPUB")

### CTA footer band (bottom)

```
┌──────────────────────────────────────────────┐
│  KICKER LINE — UPPERCASE OCHRE               │  ← mono_bold(12), OCHRE-on-INK
│                                              │
│         The Book Title (display serif)       │  ← serif_display(34), CREAM
│             by Author Name (italic)          │  ← serif_italic(17), light cream
│                                              │
│      Read free online  ·  PDF  ·  EPUB       │  ← serif_italic(16), light cream
│      url-goes-here-underlined                │  ← mono_bold(17), CREAM, underlined
└──────────────────────────────────────────────┘
                                                  ← height: ~256 px logical
```

The footer is the page's loudest element by design. It must be **the URL** that's underlined, not the kicker.

## Helpers (in starter_template.py)

The renderer provides these so all body code stays in 1× logical coordinates:

| Helper | Purpose |
|---|---|
| `text(x, y, str, font, fill, anchor)` | Draws text at logical (x, y); helper handles SCALE |
| `hline(x1, x2, y, color, w)` | Horizontal rule |
| `vline(x, y1, y2, color, w)` | Vertical rule |
| `rect(box, fill, outline, width)` | Filled/outlined rectangle |
| `tw(str, font)` | Returns logical text width (FreeType width / SCALE) |
| `wrap(str, font, max_w)` | Greedy word-wrap → list of lines |
| `draw_bullet(x, y, color, size)` | Filled circle bullet |
| `draw_check(x, y, color, size)` / `draw_cross(...)` | Verdict markers |
| `f(name, size)` | Font getter (multiplies size by SCALE internally) |

**Never call PIL primitives directly in body code.** Use the helpers. They preserve SCALE invariants.
