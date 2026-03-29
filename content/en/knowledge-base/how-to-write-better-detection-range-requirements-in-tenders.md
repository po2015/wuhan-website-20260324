---
title: "How to Write Better Detection-Range Requirements in Tenders"
slug: "how-to-write-better-detection-range-requirements-in-tenders"
url: "/knowledge-base/how-to-write-better-detection-range-requirements-in-tenders/"
description: "A practical tender-writing guide for turning vague detection-range language into measurable requirements tied to target, task, geometry, and acceptance criteria."
seo_title: "How to Write Better Detection-Range Requirements in Tenders"
seo_description: "Learn how to write better detection-range requirements in tenders by defining target assumptions, task thresholds, geometry, and site acceptance logic."
keywords:
  - "how to write better detection-range requirements in tenders"
  - "detection range tender requirements"
  - "security tender detection range"
  - "how to specify detection range"
  - "range requirements procurement guide"
categories:
  - "Compliance"
  - "System Design"
tags:
  - "Detection Range"
  - "Tender Writing"
  - "Acceptance Testing"
  - "DRI Criteria"
image: "/images/knowledge-base/how-to-write-better-detection-range-requirements-in-tenders-cover.jpg"
image_alt: "A person working on a technical blueprint, used as a lead visual for an article about writing better detection-range requirements in tenders."
image_source_name: "Pilan Filmes"
image_source_url: "https://www.pexels.com/photo/an-architect-working-on-a-blueprint-11269741/"
weight: 102
date: 2026-06-24
lastmod: 2026-03-29T10:00:00+08:00
draft: false
keypoints:
  - "A range requirement is weak if it does not define the target, the task, the geometry, and the acceptance conditions."
  - "Detection, tracking, recognition, and identification are different performance questions and should not be collapsed into one headline number."
  - "Good tenders specify probability, false-alarm behavior, line of sight, and environmental assumptions instead of only asking for the maximum range."
  - "The strongest range clauses are tied directly to site acceptance testing so the buyer can prove whether the delivered system matches the procurement language."
---

Many security tenders ask for a detection range in a way that sounds precise but is not actually measurable. A clause might say that the system must detect a drone at 5 kilometers, a person at 2 kilometers, or a vehicle at long range. The wording looks technical because it contains numbers, but it often leaves out the information needed to judge whether the number means anything operationally.

That is how procurement creates avoidable conflict. The vendor thinks the tender is asking for a nominal instrument figure under one set of assumptions. The buyer thinks the tender is asking for dependable field performance under site conditions that were never written down. The acceptance phase then becomes a dispute about meaning rather than a test of delivery.

Better range language solves this by forcing the tender to state what the system is actually expected to do. Which target? Under what scene conditions? At what probability? For detection only, or for tracking, recognition, or identification? And in what geometry? Once those questions are written clearly, range stops being a brochure number and becomes an engineering requirement.

## Range Requirements Fail When the Task Is Missing

The most common drafting error is to ask for range without asking for the task at that range.

That matters because "seeing something" can mean very different things. MIT Lincoln Laboratory's radar teaching material makes this clear in radar language: the radar equation, clutter, propagation, and detection in noise all shape how range should be understood in system design. NASA's EO/IR surveillance-range work makes the same point from the optical side: performance is not a single distance, but a relationship between warning time, geometry, field of regard, and the visual task the sensor must support.

So a tender should first ask what the range number is supposed to represent:

- initial detection,
- sustained tracking,
- recognition or classification,
- identification,
- or alerting time before a required response action.

If the clause does not answer that question, the buyer is inviting ambiguity.

For example, a radar that can detect a target at a certain distance may not maintain a stable track at the same distance in clutter. An EO/IR payload may detect at a distance far beyond where it can recognize or identify. A Remote ID receiver may receive a cooperative broadcast at one range while a generic RF layer sees a different operational envelope entirely. One word, "range," cannot hold all those meanings at once.

## Define the Target Assumption Explicitly

A good range requirement also defines the target being used for the claim.

That usually means stating:

- target class,
- target size or relevant dimension,
- target observability characteristics,
- expected altitude or approach profile,
- and whether the target is cooperative, non-cooperative, or emitting.

The buyer does not need to write a dissertation, but the target cannot remain generic. A small drone, a person, a vehicle, and a small craft create different sensing problems. Even within one class, the result changes with payload, orientation, speed, and background.

For EO/IR clauses, the classic DRI and Johnson-criteria tradition is useful because it forces the range claim to be tied to a task and a target dimension instead of a loose idea of visibility. For radar clauses, the same principle applies even if the vocabulary is different. Range must be connected to target assumptions and to the performance threshold being claimed.

A stronger tender phrase looks like this:

"The system shall detect a small low-altitude aerial target of defined size under the stated test geometry with the probability and false-alarm limits described below."

That wording is much harder to misunderstand than:

"The system shall detect drones at 5 km."

## Separate Detection, Tracking, Recognition, and Identification

The next mistake is collapsing multiple performance problems into one line item.

At minimum, a tender should separate:

- detection range,
- track-maintenance conditions,
- recognition or classification distance where relevant,
- and identification or confirmation distance where relevant.

These are not interchangeable.

NASA's detect-and-avoid EO/IR work is especially helpful here because it frames sensor usefulness in terms of alerting time and surveillance task, not only maximum reach. That perspective transfers directly to civil security. A long nominal range is meaningless if the system cannot provide a stable enough track or a usable confirmation path for the operator to act.

