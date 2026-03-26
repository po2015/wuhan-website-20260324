---
name: professional-kb-articles
description: Write rigorous Cyrentis knowledge-base articles for `content/en/knowledge-base/` when the task is technical education, standards interpretation, system-design explanation, or SEO knowledge content. Use for evidence-based articles that require primary sources, accurate terminology, sourced charts or tables, restrained internal linking, and a non-promotional tone.
---

# Professional KB Articles

Use this skill when drafting or revising Cyrentis knowledge-base articles that should read like technical explainers, engineering notes, or standards-aware educational content.

## Workflow

1. Start from `content/en/knowledge-base/template.md`.
2. Read `references/article-standard.md` and `references/taxonomy-guidance.md` before drafting.
3. Browse primary sources first: standards bodies, government agencies, academic papers, official technical documentation, or reputable research institutions.
4. Keep the article educational. Do not write sales copy, feature boasting, or unsupported competitive claims.
5. Use charts, tables, or diagrams only when the underlying data is public, citable, and methodologically clear.
6. If no trustworthy numeric dataset is available, do not invent a chart. Use a sourced comparison table or a labeled logic diagram instead.
7. Add internal links only where they genuinely improve comprehension, planning, or system selection.
8. Keep external links authoritative and directly relevant to the technical claim they support.
9. If the article needs a stock lead image, use `scripts/fetch_pexels_cover.py`, then add `image_source_name` and `image_source_url`. Before finalizing, check existing knowledge-base articles and do not reuse the same stock photo, `image_source_url`, or cover asset.
10. Rebuild with `conda run -n python314 hugo --cleanDestinationDir` when done.

## Output Rules

- Default destination: `content/en/knowledge-base/<slug>.md`
- Tone: technical, explanatory, calm, and evidence-led
- Purpose: knowledge transfer first, SEO second, product promotion last
- Allowed Cyrentis mention: only when there is a real technical fit or a clear system-design connection
- Never fabricate:
  - field data
  - performance comparisons
  - standards positions
  - scientific charts
  - third-party endorsements
- Every numeric claim should have a source, a unit, and enough context to understand what it means
- Prefer exact dates when discussing regulations, standards updates, or published studies

## Figure Rules

- Use a public stock image only as a lead visual, not as technical evidence
- Lead images must be unique across `content/en/knowledge-base/`; do not reuse the same stock photo, source URL, or previously generated cover file for another knowledge-base article unless the user explicitly asks for reuse
- Technical figures should be one of:
  - sourced data chart
  - sourced comparison table
  - clearly labeled explanatory diagram
- If a figure is based on synthesis rather than a public dataset, say so explicitly in the caption or surrounding text
- Keep figure filenames SEO-friendly and slug-based
- Keep image sizes lightweight; the current project standard is `960x540`

## Resources

- `references/article-standard.md`: article structure, evidence rules, and figure policy
- `references/taxonomy-guidance.md`: practical category and tag guidance for knowledge-base content
- `scripts/fetch_pexels_cover.py`: generic Pexels downloader and `960x540` cover resizer
