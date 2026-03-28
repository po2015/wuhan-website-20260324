---
title: SRC-C03A-1G
description: C-band pulse Doppler surveillance radar for short-range ground and waterside monitoring with up to 10 km instrumented range.
seo_title: SRC-C03A-1G Radar | C-Band Pulse Doppler Surveillance Radar
seo_description: Review the SRC-C03A-1G C-band pulse Doppler radar for 90 deg sector surveillance, short-range perimeter monitoring, and Horizon-based integration.
kicker: SRC Radar
layout: src-detail-sample
slug: src-c03a-1g
aliases:
  - /complete-products/radar/src-c03a-1g/
series_label: SRC surveillance radar series
model: SRC-C03A-1G
band: C band
system_type: Pulse Doppler
architecture_name: Electronic azimuth scanning
hero_image: /ref-image/SRC-C03A-1G.png
positioning_title: Portable C-band sector radar for short-range ground surveillance, waterside watch, and perimeter warning.
hero_summary_points:
  - 90 deg sector radar for short-range perimeter and corridor watch
  - Human, vehicle, and vessel detection in the 3 to 6.3 km class
  - 0.5 s refresh for moving-target follow-up
  - Portable form factor for fixed or relocatable deployment concepts
hero_stats:
  - icon: /images/icons/radar-target-person.svg
    label: Human
    value: 3 km
    note: 0.5 m^2 reference target
  - icon: /images/icons/radar-target-vehicle.svg
    label: Vehicle
    value: 4.2 km
    note: 2 m^2 reference target
  - icon: /images/icons/radar-target-vessel.svg
    label: Vessel
    value: 6.3 km
    note: 10 m^2 reference target
  - icon: /images/icons/radar-stat-range.svg
    label: Instrumented Range
    value: 10 km
    note: Site-planning envelope, not all-target guaranteed detection
feature_cards:
  - title: Short-range sector warning
    text: Designed for defined approach sectors, perimeter segments, and waterside lanes where a 90 deg search volume is more useful than a full rotating radar.
  - title: Fast revisit for moving targets
    text: A 0.5 second refresh cycle helps operators keep continuity on moving people, vehicles, and small craft in short-warning environments.
  - title: Portable deployment envelope
    text: The compact size, 45 W power draw, and Ethernet output make the unit easier to place in relocatable or infrastructure-light monitoring projects.
coverage_table:
  - label: Horizontal Coverage
    value: 90 deg
  - label: Vertical Coverage
    value: Not published
  - label: Coverage Area
    value: 78.5 km^2
    note: Computed at the 10 km instrumented envelope
fit_checks:
  - title: Best Fit
    text: Border sectors, utility perimeters, depot edges, and shoreline approaches where a defined corridor matters more than full 360 deg search.
  - title: Buyer Check
    text: Confirm whether the site really needs a 90 deg sector radar, what target class matters most, and whether optical or RF confirmation will sit on top of the alert layer.
  - title: Not Ideal For
    text: Buyers expecting a full rotating search radar, published air-surveillance style altitude coverage, or long-range drone-class stand-off without a broader layered design.
planning_notes:
  - title: Range context matters
    text: Treat the quoted distances as target-class references, not as one universal number. Human, vehicle, and vessel results differ because target size and reflection characteristics differ.
  - title: Sector geometry matters
    text: A 90 deg radar can be highly efficient when the monitored threat axis is known, but it should be placed carefully to avoid dead ground and wasted sector coverage.
  - title: Integration matters
    text: The unit is more valuable when its alerts are shared with optical confirmation, operator workflow, and adjacent sensors instead of left inside a device-only console.
technical_snapshot:
  - name: Operating Band
    value: C band
  - name: Waveform
    value: Pulse Doppler
  - name: Scan Architecture
    value: Electronic azimuth scanning
  - name: Target Domains
    value: Ground and near-shore waterside surveillance
  - name: Reference Targets
    value: Human 0.5 m^2, vehicle 2 m^2, vessel 10 m^2
  - name: Human Detection
    value: 3 km
  - name: Vehicle Detection
    value: 4.2 km
  - name: Vessel Detection
    value: 6.3 km
  - name: Instrumented Range
    value: 10 km
  - name: Horizontal Coverage
    value: 90 deg
  - name: Refresh Rate
    value: 0.5 s
  - name: Range Accuracy
    value: 8 m
  - name: Azimuth Accuracy
    value: 1 deg
  - name: Deployment Type
    value: Portable
  - name: Dimensions
    value: 436 x 290 x 61 mm
  - name: Weight
    value: 5.5 kg
  - name: Operating Temperature
    value: -40 to 55 C
  - name: Power Input
    value: AC 200 V
  - name: Power Consumption
    value: 45 W
  - name: Data Interface
    value: Ethernet
  - name: Protocol Support
    value: Not published
  - name: Horizon Compatible
    value: Yes
  - name: Third-Party Integration
    value: Yes
  - name: Multi-Sensor Fusion
    value: Yes
