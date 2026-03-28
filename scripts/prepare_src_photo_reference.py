from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps


CANVAS = (1280, 720)


SCENE_PRESETS = {
    "border": {
        "target_width": 228,
        "product_x_ratio": 0.73,
        "ground_y_ratio": 0.79,
        "platform_width": 180,
        "platform_height": 22,
        "shadow_blur": 18,
        "shadow_opacity": 96,
        "shadow_offset": (8, 14),
        "grade_color": 0.84,
        "grade_brightness": 0.9,
        "grade_contrast": 0.98,
        "haze": (235, 210, 176, 34),
    },
    "maritime": {
        "target_width": 208,
        "product_x_ratio": 0.74,
        "ground_y_ratio": 0.74,
        "platform_width": 170,
        "platform_height": 18,
        "shadow_blur": 16,
        "shadow_opacity": 86,
        "shadow_offset": (10, 11),
        "grade_color": 0.82,
        "grade_brightness": 0.9,
        "grade_contrast": 0.97,
        "haze": (218, 226, 233, 24),
    },
    "critical": {
        "target_width": 232,
        "product_x_ratio": 0.71,
        "ground_y_ratio": 0.84,
        "platform_width": 178,
        "platform_height": 20,
        "shadow_blur": 18,
        "shadow_opacity": 92,
        "shadow_offset": (9, 12),
        "grade_color": 0.8,
        "grade_brightness": 0.88,
        "grade_contrast": 0.99,
        "haze": (232, 237, 244, 16),
    },
}


def cover_resize(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def load_product(product_path: Path, target_width: int, scene: str) -> tuple[Image.Image, Image.Image]:
    product = Image.open(product_path).convert("RGBA")
    bbox = product.getbbox()
    if bbox:
        product = product.crop(bbox)

    scale = target_width / product.width
    target_height = int(product.height * scale)
    product = product.resize((target_width, target_height), Image.Resampling.LANCZOS)

    preset = SCENE_PRESETS[scene]
    product = ImageEnhance.Color(product).enhance(preset["grade_color"])
    product = ImageEnhance.Brightness(product).enhance(preset["grade_brightness"])
    product = ImageEnhance.Contrast(product).enhance(preset["grade_contrast"])

    alpha = product.getchannel("A")
    shadow = Image.new("RGBA", product.size, (0, 0, 0, 0))
    shadow.putalpha(alpha)
    shadow = ImageChops.multiply(shadow, Image.new("RGBA", product.size, (0, 0, 0, preset["shadow_opacity"])))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=preset["shadow_blur"]))
    return product, shadow


def add_platform(image: Image.Image, scene: str, product_box: tuple[int, int, int, int]) -> None:
    draw = ImageDraw.Draw(image)
    preset = SCENE_PRESETS[scene]
    left, top, right, bottom = product_box
    center_x = (left + right) // 2
    platform_top = bottom - 12
    platform_left = center_x - preset["platform_width"] // 2
    platform_right = center_x + preset["platform_width"] // 2
    platform_bottom = platform_top + preset["platform_height"]

    if scene == "border":
        fill = (122, 110, 98, 255)
        edge = (92, 80, 69, 255)
    elif scene == "maritime":
        fill = (157, 163, 170, 255)
        edge = (108, 116, 124, 255)
    else:
        fill = (132, 136, 141, 255)
        edge = (88, 93, 97, 255)

    draw.rounded_rectangle(
        (platform_left, platform_top, platform_right, platform_bottom),
        radius=5,
        fill=fill,
        outline=edge,
        width=2,
    )
    draw.rectangle(
        (center_x - 28, platform_bottom - 2, center_x + 28, platform_bottom + 20),
        fill=edge,
    )


def add_haze(image: Image.Image, scene: str) -> None:
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = image.size
    haze = SCENE_PRESETS[scene]["haze"]
    draw.ellipse((0, -40, width, int(height * 0.7)), fill=haze)
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=34))
    image.alpha_composite(overlay)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", required=True)
    parser.add_argument("--background", required=True)
    parser.add_argument("--scene", choices=sorted(SCENE_PRESETS.keys()), required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    preset = SCENE_PRESETS[args.scene]
    background = Image.open(args.background).convert("RGB")
    base = cover_resize(background, CANVAS).convert("RGBA")
    product, shadow = load_product(Path(args.product), preset["target_width"], args.scene)

    width, height = base.size
    x = int(width * preset["product_x_ratio"]) - product.width // 2
    y = int(height * preset["ground_y_ratio"]) - product.height

    shadow_x = x + preset["shadow_offset"][0]
    shadow_y = y + preset["shadow_offset"][1]
    base.alpha_composite(shadow, (shadow_x, shadow_y))
    add_platform(base, args.scene, (x, y, x + product.width, y + product.height))
    base.alpha_composite(product, (x, y))
    add_haze(base, args.scene)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(output_path, format="PNG", optimize=True)
    print(str(output_path.resolve()))


if __name__ == "__main__":
    main()
