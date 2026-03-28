from __future__ import annotations

import argparse
import base64
import io
import json
import mimetypes
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageOps

try:
    import winreg  # type: ignore
except ImportError:  # pragma: no cover
    winreg = None


API_ROOT = "https://api.replicate.com/v1"
MODEL_OWNER = "stability-ai"
MODEL_NAME = "sdxl"
DEFAULT_TARGET_SIZE = (1280, 720)


def resolve_token() -> str:
    token = os.environ.get("REPLICATE_API_TOKEN", "").strip()
    if token:
        return token

    if winreg is not None:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
            value, _ = winreg.QueryValueEx(key, "REPLICATE_API_TOKEN")
            if isinstance(value, str) and value.strip():
                return value.strip()
        except OSError:
            pass

    raise SystemExit("REPLICATE_API_TOKEN is missing from the process and Windows user environment.")


def to_data_uri(path: Path) -> str:
    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{data}"


def latest_version_id(token: str) -> str:
    url = f"{API_ROOT}/models/{MODEL_OWNER}/{MODEL_NAME}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, timeout=60)
    response.raise_for_status()
    payload = response.json()
    latest = payload.get("latest_version", {})
    version_id = latest.get("id", "").strip()
    if not version_id:
        raise SystemExit(f"Could not resolve latest version id for {MODEL_OWNER}/{MODEL_NAME}.")
    return version_id


def create_prediction(
    token: str,
    version_id: str,
    prompt: str,
    image_data_uri: str,
    mask_data_uri: str | None,
    seed: int,
    negative_prompt: str,
    width: int,
    height: int,
    prompt_strength: float,
    guidance_scale: float,
    num_inference_steps: int,
) -> dict[str, Any]:
    url = f"{API_ROOT}/predictions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "wait=60",
        "Cancel-After": "5m",
    }
    payload = {
        "version": version_id,
        "input": {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "image": image_data_uri,
            "width": width,
            "height": height,
            "num_outputs": 1,
            "scheduler": "K_EULER",
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "prompt_strength": prompt_strength,
            "seed": seed,
            "refine": "expert_ensemble_refiner",
            "high_noise_frac": 0.8,
            "apply_watermark": False,
        }
    }
    if mask_data_uri:
        payload["input"]["mask"] = mask_data_uri
    for attempt in range(5):
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        if response.status_code != 429:
            response.raise_for_status()
            return response.json()
        sleep_seconds = min(20, 2 * (attempt + 1))
        time.sleep(sleep_seconds)

    response.raise_for_status()
    return response.json()


def poll_prediction(token: str, prediction: dict[str, Any]) -> dict[str, Any]:
    status = prediction.get("status")
    if status in {"succeeded", "failed", "canceled"}:
        return prediction

    get_url = prediction["urls"]["get"]
    headers = {"Authorization": f"Bearer {token}"}
    deadline = time.time() + 300

    while time.time() < deadline:
        response = requests.get(get_url, headers=headers, timeout=60)
        response.raise_for_status()
        prediction = response.json()
        status = prediction.get("status")
        if status in {"succeeded", "failed", "canceled"}:
            return prediction
        time.sleep(2)

    raise SystemExit(f"Timed out waiting for prediction {prediction.get('id')}.")


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


def save_output(image_url: str, output_path: Path, width: int, height: int) -> None:
    response = requests.get(image_url, timeout=120)
    response.raise_for_status()
    image = resize_cover(response.content, width, height)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path, format="JPEG", quality=86, optimize=True, progressive=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--mask")
    parser.add_argument("--seed", type=int, default=1001)
    parser.add_argument("--negative-prompt", default="")
    parser.add_argument("--width", type=int, default=DEFAULT_TARGET_SIZE[0])
    parser.add_argument("--height", type=int, default=DEFAULT_TARGET_SIZE[1])
    parser.add_argument("--prompt-strength", type=float, default=0.48)
    parser.add_argument("--guidance-scale", type=float, default=7.5)
    parser.add_argument("--steps", type=int, default=45)
    parser.add_argument("--metadata-output", help="Optional JSON metadata output path")
    args = parser.parse_args()

    token = resolve_token()
    version_id = latest_version_id(token)
    reference_path = Path(args.reference)
    output_path = Path(args.output)
    image_data_uri = to_data_uri(reference_path)
    mask_data_uri = to_data_uri(Path(args.mask)) if args.mask else None
    negative_prompt = args.negative_prompt or (
        "cartoon, illustration, CGI, toy-like radar, duplicate radar, extra antennas, malformed radar, "
        "blurry, overprocessed, text, watermark, logo, low detail, deformed mast, duplicated objects"
    )

    prediction = create_prediction(
        token=token,
        version_id=version_id,
        prompt=args.prompt,
        image_data_uri=image_data_uri,
        mask_data_uri=mask_data_uri,
        seed=args.seed,
        negative_prompt=negative_prompt,
        width=args.width,
        height=args.height,
        prompt_strength=args.prompt_strength,
        guidance_scale=args.guidance_scale,
        num_inference_steps=args.steps,
    )
    prediction = poll_prediction(token, prediction)

    if prediction.get("status") != "succeeded":
        raise SystemExit(
            f"Prediction failed with status={prediction.get('status')}: {prediction.get('error')}"
        )

    outputs = prediction.get("output") or []
    if not outputs:
        raise SystemExit("Prediction succeeded but returned no output.")

    image_url = outputs[0]
    save_output(image_url, output_path, args.width, args.height)

    metadata = {
        "model": f"{MODEL_OWNER}/{MODEL_NAME}",
        "version": version_id,
        "prediction_id": prediction.get("id"),
        "source_output_url": image_url,
        "prompt": args.prompt,
        "reference": str(reference_path.resolve()),
        "output": str(output_path.resolve()),
        "seed": args.seed,
        "prompt_strength": args.prompt_strength,
        "guidance_scale": args.guidance_scale,
        "steps": args.steps,
    }
    if args.metadata_output:
        metadata_path = Path(args.metadata_output)
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(metadata, ensure_ascii=False))


if __name__ == "__main__":
    main()
