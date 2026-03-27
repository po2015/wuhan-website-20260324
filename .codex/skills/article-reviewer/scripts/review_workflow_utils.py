from __future__ import annotations

import hashlib
import json
import re
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PASS_THRESHOLD = 8.0
MIN_WORD_COUNT = 1000
FINAL_REVIEW_SCHEMA_VERSION = 2
EXCLUDED_FILES = {"_index.md", "template.md"}
ALLOWED_DECISIONS = {"PASS", "REQUIRE_REVISION", "REQUIRE_REWRITE"}
REVIEW_KEY_ORDER = [
    "final_decision",
    "reason_for_decision",
    "overall_score",
    "word_count",
    "dimension_scores",
    "failed_dimensions_below_5",
    "ai_signals_detected",
    "major_issues",
    "revision_actions",
    "rewrite_actions",
    "strengths",
    "summary_assessment",
]
REVIEW_DIMENSIONS = [
    "structure_logical_clarity",
    "target_classification_content_framing",
    "marketing_noise_control",
    "content_depth",
    "readability_human_quality",
    "information_density",
    "seo_knowledge_base_fitness",
    "technical_credibility",
    "decision_value",
    "original_insight",
]
REVIEW_ARRAY_FIELDS = [
    "failed_dimensions_below_5",
    "ai_signals_detected",
    "major_issues",
    "revision_actions",
    "rewrite_actions",
    "strengths",
]


def compute_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_front_matter(text: str) -> tuple[str, str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return "", text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1].strip(), parts[2].lstrip()


