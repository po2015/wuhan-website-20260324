from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps


TARGET_SIZE = (600, 400)
DEPLOYMENT_DIR = Path(r"E:/Cyrentis/site/static/images/sensors/deployment")


def process_image(path: Path) -> tuple[str, int, int]:
    before = path.stat().st_size
    image = Image.open(path)
    image = ImageOps.exif_transpose(image)

    if path.suffix.lower() in {".jpg", ".jpeg"}:
        output = ImageOps.fit(
            image.convert("RGB"),
            TARGET_SIZE,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        output.save(path, format="JPEG", quality=78, optimize=True, progressive=True)
    else:
        output = ImageOps.fit(
            image.convert("RGB"),
            TARGET_SIZE,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        quantized = output.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
        quantized.save(path, format="PNG", optimize=True, compress_level=9)

    after = path.stat().st_size
    return path.name, before, after


def main() -> None:
    results: list[tuple[str, int, int]] = []
    for path in sorted(DEPLOYMENT_DIR.iterdir()):
        if path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue
        results.append(process_image(path))

    for name, before, after in results:
        print(f"{name}\t{before}\t{after}")

    total_before = sum(item[1] for item in results)
    total_after = sum(item[2] for item in results)
    print(f"TOTAL_BEFORE\t{total_before}")
    print(f"TOTAL_AFTER\t{total_after}")


if __name__ == "__main__":
    main()
