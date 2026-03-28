from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


CANVAS = (1280, 720)


SCENE_STYLES = {
    "border": {
        "sky_top": (213, 196, 166),
        "sky_bottom": (241, 232, 208),
        "ground_top": (151, 123, 86),
        "ground_bottom": (111, 90, 64),
    },
    "maritime": {
        "sky_top": (150, 179, 209),
        "sky_bottom": (212, 226, 238),
        "ground_top": (79, 112, 141),
        "ground_bottom": (47, 74, 102),
    },
    "critical": {
        "sky_top": (179, 189, 202),
        "sky_bottom": (222, 228, 233),
        "ground_top": (104, 110, 112),
        "ground_bottom": (67, 72, 75),
    },
}


def vertical_gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    width, height = size
    image = Image.new("RGB", size)
    draw = ImageDraw.Draw(image)
    for y in range(height):
        ratio = y / max(height - 1, 1)
        color = tuple(int(top[i] * (1 - ratio) + bottom[i] * ratio) for i in range(3))
        draw.line((0, y, width, y), fill=color)
    return image


def add_scene_geometry(image: Image.Image, scene: str) -> None:
    draw = ImageDraw.Draw(image)
    width, height = image.size
    horizon = int(height * 0.58)

    if scene == "border":
        draw.polygon([(0, horizon), (width, horizon - 18), (width, height), (0, height)], fill=(137, 110, 74))
        draw.polygon([(0, horizon + 60), (width, horizon + 24), (width, height), (0, height)], fill=(97, 77, 53))
        draw.line((40, horizon + 35, width - 40, horizon - 5), fill=(86, 72, 57), width=4)
        for x in range(90, width - 30, 140):
            base_y = horizon + 34 - ((x - 90) // 140 % 2) * 4
            draw.line((x, base_y - 58, x, base_y), fill=(95, 83, 68), width=4)
            draw.line((x, base_y - 40, x + 90, base_y - 30), fill=(110, 95, 78), width=2)
            draw.line((x, base_y - 18, x + 90, base_y - 8), fill=(110, 95, 78), width=2)
        draw.line((0, horizon + 110, width * 0.55, height), fill=(119, 94, 68), width=56)
    elif scene == "maritime":
        draw.rectangle((0, horizon, width, height), fill=(65, 93, 122))
        draw.rectangle((0, horizon + 84, width, height), fill=(43, 68, 95))
        draw.line((0, horizon, width, horizon), fill=(208, 221, 230), width=3)
        draw.rectangle((0, horizon + 165, width, height), fill=(83, 86, 90))
        draw.rectangle((0, horizon + 144, width * 0.42, horizon + 165), fill=(99, 101, 104))
        for x in range(60, int(width * 0.38), 95):
            draw.line((x, horizon + 105, x, horizon + 20), fill=(76, 82, 89), width=5)
        draw.rectangle((width * 0.62, horizon + 135, width * 0.88, horizon + 170), fill=(116, 119, 123))
    elif scene == "critical":
        draw.rectangle((0, horizon, width, height), fill=(87, 91, 94))
        draw.rectangle((0, horizon + 115, width, height), fill=(60, 64, 66))
        draw.rectangle((70, horizon + 40, 360, horizon + 180), fill=(116, 120, 123))
        draw.rectangle((390, horizon + 68, 620, horizon + 180), fill=(101, 106, 110))
        draw.rectangle((750, horizon + 24, 1080, horizon + 180), fill=(123, 127, 131))
        for x in (150, 210, 270, 820, 910, 1000):
            draw.line((x, horizon + 12, x, horizon + 182), fill=(188, 191, 193), width=3)
        for x in range(70, width - 60, 150):
            draw.line((x, horizon + 95, x, height - 20), fill=(167, 171, 173), width=3)
            draw.line((x, horizon + 118, x + 120, horizon + 95), fill=(167, 171, 173), width=2)
            draw.line((x, horizon + 148, x + 120, horizon + 125), fill=(167, 171, 173), width=2)


def add_radar(image: Image.Image, mask: Image.Image, product_path: Path) -> None:
    product = Image.open(product_path).convert("RGBA")
    bbox = product.getbbox()
    if bbox:
        product = product.crop(bbox)

    target_width = 270
    scale = target_width / product.width
    target_height = int(product.height * scale)
    product = product.resize((target_width, target_height), Image.Resampling.LANCZOS)

    width, height = image.size
    center_x = int(width * 0.74)
    base_y = int(height * 0.76)
    mast_top_y = base_y - 170
    product_x = center_x - target_width // 2
    product_y = mast_top_y - target_height + 126

    draw = ImageDraw.Draw(image)
    mask_draw = ImageDraw.Draw(mask)

    draw.rounded_rectangle((center_x - 26, mast_top_y, center_x + 26, base_y), radius=12, fill=(159, 166, 172))
    draw.ellipse((center_x - 44, base_y - 16, center_x + 44, base_y + 10), fill=(118, 123, 128))
    draw.rectangle((center_x - 120, base_y + 8, center_x + 120, base_y + 26), fill=(104, 108, 111))
    mask_draw.rounded_rectangle((center_x - 30, mast_top_y - 6, center_x + 30, base_y + 8), radius=14, fill=0)
    mask_draw.rectangle((center_x - 124, base_y + 2, center_x + 124, base_y + 30), fill=0)

    image.alpha_composite(product, (product_x, product_y))
    alpha = product.getchannel("A")
    mask.paste(Image.new("L", product.size, 0), (product_x, product_y), alpha)


def add_soft_atmosphere(image: Image.Image, scene: str) -> None:
    width, height = image.size
    haze = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(haze)
    if scene == "border":
        draw.ellipse((0, -80, width * 0.65, height * 0.55), fill=(255, 227, 180, 52))
    elif scene == "maritime":
        draw.ellipse((width * 0.12, -60, width * 0.88, height * 0.58), fill=(255, 255, 255, 48))
    else:
        draw.ellipse((width * 0.2, -100, width * 0.8, height * 0.5), fill=(240, 240, 245, 36))
    haze = haze.filter(ImageFilter.GaussianBlur(radius=36))
    image.alpha_composite(haze)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", required=True)
    parser.add_argument("--scene", choices=sorted(SCENE_STYLES.keys()), required=True)
    parser.add_argument("--base-output", required=True)
    parser.add_argument("--mask-output", required=True)
    args = parser.parse_args()

    style = SCENE_STYLES[args.scene]
    sky = vertical_gradient(CANVAS, style["sky_top"], style["sky_bottom"]).convert("RGBA")
    base = sky
    add_scene_geometry(base, args.scene)
    add_soft_atmosphere(base, args.scene)
    mask = Image.new("L", CANVAS, 255)
    add_radar(base, mask, Path(args.product))

    base_path = Path(args.base_output)
    mask_path = Path(args.mask_output)
    base_path.parent.mkdir(parents=True, exist_ok=True)
    mask_path.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(base_path, format="PNG", optimize=True)
    mask.save(mask_path, format="PNG", optimize=True)
    print(str(base_path.resolve()))
    print(str(mask_path.resolve()))


if __name__ == "__main__":
    main()
