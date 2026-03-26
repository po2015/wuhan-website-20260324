---
name: src-radar-detail-pages
description: Generate, refresh, and migrate Cyrentis SRC radar detail pages from `docs/SRC-*.yaml` into `content/en/sensors/src/model-slug/index.md`. Use when creating new SRC radar detail pages, batch-regenerating the catalog, finalizing the standard detail-page format, or moving site links away from `/complete-products/radar/` while keeping backward-compatible aliases.
---

# SRC Radar Detail Pages

Use this skill to maintain the YAML-driven SRC radar detail page system for this repo.

## Workflow

1. Read `references/page-standard.md` before changing the detail-page structure, field mapping, route rules, or compliance behavior.
2. Keep the canonical detail route at `content/en/sensors/src/<slug>/index.md`.
3. Keep the old detail route only as an alias: `/complete-products/radar/<slug>/`.
4. Use `conda run -n python314 python .codex/skills/src-radar-detail-pages/scripts/generate_src_radar_detail_pages.py --all` to regenerate all SRC detail pages.
5. Use `conda run -n python314 python .codex/skills/src-radar-detail-pages/scripts/generate_src_radar_detail_pages.py --model SRC-X10B-2D` to regenerate one model.
6. Use `--remove-legacy-sources` when migrating away from the old `content/en/complete-products/radar/src-*/` source pages.
7. Keep `content/en/sensors/src/_index.md` as the canonical list page and do not reintroduce `radar_source_prefix`.
8. Show `compliance_notice` only when the YAML contains `export_compliance`.
9. Rebuild with `conda run -n python314 hugo --cleanDestinationDir` after generation.

## Template Targets

- Detail template: `layouts/_default/src-detail-sample.html`
- Detail styles: `static/css/site.css`
- Detail content root: `content/en/sensors/src/`
- Source YAML: `docs/SRC-*.yaml`

## Validation

After generation or template edits:

1. Rebuild the site.
2. Open `public/sensors/src/index.html` and confirm card links point to `/sensors/src/<slug>/`.
3. Search the generated site for legacy direct detail links:
   `rg "/complete-products/radar/src-" public`
4. Confirm compliance blocks appear only on models whose YAML contains `export_compliance`.

## Resources

### scripts/

- `generate_src_radar_detail_pages.py`: Generate or refresh SRC detail pages from YAML.

### references/

- `page-standard.md`: Route rules, field mapping, conditional sections, and content-generation conventions.
