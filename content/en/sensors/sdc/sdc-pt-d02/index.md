---
title: SDC-PT-D02
description: "Portable AOA spectrum detector for drone detection, pilot positioning, and RF situation awareness across 30 MHz to 6000 MHz."
kicker: SDC Detail
layout: sdc-detail
slug: sdc-pt-d02
weight: 1
catalog_tag: "Portable AOA Detector"
series_label: SDC spectrum detection series
model: SDC-PT-D02
hero_image: /images/sdc/sdc-pt-d02-hero.png
hero_lead: "A portable spectrum detection node built for drone signal discovery, pilot positioning, and low-altitude RF awareness in layered security operations."
hero_chips:
  - 30 MHz to 6000 MHz
  - Drone and pilot positioning
  - Blacklist / whitelist workflow
hero_stats:
  - icon: /images/icons/sdc-stat-frequency.svg
    label: Frequency Range
    value: "30 MHz to 6000 MHz"
    note: Wideband drone and emitter monitoring
  - icon: /images/icons/sdc-stat-detection.svg
    label: Detection Radius
    value: "5 to 10 km"
    note: Standard field with 0.1 W drone transmission power
  - icon: /images/icons/sdc-stat-direction.svg
    label: Direction And Position
    value: "<=5 deg / <=10 m"
    note: AOA direction finding and pilot positioning
  - icon: /images/icons/sdc-stat-capacity.svg
    label: Target Capacity
    value: ">=30 drones / >=10 pilots"
    note: Simultaneous drone and operator tracking support
feature_cards:
  - icon: /images/icons/sdc-stat-direction.svg
    title: Pilot positioning and trajectory tracking
    text: The detector can display drone trajectory, frequency band, model, unique ID, altitude, speed, drone position, and pilot position in one operating picture.
  - icon: /images/icons/product-radar-cueing.svg
    title: Multi-device linkage
    text: Extended interfaces allow the RF detector to work alongside radar, GPS deception, interference, and other site-control devices.
  - icon: /images/icons/product-cueing-chain.svg
    title: Spectrum, RID, and O4 analysis
    text: Identification logic combines spectral features, positioning analysis including O4 parsing, and RID parsing for practical low-altitude awareness.
  - icon: /images/icons/product-environment-hardening.svg
    title: Lightweight field deployment
    text: The detector is light enough for single-person setup, with a straightforward interface and IP65 protection for flexible site use.
rf_snapshot:
  - name: Product Role
    value: "Portable AOA spectrum detector for drone detection and pilot positioning"
  - name: Frequency Range
    value: "30 MHz to 6000 MHz"
  - name: Scan Speed
    value: "20 GHz/s at 25 kHz resolution"
  - name: Identification Technology
    value: "Spectral features, positioning analysis, O4 parsing, and RID parsing"
  - name: Polarization
    value: "Vertical polarization"
  - name: Simultaneous Targets
    value: ">=30 aircraft, with simultaneous pilot positioning for >=10 operators"
  - name: Detection Performance
    value: "5 to 10 km in a standard field with 0.1 W drone transmit power"
  - name: Direction Finding
    value: "<=5 degrees RMS standard field"
  - name: Positioning Accuracy
    value: "<=10 m"
  - name: Power And Interface
    value: "<=100 W, 220V AC, network port"
  - name: Physical Envelope
    value: "450 mm x 450 mm x 380 mm, <=13 kg"
  - name: Protection
    value: "IP65"
operation_image: /images/sdc/sdc-pt-d02-console.png
operation_image_alt: "Operational scenario view from the D02 detector manual"
operation_text: "The platform is designed to show detected drones, pilot position, and trajectory information in a compact operational view so RF events can move quickly into investigation or response."
integration_text: "For Cyrentis deployments, the detector should not remain isolated as a stand-alone RF screen. Frequency activity, drone alerts, pilot positioning, and event state should be shared with the wider site workflow."
integration_modules:
  - icon: /images/horizon/module-sense.svg
    title: Horizon Sense
    text: Registers the RF node as part of the managed sensing layer with shared health and device status.
  - icon: /images/horizon/module-fusion.svg
    title: Horizon Fusion
    text: Combines RF detections with radar, optics, and other site signals to reduce operator uncertainty.
  - icon: /images/horizon/module-command.svg
    title: Horizon Command
    text: Pushes verified drone and pilot alerts into the site response workflow instead of leaving them inside an isolated console.
  - icon: /images/horizon/module-link.svg
    title: Horizon Link
    text: Helps the detector work with adjacent systems such as radar, GPS deception, and other external control devices.
deployment_cards:
  - title: Fixed critical-site perimeter
    text: Works as an RF awareness node around airports, industrial compounds, campuses, or protected government sites.
  - title: Temporary event and expeditionary deployment
    text: Single-person setup and moderate power demand make it suitable for short-notice or temporary security tasks.
  - title: Layered counter-UAS cell
    text: Strong fit when RF detection must be combined with radar, optics, or intervention equipment in a shared operating picture.
---
SDC-PT-D02 is positioned as a portable RF detection node for projects that need more than simple signal presence awareness. It is intended for teams that want drone detection, pilot positioning, trajectory tracking, and practical integration with layered counter-UAS workflows.

The product is suited to security teams that need a compact deployment form, practical pilot-location support, and a clearer RF picture that can be shared with radar, optics, and response systems.
