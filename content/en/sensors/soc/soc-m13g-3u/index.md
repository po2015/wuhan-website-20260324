---
title: SOC-M13G-3U
description: "Multi-band visible and thermal surveillance optics with fire-aware analytics, radar-linked tracking, and optional laser or positioning expansion for extended site monitoring."
kicker: SOC Detail
layout: soc-detail
slug: soc-m13g-3u
weight: 3
catalog_order: 25
series_label: SOC surveillance optics series
model: SOC-M13G-3U
hero_image: /images/soc/soc-m13g-3u-hero.png
hero_lead: "A multi-band uncooled visible and thermal observation platform for long-watch monitoring, fire prevention, perimeter security, and radar-led confirmation across wide outdoor sites."
hero_chips:
  - Visible plus thermal multi-band package
  - Fire and hotspot analytics
  - Optional laser, ranging, and positioning expansion
hero_stats:
  - icon: /images/icons/radar-target-vehicle.svg
    label: Vehicle Detection
    value: 13 km
    note: Long-range vehicle observation reference from the source specification
  - icon: /images/icons/radar-target-person.svg
    label: Human Detection
    value: 4.8 km
    note: Human-size reference target in the published monitoring data
  - icon: /images/icons/radar-stat-range.svg
    label: Fire Detection
    value: 10 km
    note: 2 x 2 m fire-source reference in the published planning data
  - icon: /images/icons/product-gimbal-precision.svg
    label: PTZ Precision
    value: +/-0.1 deg
    note: 360-degree PTZ with focal-length adaptive speed control
positioning_title: "SOC-M13G-3U adds a multi-band long-watch tier to the SOC library for projects that need visible observation, thermal confirmation, hotspot awareness, and optional sensor expansion in one outdoor platform."
feature_cards:
  - icon: /images/icons/product-dual-spectrum.svg
    title: Multi-band visible and thermal sensing
    text: Combines starlight visible imaging with a 640 x 512 uncooled thermal core so the platform can hold day-night confirmation and wide-area thermal context inside one head.
  - icon: /images/icons/product-autotrack.svg
    title: Fire, hotspot, and target analytics
    text: Supports fire and smoke alarms, intrusion and boundary rules, human and vehicle filtering, temperature thresholds, and target tracking for more than simple manual viewing.
  - icon: /images/icons/product-radar-cueing.svg
    title: Radar-linked and workflow-ready
    text: The platform is suited to projects where radar, rule-based alarms, or map-linked workflows need one multi-band payload for confirmation, tracking, and evidence capture.
  - icon: /images/icons/product-environment-hardening.svg
    title: Expandable outdoor platform
    text: Optional laser illumination, laser ranging, Beidou or GPS, and fiber networking make the platform easier to adapt to large outdoor sites with different integration needs.
optical_channels:
  - title: Visible Channel
    rows:
      - name: Sensor
        value: Back-illuminated starlight CMOS
      - name: Low-Light Reference
        value: 0.0005 Lux color, 0.0001 Lux monochrome, 0 Lux with IR on
      - name: Lens
        value: 11 to 860 mm motorized zoom with manual and auto focus
      - name: Image Support
        value: White balance, electronic shutter, backlight compensation, strong-light suppression, 2D and 3D noise reduction, electronic stabilization, electronic and optical defog
      - name: Visible Role
        value: Daytime confirmation, readable detail capture, and scene follow-up when thermal cues need visible evidence
  - title: Thermal Channel
    rows:
      - name: Detector
        value: Sixth-generation uncooled VOx FPA, 640 x 512
      - name: Spectral Range
        value: 8 to 14 um
      - name: Thermal Sensitivity
        value: NETD 40 mK at 25 C, F1.0
      - name: Lens
        value: 31 to 155 mm motorized continuous zoom
      - name: Thermal Support
        value: 16 pseudo-color modes, AGC, brightness and contrast control, dual-view fusion, and picture-in-picture
technical_snapshot:
  - name: Detection And Recognition
    value: Vehicle detect 13 km and recognize 3.4 km, human detect 4.8 km and recognize 1.3 km, 2 x 2 m fire source detect 10 km
  - name: PTZ Coverage
    value: Pan 0 to 360 degrees, tilt -45 to +45 degrees
  - name: PTZ Speed
    value: Pan 0.01 to 30 degrees/s, tilt 0.01 to 15 degrees/s, with focal-length adaptive speed
  - name: Pointing Accuracy
    value: +/-0.1 degrees
  - name: Optional Expansion
    value: 3000 m IR laser illuminator, laser range finder, passive ranging, Beidou or GPS, and optional single-mode fiber output
  - name: Analytics And Fusion
    value: Intrusion, tripwire, human and vehicle filtering, target tracking, fire and smoke alarms, thermal threshold filtering, AR information overlay, and 18 fusion modes
  - name: Networking And Control
    value: RJ45 10/100 Base-T, HTTP, HTTPS, FTP, SMTP, DNS, NTP, RTSP, RTCP, RTP, TCP, UDP, ICMP, DHCP, ONVIF, GB28181, SDK access, and waterproof aviation connectors
  - name: Power Supply
    value: AC or DC24V with reverse-polarity protection
  - name: Power Consumption
    value: <=180 W
  - name: Weight
    value: 45 kg including PTZ
  - name: Environment
    value: IP66 with optional IP67, -40 to +60 C operating range, -45 to +70 C storage range, 6000 V surge protection, and 96-hour salt-mist resistance
