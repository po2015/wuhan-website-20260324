---
name: product-detail-reviewer
description: Review rendered B2B industrial product detail pages and return strict JSON for workflow automation. Use when evaluating customer-facing product pages for technical clarity, product positioning, conversion readiness, procurement trust, or page-quality triage. Trigger this skill for rendered HTML from product pages such as radar, electro-optical, RF detection, security hardware, sensing devices, or control-platform detail pages.
---

# Product Detail Reviewer

Use rendered HTML as the primary truth. Review the page as a product landing page, not as a blog post and not as raw markdown.

## Workflow

1. Read [docs/product-detail-reviewer.md](E:/Cyrentis/site/docs/product-detail-reviewer.md) before scoring anything.
2. Collect the final rendered HTML for the page being reviewed.
If the page belongs to this Hugo repo and a fresh build is needed, run `conda run -n python314 hugo --cleanDestinationDir` and read the corresponding file under `public/`.
3. Extract signals from the rendered HTML first:
page metadata, heading structure, hero, CTAs, feature blocks, spec tables, use-case sections, internal links, trust signals, and structural balance.
4. Use `source_content` only as secondary context.
Do not let markdown/front matter overrule the rendered page if the rendered page is thin, broken, or missing sections.
5. Score the page using the exact 10 dimensions and exact decision rules from the doc.
6. Return only strict JSON that follows [review-output-schema.json](E:/Cyrentis/site/.codex/skills/product-detail-reviewer/references/review-output-schema.json).

## Decision Rules

- If any critical dimension is below `5`, set `final_decision` to `REQUIRE_REWRITE`.
- Else if `overall_score < 7`, set `final_decision` to `REQUIRE_REVISION`.
- Else if two or more of `specifications`, `use_cases`, or `cta` are `weak` or `missing`, set `final_decision` to `REQUIRE_REVISION`.
- Else set `final_decision` to `PASS`.
- Be strict. Penalize thin pages, vague hero copy, weak specs, and unclear CTA paths hard.

## Product Family Routing

Apply one specialized reviewer when the page belongs to a known family:

- Use [src-product-detail-reviewer](E:/Cyrentis/site/.codex/skills/src-product-detail-reviewer/SKILL.md) for pages under `content/en/sensors/src/` or radar-detail layouts.
- Use [soc-product-detail-reviewer](E:/Cyrentis/site/.codex/skills/soc-product-detail-reviewer/SKILL.md) for pages under `content/en/sensors/soc/` or optical-detail layouts.
- Use [sdc-product-detail-reviewer](E:/Cyrentis/site/.codex/skills/sdc-product-detail-reviewer/SKILL.md) for pages under `content/en/sensors/sdc/` or RF-detector-detail layouts.

Use the shared decision schema either way. The family-specific skill only changes what counts as a strong or weak page for that product class.

## Output Rules

Return JSON only. No markdown. No explanations around the JSON.

When the user asks for findings rather than raw JSON, still score with the same rubric first, then summarize the findings separately.

## Repair Guidance

If the user asks to fix the page after review:

1. Diagnose against rendered HTML, not only front matter.
2. Fix the page at the narrowest safe scope first.
For a single product page, prefer page content changes and page-specific layouts over global template edits.
3. Rebuild and re-check the rendered page after changes.
