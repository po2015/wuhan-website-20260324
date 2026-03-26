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
- Prefer `14-18px` body text and `18-28px` heading text.
- Keep each line short enough that it fits comfortably inside the target box.
- Avoid centered paragraphs inside narrow boxes; left-align body copy unless there is a strong reason not to.
- Do not let any text or shape touch the box edge.
- Keep all labels fully inside the `viewBox`.

## Geometry Rules

- Use a clear grid or column system before drawing shapes.
- Align cards, icons, and arrows to shared anchors.
- Use consistent corner radii, stroke widths, and spacing.
- Prefer fewer, larger shapes over many tiny decorative shapes.

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
