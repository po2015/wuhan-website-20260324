from __future__ import annotations

import argparse
import json
from pathlib import Path

from review_workflow_utils import (
    article_has_pass_result,
    iter_articles,
    load_article,
    next_round_path,
    parse_date,
)


ROOT_DEFAULT = Path("content/en/knowledge-base")
REVIEW_RESULTS_DEFAULT = Path("tmp/article-review-results")
REVIEW_ROUNDS_DEFAULT = Path("tmp/article-review-runs")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT_DEFAULT), help="Knowledge-base directory")
    parser.add_argument(
        "--review-root",
        default=str(REVIEW_RESULTS_DEFAULT),
        help="Directory containing final review JSON results",
    )
    parser.add_argument(
        "--round-root",
        default=str(REVIEW_ROUNDS_DEFAULT),
        help="Directory containing intermediate per-round review JSON files",
    )
    parser.add_argument("--file", help="Specific article markdown file")
    parser.add_argument("--earliest", action="store_true", help="Select the earliest dated article")
    parser.add_argument(
        "--next-pending",
        action="store_true",
        help="Select the earliest article that does not yet have a trusted PASS review result",
    )
    parser.add_argument(
        "--strict-pass-only",
        action="store_true",
        help="Trust only sealed PASS review files with matching article hashes",
    )
    parser.add_argument("--text-only", action="store_true", help="Print only normalized article text")
    args = parser.parse_args()

    if sum([bool(args.file), bool(args.earliest), bool(args.next_pending)]) > 1:
        raise SystemExit("Use only one of --file, --earliest, or --next-pending.")

    root = Path(args.root)
    review_root = Path(args.review_root)
    round_root = Path(args.round_root)

    if args.file:
        article = load_article(Path(args.file))
    else:
        articles = iter_articles(root)
        if not articles:
            raise SystemExit("No knowledge-base articles found.")
        if args.next_pending:
            pending = [
                item
                for item in articles
                if not article_has_pass_result(
                    review_root=review_root,
                    article=item,
                    strict_pass_only=args.strict_pass_only,
                )
            ]
            if not pending:
                raise SystemExit("No pending knowledge-base articles found.")
            article = min(pending, key=lambda item: parse_date(item["date"]))
        else:
            article = min(articles, key=lambda item: parse_date(item["date"]))

    payload = {
        "path": article["path"],
        "title": article["title"],
        "slug": article["slug"],
        "date": article["date"],
        "article_sha256": article["article_sha256"],
        "normalized_review_input_sha256": article["normalized_review_input_sha256"],
        "next_round_path": str(next_round_path(round_root, article["slug"]).resolve()),
        "article_text": article["article_text"],
    }

    if args.text_only:
        print(payload["article_text"], end="")
        return

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
