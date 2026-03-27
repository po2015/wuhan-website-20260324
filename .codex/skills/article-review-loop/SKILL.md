---
name: article-review-loop
description: Enforce the Cyrentis article QA loop: review, revise or rewrite, review again until PASS, then seal the final PASS result with article-hash validation so only trusted results leave the queue.
---

# Article Review Loop

## Overview

Use this skill when the user wants to review Cyrentis repo articles under a **hard-gated workflow** instead of a soft prompt-only workflow.

This skill is the repo entrypoint for article QA loops.

It enforces:

1. review
2. revise or rewrite if needed
3. review again
4. repeat until PASS
5. seal only the final PASS result

The subordinate reviewer is [$article-reviewer](E:/Cyrentis/site/.codex/skills/article-reviewer/SKILL.md).

## Non-Negotiable Rules

- Never manually create or edit `tmp/article-review-results/<slug>.review.json`
- Every review round must exist as a raw JSON file in `tmp/article-review-runs/<slug>/`
- Only the latest PASS round may be promoted into `tmp/article-review-results/`
- Promotion must happen through `scripts/seal_final_review.py`
- Queue selection must use `--strict-pass-only`

## Workflow

1. Select the target article:
   `python .codex/skills/article-reviewer/scripts/prepare_kb_article_review.py --next-pending --strict-pass-only`

2. For a specific article, use:
   `python .codex/skills/article-reviewer/scripts/prepare_kb_article_review.py --file <path> --strict-pass-only`

3. Read the returned payload:
   - `path`
   - `article_text`
   - `next_round_path`
   - `article_sha256`
   - `normalized_review_input_sha256`

4. Review `article_text` with [$article-reviewer](E:/Cyrentis/site/.codex/skills/article-reviewer/SKILL.md) and save the raw JSON exactly to `next_round_path`

5. If the round result is:
   - `REQUIRE_REWRITE`: rewrite the article substantially, then go back to step 2
   - `REQUIRE_REVISION`: revise the article against the findings, then go back to step 2
   - `PASS`: continue to step 6

6. Seal the final PASS result:
   `python .codex/skills/article-reviewer/scripts/seal_final_review.py --article <path> --input <next_round_path>`

7. A review is complete only when the sealed PASS file exists and the strict queue no longer selects that article as pending

## Why This Is Hard-Gated

The strict queue trusts only sealed PASS files that contain:

- the current absolute article path
- the current article content SHA-256
- the current normalized review-input SHA-256
- a valid PASS review payload that still satisfies the scoring rules

If the article changes after the PASS file is sealed, the queue will treat that article as pending again.

## Output Discipline

- Intermediate review rounds live in `tmp/article-review-runs/<slug>/round-XX.review.json`
- Final trusted PASS file lives in `tmp/article-review-results/<slug>.review.json`
- The final trusted PASS file is not the raw reviewer output; it is the sealed PASS output created by `seal_final_review.py`
