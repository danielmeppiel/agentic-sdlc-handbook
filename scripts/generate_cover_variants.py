"""Generate two cover variants for comparison:
  A — v5 diagonal mesh, right-text layout, with contrast scrim behind subtitle/meta
  B — v6 vertical mesh mesh (left-side), text on right over clean dark space
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
VARS_PATH = ROOT / "_variables.yml"
COVER_DIR = ROOT / "assets" / "cover"
FLUX_V5 = COVER_DIR / "flux-mesh-v5-portrait.jpg"
FLUX_V7 = COVER_DIR / "flux-mesh-v6-vertical.jpg"
OUTPUT_A = COVER_DIR / "cover-variant-A.png"
OUTPUT_B = COVER_DIR / "cover-variant-B.png"

WIDTH = 1800
HEIGHT = 2700
BG = (12, 16, 22)


def load_variables() -> dict[str, str]:
    variables: dict[str, str] = {}
    for raw in VARS_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        variables[k.strip()] = v.strip().strip('"')
    return variables


def load_font(size: int, role: str):
    serif = [
        ROOT / ".github" / "skills" / "canvas-design" / "canvas-fonts" / "YoungSerif-Regular.ttf",
        Path("/System/Library/Fonts/Supplemental/Georgia.ttf"),
    ]
    sans = [
        Path("/System/Library/Fonts/HelveticaNeue.ttc"),
        Path("/System/Library/Fonts/Helvetica.ttc"),
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
    ]
    for c in (serif if role == "serif" else sans):
        if c.exists():
            return ImageFont.truetype(str(c), size=size)
    return ImageFont.load_default()


def load_scaled(path: Path) -> Image.Image:
    return Image.open(path).convert("RGBA").resize((WIDTH, HEIGHT), Image.LANCZOS)


def apply_top_darkening(img, strength=180, extent=0.30):
    """Quadratic dark gradient from top edge downward."""
    ov = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    end = int(HEIGHT * extent)
    for y in range(end):
        a = int(strength * (1 - y / end) ** 2)
        d.line([(0, y), (WIDTH, y)], fill=(*BG, a))
    img.alpha_composite(ov)


def apply_subtitle_scrim(img, col_x: int):
    """Gaussian-blurred dark scrim behind subtitle + meta zone (variant A only)."""
    mask = Image.new("L", (WIDTH, HEIGHT), 0)
    md = ImageDraw.Draw(mask)
    md.rectangle([col_x - 100, 1080, WIDTH, 1440], fill=190)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=80))
    dark = Image.new("RGBA", (WIDTH, HEIGHT), (*BG, 0))
    dark.putalpha(mask)
    img.alpha_composite(dark)


def draw_labels(img, variables: dict, col_x: int = 820):
    draw = ImageDraw.Draw(img)
    accent    = "#daf172"
    title_c   = "#f5f1ea"
    secondary = "#e2e6ec"   # Brighter than original #d7dbe2
    meta_c    = "#b4bac4"   # Brighter than original #8a929e

    tf = load_font(160, "serif")
    sf = load_font(50, "sans")
    af = load_font(48, "sans")
    mf = load_font(32, "sans")

    # Author name
    ay = 260
    draw.text((col_x, ay), "DANIEL MEPPIEL", fill=accent, font=af)
    nw = int(draw.textlength("DANIEL MEPPIEL", font=af))
    draw.line((col_x, ay + 62, col_x + nw, ay + 62), fill=(218, 241, 114, 120), width=3)

    # Title
    for word, y in [("The", 410), ("Agentic", 580), ("SDLC", 750), ("Handbook", 920)]:
        draw.text((col_x, y), word, fill=title_c, font=tf)

    # Subtitle
    draw.multiline_text(
        (col_x, 1150),
        "AI-native software development\nfor leaders and practitioners",
        fill=secondary, font=sf, spacing=14,
    )

    # Accent rule
    draw.line((col_x, 1290, col_x + 660, 1290), fill=(218, 241, 114, 120), width=3)

    # Draft version
    v = variables.get("version", "")
    bd = variables.get("build-date", "")
    draw.text((col_x, 1350), f"Draft v{v} · {bd}", fill=meta_c, font=mf)


def variant_a(variables):
    """v5 diagonal mesh + subtitle contrast scrim."""
    print("Building Variant A (v5 diagonal + scrim)...")
    base = load_scaled(FLUX_V5)
    apply_top_darkening(base, strength=180, extent=0.30)
    apply_subtitle_scrim(base, col_x=820)
    draw_labels(base, variables, col_x=820)
    base.convert("RGB").save(OUTPUT_A, quality=95)
    print(f"  ✓ {OUTPUT_A}")


def variant_b(variables):
    """v6 vertical mesh — mesh on left, text on right in clean dark space."""
    print("Building Variant B (v6 vertical flow)...")
    base = load_scaled(FLUX_V7)
    # Light top darkening only — the right side is already clean dark
    apply_top_darkening(base, strength=140, extent=0.22)
    draw_labels(base, variables, col_x=820)
    base.convert("RGB").save(OUTPUT_B, quality=95)
    print(f"  ✓ {OUTPUT_B}")


if __name__ == "__main__":
    v = load_variables()
    variant_a(v)
    variant_b(v)
    print("\nDone — compare both PNGs side by side.")
