---
title: "What is Radar Resolution?"
slug: "what-is-radar-resolution"
url: "/knowledge-base/what-is-radar-resolution/"
description: "A beginner-friendly guide to what radar resolution means, why range resolution and angular resolution are different, and how beamwidth, bandwidth, and geometry change what the radar can separate."
seo_title: "What is Radar Resolution? Beginner Guide"
seo_description: "Learn what radar resolution means, the difference between range and angular resolution, and why resolution is not the same as accuracy or detection range."
keywords:
  - "what is radar resolution"
  - "range resolution vs angular resolution"
  - "radar beamwidth explained"
  - "radar resolution basics"
  - "radar resolution vs accuracy"
categories:
  - "Foundation"
tags:
  - "Radar Resolution"
  - "Radar Basics"
  - "Beamwidth"
  - "Detection Geometry"
image: "/images/knowledge-base/what-is-radar-resolution-cover.svg"
image_alt: "Custom technical illustration showing radar range cells and beamwidth-driven angular separation."
image_source_name: ""
image_source_url: ""
weight: 92
date: 2025-09-29T09:00:00+08:00
lastmod: 2026-03-27T20:10:00+08:00
draft: false
keypoints:
  - "Radar resolution is the ability to separate two targets so they do not merge into one return or one cell of information."
  - "Range resolution and angular resolution are different: one is about separation along depth, the other is about separation across direction."
  - "A radar can detect a target at long range and still have weak resolution if the beam spreads or the resolution cell becomes too large."
  - "Resolution is not the same as accuracy. A radar may estimate location accurately while still being unable to separate nearby targets cleanly."
---

What is radar resolution? In simple terms, radar resolution is the radar's ability to tell that two nearby things are not actually one thing. If two targets are too close together for the radar to separate them, the radar may display them as one blob, one return, or one measurement cell. If the radar can distinguish them as separate, then its resolution is good enough for that situation.

This idea matters because beginners often focus on detection range first. Range is important, but it answers a different question. Range asks how far away the radar may detect something. Resolution asks how clearly the radar can separate details within what it detects. A radar may see far and still have trouble telling whether a return comes from one object or two. That is why high range does not automatically mean high resolution.

Official radar training material makes this clear. The National Weather Service radar training pages explain that two targets can only be resolved if they are separated enough in beamwidth and in range, and that the radar beam spreads with distance. FAA avian-radar guidance uses the idea operationally by specifying how far apart two standard avian targets must be before the system is considered able to resolve them. These are very different radar contexts, but they reinforce the same beginner lesson: resolution is about separation capability.

So the short answer is this: radar resolution is the ability to distinguish nearby targets or details instead of blending them into a single return. The practical question is what kind of separation the mission needs and how the radar's beam, pulse, and geometry affect that.

## What Radar Resolution Actually Means

At the beginner level, resolution means separation.

If two objects are close together, the radar may:

- display them as one return,
- smear them into one broader target,
- or separate them into two distinct detections.

The better the radar can separate nearby targets, the better its resolution is for that situation.

This sounds simple, but resolution is not just one number. In radar work, people often mean at least two different things:

- `range resolution`, which is separation along depth or distance from the radar,
- and `angular resolution`, sometimes described through beamwidth or cross-range separation, which is separation across direction.

These two are related but not identical. A radar may have good range resolution but only moderate angular resolution, or the opposite. That is why a single claim such as "high-resolution radar" can be too vague unless the context is clear.

For beginners, the safest mental model is that radar resolution describes the size of the detail cell the radar can separate. If two targets fall inside the same effective cell, they may merge. If they occupy different cells strongly enough, they can be distinguished.

## Range Resolution: Separating Targets in Depth

Range resolution is about telling apart two targets that lie at slightly different distances from the radar.

If one target is behind another along nearly the same direction, the radar needs enough resolution in range to show them as separate. If the range separation is too small, the returns overlap and appear as one.

