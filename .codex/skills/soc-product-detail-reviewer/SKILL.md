---
name: soc-product-detail-reviewer
description: Review rendered SOC electro-optical product detail pages and return strict JSON using optical-payload-specific expectations for sensor clarity, deployment fit, and buyer trust. Use when evaluating pages under content/en/sensors/soc, optical detail layouts, or any customer-facing page for EO/IR payloads, gimbals, PTZ systems, thermal cameras, or long-range observation products.
---

# SOC Product Detail Reviewer

Use the shared workflow in [product-detail-reviewer](E:/Cyrentis/site/.codex/skills/product-detail-reviewer/SKILL.md), then apply the optical-specific checks below before final scoring.

## Strong Optical Page Signals

- The hero states whether the product is daylight, thermal, dual-spectrum, cooled, uncooled, stabilized, or ranging-capable.
- The page separates optical channels or configurations clearly enough that the buyer can understand what changes by suffix or package.
- The page gives practical performance and deployment clues:
zoom, sensor resolution, stabilization, PTZ limits, range finder options, environment, weight, and mounting context.
- The page explains how the payload is used:
manual viewing, tracking, confirmation, vehicle mounting, rooftop watch, shipborne use, or radar cueing.

## Penalize Hard

- Pages that blur visible, thermal, and laser functions into generic marketing language.
- Missing explanation of what optional configurations actually change.
- Missing deployment envelope for a payload that clearly depends on platform type, stabilization, or environmental hardening.
- Vague "high-definition" or "long-range" language with little concrete optical detail.

## Optical-Specific Spec Expectations

Treat the page as weak or missing on specifications if most of these are absent:

- daylight channel description
- thermal channel description
- zoom or focal-length clues
- stabilization or PTZ motion detail
- range finder or illuminator options if claimed
- environmental or mounting envelope
- integration or cueing context

## Fixing Guidance

If the user asks to improve a single SOC page, prefer page data and page-level layout changes before editing the shared SOC template.
