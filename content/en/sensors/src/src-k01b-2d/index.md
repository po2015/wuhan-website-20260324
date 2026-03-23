---
title: SRC-K01B-2D
description: Ku band FMCW surveillance radar for drone detection with up to 3 km instrumented
  range.
kicker: SRC Radar
layout: src-detail-sample
slug: src-k01b-2d
aliases:
- /complete-products/radar/src-k01b-2d/
series_label: SRC surveillance radar series
model: SRC-K01B-2D
band: Ku band
system_type: FMCW
architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
hero_image: /ref-image/SRC-K01B-2D.png
positioning_title: Configured for border surveillance and maritime surveillance.
hero_stats:
- icon: /images/icons/radar-target-drone.svg
  label: Small UAV
  value: 1.5 km
  note: 0.01 m² reference target
- icon: /images/icons/radar-target-vtol.svg
  label: Large UAV
  value: 3 km
  note: 1 m² fixed-wing reference target
- icon: /images/icons/radar-stat-range.svg
  label: Maximum Range
  value: 3 km
  note: Instrumented site-planning range
feature_cards:
- title: Track capacity
  text: High data rate and strong tracking capability.
- title: Low false-alarm behavior
  text: Low probability of false alarms.
- title: Detection accuracy
  text: Wide detection range with high accuracy.
coverage_table:
- label: Horizontal Coverage
  value: 360°
- label: Vertical Coverage
  value: 65°
- label: Coverage Area
  value: 28.3 km²
  note: Computed at maximum range
technical_snapshot:
- name: Operating Band
  value: Ku band
- name: Waveform
  value: FMCW
- name: Scan Architecture
  value: Mechanical Azimuth Scanning + Electronic Elevation Steering
- name: Target Domains
  value: Air, Maritime
- name: Primary Target Types
  value: Small UAV, Large UAV, Human, Vehicle, Vessel
- name: Reference Target
  value: Small UAV (0.01 m²)
- name: Small UAV Detection
  value: 1.5 km (0.01 m² reference target)
- name: Large UAV Detection
  value: 3 km (1 m² fixed-wing reference target)
- name: Nominal Class
  value: 1.5 km
- name: Instrumented Range
  value: 3 km
- name: Blind Zone
  value: 50 m
- name: Horizontal Coverage
  value: 360°
- name: Vertical Coverage
  value: 65°
- name: Coverage Area
  value: 28.3 km²
- name: Velocity Range
  value: 1 to 100 m/s
- name: Azimuth Accuracy
  value: 0.4°
- name: Elevation Accuracy
  value: 0.4°
- name: Rotation Speed
  value: 20 rpm
- name: Rotation Options
  value: 20 rpm / 30 rpm / 60 rpm
- name: TWS Capacity
  value: '100'
- name: Deployment Type
  value: Portable
- name: Dimensions
  value: 455 × 360 × 90 mm
- name: Weight
  value: 24 kg
- name: Enclosure Rating
  value: IP66 (main unit IP67)
- name: Operating Temperature
  value: -40 to 55 °C
- name: Power Input
  value: DC 18
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
  value: 'Yes'
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
  text: Suitable for border surveillance projects that need radar warning integrated
    into a broader security workflow.
- image: /images/sensors/deployment-port.svg
  title: Port and maritime watch
  alt: Line concept illustration of a port monitoring site
  text: Suitable for maritime surveillance projects that need radar warning integrated
    into a broader security workflow.
- image: /images/sensors/deployment-industrial.svg
  title: Critical site protection
  alt: Line concept illustration of an industrial monitoring site
  text: Suitable for key site protection projects that need radar warning integrated
    into a broader security workflow.
related_products:
- model: SRC-K03B-2D
  url: /sensors/src/src-k03b-2d/
  band: Ku band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 5 km
  description: Ku band FMCW surveillance radar for drone detection with up to 5 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-K02E-2G
  url: /sensors/src/src-k02e-2g/
  band: Ku band
  system_type: FMCW
  architecture_name: Four-Face AESA Array
  max_range: 10 km
  description: Ku band FMCW surveillance radar for ground surveillance with up to
    10 km instrumented range.
  relation: Adjacent SRC model for similar deployment planning.
- model: SRC-K04A-2G
  url: /sensors/src/src-k04a-2g/
  band: Ku band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 15 km
  description: Ku band FMCW surveillance radar for ground surveillance with up to
    15 km instrumented range.
  relation: Adjacent SRC model for similar deployment planning.
- model: SRC-X05B-2D
  url: /sensors/src/src-x05b-2d/
  band: X band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 10 km
  description: X band FMCW surveillance radar for drone detection with up to 10 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-X08B-2D
  url: /sensors/src/src-x08b-2d/
  band: X band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 20 km
  description: X band FMCW surveillance radar for drone detection with up to 20 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
---
SRC-K01B-2D Surveillance Radar is positioned for border surveillance, maritime surveillance, and key site protection projects where operators need Ku band FMCW sensing and a readable site-warning layer. The mechanical azimuth scanning + electronic elevation steering architecture supports structured deployment planning and downstream response coordination.

The SRC-K01B-2D moving target surveillance radar adopts azimuth mechanical scanning and elevation digital beam forming technology. It provides all-day, all-weather continuous detection and tracking of moving targets within the area, featuring high detection sensitivity, low false alarm rate, and high precision.

In coordinated deployments, the radar can feed Horizon Sense, Horizon Fusion, Horizon Track, and Horizon AI workflows and support downstream cueing, verification, and response across border surveillance, maritime surveillance, and key site protection.