integration_modules:
  - icon: /images/horizon/module-sense.svg
    title: Horizon Sense
    text: Registers the radar as a managed sensor with device health, location, and shared asset context.
  - icon: /images/horizon/module-fusion.svg
    title: Horizon Fusion
    text: Correlates sector alerts with nearby optics, RF nodes, or adjacent radars so one device does not become an isolated alarm source.
  - icon: /images/horizon/module-track.svg
    title: Horizon Track
    text: Preserves trajectory continuity as a detected target crosses the monitored sector and moves toward a response boundary.
  - icon: /images/horizon/module-ai.svg
    title: Horizon AI
    text: Supports downstream prioritization when operators need faster sorting of ambiguous or repeated track behavior.
  - icon: /images/horizon/module-command.svg
    title: Horizon Command
    text: Pushes alerts, track history, and operator actions into one response workflow instead of disconnected local device screens.
deployment_scenarios:
  - image: /images/sensors/deployment-industrial.svg
    title: Border and corridor surveillance
    alt: Line concept illustration of a corridor surveillance sector
    text: Strong fit for ground corridors where operators want a defined warning sector covering likely movement routes rather than full circular search.
  - image: /images/sensors/deployment-industrial.svg
    title: Critical site perimeter
    alt: Line concept illustration of a protected industrial perimeter
    text: Useful around depots, substations, storage yards, and protected compounds that need a compact radar warning layer tied to response workflow.
  - image: /images/sensors/deployment-industrial.svg
    title: Waterside approach monitoring
    alt: Line concept illustration of a near-shore monitoring position
    text: Applicable to shoreline or harbor-edge watch when the buyer needs short-range awareness of small craft on a known approach axis.
related_products:
  - model: SRC-X03C-1D
    url: /sensors/src/src-x03c-1d/
    band: X band
    system_type: Pulse Doppler
    architecture_name: 2D electronic scanning single-face AESA
    max_range: 5 km
    description: X-band model for shorter-range drone-oriented deployments in a more compact class.
    relation: Compare when the project is centered on lower-range low-altitude targets rather than ground and waterside watch.
  - model: SRC-X03D-1D
    url: /sensors/src/src-x03d-1d/
    band: X band
    system_type: Pulse Doppler
    architecture_name: Electronic scanning with mechanical rotation
    max_range: 5 km
    description: Rotating X-band model for buyers who need broader search coverage in the low-altitude class.
    relation: Compare when wider search geometry matters more than this model's fixed-sector simplicity.
  - model: SRC-X03E-1D
    url: /sensors/src/src-x03e-1d/
    band: X band
    system_type: Pulse Doppler
    architecture_name: Four-face AESA array
    max_range: 5 km
    description: Four-face X-band architecture for persistent low-altitude coverage without mechanical rotation.
    relation: Compare when the deployment calls for continuous multi-face coverage rather than one 90 deg sector.
  - model: SRC-K05C-1D
    url: /sensors/src/src-k05c-1d/
    band: Ku band
    system_type: Pulse Doppler
    architecture_name: 2D electronic scanning single-face AESA
    max_range: 10 km
    description: Ku-band model in the 10 km class for buyers prioritizing low-altitude drone detection.
    relation: Compare when the mission shifts from general ground watch toward drone-specific low-altitude sensing.
  - model: SRC-K05D-1D
    url: /sensors/src/src-k05d-1d/
    band: Ku band
    system_type: Pulse Doppler
    architecture_name: Electronic scanning with mechanical rotation
    max_range: 10 km
    description: Ku-band rotating model for broader low-altitude search at the same 10 km class.
    relation: Compare when the site needs wider rotational coverage than a fixed C-band sector radar provides.
---
SRC-C03A-1G is a portable C-band pulse Doppler radar for short-range ground and waterside surveillance. It is best understood as a sector warning radar: a model for defined approach corridors, perimeter segments, and shoreline lanes where a fixed 90 degree search volume is operationally useful.

## What This Model Is Built For

This radar fits projects that need earlier warning over a known direction of approach rather than a full rotating search picture. That makes it relevant to border sectors, utility perimeters, depot edges, and selected waterside positions where operators already know which corridor, road, shoreline, or fence line matters most.

The published reference distances also make the product easier to place honestly. Human, vehicle, and vessel performance are not presented as one blended marketing number. Instead, the page shows how the instrumented envelope translates into different target classes, which is more useful for first-pass project screening.

## What Buyers Should Confirm Early

The first planning question is geometry. If the site needs full circular search, this model may not be the right fit. If the site needs a compact 90 degree warning sector tied to a response route, the design becomes much more credible. The second question is target priority. A buyer focused on perimeter movement, corridor traffic, or short-range waterside watch may value this model differently from a buyer focused on low-altitude drone search.

Buyers should also confirm how the radar will be validated in the field. Detection claims are most useful when linked to target class, sector placement, and site conditions. The page should therefore be read as an early planning tool, not as a substitute for deployment testing or a formal datasheet review.

## Integration Role in a Layered Site

SRC-C03A-1G becomes more valuable when it is part of a layered operating picture. In a practical deployment, the radar provides the first warning layer, while optical confirmation, incident rules, or adjacent sensors provide better interpretation and response support. That is why the integration path matters as much as the standalone detection number.

For teams already using a shared command workflow, the main value of this model is not that it produces more isolated alarms. It is that it gives a compact and power-light sector radar that can feed a wider monitoring and response architecture.
