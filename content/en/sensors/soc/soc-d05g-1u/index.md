---
title: SOC-D05G-1U
description: "Short-range dual-spectrum surveillance optics with configurable daylight package and optional laser ranging for mobile, fixed, and shipborne observation."
kicker: SOC Detail
layout: soc-detail
slug: soc-d05g-1u
aliases:
  - /sensors/soc/soc-s/
weight: 1
catalog_order: 10
series_label: SOC surveillance optics series
model: SOC-D05G-1U
hero_image: /images/soc/soc-d05g-1u-hero.png
hero_lead: "A short-range dual-spectrum optical payload for perimeter watch, vehicle observation, and shipborne or fixed-site deployment where stabilization and configurable optics matter more than extreme stand-off distance."
hero_chips:
  - Dual-spectrum EO + thermal
  - Gyro-stabilized short-range tier
  - Optional laser ranging
hero_stats:
  - icon: /images/icons/product-dual-spectrum.svg
    label: Daylight Options
    value: 50x / 35x
    note: Configurable visible package depending on delivered suffix
  - icon: /images/icons/radar-stat-range.svg
    label: Laser Range Finder
    value: Optional 3 km
    note: Available with the ranging configuration at 1 to 10 Hz
  - icon: /images/icons/product-gimbal-precision.svg
    label: PTZ Performance
    value: 150 deg/s + 0.005 deg
    note: Direct-drive positioning with <= 0.2 mrad stabilization
  - icon: /images/icons/product-environment-hardening.svg
    label: Site Hardening
    value: IP66 + <20 kg
    note: Suitable for fixed, vehicle, and shipborne deployment
positioning_title: "SOC-D05G-1U is the compact short-range optical tier for sites that need a stabilized day-night head with configurable daylight zoom and optional ranging inside a lighter platform envelope."
configurations_title: "The short-range product keeps one base model and uses suffixes to distinguish daylight and ranging packages."
config_suffixes:
  - suffix: A
    full_model: SOC-D05G-1U-A
    title: Standard daylight package
    text: The A configuration emphasizes optical confirmation with a 1920 x 1080 daylight camera, 50x visible zoom, uncooled thermal imaging, and gyro-stabilized observation.
    highlights:
      - 1/1.8 inch visible sensor at 1920 x 1080
      - 6 to 300 mm visible lens, 50x optical zoom
      - Uncooled 640 x 512 LWIR thermal channel
      - No integral laser range finder
  - suffix: B
    full_model: SOC-D05G-1U-B
    title: Ranging package
    text: The B configuration adds an eye-safe 3 km laser range finder and shifts to a 35x daylight channel, making it better suited to guided observation and lightweight target ranging.
    highlights:
      - 1/2 inch visible sensor with 35x optical zoom
      - 1535 nm laser range finder to 3 km
      - Optional 1 km or 2 km laser illuminator
      - Manual or auto tracking can be selected as an option
feature_cards:
  - icon: /images/icons/product-dual-spectrum.svg
    title: Lightweight dual-spectrum observation
    text: Combines uncooled thermal imaging with a configurable daylight channel so short-range confirmation can remain usable across daylight, darkness, spray, and haze.
  - icon: /images/icons/product-gimbal-precision.svg
    title: Gyro-stabilized direct drive
    text: Uses a precision direct-drive platform with gyro stabilization so the image remains readable under vehicle movement, deck motion, or exposed wind conditions.
  - icon: /images/icons/product-autotrack.svg
    title: Optional tracking workflow
    text: Tracking is available as an option when the project needs local target follow-up instead of simple manual viewing only.
  - icon: /images/icons/product-radar-cueing.svg
    title: Ready for broader sensor workflows
    text: Can work as a stand-alone optical head or as the visual confirmation layer under a radar-led or rules-led site workflow.
