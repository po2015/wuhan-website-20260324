---
name: foundation-search-kb
description: Write beginner-friendly Cyrentis knowledge-base articles for `content/en/knowledge-base/` when the goal is capturing broad search intent with simple language, short-to-medium explainers, minimal promotion, and light structure. Use for topics such as "what is X", "how does X work", "X basics", "complete guide", or glossary-style radar and sensing introductions. Prefer custom diagrams or charts over stock photography, keep internal links out of the main body, and place these articles in the `Foundation` category.
---

# Foundation Search KB

Use this skill to produce top-of-funnel knowledge-base articles that are easier to read than the standard professional KB format.

## Workflow

1. Start from `content/en/knowledge-base/template.md`, but simplify the structure.
2. Read `references/foundation-standard.md` before drafting.
3. Browse authoritative sources first. Prefer government agencies, standards bodies, research institutions, and official technical documentation.
4. Explain specialized terms in plain language the first time they appear.
5. Keep the article focused on the reader's question, not on Cyrentis promotion.
6. Prefer custom explanatory diagrams, charts, or tables stored under `static/images/knowledge-base/`.
7. Do not use Pexels-style photography unless the user explicitly asks for it.
8. Do not reuse an existing knowledge-base lead image or article-specific figure unless the user explicitly asks for reuse.
9. If creating SVG figures, read `references/svg-diagram-rules.md` first.
10. Prefer D2 for box-and-arrow diagrams, labeled workflows, and comparison figures with multiple text blocks.
11. Use `scripts/render_d2_svg.ps1` to render `.d2` sources into SVG when D2 is a good fit.
12. End with `## Related Reading` and include at least one authoritative external link there, while keeping internal links to no more than three.
13. Rebuild with `conda run -n python314 hugo --cleanDestinationDir` when done.

## Output Rules

- Default destination: `content/en/knowledge-base/<slug>.md`
- Category rule: always include `Foundation`
- Tone: clear, concrete, search-friendly, and technically correct
- Length: usually `800-1500` words unless the topic needs more
- Structure: introduction plus practical `##` sections; no mandatory `Where Cyrentis Fits` or `Conclusion`
- Related Reading links: final section only; include at least `1` authoritative external link and no more than `3` internal links unless the user explicitly asks otherwise
- Product mentions: avoid by default; include only when the user explicitly wants product context or there is a strong technical reason
- Figures: prefer self-drawn SVG diagrams, labeled comparison tables, or synthesized explanatory charts
- Image uniqueness: do not reuse the same lead image, stock photo, or article-specific figure across multiple knowledge-base articles unless the user explicitly asks for reuse
- SVG rule: use hand-authored SVG only for simple explanatory figures with predictable layout; use a layout engine or design tool when the figure has many boxes, connectors, or labels
- D2 rule: for structured diagrams with labels, prefer D2 source plus rendered SVG over fully hand-positioned SVG
- Figure honesty: if a chart or diagram is synthesized rather than drawn from one public dataset, say so in the caption or nearby text
- Never fabricate:
  - measured performance data
  - standards positions
  - third-party validation
  - sourced-looking charts without a real basis

## Resources

- `references/foundation-standard.md`: structure, tone, link limits, and diagram guidance for search-entry Foundation articles
- `references/svg-diagram-rules.md`: hard rules for text layout, sizing, icon style, and tool selection when creating SVG diagrams
- `scripts/render_d2_svg.ps1`: local wrapper for rendering `.d2` sources into SVG with a stable layout-engine default
