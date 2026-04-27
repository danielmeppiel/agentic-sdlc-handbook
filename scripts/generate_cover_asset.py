from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
VARS_PATH = ROOT / "_variables.yml"
OUTPUT_PATH = ROOT / "assets" / "cover" / "agentic-sdlc-handbook-cover.png"
FLUX_IMAGE = ROOT / "assets" / "cover" / "flux-mesh-v5-portrait.jpg"

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


FONTS_DIR = ROOT / ".github" / "skills" / "canvas-design" / "canvas-fonts"


def load_font(size: int, role: str) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    serif_candidates = [
        FONTS_DIR / "YoungSerif-Regular.ttf",
        Path("/System/Library/Fonts/Supplemental/Georgia.ttf"),
    ]
    sans_candidates = [
        FONTS_DIR / "IBMPlexSans-Regular.ttf",
        FONTS_DIR / "WorkSans-Regular.ttf",
        FONTS_DIR / "InstrumentSans-Regular.ttf",
        Path("/System/Library/Fonts/HelveticaNeue.ttc"),
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
    ]
    sans_bold_candidates = [
        FONTS_DIR / "IBMPlexSans-Bold.ttf",
        FONTS_DIR / "WorkSans-Bold.ttf",
        FONTS_DIR / "InstrumentSans-Bold.ttf",
        Path("/System/Library/Fonts/HelveticaNeue.ttc"),
    ]
    sans_light_candidates = [
        FONTS_DIR / "IBMPlexSans-Light.ttf",
        FONTS_DIR / "IBMPlexSans-Regular.ttf",
        FONTS_DIR / "WorkSans-Regular.ttf",
        FONTS_DIR / "InstrumentSans-Regular.ttf",
        Path("/System/Library/Fonts/HelveticaNeue.ttc"),
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
    ]
    if role == "serif":
        candidates = serif_candidates
    elif role == "sans-bold":
        candidates = sans_bold_candidates
    elif role == "sans-light":
        candidates = sans_light_candidates
    else:
        candidates = sans_candidates
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def load_flux_background() -> Image.Image:
    """Load the FLUX-generated mesh image, scale to cover canvas,
    and blend with dark gradients for clean text areas.

    Two gradients are applied:
      1. Top darkening — quadratic fade over top 30% for author/title contrast
      2. Right-side fade — the mesh gradually fades to the dark BG colour
         starting around 40% from the left, reaching full opacity at ~85%.
         This keeps the mesh vivid on the left while giving clean contrast
         for the right-column text.
    """
    BG = (12, 16, 22)
    flux = Image.open(FLUX_IMAGE).convert("RGBA")
    flux = flux.resize((WIDTH, HEIGHT), Image.LANCZOS)

    # --- 1. Top darkening (quadratic) ---
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    darken_end = int(HEIGHT * 0.30)
    for y in range(darken_end):
        progress = y / darken_end
        alpha = int(180 * (1 - progress) ** 2)
        draw.line([(0, y), (WIDTH, y)], fill=(*BG, alpha))
    flux.alpha_composite(overlay)

    # --- 2. Right-side fade (smooth left→right gradient) ---
    # Fade starts at 40% of width, reaches full strength at 85%
    fade_start = int(WIDTH * 0.40)
    fade_end = int(WIDTH * 0.85)
    fade_span = fade_end - fade_start
    right_overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    rd = ImageDraw.Draw(right_overlay)
    for x in range(fade_start, WIDTH):
        if x < fade_end:
            t = (x - fade_start) / fade_span
            # Smooth ease-in curve for a gentle, non-abrupt transition
            alpha = int(200 * (t ** 1.8))
        else:
            alpha = 200
        rd.line([(x, 0), (x, HEIGHT)], fill=(*BG, alpha))
    flux.alpha_composite(right_overlay)

    return flux


def _draw_shadowed(
    draw: ImageDraw.ImageDraw,
    pos: tuple[int, int],
    text: str,
    fill: str | tuple,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    **kw,
) -> None:
    """Render text with a soft dark halo for legibility over the mesh."""
    x, y = pos
    bg = (12, 16, 22)
    for radius, alpha in ((5, 110), (3, 150), (2, 190)):
        for dx in (-radius, 0, radius):
            for dy in (-radius, 0, radius):
                if dx == 0 and dy == 0:
                    continue
                draw.text((x + dx, y + dy), text, fill=(*bg, alpha), font=font, **kw)
    draw.text(pos, text, fill=fill, font=font, **kw)


def _draw_tracked(
    draw: ImageDraw.ImageDraw,
    pos: tuple[int, int],
    text: str,
    fill: str | tuple,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    tracking: int = 10,
) -> int:
    """Draw letter-spaced (tracked) text for refined caps styling.
    Returns the final x position after the last character."""
    x, y = pos
    for ch in text:
        _draw_shadowed(draw, (x, y), ch, fill, font)
        x += int(draw.textlength(ch, font=font)) + tracking
    return x


def draw_labels(image: Image.Image, variables: dict[str, str]) -> None:
    draw = ImageDraw.Draw(image)
    accent = "#daf172"
    title_color = "#f5f1ea"
    subtitle_color = "#eef1f5"
    author_color = "#e8e4dc"  # warm white — dignified, not shouting
    meta_color = "#b0b8c4"

    col_x = 820

    title_lg = load_font(160, "serif")
    title_sm = load_font(96, "serif")   # "The" at reduced size
    subtitle_font = load_font(50, "sans")
    author_font = load_font(46, "sans-bold")  # Bold for thumbnail survival
    meta_font = load_font(32, "sans-light")

    # ── Title block — "The" at 96px, main words at 160px ──
    _draw_shadowed(draw, (col_x, 300), "The", fill=title_color, font=title_sm)
    _draw_shadowed(draw, (col_x, 410), "Agentic", fill=title_color, font=title_lg)
    _draw_shadowed(draw, (col_x, 580), "SDLC", fill=title_color, font=title_lg)
    _draw_shadowed(draw, (col_x, 750), "Handbook", fill=title_color, font=title_lg)

    # ── Accent rule — lime green structural divider ──
    draw.line((col_x, 950, col_x + 660, 950), fill=(218, 241, 114, 180), width=3)

    # ── Subtitle ──
    for line, y in [
        ("AI-native software development", 990),
        ("for leaders and practitioners", 1054),
    ]:
        _draw_shadowed(draw, (col_x, y), line, fill=subtitle_color, font=subtitle_font)

    # ── Author — below subtitle, sentence case, subtle 3px tracking ──
    _draw_tracked(draw, (col_x, 1150), "Daniel Meppiel",
                  fill=author_color, font=author_font, tracking=3)

    # ── Draft metadata ──
    version = variables.get("version", "")
    build_date = variables.get("build-date", "")
    meta_text = f"Draft v{version} · {build_date}"
    _draw_shadowed(draw, (col_x, 1240), meta_text, fill=meta_color, font=meta_font)


def main() -> None:
    variables = load_variables()

    # Use FLUX-generated mesh as the full background
    base = load_flux_background()

    draw_labels(base, variables)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(OUTPUT_PATH, quality=95)
    print(f"Wrote cover image to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()