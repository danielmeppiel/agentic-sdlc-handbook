"""
gen_editorial3.py  -- Dark Software Factory / Code Autopilot reference architecture.

Rebuilt on the authentic apm editorial brand system (genesis-agent-architecture):
cream ground, near-black ink, chartreuse-lime accent, Playfair Display headlines,
IBM Plex Mono technical labels, Work Sans kickers. Components are DARK rounded
cards; SDLC layers are numbered section bands for at-a-glance scannability.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUTPUT_PATH = HERE / "dark-software-factory.png"
FONTS_DIR = Path.home() / "Repos/apm-handbook/.github/skills/canvas-design/canvas-fonts"
PLAYFAIR_TTF = Path.home() / "Library/Fonts/PlayfairDisplay.ttf"

SCALE = 2
W, H_MAX = 1440, 4200
ML, MR = 110, 110
CW = W - ML - MR

# Brand tokens (genesis system)
CREAM = (252, 252, 246)
CREAM_DEEP = (240, 238, 225)
INK = (13, 17, 23)
INK_DEEP = (8, 11, 15)
INK_CARD = (18, 22, 28)
INK_SOFT = (74, 74, 68)
INK_FAINT = (120, 122, 116)
RULE = (200, 195, 184)
LIME = (218, 241, 114)
LIME_DEEP = (190, 215, 90)
LIME_INK = (96, 120, 30)
CARD_SUB = (214, 218, 204)
CREAM_ON_INK = (224, 222, 210)
GREEN = (96, 200, 140)
GREEN_DEEP = (40, 150, 95)
AMBER = (232, 178, 84)

img = Image.new("RGB", (W * SCALE, H_MAX * SCALE), CREAM)
d = ImageDraw.Draw(img)


def f(name, size):
    return ImageFont.truetype(str(FONTS_DIR / name), int(size * SCALE))


def playfair(size, weight="Bold"):
    fnt = ImageFont.truetype(str(PLAYFAIR_TTF), int(size * SCALE))
    try:
        fnt.set_variation_by_name(weight)
    except Exception:
        pass
    return fnt


def playfair_italic(size, weight="Medium"):
    # PlayfairDisplay.ttf has no italic axis; fall back to Libre Baskerville italic
    # for true slanted serif, else roman Playfair.
    try:
        fnt = ImageFont.truetype(str(FONTS_DIR / "LibreBaskerville-Italic.ttf"), int(size * SCALE))
        return fnt
    except Exception:
        return playfair(size, weight)


sans_bold = lambda s: f("WorkSans-Bold.ttf", s)
sans_semi = lambda s: f("WorkSans-Bold.ttf", s)
sans_reg = lambda s: f("WorkSans-Regular.ttf", s)
sans_italic = lambda s: f("WorkSans-Italic.ttf", s)
mono_reg = lambda s: f("IBMPlexMono-Regular.ttf", s)
mono_med = lambda s: f("IBMPlexMono-Regular.ttf", s)
mono_bold = lambda s: f("IBMPlexMono-Bold.ttf", s)


def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x * SCALE, y * SCALE), s, font=font, fill=fill, anchor=anchor)


def hline(x1, x2, y, color=RULE, width=1):
    d.line([(x1 * SCALE, y * SCALE), (x2 * SCALE, y * SCALE)], fill=color, width=width * SCALE)


def vline(x, y1, y2, color=RULE, width=1):
    d.line([(x * SCALE, y1 * SCALE), (x * SCALE, y2 * SCALE)], fill=color, width=width * SCALE)


def rect(box, fill=None, outline=None, width=1):
    d.rectangle([c * SCALE for c in box], fill=fill, outline=outline, width=width * SCALE)


def rrect(box, radius, fill=None, outline=None, width=1):
    d.rounded_rectangle([c * SCALE for c in box], radius=radius * SCALE, fill=fill, outline=outline, width=width * SCALE)


def tw(s, font):
    return d.textlength(s, font=font) / SCALE


def arrow_right(x1, x2, y, color=INK, width=3, head=11):
    hline(x1, x2 - head, y, color, width)
    d.polygon([(x2 * SCALE, y * SCALE), ((x2 - head) * SCALE, (y - head) * SCALE),
               ((x2 - head) * SCALE, (y + head) * SCALE)], fill=color)


def arrow_down(x, y1, y2, color=INK, width=3, head=10):
    vline(x, y1, y2 - head, color, width)
    d.polygon([(x * SCALE, y2 * SCALE), ((x - head) * SCALE, (y2 - head) * SCALE),
               ((x + head) * SCALE, (y2 - head) * SCALE)], fill=color)


def arrow_up(x, y1, y2, color=INK, width=3, head=10):
    """Arrow from y1 (bottom) up to y2 (top, the arrowhead)."""
    vline(x, y2 + head, y1, color, width)
    d.polygon([(x * SCALE, y2 * SCALE), ((x - head) * SCALE, (y2 + head) * SCALE),
               ((x + head) * SCALE, (y2 + head) * SCALE)], fill=color)


def wrap(s, font, maxw):
    out, cur = [], ""
    for word in s.split():
        t = (cur + " " + word).strip()
        if tw(t, font) <= maxw:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def all_ascii(strings):
    for s in strings:
        for ch in s:
            if ord(ch) > 126:
                raise ValueError(f"Non-ASCII char {ch!r} in {s!r}")


def section(num, label, y, right=None, accent=LIME):
    """Numbered section band: lime-on-ink number chip + bold kicker + full-width rule."""
    chip_w, chip_h = 48, 42
    rrect([ML, y, ML + chip_w, y + chip_h], 8, fill=INK)
    text(ML + chip_w / 2, y + chip_h / 2, num, sans_bold(22), fill=CREAM, anchor="mm")
    text(ML + chip_w + 20, y + chip_h / 2, label, sans_bold(24), fill=INK, anchor="lm")
    if right:
        text(W - MR, y + chip_h / 2, right, sans_italic(18), fill=INK_SOFT, anchor="rm")
    ry = y + chip_h + 14
    hline(ML, W - MR, ry, INK, 2)
    return ry + 30


def node_card(x, top, w, h, title, sub=None, fill=INK_CARD, title_fill=CREAM,
              sub_fill=CARD_SUB, title_font=None, sub_font=None, accent=None, radius=9):
    rrect([x, top, x + w, top + h], radius, fill=fill)
    if accent:
        rrect([x, top, x + 8, top + h], radius, fill=accent)
        rect([x + 4, top, x + 8, top + h], fill=accent)
    tf = title_font or mono_bold(22)
    cx = x + w / 2
    if sub:
        sf = sub_font or mono_reg(13)
        lines = wrap(sub, sf, w - 28)
        line_h = sf.size + 6
        gap = 13
        total = tf.size + gap + len(lines) * line_h
        ty = top + (h - total) / 2 + tf.size / 2
        text(cx, ty, title, tf, fill=title_fill, anchor="mm")
        ly = top + (h - total) / 2 + tf.size + gap + line_h / 2
        for line in lines:
            text(cx, ly, line, sf, fill=sub_fill, anchor="mm")
            ly += line_h
    else:
        text(cx, top + h / 2, title, tf, fill=title_fill, anchor="mm")


def chip(x, y, w, h, label, fill=CREAM, outline=INK, label_fill=INK, font=None, radius=8):
    rrect([x, y, x + w, y + h], radius, fill=fill, outline=outline, width=2)
    text(x + w / 2, y + h / 2, label, font or mono_med(16), fill=label_fill, anchor="mm")


def gate_card(x, top, w, h, title, sub, hdr_h=30):
    """Human decision gate: dark card with a lime HUMAN GATE header strip + lime title."""
    rrect([x, top, x + w, top + h], 9, fill=INK_CARD)
    rrect([x, top, x + w, top + hdr_h], 9, fill=LIME)
    rect([x, top + hdr_h - 10, x + w, top + hdr_h], fill=LIME)
    text(x + w / 2, top + hdr_h / 2, "HUMAN GATE", mono_bold(12), fill=INK, anchor="mm")
    sf = mono_reg(14)
    lines = wrap(sub, sf, w - 24)
    line_h = sf.size + 4
    body_top = top + hdr_h
    title_cy = body_top + 28
    text(x + w / 2, title_cy, title, mono_bold(21), fill=LIME, anchor="mm")
    ly = title_cy + 26
    for line in lines:
        text(x + w / 2, ly, line, sf, fill=CARD_SUB, anchor="mm")
        ly += line_h


def dark_chip(x, y, w, h, label, font=None, accent=False):
    """Small chip rendered on a dark module: ink card, cream (or lime) label."""
    if accent == "outline":
        rrect([x, y, x + w, y + h], 8, fill=INK_CARD, outline=LIME_DEEP, width=2)
        text(x + w / 2, y + h / 2, label, font or mono_bold(15), fill=LIME, anchor="mm")
    elif accent:
        rrect([x, y, x + w, y + h], 8, fill=LIME)
        text(x + w / 2, y + h / 2, label, font or mono_bold(15), fill=INK, anchor="mm")
    else:
        rrect([x, y, x + w, y + h], 8, fill=INK_CARD, outline=(78, 86, 78), width=2)
        text(x + w / 2, y + h / 2, label, font or mono_med(15), fill=CREAM_ON_INK, anchor="mm")


def apm_mark(x, y, box, word_pt, dark=True):
    """Black rounded square + lime Playfair wordmark, genesis favicon style."""
    bg = INK if dark else INK
    rrect([x, y, x + box, y + box], int(box * 0.22), fill=bg)
    text(x + box / 2, y + box / 2 - box * 0.04, "a", playfair(int(box * 0.62)), fill=LIME, anchor="mm")
    return x + box


# ---- content strings (ASCII guard) ----
STRINGS = [
    "THE DARK SOFTWARE FACTORY", "REFERENCE ARCHITECTURE",
    "HUMAN INTENT -> AUTONOMOUS BUILD -> VERIFIED MERGE", "microsoft/apm",
    "The Dark", "Software Factory", "Code Autopilot",
    "Humans set the intent and sign off the result. Autonomous agents build, test, and",
    "ship everything in between -- gated by deterministic, non-LLM verification floors.",
    "CONTROL PLANE", "Autopilot orchestrator", "AUTONOMOUS BUILD CONVEYOR",
    "VERIFICATION FLOOR", "PERSONA POOL", "SUBSTRATE",
    "Human intent", "Shipped software", "TRIAGE", "MERGE",
    "Ideate", "Plan", "Implement", "Review",
    "Approve intake", "Approve merge",
    "Agent Package Manager", "Portable.  Secure.  Governed.",
    "One apm.yml manifest composes every layer above",
    "The factory is dark between the two human approvals.",
    "Human intent -> autonomous delivery -> verified merge",
    "Agent Package Manager composes the factory",
]
all_ascii(STRINGS)


def pillar_tag(y_band, label):
    """Lime pill anchored at the right of a section band -- marks the two pillars."""
    f = mono_bold(13)
    pill_w = tw(label, f) + 30
    px1 = W - MR
    px0 = px1 - pill_w
    cy = y_band + 21
    rrect([px0, cy - 15, px1, cy + 15], 15, fill=LIME)
    text((px0 + px1) / 2, cy, label, f, fill=INK, anchor="mm")


# ============================ MASTHEAD ============================
mast_h = 132
rect([0, 0, W, mast_h], fill=INK_DEEP)
y = 42
text(ML, y, "THE DARK SOFTWARE FACTORY", mono_bold(16), fill=CREAM_ON_INK)
text(W - MR, y, "PUBLIC REFERENCE IMPLEMENTATION", mono_bold(16), fill=CREAM_ON_INK, anchor="ra")
y += 30
hline(ML, W - MR, y, (60, 66, 56), 2)
y += 14
text(ML, y, "HUMAN JUDGEMENT -> COMPOSABLE AGENT WORK -> VERIFIED MERGE", mono_reg(14), fill=CREAM_ON_INK)
text(W - MR, y, "microsoft/apm", mono_reg(14), fill=CREAM_ON_INK, anchor="ra")

# ============================ MARK + TITLE ============================
y = mast_h + 50
mark_box = 56
wordmark = "microsoft/apm"
ww = tw(wordmark, mono_bold(26))
group_w = mark_box + 18 + ww
gx = W / 2 - group_w / 2
apm_mark(gx, y, mark_box, 40)
text(gx + mark_box + 18, y + mark_box / 2, wordmark, mono_bold(26), fill=INK, anchor="lm")
y += mark_box + 20
lime_w = 150
hline(W / 2 - lime_w / 2, W / 2 + lime_w / 2, y, LIME_DEEP, 4)
y += 34

# H1 -- huge Playfair display
text(W / 2, y, "The Dark Software Factory", playfair(82), fill=INK, anchor="ma")
y += 112
# highlight marquee behind "Code Autopilot" (symmetric vertical padding)
ca_font = playfair(82)
ca = "Composable Code Autopilot"
caw = tw(ca, ca_font)
rrect([W / 2 - caw / 2 - 22, y - 10, W / 2 + caw / 2 + 22, y + 100], 10, fill=LIME)
text(W / 2, y, ca, ca_font, fill=INK, anchor="ma")
y += 128

# Thesis
thesis = [
    "Humans own the judgement -- the intent, the standards, and the final call.",
    "Agents build everything in between on composable apm packages. Delegation is",
    "trustworthy because two pillars hold: judgement you encode, verification they clear.",
]
tf = sans_reg(21)
for i, line in enumerate(thesis):
    if i == 0:
        text(W / 2, y, line, sans_bold(21), fill=INK, anchor="ma")
    else:
        text(W / 2, y, line, tf, fill=INK_SOFT, anchor="ma")
    y += 32
y += 30

# ============================ 01 CONTROL PLANE ============================
y = section("01", "CONTROL PLANE", y, right="issue-to-PR orchestrator -- reconciles until mergeable")
cp_h = 104
node_card(ML, y, CW, cp_h,
          "RECONCILIATION LOOP",
          "Drives intake -> build -> review -> verify -> merge until mergeable -- bounded by a fixed retry cap, then hands back to a human.",
          title_fill=CREAM, title_font=mono_bold(24), sub_font=mono_reg(15), sub_fill=CARD_SUB)
# orchestrates the conveyor below
orch_y = y + cp_h
arrow_down(W / 2, orch_y + 6, orch_y + 30, color=INK, width=2, head=8)
text(W / 2 + 16, orch_y + 18, "orchestrates the full conveyor", sans_italic(15), fill=INK_SOFT, anchor="lm")
y += cp_h + 50

# ============================ 02 CONVEYOR ============================
y = section("02", "AUTONOMOUS BUILD CONVEYOR", y, right="one rejection gate -> one merge gate")
conv_top = y

# human approval chips (green) sit above the two gates
appr_h = 44
# geometry of the row
n_gap = 26
intake_w = 170
gate_w = 178
build_w = CW - intake_w - gate_w * 2 - 170 - n_gap * 4
shipped_w = 170
xs = ML
intake_x = xs
triage_x = intake_x + intake_w + n_gap
build_x = triage_x + gate_w + n_gap
merge_x = build_x + build_w + n_gap
shipped_x = merge_x + gate_w + n_gap

row_y = conv_top + appr_h + 18
row_h = 160
mid = row_y + row_h / 2

# directional connectors between every stage (uniform baseline, in the gaps)
for _ax0, _ax1 in [(intake_x + intake_w, triage_x), (triage_x + gate_w, build_x),
                   (build_x + build_w, merge_x), (merge_x + gate_w, shipped_x)]:
    arrow_right(_ax0, _ax1, mid, color=INK, width=3, head=10)

node_card(intake_x, row_y, intake_w, row_h, "INTENT", "business intent", title_font=mono_bold(20), sub_font=mono_reg(15))
# gates (lime HUMAN GATE header -- the two human pinch-points)
gate_card(triage_x, row_y, gate_w, row_h, "TRIAGE", "declines / escalates")
# lime keyline: triage is THE kill gate of the conveyor
rrect([triage_x, row_y, triage_x + gate_w, row_y + row_h], 9, outline=LIME, width=3)
# build card with 4 SDLC chips
node_card(build_x, row_y, build_w, row_h, "", fill=INK_CARD)
text(build_x + build_w / 2, row_y + 26, "SDLC BUILD LOOP", mono_bold(19), fill=CREAM, anchor="mm")
stages = ["Ideate", "Plan", "Implement", "Review"]
sg = 12
sw = (build_w - 36 - sg * 3) / 4
sx = build_x + 18
for st in stages:
    rrect([sx, row_y + 52, sx + sw, row_y + row_h - 32], 7, fill=(30, 36, 44))
    text(sx + sw / 2, row_y + (52 + row_h - 32) / 2, st, mono_med(16), fill=CREAM, anchor="mm")
    sx += sw + sg
# return path beneath the stages -- makes the BUILD LOOP literal (reconcile until mergeable)
rety = row_y + row_h - 16
r_left = build_x + 24
r_right = build_x + build_w - 24
hline(r_left + 10, r_right, rety, (98, 108, 102), 2)
d.polygon([(r_left * SCALE, rety * SCALE), ((r_left + 10) * SCALE, (rety - 6) * SCALE),
           ((r_left + 10) * SCALE, (rety + 6) * SCALE)], fill=(98, 108, 102))
gate_card(merge_x, row_y, gate_w, row_h, "MERGE", "CI + human approval")
node_card(shipped_x, row_y, shipped_w, row_h, "SHIPPED", "merged pull request", title_font=mono_bold(20), sub_font=mono_reg(15))

# approval chips above gates + down arrows (lime = human authority)
chip(triage_x - 4, conv_top, gate_w + 8, appr_h, "REJECT / ESCALATE", fill=LIME, outline=LIME, label_fill=INK, font=mono_bold(14))
chip(merge_x - 4, conv_top, gate_w + 8, appr_h, "APPROVE MERGE", fill=LIME, outline=LIME, label_fill=INK, font=mono_bold(14))
arrow_down(triage_x + gate_w / 2, conv_top + appr_h, row_y - 2, color=(96, 102, 92), width=2, head=8)
arrow_down(merge_x + gate_w / 2, conv_top + appr_h, row_y - 2, color=(96, 102, 92), width=2, head=8)
# rejection branch -- triage is the pre-PR kill stage, escalating by default
rj_cx = triage_x + gate_w / 2
rj_y0 = row_y + row_h
arrow_down(rj_cx, rj_y0 + 4, rj_y0 + 24, color=INK_SOFT, width=2, head=7)
text(rj_cx + 14, rj_y0 + 18, "rejected / escalated -> human", mono_med(13), fill=INK_SOFT, anchor="lm")
cap_y = rj_y0 + 50
text(ML, cap_y, "Triage is the kill stage -- most intake is declined or escalated here, before any PR opens.",
     sans_italic(16), fill=INK_SOFT)
text(ML, cap_y + 26, "Rejection rate, not throughput, is the metric.", sans_italic(16), fill=INK_SOFT)
y = cap_y + 58

# Two co-equal pillar slabs: same height, inset, radius, lime rule at LIME_Y,
# and a "READ IT -> <public file>" footer. Parity is the whole point.
SLAB_H = 236
PAD = 30
LIME_Y = 158  # relative-to-slab y of the lime rule, identical in both pillars
FOOT_Y = 182  # relative-to-slab y of the footer caption row, identical in both

# ============================ 03 ENCODED JUDGEMENT (Pillar 1) ============================
pillar_tag(y, "PILLAR 1 OF 2")
y = section("03", "ENCODED JUDGEMENT", y)
text(ML, y, "Your standards, architecture, and review bar -- pressed into the agents so they apply your taste at scale.",
     sans_reg(16), fill=INK_SOFT)
text(ML, y + 24, "This is exactly what the TRIAGE gate applies before a PR may open.", sans_italic(15), fill=(112, 114, 106))
y += 54
st = y
rrect([ML, st, W - MR, st + SLAB_H], 12, fill=INK_DEEP)
arb_w = 264
divx = W - MR - arb_w
# left: encoded review lenses (codified dimensions, not people)
text(ML + PAD, st + 30, "ENCODED REVIEW LENSES", mono_bold(13), fill=CREAM_ON_INK, anchor="lm")
reviewers = ["Architecture", "Security", "DevEx", "Test Coverage", "Performance", "Auth", "Docs"]
rcf = mono_med(15)
rch = 42
rcgap = 11
rlx0 = ML + PAD
rlx1 = divx - PAD
rxp = rlx0
ryp = st + 54
for nm in reviewers:
    cwid = tw(nm, rcf) + 32
    if rxp + cwid > rlx1:
        rxp = rlx0
        ryp += rch + rcgap
    dark_chip(rxp, ryp, cwid, rch, nm, font=rcf)
    rxp += cwid + rcgap
# divider + right: escalation owner, set apart in lime
vline(divx, st + 24, st + 150, (44, 50, 44), 2)
ax = divx + PAD
text(ax, st + 30, "ESCALATION PATH", mono_bold(13), fill=LIME, anchor="lm")
dark_chip(ax, st + 54, arb_w - PAD - 34, 56, "A HUMAN", font=mono_bold(19), accent="outline")
text(ax, st + 126, "called by default", mono_reg(13), fill=CARD_SUB, anchor="lm")
text(ax, st + 146, "on any doubt.", mono_reg(13), fill=CARD_SUB, anchor="lm")
# footer parity: neutral divider (lime is reserved for the verification floor in 04, not here)
hline(ML + PAD, W - MR - PAD, st + LIME_Y, (44, 50, 44), 2)
text(ML + PAD, st + FOOT_Y, "Your taste, encoded -- not a borrowed benchmark.", mono_reg(14), fill=CREAM_ON_INK, anchor="lm")
text(W - MR - PAD, st + FOOT_Y, "READ IT -> apm-triage-panel rubric", mono_bold(14), fill=LIME, anchor="rm")
text(W - MR - PAD, st + FOOT_Y + 20, "packages/apm-triage-panel", mono_reg(11), fill=(132, 134, 124), anchor="rm")
y = st + SLAB_H + 40

# ============================ 04 DETERMINISTIC VERIFICATION (Pillar 2) ============================
pillar_tag(y, "PILLAR 2 OF 2")
y = section("04", "DETERMINISTIC VERIFICATION", y)
text(ML, y, "Non-LLM oracles you can audit -- work is trusted because a gate cleared it, not because the agent sounded sure.",
     sans_reg(16), fill=INK_SOFT)
text(ML, y + 24, "This is exactly what the MERGE step must clear before it can land.", sans_italic(15), fill=(112, 114, 106))
y += 54
st = y
rrect([ML, st, W - MR, st + SLAB_H], 12, fill=INK_DEEP)
text(ML + PAD, st + 30, "FIVE NON-LLM ORACLES", mono_bold(13), fill=CREAM_ON_INK, anchor="lm")
oracles = [
    ("RUFF LINT", "code quality"),
    ("DUP GUARD", "no copy-paste"),
    ("TESTS", "coverage floor"),
    ("BINARY", "build is green"),
    ("APM AUDIT", "no drift"),
]
inner_l = ML + PAD
inner_r = W - MR - PAD
inner_w = inner_r - inner_l
og = 16
ow = (inner_w - og * 4) / 5
oh = 96
oy = st + 50
ox = inner_l
oracle_centers = []
for t, s in oracles:
    node_card(ox, oy, ow, oh, t, s, fill=INK_CARD, title_font=mono_bold(18), sub_font=mono_reg(14), sub_fill=CARD_SUB)
    oracle_centers.append(ox + ow / 2)
    ox += ow + og
# pass floor: one lime baseline (LIME_Y) every build must clear -- aligned with 03's rule
hline(inner_l, inner_r, st + LIME_Y, LIME_DEEP, 3)
for cx in oracle_centers:
    rect([cx - 1.5, oy + oh, cx + 1.5, st + LIME_Y], fill=LIME_DEEP)
# footer parity: HARD GATE folds in merge causality + inspectable file
text(ML + PAD, st + FOOT_Y, "HARD GATE", mono_bold(14), fill=LIME, anchor="lm")
gx2 = ML + PAD + tw("HARD GATE", mono_bold(14)) + 10
text(gx2, st + FOOT_Y, "-- every PR clears all five, or it does not merge.", mono_reg(14), fill=CREAM_ON_INK, anchor="lm")
text(W - MR - PAD, st + FOOT_Y, "READ IT -> ci.yml", mono_bold(14), fill=LIME, anchor="rm")
text(W - MR - PAD, st + FOOT_Y + 20, ".github/workflows/ci.yml", mono_reg(11), fill=(132, 134, 124), anchor="rm")
y = st + SLAB_H + 48

# ============================ 05 SUBSTRATE (APM hero) ============================
y = section("05", "SUBSTRATE", y, right="installable agent primitives -- the factory harness")
sub_h = 268
rrect([ML, y, W - MR, y + sub_h], 12, fill=INK_DEEP)
# left brand block
card_w = 398
acx = ML + card_w / 2
text(acx, y + 94, "apm", playfair(96), fill=CREAM, anchor="mm")
text(acx, y + 166, "Agent Package Manager", mono_bold(18), fill=CREAM, anchor="mm")
text(acx, y + 208, "microsoft/apm  /  MIT  /  open source", mono_reg(14), fill=(196, 198, 188), anchor="mm")
vline(ML + card_w, y + 34, y + sub_h - 34, (44, 50, 44), 2)
# right composition
rx0 = ML + card_w + 46
rx1 = W - MR - 34
text(rx0, y + 44, "Portable.  Secure.  Governed.", mono_bold(19), fill=CREAM, anchor="lm")
runtimes = [("Copilot", ".github/"), ("Claude", ".claude/"), ("Cursor", ".cursor/"), ("OpenCode", ".opencode/")]
rg = 16
rw = (rx1 - rx0 - rg * 3) / 4
ry = y + 78
rh = 104
for nm, pth in runtimes:
    rrect([rx0, ry, rx0 + rw, ry + rh], 9, fill=INK_CARD, outline=(70, 81, 90), width=2)
    text(rx0 + rw / 2, ry + 40, nm, sans_bold(21), fill=CREAM, anchor="mm")
    text(rx0 + rw / 2, ry + 74, pth, mono_reg(15), fill=CREAM_ON_INK, anchor="mm")
    rx0 += rw + rg
rx_text = ML + card_w + 46
text(rx_text, y + sub_h - 34, "One apm.yml manifest composes every layer above", sans_italic(19), fill=CREAM_ON_INK, anchor="lm")
y += sub_h + 50

# ============================ PULL QUOTE ============================
hline(ML, W - MR, y - 28, RULE, 1)
text(W / 2, y, "Encode the judgement. Verify the work.", playfair(46), fill=INK, anchor="ma")
y += 60
text(W / 2, y, "The factory runs dark; humans keep the call.", playfair(46), fill=INK, anchor="ma")
y += 76

# ============================ FOOTER ============================
foot_top = y
foot_h = 240
rect([0, foot_top, W, foot_top + foot_h], fill=INK_DEEP)
iy = foot_top + 40
text(W / 2, iy, "REFERENCE ARCHITECTURE  --  THE DARK SOFTWARE FACTORY", mono_bold(15), fill=CREAM, anchor="ma")
iy += 46
cmd = "apm install microsoft/apm/packages/apm-issue-autopilot"
cf = mono_bold(18)
cwd = tw(cmd, cf) + tw("$ ", cf)
bx0 = W / 2 - cwd / 2 - 24
bx1 = W / 2 + cwd / 2 + 24
rrect([bx0, iy, bx1, iy + 46], 8, outline=(96, 102, 90), width=2)
text(W / 2 - cwd / 2, iy + 23, "$ ", cf, fill=LIME, anchor="lm")
text(W / 2 - cwd / 2 + tw("$ ", cf), iy + 23, cmd, cf, fill=CREAM, anchor="lm")
iy += 46 + 30
text(W / 2, iy, "From the book THE AGENTIC SDLC HANDBOOK", sans_italic(15), fill=(150, 152, 142), anchor="ma")
iy += 24
text(W / 2, iy, "danielmeppiel.github.io/agentic-sdlc-handbook", mono_reg(13), fill=(128, 130, 122), anchor="ma")
y = foot_top + foot_h

final_h = y  # end exactly at the black footer's bottom edge -- no trailing cream
final = img.crop((0, 0, W * SCALE, int(final_h * SCALE)))
if OUTPUT_PATH.exists():
    OUTPUT_PATH.unlink()
final.save(OUTPUT_PATH, "PNG", optimize=True, dpi=(440, 440))
print(f"Wrote {OUTPUT_PATH} ({W * SCALE}x{int(final_h * SCALE)})")
