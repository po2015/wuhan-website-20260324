---
name: news-reviewer
description: Review one Cyrentis company news draft and return strict JSON only. Use for official company news items that must be judged for tone, factuality, time specificity, newsworthiness, structure, and low marketing noise.
---

# News Reviewer

Use this skill to review **one** company news article draft for `content/en/news/`.

This reviewer is based on [news-reviewer.md](E:/Cyrentis/site/docs/news-reviewer.md).

## Scope

This is for official company news such as:

- holiday greetings
- company event news
- milestone announcements
- exhibition participation news
- policy interpretation
- official company statements
- official notices
- general company updates

This is **not** for:

- knowledge-base articles
- long-form blog commentary
- product landing pages
- sales copy

## Workflow

1. Read [news-reviewer.md](E:/Cyrentis/site/docs/news-reviewer.md).
2. Use `references/review-output-schema.json` as the output contract.
3. Review one article only.
4. Return only valid JSON.
5. Do not add markdown, explanation, or wrapper text.

## Review Rules

- Be strict.
- Do not inflate scores because the wording is polished.
- Penalize vague, timeless, or generic corporate filler.
- Penalize any piece that reads more like a product page or company profile than a news item.
- For company-originated news, penalize body copy that keeps referring to the company in third person instead of using first-person corporate voice.
- If word count exceeds `1000`, the result cannot be `PASS`.
- If any critical dimension is below `5`, return `REQUIRE_REWRITE`.
