# Foundation Search Article Standard

## Goal

Capture broad beginner search intent with content that is easy to understand on the first read and still technically sound.
The article should still be strong enough to pass the knowledge-base reviewer without needing a rewrite.

## Best-Fit Topics

- `What is radar?`
- `How does radar work?`
- `What is AESA?`
- `Radar vs sonar`
- `What is pulse-Doppler radar?`
- glossary-style or beginner guide topics

## Writing Rules

- Lead with the plain-language answer quickly.
- Use short paragraphs and direct wording.
- Define jargon once, then keep it simple.
- Explain why the concept matters in real life.
- Avoid white-paper tone, procurement language, and product bragging.
- Prefer a short conclusion or takeaway when the draft would otherwise end abruptly.
- Avoid definition-only writing; add enough mechanism, implications, and judgment to keep the page from feeling thin.

## Structure Pattern

Use a flexible pattern such as:

1. Short introduction with the plain-language answer
2. `##` sections that answer the obvious beginner questions
3. One section on common confusion, limitations, or practical trade-offs
4. Optional FAQ
5. Short takeaway or conclusion when helpful
6. Final `## Related Reading`

Good section types include:

- `## What Radar Means`
- `## How Radar Works`
- `## What Radar Can Measure`
- `## Main Parts of a Radar System`
- `## Common Types of Radar`
- `## Where Radar Is Used`
- `## Common Mistakes or Limits`
- `## What This Means in Practice`
- `## FAQ`

## Length Standard

- Default floor: `1500` words of substantive article text
- Preferred target: `1500-1900` words
- Do not pad with repetitive examples or keyword stuffing
- If the topic is simple, deepen it with real-world implications, common misconceptions, comparison logic, or operational limits

## Link Policy

- Keep internal links out of the main body by default.
- Use the final `## Related Reading` section for links.
- Include at least `1` authoritative external link in `## Related Reading`.
- Add no more than `3` internal links in `## Related Reading`.
- Do not add a `Where Cyrentis Fits` section unless the user explicitly asks for it.

## Category and Tags

- Always include `Foundation` in `categories`
- Use simple, searchable tags
- Prefer `1` category and `2-4` tags

## Figure Rules

- Prefer custom SVG diagrams, tables, or charts over stock photography.
- Do not reuse the same lead image or article-specific figure across multiple knowledge-base articles unless the user explicitly approves it.
- Use diagrams to explain mechanism, workflow, components, or comparisons.
- Keep the visual language clean and technical rather than decorative.
- Store generated figures in `static/images/knowledge-base/`.
- Use SEO-friendly filenames based on the article slug.
- If the figure is synthesized rather than sourced from one public dataset, state that near the figure.
- Treat Foundation covers and internal figures differently:
  - covers should use one standardized cover layout across the series
  - internal figures should remain topic-specific
- Standardized Foundation covers should follow the same visual language as `what-is-utm-u-space` and `what-is-remote-id`:
  - dark technical background
  - title block
  - subtitle
  - topic-specific background illustration
  - optional `2-3` short support items
- Keep the Foundation cover title fully inside the title block.
- If the title would still fit within about `80%` of the full image width, keep it on one line rather than wrapping it.
- For workflow, comparison, service-stack, or architecture diagrams, use D2 by default.
- If a figure has more than `3` labeled boxes, arrows between labeled blocks, or sentence-length labels, treat D2 as mandatory.
- Reserve hand-authored SVG for the standardized Foundation cover system or simple object diagrams with short labels and predictable layout.
- When D2 is used, keep the `.d2` source alongside the rendered SVG when practical so the figure can be revised cleanly later.
- In D2, prefer auto-height text boxes. Do not lock a text-bearing box to a fixed height unless the rendered SVG has been checked and the text is still inside the shape.
- Break D2 labels manually into short lines. Avoid sentence-length single lines inside shapes.
- Before finalizing, visually inspect the figure at article width and narrow mobile width. Reject it if text overlaps, spills, or turns into one large unreadable block.
- Use one shared Foundation cover skeleton across the series unless the user explicitly asks for a special cover.
- Keep Foundation covers simpler than internal figures: title, subtitle, background scene, and `2-3` short support items are usually enough.
- Adjust the title block width before shrinking the title font. The default should be a clear, readable title that does not spill past the colored panel.
- Do not place the cover image again inside the article body.
- Each article should include at least one internal visual motif that belongs to the topic itself rather than to a generic diagram template.
- Avoid diagrams that look like presentation slides with large text cards. Prefer lighter labels, physical relationships, and topic-native shapes when possible.

## SEO Rules

- Put the primary keyword in the title, slug, SEO title, and first paragraph.
- Prefer human-readable titles over aggressive keyword stuffing.
- Match common beginner search phrasing such as `what is`, `how does`, `guide`, `basics`, or `explained`.

## Research Rules

- Prefer primary sources first.
- If the topic is stable, use the clearest authoritative sources, not the most obscure ones.
- Avoid making numeric claims unless the source is clear and the number actually helps the reader.
- When multiple definitions exist, say that plainly instead of pretending one wording is universal.

## Reviewer Safety Checklist

Before finalizing, check that the draft is unlikely to fail on:

- shallow explanation
- low information density
- repetitive AI-like transitions
- weak decision value
- abrupt or underdeveloped ending

If any of these are present, revise before finalizing.
