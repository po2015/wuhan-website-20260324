# Icon Style Standard

This file defines the shared icon style for this project.

From this point forward, new icons in this repo should follow this standard unless the style guide is intentionally updated first.

## Style Name

Recommended internal name:

`Soft Enterprise Duotone SVG`

This is a clean enterprise software icon language for product pages, platform narratives, workflows, and capability explanations. It is not intended to look like an app-store icon set, a realistic illustration pack, or a decorative marketing sticker set.

## Core Characteristics

- Rounded square base tile
- Soft pastel duotone palette
- Geometric flat vector shapes
- Clear semantic metaphor
- Low visual noise
- Minimal detail
- Easy to maintain as SVG

## Recommended Canvas

- Use `88x88` or `104x104` artboards by default
- Prefer an outer tile starting near `x=8 y=8`
- Preferred tile size: about `88x88`
- Preferred corner radius: `rx=22` to `24`
- Keep the main shape inside a safe area
- Let the visual subject occupy about `55%` to `72%` of the usable area

## Construction Rules

- One icon should communicate one core idea
- Prefer one main symbol
- Add only `1-3` helper nodes, markers, or connectors when needed
- Prefer circles, rounded rectangles, straight lines, simple paths, and compact geometry
- Do not add text inside the SVG
- Avoid decorative elements that do not help meaning
- Avoid realistic perspective
- Avoid heavy visual layering

## Stroke Rules

- Main stroke: `2` or `2.5`
- Secondary stroke: usually `2`
- Use `round` line caps
- Use `round` line joins
- Do not mix too many stroke weights inside one icon

## Color System

Icons can vary by function category, but the structure and rendering logic should remain consistent.

### 1. Sensing / Spatial

- Tile fill: `#E7F9FF` or `#ECFBFF`
- Tile stroke: `#8DD7F7` or `#97E2F8`
- Primary: `#0EA5E9`
- Secondary: `#38BDF8`
- Deep line: `#0284C7`

### 2. Correlation / Intelligence

- Tile fill: `#F3EEFF` or `#F5F0FF`
- Tile stroke: `#D2C2FF` or `#D9CAFF`
- Primary: `#7C3AED`
- Secondary: `#8B5CF6`
- Deep line: `#6D28D9`

### 3. Command / Notification / Archive

- Tile fill: `#FFF6E7`
- Tile stroke: `#FFD48B`
- Primary: `#D97706`
- Secondary: `#F59E0B`
- Highlight: `#FBBF24`

### 4. Link / Integration

- Tile fill: `#ECFFF4`
- Tile stroke: `#A7F3C6`
- Primary: `#059669`
- Secondary: `#10B981`
- Highlight: `#34D399`

## Composition Patterns

Prefer these composition patterns:

- Central symbol plus helper nodes
- Central symbol plus directional path
- Container shape plus one action mark
- Multiple nodes converging into one center for orchestration or fusion
- A path or arrow chain for flow, tracking, or response

## Visual Tone

The icons should feel:

- Enterprise
- Platform-oriented
- Rational
- Clean
- Readable
- Stable

Avoid these directions:

- 3D skeuomorphic styling
- Heavy glow effects
- Game UI styling
- Excessive futuristic noise
- Mascot-like character design
- Overbuilt gradient stacks

## Layout and Usage

- Do not embed shadows inside the SVG unless there is a very strong reason
- If a shadow is needed, prefer a light CSS `drop-shadow`
- Keep the SVG scalable without changing the internal proportions
- Typical display size on the page: `80px` to `110px`
- Preserve enough whitespace around the icon
- Avoid wrapping the icon in a heavy dark container unless the page design explicitly requires it

## Naming Convention

Use lowercase kebab-case names:

- `module-sense.svg`
- `module-track.svg`
- `blueprint-respond.svg`
- `positioning-unified-view.svg`

Recommended semantic prefixes:

- `module-*`
- `blueprint-*`
- `positioning-*`
- `service-*`
- `product-*`

## Source of Truth

Current style references in this repo:

- `static/images/horizon/module-sense.svg`
- `static/images/horizon/module-spatial.svg`
- `static/images/horizon/module-fusion.svg`
- `static/images/horizon/module-track.svg`
- `static/images/horizon/module-ai.svg`
- `static/images/horizon/module-command.svg`
- `static/images/horizon/module-notify.svg`
- `static/images/horizon/module-archive.svg`
- `static/images/horizon/module-link.svg`
- `static/images/horizon/blueprint-sense.svg`
- `static/images/horizon/blueprint-understand.svg`
- `static/images/horizon/blueprint-respond.svg`
- `static/images/horizon/positioning-fragmented-ops.svg`
- `static/images/horizon/positioning-unified-view.svg`
- `static/images/horizon/positioning-workflow.svg`
- `static/images/horizon/positioning-decision-flow.svg`

New icons should match the balance, line weight, spacing, corner treatment, and color behavior found in those files.

## AI Prompt Reference

If AI is used to generate SVG drafts, start from a prompt like this:

```text
Clean enterprise software icon, rounded square tile background, soft pastel duotone palette, geometric flat vector, 2px to 2.5px strokes, minimal details, clear semantic metaphor, no realism, no 3D, no heavy shadow, SVG-friendly composition.
```

To keep it closer to the current repo style, add:

```text
Use a calm enterprise UI icon language with soft cyan, violet, amber, or emerald accents depending on function category. Keep one main symbol and one to three supporting nodes or connectors.
```

## Acceptance Checklist

Before finalizing a new icon, check:

- Is the core meaning readable at a glance?
- Does it still look like part of the same family?
- Is the spacing safe, with no edge collisions?
- Is there any decoration that does not help meaning?
- Are stroke weight, corner radius, and density consistent with the existing set?
- Does it work well in a product explanation block on the site?

## Project Rule

This file is the default icon standard for this project.

If the icon language needs to evolve later, update this file first, then apply the change across icon assets.
