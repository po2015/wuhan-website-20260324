---
title: SOC-D13G-2A
description: "Dual-spectrum air-surveillance payload with visible zoom, thermal imaging, precision PTZ, and radar-linked target confirmation."
kicker: SOC Detail
layout: soc-detail
slug: soc-d13g-2a
aliases:
  - /sensors/soc/soc-m/
weight: 2
catalog_order: 20
series_label: SOC surveillance optics series
model: SOC-D13G-2A
hero_image: /images/soc/soc-d13g-2a-hero.png
hero_lead: "A medium-range EO and thermal payload for visual confirmation, target tracking, and radar-cued response in low-altitude security and critical-site operations."
hero_chips:
  - Dual-spectrum EO + thermal
  - Gimbal-stabilized PTZ
  - Air-surveillance mission profile
hero_stats:
  - icon: /images/icons/radar-target-vehicle.svg
    label: Vehicle D / R / I
    value: 13 / 3.4 / 1.7 km
    note: 2.3 x 2.3 m reference target
  - icon: /images/icons/radar-target-person.svg
    label: Human D / R / I
    value: 4.8 / 2.5 / 1.3 km
    note: 1.8 x 0.6 m reference target
  - icon: /images/icons/radar-target-drone.svg
    label: Drone Cueing
    value: 2.5 / 1.5 km
    note: Visible / thermal tracking on a 0.3 x 0.3 m UAV
  - icon: /images/icons/product-gimbal-precision.svg
    label: PTZ Performance
    value: 120 deg/s + 0.01 deg
    note: High-speed pan with digital angle positioning
positioning_title: "Configured for radar-assisted confirmation, long-range visual verification, and day-night tracking where operators need one optical payload to close the gap between alert and decision."
feature_cards:
  - icon: /images/icons/product-dual-spectrum.svg
    title: Dual-spectrum payload
    text: Combines 2560 x 1440 visible imaging with a 640 x 512 LWIR thermal channel so operators can verify activity across daylight, darkness, glare, haze, and thermal contrast conditions.
  - icon: /images/icons/product-autotrack.svg
    title: Front-end auto tracking
    text: Supports manual and automatic tracking logic at the payload side, reducing the need to re-acquire the target every time the optical channel changes or the scene shifts.
  - icon: /images/icons/product-radar-cueing.svg
    title: Radar and software cueing
    text: Fits workflows where radar provides the first alert and the optical payload delivers visual confirmation, classification support, and operator evidence inside a shared command screen.
  - icon: /images/icons/product-environment-hardening.svg
    title: Built for exposed sites
    text: IP66 sealing, anti-salt design, strong-light handling, and wind resistance make the payload more credible for rooftop, coastal, fixed-site, and mobile deployment.
performance_notes:
  - title: Drone tracking
    image: /images/soc/soc-d13g-2a-software.png
    alt: Native software showing tracked targets and mapped context
    text: The visible channel supports UAV tracking to 2.5 km, while the thermal channel supports 1.5 km tracking on a 0.3 x 0.3 m target.
  - title: Fire detection
    image: /images/soc/soc-d13g-2a-fire.png
    alt: Thermal image showing hotspot detection
    text: Public project positioning can use a 10 km fire-detection figure, with 6 km on a 2 x 2 m fire target.
  - title: IVS reach
    image: /images/soc/soc-d13g-2a-analytics.jpeg
    alt: Thermal analytics view with multiple detected targets
    text: Intelligent video analysis is specified to 4.6 km for vehicles and 1.6 km for humans.
  - title: Thermal note
    image: /images/soc/soc-d13g-2a-dri.jpeg
    alt: Thermal image illustrating detection, recognition, and identification range
    text: DRI values are environmental reference values and should be read as solution-planning guidance rather than an unconditional field guarantee.
optical_channels:
  - title: Visible Channel
    rows:
      - name: Sensor
        value: 1/1.8 inch starlight CMOS
      - name: Resolution
        value: 2560 x 1440
      - name: Lens
        value: 8 to 500 mm, 62x optical zoom
      - name: Digital Zoom
        value: 16x
      - name: Image Support
        value: WDR, defog, strong-light suppression, image stabilization
  - title: Thermal Channel
    rows:
      - name: Sensor
        value: 640 x 512 uncooled LWIR core
      - name: Thermal Sensitivity
        value: NETD <= 30 mK
      - name: Spectral Range
        value: 7.5 to 14 um
      - name: Lens
        value: 31 to 155 mm continuous zoom, 5x optical range
      - name: Thermal Functions
        value: Pseudo color, image fusion, hot-spot alarm, temperature filtering