National Weather Service radar training explains this in practical terms by discussing pulse length and beam geometry together. The same training notes that targets must be separated in range by more than about half the pulse length to be resolved. That is a useful beginner rule because it shows that range resolution is closely tied to the size of the radar's sampled distance cell.

In modern radar language, this is often linked to bandwidth as well. More bandwidth generally supports finer range resolution because the radar can discriminate smaller differences in delay between returning echoes. But even without diving deep into waveform mathematics, the beginner should remember the operational truth: range resolution asks whether two targets at different distances blend together or remain separate.

This matters in many scenarios:

- two vehicles on the same road axis,
- multiple birds or drones in a similar approach line,
- clutter plus a target behind it,
- or a shoreline scene where several returns stack up along the same radar direction.

If the radar cannot separate them in range, the operator gets less useful detail about what is really happening.

## Angular Resolution: Separating Targets Across Direction

Angular resolution is about telling apart two targets that are at similar range but slightly different directions.

This is where beamwidth becomes especially important. The NWS training material explains that, for a radar to detect two targets separately, the targets must be separated by more than the width of the beam at that range. That is a strong beginner lesson because it reveals why radar resolution usually gets worse with distance even if the nominal beamwidth angle stays the same. The beam spreads as it travels outward, so the patch of space covered by that beam becomes wider.

The Weather Service beam-property tools and radar training materials also show this visually: farther from the radar, the beam occupies a larger physical diameter. That means two nearby targets that might be separable at short range can blur together at longer range.

FAA avian-radar guidance makes the same point operational by requiring systems to differentiate two standard avian targets when separated by a specified distance in both range and azimuth. That is a procurement way of saying resolution must remain useful enough to distinguish multiple nearby objects, not just detect a general echo.

So if range resolution is about front-to-back separation, angular resolution is about side-to-side separation from the radar's point of view.

![How radar resolution works](/images/knowledge-base/what-is-radar-resolution-how-it-works.svg)

*Figure: Synthesized explainer showing how range separation and beamwidth-driven angular separation create different resolution limits in radar space.*

## Resolution Is Not the Same as Accuracy

This is one of the most common beginner mistakes.

`Accuracy` is about how close the radar's reported position is to the true position. `Resolution` is about whether the radar can distinguish two nearby targets from each other. A radar may report the position of a target quite accurately while still being unable to separate it cleanly from another nearby object.

Think of it this way:

- accuracy asks, "Did the radar place the return in the right spot?"
- resolution asks, "Did the radar understand that there were two things instead of one?"

Those are not the same question.

This distinction matters because a data sheet may list range accuracy, azimuth accuracy, or location accuracy, while the real operational challenge is target separation. If the mission involves multiple close targets, cluttered environments, or detailed discrimination, then resolution often deserves more attention than raw accuracy alone.

## Why Resolution Changes with Range

Beginners often assume the radar's resolution is a fixed property. In practice, part of it changes with geometry.

Angular resolution is the clearest example. The beamwidth may be fixed in degrees, but its physical footprint grows with distance. NWS training makes this easy to see by showing how the beam diameter becomes much larger at 50 or 100 nautical miles than it is close to the radar. That means the same radar can separate targets much better nearby than far away.

Range resolution can also interact with geometry and waveform choices. If the system's range cell is coarse relative to the scene, nearby targets along the same line of sight may merge. In addition, real scenes include clutter, multipath, and target motion, which can make practical separation harder than the simple textbook case suggests.

So the right beginner conclusion is that radar resolution depends partly on the radar design and partly on where in space the problem occurs.

## What Changes Radar Resolution

Several practical factors shape radar resolution quality.

### Bandwidth or Pulse Characteristics

Range resolution is strongly tied to the radar's transmitted signal properties. Shorter effective distance cells or greater usable bandwidth generally improve the radar's ability to separate returns in depth.

### Beamwidth

Angular resolution depends heavily on beamwidth. Narrower beams usually separate directional targets better than wider beams.

### Range to Target

