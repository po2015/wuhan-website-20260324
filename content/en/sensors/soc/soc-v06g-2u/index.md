---
title: SOC-V06G-2U
description: "Visible-light long-zoom laser surveillance optics for extended day-night watch across perimeter, waterfront, transport, and industrial monitoring sites."
kicker: SOC Detail
layout: soc-detail
slug: soc-v06g-2u
weight: 2
catalog_order: 15
series_label: SOC surveillance optics series
model: SOC-V06G-2U
hero_image: /images/soc/soc-v06g-2u-hero.png
hero_lead: "A visible-spectrum long-zoom and laser-assisted optical payload for sites that need readable day-night confirmation, continuous pan-tilt watch, and AI-supported scene monitoring without moving to a thermal-led platform."
hero_chips:
  - Visible long-zoom plus IR laser
  - 78x optical zoom
  - 360 degree continuous PTZ
hero_stats:
  - icon: /images/icons/radar-stat-range.svg
    label: Day Observation
    value: 5.5 km
    note: Long-range daylight monitoring reference from the source specification
  - icon: /images/icons/radar-stat-range.svg
    label: Night Observation
    value: 2.5 km
    note: IR laser assisted night-watch reference
  - icon: /images/icons/product-autotrack.svg
    label: AI Analytics
    value: Human, vehicle, vessel
    note: Edge analytics and alarm-linked target tracking are built in
  - icon: /images/icons/product-gimbal-precision.svg
    label: PTZ Motion
    value: 360 deg + 30 deg/s
    note: Heavy-duty split PTZ with continuous pan observation
positioning_title: "SOC-V06G-2U extends the SOC family with a visible-only long-zoom and laser-assisted platform for riverbanks, ports, transport corridors, industrial perimeters, and elevated urban watch positions."
feature_cards:
  - icon: /images/icons/product-gimbal-precision.svg
    title: 78x long-zoom daylight reach
    text: Uses an 11 to 860 mm visible lens and starlight CMOS imaging so the platform can hold readable distant scenes during daylight and twilight conditions.
  - icon: /images/icons/product-radar-cueing.svg
    title: Integrated laser night assistance
    text: The 15 W IR laser package extends night-watch usability where the project still wants a visible-light workflow instead of shifting to a thermal-first architecture.
  - icon: /images/icons/product-autotrack.svg
    title: Edge analytics and tracking
    text: Supports intrusion, tripwire, region-based analytics, human and vehicle classification, vessel recognition, smoke or fire recognition, and alarm-linked tracking.
  - icon: /images/icons/product-environment-hardening.svg
    title: Heavy-duty outdoor construction
    text: The split PTZ structure, aluminum housing, anti-corrosion coating, and IP66 sealing make the platform credible for exposed fixed-site deployment.
optical_channels:
  - title: Visible Channel
    rows:
      - name: Sensor
        value: Back-illuminated starlight CMOS
      - name: Low-Light Reference
        value: 0.0005 Lux color, 0.0001 Lux monochrome, 0 Lux with IR on
      - name: Lens
        value: 11 to 860 mm continuous zoom, 78x optical zoom
      - name: Digital Zoom
        value: 32x
      - name: Image Support
        value: WDR, defog, backlight compensation, strong-light suppression, 2D and 3D noise reduction, electronic stabilization
  - title: Laser Illumination
    rows:
      - name: Source
        value: 15 W, 810 nm IR laser
      - name: Beam Control
        value: 0.5 to 20 degrees DSS synchronized beam-angle control
      - name: Alignment
        value: Motorized alignment with 0.01 degree optical-axis self-lock
      - name: Night Role
        value: Long-range visible-scene enhancement with synchronized zoom matching
      - name: Safety Basis
        value: IEC60825 aligned laser-safety handling
technical_snapshot:
  - name: Observation Reference
    value: Day 5.5 km, night 2.5 km
  - name: PTZ Coverage
    value: Pan 360 degrees continuous, tilt -45 to +45 degrees
  - name: PTZ Speed
    value: Pan 0.01 to 30 degrees/s, tilt 0.01 to 15 degrees/s
  - name: Presets And Patrol
    value: 3000 presets, 16 patrol routes, up to 256 preset points per route
  - name: Analytics And Tracking
    value: Intrusion, tripwire, region entry and exit, loitering, people gathering, fast movement, object left or removed, human, vehicle, animal, vessel, smoke or fire recognition, and alarm-linked tracking
  - name: Networking
    value: RJ45 10/100 Base-T, HTTP, HTTPS, FTP, SMTP, DNS, NTP, RTSP, RTCP, RTP, TCP, UDP, ICMP, DHCP, ONVIF, GB28181, and SDK access
  - name: Power Supply
    value: DC24V
  - name: Power Consumption
    value: 180 W
  - name: Weight
    value: 45 kg
  - name: Environment
    value: IP66, -40 to +60 C, <=95 percent RH, 6000 V surge protection, 96-hour salt-mist resistance
