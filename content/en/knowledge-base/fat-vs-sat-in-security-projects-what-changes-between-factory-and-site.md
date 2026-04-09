---
title: "FAT vs SAT in Security Projects: What Changes Between Factory and Site"
slug: "fat-vs-sat-in-security-projects-what-changes-between-factory-and-site"
url: "/knowledge-base/fat-vs-sat-in-security-projects-what-changes-between-factory-and-site/"
description: "A practical guide to FAT versus SAT in security projects, including what can be proven at the factory, what only becomes real on site, and how acceptance criteria should change."
seo_title: "FAT vs SAT in Security Projects: What Changes Between Factory and Site"
seo_description: "Learn the difference between FAT and SAT in security projects, what should be tested at the factory, and what must be validated only after installation on site."
keywords:
  - "fat vs sat in security projects what changes between factory and site"
  - "fat vs sat security project"
  - "factory acceptance test site acceptance test security"
  - "security system commissioning fat sat"
  - "acceptance testing security systems"
categories:
  - "Compliance"
tags:
  - "FAT"
  - "SAT"
  - "Commissioning"
  - "Acceptance Testing"
image: "/images/knowledge-base/fat-vs-sat-in-security-projects-what-changes-between-factory-and-site-cover.jpg"
image_alt: "A person in a safety vest holding a checklist, used as a lead visual for an article about FAT and SAT in security projects."
image_source_name: "RDNE Stock project"
image_source_url: "https://www.pexels.com/photo/person-in-yellow-reflective-safety-vest-holding-a-pen-and-checklist-of-house-inspection-8293680/"
weight: 117
date: 2026-08-18
lastmod: 2026-04-09T13:00:00+08:00
draft: false
keypoints:
  - "Factory acceptance testing proves build completeness, interface behavior, and design intent under controlled conditions, but it does not prove that the installed system works in the real site."
  - "Site acceptance testing must validate the installed environment, including coverage geometry, communications, power quality, latency, configuration, and operator workflow."
  - "A strong security project does not duplicate FAT and SAT blindly; it assigns each test to the earliest place where the result is meaningful and repeatable."
  - "Many disputes happen because the acceptance criteria do not state what is being proven in the factory, what is being proven on site, and which field variables can legitimately change the outcome."
---

FAT and SAT are two of the most familiar terms in project delivery, yet they are also two of the most frequently blurred. Teams say a system has "passed FAT" and start treating that as if the installed deployment is nearly proven. Then site commissioning begins and the real variables appear: different network timing, different mast behavior, unexpected reflections, power issues, misaligned zones, awkward operator workflow, and field devices that behave differently once they leave the controlled factory environment.

That is why the distinction matters. Factory acceptance testing and site acceptance testing are not redundant checkpoints for the same truth. They answer different questions. FAT asks whether the built system behaves correctly in a controlled pre-delivery environment. SAT asks whether the installed system behaves correctly in the real operating environment. The second question cannot be fully answered by the first.

In security projects this difference is especially important because the field environment is part of the system. Coverage, false alarms, cueing quality, evidence usability, and operator response all depend on site conditions that do not exist inside the factory. A good project therefore uses FAT and SAT as complementary proof stages, not as paperwork milestones.

## FAT Proves Design Intent Under Controlled Conditions

Factory acceptance testing should answer a disciplined question: was the promised system assembled and configured correctly enough to demonstrate the intended functions before shipment or deployment?

IEC 62381 is useful here because it treats acceptance and commissioning as staged activities rather than one undifferentiated signoff moment. That staging mindset fits security projects well. Before a system reaches the site, some things can be proven reliably in the factory:

- hardware completeness,
- software version alignment,
- interface behavior between subsystems,
- alarm and event logic,
- recorder or database function,
- user-rights setup,
- basic display behavior,
- and protocol integration with representative devices or simulators.

These are all appropriate FAT subjects because the factory is a controlled environment. The team can reproduce conditions, isolate variables, freeze software builds, and verify whether the system as built matches the intended architecture.

For security projects, FAT is also the right place to validate documentary discipline. Asset lists, wiring schedules, naming conventions, event tables, network plans, and configuration baselines should be checked before shipment because those are easier to correct in the factory than in the field.

