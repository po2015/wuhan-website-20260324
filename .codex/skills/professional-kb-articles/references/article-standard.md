# Article Standard

## Goal

Produce long-form knowledge content that helps engineers, planners, buyers, and technically curious visitors understand a topic without reading like a brochure.

## Recommended Structure

1. Short introduction
2. Main technical explanation with `##` sections
3. One or more comparison, implications, or deployment sections
4. Optional "Where Cyrentis Fits" section only when genuinely useful
5. Short conclusion

## Research Standard

- Prefer primary sources
- Use secondary summaries only when they cite their own sources clearly
- For research papers, favor review papers, official labs, or highly cited foundational references when possible
- For regulations and export control, use the authoritative regulator or agency source

## Evidence Standard

- Separate facts from interpretation
- Do not collapse multiple source assumptions into one unqualified conclusion
- If a chart depends on a specific environment, date range, or test method, say so
- If evidence is incomplete, write the limitation directly instead of smoothing it over

## Writing Standard

- Avoid marketing adjectives such as `leading`, `best-in-class`, `revolutionary`, or `game-changing`
- Prefer concrete language over inflated summary
- Define specialized terms once, then use them consistently
- Keep paragraphs compact and decision-useful

## Internal Links

Use only when they help the reader continue a technical journey, for example:

- `/horizon/` for operator workflow, fusion, or command software
- `/sensors/src/` for radar selection or architecture
- `/sensors/soc/` for EO confirmation
- `/sensors/sdc/` for RF or spectrum topics
- `/services/security-solution-design/` when the topic is deployment architecture

## Charts and Tables

Use a chart only when:

- the data is public
- the source is linkable
- the time range is clear
- the units are clear
- the chart answers a real question in the article

If those conditions are not met, use:

- a comparison table
- a bullet comparison
- a clearly labeled explanatory diagram

## Image Standard

- Knowledge-base lead images must be unique across `content/en/knowledge-base/`
- Do not reuse the same stock photo, `image_source_url`, or generated cover asset for multiple knowledge-base articles unless the user explicitly approves reuse
- When using stock photography, check existing knowledge-base front matter first to avoid duplicate cover sources
- Keep descriptive alt text specific to the article instead of copying the same image wording between posts

## SEO Standard

- Put the main keyword in title, slug, SEO title, and intro
- Keep the title readable for humans first
- Use descriptive alt text
- Prefer filenames that mirror the article slug
