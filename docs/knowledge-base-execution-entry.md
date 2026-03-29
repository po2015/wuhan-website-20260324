# Knowledge Base Execution Entry

This file is the single entry point for knowledge-base execution.

It keeps:

- the executable publishing schedule
- the `Planned -> PASS` execution progress
- the only required workflow constraint

## Fixed Rules

1. Writing skill: `professional-kb-articles`
2. After each article is written, send it through `article-review-loop`
3. If the result is `REQUIRE_REVISION` or `REQUIRE_REWRITE`, revise and run the loop again
4. Only `PASS` counts as completed

## Progress

### Completed

| Date | Topic | File | Review | Status |
| --- | --- | --- | --- | --- |
| 2026-04-01 | Remote ID vs Basic RF Detection: What Each Layer Actually Adds | `content/en/knowledge-base/remote-id-vs-basic-rf-detection.md` | `PASS` | Done |
| 2026-04-08 | How DRI Criteria Change EO/IR System Selection | `content/en/knowledge-base/how-dri-criteria-change-eo-ir-system-selection.md` | `PASS` | Done |
| 2026-04-15 | What Makes an RF Bearing Trustworthy in Real Sites? | `content/en/knowledge-base/what-makes-an-rf-bearing-trustworthy-in-real-sites.md` | `PASS` | Done |
| 2026-04-22 | How to Turn Sensor Alerts Into Operator Queues | `content/en/knowledge-base/how-to-turn-sensor-alerts-into-operator-queues.md` | `PASS` | Done |
| 2026-04-29 | Perimeter Zoning Strategy for Data Centers: Fence, Roofline, and Airspace | `content/en/knowledge-base/perimeter-zoning-strategy-for-data-centers-fence-roofline-and-airspace.md` | `PASS` | Done |
| 2026-05-06 | Console Layout and Screen Zoning for Multi-Sensor Operations | `content/en/knowledge-base/console-layout-and-screen-zoning-for-multi-sensor-operations.md` | `PASS` | Done |
| 2026-05-13 | What a Good Civil-Security Tender Should Ask About Verification, Not Just Detection | `content/en/knowledge-base/what-a-good-civil-security-tender-should-ask-about-verification-not-just-detection.md` | `PASS` | Done |
| 2026-05-20 | When a Verification Camera Needs Narrow FOV and When It Does Not | `content/en/knowledge-base/when-a-verification-camera-needs-narrow-fov-and-when-it-does-not.md` | `PASS` | Done |
| 2026-05-27 | False Alarm Escalation vs False Alarm Rate: Why They Are Not the Same KPI | `content/en/knowledge-base/false-alarm-escalation-vs-false-alarm-rate-why-they-are-not-the-same-kpi.md` | `PASS` | Done |
| 2026-06-03 | PTZ vs Fixed Thermal Cameras for Perimeter Projects | `content/en/knowledge-base/ptz-vs-fixed-thermal-cameras-for-perimeter-projects.md` | `PASS` | Done |
| 2026-06-09 | How to Choose Focal Length for Long-Range Surveillance | `content/en/knowledge-base/how-to-choose-focal-length-for-long-range-surveillance.md` | `PASS` | Done |
| 2026-06-10 | AOA vs TDOA vs FDOA: Which RF Geolocation Method Fits Which Project? | `content/en/knowledge-base/aoa-vs-tdoa-vs-fdoa-which-rf-geolocation-method-fits-which-project.md` | `PASS` | Done |
| 2026-06-16 | Alert Triage Design for Multi-Sensor Security Platforms | `content/en/knowledge-base/alert-triage-design-for-multi-sensor-security-platforms.md` | `PASS` | Done |
| 2026-06-17 | Data Center Perimeter Security System Design | `content/en/knowledge-base/data-center-perimeter-security-system-design.md` | `PASS` | Done |
| 2026-06-23 | How to Reduce False Alarms Without Slowing Response | `content/en/knowledge-base/how-to-reduce-false-alarms-without-slowing-response.md` | `PASS` | Done |
| 2026-06-24 | How to Write Better Detection-Range Requirements in Tenders | `content/en/knowledge-base/how-to-write-better-detection-range-requirements-in-tenders.md` | `PASS` | Done |
| 2026-06-30 | Visible + Thermal Camera Pairing: When Dual-Sensor Payloads Matter | `content/en/knowledge-base/visible-and-thermal-camera-pairing-when-dual-sensor-payloads-matter.md` | `PASS` | Done |
| 2026-07-01 | Remote ID Reception Range: What Actually Changes It? | `content/en/knowledge-base/remote-id-reception-range-what-actually-changes-it.md` | `PASS` | Done |

