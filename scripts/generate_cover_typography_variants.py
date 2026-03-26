"""Generate 3 typography variant covers for side-by-side comparison.

Variant A: Young Serif + Instrument Sans (Illustrator recommendation)
  - Author at top, tighter tracking (8), "The" reduced to 96px inline
Variant B: Playfair Display + IBM Plex Sans (Brand-aligned with theainativemind.com)
  - Same layout as A but with landing-page fonts
Variant C: Young Serif + IBM Plex Sans, author below subtitle (Chief Editor)
  - Author moves below subtitle, sentence case, warm white
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
VARS_PATH = ROOT / "_variables.yml"
FLUX_IMAGE = ROOT / "assets" / "cover" / "flux-mesh-v5-portrait.jpg"
FONTS_DIR = ROOT / ".github" / "skills" / "canvas-design" / "canvas-fonts"
OUTPUT_DIR = ROOT / "assets" / "cover"

WIDTH = 1800
HEIGHT = 2700


def load_variables() -> dict[str, str]:
    variables: dict[str, str] = {}
    for raw_line in VARS_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        variables[key.strip()] = value.strip().strip('"')
    return variables


def _font(path: Path, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if path.exists():
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def load_flux_background() -> Image.Image:
    BG = (12, 16, 22)
    flux = Image.open(FLUX_IMAGE).convert("RGBA")
    flux = flux.resize((WIDTH, HEIGHT), Image.LANCZOS)

    # Top darkening
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    darken_end = int(HEIGHT * 0.30)
    for y in range(darken_end):
        progress = y / darken_end
        alpha = int(180 * (1 - progress) ** 2)
        draw.line([(0, y), (WIDTH, y)], fill=(*BG, alpha))
    flux.alpha_composite(overlay)

    # Right-side fade
    fade_start = int(WIDTH * 0.40)
    fade_end = int(WIDTH * 0.85)
    fade_span = fade_end - fade_start
    right_overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    rd = ImageDraw.Draw(right_overlay)
    for x in range(fade_start, WIDTH):
        if x < fade_end:
            t = (x - fade_start) / fade_span
            alpha = int(200 * (t ** 1.8))
        else:
            alpha = 200
        rd.line([(x, 0), (x, HEIGHT)], fill=(*BG, alpha))
    flux.alpha_composite(right_overlay)
    return flux


def _draw_shadowed(draw, pos, text, fill, font, **kw):
    x, y = pos
    bg = (12, 16, 22)
    for radius, alpha in ((5, 110), (3, 150), (2, 190)):
        for dx in (-radius, 0, radius):
            for dy in (-radius, 0, radius):
                if dx == 0 and dy == 0:
                    continue
                draw.text((x + dx, y + dy), text, fill=(*bg, alpha), font=font, **kw)
    draw.text(pos, text, fill=fill, font=font, **kw)


def _draw_tracked(draw, pos, text, fill, font, tracking=8):
    x, y = pos
    for ch in text:
        _draw_shadowed(draw, (x, y), ch, fill, font)
        x += int(draw.textlength(ch, font=font)) + tracking
    return x


# ── Colors ──────────────────────────────────────────────────────────
ACCENT = "#daf172"
TITLE_COLOR = "#f5f1ea"
SUBTITLE_COLOR = "#eef1f5"
META_COLOR = "#b0b8c4"
AUTHOR_WARM = "#e8e4dc"  # warm white for Chief Editor variant
COL_X = 820


def variant_a(bg: Image.Image, variables: dict[str, str]) -> Image.Image:
    """Young Serif + Instrument Sans — illustrator recommendation."""
    img = bg.copy()
    draw = ImageDraw.Draw(img)

    # Fonts
    title_lg = _font(FONTS_DIR / "YoungSerif-Regular.ttf", 160)
    title_sm = _font(FONTS_DIR / "YoungSerif-Regular.ttf", 96)
    subtitle_f = _font(FONTS_DIR / "InstrumentSans-Regular.ttf", 50)
    author_f = _font(FONTS_DIR / "InstrumentSans-Bold.ttf", 44)
    meta_f = _font(FONTS_DIR / "InstrumentSans-Regular.ttf", 32)

    # Author — top, tracked caps, tighter tracking (8)
    author_y = 260
    final_x = _draw_tracked(draw, (COL_X, author_y), "DANIEL MEPPIEL",
                            fill=ACCENT, font=author_f, tracking=8)
    draw.line((COL_X, author_y + 58, final_x, author_y + 58),
              fill=(218, 241, 114, 180), width=3)

    # Title — "The" at 96px inline with "Agentic" on next line
    _draw_shadowed(draw, (COL_X, 420), "The", fill=TITLE_COLOR, font=title_sm)
    _draw_shadowed(draw, (COL_X, 530), "Agentic", fill=TITLE_COLOR, font=title_lg)
    _draw_shadowed(draw, (COL_X, 700), "SDLC", fill=TITLE_COLOR, font=title_lg)
    _draw_shadowed(draw, (COL_X, 870), "Handbook", fill=TITLE_COLOR, font=title_lg)

    # Subtitle — tighter to title (y=1050)
    for line, y in [
        ("AI-native software development", 1050),
        ("for leaders and practitioners", 1114),
    ]:
        _draw_shadowed(draw, (COL_X, y), line, fill=SUBTITLE_COLOR, font=subtitle_f)

    # Accent rule
    draw.line((COL_X, 1190, COL_X + 660, 1190), fill=(218, 241, 114, 180), width=3)

    # Meta
    version = variables.get("version", "")
    build_date = variables.get("build-date", "")
    _draw_shadowed(draw, (COL_X, 1240), f"Draft v{version} · {build_date}",
                   fill=META_COLOR, font=meta_f)

    # Label
    label_f = _font(FONTS_DIR / "InstrumentSans-Regular.ttf", 36)
    draw.text((60, HEIGHT - 80), "VARIANT A — Young Serif + Instrument Sans",
              fill="#666666", font=label_f)
    return img


def variant_b(bg: Image.Image, variables: dict[str, str]) -> Image.Image:
    """Playfair Display + IBM Plex Sans — brand-aligned with landing page."""
    img = bg.copy()
    draw = ImageDraw.Draw(img)

    # Fonts
    title_lg = _font(FONTS_DIR / "PlayfairDisplay-Bold.ttf", 155)
    title_sm = _font(FONTS_DIR / "PlayfairDisplay-Regular.ttf", 90)
    subtitle_f = _font(FONTS_DIR / "IBMPlexSans-Regular.ttf", 50)
    author_f = _font(FONTS_DIR / "IBMPlexSans-Bold.ttf", 44)
    meta_f = _font(FONTS_DIR / "IBMPlexSans-Light.ttf", 32)

    # Author — top, tracked caps
    author_y = 260
    final_x = _draw_tracked(draw, (COL_X, author_y), "DANIEL MEPPIEL",
                            fill=ACCENT, font=author_f, tracking=8)
    draw.line((COL_X, author_y + 58, final_x, author_y + 58),
              fill=(218, 241, 114, 180), width=3)

    # Title — "The" small inline
    _draw_shadowed(draw, (COL_X, 420), "The", fill=TITLE_COLOR, font=title_sm)
    _draw_shadowed(draw, (COL_X, 530), "Agentic", fill=TITLE_COLOR, font=title_lg)
    _draw_shadowed(draw, (COL_X, 700), "SDLC", fill=TITLE_COLOR, font=title_lg)
    _draw_shadowed(draw, (COL_X, 870), "Handbook", fill=TITLE_COLOR, font=title_lg)

    # Subtitle
    for line, y in [
        ("AI-native software development", 1050),
        ("for leaders and practitioners", 1114),
    ]:
        _draw_shadowed(draw, (COL_X, y), line, fill=SUBTITLE_COLOR, font=subtitle_f)

    # Accent rule
    draw.line((COL_X, 1190, COL_X + 660, 1190), fill=(218, 241, 114, 180), width=3)

    # Meta
    version = variables.get("version", "")
    build_date = variables.get("build-date", "")
    _draw_shadowed(draw, (COL_X, 1240), f"Draft v{version} · {build_date}",
                   fill=META_COLOR, font=meta_f)

    # Label
    label_f = _font(FONTS_DIR / "IBMPlexSans-Regular.ttf", 36)
    draw.text((60, HEIGHT - 80), "VARIANT B — Playfair Display + IBM Plex Sans",
              fill="#666666", font=label_f)
    return img


def variant_c(bg: Image.Image, variables: dict[str, str]) -> Image.Image:
    """Young Serif + IBM Plex Sans, author below subtitle (Chief Editor)."""
    img = bg.copy()
    draw = ImageDraw.Draw(img)

    # Fonts
    title_lg = _font(FONTS_DIR / "YoungSerif-Regular.ttf", 160)
    title_sm = _font(FONTS_DIR / "YoungSerif-Regular.ttf", 96)
    subtitle_f = _font(FONTS_DIR / "IBMPlexSans-Regular.ttf", 50)
    author_f = _font(FONTS_DIR / "IBMPlexSans-Regular.ttf", 44)
    meta_f = _font(FONTS_DIR / "IBMPlexSans-Light.ttf", 32)

    # Title first — "The" small
    _draw_shadowed(draw, (COL_X, 300), "The", fill=TITLE_COLOR, font=title_sm)
    _draw_shadowed(draw, (COL_X, 410), "Agentic", fill=TITLE_COLOR, font=title_lg)
    _draw_shadowed(draw, (COL_X, 580), "SDLC", fill=TITLE_COLOR, font=title_lg)
    _draw_shadowed(draw, (COL_X, 750), "Handbook", fill=TITLE_COLOR, font=title_lg)

    # Accent rule — between title and subtitle (structural divider)
    draw.line((COL_X, 950, COL_X + 660, 950), fill=(218, 241, 114, 180), width=3)

    # Subtitle
    for line, y in [
        ("AI-native software development", 990),
        ("for leaders and practitioners", 1054),
    ]:
        _draw_shadowed(draw, (COL_X, y), line, fill=SUBTITLE_COLOR, font=subtitle_f)

    # Author — below subtitle, sentence case, warm white (no caps, no tracking)
    _draw_shadowed(draw, (COL_X, 1140), "Daniel Meppiel",
                   fill=AUTHOR_WARM, font=author_f)

    # Meta
    version = variables.get("version", "")
    build_date = variables.get("build-date", "")
    _draw_shadowed(draw, (COL_X, 1220), f"Draft v{version} · {build_date}",
                   fill=META_COLOR, font=meta_f)

    # Label
    label_f = _font(FONTS_DIR / "IBMPlexSans-Regular.ttf", 36)
    draw.text((60, HEIGHT - 80),
              "VARIANT C — Young Serif + IBM Plex Sans (author below)",
              fill="#666666", font=label_f)
    return img


def main():
    variables = load_variables()
    bg = load_flux_background()

    for label, func in [("A", variant_a), ("B", variant_b), ("C", variant_c)]:
        img = func(bg, variables)
        out = OUTPUT_DIR / f"typography-variant-{label}.png"
        img.convert("RGB").save(out, quality=95)
        print(f"  Wrote {out}")

    print("\nDone — 3 variants in assets/cover/")


if __name__ == "__main__":
    main()
