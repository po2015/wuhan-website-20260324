---
title: SRC-K04A-2G
description: Ku band FMCW surveillance radar for ground surveillance with up to 15
  km instrumented range.
kicker: SRC Radar
layout: src-detail-sample
slug: src-k04a-2g
aliases:
- /complete-products/radar/src-k04a-2g/
series_label: SRC surveillance radar series
model: SRC-K04A-2G
band: Ku band
system_type: FMCW
architecture_name: Electronic Azimuth Scanning
hero_image: /ref-image/SRC-K04A-2G.png
positioning_title: Configured for land border surveillance and maritime surveillance.
hero_stats:
- icon: /images/icons/radar-target-person.svg
  label: Human
  value: 4 km
  note: 0.5 m² reference target
- icon: /images/icons/radar-target-vehicle.svg
  label: Vehicle
  value: 5.7 km
  note: 2 m² reference target
- icon: /images/icons/radar-target-vessel.svg
  label: Vessel
  value: 8.5 km
  note: 10 m² reference target
- icon: /images/icons/radar-stat-range.svg
  label: Maximum Range
  value: 15 km
  note: Instrumented site-planning range
feature_cards:
- title: Low false-alarm behavior
  text: Low false alarm probability.
- title: Track capacity
  text: Excellent tracking performance under dense target conditions.
- title: Practical deployment
  text: High cost-effectiveness.
coverage_table:
- label: Horizontal Coverage
  value: 90°
- label: Vertical Coverage
  value: Not published
- label: Coverage Area
  value: 176.7 km²
  note: Computed at maximum range
technical_snapshot:
- name: Operating Band
  value: Ku band
- name: Waveform
  value: FMCW
- name: Scan Architecture
  value: Electronic Azimuth Scanning
- name: Target Domains
  value: Ground, Maritime
- name: Primary Target Types
  value: Human, Vehicle, Vessel
- name: Reference Target
  value: Human (0.5 m²)
- name: Human Detection
  value: 4 km (0.5 m² reference target)
- name: Vehicle Detection
  value: 5.7 km (2 m² reference target)
- name: Vessel Detection
  value: 8.5 km (10 m² reference target)
- name: Nominal Class
  value: 4 km
- name: Instrumented Range
  value: 15 km
- name: Horizontal Coverage
  value: 90°
- name: Coverage Area
  value: 176.7 km²
- name: Refresh Rate
  value: 0.25 s
- name: Velocity Range
  value: 0.4 to 60 m/s
- name: Azimuth Accuracy
  value: 0.3°
- name: TWS Capacity
  value: '100'
- name: Deployment Type
  value: Portable
- name: Dimensions
  value: 340 × 240 × 75 mm
- name: Weight
  value: 5 kg
- name: Enclosure Rating
  value: IP67
- name: Operating Temperature
  value: -40 to 55 °C
- name: Power Input
  value: DC 18~28V (with AC 220V to DC 24V adapter)
- name: Power Consumption
  value: 85 W
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
- model: SRC-K02E-2G
  url: /sensors/src/src-k02e-2g/
  band: Ku band
  system_type: FMCW
  architecture_name: Four-Face AESA Array
  max_range: 10 km
  description: Ku band FMCW surveillance radar for ground surveillance with up to
    10 km instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-X05A-2G
  url: /sensors/src/src-x05a-2g/
  band: X band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 20 km
  description: X band FMCW surveillance radar for ground surveillance with up to 20
    km instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-K01B-2D
  url: /sensors/src/src-k01b-2d/
  band: Ku band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 3 km
  description: Ku band FMCW surveillance radar for drone detection with up to 3 km
    instrumented range.
  relation: Adjacent SRC model for similar deployment planning.
- model: SRC-K03B-2D
  url: /sensors/src/src-k03b-2d/
  band: Ku band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 5 km
  description: Ku band FMCW surveillance radar for drone detection with up to 5 km
    instrumented range.
  relation: Adjacent SRC model for similar deployment planning.
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
SRC-K04A-2G Surveillance Radar is positioned for land border surveillance, maritime surveillance, and critical site protection projects where operators need Ku band FMCW sensing and a readable site-warning layer. The electronic azimuth scanning architecture supports structured deployment planning and downstream response coordination.

The SRC-K04A-2G moving target surveillance radar employs a Digital Beamforming (DBF) system, enabling continuous, all-day, all-weather detection and tracking of moving targets within its coverage area. It offers advantages such as high detection sensitivity, low false alarm rate, and excellent accuracy.

In coordinated deployments, the radar can feed Horizon Sense, Horizon Fusion, Horizon Track, and Horizon AI workflows and support downstream cueing, verification, and response across land border surveillance, maritime surveillance, and critical site protection.