### Next Planned

| Date | Topic | Target File | Status |
| --- | --- | --- | --- |
| 2026-07-07 | What Makes a Good Control Room Layout for Multi-Sensor Operations? | `content/en/knowledge-base/what-makes-a-good-control-room-layout-for-multi-sensor-operations.md` | Planned |
| 2026-07-08 | Substation and Power Grid Perimeter Monitoring | `content/en/knowledge-base/substation-and-power-grid-perimeter-monitoring.md` | Planned |
| 2026-07-14 | What Limits Thermal Detection in Humidity, Rain, and Haze? | `content/en/knowledge-base/what-limits-thermal-detection-in-humidity-rain-and-haze.md` | Planned |
| 2026-07-15 | How RF Antenna Placement Changes Detection and Bearing Accuracy | `content/en/knowledge-base/how-rf-antenna-placement-changes-detection-and-bearing-accuracy.md` | Planned |
| 2026-07-21 | Data Retention Design for Security Events, Tracks, and Evidence | `content/en/knowledge-base/data-retention-design-for-security-events-tracks-and-evidence.md` | Planned |

## Publishing Schedule

### Schedule Rules

- `2026-03-31` through `2026-12-30`: publish on **Tuesday and Wednesday** each week
- `2027-01-06` onward: switch to **one article every Wednesday**

### 2026 Publishing Table

