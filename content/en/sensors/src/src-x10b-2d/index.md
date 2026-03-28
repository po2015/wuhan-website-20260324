---
title: SRC-X10B-2D
description: X band FMCW surveillance radar for drone detection with up to 20 km instrumented
  range.
kicker: SRC Radar
layout: src-detail-sample
slug: src-x10b-2d
aliases:
- /complete-products/radar/src-x10b-2d/
series_label: SRC surveillance radar series
model: SRC-X10B-2D
band: X band
system_type: FMCW
architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
hero_image: /ref-image/SRC-X10B-2D.png
positioning_title: Configured for low-altitude surveillance and critical site protection.
hero_stats:
- icon: /images/icons/radar-target-drone.svg
  label: Small UAV
  value: 10 km
  note: 0.01 m² reference target
- icon: /images/icons/radar-target-vtol.svg
  label: Large UAV
  value: 18 km
  note: 1 m² fixed-wing reference target
- icon: /images/icons/radar-stat-range.svg
  label: Maximum Range
  value: 20 km
  note: Instrumented site-planning range
feature_cards:
- title: Wide Detection Range
  text: Capable of detecting small UAVs (RCS 0.01 m²) at distances up to 10 km, providing
    early warning and ample response time.
- title: Strong Tracking Capability
  text: By adopting advanced tracking filtering algorithms, it has significantly improved
    its target tracking performance.
- title: Effective Small Target Detection
  text: Utilizing a Frequency Modulated Continuous Wave (FMCW) system, it avoids the
    signal-to-noise ratio mutation issues caused by waveform handover in pulse radars,
    ensuring continuous detection of very small targets (such as the DJI Mini 3) at
    all elevation angles.
coverage_table:
- label: Horizontal Coverage
  value: 360°
- label: Vertical Coverage
  value: 65°
  note: -5 to 60 degrees
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
  value: Air
- name: Primary Target Types
  value: Small UAV, Large UAV
- name: Reference Target
  value: Small UAV (0.01 m²)
- name: Small UAV Detection
  value: 10 km (0.01 m² reference target)
- name: Large UAV Detection
  value: 18 km (1 m² fixed-wing reference target)
- name: Nominal Class
  value: 10 km
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
- name: Refresh Rate
  value: 2 s
- name: Velocity Range
  value: 1 to 150 m/s
- name: Range Accuracy
  value: 5 m
- name: Azimuth Accuracy
  value: 0.5°
- name: Elevation Accuracy
  value: 0.5°
- name: Rotation Speed
  value: 30 rpm
- name: Rotation Options
  value: 20 rpm / 30 rpm / 60 rpm
- name: TWS Capacity
  value: '500'
- name: Deployment Type
  value: Fixed
- name: Mounting Options
  value: Pole Mounted, Tower Mounted
- name: Weight
  value: 66 kg
- name: Enclosure Rating
  value: IP66
- name: Operating Temperature
  value: -40 to 55 °C
- name: Power Input
  value: DC 36-52V
- name: Data Interfaces
  value: Ethernet
- name: Protocol Support
  value: UDP
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
- image: /images/sensors/deployment/radar-deployment-container-port-terminal-overview.png
  title: Low Altitude Surveillance
  alt: Container terminal lanes and waterfront logistics estate
  text: Suitable for broad site airspace where operators need earlier low-altitude warning across approach lanes, rooflines, and working zones.
- image: /images/sensors/deployment/radar-deployment-refinery-perimeter-night-security.png
  title: Critical site protection
  alt: Fenced refinery perimeter under night security lighting
  text: Suitable for protected compounds, industrial assets, and utility sites that need continuous low-altitude awareness tied to response workflow.
- image: /images/sensors/deployment/radar-deployment-airport-control-tower-apron-view.png
  title: Airport and low-altitude security
  alt: Airport control tower and terminal apron under open sky
  text: Suitable for airports and adjacent low-altitude corridors where early warning is needed across runway, apron, and perimeter airspace.
related_products:
- model: SRC-X10A-2G
  url: /sensors/src/src-x10a-2g/
  band: X band
  system_type: FMCW
  architecture_name: Electronic Azimuth Scanning
  max_range: 30 km
  description: X band FMCW surveillance radar for ground surveillance with up to 30
    km instrumented range.
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
- model: SRC-X05B-2D
  url: /sensors/src/src-x05b-2d/
  band: X band
  system_type: FMCW
  architecture_name: Mechanical Azimuth Scanning + Electronic Elevation Steering
  max_range: 10 km
  description: X band FMCW surveillance radar for drone detection with up to 10 km
    instrumented range.
  relation: Comparable mission-focused model with a similar waveform approach.
- model: SRC-X10C-1D
  url: /sensors/src/src-x10c-1d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: 2D Electronic Scanning (Single-Face AESA)
  max_range: 15 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 15 km instrumented range.
  relation: Comparable model in the same band and range class.
- model: SRC-X10D-1D
  url: /sensors/src/src-x10d-1d/
  band: X band
  system_type: Pulse Doppler
  architecture_name: Electronic Scanning with Mechanical Rotation
  max_range: 15 km
  description: X band Pulse Doppler surveillance radar for drone detection with up
    to 15 km instrumented range.
  relation: Comparable model in the same band and range class.
compliance_notice:
  title: PRC dual-use export control notice
  text: This specification should be handled as an export-controlled civil-security
    radar under the PRC Dual-Use Export Control List. The public basis is Category
    6 Sensors and Lasers, item 6A108.a, issued under MOFCOM Announcement No. 51 of
    2024 and effective December 1, 2024. Cyrentis can assist eligible civil customers
    with export-license preparation and submission support.
  basis: 'Basis: PRC Dual-Use Export Control List, Category 6 Sensors and Lasers,
    item 6A108.a.'
  links:
  - label: MOFCOM Announcement No. 51 of 2024
    url: https://www.mofcom.gov.cn/zfxxgk/fdzdgknr/ztfl/dwmygl/art/2024/art_8300c93ceef047debcf4da0ced080629.html
---
SRC-X10B-2D Low-Altitude Surveillance Radar is positioned for low-altitude surveillance, critical site protection, and counter-uas early warning projects where operators need X band FMCW sensing and a readable site-warning layer. The mechanical azimuth scanning + electronic elevation steering architecture supports structured deployment planning and downstream response coordination.

The SRC-X10B-2D Low-Altitude Surveillance Radar is an intelligent detection 3D radar. It can rapidly detect and continuously track targets such as UAVs, aircraft, vehicles and birds.

In coordinated deployments, the radar can feed Horizon Sense, Horizon Fusion, Horizon Track, and Horizon AI workflows and support downstream cueing, verification, and response across low-altitude surveillance, critical site protection, and counter-uas early warning.
