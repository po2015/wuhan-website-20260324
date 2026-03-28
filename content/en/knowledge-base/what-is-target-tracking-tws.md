---
title: "What is Target Tracking (TWS)?"
slug: "what-is-target-tracking-tws"
url: "/knowledge-base/what-is-target-tracking-tws/"
description: "A beginner-friendly explanation of radar target tracking and track-while-scan, including how systems maintain tracks while still searching the wider scene."
seo_title: "What is Target Tracking (TWS)? Beginner Guide"
seo_description: "Learn what target tracking and track-while-scan mean in radar, how TWS works, and why tracking is different from simple detection."
keywords:
  - "what is target tracking tws"
  - "track while scan explained"
  - "radar tracking basics"
  - "tws radar"
  - "target tracking explained"
categories:
  - "Foundation"
tags:
  - "Target Tracking"
  - "TWS"
  - "Radar Basics"
  - "Tracking"
image: "/images/knowledge-base/what-is-target-tracking-tws-cover.svg"
image_alt: "A technical illustration of a radar maintaining several target tracks while continuing to scan the wider scene."
image_source_name: ""
image_source_url: ""
weight: 43
date: 2026-01-21
lastmod: 2026-03-27T20:15:00+08:00
draft: false
keypoints:
  - "Target tracking means maintaining a continuous estimate of a target's position and motion over time."
  - "Track-while-scan lets a radar keep searching while also updating existing tracks."
  - "Tracking requires prediction, correlation, and repeated updates, not just one detection."
  - "Good tracking depends on revisit rate, clutter conditions, and track-management logic."
---

What is target tracking in radar? Target tracking means maintaining a continuing estimate of where a target is, how it is moving, and where it is likely to be next.

That is different from simple detection. A detection says, "something was seen here." A track says, "this is the same object over time, and the system is following it."

When people say `TWS`, they usually mean **track-while-scan**. That is a radar operating idea in which the system keeps searching the wider scene while also updating known tracks.

## Detection vs Tracking

This distinction matters more than many beginners expect.

A single detection may be:

- momentary,
- noisy,
- or ambiguous.

Tracking tries to connect multiple observations together so the system can build continuity. That continuity is what makes the detection operationally useful.

## How Track-While-Scan Works

A track-while-scan radar does not stop scanning the scene just because it already found something interesting. Instead, it divides its attention.

In broad terms, the cycle looks like this:

1. search the wider scene,
2. detect candidate targets,
3. create or update track files,
4. predict where tracked targets should appear next,
5. and revisit them during later scans.

![How track-while-scan maintains tracks](/images/knowledge-base/what-is-target-tracking-tws-how-tracks-are-maintained.svg)

*Figure: Synthesized explanatory diagram showing how detections become maintained tracks in a track-while-scan workflow. It is an educational illustration, not a radar console capture.*

This allows one radar to keep broad awareness while still paying extra attention to targets it already cares about.

## What a Track File Really Is

Behind the scenes, tracking software usually keeps a stored record for each target. That record may include things like:

- estimated position,
- estimated velocity,
- update history,
- confidence or track quality,
- and prediction data for the next expected observation.

This stored record is often called a **track file**.

The beginner point is simple: tracking is partly a sensing problem, but also very much a software and estimation problem.

## How Tracks Start, Continue, and End

Tracking is not just a single loop. A real tracker usually has to decide:

- when a new detection should become a new track,
- when a missing update should be tolerated,
- when the system should predict through temporary loss,
- and when a track should be dropped as unreliable or stale.

That means target tracking always includes some form of initiation, maintenance, coasting, and termination logic. If those rules are weak, the radar may create too many false tracks, keep stale tracks alive too long, or lose real targets too quickly.

## Why TWS Is Useful

Track-while-scan is useful because operators rarely want a radar that can only do one thing at a time.

They usually want the system to:

- keep looking for new targets,
- continue following known targets,
- prioritize the most important ones,
- and support cueing, display, or decision workflows.

TWS is one of the classic ways to support that balance.

## What Makes Tracking Hard

Tracking sounds straightforward until the environment gets messy.

Several things can make tracks unstable:

- clutter,
- low revisit rate,
- closely spaced targets,
- abrupt target maneuvers,
- temporary missed detections,
- and poor correlation logic.

If the radar revisits too slowly or if the target picture is too noisy, the tracker may lose confidence, coast incorrectly, or confuse one target with another.

## Revisit Rate Is Important, but Not Sufficient

Fast updates help, but good tracking is not just about update speed.

It also depends on:

- how well the radar measures target position,
- how stable the track filters are,
- how the system handles missed observations,
- and how it decides whether a new hit belongs to an old track or a new one.

This is why tracking quality often tells you more about a radar system than the raw word "tracking" in a feature list.

## Why a Big TWS Number Is Not the Whole Story

Datasheets sometimes emphasize how many tracks a radar can maintain. That figure can be useful, but it is not a complete quality metric.

A large TWS number does not tell you by itself:

- how often each target is updated,
- how stable those tracks remain in clutter,
- whether the radar is preserving full search coverage,
- or how the tracker behaves when the scene becomes crowded.

The better question is not only how many tracks exist. It is how much tracking quality the system preserves while still doing its search mission.

## Why Tracking Matters to the Rest of the System

Tracking is not valuable only inside the radar. Stable tracks support camera cueing, fusion, alert prioritization, and operator confidence. If tracking quality is poor, the wider system becomes harder to trust even when the radar is still producing detections.

That is why tracking should be treated as an operational output, not only as an internal radar feature.

## Where TWS Fits in Real Systems

Track-while-scan is common in surveillance and air-defense history, but the underlying idea appears much more broadly: maintain awareness while continuing to search.

In modern systems, that idea often connects directly to:

- operator displays,
- automatic alerts,
- EO cueing,
- fusion engines,
- and prioritization of higher-interest tracks.

That is why even a beginner article on TWS should treat it as both a radar behavior and a workflow enabler.

## A Good Beginner Mental Model

The easiest way to think about TWS is this:

it is the radar's way of **remembering and predicting** while still watching the wider scene.

That memory is what turns isolated detections into something an operator can act on.

That is also why tracking quality should be tested under realistic clutter, crossing targets, and temporary missed detections rather than judged only from quiet demonstration scenes.

## Official Reading

- [NTIA: Characteristics of Federal Radar Systems](https://www.ntia.doc.gov/sites/default/files/publications/ntia00-40_0.pdf) - Useful for formal radar terminology and track-while-scan context in federal radar systems.
- [MIT Lincoln Laboratory: Introduction to Radar Systems](https://www.ll.mit.edu/outreach/online-course-radar-introduction-radar-systems) - Good foundation for understanding how radar tracking depends on the full sensing chain.
- [FAS / Fundamentals of Naval Weapons Systems, Chapter 6](https://man.fas.org/dod-101/navy/docs/fun/part06.htm) - Helpful for beginner-level tracking and search concepts in multifunction radar operations.
