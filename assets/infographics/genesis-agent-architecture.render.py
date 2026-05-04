"""
genesis-agent-architecture.render.py

Renders the LinkedIn-square infographic for the Genesis skill, anchored
to The Agentic SDLC Handbook Part III. Spec: genesis-agent-architecture.spec.md

Adapted from packages/editorial-infographic/.apm/skills/editorial-infographic/
assets/starter_template.py with:
  - Square-like canvas (1200 x ~1500 logical) instead of long portrait.
  - Custom Section 01: monospace prompt block in a CREAM_DEEP terminal-style box.
  - Custom Section 02: hand-drawn architecture diagram (boxes + arrows).
  - Custom CTA footer: terminal-style install command box.

Run:
    python3 genesis-agent-architecture.render.py

Output:
    genesis-agent-architecture.png  (next to this file)
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS_DIR = Path.home() / "Repos/apm-handbook/.github/skills/canvas-design/canvas-fonts"

# CONFIG
PUBLICATION   = "THE  AGENTIC  SDLC  HANDBOOK"
CHAPTER_LABEL = "PART  III  -  FOR  PRACTITIONERS"
PIECE_TITLE   = "CH 17  -  ARCHITECTURAL PATTERNS: A ROSETTA STONE"
FORMAT_LINE   = "FREE  -  WEB  -  PDF"
OUTPUT_PATH   = HERE / "genesis-agent-architecture.png"

# BRAND TOKENS
SCALE = 2
W, H_MAX = 1440, 3000
ML, MR = 100, 100
CW = W - ML - MR

CREAM       = (252, 252, 246)
CREAM_DEEP  = (240, 238, 225)
INK         = (13, 17, 23)
INK_DEEP    = (8, 11, 15)
# Audit fix (branding F4): bump grey labels from ~#8a8a82 to ~#4a4a44 so
# pattern lists, "imports", "composed of" pass AA on a sunlit phone.
INK_SOFT    = (74, 74, 68)
INK_FAINT   = (90, 90, 84)
RULE        = (200, 195, 184)
CHARTREUSE       = (218, 241, 114)
CHARTREUSE_DEEP  = (190, 215, 90)
OCHRE       = CHARTREUSE
OCHRE_DARK  = CHARTREUSE_DEEP
LIGHT_CREAM = (215, 215, 200)

img = Image.new("RGB", (W * SCALE, H_MAX * SCALE), CREAM)
d = ImageDraw.Draw(img)

# FONTS
# Round 1 audit fix (F3): kill Crimson Pro entirely. Three families, three roles:
#   - Playfair Display (display only -- H1 + favicon + wordmark)
#   - IBM Plex Mono (chrome / code / labels / diagram type)
#   - Work Sans (body sans + italic accents)
PLAYFAIR_TTF = Path.home() / "Library/Fonts/PlayfairDisplay.ttf"

def f(name, size):
    return ImageFont.truetype(str(FONTS_DIR / name), int(size * SCALE))

def playfair_bold(size):
    fnt = ImageFont.truetype(str(PLAYFAIR_TTF), int(size * SCALE))
    fnt.set_variation_by_name("Bold")
    return fnt

# Aliases preserved for any caller that still references the old names.
serif_display = playfair_bold
sans_bold     = lambda s: f("WorkSans-Bold.ttf", s)
sans_reg      = lambda s: f("WorkSans-Regular.ttf", s)
sans_italic   = lambda s: f("WorkSans-Italic.ttf", s)
mono_reg      = lambda s: f("IBMPlexMono-Regular.ttf", s)
mono_bold     = lambda s: f("IBMPlexMono-Bold.ttf", s)

def line_h(font, leading=1.25):
    """Logical line height for a font."""
    a, descent = font.getmetrics()
    return int((a + descent) / SCALE * leading)

# HELPERS
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

def rrect(box, radius, fill=None, outline=None, width=1):
    sb = [c * SCALE for c in box]
    d.rounded_rectangle(sb, radius=radius * SCALE, fill=fill,
                        outline=outline, width=width * SCALE)

def tw(s, font):
    return d.textlength(s, font=font) / SCALE

def arrow_down(x, y1, y2, color=INK, width=2, head=8):
    vline(x, y1, y2 - head, color, width)
    pts = [(x * SCALE, y2 * SCALE),
           ((x - head) * SCALE, (y2 - head) * SCALE),
           ((x + head) * SCALE, (y2 - head) * SCALE)]
    d.polygon(pts, fill=color)

def diagram_box(cx, top, w, h, lines, line_fonts, line_fills,
                fill=CREAM, outline=INK, border_w=2, radius=6,
                pad_top=None, pad_bot=None):
    """Draw a centered rounded box with vertically-centered, font-metric-aware text."""
    left = cx - w // 2
    rrect([left, top, left + w, top + h], radius=radius,
          fill=fill, outline=outline, width=border_w)
    # Compute total stack height using actual font metrics, with small inter-line gap.
    gap = 10
    heights = []
    ascents = []
    for fnt in line_fonts:
        a, dsc = fnt.getmetrics()
        heights.append((a + dsc) / SCALE)
        ascents.append(a / SCALE)
    stack_h = sum(heights) + gap * (len(lines) - 1)
    # Vertically center the stack inside the box.
    y0 = top + (h - stack_h) / 2
    cy = y0
    for line, fnt, fl, hgt in zip(lines, line_fonts, line_fills, heights):
        # Use baseline anchor "ms" for cleaner vertical alignment across mixed fonts.
        text(cx, cy + hgt * 0.78, line, fnt, fill=fl, anchor="ms")
        cy += hgt + gap

# MASTHEAD (chrome band 1) -- font scale matches CTA footer for legibility
mast_h = 140
rect([0, 0, W, mast_h], fill=INK)
y = 38
text(ML, y, PUBLICATION, mono_bold(22), fill=CHARTREUSE)
text(W - MR, y, CHAPTER_LABEL, mono_bold(22), fill=CHARTREUSE, anchor="ra")
y += 36
hline(ML, W - MR, y, CREAM, 2)
y += 18
text(ML, y, PIECE_TITLE, mono_bold(20), fill=LIGHT_CREAM)
text(W - MR, y, FORMAT_LINE.replace("-", "|"), mono_reg(20), fill=LIGHT_CREAM, anchor="ra")

y = mast_h + 28

# GENESIS BRAND BADGE (logo + wordmark, just below the masthead)
# Logomark renders the EXACT geometry of Repos/genesis/branding/logo.svg --
# rrect 320x320 rx=50 fill #000, Playfair Display Bold "G" fill #daf172 at
# (x=160 y=245 size=240) in the 320 viewBox. We scale that geometry down to
# `badge_logo_size` and rasterize directly via PIL using the installed
# PlayfairDisplay.ttf so the G is pixel-perfect (no font-fallback drift).
badge_logo_size = 60
badge_gap = 14
# Audit fix (LinkedIn F3): drop "-skill" suffix from the wordmark.
badge_wordmark = "danielmeppiel/genesis"
badge_wm_font = mono_bold(28)
badge_wm_w = tw(badge_wordmark, badge_wm_font)
badge_total_w = int(badge_logo_size + badge_gap + badge_wm_w)
badge_left = int((W - badge_total_w) // 2)

def _render_genesis_logo(size_px):
    """Render the official logo.svg geometry at `size_px` square (RGBA)."""
    s = size_px
    logo = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    ld = ImageDraw.Draw(logo)
    # rrect: rx=50 in 320 viewBox -> proportional radius
    radius = int(round(50 / 320 * s))
    ld.rounded_rectangle((0, 0, s - 1, s - 1), radius=radius, fill=(0, 0, 0, 255))
    # G: Playfair Display Bold, font-size 240 in 320 viewBox -> 240/320 * s
    g_font = ImageFont.truetype(str(PLAYFAIR_TTF), int(round(240 / 320 * s)))
    g_font.set_variation_by_name("Bold")
    # SVG places baseline at y=245 in viewBox, x=160 anchored middle.
    # PIL anchor "ms" = horizontal middle, baseline.
    ld.text(
        (s / 2, 245 / 320 * s),
        "G",
        font=g_font,
        fill=(218, 241, 114, 255),
        anchor="ms",
    )
    return logo

_logo_img = _render_genesis_logo(badge_logo_size * SCALE)
img.paste(_logo_img, (badge_left * SCALE, y * SCALE), _logo_img)
# Wordmark, vertically centered with the logomark
text(badge_left + badge_logo_size + badge_gap,
     y + badge_logo_size // 2 + 10,
     badge_wordmark, badge_wm_font, fill=INK, anchor="ls")
y += badge_logo_size + 18

# AUDIT FIX (LinkedIn F1): chartreuse hit in the top viewport. A 6px chartreuse
# rule under the wordmark gives color a job in the first 1100px so the thumb
# stops on color, not just serif. Width matches the headline text region.
rule_w = 520
rule_left = (W - rule_w) // 2
rect([rule_left, y, rule_left + rule_w, y + 6], fill=CHARTREUSE)
y += 28

# TOP-LEVEL TITLE (Playfair Display Bold; 2-line headline). Audit F3: Crimson
# Pro killed; H1 now in Playfair to match the favicon's typographic voice.
text(W // 2, y + 56, "Stop writing agents.",
     playfair_bold(72), fill=INK, anchor="ms")
y += 88

# Line 2 with chartreuse pill behind "designing" (LinkedIn F1, second hit).
# Layout: "Start " + [chartreuse pill: "designing"] + " them."
# We measure each segment, position the pill rrect first, then draw the text on
# top so the ink type stays AAA-legible on chartreuse.
h2_font   = playfair_bold(72)
seg_left  = "Start "
seg_pill  = "designing"
seg_right = " them."
w_left    = tw(seg_left,  h2_font)
w_pill    = tw(seg_pill,  h2_font)
w_right   = tw(seg_right, h2_font)
total_w   = w_left + w_pill + w_right
x0        = (W - total_w) / 2
baseline_y = y + 56
# Pill geometry: hugs the cap height tightly so it never bleeds into line 1.
pill_pad_x = 14
pill_pad_y = 4
ascent, descent = h2_font.getmetrics()
cap_h = (ascent + descent) / SCALE
pill_left = x0 + w_left - pill_pad_x
pill_right = x0 + w_left + w_pill + pill_pad_x
pill_top = baseline_y - cap_h * 0.62 - pill_pad_y
pill_bot = baseline_y + cap_h * 0.16 + pill_pad_y
rrect([int(pill_left), int(pill_top), int(pill_right), int(pill_bot)],
      radius=10, fill=CHARTREUSE)
text(x0,                   baseline_y, seg_left,  h2_font, fill=INK, anchor="ls")
text(x0 + w_left,          baseline_y, seg_pill,  h2_font, fill=INK, anchor="ls")
text(x0 + w_left + w_pill, baseline_y, seg_right, h2_font, fill=INK, anchor="ls")
y += 96

# THESIS / SUBTITLE -- category line under H1 (definition before claim).
# SWE-native vocabulary: tells the reader what this IS in 5 words.
text(W // 2, y + 30, "Software Design Patterns - ported to Agents.",
     sans_italic(36), fill=INK, anchor="ms")
y += 76

# SECTION 01 HEADER  (no right kicker; bigger verb)
text(ML, y + 26, "01", mono_bold(26), fill=INK, anchor="ls")
text(ML + 80, y + 26, "THE PROMPT", mono_bold(30), fill=INK, anchor="ls")
y += 38
hline(ML, W - MR, y, INK, 2)
y += 22

# PROMPT BOX (terminal-style; 28pt mono floor, breathing padding)
prompt_lines = [
    "/genesis  design an agent to cut a release.",
    "Sanitize the changelog, bump pyproject.toml,",
    "migrate open milestones.  Run it on GitHub Actions.",
]
pb_pad_y = 32
pb_line_h = 44
pb_h = 2 * pb_pad_y + pb_line_h * len(prompt_lines)
rrect([ML, y, W - MR, y + pb_h], radius=12, fill=CREAM_DEEP,
      outline=INK, width=2)
ty = y + pb_pad_y + 28
for i, line in enumerate(prompt_lines):
    if i == 0:
        cmd = "/genesis"
        rest = line[len(cmd):]
        w_cmd  = tw(cmd, mono_bold(28))
        w_rest = tw(rest, mono_reg(28))
        total  = w_cmd + w_rest
        x0 = (W - total) // 2
        text(x0, ty, cmd, mono_bold(28), fill=INK, anchor="ls")
        text(x0 + w_cmd, ty, rest, mono_reg(28), fill=INK, anchor="ls")
    else:
        text(W // 2, ty, line, mono_reg(28), fill=INK, anchor="ms")
    ty += pb_line_h
y += pb_h + 28

# SECTION 02 HEADER
text(ML, y + 26, "02", mono_bold(26), fill=INK, anchor="ls")
text(ML + 80, y + 26, "THE GENERATED ARCHITECTURE", mono_bold(30), fill=INK, anchor="ls")
y += 38
hline(ML, W - MR, y, INK, 2)
y += 26

# DIAGRAM
# Audit fix (branding F4): unify ALL diagram boxes with the Section 03 chip
# vocabulary. Single visual contract:
#   - ink-fill rrect (#0d1117), no border
#   - cream Plex Mono Bold for the title row
#   - cream Plex Mono Regular for the secondary label
#   - italic sublabels DROPPED (LinkedIn fix #4: trim labels so the tree reads
#     in 2s, not 6s)
cx = W // 2

def _ink_box(cx_, top_, w_, h_, title_, sub_, title_size=30, sub_size=20):
    left = cx_ - w_ // 2
    rrect([left, top_, left + w_, top_ + h_], radius=12, fill=INK)
    # Two centered rows, vertically centered.
    title_font = mono_bold(title_size)
    sub_font = mono_reg(sub_size)
    a1, d1 = title_font.getmetrics()
    a2, d2 = sub_font.getmetrics()
    h1 = (a1 + d1) / SCALE
    h2 = (a2 + d2) / SCALE
    gap = 8
    stack = h1 + gap + h2
    y0 = top_ + (h_ - stack) / 2
    text(cx_, y0 + h1 * 0.78, title_, title_font, fill=CREAM,       anchor="ms")
    text(cx_, y0 + h1 + gap + h2 * 0.78, sub_, sub_font, fill=LIGHT_CREAM, anchor="ms")

# Top box: GitHub Agentic Workflow
top_w, top_h = 560, 132
_ink_box(cx, y, top_w, top_h, "cut-release", "GITHUB AGENTIC WORKFLOW")
y += top_h

# Arrow + "imports" label (F4: keep arrow_down -- already 2px ink + filled
# triangle, matches the unified vocab).
arrow_top = y + 10
arrow_bottom = y + 62
arrow_down(cx, arrow_top, arrow_bottom, color=INK, width=2, head=10)
text(cx + 18, (arrow_top + arrow_bottom) // 2, "imports",
     mono_reg(16), fill=INK_SOFT, anchor="lm")
y = arrow_bottom + 10

# Middle box: Agent Skill
mid_w, mid_h = 560, 132
_ink_box(cx, y, mid_w, mid_h, "cut-release", "AGENT SKILL")
y += mid_h

# Arrow + "composed of" label
arrow_top = y + 10
arrow_bottom = y + 64
arrow_down(cx, arrow_top, arrow_bottom, color=INK, width=2, head=10)
text(cx + 18, (arrow_top + arrow_bottom) // 2, "composed of",
     mono_reg(16), fill=INK_SOFT, anchor="lm")
y = arrow_bottom + 6

# Three children boxes side-by-side -- same ink/cream vocab.
child_w, child_h = 380, 110
gap = 24
total_w = 3 * child_w + 2 * gap
left0 = (W - total_w) // 2
centers = [left0 + child_w // 2 + i * (child_w + gap) for i in range(3)]

stem_y = y + 10
hline(centers[0], centers[2], stem_y, INK, 2)
for c in centers:
    vline(c, stem_y, stem_y + 28, INK, 2)
for c in centers:
    pts = [(c * SCALE, (stem_y + 28) * SCALE),
           ((c - 8) * SCALE, (stem_y + 20) * SCALE),
           ((c + 8) * SCALE, (stem_y + 20) * SCALE)]
    d.polygon(pts, fill=INK)
y = stem_y + 32

child_specs = [
    ("scripts",    "DETERMINISTIC BITS"),
    ("references", "WHAT GROUNDS THE LLM"),
    ("output",     "WHAT IT WRITES BACK"),
]
for c, (title, cap) in zip(centers, child_specs):
    _ink_box(c, y, child_w, child_h, title, cap, title_size=26, sub_size=14)
y += child_h + 56

# ============================================================================
# SECTION 03 -- THE PATTERN STACK (Option A: stepped descent, count is hero)
# ============================================================================
text(ML, y + 26, "03", mono_bold(26), fill=INK, anchor="ls")
text(ML + 80, y + 26, "THE PATTERN STACK", mono_bold(30), fill=INK, anchor="ls")
y += 38
hline(ML, W - MR, y, INK, 2)
y += 22
text(ML, y + 22, "Why Genesis ships good designs: it composes from a layered catalog.",
     sans_italic(22), fill=INK_SOFT, anchor="ls")
y += 50

# Stepped stack: each card narrows by INDENT_STEP per descent. Hero metric =
# the count number, rendered as a chartreuse-on-ink BADGE (the only visual
# anchor per row). Right side = 2 rows only: tier name + samples (no caption).
# Sample names use sentence case (caps banned per design call).
stack_rows = [
    ("10", "ARCHITECTURAL PATTERNS",
     "Panel  .  Pipeline  .  Saga  .  Supervised Execution  .  +6"),
    ("24", "DESIGN PATTERNS",
     "Fan-out  .  Proxy  .  Decorator  .  Memento  .  Attention Anchor  .  +19"),
    ("5",  "IDIOMS",
     "Claude Code  .  Cursor  .  Copilot  .  Codex  .  OpenCode"),
    ("6",  "AGENTIC PRIMITIVES",
     "persona  .  skill  .  rule  .  subagent  .  trigger  .  plan-store"),
]

card_h     = 130
card_gap   = 16
indent_step = 60
full_w = W - ML - MR
# Count badge: ink rrect with chartreuse number. Fixed size so the four badges
# stack into a column the eye can scan top-down.
badge_w, badge_h = 120, 90
for i, (count, name, samples) in enumerate(stack_rows):
    cw = full_w - i * indent_step
    cx0 = ML + i * indent_step // 2
    cx1 = cx0 + cw
    box_top = y
    box_bot = y + card_h
    rrect([cx0, box_top, cx1, box_bot],
          radius=10, fill=CREAM_DEEP, outline=INK, width=2)

    # Hero count BADGE: ink fill, chartreuse digits, vertically centered in card.
    badge_left = cx0 + 24
    badge_top = box_top + (card_h - badge_h) // 2
    rrect([badge_left, badge_top, badge_left + badge_w, badge_top + badge_h],
          radius=10, fill=INK)
    # Center the digits in the badge (mono bold 60pt; "ms" anchor for baseline).
    text(badge_left + badge_w // 2, badge_top + badge_h // 2 + 22,
         count, mono_bold(60), fill=CHARTREUSE, anchor="ms")

    # Right column: 2 rows, vertically centered against badge midline.
    # Row 1 (tier name) above midline, Row 2 (samples) below.
    text_x = badge_left + badge_w + 28
    mid_y = box_top + card_h // 2
    text(text_x, mid_y - 6,  name,    mono_bold(28), fill=INK,      anchor="ls")
    text(text_x, mid_y + 32, samples, mono_reg(20),  fill=INK_SOFT, anchor="ls")

    y += card_h + card_gap

y += 14
# Closer line -- earned payoff after layers + patterns are visible above.
text(W // 2, y + 30, "The difference between a reliable agent",
     sans_reg(34), fill=INK, anchor="ms")
y += 50
text(W // 2, y + 30, "and an unreliable one is ARCHITECTURE.",
     sans_reg(34), fill=INK, anchor="ms")
y += 76

# CTA FOOTER (chrome band 2)
# Audit fix (LinkedIn F2): collapse to ONE primary chartreuse CTA. Drop the
# github URL block (redundant with the install command) and the kicker line.
# Result: install command is the ONLY chartreuse element below the masthead;
# handbook ref demoted to a single small caption + URL.
cta_top = y
cta_h = 280
rect([0, cta_top, W, cta_top + cta_h], fill=INK)

inner = cta_top + 40

# Install lede (small, recessive -- sets up the command).
text(W // 2, inner + 18, "Install with Agent Package Manager (APM):",
     sans_italic(22), fill=LIGHT_CREAM, anchor="ms")
inner += 42

# THE primary CTA: terminal-style install command box. The only chartreuse
# in the footer so the eye lands here unambiguously.
cmd_prompt = "$ "
cmd_str = "apm install danielmeppiel/genesis"
cmd_font = mono_bold(32)
cmd_w_prompt = tw(cmd_prompt, cmd_font)
cmd_w_str = tw(cmd_str, cmd_font)
tb_w = int(cmd_w_prompt + cmd_w_str + 96)
tb_h = 76
tb_left = (W - tb_w) // 2
rrect([tb_left, inner, tb_left + tb_w, inner + tb_h],
      radius=10, fill=INK_DEEP, outline=CHARTREUSE, width=2)
cmd_x0 = tb_left + (tb_w - cmd_w_prompt - cmd_w_str) // 2
text(cmd_x0, inner + tb_h // 2 + 12, cmd_prompt, cmd_font,
     fill=CHARTREUSE, anchor="ls")
text(cmd_x0 + cmd_w_prompt, inner + tb_h // 2 + 12, cmd_str, cmd_font,
     fill=CREAM, anchor="ls")
inner += tb_h + 36

# Handbook caption -- bigger so it's actually readable on the feed. No chartreuse
# (install command stays the only chartreuse CTA below the masthead).
hb_prefix = "Get the book:  "
hb_url = "theainativemind.com"
hb_font_pre = mono_reg(28)
hb_font_url = mono_bold(28)
hb_w_pre = tw(hb_prefix, hb_font_pre)
hb_w_url = tw(hb_url, hb_font_url)
hb_x0 = (W - hb_w_pre - hb_w_url) // 2
text(hb_x0, inner + 22, hb_prefix, hb_font_pre,
     fill=LIGHT_CREAM, anchor="ls")
text(hb_x0 + hb_w_pre, inner + 22, hb_url, hb_font_url,
     fill=CREAM, anchor="ls")

y = cta_top + cta_h

# CROP + SAVE
final_h = y
final = img.crop((0, 0, W * SCALE, final_h * SCALE))

if OUTPUT_PATH.exists():
    OUTPUT_PATH.unlink()
final.save(OUTPUT_PATH, "PNG", optimize=True, dpi=(440, 440))
print(f"Wrote {OUTPUT_PATH}  ({W * SCALE}x{final_h * SCALE})")
print(f"Aspect ratio (logical): {W} x {final_h}  =  {W/final_h:.2f}")