| Date | Day | Status | Category | Topic |
| --- | --- | --- | --- | --- |
| 2026-03-31 | Tue | Scheduled | Counter-UAS, System Design | How to Design a Drone Detection System |
| 2026-04-01 | Wed | PASS | Digital RF | Remote ID vs Basic RF Detection: What Each Layer Actually Adds |
| 2026-04-07 | Tue | Scheduled | Counter-UAS, System Design | Radar + EO + RF Integration Guide |
| 2026-04-08 | Wed | PASS | Technology Basics | How DRI Criteria Change EO/IR System Selection |
| 2026-04-14 | Tue | Scheduled | Radar Planning, System Design | Choosing the Right Radar System |
| 2026-04-15 | Wed | PASS | Digital RF | What Makes an RF Bearing Trustworthy in Real Sites? |
| 2026-04-21 | Tue | Scheduled | Radar Planning, System Design | How to Select Detection Range |
| 2026-04-22 | Wed | PASS | System Design | How to Turn Sensor Alerts Into Operator Queues |
| 2026-04-28 | Tue | Scheduled | Deployment, System Design | Fixed vs Mobile Surveillance Systems |
| 2026-04-29 | Wed | PASS | Deployment | Perimeter Zoning Strategy for Data Centers: Fence, Roofline, and Airspace |
| 2026-05-05 | Tue | Scheduled | Counter-UAS, System Design | System Architecture for Low-Altitude Security |
| 2026-05-06 | Wed | PASS | System Design | Console Layout and Screen Zoning for Multi-Sensor Operations |
| 2026-05-12 | Tue | Scheduled | System Design, Deployment | Centralized Command Platform Design |
| 2026-05-13 | Wed | PASS | Compliance | What a Good Civil-Security Tender Should Ask About Verification, Not Just Detection |
| 2026-05-19 | Tue | Scheduled | System Design, Deployment | Data Fusion System Design |
| 2026-05-20 | Wed | PASS | Technology Basics | When a Verification Camera Needs Narrow FOV and When It Does Not |
| 2026-05-26 | Tue | Scheduled | System Design, Machine Vision | AI Integration in Security Systems |
| 2026-05-27 | Wed | PASS | System Design | False Alarm Escalation vs False Alarm Rate: Why They Are Not the Same KPI |
| 2026-06-02 | Tue | Scheduled | System Design, Deployment | Real-Time Monitoring Systems |
| 2026-06-03 | Wed | PASS | Technology Basics | PTZ vs Fixed Thermal Cameras for Perimeter Projects |
| 2026-06-09 | Tue | PASS | System Design | How to Choose Focal Length for Long-Range Surveillance |
| 2026-06-10 | Wed | PASS | Digital RF | AOA vs TDOA vs FDOA: Which RF Geolocation Method Fits Which Project? |
| 2026-06-16 | Tue | PASS | System Design | Alert Triage Design for Multi-Sensor Security Platforms |
| 2026-06-17 | Wed | PASS | Deployment | Data Center Perimeter Security System Design |
| 2026-06-23 | Tue | PASS | System Design | How to Reduce False Alarms Without Slowing Response |
| 2026-06-24 | Wed | PASS | Compliance | How to Write Better Detection-Range Requirements in Tenders |
| 2026-06-30 | Tue | PASS | Technology Basics | Visible + Thermal Camera Pairing: When Dual-Sensor Payloads Matter |
| 2026-07-01 | Wed | PASS | Digital RF | Remote ID Reception Range: What Actually Changes It? |
| 2026-07-07 | Tue | Planned | System Design | What Makes a Good Control Room Layout for Multi-Sensor Operations? |
| 2026-07-08 | Wed | Planned | Deployment | Substation and Power Grid Perimeter Monitoring |
| 2026-07-14 | Tue | Planned | Technology Basics | What Limits Thermal Detection in Humidity, Rain, and Haze? |
| 2026-07-15 | Wed | Planned | Digital RF | How RF Antenna Placement Changes Detection and Bearing Accuracy |
| 2026-07-21 | Tue | Planned | System Design | Data Retention Design for Security Events, Tracks, and Evidence |
| 2026-07-22 | Wed | Planned | Export Control | What an Export-Ready Security Sensor Datasheet Should Include |
| 2026-07-28 | Tue | Planned | System Design | How to Design a Sensor Health Monitoring Workflow |
| 2026-07-29 | Wed | Planned | Digital RF | What Causes RF Multipath and Bearing Error in Urban Sites? |
| 2026-08-04 | Tue | Planned | System Design | Latency Budgets in Multi-Sensor Systems: Why Seconds Matter |
| 2026-08-05 | Wed | Planned | Deployment | Solar Farm Security Monitoring: Geometry, Power, and Communications |
| 2026-08-11 | Tue | Planned | Technology Basics | How Stabilization Affects Long-Range EO Tracking |
| 2026-08-12 | Wed | Planned | Digital RF | Passive RF Detection vs Protocol Decoding: What Do You Actually Get? |
| 2026-08-18 | Tue | Planned | Compliance | FAT vs SAT in Security Projects: What Changes Between Factory and Site |
| 2026-08-19 | Wed | Planned | Technology Basics | How to Estimate Camera Identification Range for People, Vehicles, and Small Craft |
| 2026-08-25 | Tue | Planned | Counter-UAS | How to Plan RF Coverage for Drone Detection Around Buildings |
| 2026-08-26 | Wed | Planned | System Design | Network Topology for Distributed Sensor Sites: Fiber, Wireless, and Redundancy |
| 2026-09-01 | Tue | Planned | Deployment | Warehouse and Logistics Park Surveillance Design |
| 2026-09-02 | Wed | Planned | System Design | Why Narrow FOV and Wide FOV Need to Work Together in EO Verification |
| 2026-09-08 | Tue | Planned | Compliance | Spectrum Monitoring vs Communications Intelligence: Where the Line Is for Civil Projects |
| 2026-09-09 | Wed | Planned | System Design | API vs SDK vs Protocol Gateways in Security System Integration |
| 2026-09-15 | Tue | Planned | Deployment | Border River and Canal Monitoring Design |
| 2026-09-16 | Wed | Planned | Technology Basics | How EO Auto-Tracking Works and Where It Fails |
| 2026-09-22 | Tue | Planned | Counter-UAS | What Makes Non-Cooperative Drone Detection Hard in RF Systems? |
| 2026-09-23 | Wed | Planned | System Design | Acceptance Testing for Multi-Sensor Projects: What Should Be Verified On Site? |
| 2026-09-29 | Tue | Planned | Compliance | Radar + EO + RF Bill of Materials: How to Scope an Early Budget |
| 2026-09-30 | Wed | Planned | Technology Basics | When Cooled Thermal Actually Pays Off in Infrastructure Projects |
| 2026-10-06 | Tue | Planned | Counter-UAS | How 2.4 GHz and 5.8 GHz Conditions Change Counter-UAS RF Performance |
| 2026-10-07 | Wed | Planned | System Design | Operator Handover Design Between Shifts and Teams |
| 2026-10-13 | Tue | Planned | Deployment | Bridge and Elevated Corridor Surveillance |
| 2026-10-14 | Wed | Planned | Technology Basics | Lens Selection for EO/IR Payloads: Zoom, Aperture, and Sensor Size |
| 2026-10-20 | Tue | Planned | Digital RF | RF Detection in Ports and Coastal Sites: Noise, Reflections, and Layout |
| 2026-10-21 | Wed | Planned | System Design | Alarm Escalation Logic: From Detection to Verification to Response |
| 2026-10-27 | Tue | Planned | Emerging Sensors | When mmWave 4D Imaging Radar Matters Outside Automotive |
| 2026-10-28 | Wed | Planned | System Design | Day/Night Verification Workflow for Radar-Cued EO Systems |
| 2026-11-03 | Tue | Planned | Deployment | Reservoir and Dam Perimeter Monitoring |
| 2026-11-04 | Wed | Planned | Counter-UAS | How to Fuse Remote ID, RF Bearings, and Radar Tracks |
| 2026-11-10 | Tue | Planned | Technology Watch | Photonic Radar: What Is Hype and What Is Practical? |
| 2026-11-11 | Wed | Planned | System Design | Multi-Site Command Architecture for Regional Security Operations |
| 2026-11-17 | Tue | Planned | Deployment | Mining Site Security Monitoring |
| 2026-11-18 | Wed | Planned | Civil Applications | Shoreline and Maritime EO Challenges: Glint, Humidity, and Horizon |
| 2026-11-24 | Tue | Planned | Technology Watch | Cognitive Radar for Civil Security: What Could Arrive First? |
| 2026-11-25 | Wed | Planned | System Design | How to Plan Storage for Video, Tracks, and RF Event History |
| 2026-12-01 | Tue | Planned | Deployment | Temporary Event Venue Monitoring Beyond Counter-UAS |
| 2026-12-02 | Wed | Planned | Digital RF | What Buyers Should Ask About RF Libraries, Protocol Updates, and Maintenance |
| 2026-12-08 | Tue | Planned | Technology Watch | Low Earth Orbit SAR Constellations: What Civil Buyers Should Actually Care About |
| 2026-12-09 | Wed | Planned | Technology Basics | What Causes Thermal False Alarms in Real Projects? |
| 2026-12-15 | Tue | Planned | Deployment | Industrial Port Entry and Waterside Surveillance |
| 2026-12-16 | Wed | Planned | System Design | What to Standardize First in a Growing Security Platform |
| 2026-12-22 | Tue | Planned | Deployment | Campus Low-Altitude Security Design |
| 2026-12-23 | Wed | Planned | Technology Watch | Quantum Radar Claims: How to Read Them Without Getting Misled |
| 2026-12-29 | Tue | Planned | Deployment | Airport Landside vs Airside Detection Workflow |
| 2026-12-30 | Wed | Planned | System Design | How to Split Responsibilities Between Local Sites and Central Command |

