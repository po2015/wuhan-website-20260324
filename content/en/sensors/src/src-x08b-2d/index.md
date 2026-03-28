---
title: SRC-X08B-2D
description: X band FMCW surveillance radar for drone detection with up to 20 km instrumented
  range.
kicker: SRC Radar
layout: src-detail-sample
slug: src-x08b-2d
aliases:
- /complete-products/radar/src-x08b-2d/
series_label: SRC surveillance radar series
model: SRC-X08B-2D
band: X band
system_type: FMCW
architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
hero_image: /ref-image/SRC-X08B-2D.png
positioning_title: Configured for border surveillance and maritime surveillance.
hero_stats:
- icon: /images/icons/radar-target-drone.svg
  label: Small UAV
  value: 8 km
  note: 0.01 m² reference target
- icon: /images/icons/radar-target-vtol.svg
  label: Large UAV
  value: 20 km
  note: 1 m² fixed-wing reference target
- icon: /images/icons/radar-stat-range.svg
  label: Maximum Range
  value: 20 km
  note: Instrumented site-planning range
feature_cards:
- title: Track capacity
  text: High data rate and strong tracking capability.
- title: Low false-alarm behavior
  text: Low false alarm probability.
- title: Detection accuracy
  text: Wide detection range and high accuracy.
coverage_table:
- label: Horizontal Coverage
  value: 360°
- label: Vertical Coverage
  value: 65°
- label: Coverage Area
  value: 1,256.6 km²
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
  value: 8 km (0.01 m² reference target)
- name: Large UAV Detection
  value: 20 km (1 m² fixed-wing reference target)
- name: Nominal Class
  value: 8 km
- name: Instrumented Range
  value: 20 km
- name: Blind Zone
  value: 50 m
- name: Horizontal Coverage
  value: 360°
- name: Vertical Coverage
  value: 65°
- name: Coverage Area
  value: 1,256.6 km²
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
  value: '300'
- name: Deployment Type
  value: Portable
- name: Dimensions
  value: 655 × 680 × 115 mm
- name: Weight
  value: 40 kg
- name: Enclosure Rating
  value: IP66 (main unit IP67)
- name: Operating Temperature
  value: -40 to 55 °C
- name: Power Input
  value: DC 36
- name: Power Consumption
  value: 330 W
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
- image: /images/sensors/deployment/radar-deployment-fenced-perimeter-guard-corridor.png
  title: Border and perimeter zones
  alt: Fenced perimeter corridor with guard post and drainage berm
  text: Suitable for land borders, fenced perimeters, and open approach sectors where operators need earlier warning before a target reaches the protected line.
- image: /images/sensors/deployment/radar-deployment-harbor-terminal-access-corridor.png
  title: Port and maritime watch
  alt: Harbor terminal access roads and waterfront logistics apron
  text: Suitable for ports, shorelines, and mixed land-water approach lanes where low-altitude traffic must be tracked across the waterfront.
- image: /images/sensors/deployment/radar-deployment-refinery-perimeter-night-security.png
  title: Critical site protection
  alt: Fenced refinery perimeter under night security lighting
  text: Suitable for plants, substations, storage areas, and other protected compounds that need persistent low-altitude awareness around critical infrastructure.
related_products:
- model: SRC-X10B-2D
  url: /sensors/src/src-x10b-2d/
  band: X band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 20 km
  description: X band FMCW surveillance radar for drone detection with up to 20 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-X05B-2D
  url: /sensors/src/src-x05b-2d/
  band: X band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 10 km
  description: X band FMCW surveillance radar for drone detection with up to 10 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-X08E-3D
  url: /sensors/src/src-x08e-3d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: Four-Face AESA Array
  max_range: 10 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Comparable model in the same band and range class.
- model: SRC-X05A-2G
  url: /sensors/src/src-x05a-2g/
  band: X band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 20 km
  description: X band FMCW surveillance radar for ground surveillance with up to 20
    km instrumented range.
  relation: Adjacent SRC model for similar deployment planning.
- model: SRC-K01B-2D
  url: /sensors/src/src-k01b-2d/
  band: Ku band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 3 km
  description: Ku band FMCW surveillance radar for drone detection with up to 3 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
---
SRC-X08B-2D Surveillance Radar is positioned for border surveillance, maritime surveillance, and critical site protection projects where operators need X band FMCW sensing and a readable site-warning layer. The mechanical azimuth scanning + electronic elevation steering architecture supports structured deployment planning and downstream response coordination.

The SRC-X08B-2D moving target surveillance radar utilizes an azimuth mechanical scanning and elevation digital beamforming system. It enables continuous, all-day, all-weather detection and tracking of moving targets within the designated area, offering advantages such as high detection sensitivity, low false alarm rate, and high accuracy.

In coordinated deployments, the radar can feed Horizon Sense, Horizon Fusion, Horizon Track, and Horizon AI workflows and support downstream cueing, verification, and response across border surveillance, maritime surveillance, and critical site protection.