optical_channels:
  - title: Visible Channel
    rows:
      - name: Configuration A
        value: 1/1.8 inch CMOS, 1920 x 1080, 6 to 300 mm, 50x optical zoom
      - name: Configuration B
        value: 1/2 inch CMOS, 6 to 210 mm, 35x optical zoom
      - name: Low-Light Performance
        value: 0.005 Lux color and 0.0005 Lux black-and-white reference
      - name: Use Case
        value: Daytime confirmation, guided observation, and short-range visual verification
  - title: Thermal Channel
    rows:
      - name: Sensor
        value: Uncooled LWIR, 640 x 512
      - name: Spectral Range
        value: 8 to 14 um
      - name: Thermal Sensitivity
        value: NETD <= 40 mK at 25 C
      - name: Lens
        value: 20 to 100 mm continuous zoom
      - name: Thermal Role
        value: Day-night observation and short-range target confirmation in complex weather
technical_snapshot:
  - name: Pan-Tilt Coverage
    value: Pan n x 360 degrees, tilt -20 to +90 degrees
  - name: PTZ Response
    value: 150 degrees/s maximum angular velocity and 150 degrees/s2 maximum angular acceleration
  - name: Pointing And Stability
    value: <= 0.005 degrees positioning accuracy and <= 0.2 mrad stabilization accuracy
  - name: Range Finder Option
    value: 1535 nm, 1 to 10 Hz, <= +/-2 m RMS, >= 3 km
  - name: Illuminator Option
    value: 808 nm, 1 km or 2 km, electric synchronous zoom
  - name: Power And Envelope
    value: 27VDC, <= 150 W, <= 280 mm x 430 mm, < 20 kg
  - name: Environment
    value: IP66, -40 to +60 C, aluminium alloy housing
integration_native_title: "The native short-range optical workflow for fixed, vehicle, and shipborne observation."
integration_image: /images/soc/soc-d13g-2a-software.png
integration_image_alt: "Generic optical control software view for SOC workflows"
integration_text: "SOC-D05G-1U can remain a compact local optical head, but it becomes more useful when alert, stream, and pointing data are shared with the surrounding security workflow instead of isolated at the device console."
integration_horizon_title: "How SOC-D05G-1U fits the Horizon operating picture."
integration_horizon_text: "In Cyrentis deployments, the short-range optical layer should provide stream, angle, and event context to Horizon so radar, RF, and optical confirmation do not split into unrelated operator screens."
integration_modules:
  - icon: /images/horizon/module-sense.svg
    title: Horizon Sense
    text: Registers the short-range optical payload as part of the managed sensing layer.
  - icon: /images/horizon/module-track.svg
    title: Horizon Track
    text: Carries short-range follow-up from the first alert into visual confirmation and continued observation.
  - icon: /images/horizon/module-command.svg
    title: Horizon Command
    text: Connects local optical confirmation to dispatch or on-site response decisions.
  - icon: /images/horizon/module-link.svg
    title: Horizon Link
    text: Keeps the payload usable with adjacent radar, RF, and external control environments.
deployment_scenarios:
  - image: /images/soc/soc-d13g-2a-rooftop.jpeg
    title: Fixed perimeter and rooftop watch
    alt: Short-range optical payload mounted at a fixed site
    text: Suitable for compact perimeter and critical-site positions where a lighter stabilized head is preferred over a heavier long-range platform.
  - image: /images/soc/soc-d13g-2a-vehicle.jpeg
    title: Vehicle-mounted observation
    alt: Short-range optical payload mounted on a vehicle
    text: Strong fit for mobile teams that need stabilized viewing under motion without carrying a large cooled payload.
  - image: /images/soc/soc-d13g-2a-field.jpeg
    title: Shipborne and rapid field use
    alt: Short-range optical payload deployed with adjacent sensors in the field
    text: Works in temporary field deployments and lighter shipborne observation roles where stabilization and compact size matter.
---
SOC-D05G-1U is the short-range member of the Cyrentis SOC line. It is designed for projects that need a lighter gyro-stabilized day-night payload with configurable daylight optics and an optional rangefinder, rather than the longer reach and heavier envelope of the cooled series.

For the public page, the emphasis stays on platform form factor, configurable visible and ranging options, stabilization value, and deployment fit. Lower-level interface permutations and maintenance details should remain in the Cyrentis datasheet.
