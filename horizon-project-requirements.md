# Horizon Executable Requirements Document

## 1. Document Status

This document is the **primary executable requirement document** for the next Horizon demo project.

It is written so it can be taken into a brand-new repository without depending on the current conversation context.

If a new project is created later, this file should be treated as the baseline product, UX, and implementation brief for the first usable Horizon demo build.

## 2. Why This Document Exists

The purpose of this document is to define a version of Horizon that can be:

- built quickly
- demonstrated to users quickly
- visually convincing
- understandable without backend infrastructure
- suitable for internal review and customer-facing presentation

This is not intended to describe a full production software platform implementation.

It is intended to define a **high-quality frontend-only demo product** that expresses what Horizon is supposed to become.

## 3. Cyrentis Background

### 3.1 Company Positioning

Cyrentis is a technology company focused on integrated sensing systems for:

- security monitoring
- low-altitude awareness
- practical multi-sensor deployment projects

The company is not positioned as only a single-device vendor.

The core Cyrentis business structure is:

1. Horizon software platform
2. Sensor products
3. Deployment-oriented consulting and integration services

### 3.2 Sensor Product Families

Cyrentis currently presents three sensor families:

- SRC: Surveillance Radar
- SOC: Surveillance Optics
- SDC: Spectrum Detection

These three sensing families are intended to work together as a layered monitoring system.

### 3.3 Services Context

Cyrentis also provides services that support deployment, especially:

- software customization
- security solution design
- security equipment integration

This matters because Horizon is not only a software UI concept.
It is the software layer that helps tie sensing products and deployment logic together.

### 3.4 Company Philosophy

Cyrentis should be understood as building:

- layered monitoring systems
- unified operations
- scenario-driven designs
- open integration paths

The Horizon demo should therefore reflect:

- software and sensing alignment
- practical deployment thinking
- operator workflow continuity
- multi-sensor coordination

## 4. Horizon Background

### 4.1 What Horizon Is

Horizon is the Cyrentis software platform for unified multi-sensor operations.

Its role is to bring:

- radar
- electro-optical sensing
- RF / spectrum sensing
- site context
- operator workflow

into one coherent software environment.

### 4.2 What Horizon Should Communicate

Horizon should communicate these ideas clearly:

- one platform instead of fragmented device tools
- one site view instead of disconnected software layers
- one operator workflow from sensing to response
- one place to understand coverage, events, tracks, and action

### 4.3 What Horizon Is Not

For this demo, Horizon should **not** be presented as:

- a finished production command-and-control platform
- a military C4ISR system
- a real-time integrated deployment with live hardware drivers
- a finished enterprise backend product

This demo is a product prototype for:

- concept validation
- interface review
- customer explanation
- future implementation planning

### 4.4 Core Horizon Module Language

The current Horizon concept on the website already defines a module narrative that should carry into the new project.

Core modules currently represented are:

- Horizon Sense
- Horizon Spatial
- Horizon Fusion
- Horizon Track
- Horizon AI
- Horizon Command
- Horizon Notify
- Horizon Archive
- Horizon Link

The demo does not need to fully implement each module as a real system.
However, it should visually and structurally respect this module language where useful.

## 5. Primary Objective of the New Demo Project

Build a **pure frontend Horizon demo site/application** that quickly helps a user understand:

- how a multi-sensor site can be represented in one interface
- how devices can be positioned and configured
- how radar, optics, and spectrum coverage differ
- how radar scanning behaves dynamically
- how Horizon can look and feel as a unified operations product

The most important outcome is **demo credibility**.

## 6. Intended Audience

The demo is primarily intended for:

- prospective customers
- solution partners
- internal Cyrentis review
- sales and presentation scenarios
- early design and product discussion

Typical scenario audiences may include:

- airport security or perimeter stakeholders
- coastal or fishery monitoring projects
- industrial site protection projects
- system integrators

## 7. What Users Should Understand in 3 Minutes

If a user sees the demo for only three minutes, they should leave with these impressions:

1. Horizon is the software layer above multiple sensor types
2. Cyrentis understands layered site awareness, not just single devices
3. Radar, EO, and RF can be explained in one interface
4. The platform is visually coherent and operationally believable

## 8. Product Direction for This Demo

This project should be a **frontend-first visual product prototype**, not a backend-heavy engineering exercise.

The demo should prioritize:

- map-based understanding
- device placement
- sensing visualization
- smooth motion and interaction quality
- operator-facing clarity

If a better design idea appears during implementation that improves clarity, realism, or product quality, it is acceptable to improve beyond the basic suggestions in this document.

The document defines the floor, not the ceiling.

## 9. Non-Goals

The following are not required in the first version:

- backend API
- authentication
- database persistence
- real device connectivity
- production alarm engine
- full access control
- real AI inference
- final enterprise integration layer

The first version should stay focused on presentation quality and interaction quality.

## 10. Required Technical Direction

### 10.1 Core Architecture

The project must be:

- frontend only
- static-build friendly
- easy to run locally
- easy to demo from a static deployment

### 10.2 Recommended Stack

- React
- TypeScript
- Vite
- Tailwind CSS
- Zustand
- `@react-google-maps/api`

Optional but recommended:

- Framer Motion for panel and interface transitions

### 10.3 Visualization Approach

For the sensing overlays:

- use Google Maps for the base map
- use frontend-only overlays for coverage visualization
- use Canvas and `requestAnimationFrame` where animated radar effects need better smoothness
- use SVG where static icons, small markers, or semantic overlays are sufficient

### 10.4 Deployment

The output should be distributable as:

- static frontend assets
- a build that can run on simple static hosting
- an intranet-hosted web demo
- optionally a preview deployment through a simple frontend hosting service

## 11. Required Source Assets and Style References

When the new project is created, it should carry over or reference the following materials from the current site project:

- `icon-style.md`
- `logo.png`
- `icon.png`
- `static/images/horizon/module-sense.svg`
- `static/images/horizon/module-spatial.svg`
- `static/images/horizon/module-fusion.svg`
- `static/images/horizon/module-track.svg`
- `static/images/horizon/module-ai.svg`
- `static/images/horizon/module-command.svg`
- `static/images/horizon/module-notify.svg`
- `static/images/horizon/module-archive.svg`
- `static/images/horizon/module-link.svg`

These assets are important because the visual language already exists and should not be reinvented from scratch without reason.

## 12. Visual and Brand Direction

### 12.1 Desired Feel

The Horizon demo should feel:

- serious
- modern
- operational
- product-oriented
- visually polished
- technically credible

### 12.2 What It Should Not Feel Like

It should not feel like:

- a generic admin dashboard
- a static corporate microsite
- a game-like tactical UI
- a cluttered engineering mockup

### 12.3 Brand Alignment

The visual direction should remain compatible with the current Cyrentis site language:

- clean enterprise interface
- layered information presentation
- controlled motion
- restrained but high-quality use of color
- iconography consistent with the current site

### 12.4 Design Freedom

The implementation can improve on the exact layout ideas listed here if the result is:

- more readable
- more convincing
- more demo-friendly
- more visually coherent

## 13. Product Scope for v1

The first demo version should focus on four major capabilities:

1. Site map and map controls
2. Device placement and editing
3. Sensor coverage and animated scanning
4. A light but credible Horizon interface shell around those capabilities

## 14. Core Functional Requirements

### 14.1 Google Maps

The application must use Google Maps as the mapping base.

Required map features:

- map load on app start
- street view mode
- satellite view mode
- map type switching
- zoom
- pan
- site-centered camera presets

The map should be the visual center of the experience.

### 14.2 Device Placement and Editing

The demo must allow users to place and edit device positions.

Each device should support:

- name
- type
- latitude
- longitude
- heading or orientation where applicable
- enabled / disabled state

Recommended interactions:

- add device from a device library or toolbar
- click on map to place
- drag to reposition
- edit values in a side panel
- update coordinates numerically

### 14.3 Supported Device Categories

At minimum, the demo must support:

- radar
- electro-optical
- spectrum detection

Optional device extensions may be added later.

## 15. Radar Requirements

Radar is the most important dynamic layer in the demo.

Each radar device should support:

- device position
- heading
- coverage radius
- sector angle
- rotation speed in RPM
- optional sector mode or full-rotation mode

### 15.1 Radar Motion

Radar scan motion should be:

- smooth
- premium
- readable
- stable during zoom and pan

### 15.2 Radar Visuals

Recommended radar visual components:

- soft range area
- animated sweep beam
- fading trail or glow tail
- optional range rings
- optional sector boundary guides

### 15.3 Radar Modes

If the configuration model allows it, radar should support:

- fixed sector scan
- rotating sector scan
- full 360 rotating scan

## 16. Electro-Optical Requirements

Electro-optical devices should support:

- position
- heading
- narrow coverage angle
- visible range distance

The EO layer should visually feel more precise and narrower than radar.

Recommended visual treatment:

- slim wedge
- controlled transparency
- subtle directional emphasis

EO animation should remain light and should not visually overpower radar.

## 17. Spectrum Detection Requirements

Spectrum detection devices should support:

- position
- configurable radius
- default 360 degree coverage behavior

Recommended visual treatment:

- circular coverage region
- pulse or ring effect
- lower visual emphasis than radar sweep

The purpose is to communicate presence and monitoring footprint, not to mimic radar behavior.

