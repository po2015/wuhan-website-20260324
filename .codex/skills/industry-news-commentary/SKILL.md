---
name: industry-news-commentary
description: Create Cyrentis news commentary articles for `content/en/news/` when the task is to turn a current industry event, regulation, procurement, technology launch, or security incident into an SEO-friendly Cyrentis viewpoint article. Use for sourced news analysis that explains why the event matters to security, low-altitude awareness, Horizon, sensor products, or integration services.
---

# Industry News Commentary

Use this skill when drafting a news post that starts from an external event and ends with a measured Cyrentis point of view.

## Workflow

1. Start from `content/en/news/template.md`.
2. Read `references/news-standard.md` and `references/taxonomy-guidance.md` before drafting.
3. Search for the original event source first. Use one authoritative source as the anchor for the body. Collect additional relevant sources for the closing reference list.
4. Establish the event timeline for your own accuracy, but do not make relative-time wording part of the published article unless it is strictly necessary.
5. Write the article in this order:
   - what happened
   - why it matters to security or sensing
   - what it may mean for Cyrentis and its product or service positioning
   - what opportunities, risks, or design implications follow
   - a short closing view
6. Keep the body clean. Use at most one external source inside the main body. Put the broader source set in a short `Reference Reading` section at the end.
7. Add internal links only when the event clearly connects to existing Cyrentis pages.
8. Use `scripts/fetch_pexels_cover.py` for the cover image and include `image_source_name` and `image_source_url`.
9. Rebuild with `conda run -n python314 hugo --cleanDestinationDir` when done.

## Output Rules

- Default destination: `content/en/news/<slug>.md`
- Tone: timely, analytical, and brand-aware, but not hype-driven
- The article may contain a Cyrentis viewpoint, but it must stay anchored to the event
- Write for archive durability:
  - avoid `recent`, `recently`, `today`, `this week`, `currently`, and similar relative phrasing
  - avoid date-heavy narration in the body unless the exact date is material to the meaning
  - do not make the title depend on temporary wording such as `latest` or `recent`
- Do not invent:
  - partnerships
  - customer names
  - procurement wins
  - product capabilities
  - policy impacts that are not evidenced
- Avoid generic commentary. The article should explicitly connect the event to:
  - site security
  - low-altitude monitoring
  - operator workflow
  - system integration
  - deployment demand

## Link Rules

- Main body: use at most one authoritative external link
- `Reference Reading`: list the primary source first, then add other relevant external links when they help readers go deeper
- End-of-article references may include multiple external links as long as they are useful and not repetitive
- Internal links: use only when the event naturally connects to:
  - `/horizon/`
  - `/sensors/src/`
  - `/sensors/soc/`
  - `/sensors/sdc/`
  - `/services/`
  - a relevant knowledge-base article

## Image Rules

- One lead image is enough for most news posts
- Use real images, not abstract SVG placeholders
- Keep filenames slug-based and SEO-friendly
- Keep size lightweight; the current site standard is `960x540`
- Always add source metadata for stock images

## Resources

- `references/news-standard.md`: event selection, article structure, and commentary rules
- `references/taxonomy-guidance.md`: practical category and tag guidance for news posts
- `scripts/fetch_pexels_cover.py`: generic Pexels downloader and `960x540` cover resizer
