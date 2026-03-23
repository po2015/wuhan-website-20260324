# SOC Product Rules

## 1. Product Line

The current public Cyrentis optics line includes the following base products:

- `SOC-D05G-1U` = short-range dual-spectrum surveillance optics
- `SOC-V06G-2U` = visible-light long-zoom laser surveillance optics
- `SOC-D13G-2A` = medium-range dual-spectrum surveillance optics
- `SOC-M13G-3U` = multi-band long-watch surveillance optics
- `SOC-D20G-2U` = long-range cooled surveillance optics

Public website messaging should present the SOC family as a focused but expandable catalog rather than as an open-ended dump of every source-manufacturer variant.

## 2. Naming Convention

Public product naming follows this structure:

`SOC-[Payload][ObservationClass][Stabilization]-[Generation][Mission]`

Examples:

- `SOC-D05G-1U`
- `SOC-V06G-2U`
- `SOC-D13G-2A`
- `SOC-M13G-3U`
- `SOC-D20G-2U`

### Payload Codes

- `D` = dual-spectrum EO + thermal payload
- `T` = thermal-only payload
- `V` = visible-only long-zoom payload
- `M` = multi-sensor payload with extended sensing or ranging functions

### Observation Class Codes

- Two digits representing the nominal observation class in kilometers
- `05` = short-range tier
- `06` = visible laser long-zoom tier
- `13` = medium-range tier
- `20` = long-range tier based on the current cooled series positioning

### Stabilization Codes

- `G` = gimbal-stabilized pan/tilt payload
- `F` = fixed observation head
- `M` = mast-mounted integrated unit
- `V` = vehicle-mounted mobile unit

### Generation Codes

- `1` = first-generation integrated optics
- `2` = second-generation networked and tracking-ready payload
- `3` = third-generation fused observation platform

### Mission Codes

- `A` = air surveillance and counter-UAS visual confirmation
- `P` = perimeter and critical-site security
- `M` = maritime or coastal observation
- `U` = multi-mission general surveillance

## 3. Configuration Suffix Convention

Delivered configurations keep the same public product name and use a suffix when a specific sensor package, lens set, or ranging option must be identified.

Configuration format:

`SOC-[Payload][ObservationClass][Stabilization]-[Generation][Mission]-[Suffix]`

Current public mappings:

- `SOC-D05G-1U-A` = short-range standard daylight package
- `SOC-D05G-1U-B` = short-range ranging package
- `SOC-D20G-2U-C` = long-range 52x daylight package
- `SOC-D20G-2U-CL` = long-range 60x daylight package

The website should present the base product model as the main page title and explain the active suffix or suffixes inside the detail page.

## 4. Current Source Mapping

The current public product library is derived from the available source material as follows:

- `source_material/soc/GD-280 Series Technical Specification(1).docx` -> `SOC-D05G-1U`
- `source_material/soc/new/HP-RC2186远距离高清激光摄像机V2.1.docx` -> `SOC-V06G-2U`
- `source_material/SOC.docX` -> `SOC-D13G-2A`
- `source_material/soc/new/HP-TTVC6516-2186多波段摄像机V1.1.docx` -> `SOC-M13G-3U`
- `source_material/soc/EOS-S520C Series v1.5.docx` -> `SOC-D20G-2U`

## 5. Canonical Hugo Routes

SOC product detail pages live under:

- `content/en/sensors/soc/soc-d05g-1u/index.md`
- `content/en/sensors/soc/soc-v06g-2u/index.md`
- `content/en/sensors/soc/soc-d13g-2a/index.md`
- `content/en/sensors/soc/soc-m13g-3u/index.md`
- `content/en/sensors/soc/soc-d20g-2u/index.md`

## 6. What To Show On The Web Page

SOC web pages should prioritize first-pass selection information:

- role of the payload in the monitoring workflow
- day and thermal sensing structure
- practical DRI or cueing ranges
- visible zoom class and thermal focal-length class
- laser range finder reach when equipped
- pan-tilt coverage, response speed, and positioning accuracy
- radar cueing, auto tracking, and software workflow value
- supported deployment forms such as fixed site, vehicle, and shipborne use
- how the payload can remain native or be integrated into Horizon

## 7. What To Keep In The Cyrentis Datasheet

These items are better kept in the product datasheet, proposal, or project package:

- full protocol matrices and network permutations
- every encoded output resolution and bitrate combination
- complete patrol-route and preset-count listings
- complete image-processing option lists
- account-policy, diagnostics, and alarm-matrix details
- low-level maintenance and lifecycle counters
- detailed servo or internal controller descriptions that do not affect first-pass selection

## 8. Public Page Principle

SOC pages should read like product-positioning pages for integrators and end users, not like raw source-manufacturer spec dumps.

The page should quickly answer:

- what distance class this product serves
- what sensing package it carries
- what the active configuration suffix means when options exist
- how it confirms or tracks targets
- where it can be deployed
- how it fits a radar-led or Horizon-led security workflow