Because the beam spreads with distance, directional separation gets harder at longer range. This is one reason why far-range tracks can appear broader, blockier, or more merged.

### Signal Processing and Display Logic

The operator does not see raw physics alone. The radar's processing, track association, thresholding, and display choices affect how clearly multiple targets remain separate.

### Target Size and Contrast

If one target is strong and another is weak, the stronger return may dominate the display or complicate separation. Resolution is therefore not only geometry. Signal strength matters too.

### Environment and Clutter

Terrain, precipitation, sea clutter, buildings, and ground returns can hide or smear fine structure. The radar may have good nominal resolution and still perform poorly in a difficult scene.

![What changes radar resolution](/images/knowledge-base/what-is-radar-resolution-what-changes-it.svg)

*Figure: Synthesized factor map showing why radar resolution depends on waveform, beamwidth, range, signal processing, target contrast, and clutter conditions.*

For beginners, this means resolution should be treated as both a design parameter and a scene-dependent operational result.

## Why Resolution Matters in Real Operations

Resolution changes what the radar picture can tell the operator.

If the mission only needs coarse awareness that "something is out there," moderate resolution may be acceptable. But if the operator needs to understand whether one return is really several objects, or whether a drone is separated from nearby clutter, resolution becomes much more important.

Examples include:

- distinguishing multiple targets in a corridor,
- separating a low-altitude target from background clutter,
- understanding whether one track is actually a pair of closely spaced tracks,
- and deciding how much confidence to place in a radar image or track list.

This is why radar resolution often connects directly to downstream tasks such as classification, tracking, and operator trust. Poor resolution can still produce detections, but it reduces the clarity of what those detections actually mean.

## Common Mistakes

Several misunderstandings appear repeatedly.

### "High range means high resolution"

No. A radar can detect far away and still have weak target separation at that distance.

### "Resolution is just one number"

No. Range resolution and angular resolution are different, and both matter.

### "Resolution and accuracy mean the same thing"

No. Accuracy is about closeness to truth. Resolution is about separating nearby targets.

### "If the beam angle is fixed, resolution does not change"

No. A fixed beam angle still covers a larger physical area at longer range.

### "Display sharpness is the same thing as radar resolution"

No. A clean display can still hide merged returns if the underlying sensing cell is large.

## What This Means in Practice

For a beginner, the best mental model is this: radar resolution describes how small a difference the radar can meaningfully separate in space.

If you are evaluating a radar, useful questions include:

- what the range resolution is,
- what beamwidth or cross-range behavior looks like,
- how the beam footprint grows with distance,
- what level of multi-target separation the mission needs,
- and whether the environment will make practical resolution worse than the nominal value suggests.

These questions are often more useful than asking only for maximum range or headline sensitivity.

This also explains why resolution belongs in system design discussions, not only in engineering manuals. The radar may be technically capable, but if the resolution cell is too large for the task, the downstream operator picture will still be weak. Good radar planning therefore asks not just "Can the radar detect?" but also "Can it separate what matters?"

## Conclusion

Radar resolution is the radar's ability to distinguish nearby targets instead of merging them into one return. Range resolution deals with separation in depth, while angular resolution deals with separation across direction. Both influence how much useful structure the radar can reveal in a scene.

The key takeaway is that resolution is not the same as range or accuracy. It is a separation question shaped by beamwidth, waveform, distance, clutter, and processing. A radar with honest resolution planning will usually produce a more useful operational picture than one judged only by maximum detection range.

## Related Reading

- [NWS Radar Basics](https://training.weather.gov/nwstc/NEXRAD/RADAR/Section1-2.html)
- [NWS Beam Property Calculator](https://training.weather.gov/wdtd/tools/beamwidth3/)
- [FAA Advisory Circular AC 150/5220-25](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_150_5220-25.pdf)
- [What is Detection Range?](/knowledge-base/what-is-detection-range/)
- [What is Radar? Complete Guide](/knowledge-base/what-is-radar-complete-guide/)
