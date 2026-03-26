from __future__ import annotations

import argparse
import io
import os
from pathlib import Path

import requests
from PIL import Image, ImageOps


TARGET_RATIO = 960 / 540


def require_key() -> str:
    api_key = os.environ.get("PEXELS_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("PEXELS_API_KEY is missing from the environment.")
    return api_key


def new_session(api_key: str) -> requests.Session:
    session = requests.Session()
    session.trust_env = False
    session.headers.update({"Authorization": api_key})
    return session


def choose_photo(photos: list[dict]) -> dict:
    return sorted(
        photos,
        key=lambda photo: (
            abs((photo.get("width", 960) / max(photo.get("height", 540), 1)) - TARGET_RATIO),
            -(photo.get("width", 0) * photo.get("height", 0)),
        ),
    )[0]


def fetch_photo(api_key: str, query: str, photo_id: int | None) -> dict:
    session = new_session(api_key)
    if photo_id is not None:
        response = session.get(f"https://api.pexels.com/v1/photos/{photo_id}", timeout=30)
        response.raise_for_status()
        return response.json()

    response = session.get(
        "https://api.pexels.com/v1/search",
        params={"query": query, "per_page": 20, "orientation": "landscape", "size": "medium"},
        timeout=30,
    )
    response.raise_for_status()
    photos = response.json().get("photos") or []
    if not photos:
        raise SystemExit(f"No Pexels photos found for query: {query}")
    return choose_photo(photos)


def resize_cover(image_bytes: bytes, width: int, height: int) -> Image.Image:
    image = Image.open(io.BytesIO(image_bytes))
    image = ImageOps.exif_transpose(image).convert("RGB")
    ratio = width / height
    source_ratio = image.width / max(image.height, 1)

    if source_ratio > ratio:
        crop_width = int(image.height * ratio)
        left = (image.width - crop_width) // 2
        image = image.crop((left, 0, left + crop_width, image.height))
    else:
        crop_height = int(image.width / ratio)
        top = (image.height - crop_height) // 2
        image = image.crop((0, top, image.width, top + crop_height))

    return image.resize((width, height), Image.Resampling.LANCZOS)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", default="", help="Pexels search query")
    parser.add_argument("--photo-id", type=int, help="Use a specific Pexels photo id")
    parser.add_argument("--output", required=True, help="Output image path")
    parser.add_argument("--width", type=int, default=960)
    parser.add_argument("--height", type=int, default=540)
    args = parser.parse_args()

    if not args.query and not args.photo_id:
        raise SystemExit("Provide --query or --photo-id.")

    api_key = require_key()
    photo = fetch_photo(api_key, args.query, args.photo_id)
    image_url = photo.get("src", {}).get("large2x") or photo.get("src", {}).get("large") or photo.get("src", {}).get("original")
    if not image_url:
        raise SystemExit("No downloadable image URL found.")

    session = new_session(api_key)
    response = session.get(image_url, timeout=60)
    response.raise_for_status()

    image = resize_cover(response.content, args.width, args.height)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="JPEG", quality=82, optimize=True, progressive=True)

    print(f"saved: {output_path}")
    print(f"photo_id: {photo.get('id')}")
    print(f"photographer: {photo.get('photographer', '')}")
    print(f"source_url: {photo.get('url', '')}")


if __name__ == "__main__":
    main()
