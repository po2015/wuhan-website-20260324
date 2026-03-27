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
12. Use D2 as the default for any workflow, comparison, service-stack, architecture, or multi-box explanatory figure.
13. Treat D2 as mandatory, not optional, when a figure has more than `3` labeled boxes, any connectors between boxes, sentence-length labels, or multiple rows of explanatory text.
14. Hand-authored SVG is allowed only for Foundation covers or simple object diagrams with predictable layout and short labels.
15. When D2 is used, save the `.d2` source alongside the rendered SVG using the same basename when practical.
16. Use `scripts/render_d2_svg.ps1` to render `.d2` sources into SVG.
17. Foundation cover images should use one standardized hand-authored SVG cover style across the series unless the user explicitly asks for a different cover system.
18. The standardized Foundation cover should follow the visual language already used by `what-is-utm-u-space` and `what-is-remote-id`:
   - title block
   - subtitle
   - topic-specific background scene
   - optional `2-3` short support items or tags
19. Foundation cover titles must stay inside the title background block. Do not let any title glyphs spill outside the colored title panel.
20. If a Foundation cover title is shorter than roughly `80%` of the image width, keep it on one line. Only wrap when a single-line title would clearly exceed that threshold or become unreadably small.
21. Foundation covers are for the lead image only. Do not reuse the cover image inside the article body.
22. Internal figures should remain topic-specific. Do not let every internal figure default to the same box-card template. At least one internal figure per article should be topic-native, such as a waveform, scan sector, scene comparison, sensing geometry, or physical process sketch.
23. Cover images should stay simpler than internal diagrams. Keep the cover readable as a list thumbnail: title, subtitle, and background should remain clear even when reduced.
24. In D2, do not give fixed heights to text-bearing boxes unless the rendered SVG has already been checked and confirmed safe. Prefer auto height plus explicit manual line breaks.
25. Every D2 text box must use short phrase labels with manual line breaks. Keep each box to roughly `2-4` short lines and avoid sentence-length single lines inside shapes.
26. Before finalizing, visually check every figure for article-width and mobile-width safety. No overlaps, no cropped text, no giant text blocks, and no labels that depend on perfect desktop scaling.
27. End with `## Related Reading` and include at least one authoritative external link there, while keeping internal links to no more than three.
28. Before finalizing, self-check the article for reviewer risk: weak closure, shallow explanation, low decision value, repetitive filler, generic AI transitions, or keyword-led padding.
29. Rebuild with `conda run -n python314 hugo --cleanDestinationDir` when done.

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
- SVG rule: use hand-authored SVG for the standardized Foundation cover system or for simple explanatory figures with predictable layout and short labels; do not hand-position complex text-heavy workflow graphics
- D2 rule: for structured diagrams with labels, use D2 source plus rendered SVG instead of fully hand-positioned SVG
- Figure gate: if a figure has more than `3` labeled boxes, any arrows between labeled blocks, or sentence-length text inside shapes, it must be built in D2 or another layout tool
- Figure QA: before finalizing, confirm the SVG remains readable at article width and on a narrow mobile viewport without overlaps or cropped text
- D2 text rule: break labels manually into short lines; do not leave D2 to carry a long sentence on one line inside a box
- D2 sizing rule: avoid fixed heights on text boxes unless the rendered SVG has been checked and all text baselines stay inside the box bounds
- Cover consistency rule: Foundation covers should follow the shared `what-is-utm-u-space` / `what-is-remote-id` style with a title block, subtitle, and topic-specific background unless the user explicitly asks for a different cover system
- Cover title-fit rule: Foundation cover titles must remain inside the title block, and titles that fit within about `80%` of the canvas width should stay on one line
- Cover-body separation rule: the cover image belongs only in front matter as the lead image and must not be embedded again in the article body
- Internal diversity rule: do not let all figures in one article collapse into the same card-grid or step-card style
- Topic motif rule: internal figures should include visual cues native to the topic, such as pulses and range rings for radar, array panels and beam steering for phased array, or heat gradients and infrared surfaces for thermal imaging
- Text-weight rule: avoid large text-heavy blocks that visually read like slides rather than diagrams
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