integration_native_title: "The native long-zoom watch path for waterline, perimeter, and corridor observation."
integration_image: /images/soc/soc-d13g-2a-software.png
integration_image_alt: "Optical monitoring software view for long-zoom surveillance workflows"
integration_text: "SOC-V06G-2U is designed to stay readable across daylight and laser-assisted night watch, but its practical project value is higher when device health, alarm state, pan-tilt angle, and live stream context are shared with the surrounding site workflow instead of remaining in a stand-alone camera console."
integration_horizon_title: "How SOC-V06G-2U contributes to Horizon-led visual confirmation."
integration_horizon_text: "In Cyrentis projects, the visible long-zoom layer should serve as the confirmation and evidence tool for sites where radar, RF, or rules-based detection produces the first alert. Horizon should absorb the stream and event context so operators do not switch between disconnected device interfaces."
integration_modules:
  - icon: /images/horizon/module-sense.svg
    title: Horizon Sense
    text: Registers the camera, stream, and health state as part of the shared sensing layer.
  - icon: /images/horizon/module-track.svg
    title: Horizon Track
    text: Carries a first alert into readable visible follow-up and continued observation.
  - icon: /images/horizon/module-command.svg
    title: Horizon Command
    text: Connects long-zoom confirmation to response review, dispatch, and escalation.
  - icon: /images/horizon/module-link.svg
    title: Horizon Link
    text: Keeps the camera usable with adjacent radar, RF, and external control environments.
performance_notes:
  - title: Waterside deployment
    image: /images/soc/soc-v06g-2u-field.jpeg
    alt: Laser-assisted long-zoom camera installed above a waterside site
    text: The split heavy-duty PTZ architecture is better suited to fixed waterside or riverbank positions than to lightweight pole-only deployment.
  - title: Laser-assisted night reach
    image: /images/soc/soc-v06g-2u-night-vehicle.jpeg
    alt: Night vehicle scene captured with laser-assisted long-zoom monitoring
    text: The integrated IR laser package is the main reason to choose this model when the site still needs readable night scenes from a visible-light workflow.
  - title: Maritime and harbor observation
    image: /images/soc/soc-v06g-2u-maritime.png
    alt: Harbor and vessel scene observed through a long-zoom camera
    text: Ports, docks, marine ranching, and coastal infrastructure are strong fits where vessel observation and evidence capture matter more than thermal classification depth.
deployment_scenarios:
  - image: /images/soc/soc-v06g-2u-port.jpeg
    title: Port and coastal rooftop watch
    alt: Long-zoom laser camera installed at an elevated port-side site
    text: Fits elevated harbor, dock, and shoreline positions that need wide watch arcs and readable long focal daylight scenes.
  - image: /images/soc/soc-v06g-2u-field.jpeg
    title: River, reservoir, and embankment monitoring
    alt: Long-zoom laser camera deployed above a waterline monitoring site
    text: Strong fit for riverbanks, reservoirs, and waterway management where day-night visibility and continuous PTZ coverage matter.
  - image: /images/soc/soc-v06g-2u-rooftop.jpeg
    title: Rooftop and corridor security observation
    alt: Long-zoom laser camera installed on a rooftop mast
    text: Suitable for industrial perimeters, highways, rail corridors, and elevated urban observation points that need persistent long-range watch.
---
SOC-V06G-2U brings a visible-only and laser-assisted option into the Cyrentis SOC library. It sits between compact dual-spectrum heads and the heavier cooled line, giving projects a dedicated long-zoom day-night camera where thermal sensing is not the primary purchase driver.

For the public page, the emphasis stays on visible reach, laser night support, analytics, PTZ behavior, and fixed-site deployment fit. Lower-level maintenance routines, security-policy tables, and full patrol logic should remain in the Cyrentis datasheet.
