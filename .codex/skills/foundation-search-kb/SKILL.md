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
5. Write for first-pass `PASS` under the knowledge-base reviewer rubric even though the tone is simpler than the professional KB format.
6. Build the article to at least `1500` words of substantive explanation unless the user explicitly asks for a shorter answer.
If the beginner topic feels too short, expand with mechanisms, common misunderstandings, real-world implications, limitations, and a practical decision section rather than filler.
7. Keep the article focused on the reader's question, not on Cyrentis promotion.
8. Prefer custom explanatory diagrams, charts, or tables stored under `static/images/knowledge-base/`.
9. Do not use Pexels-style photography unless the user explicitly asks for it.
10. Do not reuse an existing knowledge-base lead image or article-specific figure unless the user explicitly asks for reuse.
11. If creating SVG figures, read `references/svg-diagram-rules.md` first.
12. Prefer D2 for box-and-arrow diagrams, labeled workflows, and comparison figures with multiple text blocks.
13. Use `scripts/render_d2_svg.ps1` to render `.d2` sources into SVG when D2 is a good fit.
14. End with `## Related Reading` and include at least one authoritative external link there, while keeping internal links to no more than three.
15. Before finalizing, self-check the article for reviewer risk: weak closure, shallow explanation, low decision value, repetitive filler, generic AI transitions, or keyword-led padding.
16. Rebuild with `conda run -n python314 hugo --cleanDestinationDir` when done.

## Output Rules

- Default destination: `content/en/knowledge-base/<slug>.md`
- Category rule: always include `Foundation`
- Tone: clear, concrete, search-friendly, and technically correct
- Length: target `1500-1900` words; treat `1500` as the default floor unless the user explicitly requests a shorter format
- Structure: introduction plus practical `##` sections, including plain-language mechanism explanation, practical implications, and at least one limitations, comparison, or common-mistakes section
- Related Reading links: final section only; include at least `1` authoritative external link and no more than `3` internal links unless the user explicitly asks otherwise
- Product mentions: avoid by default; include only when the user explicitly wants product context or there is a strong technical reason
- Figures: prefer self-drawn SVG diagrams, labeled comparison tables, or synthesized explanatory charts
- Image uniqueness: do not reuse the same lead image, stock photo, or article-specific figure across multiple knowledge-base articles unless the user explicitly asks for reuse
- SVG rule: use hand-authored SVG only for simple explanatory figures with predictable layout; use a layout engine or design tool when the figure has many boxes, connectors, or labels
- D2 rule: for structured diagrams with labels, prefer D2 source plus rendered SVG over fully hand-positioned SVG
- Figure honesty: if a chart or diagram is synthesized rather than drawn from one public dataset, say so in the caption or nearby text
- Do not end on a thin definition-only section; add a short takeaway or closing synthesis when the article would otherwise feel unfinished
- Do not pad to reach length; each extra section should reduce beginner confusion or improve practical judgment
- Never fabricate:
  - measured performance data
  - standards positions
  - third-party validation
  - sourced-looking charts without a real basis

## Resources

- `references/foundation-standard.md`: structure, tone, link limits, and diagram guidance for search-entry Foundation articles
- `references/svg-diagram-rules.md`: hard rules for text layout, sizing, icon style, and tool selection when creating SVG diagrams
- `scripts/render_d2_svg.ps1`: local wrapper for rendering `.d2` sources into SVG with a stable layout-engine default