### 2027 First 25 Weekly Wednesday Articles

| Date | Day | Status | Category | Topic |
| --- | --- | --- | --- | --- |
| 2027-01-06 | Wed | Planned | Technology Basics | Understanding NETD, Lens Size, and Scene Contrast in Thermal Imaging |
| 2027-01-13 | Wed | Planned | Digital RF | How RF Sensor Baselines Change Geolocation Accuracy |
| 2027-01-20 | Wed | Planned | Deployment | Industrial Park Perimeter Monitoring Beyond the Fence Line |
| 2027-01-27 | Wed | Planned | System Design | What Makes a Good Incident Replay Workflow for Security Platforms |
| 2027-02-03 | Wed | Planned | Counter-UAS | When Drone Detection Needs More Than One RF Site |
| 2027-02-10 | Wed | Planned | Deployment | Pumping Station and Valve Site Monitoring for Pipeline Networks |
| 2027-02-17 | Wed | Planned | Compliance | How to Compare Detection, Classification, and Verification KPIs in Acceptance Tests |
| 2027-02-24 | Wed | Planned | Technology Basics | How Seasonal Temperature Changes Affect Thermal Detection |
| 2027-03-03 | Wed | Planned | Digital RF | Geolocation Confidence Scoring for RF Events |
| 2027-03-10 | Wed | Planned | System Design | How to Design an Incident Timeline for Radar, EO, and RF Evidence |
| 2027-03-17 | Wed | Planned | Deployment | Mast Height Planning for EO, RF, and Radar Sensors |
| 2027-03-24 | Wed | Planned | Counter-UAS | When Remote ID Still Needs Radar or EO Confirmation |
| 2027-03-31 | Wed | Planned | System Design | Maintenance Planning for Distributed Sensor Networks |
| 2027-04-07 | Wed | Planned | Deployment | Port Crane, Yard, and Waterside Blind Spots in Security Design |
| 2027-04-14 | Wed | Planned | Technology Basics | Understanding Pixel Pitch, F-Number, and Focal Length in EO/IR Selection |
| 2027-04-21 | Wed | Planned | Digital RF | Friendly Emitters, Whitelists, and RF Environment Baselines |
| 2027-04-28 | Wed | Planned | System Design | Time Synchronization in Multi-Sensor Fusion: Why Timestamps Break Systems |
| 2027-05-05 | Wed | Planned | Deployment | Railway Corridor Monitoring Beyond Station Perimeters |
| 2027-05-12 | Wed | Planned | Technology Watch | How to Evaluate Vendor Claims Around AI Detection Models |
| 2027-05-19 | Wed | Planned | Technology Watch | Passive Radar for Civil Security: Where It Can Fit and Where It Cannot |
| 2027-05-26 | Wed | Planned | Digital RF | What Makes an RF Signal Library Maintainable Over Time |
| 2027-06-02 | Wed | Planned | Deployment | Waterfront Industrial Security: Radar, EO, and Lighting Coordination |
| 2027-06-09 | Wed | Planned | System Design | Designing Escalation Rules for Shared Regional Command Centers |
| 2027-06-16 | Wed | Planned | Technology Basics | Range, Bearing, and Video: How Operators Learn to Trust Combined Cues |
| 2027-06-23 | Wed | Planned | Counter-UAS | How to Handle Friendly Drone Operations Inside a Protected Site |
