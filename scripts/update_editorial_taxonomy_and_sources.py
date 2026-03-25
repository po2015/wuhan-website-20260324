from __future__ import annotations

import io
import os
import re
from dataclasses import dataclass
from pathlib import Path

import requests
from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PHOTO_ENDPOINT = "https://api.pexels.com/v1/photos/{photo_id}"
SEARCH_ENDPOINT = "https://api.pexels.com/v1/search"
TARGET_SIZE = (960, 540)
TARGET_RATIO = TARGET_SIZE[0] / TARGET_SIZE[1]


@dataclass(frozen=True)
class ArticleConfig:
    path: str
    categories: tuple[str, ...]
    tags: tuple[str, ...]
    photo_id: int | None = None
    image_alt: str | None = None
    replace_queries: tuple[str, ...] = ()
    strip_lead_image: bool = False


ARTICLE_CONFIGS: tuple[ArticleConfig, ...] = (
    ArticleConfig(
        path="content/en/news/cyrentis-founded-and-launches-horizon-sense.md",
        categories=("Company News", "Horizon"),
        tags=("Corporate Launch", "Software Roadmap", "Integrated Monitoring"),
        photo_id=11044812,
    ),
    ArticleConfig(
        path="content/en/news/horizon-expands-with-fusion-command-and-link.md",
        categories=("Platform Updates", "Horizon"),
        tags=("Fusion Module", "Command Workflow", "Archive Layer"),
        photo_id=3582392,
    ),
    ArticleConfig(
        path="content/en/news/cyrentis-signs-electro-optical-equipment-contract.md",
        categories=("Business News", "Electro-Optical"),
        tags=("Contract Signing", "SOC Product Line", "Project Delivery"),
        photo_id=6814554,
    ),
    ArticleConfig(
        path="content/en/news/cyrentis-new-year-message-2026.md",
        categories=("Corporate Message", "Company News"),
        tags=("New Year Message", "Customer Thanks", "2026 Outlook"),
        photo_id=3597632,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/radar-lidar-ultrasonic-and-oth-which-sensing-layer-solves-which-problem.md",
        categories=("Radar Planning", "System Design"),
        tags=("Sensor Fusion", "LiDAR", "Ultrasonic"),
        photo_id=36028039,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/radar-system-components-front-end-back-end-and-data-flow.md",
        categories=("Radar Architecture", "System Design"),
        tags=("Transmit Chain", "Signal Processing", "Operator Workflow"),
        photo_id=14887694,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/synthetic-aperture-radar-sar-principles-imaging-modes-and-civil-applications.md",
        categories=("Radar Architecture", "Civil Applications"),
        tags=("SAR", "Earth Observation", "Imaging Modes"),
        photo_id=31505743,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/from-gaas-to-gan-what-makes-aesa-radar-industrially-ready.md",
        categories=("Radar Architecture", "Manufacturing"),
        tags=("GaAs", "GaN", "AESA Production"),
        photo_id=1448561,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/why-rf-digitization-is-reshaping-modern-radar-systems.md",
        categories=("Digital RF", "Radar Architecture"),
        tags=("Direct RF Sampling", "Digital Beamforming", "Software-Defined Radar"),
        photo_id=7513422,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/layered-radar-architectures-what-civil-security-planners-can-borrow.md",
        categories=("System Design", "Deployment"),
        tags=("Layered Surveillance", "Civil Security Planning", "Range Architecture"),
        photo_id=13766369,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/bionic-fmcw-lidar-and-adaptive-4d-machine-vision.md",
        categories=("Emerging Sensors", "Machine Vision"),
        tags=("FMCW LiDAR", "Adaptive Perception", "4D Sensing"),
        photo_id=35076211,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/radar-basics-mechanical-scan-phased-array-aesa-and-over-the-horizon.md",
        categories=("Radar Architecture", "Technology Basics"),
        tags=("Mechanical Scan", "Phased Array", "AESA"),
        photo_id=12102906,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/high-power-microwave-counter-uas-systems-where-they-fit-in-layered-defense.md",
        categories=("Counter-UAS", "System Design"),
        tags=("Directed Energy", "Layered Defense", "Airspace Security"),
        photo_id=319968,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/frontier-radar-technologies-what-is-real-what-is-emerging-and-what-to-watch.md",
        categories=("Emerging Radar", "Technology Watch"),
        tags=("4D Radar", "Cognitive Sensing", "Future Systems"),
        photo_id=28975867,
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/choosing-radar-frequency-bands-pros-cons-and-application-scenarios.md",
        categories=("Radar Planning", "Frequency Selection"),
        tags=("C Band", "X Band", "Ku Band"),
        replace_queries=("airport surveillance antenna", "radar control room display", "outdoor antenna installation"),
        image_alt="Antenna and monitoring equipment scene representing radar frequency band planning.",
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/comparison-of-different-radar-scanning-architectures.md",
        categories=("Radar Architecture", "System Design"),
        tags=("Mechanical Rotation", "Electronic Scan", "Volume Search"),
        replace_queries=("surveillance antenna on rooftop", "operations room radar display", "sensor mast antenna"),
        image_alt="Surveillance installation scene representing different radar scanning architectures.",
        strip_lead_image=True,
    ),
    ArticleConfig(
        path="content/en/knowledge-base/compliance-overview-for-dual-use-export-of-civil-security-radar-products.md",
        categories=("Compliance", "Export Control"),
        tags=("Export Licensing", "Dual-Use Review", "China Compliance"),
        photo_id=6752846,
        strip_lead_image=True,
    ),
)