This is why tenders should avoid phrases such as:

- "detection and identification range,"
- "effective monitoring range,"
- or "full-range warning and confirmation"

unless the clause then breaks those terms apart into measurable subrequirements.

If the project needs multiple layers, the tender should say so directly. For example:

- radar detection range,
- optical recognition range after cueing,
- and verification time from first alert to operator-readable image.

That produces a testable chain rather than one inflated headline promise.

## State Geometry and Environment, Not Only Distance

Range is never independent of geometry.

The tender should specify, where relevant:

- expected approach direction,
- expected altitude or elevation band,
- line-of-sight assumptions,
- mounting-height assumptions,
- and masking conditions that are known to matter.

If the site includes berms, rooflines, trees, cranes, service buildings, or shoreline structures, then a pure distance requirement is incomplete. The system may satisfy the number in one sector and fail in the sector that actually matters most.

Environmental assumptions also matter. A range claim without scene context often produces a dispute later about whether the trial was fair. The tender should therefore say whether the claimed performance is expected:

- in clear daytime conditions only,
- day and night,
- in light haze or light fog,
- in rain exclusions,
- or under another declared environmental envelope.

The goal is not to demand impossible universality. The goal is to stop the system from being accepted on one set of conditions and expected to operate later under another.

## Require Probability, False-Alarm Behavior, and Update Logic

A range requirement is also weak if it never states the performance threshold.

For radar or other detection sensors, the tender should consider stating:

- probability of detection,
- false-alarm behavior or false-alarm constraints,
- track update or revisit behavior,
- and the persistence needed before an alarm is considered valid.

This matters because a vendor can often increase visible sensitivity by accepting more nuisance behavior. Without a false-alarm boundary or tracking condition, the buyer may unknowingly reward the wrong design compromise.

For EO/IR confirmation layers, the equivalent requirement may be framed differently:

- recognition task,
- identification task,
- field of view or zoom state,
- stabilization assumptions,
- and the time available after cueing.

The important point is that the tender should name the quality threshold, not only the distance.

In procurement language, that often means replacing a single number with a compact requirement bundle:

- target,
- task,
- range,
- probability or confidence threshold,
- false-alarm or nuisance boundary,
- and test context.

## Tie the Tender to Site Acceptance Testing

The strongest range requirement is the one that already hints at how it will be tested.

A tender should say, at least at a high level:

- which scenarios will be used for acceptance,
- what constitutes a valid run,
- how many repetitions are expected,
- which environmental conditions invalidate the test,
- what evidence must be logged,
- and how the operator workflow is included if the system is not a standalone sensor.

This is especially important for multi-sensor projects. A buyer may procure a perimeter system, not a single detector. In that case, the acceptance test should not only ask whether one sensor produced a hit. It should ask whether the delivered system:

- detected,
- tracked or localized as required,
- opened the right operator context,
- and supported the decision path promised in the tender.

That change in drafting discipline eliminates many arguments later. The system is no longer being judged against an implied expectation. It is being judged against the same operational question that justified the procurement.

## Bad Tender Phrases and Better Replacements

Weak range clauses usually sound impressive because they are short.

### Weak

"The system shall detect drones at 5 km."

### Better

"The system shall provide initial detection of the defined aerial target under the stated geometry and environmental conditions, with declared probability and nuisance constraints, and shall support the verification workflow described in the acceptance section."

### Weak

"The camera shall identify a target at long range."

### Better

"The EO/IR subsystem shall meet the stated recognition or identification task for the defined target class at the declared zoom state and scene conditions, and shall be tested at site acceptance against those criteria."

### Weak

"The system shall provide all-weather long-distance monitoring."

### Better

"The tender shall distinguish between operating conditions in which the claimed performance is required, conditions in which degraded performance is acceptable, and conditions excluded from the acceptance claim."

The better versions are longer, but they are also much more defensible.

## Conclusion

Detection-range requirements in tenders become stronger when they stop pretending that one number can carry the whole engineering meaning. A useful clause defines the target, the task, the geometry, the quality threshold, and the acceptance context. That is what turns a range claim into a contract-ready requirement.

The practical takeaway is straightforward. Ask not only "how far?" Ask "for what target, doing what task, under what conditions, with what proof?" Once that language is written clearly, the system is much easier to buy, test, and defend.

## Related Reading

- [How to Select Detection Range](/knowledge-base/how-to-select-detection-range/)
- [How DRI Criteria Change EO/IR System Selection](/knowledge-base/how-dri-criteria-change-eo-ir-system-selection/)
- [What a Good Civil-Security Tender Should Ask About Verification, Not Just Detection](/knowledge-base/what-a-good-civil-security-tender-should-ask-about-verification-not-just-detection/)

## Official Reading

- [MIT Lincoln Laboratory: Introduction to Radar Systems](https://www.ll.mit.edu/outreach/online-course-radar-introduction-radar-systems)
- [NASA/TM-20210025061: Detect-and-Avoid Surveillance Range Requirements for EO/IR Sensors](https://ntrs.nasa.gov/api/citations/20210025061/downloads/20210025061_Wu_TM-EOIRSensors_manuscript%20%281%29.pdf)
- [Institute for Defense Analyses: Performance Model Tutorial](https://ida.org/~/media/corporate/files/publications/ida_documents/sed/ida-document-d-4642.pdf)
