# SVG Diagram Rules

Use this file whenever the article needs a custom SVG diagram.

## Decision Rule

- Use hand-authored SVG for:
  - simple explainers
  - 3-6 boxes or stages
  - one small comparison table
  - one radar, one beam, one or two targets
- Prefer a layout tool or diagram DSL for:
  - dense process diagrams
  - many connectors
  - more than 6 labeled blocks
  - anything that depends on automatic routing or text flow

## Hard Gate

- If the figure is a workflow, comparison, service stack, architecture map, or any box-and-arrow explainer with sentence-length labels, use D2.
- If any label would naturally exceed one short phrase, use D2.
- If the figure needs more than one row of explanatory cards, use D2.
- If the diagram only looks correct because the author manually guessed text positions, it is the wrong tool choice.
- In D2, do not force a fixed height on text-heavy boxes unless you have already rendered and verified that every line stays inside the box.
- In D2, insert manual line breaks before rendering. Do not rely on one long sentence to fit inside a shape.
- Hand-authored SVG is for simple illustrations, not text-dense information graphics.
- Foundation cover exception: covers may intentionally reuse the same standardized `what-is-utm-u-space` / `what-is-remote-id` composition across the series.
- Foundation covers should stay hand-authored SVG by default. Use D2 for internal explanatory figures, not for the cover, unless the user explicitly asks for a different cover system.
- If a figure is starting to look like a slide full of cards, stop and redesign it around the topic's native geometry.

Good alternatives:

- `D2` for polished diagrams with automatic layout
- `Mermaid` for simple flowcharts and sequence diagrams
- `Graphviz` for graph-like layouts
- `Figma` or `Illustrator` when visual polish matters more than code generation

## Text Layout Rules

- Never place long text as one raw SVG line and hope it fits.
- Use `<text>` plus `<tspan>` for multi-line labels.
- Keep line count inside a box to `2-4` lines.
- Leave at least `16-24px` inner padding on all sides.
- Size the box around the text, not the other way around.
- For D2, the same rule applies: size the box around the text, not the text around a fixed-height box.
- Prefer `14-18px` body text and `18-28px` heading text.
- Keep each line short enough that it fits comfortably inside the target box.
- Avoid centered paragraphs inside narrow boxes; left-align body copy unless there is a strong reason not to.
- Do not let any text or shape touch the box edge.
- Keep all labels fully inside the `viewBox`.
- If you cannot keep text comfortably inside the box with short lines and padding, switch to D2 or split the figure.
- For standardized Foundation covers, keep the title fully inside the title block. If the title is shorter than roughly `80%` of the canvas width, keep it on one line and resize the block before forcing a wrap.

## Geometry Rules

- Use a clear grid or column system before drawing shapes.
- Align cards, icons, and arrows to shared anchors.
- Use consistent corner radii, stroke widths, and spacing.
- Prefer fewer, larger shapes over many tiny decorative shapes.
- Do not default every figure to stacked rounded rectangles. Use circles, rings, wavefronts, sectors, silhouettes, gradients, or axes when the topic naturally supports them.

## Radar Illustration Rules

- Do not draw a random sci-fi shape and call it radar.
- Base radar visuals on recognizable forms:
  - dish antenna
  - flat panel array
  - rotating bar antenna
  - range rings
  - scan sector
  - target blips or tracks
- Show beam direction and target relationship clearly.
- Use arcs, rings, sweep sectors, and echoes more than abstract splines.
- Keep the radar silhouette simple and believable.

## Robustness Rules

- Avoid `foreignObject` for main labels because browser support can vary.
- Prefer system-safe fonts already used by the site.
- Keep diagrams readable at both article width and reduced mobile width.
- If the figure feels crowded, split one figure into two smaller figures.

## Quality Check

Before finalizing, verify:

1. No text exceeds its box.
2. No text overlaps icons, arrows, or rings.
3. The radar or sensor shape is recognizable without reading the caption.
4. The figure still makes sense if viewed quickly.
5. The figure supports the article's explanation instead of merely decorating it.
6. The figure still reads correctly when scaled down to a narrow mobile viewport.
7. No label depends on a single very long line to stay readable.
8. Internal figures should not look interchangeable with the previous two Foundation articles unless they are part of an intentional standardized cover system.
