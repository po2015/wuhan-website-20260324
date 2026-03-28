---
title: SRC-X05D-1D
description: X band Pulse Doppler surveillance radar for drone detection with up to
  10 km instrumented range.
kicker: SRC Radar
layout: src-detail-sample
slug: src-x05d-1d
aliases:
- /complete-products/radar/src-x05d-1d/
series_label: SRC surveillance radar series
model: SRC-X05D-1D
band: X band
system_type: Pulse Doppler
architecture_name: Electronic Scanning with Mechanical Rotation
hero_image: /ref-image/SRC-X05D-1D.png
positioning_title: Configured for low-altitude surveillance and critical site protection.
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
  text: Pulse Doppler architecture for stable target detection and tracking in security
    surveillance scenarios.
- title: Operational advantage 02
  text: 360 degree azimuth coverage and 80 degree elevation coverage for wide-area
    surveillance.
- title: Continuous surveillance
  text: Designed for all-day, all-weather operation in complex environments.
coverage_table:
- label: Horizontal Coverage
  value: 360°
- label: Vertical Coverage
  value: 80°
- label: Coverage Area
  value: 314.2 km²
  note: Computed at maximum range
technical_snapshot:
- name: Operating Band
  value: X band
- name: Waveform
  value: Pulse Doppler
- name: Scan Architecture
  value: Electronic Scanning with Mechanical Rotation
- name: Target Domains
  value: Air
- name: Primary Target Types
  value: Small UAV, Large UAV
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
  value: 150 m
- name: Horizontal Coverage
  value: 360°
- name: Vertical Coverage
  value: 80°
- name: Coverage Area
  value: 314.2 km²
- name: Refresh Rate
  value: 3.2 s
- name: Velocity Range
  value: 1 to 100 m/s
- name: Range Accuracy
  value: 10 m
- name: Azimuth Accuracy
  value: 0.3°
- name: Elevation Accuracy
  value: 0.4°
- name: Rotation Speed
  value: 18.8 rpm
- name: Rotation Options
  value: 18.8 rpm
- name: TAS Capacity
  value: '6'
- name: Deployment Type
  value: Fixed
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
  value: Horizon Sense, Horizon Fusion, Horizon Track, Horizon Command
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
- icon: /images/horizon/module-command.svg
  title: Horizon Command
  text: Pushes alarms, live track state, and operator actions into one command workflow
    instead of disconnected device screens.
deployment_scenarios:
- image: /images/sensors/deployment/radar-deployment-industrial-complex-overview.jpg
  title: Low Altitude Surveillance
  alt: Aerial view of an industrial complex and process area
  text: Suitable for broad site airspace where operators need earlier low-altitude warning across approach lanes, rooflines, and working zones.
- image: /images/sensors/deployment/radar-deployment-industrial-complex-overview.jpg
  title: Critical site protection
  alt: Aerial view of an industrial complex and process area
  text: Suitable for protected compounds, industrial assets, and utility sites that need continuous low-altitude awareness tied to response workflow.
- image: /images/sensors/deployment/radar-deployment-airport-control-tower-apron-view.png
  title: Airport and low-altitude security
  alt: Airport control tower and terminal apron under open sky
  text: Suitable for airports and adjacent low-altitude corridors where early warning is needed across runway, apron, and perimeter airspace.
related_products:
- model: SRC-X05C-1D
  url: /sensors/src/src-x05c-1d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: 2D Electronic Scanning (Single-Face AESA)
  max_range: 10 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Same band and range class with an alternate scan architecture.
- model: SRC-X05E-1D
  url: /sensors/src/src-x05e-1d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: Four-Face AESA Array
  max_range: 10 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Same band and range class with an alternate scan architecture.
- model: SRC-X05E-3D
  url: /sensors/src/src-x05e-3d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: Four-Face AESA Array
  max_range: 10 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Comparable model in the same band and range class.
- model: SRC-K05C-1D
  url: /sensors/src/src-k05c-1d/
  band: Ku band
  system_type: Pulse Doppler
  architecture_name: 2D Electronic Scanning (Single-Face AESA)
  max_range: 10 km
  description: Ku band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-K05D-1D
  url: /sensors/src/src-k05d-1d/
  band: Ku band
  system_type: Pulse Doppler
  architecture_name: Electronic Scanning with Mechanical Rotation
  max_range: 10 km
  description: Ku band Pulse Doppler surveillance radar for drone detection with up
    to 10 km instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
---
SRC-X05D-1D Surveillance Radar is positioned for low-altitude surveillance, critical site protection, and counter-uas early warning projects where operators need X band Pulse Doppler sensing and a readable site-warning layer. The electronic scanning with mechanical rotation architecture supports structured deployment planning and downstream response coordination.

SRC-X05D-1D Surveillance Radar is a X band Pulse Doppler surveillance radar designed for drone detection. It uses electronic scanning with mechanical rotation for practical security monitoring and response workflows.

In coordinated deployments, the radar can feed Horizon Sense, Horizon Fusion, Horizon Track, and Horizon Command workflows and support downstream cueing, verification, and response across low-altitude surveillance, critical site protection, and counter-uas early warning.