def require_api_key() -> str:
    api_key = os.environ.get("PEXELS_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("PEXELS_API_KEY is missing from the environment.")
    return api_key


def new_session(api_key: str) -> requests.Session:
    s = requests.Session()
    s.trust_env = False
    s.headers.update({"Authorization": api_key})
    return s


def parse_front_matter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\n(?P<front>.*?)\n---\n(?P<body>.*)\Z", text, re.S)
    if not match:
        raise ValueError("Front matter not found.")
    return match.group("front"), match.group("body")


def build_yaml_list(name: str, values: tuple[str, ...]) -> str:
    return name + ":\n" + "\n".join(f'  - "{value}"' for value in values)


def replace_block(front: str, name: str, values: tuple[str, ...]) -> str:
    pattern = rf"^{name}:\n(?:  - .+\n)+"
    replacement = build_yaml_list(name, values) + "\n"
    if re.search(pattern, front, flags=re.M):
        return re.sub(pattern, replacement, front, count=1, flags=re.M)
    return front + "\n" + replacement


def upsert_scalar(front: str, name: str, value: str) -> str:
    escaped = value.replace('"', '\\"')
    pattern = rf'^{name}:\s*".*?"\s*$'
    replacement = f'{name}: "{escaped}"'
    if re.search(pattern, front, flags=re.M):
        return re.sub(pattern, replacement, front, count=1, flags=re.M)
    anchor = re.search(r'^image_alt:\s*".*?"\s*$', front, flags=re.M)
    if anchor:
        pos = anchor.end()
        return front[:pos] + "\n" + replacement + front[pos:]
    return front + "\n" + replacement


def update_image_path(front: str, image_path: str, image_alt: str) -> str:
    front = re.sub(r'^image:\s*".*?"\s*$', f'image: "{image_path}"', front, count=1, flags=re.M)
    if re.search(r'^image_alt:\s*".*?"\s*$', front, flags=re.M):
        front = re.sub(r'^image_alt:\s*".*?"\s*$', f'image_alt: "{image_alt}"', front, count=1, flags=re.M)
    else:
        front = upsert_scalar(front, "image_alt", image_alt)
    return front


def strip_lead_image(body: str) -> str:
    lines = body.splitlines()
    while lines and not lines[0].strip():
        lines = lines[1:]
    if lines and lines[0].startswith("![") and "](" in lines[0]:
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines)


