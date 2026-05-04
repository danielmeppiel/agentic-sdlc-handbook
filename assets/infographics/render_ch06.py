"""
Ch06 Team Topologies — editorial infographic renderer (v2).

Source-of-truth content: assets/infographics/ch06-team-topologies.md
Brand spec: .github/skills/editorial-infographic/references/BRAND_SYSTEM.md
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# ═══ CONFIG ═════════════════════════════════════════════════════════════════
PUBLICATION    = "THE  AGENTIC  SDLC  HANDBOOK"
CHAPTER_LABEL  = "BLOCK  II  ·  LEADERS    CH  06"
PIECE_TITLE    = "THE AGENTIC SDLC ORG CHART  ·  CH 06  TEAM STRUCTURES"
FORMAT_LINE    = "FREE  ONLINE  ·  PDF  ·  EPUB"
CTA_FORMAT     = "Read free online  ·  PDF  ·  EPUB"
PAGE_TITLE_1   = "The Agentic SDLC"
PAGE_TITLE_2   = "Org Chart"
SUBTITLE_LINES = [
    "The hardest part of the Agentic SDLC is not the agents.",
    "It is the org chart. Three new seats appear at the table,",
    "existing roles evolve, and team composition tilts toward judgment.",
]
CTA_KICKER     = "READ THE FULL CHAPTER — AND THE OTHER 21."
BOOK_TITLE     = "The Agentic SDLC Handbook"
AUTHOR_LINE    = "by Daniel Meppiel"
URL            = "danielmeppiel.github.io/agentic-sdlc-handbook"

OUTPUT_PATH    = Path(__file__).resolve().parent / "ch06-team-topologies.png"
DESKTOP_COPY   = Path.home() / "Desktop" / "ch06-team-topologies.png"

FONTS_DIR = (Path(__file__).resolve().parents[2]
             / ".github" / "skills" / "canvas-design" / "canvas-fonts")

# ═══ BRAND TOKENS ═══════════════════════════════════════════════════════════
SCALE = 2
W, H_MAX = 1200, 6500
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
OCHRE_DARK  = (232, 198, 120)
LIGHT_CREAM = (210, 205, 195)

img = Image.new("RGB", (W * SCALE, H_MAX * SCALE), CREAM)
d   = ImageDraw.Draw(img)

# ═══ FONTS ══════════════════════════════════════════════════════════════════
def f(name, size):
    return ImageFont.truetype(str(FONTS_DIR / name), int(size * SCALE))

serif_display = lambda s: f("CrimsonPro-Bold.ttf", s)
serif_italic  = lambda s: f("CrimsonPro-Italic.ttf", s)
serif_reg     = lambda s: f("CrimsonPro-Regular.ttf", s)
sans_bold     = lambda s: f("WorkSans-Bold.ttf", s)
sans_reg      = lambda s: f("WorkSans-Regular.ttf", s)
mono_reg      = lambda s: f("IBMPlexMono-Regular.ttf", s)
mono_bold     = lambda s: f("IBMPlexMono-Bold.ttf", s)

# ═══ HELPERS ════════════════════════════════════════════════════════════════
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
    return d.textlength(s, font=font) / SCALE

def wrap(text_str, font, max_w):
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

def tri_up(x, y, color, size=10):
    """Filled equilateral-ish triangle pointing up."""
    s = size
    d.polygon([
        ((x) * SCALE,         (y + s) * SCALE),
        ((x + s) * SCALE,     (y + s) * SCALE),
        ((x + s / 2) * SCALE, (y) * SCALE),
    ], fill=color)

def circle(x, y, color, size=10):
    """Filled circle bullet, top-left at (x,y)."""
    d.ellipse([(x * SCALE, y * SCALE),
               ((x + size) * SCALE, (y + size) * SCALE)],
              fill=color)

def arrow_right(x, y, color, length=22, head=6, w=2):
    """Right-pointing arrow with shaft."""
    y_mid = y
    d.line([(x * SCALE, y_mid * SCALE),
            ((x + length) * SCALE, y_mid * SCALE)],
           fill=color, width=w * SCALE)
    d.polygon([
        ((x + length) * SCALE,        y_mid * SCALE),
        ((x + length - head) * SCALE, (y_mid - head / 2) * SCALE),
        ((x + length - head) * SCALE, (y_mid + head / 2) * SCALE),
    ], fill=color)

def warn_tri(x, y, color, size=18):
    """Warning triangle with exclamation, top-left at (x,y)."""
    d.polygon([
        ((x + size / 2) * SCALE, y * SCALE),
        (x * SCALE,             (y + size) * SCALE),
        ((x + size) * SCALE,    (y + size) * SCALE),
    ], outline=color, fill=None, width=2 * SCALE)
    # exclamation: dot + stem
    d.line([((x + size / 2) * SCALE, (y + size * 0.35) * SCALE),
            ((x + size / 2) * SCALE, (y + size * 0.70) * SCALE)],
           fill=color, width=2 * SCALE)
    d.ellipse([((x + size / 2 - 1.5) * SCALE, (y + size * 0.78) * SCALE),
               ((x + size / 2 + 1.5) * SCALE, (y + size * 0.92) * SCALE)],
              fill=color)

def red_x(x, y, color, size=12, w=2):
    d.line([(x * SCALE,            y * SCALE),
            ((x + size) * SCALE,   (y + size) * SCALE)],
           fill=color, width=w * SCALE)
    d.line([(x * SCALE,            (y + size) * SCALE),
            ((x + size) * SCALE,   y * SCALE)],
           fill=color, width=w * SCALE)

def section_header(y, number, verb, kicker, kicker_max_w=None):
    text(ML, y, number, mono_bold(15), fill=INK)
    text(ML + 50, y - 1, verb, sans_bold(20), fill=INK)
    # right-align kicker; if it overflows, shrink to fit
    k_font = serif_italic(17)
    if kicker_max_w and tw(kicker, k_font) > kicker_max_w:
        k_font = serif_italic(15)
    text(W - MR, y + 4, kicker, k_font, fill=INK_SOFT, anchor="ra")
    y += 30
    hline(ML, W - MR, y, INK, 2)
    return y + 24

def render_lines(lines, x, y, font, fill=INK, line_h=None):
    if line_h is None:
        line_h = font.size / SCALE + 6
    for line in lines:
        text(x, y, line, font, fill=fill)
        y += line_h
    return y

# ═══ MASTHEAD ═══════════════════════════════════════════════════════════════
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

# ═══ TITLE + SUBTITLE  (matches agentic-sdlc-rollout-strategy.png) ══════════
y += 60
text(W // 2, y, PAGE_TITLE_1, serif_display(80), anchor="ma")
y += 100
text(W // 2, y, PAGE_TITLE_2, serif_italic(80), anchor="ma")
y += 130

# Prose subtitle — multi-line italic centered (rollout-style standfirst)
for line in SUBTITLE_LINES:
    text(W // 2, y, line, serif_reg(22), fill=INK, anchor="ma")
    y += 32
y += 22
# Short centered rule (rollout-style)
hline(W // 2 - 70, W // 2 + 70, y, INK, 1)
y += 56

# ═══ § 01 — DIAGNOSE  (rollout-style header + 2-col cards) ══════════════════
y = section_header(y, "01", "DIAGNOSE", "", kicker_max_w=620)

# Lede right below header (matches §02/§03 lede style: italic 18 INK_SOFT, no quotes)
text(ML, y, "The multiplier is in the system, not the individual.",
     serif_italic(18), fill=INK_SOFT)
y += 36

# Two outlined cards, sibling rhythm to §02's three cards
d_gap = 24
d_card_w = (CW - d_gap) // 2
d_card_h = 268
d_pad = 22
d_cards = [
    {
        "marker": ("tri", RED),
        "tag":    "THE MYTH",
        "name":   ["THE 10× DEVELOPER"],
        "bullets": [
            "One hero plus tools.",
            "Productivity = velocity.",
            "Title-first reorgs.",
        ],
    },
    {
        "marker": ("circle", GREEN),
        "tag":    "THE REALITY",
        "name":   ["THE 10× TEAM"],
        "bullets": [
            "System designed for leverage.",
            "Productivity = working software shipped.",
            "Work-first role design.",
        ],
    },
]
for i, c in enumerate(d_cards):
    x = ML + i * (d_card_w + d_gap)
    rect([x, y, x + d_card_w, y + d_card_h], outline=RULE, width=1)
    cy = y + d_pad
    # marker + small tag kicker
    mk_kind, mk_color = c["marker"]
    if mk_kind == "tri":
        tri_up(x + d_pad, cy + 4, mk_color, size=12)
    else:
        circle(x + d_pad, cy + 4, mk_color, size=12)
    text(x + d_pad + 24, cy, c["tag"], mono_bold(12), fill=mk_color)
    cy += 28
    hline(x + d_pad, x + d_card_w - d_pad, cy, RULE_SOFT, 1)
    cy += 18
    # big card title
    for line in c["name"]:
        text(x + d_pad, cy, line, sans_bold(24), fill=INK)
        cy += 36
    cy += 6
    # bullets
    for b in c["bullets"]:
        for ln in wrap(b, serif_reg(17), d_card_w - 2 * d_pad):
            text(x + d_pad, cy, ln, serif_reg(17), fill=INK)
            cy += 24
        cy += 4
y += d_card_h + 32

# Section footer pull-quote — L214 (kept, relocated below new 2-col cards)
text(W // 2, y,
     "\u201cCreate the role when the work exists,",
     serif_italic(20), fill=INK, anchor="ma")
y += 28
text(W // 2, y,
     "not when the title sounds innovative.\u201d",
     serif_italic(20), fill=INK, anchor="ma")
y += 30
text(W // 2, y, "— Ch 06, L214",
     mono_reg(11), fill=INK_FAINT, anchor="ma")
y += 38

# ═══ § 02 — WHO OWNS THE NEW WORK? ══════════════════════════════════════════
y = section_header(y, "02", "WHO OWNS THE NEW WORK?", "",
                   kicker_max_w=380)

text(ML, y, "Three areas of work that did not exist before agentic development.",
     serif_italic(18), fill=INK_SOFT)
y += 26
text(ML, y, "The seats may be filled by existing experts or by new hires.",
     serif_italic(18), fill=INK_SOFT)
y += 40

# Three-column role cards
gap = 20
card_w = (CW - 2 * gap) // 3
card_h = 264
pad = 18
cards = [
    {
        "tag":  "WHAT",
        "name": ["DOMAIN", "SPECIALIST"],
        "aka":  None,
        "owns": "Owns what a Skill encodes.",
        "note": ("Often an existing expert, "
                 "newly in the engineering loop."),
        "cite": "Ch 06, L156",
    },
    {
        "tag":  "HOW",
        "name": ["AGENTIC WORKFLOW", "ENGINEER"],
        "aka":  "the \u201cContext Engineer\u201d role, at maturity",
        "owns": "Owns how a Skill composes.",
        "note": ("In small teams, the senior "
                 "engineer wears the hat."),
        "cite": "Ch 06, L168 · L174 · L210",
    },
    {
        "tag":  "OPERATIONS",
        "name": ["AGENT OPERATIONS", "SPECIALIST"],
        "aka":  None,
        "owns": "Owns the eval and safety loop.",
        "note": ("Production reliability for "
                 "agents in the loop."),
        "cite": "Ch 06, L178",
    },
]

for i, c in enumerate(cards):
    x = ML + i * (card_w + gap)
    rect([x, y, x + card_w, y + card_h], outline=RULE, width=1)
    # tag
    text(x + pad, y + pad, c["tag"], mono_bold(11), fill=OCHRE)
    # rule under tag
    hline(x + pad, x + card_w - pad, y + pad + 22, RULE_SOFT, 1)
    # name (sans bold, may wrap to 2 lines)
    name_y = y + pad + 36
    for line in c["name"]:
        text(x + pad, name_y, line, sans_bold(17), fill=INK)
        name_y += 24
    # alias (italic, soft) — only if present
    if c.get("aka"):
        for line in wrap(c["aka"], serif_italic(13), card_w - 2 * pad):
            text(x + pad, name_y + 2, line, serif_italic(13), fill=INK_SOFT)
            name_y += 18
        owns_y = name_y + 16
    else:
        owns_y = name_y + 18
    # owns
    for line in wrap(c["owns"], serif_reg(16), card_w - 2 * pad):
        text(x + pad, owns_y, line, serif_reg(16), fill=INK)
        owns_y += 22
    # note (italic, soft)
    note_y = owns_y + 12
    for line in wrap(c["note"], serif_italic(15), card_w - 2 * pad):
        text(x + pad, note_y, line, serif_italic(15), fill=INK_SOFT)
        note_y += 21
    # cite at bottom
    text(x + pad, y + card_h - pad - 12, c["cite"],
         mono_reg(10), fill=INK_FAINT)

y += card_h + 48

# ═══ § 03 — RESHAPE ═════════════════════════════════════════════════════════
y = section_header(y, "03", "RESHAPE",
                   "existing roles, new center of gravity",
                   kicker_max_w=440)

text(ML, y, "Same titles. New work mix. The growth path bends, but it doesn't break.",
     serif_italic(18), fill=INK_SOFT)
y += 36

# Three stacked cards (senior, junior, tech lead).
# Shift line is rendered as: "From X" + arrow primitive + "to Y" so glyphs always render.
def reshape_card(y, title, from_part, to_part, body, cite, tall=True):
    # Pre-measure to size box height
    body_lines = body or []
    has_body = bool(body_lines) and tall
    # heights: title 18, gap 8, "From X" 26, arrow row 26, body lines 22 each, paddings
    inner_pad_top = 18
    after_title   = 26
    from_h        = 26
    to_h          = 28
    body_h        = (len(body_lines) * 22 + 12) if has_body else 0
    cite_h        = 24
    h = inner_pad_top + after_title + from_h + to_h + body_h + cite_h
    rect([ML, y, W - MR, y + h], outline=RULE, width=1)
    text(ML + 22, y + inner_pad_top, title, sans_bold(15), fill=INK)
    fy = y + inner_pad_top + after_title
    text(ML + 22, fy, "From  " + from_part, serif_italic(20), fill=INK)
    # arrow + to_part on next line, slightly indented
    arrow_x = ML + 60
    arrow_y = fy + 30 + 10  # vertical center of next text line
    arrow_right(arrow_x, arrow_y, INK_SOFT, length=24, head=7, w=2)
    text(arrow_x + 32, fy + 30, "to  " + to_part,
         serif_italic(20), fill=INK)
    if has_body:
        by = fy + 30 + 30
        for i, line in enumerate(body_lines):
            text(ML + 22, by + i * 22, line,
                 serif_reg(15), fill=INK_SOFT)
    text(W - MR - 22, y + h - 18, cite,
         mono_reg(10), fill=INK_FAINT, anchor="ra")
    return y + h + 16

y = reshape_card(
    y,
    "SENIOR ENGINEERS",
    "writing the hardest code",
    "shaping the system that writes the code.",
    [
        "Time spent on: architecture · context engineering · review · mentoring.",
        "Less time on: heads-down implementation.",
    ],
    "Ch 06, L95",
    tall=True,
)
y = reshape_card(
    y,
    "JUNIOR ENGINEERS",
    "writing code",
    "reviewing agent output, writing specs, diagnosing failures.",
    [
        "Growth path is real — but it bypasses keyboard hours that built judgment.",
        "Mentorship is now a system problem, not a 1:1 problem.",
    ],
    "Ch 06, L97 · L103–105",
    tall=True,
)
y = reshape_card(
    y,
    "TECH LEADS",
    "owning the critical path",
    "owning the agent fleet's judgment surface.",
    None,
    "Ch 06, L110–114",
    tall=False,
)
y += 18

# ═══ § 04 — REBALANCE ═══════════════════════════════════════════════════════
y = section_header(y, "04", "REBALANCE",
                   "composition shift, not headcount cut",
                   kicker_max_w=400)

# Headline callout — L317 (single line, no break)
callout_h = 70
rect([ML, y, W - MR, y + callout_h], fill=INK)
text(ML + 26, y + 22,
     "\u201cThe staffing question is about composition and capability, not reduction.\u201d",
     serif_italic(20), fill=CREAM)
text(W - MR - 26, y + callout_h - 18, "— Ch 06, L317",
     mono_reg(11), fill=OCHRE_DARK, anchor="ra")
y += callout_h + 28

# Composition matrix
table_rows = [
    ("SENIOR : JUNIOR",          "1:2 to 1:3",    "1:1 to 2:1"),
    ("CONTEXT ENGINEERING",      "0%",            "10–20% of capacity"),
    ("REVIEW ALLOCATION",        "15–20%",        "25–35% of capacity"),
    ("Team size  (downstream)",  "6–10 engineers","4–7 engineers"),
]
col1_w = 360
col2_w = 280
col3_w = CW - col1_w - col2_w

# header row
hdr_y = y
text(ML, hdr_y, "DIMENSION",        mono_bold(11), fill=INK)
text(ML + col1_w, hdr_y, "PRE-AGENTIC",  mono_bold(11), fill=INK)
text(ML + col1_w + col2_w, hdr_y, "AGENTIC  (MATURE) †", mono_bold(11), fill=INK)
y += 22
hline(ML, W - MR, y, INK, 1)
y += 14

for i, (dim, pre, post) in enumerate(table_rows):
    is_size_row = (i == len(table_rows) - 1)
    dim_font  = sans_reg(15) if is_size_row else sans_bold(15)
    val_font  = serif_reg(17) if is_size_row else serif_reg(18)
    fill      = INK_SOFT if is_size_row else INK
    text(ML, y, dim, dim_font, fill=fill)
    text(ML + col1_w, y, pre, val_font, fill=fill)
    text(ML + col1_w + col2_w, y, post, val_font, fill=fill)
    y += 30
    hline(ML, W - MR, y - 6, RULE_SOFT, 1)

y += 4
text(ML, y, "†  Projected from early-adopter signals.   (Ch 06, L302–311)",
     mono_reg(11), fill=INK_FAINT)
y += 32

# Guardrail callout — single-line sentence-case headline + verbatim L329 body
gr_h = 178
rect([ML, y, W - MR, y + gr_h], fill=CREAM_DEEP, outline=RED, width=2)
warn_tri(ML + 22, y + 22, RED, size=22)
text(ML + 58, y + 22,
     "Without a deliberate rebalance, you lose twice.",
     serif_display(22), fill=RED)
quote_lines = wrap(
    "\u201cThe worst outcome is an accidental rebalance where juniors leave "
    "because they see no growth path, and seniors burn out because they "
    "are covering the gap.\u201d",
    serif_italic(18), CW - 80)
qy = y + 68
for line in quote_lines:
    text(ML + 22, qy, line, serif_italic(18), fill=INK)
    qy += 26
qy += 6
text(ML + 22, qy,
     "Both losses compound: lost growth path on one side, lost craft on the other.",
     serif_italic(15), fill=INK_SOFT)
text(W - MR - 22, y + gr_h - 22, "— Ch 06, L329",
     mono_reg(11), fill=INK_FAINT, anchor="ra")
y += gr_h + 32

# Anti-pattern checklist — 3 columns
text(ML, y, "WHAT DOESN'T WORK", mono_bold(11), fill=OCHRE)
y += 22
hline(ML, W - MR, y, RULE_SOFT, 1)
y += 18
ap_col_w = (CW - 40) // 3
ap_gutter = 20
antipatterns = [
    ("Replace team roles with agents",
     "lose the judgment layer.",
     "Ch 06, L236"),
    ("Title-first reorgs",
     "roles without work to back them.",
     "Ch 06, L214"),
    ("Cut juniors to \u201cafford\u201d seniors",
     "the pipeline collapses.",
     "Ch 06, L329"),
]
ap_top = y
ap_max_h = 0
for i, (cause, effect, cite) in enumerate(antipatterns):
    cx = ML + i * (ap_col_w + ap_gutter)
    cy = ap_top
    red_x(cx + 2, cy + 4, RED, size=12, w=2)
    cause_lines = wrap(cause, serif_reg(16), ap_col_w - 28)
    for line in cause_lines:
        text(cx + 28, cy, line, serif_reg(16), fill=INK)
        cy += 22
    cy += 6
    arrow_right(cx + 4, cy + 9, RED, length=18, head=6, w=2)
    effect_lines = wrap(effect, serif_reg(16), ap_col_w - 28)
    for line in effect_lines:
        text(cx + 28, cy, line, serif_reg(16), fill=INK_SOFT)
        cy += 22
    cy += 6
    text(cx, cy, cite, mono_reg(10), fill=INK_FAINT)
    cy += 18
    ap_max_h = max(ap_max_h, cy - ap_top)
y = ap_top + ap_max_h + 18

# ═══ LEAVE-WITH QUOTE ═══════════════════════════════════════════════════════
hline(ML, W - MR, y, INK, 2)
y += 56
quote_text = (
    "A team of solid engineers with a well-maintained context layer "
    "will outperform a team of exceptional engineers "
    "working in a knowledge vacuum."
)
quote_font = serif_italic(34)
for line in wrap(quote_text, quote_font, CW - 40):
    text(W // 2, y, line, quote_font, fill=INK, anchor="ma")
    y += 50
y += 14
text(W // 2, y, "— Daniel Meppiel,  Ch 06, L78",
     mono_reg(12), fill=INK_FAINT, anchor="ma")
y += 36
hline(ML, W - MR, y, INK, 2)
y += 28

# ═══ CTA FOOTER ═════════════════════════════════════════════════════════════
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
text(W // 2, inner, CTA_FORMAT, serif_italic(16), fill=LIGHT_CREAM, anchor="ma")
inner += 32
text(W // 2, inner, URL, mono_bold(17), fill=CREAM, anchor="ma")
url_w = tw(URL, mono_bold(17))
hline(int(W // 2 - url_w / 2), int(W // 2 + url_w / 2),
      inner + 26, CREAM, 1)

y = cta_top + cta_h

# ═══ CROP + SAVE ═══════════════════════════════════════════════════════════
final_h = y
final = img.crop((0, 0, W * SCALE, final_h * SCALE))

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
if OUTPUT_PATH.exists():
    OUTPUT_PATH.unlink()
final.save(OUTPUT_PATH, "PNG", optimize=True, dpi=(440, 440))
print(f"Wrote {OUTPUT_PATH}  ({W * SCALE}x{final_h * SCALE})")

# Also drop a Desktop copy for quick share
try:
    if DESKTOP_COPY.exists():
        DESKTOP_COPY.unlink()
    final.save(DESKTOP_COPY, "PNG", optimize=True, dpi=(440, 440))
    print(f"Wrote {DESKTOP_COPY}")
except Exception as e:
    print(f"(skipped Desktop copy: {e})")
