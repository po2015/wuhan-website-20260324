---
name: src-product-detail-reviewer
description: Review rendered SRC radar product detail pages and return strict JSON using radar-specific expectations for technical completeness, mission fit, and procurement credibility. Use when evaluating pages under content/en/sensors/src, radar detail layouts, or any customer-facing page for surveillance radar, drone-detection radar, perimeter radar, maritime radar, or low-altitude radar products.
---

# SRC Product Detail Reviewer

Use the shared workflow in [product-detail-reviewer](E:/Cyrentis/site/.codex/skills/product-detail-reviewer/SKILL.md), then apply the radar-specific checks below before final scoring.

## Strong Radar Page Signals

- The hero makes the product category obvious in one glance:
radar type, band, waveform or scan family, and primary mission.
- The page gives concrete detection context:
range, target class or reference target, sector coverage, scan/update behavior, and accuracy or refresh clues.
- The page explains where the radar fits operationally:
border, perimeter, coast, airport, base, or counter-UAS, instead of generic "wide coverage" copy.
- The page shows real deployment and integration credibility:
power, interface, environmental envelope, portable/fixed role, fusion or cueing context, and adjacent models.

## Penalize Hard

- Garbled units or mojibake such as broken degree, area, or temperature symbols.
- Vague claims like "wide coverage" or "strong target monitoring" without real numeric support nearby.
- Specs that omit what the range refers to.
If the page gives range numbers, it should also make target class or measurement context understandable.
- Hero copy that does not explain whether the product is for ground surveillance, drone detection, maritime watch, or another radar mission.
- Radar family pages that do not help the buyer understand why this model is distinct from adjacent models.

## Radar-Specific Spec Expectations

Treat the page as weak or missing on specifications if most of these are absent:

- band or frequency class
- waveform or scan architecture
- target domain or target classes
- detection range context
- coverage angle or sector
- refresh, update, or accuracy clues
- deployment type or physical envelope
- interface or integration path

## Fixing Guidance

If the user asks to improve a single SRC page:

1. Review the rendered page first.
2. Fix page data, copy, and page-specific template issues before touching shared SRC layouts.
3. Prefer a custom layout for that one page when the design or structure needs experimentation.