def choose_unique_photo(api_key: str, queries: tuple[str, ...], disallow_ids: set[int]) -> dict:
    s = new_session(api_key)
    for query in queries:
        resp = s.get(
            SEARCH_ENDPOINT,
            params={"query": query, "per_page": 20, "orientation": "landscape", "size": "medium"},
            timeout=30,
        )
        resp.raise_for_status()
        for photo in resp.json().get("photos", []):
            photo_id = int(photo["id"])
            if photo_id not in disallow_ids:
                return photo
    raise RuntimeError(f"No unique photo found for queries: {queries}")


def get_photo(api_key: str, photo_id: int) -> dict:
    s = new_session(api_key)
    resp = s.get(PHOTO_ENDPOINT.format(photo_id=photo_id), timeout=30)
    resp.raise_for_status()
    return resp.json()


def download_and_resize(api_key: str, image_url: str, output_path: Path) -> None:
    s = new_session(api_key)
    resp = s.get(image_url, timeout=60)
    resp.raise_for_status()
    image = Image.open(io.BytesIO(resp.content))
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


def image_output_path(front: str) -> Path:
    match = re.search(r'^image:\s*"(?P<path>/images/[^"]+)"\s*$', front, flags=re.M)
    if not match:
        raise ValueError("Image path missing from front matter.")
    rel = match.group("path").lstrip("/")
    return ROOT / "static" / rel.replace("images/", "images/", 1)


def image_public_path(front: str) -> str:
    match = re.search(r'^image:\s*"(?P<path>/images/[^"]+)"\s*$', front, flags=re.M)
    if not match:
        raise ValueError("Image path missing from front matter.")
    return match.group("path")


def main() -> None:
    api_key = require_api_key()

    reserved_ids = {
        11044812,
        3582392,
        6814554,
        3597632,
        36028039,
        14887694,
        31505743,
        1448561,
        7513422,
        13766369,
        35076211,
        12102906,
        319968,
        28975867,
        6752846,
    }
    used_ids: set[int] = set()

    for config in ARTICLE_CONFIGS:
        file_path = ROOT / config.path
        text = file_path.read_text(encoding="utf-8")
        front, body = parse_front_matter(text)

        front = replace_block(front, "categories", config.categories)
        front = replace_block(front, "tags", config.tags)

        if config.replace_queries:
            photo = choose_unique_photo(api_key, config.replace_queries, reserved_ids | used_ids)
            photo_id = int(photo["id"])
            used_ids.add(photo_id)
            image_url = photo["src"].get("large2x") or photo["src"].get("large") or photo["src"]["original"]
            output_path = image_output_path(front)
            image_alt = config.image_alt or "Editorial cover image."
            download_and_resize(api_key, image_url, output_path)
            front = update_image_path(front, image_public_path(front), image_alt)
            source_name = photo.get("photographer", "Pexels contributor")
            source_url = photo.get("url", f"https://www.pexels.com/photo/{photo_id}/")
        else:
            photo_id = config.photo_id
            if photo_id is None:
                raise ValueError(f"Photo id missing for {config.path}")
            used_ids.add(photo_id)
            photo = get_photo(api_key, photo_id)
            source_name = photo.get("photographer", "Pexels contributor")
            source_url = photo.get("url", f"https://www.pexels.com/photo/{photo_id}/")

        front = upsert_scalar(front, "image_source_name", source_name)
        front = upsert_scalar(front, "image_source_url", source_url)

        if config.strip_lead_image:
            body = strip_lead_image(body)

        file_path.write_text(f"---\n{front}\n---\n{body}", encoding="utf-8")
        print(f"updated {config.path}")


if __name__ == "__main__":
    main()
