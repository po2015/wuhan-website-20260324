---
title: SOC-D20G-2U
description: "Long-range cooled EO and thermal surveillance optics with configurable daylight package and extended laser ranging for tower, coastal, vehicle, and shipborne observation."
kicker: SOC Detail
layout: soc-detail
slug: soc-d20g-2u
aliases:
  - /sensors/soc/soc-l/
weight: 3
catalog_order: 30
series_label: SOC surveillance optics series
model: SOC-D20G-2U
hero_image: /images/soc/soc-l-hero.png
hero_lead: "A long-range cooled optical payload for extended identification, stabilized tracking, and long-watch confirmation where the visible package can be selected to match the deployment."
hero_chips:
  - Cooled MWIR + configurable daylight imaging
  - Long-range observation tier
  - Laser ranging up to 20 km
hero_stats:
  - icon: /images/icons/radar-target-vehicle.svg
    label: Thermal D / R / I
    value: Up to 21.8 / 15.3 / 10.7 km
    note: Highest values correspond to the CL long-focal configuration
  - icon: /images/icons/product-dual-spectrum.svg
    label: Daylight Options
    value: 52x / 60x
    note: 3 MP and 4 MP visible packages available by suffix
  - icon: /images/icons/radar-stat-range.svg
    label: Laser Range Finder
    value: 12 km / 20 km
    note: Available according to C or CL configuration
  - icon: /images/icons/product-gimbal-precision.svg
    label: PTZ Precision
    value: 120 deg/s + 0.005 deg
    note: Direct-drive response with high positioning accuracy
positioning_title: "SOC-D20G-2U is the long-range cooled member of the SOC line for projects that need deeper identification distance, larger focal packages, and a stronger fit for tower, coastal, shipborne, or large vehicle observation."
configurations_title: "The long-range product keeps one base model and uses suffixes to distinguish visible and long-focal optical packages."
config_suffixes:
  - suffix: C
    full_model: SOC-D20G-2U-C
    title: 52x daylight package
    text: The C configuration combines cooled thermal imaging with a 3 MP visible channel, 52x daylight zoom, and a 12 km laser range finder for projects that need strong range without the largest optical head.
    highlights:
      - 35 to 700 mm cooled thermal lens, 640 x 512 MCT detector
      - 2048 x 1536 visible output with 15 to 775 mm, 52x optical zoom
      - 1535 nm laser range finder to 12 km
      - Better fit where reach matters but envelope and budget still need control
  - suffix: CL
    full_model: SOC-D20G-2U-CL
    title: 60x daylight package
    text: The CL configuration uses the longest thermal and daylight package in the current line and extends the range finder to 20 km for open-area and coastal watch tasks.
    highlights:
      - 110 to 1100 mm cooled thermal lens, 640 x 512 MCT detector
      - 2688 x 1520 visible output with 20 to 1200 mm, 60x optical zoom
      - 1570 nm laser range finder to 20 km
      - Best fit for coastal, shipborne, and extended tower observation
feature_cards:
  - icon: /images/icons/product-dual-spectrum.svg
    title: Long-focal cooled observation
    text: Uses a cooled MWIR thermal pack with long-focal visible support so operators can maintain readable observation farther into open terrain, water, and low-contrast scenes.
  - icon: /images/icons/radar-stat-range.svg
    title: Integrated ranging support
    text: Adds an eye-safe laser range finder so the payload can contribute distance confirmation as well as image-based target verification.
  - icon: /images/icons/product-autotrack.svg
    title: Visible and thermal tracking
    text: Supports manual and auto tracking with visible and thermal image switching so the operator can keep follow-up continuity through changing background or weather.
  - icon: /images/icons/product-environment-hardening.svg
    title: Heavy-duty deployment fit
    text: IP66 protection, wide environmental tolerance, and direct-drive mechanics make the payload credible for tower, coastal, vehicle, and shipborne roles.
performance_notes:
  - title: Thermal reach reference
    image: /images/soc/soc-l-thermal.jpeg
    alt: Thermal observation sample from the long-range cooled platform
    text: The long-focal cooled thermal package is the main differentiator of SOC-D20G-2U, especially in the CL configuration where identification distance becomes the primary purchase driver.
  - title: Daylight zoom package
    image: /images/soc/soc-l-zoom.jpeg
    alt: Visible zoom observation sample from the long-range payload
    text: The visible channel can be configured around the 52x or 60x package, allowing the daylight side of the product to match the deployment rather than forcing one camera choice.
  - title: Platform architecture
    image: /images/soc/soc-l-drawing.jpeg
    alt: Long-range optics platform drawing
    text: The integrated head combines cooled thermal imaging, daylight observation, laser ranging, and stabilized motion control in one platform.
  - title: Base and envelope
    image: /images/soc/soc-l-base.jpeg
    alt: Long-range optics base drawing
    text: The heavier base and platform envelope align with fixed towers, coastal sites, and larger vehicle or shipborne integration work.