What FAT should not claim is that the live site is already proven. That is not a weakness in FAT. It is simply not the job FAT exists to do.

## SAT Proves Installed Behavior, Not Just Delivered Hardware

Site acceptance testing asks a different question: does the installed system work correctly where it will actually be used?

This distinction is critical in security. A radar that passed interface testing in the factory may still have unwanted clutter sectors after installation. A camera that streamed cleanly during FAT may face atmospheric haze, backlight, mast vibration, or narrow-FOV settling issues on site. An RF detector that looked stable in bench integration may encounter multipath, roof clutter, and friendly emitters once deployed around real buildings.

SAT is therefore the stage where the site itself becomes part of the acceptance object. Typical SAT concerns include:

- actual coverage and blind spots,
- installed power quality and backup behavior,
- site communications and latency,
- environmental effects on sensors,
- final calibration and alignment,
- operator workflow from the real control positions,
- and interoperability with the customer's real infrastructure.

This is why SAT cannot be reduced to "repeat FAT after installation." The same test script may still be useful in part, but the acceptance question has changed. The field system is now interacting with geometry, weather, access routes, background emitters, and human workflows that were absent or abstracted in the factory.

## The Same Function May Need Different Acceptance Criteria at FAT and SAT

A mature project does not copy the same pass criteria from FAT into SAT without thinking. The function may be the same, but the acceptance logic often needs to change.

Take an alert workflow as an example.

At FAT, the team may need to prove:

- the correct event is generated,
- the event lands in the right queue,
- the acknowledgement state changes correctly,
- and the evidence object is stored as expected.

At SAT, the workflow question becomes broader:

- does the alert arrive fast enough over the real network,
- is it visible at the operator's actual workstation,
- does the live cue map to the correct zone,
- and can the operator make a usable decision under the site's real workload?

The same applies to detection layers.

At FAT, a sensor may be checked for interface readiness, status reporting, configuration completeness, and basic simulated alarm behavior. At SAT, the project should validate how the installed sensor actually performs in the local environment, including the nuisance sources, obstruction geometry, and coverage edges that matter to the site.

This difference is one reason acceptance disputes happen. A vendor may believe a function was already proven during FAT, while the customer is asking whether it works in the operating environment. Both may be reasonable, but they are asking different questions.

## FAT Is the Best Place to Remove Avoidable Site Risk

Although FAT cannot replace site proof, it can remove a great deal of site risk if it is designed well.

The strongest FAT plans do more than power the system on. They try to eliminate surprises before the site phase by validating:

- end-to-end signal mapping,
- user roles and permissions,
- alarm escalation logic,
- recording and export paths,
- interface contracts,
- failover behavior where the architecture supports it,
- and configuration portability from staging into production.

For multi-sensor security platforms, FAT is also the right place to test with realistic simulated inputs. If radar, EO, RF, doors, analytics, and mapping layers will interact on site, the factory should already prove that the platform understands these objects correctly. The closer the factory test environment is to the intended architecture, the more useful FAT becomes.

This is not just an engineering convenience. It is an efficiency rule. Every avoidable ambiguity left until site commissioning becomes more expensive once crews, access permits, and customer operations are involved.

## SAT Must Validate the Field Variables the Factory Could Not Reproduce

The site phase should focus on what only the site can reveal.

For physical security systems, those field variables usually include:

- real line of sight and masking,
- local reflections or clutter,
- mast or pole stability,
- lighting and contrast conditions,
- actual fence and corridor geometry,
- real operator seating and screen layout,
- actual backhaul capacity,
- and integration with live customer systems rather than test surrogates.

NPSA guidance on protective intrusion detection is useful in spirit here because it treats detection performance as dependent on installation quality and environment, not only on sensor choice. That lesson generalizes well. Many security functions do not become meaningful until the system has been installed in the geometry, background conditions, and workflow context it is meant to protect.

This is also where acceptance must become scenario-based rather than purely component-based. Instead of proving only that each subsystem reports healthy status, the team should prove that the installed system supports real operational outcomes such as:

- detecting movement in the intended corridor,
- cueing the right verification device,
- presenting the alert to the right operator,
- storing the required evidence,
- and recovering cleanly from representative faults.

## FAT and SAT Should Be Connected by Clear Configuration Control

One reason FAT and SAT diverge badly is weak configuration discipline between the two stages.

If the factory build, network settings, event tables, naming conventions, or software versions change informally between FAT and SAT, the project stops comparing the same system across two stages. Then site issues become harder to diagnose because the team no longer knows whether the problem comes from the environment or from undocumented configuration drift.

A stronger delivery model keeps tight control over:

- tested software versions,
- exportable configuration packages,
- change records after FAT,
- device inventories,
- and site-specific parameter adjustments made during commissioning.

This is especially important when the site legitimately needs tuning. Many projects do need field adjustments for zone boundaries, thresholds, timing, or display logic. That is normal. The key is to record which changes were environmental tuning and which changes were corrections to an incomplete factory configuration. Without that distinction, acceptance history becomes muddy and future maintenance becomes harder.

## What Buyers Should Put Into the Acceptance Plan

The best way to avoid FAT-versus-SAT confusion is to make the proof model explicit before delivery begins.

The acceptance plan should state:

- which functions are factory-proven,
- which functions are site-proven,
- what inputs or simulators are acceptable at FAT,
- what real-world conditions must be demonstrated at SAT,
- and what counts as completion if a site variable cannot be reproduced exactly on one test day.

For security projects, this also means deciding early whether the site wants to accept:

- component readiness,
- end-to-end workflow readiness,
- operational performance by zone,
- or all three.

Those are related but not interchangeable. A project that accepts only component readiness may ship faster but still face operational gaps later. A project that wants operational performance proof should say so early and tie the SAT cases to zones, scenarios, and evidence requirements that both sides recognize.

## Common Mistakes

Several mistakes repeatedly weaken acceptance planning.

### Treating FAT as early SAT

The factory cannot prove site geometry, local clutter, or real operator workflow.

### Repeating the same script without changing the question

The installed environment changes what must be proven.

### Leaving configuration control loose after FAT

Undocumented drift makes SAT findings harder to interpret.

### Failing to define scenario-based site tests

A system can be healthy component by component and still fail the operational mission.

### Mixing deliverable completeness with operational performance

Both matter, but they should be evaluated explicitly rather than implicitly.

## Conclusion

FAT and SAT in security projects are not duplicate ceremonies. FAT proves the system has been built, configured, and integrated correctly in a controlled environment. SAT proves the installed system works in the field environment where geometry, background conditions, communications, and human workflow all influence the result. The difference is not procedural trivia. It determines what acceptance evidence is actually meaningful.

The practical takeaway is simple. Use FAT to remove avoidable integration risk early, and use SAT to prove the real site behavior the factory could never fully reproduce. When the proof boundaries are stated clearly, projects move faster and arguments during commissioning become much easier to resolve.

## Related Reading

- [What a Good Civil-Security Tender Should Ask About Verification, Not Just Detection](/knowledge-base/what-a-good-civil-security-tender-should-ask-about-verification-not-just-detection/)
- [How to Reduce False Alarms Without Slowing Response](/knowledge-base/how-to-reduce-false-alarms-without-slowing-response/)
- [Latency Budgets in Multi-Sensor Systems: Why Seconds Matter](/knowledge-base/latency-budgets-in-multi-sensor-systems-why-seconds-matter/)

## Official Reading

- [IEC 62381: Automation systems in the process industry - Factory acceptance test (FAT), site acceptance test (SAT), and site integration test (SIT)](https://webstore.iec.ch/en/publication/24148)
- [ISA cybersecurity factory acceptance testing excerpt](https://www.isa.org/getmedia/de11a98a-13b4-4c83-b5da-8a401a46da6d/Gruhen-Lucchini-Safety-Excerpt-FINAL.pdf)
- [NPSA: Guide to PIDS](https://www.npsa.gov.uk/system/files/documents/2c/80/Guide-to-PIDS.pdf)
- [ISA-105 Standards](https://www.isa.org/standards-and-publications/isa-standards/isa-105-standards)