def read_scalar(front_matter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", front_matter)
    if not match:
        return ""
    value = match.group(1).strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    return value


def read_list(front_matter: str, key: str) -> list[str]:
    pattern = rf"(?ms)^{re.escape(key)}:\s*\n((?:\s+-\s+.+\n?)*)"
    match = re.search(pattern, front_matter)
    if not match:
        return []

    items: list[str] = []
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line.startswith("- "):
            continue
        item = line[2:].strip()
        if item.startswith('"') and item.endswith('"'):
            item = item[1:-1]
        if item.startswith("'") and item.endswith("'"):
            item = item[1:-1]
        items.append(item)
    return items


def parse_date(date_text: str) -> datetime:
    normalized = date_text.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def is_draft(front_matter: str) -> bool:
    return read_scalar(front_matter, "draft").lower() == "true"


def normalize_article_text(title: str, description: str, keypoints: list[str], body: str) -> str:
    parts: list[str] = []
    if title:
        parts.append(f"Title: {title}")
    if description:
        parts.append(f"Description: {description}")
    if keypoints:
        parts.append("Keypoints:\n" + "\n".join(f"- {item}" for item in keypoints))
    parts.append("Article:\n" + body.strip())
    return "\n\n".join(parts).strip() + "\n"


def load_article(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig")
    front_matter, body = split_front_matter(text)
    article_text = normalize_article_text(
        read_scalar(front_matter, "title"),
        read_scalar(front_matter, "description"),
        read_list(front_matter, "keypoints"),
        body,
    )
    return {
        "path": str(path.resolve()),
        "title": read_scalar(front_matter, "title"),
        "slug": read_scalar(front_matter, "slug"),
        "date": read_scalar(front_matter, "date"),
        "description": read_scalar(front_matter, "description"),
        "keypoints": read_list(front_matter, "keypoints"),
        "body": body,
        "raw_text": text,
        "article_text": article_text,
        "article_sha256": compute_sha256(text),
        "normalized_review_input_sha256": compute_sha256(article_text),
    }


def iter_articles(root: Path) -> list[dict[str, Any]]:
    articles: list[dict[str, Any]] = []
    for path in root.glob("*.md"):
        if path.name in EXCLUDED_FILES:
            continue
        text = path.read_text(encoding="utf-8-sig")
        front_matter, _body = split_front_matter(text)
        if not front_matter or is_draft(front_matter):
            continue
        date_text = read_scalar(front_matter, "date")
        if not date_text:
            continue
        articles.append(load_article(path))
    return articles


def review_result_path(review_root: Path, slug: str) -> Path:
    return review_root / f"{slug}.review.json"


def review_rounds_dir(round_root: Path, slug: str) -> Path:
    return round_root / slug


def next_round_path(round_root: Path, slug: str) -> Path:
    slug_dir = review_rounds_dir(round_root, slug)
    slug_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(slug_dir.glob("round-*.review.json"))
    round_number = len(existing) + 1
    return slug_dir / f"round-{round_number:02d}.review.json"


def expected_overall_score(dimension_scores: dict[str, Any]) -> float:
    total = sum(int(dimension_scores[key]) for key in REVIEW_DIMENSIONS)
    return round(total / len(REVIEW_DIMENSIONS), 1)


def compute_failed_dimensions(dimension_scores: dict[str, Any]) -> list[str]:
    return [key for key in REVIEW_DIMENSIONS if int(dimension_scores[key]) < 5]


def _json_number_to_float(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    return None


def validate_review_payload(payload: Any, require_pass: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["Review payload must be a JSON object."]

    for key in REVIEW_KEY_ORDER:
        if key not in payload:
            errors.append(f"Missing top-level key: {key}")

    if errors:
        return errors

    final_decision = payload.get("final_decision")
    if final_decision not in ALLOWED_DECISIONS:
        errors.append("final_decision must be PASS, REQUIRE_REVISION, or REQUIRE_REWRITE.")

    if not isinstance(payload.get("reason_for_decision"), str) or not payload["reason_for_decision"].strip():
        errors.append("reason_for_decision must be a non-empty string.")

    overall_score = _json_number_to_float(payload.get("overall_score"))
    if overall_score is None:
        errors.append("overall_score must be numeric.")

    word_count = payload.get("word_count")
    if not isinstance(word_count, int) or word_count < 0:
        errors.append("word_count must be a non-negative integer.")

    dimension_scores = payload.get("dimension_scores")
    if not isinstance(dimension_scores, dict):
        errors.append("dimension_scores must be an object.")
    else:
        for key in REVIEW_DIMENSIONS:
            value = dimension_scores.get(key)
            if not isinstance(value, int):
                errors.append(f"dimension_scores.{key} must be an integer.")
                continue
            if value < 1 or value > 10:
                errors.append(f"dimension_scores.{key} must be between 1 and 10.")

    for key in REVIEW_ARRAY_FIELDS:
        if not isinstance(payload.get(key), list):
            errors.append(f"{key} must be an array.")

    if not isinstance(payload.get("summary_assessment"), str) or not payload["summary_assessment"].strip():
        errors.append("summary_assessment must be a non-empty string.")

    if errors or not isinstance(dimension_scores, dict):
        return errors

    expected_failed = compute_failed_dimensions(dimension_scores)
    actual_failed = payload["failed_dimensions_below_5"]
    if actual_failed != expected_failed:
        errors.append("failed_dimensions_below_5 does not match the dimension scores.")

    expected_overall = expected_overall_score(dimension_scores)
    if overall_score is not None and round(overall_score, 1) != expected_overall:
        errors.append("overall_score does not match the arithmetic mean of the 10 dimensions.")

    if require_pass:
        if final_decision != "PASS":
            errors.append("Final review must have final_decision = PASS.")
        if isinstance(word_count, int) and word_count < MIN_WORD_COUNT:
            errors.append(f"PASS requires word_count >= {MIN_WORD_COUNT}.")
        if overall_score is not None and round(overall_score, 1) < PASS_THRESHOLD:
            errors.append(f"PASS requires overall_score >= {PASS_THRESHOLD:.1f}.")
        if expected_failed:
            errors.append("PASS requires no dimension score below 5.")

    return errors


def build_sealed_review_payload(
    article: dict[str, Any],
    raw_review_payload: dict[str, Any],
    source_round_path: Path,
    workflow_name: str,
) -> OrderedDict[str, Any]:
    sealed = OrderedDict()
    for key in REVIEW_KEY_ORDER:
        sealed[key] = raw_review_payload[key]
    sealed["review_metadata"] = OrderedDict(
        [
            ("schema_version", FINAL_REVIEW_SCHEMA_VERSION),
            ("workflow", workflow_name),
            ("article_path", article["path"]),
            ("article_sha256", article["article_sha256"]),
            ("normalized_review_input_sha256", article["normalized_review_input_sha256"]),
            ("source_round_path", str(source_round_path.resolve())),
            ("sealed_at_utc", datetime.now(timezone.utc).replace(microsecond=0).isoformat()),
        ]
    )
    return sealed


def validate_sealed_pass_result(article: dict[str, Any], payload: Any) -> list[str]:
    errors = validate_review_payload(payload, require_pass=True)
    if not isinstance(payload, dict):
        return errors

    metadata = payload.get("review_metadata")
    if not isinstance(metadata, dict):
        errors.append("Missing review_metadata block.")
        return errors

    if metadata.get("schema_version") != FINAL_REVIEW_SCHEMA_VERSION:
        errors.append("review_metadata.schema_version is invalid.")
    if metadata.get("article_path") != article["path"]:
        errors.append("review_metadata.article_path does not match the current article path.")
    if metadata.get("article_sha256") != article["article_sha256"]:
        errors.append("review_metadata.article_sha256 does not match the current article content.")
    if metadata.get("normalized_review_input_sha256") != article["normalized_review_input_sha256"]:
        errors.append(
            "review_metadata.normalized_review_input_sha256 does not match the current review input."
        )
    source_round_path = metadata.get("source_round_path")
    if not isinstance(source_round_path, str) or not source_round_path.strip():
        errors.append("review_metadata.source_round_path must be a non-empty string.")
    sealed_at = metadata.get("sealed_at_utc")
    if not isinstance(sealed_at, str) or not sealed_at.strip():
        errors.append("review_metadata.sealed_at_utc must be a non-empty string.")
    return errors


def article_has_pass_result(
    review_root: Path,
    article: dict[str, Any],
    strict_pass_only: bool = False,
) -> bool:
    result_path = review_result_path(review_root, article["slug"])
    if not result_path.exists():
        return False
    try:
        payload = json.loads(result_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False

    if strict_pass_only:
        return not validate_sealed_pass_result(article, payload)

    errors = validate_review_payload(payload, require_pass=True)
    if errors:
        return False
    metadata = payload.get("review_metadata")
    if isinstance(metadata, dict):
        strict_errors = validate_sealed_pass_result(article, payload)
        if not strict_errors:
            return True
    return payload.get("final_decision") == "PASS"
