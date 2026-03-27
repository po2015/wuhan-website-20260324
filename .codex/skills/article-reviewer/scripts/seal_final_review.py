from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from review_workflow_utils import (
    build_sealed_review_payload,
    load_article,
    review_result_path,
    validate_review_payload,
)


REVIEW_RESULTS_DEFAULT = Path("tmp/article-review-results")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article", required=True, help="Article markdown file path")
    parser.add_argument("--input", required=True, help="Raw PASS review JSON file produced by a review round")
    parser.add_argument(
        "--review-root",
        default=str(REVIEW_RESULTS_DEFAULT),
        help="Directory containing final review JSON results",
    )
    parser.add_argument(
        "--workflow",
        default="article-review-loop",
        help="Workflow name to record in review_metadata.workflow",
    )
    args = parser.parse_args()

    article = load_article(Path(args.article))
    raw_review_path = Path(args.input)
    payload = json.loads(raw_review_path.read_text(encoding="utf-8"))
    errors = validate_review_payload(payload, require_pass=True)
    if errors:
        raise SystemExit(
            "Refusing to seal final review result because the raw review JSON is not a valid PASS:\n"
            + "\n".join(f"- {item}" for item in errors)
        )

    sealed_payload = build_sealed_review_payload(
        article=article,
        raw_review_payload=payload,
        source_round_path=raw_review_path,
        workflow_name=args.workflow,
    )

    review_root = Path(args.review_root)
    review_root.mkdir(parents=True, exist_ok=True)
    output_path = review_result_path(review_root, article["slug"])
    output_path.write_text(
        json.dumps(sealed_payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    sys.stdout.write(str(output_path.resolve()))


if __name__ == "__main__":
    main()
