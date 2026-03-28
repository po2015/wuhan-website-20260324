from __future__ import annotations

import base64
import textwrap
from dataclasses import dataclass
from pathlib import Path

from openai import OpenAI
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "static" / "images" / "cards"
FRONT_PATH = OUTPUT_DIR / "hu-po-business-card-front.png"
BACK_PATH = OUTPUT_DIR / "hu-po-business-card-back.png"
PREVIEW_PATH = OUTPUT_DIR / "hu-po-business-card-preview.png"
AI_BG_PATH = OUTPUT_DIR / "hu-po-business-card-ai-background.png"
LOGO_DARK_PATH = ROOT / "static" / "images" / "logo.png"
LOGO_LIGHT_PATH = ROOT / "static" / "images" / "logo_white.png"

CARD_WIDTH = 1050
CARD_HEIGHT = 600

NAVY = (14, 31, 56)
NAVY_SOFT = (26, 49, 83)
CYAN = (78, 180, 245)
CYAN_GLOW = (112, 205, 255)
STEEL = (98, 122, 150)
TEXT_LIGHT = (244, 249, 255)
TEXT_MID = (192, 214, 232)
TEXT_DARK = (22, 39, 67)
WHITE = (255, 255, 255)
OFF_WHITE = (245, 249, 253)
LINE = (207, 220, 235)


@dataclass(frozen=True)
class Person:
    name: str
    role: str
    company: str
    descriptor: str
    mobile: str
    email_primary: str
    email_secondary: str
    website: str


PERSON = Person(
    name="Hu Po",
    role="General Manager",
    company="Cyrentis",
    descriptor="Integrated Sensing Systems",
    mobile="+86 139 8605 3927",
    email_primary="poh@cyrentis.com",
    email_secondary="jhu8605@gmail.com",
    website="www.cyrentis.com",
)

ABOUT = (
    "Cyrentis integrates Horizon software, surveillance radar, electro-optical, "
    "and RF systems into practical site-security and low-altitude monitoring projects."
)

BUSINESS_ITEMS = [
    ("Horizon Software", "Unified status, alerts, tracks, and operator workflow."),
    ("Sensor Products", "Radar, electro-optical, and RF sensing for layered awareness."),
    ("System Delivery", "Solution design, customization, and equipment integration."),
    ("Global Support", "Export sourcing, compliance support, and global logistics."),
]


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size=size)


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_ai_background() -> Image.Image:
    if AI_BG_PATH.exists():
        return Image.open(AI_BG_PATH).convert("RGBA")

    prompt = textwrap.dedent(
        """
        Create a premium, landscape corporate visual for an international business card background.
        Brand context: Cyrentis, integrated sensing systems, Horizon software, surveillance radar,
        electro-optical systems, RF detection, site security, low-altitude awareness, global technology export.

        Art direction:
        - elegant and authoritative
        - minimal, refined, executive, premium
        - deep navy, steel blue, and cyan palette
        - subtle horizon line, layered signal waves, radar arcs, and soft luminous geometry
        - clean negative space suitable for professional card layout
        - high-end technology atmosphere without becoming sci-fi

        Hard requirements:
        - no text
        - no letters
        - no numbers
        - no logos
        - no people
        - no buildings
        - no mockup frame
        - no watermark
        """
    ).strip()

    client = OpenAI()
    response = client.images.generate(
        model="gpt-image-1.5",
        prompt=prompt,
        size="1536x1024",
        quality="medium",
        output_format="png",
    )
    AI_BG_PATH.write_bytes(base64.b64decode(response.data[0].b64_json))
    return Image.open(AI_BG_PATH).convert("RGBA")


