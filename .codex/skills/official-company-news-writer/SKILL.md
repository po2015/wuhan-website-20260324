---
name: official-company-news-writer
description: Write reviewer-safe Cyrentis company news for `content/en/news/` when the goal is a formal corporate news item anchored to a specific event, date, and subject. Use for company milestones, exhibition participation, contract news, holiday messages, official notices, policy interpretations, and formal company statements that must survive strict news review.
---

# Official Company News Writer

Use this skill when the target output is a **real company news item**, not a blog post and not an industry commentary article.

If the task is mainly about an external industry event plus Cyrentis analysis, use [$industry-news-commentary](E:/Cyrentis/site/.codex/skills/industry-news-commentary/SKILL.md) instead.

This skill is designed to produce news that can pass [$news-reviewer](E:/Cyrentis/site/.codex/skills/news-reviewer/SKILL.md), which is aligned to [news-reviewer.md](E:/Cyrentis/site/docs/news-reviewer.md).

## Required References

Before drafting, read:

1. `references/news-pass-standard.md`
2. `references/frontmatter-template.md`
3. [news-reviewer.md](E:/Cyrentis/site/docs/news-reviewer.md)

## Non-Negotiable Rules

- The article must belong to **one primary news category**:
  - `holiday_greeting`
  - `policy_interpretation`
  - `company_statement`
  - `company_event`
  - `exhibition_news`
  - `milestone_update`
  - `official_notice`
  - `general_company_news`
- The article must clearly state:
  - when the event happened or is happening
  - what happened
  - who is involved
  - why it matters
- The article must keep **one main event**. Do not mix multiple unrelated updates into one page.
- The article must stay under `1000` words. Do not pad.
- The article must sound official, factual, concise, and publishable on a corporate News page.
- For company-originated news, the summary copy and body must use first-person corporate stance such as `we` and `our`, while staying formal and restrained.
- If you cannot identify a specific time reference, event reference, or subject actor, do not finalize the article as news.
- Do not invent:
  - customer names
  - partner names
  - event participation
  - certifications
  - policy effects
  - shipment facts
  - metrics or claims not provided by the user or supported by a source

## Workflow

1. Decide whether the topic is actually newsworthy.
   If the topic is timeless, generic, or mostly explanatory, stop and suggest a knowledge-base article instead.

2. Classify the article into one reviewer category before writing.

3. Collect the factual anchors:
   - exact date or time window
   - event or announcement name
   - main subject or actor
   - publication-worthy reason

4. Choose the word target by category:
   - `holiday_greeting`: `180-320`
   - `company_event`, `exhibition_news`, `milestone_update`, `official_notice`, `general_company_news`, `company_statement`: `280-700`
   - `policy_interpretation`: `450-900`
   Hard cap: `1000`

5. Draft the body in a news structure:
   - lead paragraph: what happened, when, who, why it matters
   - supporting paragraph(s): concrete details and relevant context
   - controlled close: next step, official position, or relevant Cyrentis context

6. Keep the body factual and restrained:
   - use first-person company voice for summary and body copy
   - avoid slogans
   - avoid AI filler
   - avoid scene-setting without substance
   - avoid sales-page phrasing
   - avoid broad timeless language that could fit any date
   - avoid repeatedly referring to Cyrentis in third person inside the body unless legal precision requires it

7. Use a lead image from Pexels via:
   `E:/Cyrentis/site/.codex/skills/industry-news-commentary/scripts/fetch_pexels_cover.py`
   and fill:
   - `image`
   - `image_alt`
   - `image_source_name`
   - `image_source_url`

8. Save to:
   `content/en/news/<slug>.md`

9. Review the finished draft with [$news-reviewer](E:/Cyrentis/site/.codex/skills/news-reviewer/SKILL.md).

10. If the reviewer returns:
   - `REQUIRE_REWRITE`: rewrite the article substantially
   - `REQUIRE_REVISION`: revise against the findings
   - `PASS`: finalize

11. Do not stop at a failed review. Revise or rewrite and review again until the article reaches `PASS`.

12. Rebuild when done:
   `conda run -n python314 hugo --cleanDestinationDir`

## Output Rules

- Destination: `content/en/news/<slug>.md`
- Keep the title concrete and news-like. Good patterns:
  - `Cyrentis Signs ...`
  - `Cyrentis Participates in ...`
  - `Cyrentis Issues ...`
  - `Cyrentis Shares ...`
  - `Cyrentis Announces ...`
- Use `1-2` broad categories and `2-4` specific tags.
- Add `3` concise `keypoints`.
- Write `description`, `seo_description`, `keypoints`, and the body in first-person company voice for company-originated news.
- Use exact dates when they materially anchor the event.
- For event, exhibition, or milestone news, the opening paragraph should usually contain the date.
- For policy interpretation, identify the issuing authority and the policy clearly.
- For holiday messages, keep the piece brief, official, and occasion-specific.
- Internal links are allowed only when they are directly relevant to the news item:
  - `/horizon/`
  - `/sensors/`
  - `/sensors/src/`
  - `/sensors/soc/`
  - `/sensors/sdc/`
  - `/services/`

## Hard Self-Check Before Review

Do not finalize the draft unless all of these are true:

- `specific_time_reference` is at least `adequate`
- `specific_event_reference` is at least `adequate`
- `clear_subject_actor` is at least `adequate`
- `clear_main_message` is at least `adequate`
- `publication_worthy_reason` is at least `adequate`
- the draft reads like official news rather than commentary or marketing
- the summary and body read in first-person company voice
- the body is under `1000` words
