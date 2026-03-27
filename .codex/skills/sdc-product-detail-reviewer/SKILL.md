---
name: sdc-product-detail-reviewer
description: Review rendered SDC spectrum-detection product detail pages and return strict JSON using RF-detector-specific expectations for technical usefulness, workflow fit, and conversion quality. Use when evaluating pages under content/en/sensors/sdc, RF detail layouts, or any customer-facing page for spectrum monitoring, RF drone detection, Remote ID sensing, or pilot-location products.
---

# SDC Product Detail Reviewer

Use the shared workflow in [product-detail-reviewer](E:/Cyrentis/site/.codex/skills/product-detail-reviewer/SKILL.md), then apply the RF-detector-specific checks below before final scoring.

## Strong RF Detector Page Signals

- The hero makes it obvious that the product is an RF or spectrum detector rather than a generic security sensor.
- The page explains what the detector actually does:
signal discovery, protocol parsing, pilot positioning, Remote ID parsing, blacklist or whitelist logic, or emitter location.
- The page provides real RF-operational detail:
frequency range, direction finding or positioning accuracy, detection radius assumptions, simultaneous target capacity, and deployment envelope.
- The page shows how the detector fits into a larger workflow with radar, optics, intervention devices, or platform software.

## Penalize Hard

- Pages that sound like generic "anti-drone AI" pages with little RF language.
- Missing frequency range, positioning, or target-capacity detail.
- Deployment copy that ignores whether the detector is portable, fixed, mast-mounted, or integrated into a broader counter-UAS cell.
- No explanation of what the buyer is expected to do after an RF alert appears.

## RF-Specific Spec Expectations

Treat the page as weak or missing on specifications if most of these are absent:

- frequency range
- scan speed or signal-processing clue
- positioning or direction-finding accuracy
- target or pilot capacity
- power and physical envelope
- protocol or signal-analysis methods
- integration path into broader operations

## Fixing Guidance

If the user asks to improve a single SDC page, prefer page data and page-level layout changes before editing the shared SDC template.