## 18. Demo Data Requirements

The project should use local demo data only.

Preferred data sources:

- JSON files
- TypeScript mock modules

The first version should ship with:

- predefined sites
- predefined device sets
- scenario presets
- sample event data if needed
- optional track samples

Optional but acceptable:

- save current device layout to `localStorage`

## 19. Required Demo Scenarios

The first version should ship with at least three scenario presets.

### 19.1 Airport Perimeter

Suggested characteristics:

- line of radar coverage
- EO confirmation positions
- RF awareness nodes

### 19.2 Coastal or Fishery Site

Suggested characteristics:

- coastal geometry
- tower EO
- long-view sensing
- broader RF awareness

### 19.3 Industrial Facility

Suggested characteristics:

- compact protected area
- multiple overlapping sensing devices
- obvious zone boundaries

Each scenario should be switchable from the UI.

## 20. Required Screens

This project does not need many pages.

It needs a small number of strong, useful screens.

Recommended screen set:

1. Intro or landing screen
2. Main Horizon demo screen
3. Device configuration drawer or panel
4. Scenario and layer control area
5. Optional event or timeline panel

The main Horizon demo screen is the most important screen in the project.

## 21. Main Demo Screen Requirements

The main screen should include:

- top app shell or header
- large map area
- scenario controls
- layer visibility controls
- selected device detail or edit drawer
- optional playback or demo control strip

The layout should prioritize map and sensing logic over dashboard card clutter.

## 22. Interaction Requirements

### 22.1 Layer Controls

The user should be able to toggle:

- radar layer
- EO layer
- spectrum layer
- device labels
- range rings
- optional event markers

### 22.2 Scenario Controls

The user should be able to:

- switch scenarios
- reset current scenario
- restore default camera framing

### 22.3 Device Editing

The user should be able to:

- select a device
- inspect its parameters
- change coordinates
- change heading
- change radius
- change sector angle
- change radar RPM

### 22.4 Animation Controls

The user should be able to:

- pause or resume demo animation if useful
- reset animated state
- optionally adjust radar motion speed globally for presentation purposes

## 23. Optional Modules Worth Including

These are not mandatory but may improve demo quality significantly.

### 23.1 Event Timeline

A lightweight event stream could show:

- sensor trigger
- fused alert
- acknowledgement or workflow state

### 23.2 Track Simulation

Simple simulated moving targets can make the map feel much more alive.

This is especially useful if:

- radar sees the moving object
- EO direction aligns with it
- spectrum coverage also overlaps the scene

### 23.3 Guided Story Mode

A guided presentation mode is recommended.

Example sequence:

1. show the site
2. reveal radar layer
3. reveal EO layer
4. reveal RF layer
5. emphasize the unified Horizon value

### 23.4 Device Library

The user may be allowed to add demo devices from a simple library:

- radar
- EO
- spectrum node

## 24. Suggested Internal Data Model

Even though this is frontend-only, the internal model should still be clean.

Recommended types:

- `Scenario`
- `Site`
- `MapCameraPreset`
- `Device`
- `RadarDevice`
- `OpticalDevice`
- `SpectrumDevice`
- `CoverageConfig`
- `Track`
- `Event`
- `LayerVisibilityState`

## 25. Deliverables

The first reviewable project should include:

1. Working frontend application
2. Local demo data
3. At least three scenario presets
4. Smooth radar animation
5. EO and spectrum coverage visualization
6. Basic device editing UI
7. README with setup and run instructions
8. Static production build output

## 26. Acceptance Criteria

The first version is successful if:

1. It runs as a pure frontend project
2. It can be built and distributed as static assets
3. Google Maps loads correctly
4. Street and satellite switching works
5. Devices can be placed and edited by latitude and longitude
6. Radar scan animation is smooth and visually convincing
7. EO coverage and spectrum coverage are visible and clearly different from radar
8. Scenario switching works
9. The interface is polished enough for demo use
10. A new engineer reading only this document can understand the product context and begin implementation

## 27. Recommended Build Order

Recommended implementation order:

1. app shell and Google Maps integration
2. scenario data model
3. device placement and editing
4. radar coverage and radar animation
5. EO and spectrum overlays
6. scenario switching and layer controls
7. optional event and track presentation
8. visual polish

## 28. Final Recommendation

The new Horizon project should be built as:

- a pure frontend demo
- a static-build friendly application
- a Google Maps-based multi-sensor site visualization
- a product-quality prototype using local demo data

The most important thing is not backend complexity.

The most important thing is to create a convincing Horizon experience that clearly demonstrates:

- unified site awareness
- multi-sensor layering
- device placement logic
- radar scan behavior
- Cyrentis product thinking

This document should be sufficient to start that project in a new repository without relying on the current chat history.