optical_channels:
  - title: Visible Channel
    rows:
      - name: Configuration C
        value: 1/1.8 inch CMOS, 2048 x 1536, 15 to 775 mm continuous zoom, 52x
      - name: Configuration CL
        value: 1/1.8 inch CMOS, 2688 x 1520, 20 to 1200 mm continuous zoom, 60x
      - name: Focus
        value: Auto, manual, and semi-auto
      - name: Image Support
        value: Electronic and optical defog
  - title: Thermal Channel
    rows:
      - name: Sensor
        value: MCT cooled 640 x 512 FPA, 15 um pixel pitch
      - name: Spectral Range
        value: 3 to 5 um
      - name: Thermal Sensitivity
        value: NETD <= 25 mK
      - name: Configuration C
        value: 35 to 700 mm continuous zoom, 10x
      - name: Configuration CL
        value: 110 to 1100 mm continuous zoom, 10x
technical_snapshot:
  - name: PTZ Coverage
    value: Pan n x 360 degrees, tilt -10 to +185 degrees
  - name: PTZ Response
    value: 120 degrees/s maximum angular velocity and 150 degrees/s2 maximum angular acceleration
  - name: Pointing Accuracy
    value: <= 0.005 degrees
  - name: Laser Range Finder Options
    value: 1535 nm to 12 km or 1570 nm to 20 km, depending on configuration
  - name: Tracking
    value: Visible and thermal switching tracking with manual and auto modes
  - name: Video And Control
    value: Two channels of network video plus one 14-bit thermal output, RJ45 / RS422, Pelco-P and Pelco-D
  - name: Environment
    value: IP66, -40 to +60 C, <= 95 percent RH
  - name: Power And Weight
    value: 48VDC +/-10 percent, <= 500 W peak, <= 95 kg
integration_native_title: "The native long-range observation path from cue to verified target."
integration_image: /images/soc/soc-d13g-2a-software.png
integration_image_alt: "Generic optical control software view for SOC workflows"
integration_text: "SOC-D20G-2U can operate as a stand-alone long-range optical head for local control, but its project value is higher when stream, range, target, and pointing data are forwarded into the broader site workflow."
integration_horizon_title: "How SOC-D20G-2U fits inside Horizon for long-watch operations."
integration_horizon_text: "For Cyrentis deployments, the long-range optical layer should not remain a separate console. Its cueing, stream, ranging, and tracking context should be absorbed into Horizon so operators keep one operational picture."
integration_modules:
  - icon: /images/horizon/module-sense.svg
    title: Horizon Sense
    text: Registers the payload, stream, and health state as part of the monitored device layer.
  - icon: /images/horizon/module-track.svg
    title: Horizon Track
    text: Carries long-range follow-up from the first cue through persistent observation and operator review.
  - icon: /images/horizon/module-command.svg
    title: Horizon Command
    text: Connects long-range optical confirmation to dispatch and response decisions.
  - icon: /images/horizon/module-archive.svg
    title: Horizon Archive
    text: Preserves event-linked imagery for evidence, review, and reporting after long-watch operations.
deployment_scenarios:
  - image: /images/soc/soc-d13g-2a-rooftop.jpeg
    title: Coastal and fixed tower deployment
    alt: Long-range optics mounted at an elevated fixed site
    text: Suitable for coastal or exposed tower positions where large stand-off distance and stable pointing matter more than compact size.
  - image: /images/soc/soc-d13g-2a-vehicle.jpeg
    title: Large vehicle or mast integration
    alt: Long-range optics adapted for vehicle integration
    text: Works for larger mobile platforms that can carry a heavier long-range optical head and still benefit from stabilized tracking and ranging.
  - image: /images/soc/soc-d13g-2a-field.jpeg
    title: Open-area and shipborne watch
    alt: Long-range optics supporting extended open-area observation
    text: Fits extended observation tasks over open terrain or water where the project needs the strongest optical reach in the current SOC line.
---
SOC-D20G-2U is the long-range cooled member of the current Cyrentis SOC product line. It is intended for projects that need deeper identification distance, a configurable daylight package, and a stronger fit for coastal, shipborne, or large fixed-site deployment.

For the public page, the emphasis stays on cooled thermal reach, visible package options, laser range finder capacity, and workflow value. Lower-level protocol tables and maintenance details should remain in the Cyrentis datasheet.