technical_snapshot:
  - name: PTZ Coverage
    value: Pan 0 to 360 degrees, tilt -30 to +60 degrees
  - name: PTZ Speed
    value: Pan 0.01 to 120 degrees/s, tilt 0.01 to 100 degrees/s
  - name: Pointing Accuracy
    value: 0.01 degrees
  - name: Tracking And AI
    value: Intrusion, boundary crossing, loitering, people and vehicle filtering, hot-spot alarm, manual and auto tracking
  - name: Video And Control
    value: Single-IP operation, H.265 / H.264 / MJPEG, ONVIF and standard IP protocols
  - name: Environment
    value: IP66, -25 to +55 C, anti-salt, strong-light and 33 m/s wind resistance
  - name: Power And Weight
    value: DC48V, 150 W stable / 350 W peak, 40 kg
integration_native_title: "The native software path from alert to visual confirmation."
integration_image: /images/soc/soc-d13g-2a-software.png
integration_image_alt: "SOC software view showing visual confirmation and mapped command context"
integration_text: "The source platform demonstrates the workflow this payload should support on the site: radar or rule-based alerting, live optical confirmation, operator tracking, mapped event context, and a visible path into command and archive. On Cyrentis projects, the same device outputs can be coordinated with Horizon for shared device, event, and response handling."
integration_horizon_title: "How the payload fits inside Horizon instead of remaining a stand-alone software island."
integration_horizon_text: "For Cyrentis projects, the objective is not to duplicate the native software screen forever. The payload should expose stream, angle, alert, and tracking context to Horizon so operators can move between radar cueing, optical confirmation, command action, and archive review without splitting the workflow across unrelated consoles."
integration_modules:
  - icon: /images/horizon/module-sense.svg
    title: Horizon Sense
    text: Registers the EO payload as a managed device with shared health, angle, and stream context.
  - icon: /images/horizon/module-track.svg
    title: Horizon Track
    text: Carries target state from radar alert to optical follow-up without forcing the operator to restart interpretation.
  - icon: /images/horizon/module-ai.svg
    title: Horizon AI
    text: Supports downstream classification, rule evaluation, and scene-based prioritization when the payload detects ambiguous activity.
  - icon: /images/horizon/module-command.svg
    title: Horizon Command
    text: Pushes optical confirmation, alert review, and operator actions into one dispatch workflow.
  - icon: /images/horizon/module-archive.svg
    title: Horizon Archive
    text: Preserves event-linked imagery and operator evidence for review, reporting, and project audit needs.
deployment_scenarios:
  - image: /images/soc/soc-d13g-2a-rooftop.jpeg
    title: Fixed rooftop and perimeter watch
    alt: EO payload installed on a rooftop platform
    text: Suitable for exposed fixed sites where long-range visual confirmation must remain stable through strong light, weather, and open-air installation.
  - image: /images/soc/soc-d13g-2a-field.jpeg
    title: Tripod and rapid field deployment
    alt: EO payload deployed together with adjacent sensing equipment in the field
    text: Fits temporary low-altitude security setups where radar, RF, and optics need to be assembled quickly around one monitored area.
  - image: /images/soc/soc-d13g-2a-vehicle.jpeg
    title: Vehicle-mounted mobile observation
    alt: EO payload mounted on a vehicle roof together with adjacent equipment
    text: Works for mobile surveillance teams that need a stabilized optical head and fast cueing response without a permanent mast installation.
---
SOC-D13G-2A is positioned as a dual-spectrum observation payload for projects where an alert alone is not enough and the operator still needs readable confirmation. The visible and thermal channels are strong enough to support day-night target verification, while the gimbal architecture keeps the payload credible on rooftops, temporary field positions, and mobile platforms.

For the website, the page focuses on DRI values, cueing value, PTZ behavior, integration readiness, and deployment form. Deeper codec tables, alarm matrices, patrol counts, and image-processing option lists should stay in the Cyrentis datasheet or proposal package.
