---
title: SRC-X05B-2D
description: X band FMCW surveillance radar for drone detection with up to 10 km instrumented
  range.
kicker: SRC Radar
layout: src-detail-sample
slug: src-x05b-2d
aliases:
- /complete-products/radar/src-x05b-2d/
series_label: SRC surveillance radar series
model: SRC-X05B-2D
band: X band
system_type: FMCW
architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
hero_image: /ref-image/SRC-X05B-2D.png
positioning_title: Configured for border surveillance and maritime surveillance.
hero_stats:
- icon: /images/icons/radar-target-drone.svg
  label: Small UAV
  value: 5 km
  note: 0.01 m² reference target
- icon: /images/icons/radar-target-vtol.svg
  label: Large UAV
  value: 10 km
  note: 1 m² fixed-wing reference target
- icon: /images/icons/radar-stat-range.svg
  label: Maximum Range
  value: 10 km
  note: Instrumented site-planning range
feature_cards:
- title: Track capacity
  text: High data rate and strong tracking capability.
- title: Low false-alarm behavior
  text: Low false alarm probability.
- title: Range coverage
  text: Wide detection range and high precision.
coverage_table:
- label: Horizontal Coverage
  value: 360°
- label: Vertical Coverage
  value: 65°
- label: Coverage Area
  value: 314.2 km²
  note: Computed at maximum range
technical_snapshot:
- name: Operating Band
  value: X band
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
  value: 5 km (0.01 m² reference target)
- name: Large UAV Detection
  value: 10 km (1 m² fixed-wing reference target)
- name: Nominal Class
  value: 5 km
- name: Instrumented Range
  value: 10 km
- name: Blind Zone
  value: 50 m
- name: Horizontal Coverage
  value: 360°
- name: Vertical Coverage
  value: 65°
- name: Coverage Area
  value: 314.2 km²
- name: Velocity Range
  value: 1 to 150 m/s
- name: Azimuth Accuracy
  value: 0.4°
- name: Elevation Accuracy
  value: 0.4°
- name: Rotation Speed
  value: 20 rpm
- name: Rotation Options
  value: 20 rpm / 30 rpm / 60 rpm
- name: TWS Capacity
  value: '200'
- name: Deployment Type
  value: Portable
- name: Dimensions
  value: 505 × 600 × 105 mm
- name: Weight
  value: 30 kg
- name: Enclosure Rating
  value: IP66 (main unit IP67)
- name: Operating Temperature
  value: -40 to 55 °C
- name: Power Input
  value: DC 36
- name: Power Consumption
  value: 260 W
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
- model: SRC-X05A-2G
  url: /sensors/src/src-x05a-2g/
  band: X band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 20 km
  description: X band FMCW surveillance radar for ground surveillance with up to 20
    km instrumented range.
  relation: Comparable model in the same band and range class.
- model: SRC-X05E-3D
  url: /sensors/src/src-x05e-3d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: Four-Face AESA Array
  max_range: 10 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Comparable model in the same band and range class.
- model: SRC-X08B-2D
  url: /sensors/src/src-x08b-2d/
  band: X band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 20 km
  description: X band FMCW surveillance radar for drone detection with up to 20 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-X05C-1D
  url: /sensors/src/src-x05c-1d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: 2D Electronic Scanning (Single-Face AESA)
  max_range: 10 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Comparable model in the same band and range class.
- model: SRC-X05D-1D
  url: /sensors/src/src-x05d-1d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: Electronic Scanning with Mechanical Rotation
  max_range: 10 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Comparable model in the same band and range class.
---
SRC-X05B-2D Surveillance Radar is positioned for border surveillance, maritime surveillance, and key site protection projects where operators need X band FMCW sensing and a readable site-warning layer. The mechanical azimuth scanning + electronic elevation steering architecture supports structured deployment planning and downstream response coordination.

The SRC-X05B-2D moving target surveillance radar adopts azimuth mechanical scanning and elevation digital beamforming technology. It provides all-day, all-weather continuous detection and tracking of moving targets within the designated area, offering advantages such as high detection sensitivity, low false alarm rate, and high precision.

In coordinated deployments, the radar can feed Horizon Sense, Horizon Fusion, Horizon Track, and Horizon AI workflows and support downstream cueing, verification, and response across border surveillance, maritime surveillance, and key site protection.