def fit_image(image: Image.Image, width: int, height: int) -> Image.Image:
    return ImageOps.fit(image, (width, height), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def vertical_gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    width, height = size
    image = Image.new("RGBA", size)
    px = image.load()
    for y in range(height):
        ratio = y / max(height - 1, 1)
        color = tuple(int(top[i] + (bottom[i] - top[i]) * ratio) for i in range(3)) + (255,)
        for x in range(width):
            px[x, y] = color
    return image


def horizontal_fade_mask(width: int, height: int, start_alpha: int, end_alpha: int) -> Image.Image:
    mask = Image.new("L", (width, height))
    px = mask.load()
    for x in range(width):
        ratio = x / max(width - 1, 1)
        alpha = int(start_alpha + (end_alpha - start_alpha) * ratio)
        for y in range(height):
            px[x, y] = alpha
    return mask


def draw_signal_arcs(draw: ImageDraw.ImageDraw, center: tuple[int, int], radii: list[int], color: tuple[int, int, int], width: int) -> None:
    cx, cy = center
    for radius in radii:
        box = (cx - radius, cy - radius, cx + radius, cy + radius)
        draw.arc(box, start=300, end=58, fill=color, width=width)


def add_shadow(canvas: Image.Image, card: Image.Image, origin: tuple[int, int]) -> None:
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sx, sy = origin
    ImageDraw.Draw(shadow).rounded_rectangle(
        (sx + 14, sy + 18, sx + card.width + 14, sy + card.height + 18),
        radius=34,
        fill=(5, 16, 34, 60),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    canvas.alpha_composite(shadow)
    canvas.alpha_composite(card, origin)


def resize_logo(path: Path, target_width: int) -> Image.Image:
    logo = Image.open(path).convert("RGBA")
    ratio = target_width / logo.width
    target_height = int(logo.height * ratio)
    return logo.resize((target_width, target_height), Image.Resampling.LANCZOS)


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    spacing: int = 6,
) -> None:
    draw.multiline_text(xy, text, font=font, fill=fill, spacing=spacing)


def create_front(background: Image.Image) -> Image.Image:
    bg = fit_image(background, CARD_WIDTH, CARD_HEIGHT)
    front = Image.blend(bg, Image.new("RGBA", bg.size, NAVY + (255,)), 0.52)

    draw = ImageDraw.Draw(front)
    overlay = Image.new("RGBA", front.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rounded_rectangle((555, 88, 988, 536), radius=34, fill=(8, 25, 44, 132), outline=(109, 185, 246, 86), width=2)
    overlay_draw.ellipse((640, 26, 1160, 546), outline=(92, 170, 231, 34), width=3)
    overlay_draw.ellipse((700, 86, 1100, 486), outline=(92, 170, 231, 26), width=2)
    overlay = overlay.filter(ImageFilter.GaussianBlur(1))
    front.alpha_composite(overlay)

    draw_signal_arcs(draw, (922, 112), [54, 92, 132], (109, 194, 249), 5)
    draw.line((72, 218, 332, 218), fill=CYAN_GLOW, width=3)
    draw.line((506, 146, 506, 488), fill=(91, 173, 237), width=2)

    logo = resize_logo(LOGO_LIGHT_PATH, 292)
    front.alpha_composite(logo, (68, 52))

    font_descriptor = load_font("bahnschrift.ttf", 28)
    font_name = load_font("bahnschrift.ttf", 86)
    font_role = load_font("segoeuil.ttf", 32)
    font_label = load_font("bahnschrift.ttf", 20)
    font_body = load_font("segoeui.ttf", 29)
    font_body_small = load_font("segoeui.ttf", 24)

    draw.text((72, 240), PERSON.descriptor.upper(), font=font_descriptor, fill=TEXT_MID)
    draw.text((72, 284), PERSON.name, font=font_name, fill=TEXT_LIGHT)
    draw.text((76, 392), PERSON.role, font=font_role, fill=CYAN_GLOW)

    label_x = 568
    value_x = 568
    y = 152

    draw.text((label_x, y), "M / WHATSAPP", font=font_label, fill=TEXT_MID)
    draw.text((value_x, y + 30), PERSON.mobile, font=font_body, fill=TEXT_LIGHT)

    y += 122
    draw.text((label_x, y), "E", font=font_label, fill=TEXT_MID)
    draw.text((value_x, y + 30), PERSON.email_primary, font=font_body, fill=TEXT_LIGHT)
    draw.text((value_x, y + 66), PERSON.email_secondary, font=font_body_small, fill=TEXT_MID)

    y += 148
    draw.text((label_x, y), "W", font=font_label, fill=TEXT_MID)
    draw.text((value_x, y + 30), PERSON.website, font=font_body, fill=TEXT_LIGHT)

    return front


def create_back(background: Image.Image) -> Image.Image:
    base = vertical_gradient((CARD_WIDTH, CARD_HEIGHT), (252, 254, 255), (239, 245, 252))
    back = base.convert("RGBA")

    bg = fit_image(background, 700, CARD_HEIGHT + 80).filter(ImageFilter.GaussianBlur(6))
    bg = Image.blend(bg, Image.new("RGBA", bg.size, WHITE + (255,)), 0.58)
    mask = horizontal_fade_mask(bg.width, bg.height, 0, 180)
    back.paste(bg, (350, -24), mask)

    draw = ImageDraw.Draw(back)
    draw.rounded_rectangle((54, 54, 996, 546), radius=34, outline=(207, 220, 235), width=2)
    draw_signal_arcs(draw, (906, 120), [70, 116, 164], (152, 210, 246), 4)
    draw_signal_arcs(draw, (990, 468), [88, 130], (201, 228, 247), 4)

    logo = resize_logo(LOGO_DARK_PATH, 244)
    back.alpha_composite(logo, (72, 64))

    font_tag = load_font("bahnschrift.ttf", 22)
    font_title = load_font("bahnschrift.ttf", 44)
    font_body = load_font("segoeui.ttf", 22)
    font_card_title = load_font("bahnschrift.ttf", 22)
    font_card_body = load_font("segoeui.ttf", 18)

    draw.text((72, 184), "MAIN BUSINESS", font=font_tag, fill=STEEL)
    draw.text((72, 214), "Integrated Sensing Systems", font=font_title, fill=TEXT_DARK)

    about_lines = textwrap.fill(ABOUT, width=56)
    draw_multiline(draw, about_lines, (72, 286), font_body, (68, 86, 112), spacing=10)

    card_boxes = [
        (72, 390, 474, 476),
        (496, 390, 898, 476),
        (72, 486, 474, 572),
        (496, 486, 898, 572),
    ]

    for index, ((title, body), box) in enumerate(zip(BUSINESS_ITEMS, card_boxes, strict=True)):
        x1, y1, x2, y2 = box
        if y2 > CARD_HEIGHT - 26:
            offset = y2 - (CARD_HEIGHT - 26)
            y1 -= offset
            y2 -= offset
        draw.rounded_rectangle((x1, y1, x2, y2), radius=24, fill=(255, 255, 255, 224), outline=(213, 224, 237), width=2)
        chip_width = 72
        chip_color = (18, 81 + index * 16, 126 + index * 18)
        draw.rounded_rectangle((x1 + 18, y1 + 18, x1 + 18 + chip_width, y1 + 48), radius=14, fill=chip_color)
        draw.text((x1 + 40, y1 + 22), f"{index + 1:02d}", font=font_tag, fill=WHITE)
        draw.text((x1 + 108, y1 + 18), title, font=font_card_title, fill=TEXT_DARK)
        body_text = textwrap.fill(body, width=31)
        draw_multiline(draw, body_text, (x1 + 108, y1 + 44), font_card_body, (84, 103, 129), spacing=4)

    return back


def create_preview(front: Image.Image, back: Image.Image) -> Image.Image:
    canvas = Image.new("RGBA", (2320, 860), (236, 242, 248, 255))
    bg_draw = ImageDraw.Draw(canvas)
    bg_draw.rounded_rectangle((28, 28, 2292, 832), radius=42, fill=(245, 248, 252, 255))
    bg_draw.ellipse((-160, -40, 620, 640), fill=(220, 232, 244, 96))
    bg_draw.ellipse((1710, 250, 2520, 1010), fill=(208, 226, 242, 84))

    add_shadow(canvas, front, (110, 130))
    add_shadow(canvas, back, (1160, 130))

    draw = ImageDraw.Draw(canvas)
    font_label = load_font("bahnschrift.ttf", 34)
    draw.text((110, 70), "Front", font=font_label, fill=TEXT_DARK)
    draw.text((1160, 70), "Back", font=font_label, fill=TEXT_DARK)
    return canvas


def save_image(image: Image.Image, path: Path) -> None:
    image.save(path, format="PNG", dpi=(300, 300))


def main() -> None:
    ensure_output_dir()
    background = generate_ai_background()
    front = create_front(background)
    back = create_back(background)
    preview = create_preview(front, back)

    save_image(front, FRONT_PATH)
    save_image(back, BACK_PATH)
    save_image(preview, PREVIEW_PATH)

    print(FRONT_PATH)
    print(BACK_PATH)
    print(PREVIEW_PATH)


if __name__ == "__main__":
    main()
