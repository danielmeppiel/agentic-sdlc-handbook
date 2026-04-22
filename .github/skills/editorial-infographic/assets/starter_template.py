"""
Editorial Infographic — Starter Template

A reusable scaffold for a 1-page longform infographic. Distilled from
The Agentic SDLC Handbook Ch.7 build. Ships as: dark masthead band → cream
body with 3–5 numbered sections → dark CTA footer band.

USAGE
─────
1. Run the panel pipeline (references/PIPELINE.md) and approve an ASCII
   mockup (assets/ascii_mockup_template.md) BEFORE editing this file.
2. Update the CONFIG block (publication, chapter, title, URL).
3. Replace each "SECTION N — VERB" block with your approved content.
4. Replace the LEAVE-WITH quote block with your verbatim source quote.
5. Run: python3 starter_template.py
6. Run REVIEW_CHECKLIST.md before declaring shipped.

DO NOT
──────
- Do not call PIL primitives directly. Use the helpers (text, hline, rect, ...).
- Do not introduce a third dark band. Chrome bookends only.
- Do not add a fifth color to the palette.
- Do not add a section without panel review.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# ═══ CONFIG — EDIT THESE ═════════════════════════════════════════════════════
PUBLICATION    = "THE  PUBLICATION  NAME"          # masthead top-left
CHAPTER_LABEL  = "CHAPTER  N"                       # masthead top-right
PIECE_TITLE    = "THIS  PIECE  TITLE"               # masthead bottom-left
FORMAT_LINE    = "FREE  ONLINE  ·  PDF  ·  EPUB"   # masthead bottom-right + CTA
PAGE_TITLE_1   = "Page Title Line 1"                # display serif
PAGE_TITLE_2   = "Subtitle (italic)"                # serif italic
THESIS_LINES   = [                                  # serif regular, centered
    "One- to two-sentence thesis.",
    "Sets the frame for the four sections below.",
]
CTA_KICKER     = "READ THE FULL CHAPTER — AND THE REST."
BOOK_TITLE     = "The Book Title"
AUTHOR_LINE    = "by Author Name"
URL            = "your-url-here.example.com"
OUTPUT_PATH    = Path.home() / "Desktop" / "infographic.png"

FONTS_DIR = Path(__file__).resolve().parents[2] / "canvas-design" / "canvas-fonts"

# ═══ BRAND TOKENS ════════════════════════════════════════════════════════════
SCALE = 2  # supersampling — render 2× for retina-sharp; DO NOT CHANGE.
W, H_MAX = 1200, 6000  # H_MAX is upper bound; canvas is cropped at the end.
ML, MR = 80, 80
CW = W - ML - MR

CREAM       = (245, 241, 234)
CREAM_DEEP  = (238, 233, 222)
INK         = (26, 35, 50)
INK_SOFT    = (78, 88, 104)
INK_FAINT   = (140, 145, 155)
RULE        = (200, 195, 184)
RULE_SOFT   = (220, 215, 205)
RED         = (176, 58, 46)
GREEN       = (25, 111, 61)
OCHRE       = (176, 130, 35)
OCHRE_DARK  = (232, 198, 120)  # ochre that reads on INK background
LIGHT_CREAM = (210, 205, 195)  # light cream for de-emphasized text on INK

img = Image.new("RGB", (W * SCALE, H_MAX * SCALE), CREAM)
d = ImageDraw.Draw(img)

# ═══ FONT LOADERS ════════════════════════════════════════════════════════════
def f(name, size):
    return ImageFont.truetype(str(FONTS_DIR / name), int(size * SCALE))

serif_display = lambda s: f("CrimsonPro-Bold.ttf", s)
serif_italic  = lambda s: f("CrimsonPro-Italic.ttf", s)
serif_reg     = lambda s: f("CrimsonPro-Regular.ttf", s)
sans_bold     = lambda s: f("WorkSans-Bold.ttf", s)
sans_reg      = lambda s: f("WorkSans-Regular.ttf", s)
sans_light    = lambda s: f("WorkSans-Regular.ttf", s)  # canvas-fonts has no Light
mono_reg      = lambda s: f("IBMPlexMono-Regular.ttf", s)
mono_bold     = lambda s: f("IBMPlexMono-Bold.ttf", s)

# ═══ HELPERS — always use these, never PIL directly in body code ═════════════
def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x * SCALE, y * SCALE), s, font=font, fill=fill, anchor=anchor)

def hline(x1, x2, y, color=RULE, width=1):
    d.line([(x1 * SCALE, y * SCALE), (x2 * SCALE, y * SCALE)],
           fill=color, width=width * SCALE)

def vline(x, y1, y2, color=RULE, width=1):
    d.line([(x * SCALE, y1 * SCALE), (x * SCALE, y2 * SCALE)],
           fill=color, width=width * SCALE)

def rect(box, fill=None, outline=None, width=1):
    sb = [c * SCALE for c in box]
    d.rectangle(sb, fill=fill, outline=outline, width=width * SCALE)

def tw(s, font):
    """Logical (1×) text width."""
    return d.textlength(s, font=font) / SCALE

def wrap(text_str, font, max_w):
    """Greedy word-wrap → list of lines."""
    words = text_str.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if tw(trial, font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_bullet(x, y, color, size=6):
    px, py = x * SCALE, y * SCALE
    sz = size * SCALE
    d.polygon([(px, py), (px + sz + 2 * SCALE, py + sz), (px, py + sz * 2)],
              fill=color)

def draw_check(x, y, color, size=12, w=2):
    px, py, sz = x * SCALE, y * SCALE, size * SCALE
    d.line([(px, py + sz // 2 + SCALE), (px + sz // 2 - SCALE, py + sz)],
           fill=color, width=w * SCALE)
    d.line([(px + sz // 2 - SCALE, py + sz), (px + sz + SCALE, py + SCALE)],
           fill=color, width=w * SCALE)

def draw_cross(x, y, color, size=12, w=2):
    px, py, sz = x * SCALE, y * SCALE, size * SCALE
    d.line([(px, py + SCALE), (px + sz, py + sz + SCALE)],
           fill=color, width=w * SCALE)
    d.line([(px, py + sz + SCALE), (px + sz, py + SCALE)],
           fill=color, width=w * SCALE)

def section_header(y, number, verb, kicker):
    """Standard section header. Returns the new y after the header block.

    Pattern: `01  ASSESS                          italic kicker right-aligned`
    """
    text(ML, y, number, mono_bold(15), fill=INK)
    text(ML + 50, y - 1, verb, sans_bold(20), fill=INK)
    text(W - MR, y + 4, kicker, serif_italic(17), fill=INK_SOFT, anchor="ra")
    y += 30
    hline(ML, W - MR, y, INK, 2)
    return y + 22

# ═══ MASTHEAD — dark band #1 (top bookend) ═══════════════════════════════════
mast_h = 116
rect([0, 0, W, mast_h], fill=INK)

y = 50
text(ML, y, PUBLICATION, mono_reg(14), fill=OCHRE_DARK)
text(W - MR, y, CHAPTER_LABEL, mono_reg(14), fill=OCHRE_DARK, anchor="ra")
y += 26
hline(ML, W - MR, y, CREAM, 2)
y += 10
text(ML, y, PIECE_TITLE, mono_reg(11), fill=LIGHT_CREAM)
text(W - MR, y, FORMAT_LINE, mono_reg(11), fill=LIGHT_CREAM, anchor="ra")

y = mast_h + 8
hline(ML, W - MR, y, RULE, 1)

# ═══ TITLE + THESIS ══════════════════════════════════════════════════════════
y += 56
text(W // 2, y, PAGE_TITLE_1, serif_display(82), anchor="ma")
y += 96
text(W // 2, y, PAGE_TITLE_2, serif_italic(82), anchor="ma")
y += 110

for line in THESIS_LINES:
    text(W // 2, y, line, serif_reg(23), fill=INK_SOFT, anchor="ma")
    y += 32
y += 30
hline(ML, W - MR, y, RULE, 1)
y += 36

# ═══ SECTION 01 ══════════════════════════════════════════════════════════════
y = section_header(y, "01", "VERB ONE", "italic kicker that names the subject")

# REPLACE THIS BLOCK with your panel-approved content for section 1.
# Pick a layout pattern from references/LAYOUT_PATTERNS.md.
# Example: simple two-column body.
half_w = (CW - 40) // 2
text(ML, y, "LEFT KICKER", mono_bold(11), fill=OCHRE)
text(ML + half_w + 40, y, "RIGHT KICKER", mono_bold(11), fill=OCHRE)
y += 22
for line in wrap("Replace this with verbatim or distilled content from the source.", serif_reg(17), half_w):
    text(ML, y, line, serif_reg(17), fill=INK_SOFT)
    y += 24
y += 30

# ═══ SECTION 02 ══════════════════════════════════════════════════════════════
y = section_header(y, "02", "VERB TWO", "italic kicker that names the subject")

# REPLACE — use a DIFFERENT layout pattern than section 01.
text(ML, y, "Replace with section 2 content. Use a different pattern (matrix, lifecycle, etc.).",
     serif_reg(17), fill=INK_SOFT)
y += 80

# ═══ SECTION 03 ══════════════════════════════════════════════════════════════
y = section_header(y, "03", "VERB THREE", "italic kicker that names the subject")

text(ML, y, "Replace with section 3 content.", serif_reg(17), fill=INK_SOFT)
y += 80

# ═══ SECTION 04 ══════════════════════════════════════════════════════════════
y = section_header(y, "04", "VERB FOUR", "italic kicker that names the subject")

text(ML, y, "Replace with section 4 content.", serif_reg(17), fill=INK_SOFT)
y += 80

# ═══ LEAVE-WITH QUOTE ════════════════════════════════════════════════════════
# Verbatim from source. Single distilled principle. Do not use generic
# motivational closings. Pattern F from LAYOUT_PATTERNS.md.
y += 14
hline(ML, W - MR, y, INK, 2)
y += 36
quote_lines = [
    "Replace with the verbatim",
    "leave-with quote from",
    "the source — broken into",
    "rhythmic lines, centered.",
]
for line in quote_lines:
    text(W // 2, y, line, serif_italic(38), fill=INK, anchor="ma")
    y += 48
y += 30
hline(ML, W - MR, y, INK, 2)
y += 28

# ═══ CTA FOOTER — dark band #2 (bottom bookend) ══════════════════════════════
y += 24
cta_top = y
cta_h = 256
rect([0, cta_top, W, cta_top + cta_h], fill=INK)

inner = cta_top + 32
text(W // 2, inner, CTA_KICKER, mono_bold(12), fill=OCHRE_DARK, anchor="ma")
inner += 38
text(W // 2, inner, BOOK_TITLE, serif_display(34), fill=CREAM, anchor="ma")
inner += 44
text(W // 2, inner, AUTHOR_LINE, serif_italic(17), fill=LIGHT_CREAM, anchor="ma")
inner += 36
text(W // 2, inner, FORMAT_LINE.replace("  ·  ", "  ·  "), serif_italic(16),
     fill=LIGHT_CREAM, anchor="ma")
inner += 32

# URL is the loudest element by design. Underlined.
text(W // 2, inner, URL, mono_bold(17), fill=CREAM, anchor="ma")
url_w = tw(URL, mono_bold(17))
hline(int(W // 2 - url_w / 2), int(W // 2 + url_w / 2),
      inner + 26, CREAM, 1)

y = cta_top + cta_h

# ═══ FINAL CROP + SAVE ═══════════════════════════════════════════════════════
final_h = y + 60
final = img.crop((0, 0, W * SCALE, final_h * SCALE))

if OUTPUT_PATH.exists():
    OUTPUT_PATH.unlink()
final.save(OUTPUT_PATH, "PNG", optimize=True, dpi=(440, 440))
print(f"Wrote {OUTPUT_PATH}  ({W * SCALE}x{final_h * SCALE})")
