from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT_DEFAULT = Path("content/en/knowledge-base")
EXCLUDED_FILES = {"_index.md", "template.md"}
REVIEW_RESULTS_DEFAULT = Path("tmp/article-review-results")


def split_front_matter(text: str) -> tuple[str, str]:
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
    value = read_scalar(front_matter, "draft").lower()
    return value == "true"


def normalize_article_text(title: str, description: str, keypoints: list[str], body: str) -> str:
    parts: list[str] = []
    if title:
        parts.append(f"Title: {title}")
    if description:
        parts.append(f"Description: {description}")
    if keypoints:
        keypoint_lines = "\n".join(f"- {item}" for item in keypoints)
        parts.append(f"Keypoints:\n{keypoint_lines}")
    parts.append("Article:\n" + body.strip())
    return "\n\n".join(parts).strip() + "\n"


def review_result_path(review_root: Path, slug: str) -> Path:
    return review_root / f"{slug}.review.json"


def article_has_pass_result(review_root: Path, slug: str) -> bool:
    result_path = review_result_path(review_root, slug)
    if not result_path.exists():
        return False
    try:
        payload = json.loads(result_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return payload.get("final_decision") == "PASS"


def iter_articles(root: Path) -> list[dict]:
    articles: list[dict] = []
    for path in root.glob("*.md"):
        if path.name in EXCLUDED_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        front_matter, body = split_front_matter(text)
        if not front_matter or is_draft(front_matter):
            continue

        date_text = read_scalar(front_matter, "date")
        title = read_scalar(front_matter, "title")
        slug = read_scalar(front_matter, "slug")
        description = read_scalar(front_matter, "description")
        keypoints = read_list(front_matter, "keypoints")
        if not date_text:
            continue

        articles.append(
            {
                "path": str(path.resolve()),
                "title": title,
                "slug": slug,
                "date": date_text,
                "description": description,
                "keypoints": keypoints,
                "body": body,
                "article_text": normalize_article_text(title, description, keypoints, body),
            }
        )
    return articles


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT_DEFAULT), help="Knowledge-base directory")
    parser.add_argument(
        "--review-root",
        default=str(REVIEW_RESULTS_DEFAULT),
        help="Directory containing review JSON results",
    )
    parser.add_argument("--file", help="Specific article markdown file")
    parser.add_argument("--earliest", action="store_true", help="Select the earliest dated article")
    parser.add_argument(
        "--next-pending",
        action="store_true",
        help="Select the earliest article that does not yet have a PASS review result",
    )
    parser.add_argument("--text-only", action="store_true", help="Print only normalized article text")
    args = parser.parse_args()

    if sum([bool(args.file), bool(args.earliest), bool(args.next_pending)]) > 1:
        raise SystemExit("Use only one of --file, --earliest, or --next-pending.")

    root = Path(args.root)
    review_root = Path(args.review_root)
    if args.file:
        path = Path(args.file)
        text = path.read_text(encoding="utf-8")
        front_matter, body = split_front_matter(text)
        article = {
            "path": str(path.resolve()),
            "title": read_scalar(front_matter, "title"),
            "slug": read_scalar(front_matter, "slug"),
            "date": read_scalar(front_matter, "date"),
            "description": read_scalar(front_matter, "description"),
            "keypoints": read_list(front_matter, "keypoints"),
            "body": body,
        }
        article["article_text"] = normalize_article_text(
            article["title"], article["description"], article["keypoints"], article["body"]
        )
    else:
        articles = iter_articles(root)
        if not articles:
            raise SystemExit("No knowledge-base articles found.")
        if args.next_pending:
            pending = [item for item in articles if not article_has_pass_result(review_root, item["slug"])]
            if not pending:
                raise SystemExit("No pending knowledge-base articles found.")
            selected = min(pending, key=lambda item: parse_date(item["date"]))
        else:
            selected = min(articles, key=lambda item: parse_date(item["date"]))
        article = selected

    payload = {
        "path": article["path"],
        "title": article["title"],
        "slug": article["slug"],
        "date": article["date"],
        "article_text": article["article_text"],
    }

    if args.text_only:
        print(payload["article_text"], end="")
        return

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
