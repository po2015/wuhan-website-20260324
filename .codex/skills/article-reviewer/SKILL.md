---
name: article-reviewer
description: Review a single knowledge-base or B2B technical article and return only strict JSON for workflow automation. Use when the input is raw article text or a normalized article body and you need a PASS / REQUIRE_REVISION / REQUIRE_REWRITE decision with deterministic scoring.
---

# Article Reviewer

## Overview

Use this skill to review one article at a time against a strict 10-dimension editorial rubric and return automation-safe JSON only.

This skill is for article QA, not article writing. It should be used when the user wants a structured review result, a gating decision, or machine-readable editorial feedback.

## Workflow

1. If the user gives a repository article file instead of raw text, run `scripts/prepare_kb_article_review.py`.
2. Read `references/review-rubric.md` for the scoring rules and decision logic.
3. Read `references/review-schema.json` for the exact output contract.
4. Review the article body only. Ignore YAML front matter for scoring except when title, description, or keypoints are intentionally included in the normalized review input.
5. Return only valid JSON. No markdown, no code fences, no commentary before or after the JSON object.
6. In iterative QA workflows, treat any score below pass threshold as blocked work: revise the article for `REQUIRE_REVISION`, rewrite the article for `REQUIRE_REWRITE`, then review again until the result is `PASS`.

## Input Contract

- Preferred input: raw article text
- Acceptable normalized input: title, description, keypoints, and article body prepared by `scripts/prepare_kb_article_review.py`
- Scope: one article only

## Deterministic Output Rules

- Output must match `references/review-schema.json` exactly
- Preserve the key order from the schema
- `overall_score` must be the arithmetic mean of the 10 dimension scores, rounded to 1 decimal place
- `dimension_scores` values must be integers from `1` to `10`
- `word_count` must be an integer based on the article text being reviewed
- `failed_dimensions_below_5` must list only dimensions with scores below `5`, in schema order
- Arrays must always be present; use `[]` when there is nothing to list
- Keep findings concrete and article-specific
- Never output markdown

## Review Boundaries

- Be strict
- Do not reward fluency if the content is generic or padded
- Do not invent missing evidence
- Do not soften the final decision when the rubric says the article fails
- If a dimension is weak enough to block publication, score it accordingly instead of hiding the problem inside prose
- `PASS` requires an `overall_score` of at least `8.0`, `word_count >= 1000`, and no dimension below `5`

## Repo Workflow

When reviewing Cyrentis knowledge-base content in this repo:

- Use `python .codex/skills/article-reviewer/scripts/prepare_kb_article_review.py --earliest`
  to select the earliest dated article and emit normalized review input
- Use `python .codex/skills/article-reviewer/scripts/prepare_kb_article_review.py --file <path>`
  to review a specific article

The script helps automation by selecting the file, stripping front matter, and producing a stable text payload for this skill.