integration_native_title: "The native multi-band workflow for long-watch monitoring, alarm review, and fire-aware observation."
integration_image: /images/soc/soc-m13g-3u-software.jpeg
integration_image_alt: "Native multi-band optics software screen showing alarm and mapped review"
integration_text: "The native platform behind SOC-M13G-3U already points toward a broader operations workflow: dual-channel preview, PTZ control, alarm review, GIS mapping, and fire or hotspot management. For Cyrentis projects, those outputs should feed a shared command environment rather than remain isolated as a stand-alone camera screen."
integration_horizon_title: "How SOC-M13G-3U connects into Horizon."
integration_horizon_text: "In Horizon-led deployments, SOC-M13G-3U should contribute its visible stream, thermal stream, fire or hotspot alarms, tracking state, and optional range or position context so operators can move from alert to confirmation without switching tools."
integration_modules:
  - icon: /images/horizon/module-sense.svg
    title: Horizon Sense
    text: Registers visible, thermal, and optional expansion sensors as part of one managed payload.
  - icon: /images/horizon/module-ai.svg
    title: Horizon AI
    text: Carries fire, hotspot, and rule-based alert logic into the broader site decision layer.
  - icon: /images/horizon/module-track.svg
    title: Horizon Track
    text: Keeps radar-cued or rules-based follow-up attached to one multi-band target context.
  - icon: /images/horizon/module-command.svg
    title: Horizon Command
    text: Pushes confirmed events into response review, dispatch, and escalation workflows.
  - icon: /images/horizon/module-archive.svg
    title: Horizon Archive
    text: Preserves dual-channel imagery and event-linked evidence for review and reporting.
performance_notes:
  - title: Visible analytics reference
    image: /images/soc/soc-m13g-3u-visible.jpeg
    alt: Visible-channel target recognition reference from the multi-band platform
    text: The visible channel supports high-resolution confirmation when the site still needs identifiable daytime imagery instead of thermal-only cues.
  - title: Thermal reach reference
    image: /images/soc/soc-m13g-3u-thermal.jpeg
    alt: Thermal observation reference from the multi-band platform
    text: The uncooled thermal side carries the platform through night scenes, haze, and low-contrast backgrounds while preserving longer-watch coverage than a compact short-range head.
  - title: Native software context
    image: /images/soc/soc-m13g-3u-software.jpeg
    alt: Multi-band platform software with mapped alarm review
    text: Alarm review, map context, and dual-channel imagery indicate why this model fits broader command workflows rather than simple one-camera viewing.
  - title: Airfield and open-area confirmation
    image: /images/soc/soc-m13g-3u-airport.jpeg
    alt: Dual-view airfield confirmation scene from a multi-band platform
    text: The platform can support airfield, boundary, and open-area observation tasks where visible and thermal views must remain aligned in one operator experience.
deployment_scenarios:
  - image: /images/soc/soc-m13g-3u-highway.png
    title: Highway and corridor watch
    alt: Thermal monitoring scene along a highway corridor
    text: Suitable for long transport corridors and roadside positions where all-weather observation matters more than a compact head.
  - image: /images/soc/soc-m13g-3u-urban.png
    title: Urban high-point overview
    alt: Thermal overview of an urban street scene
    text: Fits elevated city and industrial sites that need wide-area thermal context with readable visible follow-up during the day.
  - image: /images/soc/soc-m13g-3u-airport.jpeg
    title: Airport and open-area perimeter monitoring
    alt: Dual visible and thermal scene showing an aircraft approach
    text: Strong fit for airport boundaries, base protection, fire-aware open terrain watch, and other large outdoor areas with mixed detection tasks.
---
SOC-M13G-3U expands the Cyrentis SOC library with a multi-band visible and thermal platform aimed at longer-watch, fire-aware, and integration-heavy deployments. It sits above the medium dual-spectrum tier when the site needs broader analytics, more alarm context, and optional sensor expansion inside one outdoor payload.

For the public page, the emphasis stays on multi-band sensing, detection references, fire or hotspot workflow value, PTZ behavior, and integration fit. Low-level platform administration, full account policy, and detailed lifecycle counters should remain in the Cyrentis datasheet.
