# SRC Radar Detail Page Standard

## Canonical Routes

- Canonical detail route: `/sensors/src/<slug>/`
- Legacy detail route: `/complete-products/radar/<slug>/`
- Implement the legacy route as an alias on the canonical page.
- Do not keep live source pages under `content/en/complete-products/radar/src-*/`.

## Source And Output

- Source of truth: `docs/SRC-*.yaml`
- Generated output: `content/en/sensors/src/<slug>/index.md`
- Canonical list page: `content/en/sensors/src/_index.md`

## Front Matter Contract

Generated pages should provide these keys:

- `title`
- `description`
- `kicker`
- `layout`
- `slug`
- `aliases`
- `series_label`
- `model`
- `band`
- `system_type`
- `architecture_name`
- `hero_image`
- `positioning_title`
- `hero_stats`
- `feature_cards`
- `coverage_table`
- `technical_snapshot`
- `integration_modules`
- `deployment_scenarios`
- `related_products`
- `compliance_notice` only when `export_compliance` exists

## Section Order

Keep the page flow in this order:

1. Hero
2. Compliance alert, conditional
3. Stat cards
4. Operational Position
5. Feature grid
6. Detection Envelope
7. Technical Snapshot
8. Integration Narrative
9. Deployment Fit
10. Related Products

## Content Rules

- Use `SRC surveillance radar series` as the series label.
- Use the model code as the page title.
- Keep the hero lead concise. Put broader explanation into the Markdown body.
- Build hero stats from actual target-distance fields in YAML when available.
- Include `Maximum Range` from `coverage.instrumented_range_km` or `detection.nominal_class_km`.
- Include `TWS` and `TAS` cards only when the values are real, not null and not `N/A`.
- Build feature cards from `content.key_features`, using heuristic titles when the YAML does not provide one.
- Build deployment scenarios from YAML use cases and map them to the existing real scenario images.
- Build related products from the wider SRC catalog.
- Prefer models in the same band, detection class, generation, and mission group.
- Group architecture variants together when the main difference is scan mode, such as `C / D / E`.
- Cap the related-products list at five items.

## Compliance Rule

- Show compliance only when the YAML contains `export_compliance`.
- Do not render a compliance section for normal civil models without that block.
- Use the public PRC dual-use wording and the MOFCOM public link already used in the finalized X10B page.

## Template Notes

- The current finalized detail template is `layouts/_default/src-detail-sample.html`.
- The current finalized styles live in `static/css/site.css`.
- Internal class names may still include `src-sample-*`; treat that as implementation detail, not user-facing copy.

## List Page Rule

- The `sensors/src/` list page should source its cards from child detail pages under the same section.
- Do not rely on `radar_source_prefix` after migration.
