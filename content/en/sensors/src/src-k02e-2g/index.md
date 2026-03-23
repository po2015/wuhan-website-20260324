---
title: SRC-K02E-2G
description: Ku band FMCW surveillance radar for ground surveillance with up to 10
  km instrumented range.
kicker: SRC Radar
layout: src-detail-sample
slug: src-k02e-2g
aliases:
- /complete-products/radar/src-k02e-2g/
series_label: SRC surveillance radar series
model: SRC-K02E-2G
band: Ku band
system_type: FMCW
architecture_name: Four-Face AESA Array
hero_image: /ref-image/SRC-K02E-2G.png
positioning_title: Configured for land border surveillance and maritime surveillance.
hero_stats:
- icon: /images/icons/radar-target-person.svg
  label: Human
  value: 2 km
  note: 0.5 m² reference target
- icon: /images/icons/radar-target-vehicle.svg
  label: Vehicle
  value: 2.8 km
  note: 2 m² reference target
- icon: /images/icons/radar-target-vessel.svg
  label: Vessel
  value: 4.2 km
  note: 10 m² reference target
- icon: /images/icons/radar-stat-range.svg
  label: Maximum Range
  value: 10 km
  note: Instrumented site-planning range
feature_cards:
- title: Track capacity
  text: Accurate detection and stable tracking.
- title: Low false-alarm behavior
  text: Low false alarm rate.
- title: Track capacity
  text: Strong multi-target tracking capability.
coverage_table:
- label: Horizontal Coverage
  value: 360°
- label: Vertical Coverage
  value: Not published
- label: Coverage Area
  value: 314.2 km²
  note: Computed at maximum range
technical_snapshot:
- name: Operating Band
  value: Ku band
- name: Waveform
  value: FMCW
- name: Scan Architecture
  value: Four-Face AESA Array
- name: Target Domains
  value: Ground, Maritime
- name: Primary Target Types
  value: Human, Vehicle, Vessel
- name: Reference Target
  value: Human (0.5 m²)
- name: Human Detection
  value: 2 km (0.5 m² reference target)
- name: Vehicle Detection
  value: 2.8 km (2 m² reference target)
- name: Vessel Detection
  value: 4.2 km (10 m² reference target)
- name: Nominal Class
  value: 2 km
- name: Instrumented Range
  value: 10 km
- name: Horizontal Coverage
  value: 360°
- name: Coverage Area
  value: 314.2 km²
- name: Refresh Rate
  value: 0.25 s
- name: Velocity Range
  value: 0.4 to 60 m/s
- name: Azimuth Accuracy
  value: 0.4°
- name: TWS Capacity
  value: '400'
- name: Deployment Type
  value: Portable
- name: Dimensions
  value: 340 × 320 × 350 mm
- name: Weight
  value: 14 kg
- name: Enclosure Rating
  value: IP67
- name: Operating Temperature
  value: -40 to 55 °C
- name: Power Input
  value: DC 18~28V (with AC 220V to DC 24V adapter)
- name: Power Consumption
  value: 120 W
- name: Data Interfaces
  value: Ethernet
- name: Protocol Support
  value: Ethernet
- name: Horizon Compatible
  value: 'Yes'
- name: Third-Party Integration
  value: 'Yes'
- name: Cueing To Optics
  value: 'No'
- name: Multi-Sensor Fusion
  value: 'Yes'
- name: Compatible Platforms
  value: Cyrentis Horizon
- name: Supported Horizon Modules
  value: Horizon Sense, Horizon Fusion, Horizon Track, Horizon AI, Horizon Command
integration_modules:
- icon: /images/horizon/module-sense.svg
  title: Horizon Sense
  text: Registers the radar as a managed sensing asset with shared device, health,
    and status context.
- icon: /images/horizon/module-fusion.svg
  title: Horizon Fusion
  text: Correlates radar detections with adjacent sensing layers so alarms do not
    remain isolated inside one subsystem.
- icon: /images/horizon/module-track.svg
  title: Horizon Track
  text: Maintains trajectory continuity and target history as detections move through
    the monitored scene.
- icon: /images/horizon/module-ai.svg
  title: Horizon AI
  text: Supports downstream recognition and prioritization when operators need faster
    interpretation of ambiguous tracks.
- icon: /images/horizon/module-command.svg
  title: Horizon Command
  text: Pushes alarms, live track state, and operator actions into one command workflow
    instead of disconnected device screens.
deployment_scenarios:
- image: /images/sensors/deployment-industrial.svg
  title: Border and perimeter zones
  alt: Line concept illustration of an industrial monitoring site
  text: Suitable for land border surveillance projects that need radar warning integrated
    into a broader security workflow.
- image: /images/sensors/deployment-port.svg
  title: Port and maritime watch
  alt: Line concept illustration of a port monitoring site
  text: Suitable for maritime surveillance projects that need radar warning integrated
    into a broader security workflow.
- image: /images/sensors/deployment-industrial.svg
  title: Critical site protection
  alt: Line concept illustration of an industrial monitoring site
  text: Suitable for critical site protection projects that need radar warning integrated
    into a broader security workflow.
related_products:
- model: SRC-K04A-2G
  url: /sensors/src/src-k04a-2g/
  band: Ku band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 15 km
  description: Ku band FMCW surveillance radar for ground surveillance with up to
    15 km instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-K03B-2D
  url: /sensors/src/src-k03b-2d/
  band: Ku band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 5 km
  description: Ku band FMCW surveillance radar for drone detection with up to 5 km
    instrumented range.
  relation: Adjacent SRC model for similar deployment planning.
- model: SRC-K01B-2D
  url: /sensors/src/src-k01b-2d/
  band: Ku band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 3 km
  description: Ku band FMCW surveillance radar for drone detection with up to 3 km
    instrumented range.
  relation: Adjacent SRC model for similar deployment planning.
- model: SRC-X05A-2G
  url: /sensors/src/src-x05a-2g/
  band: X band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 20 km
  description: X band FMCW surveillance radar for ground surveillance with up to 20
    km instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-X10A-2G
  url: /sensors/src/src-x10a-2g/
  band: X band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 30 km
  description: X band FMCW surveillance radar for ground surveillance with up to 30
    km instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
---
SRC-K02E-2G moving target surveillance radar is positioned for land border surveillance, maritime surveillance, and critical site protection projects where operators need Ku band FMCW sensing and a readable site-warning layer. The four-face aesa array architecture supports structured deployment planning and downstream response coordination.

The SRC-K02E-2G moving target surveillance radar is specifically designed for the detection and real-time tracking of moving targets on the ground and water surfaces. It serves as an all-weather, day-and-night efficient surveillance system, capable of stable operation even in complex environments and harsh weather conditions.

In coordinated deployments, the radar can feed Horizon Sense, Horizon Fusion, Horizon Track, and Horizon AI workflows and support downstream cueing, verification, and response across land border surveillance, maritime surveillance, and critical site protection.
