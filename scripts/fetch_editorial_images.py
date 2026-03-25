from __future__ import annotations

import io
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests
from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PEXELS_SEARCH_URL = "https://api.pexels.com/v1/search"
TARGET_SIZE = (960, 540)
TARGET_RATIO = TARGET_SIZE[0] / TARGET_SIZE[1]


@dataclass(frozen=True)
class ArticleImageSpec:
    content_path: str
    image_dir: str
    image_name: str
    image_alt: str
    queries: tuple[str, ...]


ARTICLE_SPECS: tuple[ArticleImageSpec, ...] = (
    ArticleImageSpec(
        content_path="content/en/news/cyrentis-founded-and-launches-horizon-sense.md",
        image_dir="static/images/news",
        image_name="cyrentis-founded-and-launches-horizon-sense-cover.jpg",
        image_alt="Monitoring software and multi-screen control room environment related to Horizon Sense.",
        queries=(
            "control room software monitoring screens technology",
            "security operations center software screens",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/news/horizon-expands-with-fusion-command-and-link.md",
        image_dir="static/images/news",
        image_name="horizon-expands-with-fusion-command-and-link-cover.jpg",
        image_alt="Operations room with coordinated monitoring displays representing Horizon software modules.",
        queries=(
            "command center monitoring screens dashboard",
            "operations center software screens",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/news/cyrentis-signs-electro-optical-equipment-contract.md",
        image_dir="static/images/news",
        image_name="cyrentis-signs-electro-optical-equipment-contract-cover.jpg",
        image_alt="Business contract meeting for electro-optical equipment cooperation.",
        queries=(
            "business contract meeting technology handshake",
            "business people signing contract office",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/news/cyrentis-new-year-message-2026.md",
        image_dir="static/images/news",
        image_name="cyrentis-new-year-message-2026-cover.jpg",
        image_alt="Festive city skyline and lights for a corporate new year message.",
        queries=(
            "new year city lights skyline celebration",
            "new year fireworks city skyline",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/radar-lidar-ultrasonic-and-oth-which-sensing-layer-solves-which-problem.md",
        image_dir="static/images/knowledge-base",
        image_name="radar-lidar-ultrasonic-and-oth-sensing-layers-cover.jpg",
        image_alt="Sensor equipment and aerial surveillance scene representing multiple sensing layers.",
        queries=(
            "drone surveillance radar sensor technology",
            "industrial monitoring sensors technology",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/radar-system-components-front-end-back-end-and-data-flow.md",
        image_dir="static/images/knowledge-base",
        image_name="radar-system-components-front-end-back-end-data-flow-cover.jpg",
        image_alt="Electronics and radar hardware environment representing radar system components and data flow.",
        queries=(
            "electronics circuit board signal processing technology",
            "radar equipment electronics laboratory",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/synthetic-aperture-radar-sar-principles-imaging-modes-and-civil-applications.md",
        image_dir="static/images/knowledge-base",
        image_name="synthetic-aperture-radar-sar-civil-applications-cover.jpg",
        image_alt="Earth observation satellite scene related to synthetic aperture radar applications.",
        queries=(
            "satellite earth observation space",
            "satellite imaging earth technology",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/from-gaas-to-gan-what-makes-aesa-radar-industrially-ready.md",
        image_dir="static/images/knowledge-base",
        image_name="gaas-to-gan-aesa-radar-industrial-maturity-cover.jpg",
        image_alt="Semiconductor wafer and advanced electronics manufacturing scene related to radar hardware maturity.",
        queries=(
            "semiconductor wafer electronics manufacturing",
            "chip manufacturing technology",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/why-rf-digitization-is-reshaping-modern-radar-systems.md",
        image_dir="static/images/knowledge-base",
        image_name="rf-digitization-modern-radar-systems-cover.jpg",
        image_alt="Signal processing and RF electronics environment related to radar digitization.",
        queries=(
            "signal processing electronics laboratory",
            "radio frequency electronics equipment",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/layered-radar-architectures-what-civil-security-planners-can-borrow.md",
        image_dir="static/images/knowledge-base",
        image_name="layered-radar-architectures-civil-security-cover.jpg",
        image_alt="Radar installation overlooking a wide protected area for layered security planning.",
        queries=(
            "radar antenna landscape surveillance",
            "airport radar installation",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/bionic-fmcw-lidar-and-adaptive-4d-machine-vision.md",
        image_dir="static/images/knowledge-base",
        image_name="bionic-fmcw-lidar-adaptive-machine-vision-cover.jpg",
        image_alt="LiDAR and machine vision technology scene representing adaptive 4D sensing.",
        queries=(
            "lidar sensor autonomous technology",
            "machine vision sensor technology",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/radar-basics-mechanical-scan-phased-array-aesa-and-over-the-horizon.md",
        image_dir="static/images/knowledge-base",
        image_name="radar-basics-mechanical-scan-phased-array-aesa-cover.jpg",
        image_alt="Radar antenna scene representing basic radar scanning architectures.",
        queries=(
            "radar antenna tower sunset",
            "radar antenna technology",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/high-power-microwave-counter-uas-systems-where-they-fit-in-layered-defense.md",
        image_dir="static/images/knowledge-base",
        image_name="high-power-microwave-counter-uas-layered-defense-cover.jpg",
        image_alt="Drone surveillance and airspace monitoring scene related to counter-UAS defense.",
        queries=(
            "drone sky surveillance technology",
            "airspace monitoring drone",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/frontier-radar-technologies-what-is-real-what-is-emerging-and-what-to-watch.md",
        image_dir="static/images/knowledge-base",
        image_name="frontier-radar-technologies-emerging-systems-cover.jpg",
        image_alt="Advanced radar technology environment representing emerging surveillance systems.",
        queries=(
            "phased array radar technology",
            "advanced radar antenna technology",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/choosing-radar-frequency-bands-pros-cons-and-application-scenarios.md",
        image_dir="static/images/knowledge-base",
        image_name="choosing-radar-frequency-bands-application-scenarios-cover.jpg",
        image_alt="Radar equipment scene representing frequency band planning and deployment choices.",
        queries=(
            "radar dish antenna technology",
            "radar antenna equipment",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/comparison-of-different-radar-scanning-architectures.md",
        image_dir="static/images/knowledge-base",
        image_name="comparison-of-radar-scanning-architectures-cover.jpg",
        image_alt="Radar installation and scanning hardware scene related to architecture comparison.",
        queries=(
            "radar antenna scanning technology",
            "surveillance radar installation",
        ),
    ),
    ArticleImageSpec(
        content_path="content/en/knowledge-base/compliance-overview-for-dual-use-export-of-civil-security-radar-products.md",
        image_dir="static/images/knowledge-base",
        image_name="dual-use-export-compliance-civil-security-radar-cover.jpg",
        image_alt="Shipping containers and export logistics scene related to compliance review.",
        queries=(
            "shipping containers port logistics customs",
            "export logistics containers port",
        ),
    ),
)


def require_api_key() -> str:
    api_key = os.environ.get("PEXELS_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("PEXELS_API_KEY is missing from the environment.")
    return api_key


def parse_front_matter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\n(?P<front>.*?)\n---\n(?P<body>.*)\Z", text, re.S)
    if not match:
        raise ValueError("Markdown front matter block was not found.")
    return match.group("front"), match.group("body")


def update_front_matter(front_matter: str, image_path: str, image_alt: str) -> str:
    if not re.search(r"^image:\s*", front_matter, re.M):
        raise ValueError("Expected an image field in front matter.")

    front_matter = re.sub(
        r'^image:\s*".*?"\s*$',
        f'image: "{image_path}"',
        front_matter,
        count=1,
        flags=re.M,
    )

    if re.search(r"^image_alt:\s*", front_matter, re.M):
        front_matter = re.sub(
            r'^image_alt:\s*".*?"\s*$',
            f'image_alt: "{escape_quotes(image_alt)}"',
            front_matter,
            count=1,
            flags=re.M,
        )
    else:
        front_matter = re.sub(
            r'^(image:\s*".*?")\s*$',
            r'\1' + "\n" + f'image_alt: "{escape_quotes(image_alt)}"',
            front_matter,
            count=1,
            flags=re.M,
        )

    return front_matter


def update_body_image(body: str, image_path: str, image_alt: str) -> str:
    return re.sub(
        r'!\[[^\]]*\]\((/images/(?:news|knowledge-base)/[^)]+)\)',
        f'![{image_alt}]({image_path})',
        body,
        count=1,
    )


def escape_quotes(value: str) -> str:
    return value.replace('"', '\\"')


def choose_photo(photos: Iterable[dict]) -> dict:
    ranked = sorted(
        photos,
        key=lambda photo: (
            abs((photo.get("width", TARGET_SIZE[0]) / max(photo.get("height", TARGET_SIZE[1]), 1)) - TARGET_RATIO),
            photo.get("height", 0) * photo.get("width", 0) * -1,
        ),
    )
    return ranked[0]


def search_photo(api_key: str, queries: tuple[str, ...]) -> tuple[dict, str]:
    headers = {"Authorization": api_key}
    session = requests.Session()
    session.trust_env = False
    for query in queries:
        response = session.get(
            PEXELS_SEARCH_URL,
            headers=headers,
            params={
                "query": query,
                "per_page": 12,
                "orientation": "landscape",
                "size": "medium",
            },
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()
        photos = payload.get("photos") or []
        if photos:
            return choose_photo(photos), query
    raise RuntimeError(f"No Pexels images found for queries: {queries}")


def download_and_resize(image_url: str, output_path: Path) -> None:
    session = requests.Session()
    session.trust_env = False
    response = session.get(image_url, timeout=60)
    response.raise_for_status()
    image = Image.open(io.BytesIO(response.content))
    image = ImageOps.exif_transpose(image).convert("RGB")

    width, height = image.size
    source_ratio = width / max(height, 1)
    if source_ratio > TARGET_RATIO:
        crop_width = int(height * TARGET_RATIO)
        left = (width - crop_width) // 2
        image = image.crop((left, 0, left + crop_width, height))
    else:
        crop_height = int(width / TARGET_RATIO)
        top = (height - crop_height) // 2
        image = image.crop((0, top, width, top + crop_height))

    image = image.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="JPEG", quality=82, optimize=True, progressive=True)


def update_article(spec: ArticleImageSpec, image_path: str) -> None:
    content_file = ROOT / spec.content_path
    original = content_file.read_text(encoding="utf-8")
    front_matter, body = parse_front_matter(original)
    front_matter = update_front_matter(front_matter, image_path, spec.image_alt)
    body = update_body_image(body, image_path, spec.image_alt)
    content_file.write_text(f"---\n{front_matter}\n---\n{body}", encoding="utf-8")


def main() -> None:
    api_key = require_api_key()

    for spec in ARTICLE_SPECS:
        photo, query = search_photo(api_key, spec.queries)
        image_url = (
            photo.get("src", {}).get("large2x")
            or photo.get("src", {}).get("large")
            or photo.get("src", {}).get("original")
        )
        if not image_url:
            raise RuntimeError(f"No downloadable image URL found for {spec.content_path}")

        output_path = ROOT / spec.image_dir / spec.image_name
        rel_image_path = "/" + str(Path(spec.image_dir).joinpath(spec.image_name).as_posix()).removeprefix("static/")

        download_and_resize(image_url, output_path)
        update_article(spec, rel_image_path)

        print(
            f"updated {spec.content_path} -> {rel_image_path} "
            f"(query='{query}', photo_id={photo.get('id')}, photographer='{photo.get('photographer', '')}')"
        )


if __name__ == "__main__":
    main()
