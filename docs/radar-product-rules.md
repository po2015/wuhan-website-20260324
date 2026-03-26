# Radar Product Page Rules

## 1. Naming Convention
Model naming follows this structure:

SRC-[Band][DetectionLevel][Architecture]-[Generation][Purpose]

### Band Codes
- C = C band
- X = X band
- K = Ku band

### Detection Level Codes
- 01 = 1.5 km
- 03 = 3 km
- 05 = 5 km
- 08 = 8 km
- 10 = 10 km
- 12 = 12 km
- 25 = 25 km
- 50 = 50 km

### Scanning Architecture Codes
- A = Azimuth Electronic Scan
- B = Mechanical Azimuth Scan + Electronic Elevation Scan
- C = Two-Dimensional Electronic Scan (Single-Face AESA)
- D = 2D Electronic Scan + Mechanical Rotation
- E = Four-Face AESA Array

### Generation Codes
- 2 = Second Generation, FMCW
- 1 = First Generation, Pulse Doppler
- 3 = Third Generation, Pulse Doppler

### Purpose Codes
- D = Drone detection
- G = Ground surveillance
- M = Multi-purpose

## 2. Hugo File Location
Each radar product detail page must be created under:
content/en/sensors/src/<slug>/index.md

## 3. Frontmatter Requirements
Each radar product page must include:
- title
- slug
- description
- weight, to order the product pages from small to big number.
- seo_title
- seo_description
- keywords
- model
- band
- architecture_code
- architecture_name
- generation
- system_type
- purpose
- max_range_km
- targets
- highlight
- image
- product_weight
- factory_location (default: Xi'an, China)
- draft

## 4. Detail Page Requirements
Each detail page must contain:

1. Hero section with title, introduction, explaition of model string according to the naming rule, and main product image.

### Fixed Model Code Breakdown Style
This section is deprecated.

Current SRC detail pages are generated from `docs/SRC-*.yaml` into `content/en/sensors/src/<slug>/index.md` and rendered with the standard detail-page template at `layouts/_default/src-detail-sample.html`.

Do not use the deleted `model-breakdown` shortcode or the removed `radar-product` layout for new pages.

2. Key feature badges displayed near the title:
   - Band (C / X / Ku Band)
   - Scanning architecture, for FMCW, use full phrase. 
   - Target-distance capability bars
   - factory location

4. Technical specification table including (but not limited to):
   - Band
   - Detection range
   - Radar operating mode
   - Blind zone
   - Horizontal field of view
   - Elevation field of view
   - Velocity measurement range
   - Rotation speed (only for architectures with mechanical rotation; otherwise N/A)
   - Data update rate
   - Simultaneous tracking targets (TWS and TAS)
   - Range accuracy
   - Azimuth accuracy
   - Elevation accuracy (N/A for A-type architectures)
   - Communication interface
   - Power supply range
   - Power consumption
   - Environmental adaptability
   - Weight
   - Dimensions
5. Typical Application Scenarios
6. FAQ Section 
The FAQ section should address common technical, commercial, and deployment questions typically raised by international security integrators and project buyers. make it univeral for all the radar product. 

The following topics can be covered:

a. Manufacturer and Distributor Relationship  
Explain that Cyrentis is a solution provider and international distributor rather than the original manufacturer.  
The radar products are manufactured by specialized radar manufacturers in China who focus on engineering and production, while Cyrentis focuses on international project support, integration consulting, and global delivery.  
Highlight that customers working through Cyrentis receive stronger technical coordination, integration assistance, and competitive channel pricing.

b. System Integration Capability  
Explain that the radar systems provide open communication protocols and standard interfaces.  
They can be easily integrated with other subsystems such as:
- EO/IR optical tracking systems
- soft-kill countermeasure systems
- hard-kill interception systems
- centralized command and monitoring platforms  
Mention that Cyrentis can also provide complete integrated solutions combining radar, electro-optical sensors, communication equipment, and control software.

c. Deployment and Mobility  
Explain that the radar systems are designed for easy installation and rapid deployment.  
With standard mounting structures and clear documentation, trained technical teams can quickly assemble, install, and operate the system.  
Highlight that many models are suitable for mobile deployment scenarios.

d. AI-Assisted Target Recognition  
Explain that the radar algorithms incorporate trained AI models that significantly improve target classification accuracy.  
Mention that the systems have been tested in challenging environments such as tropical rainforest regions with heavy bird activity (e.g., Southeast Asia), improving the ability to distinguish drones from birds and other objects.

e. Civil Security Use and Export Compliance  
Clearly state that all radar products are intended strictly for civil security applications.  
Radar systems fall under export control regulations of the People's Republic of China as dual-use items.  
Export therefore requires the appropriate dual-use export license issued by the relevant authorities.

Use the following official PRC sources as the basis for general compliance wording:
- PRC Dual-Use Export Control List effective December 1, 2024
- MOFCOM / GACC / CMC Equipment Development Department Announcement No. 31 of 2024

For structured SRC radar data, apply an internal compliance escalation rule:
- If `detection.typical_detection_ranges_km.small_uav_0_01m2 >= 10`, mark the product record as `special_permit_required`.
- This 10 km threshold is a project review trigger for manual compliance escalation.
- Do not describe the 10 km threshold as a verbatim quotation from PRC law unless separately verified for the exact product and transaction context.

Include a link to a dedicated Knowledge Base article explaining dual-use export regulations and compliance procedures.

7. Compliance Notice

Each radar product page must include a clear compliance notice stating that:

- the systems are designed for civil security applications,
- export is subject to dual-use export control regulations,
- proper licensing procedures must be followed before international delivery.


## 6. Knowledge Base Articles to Create
Create these knowledge base articles:
1. Choosing Radar Frequency Bands: Pros, Cons, and Application Scenarios
2. Comparison of Different Radar Scanning Architectures
3. Compliance Overview for Dual-Use Export of Civil Security Radar Products

### Writing Tone
- Professional and technically credible
- International B2B oriented
- Civil security use only
- Avoid military marketing tone
- Keep wording compliant and export-conscious
- Clear, concise, and structured
- Focus on practical value, deployment scenarios, and integration benefits
- Avoid exaggerated claims or sensational language

### Content Presentation
- Use short paragraphs and clear section headings
- Use comparison tables for technical specifications
- Use highlight badges to emphasize key strengths such as range, reliability, deployment flexibility, or integration readiness
- Use icon-supported feature lists where appropriate
- Add simple explanatory notes for technical concepts to improve readability for non-engineering buyers
- Where useful, include visual aids such as target-range bars, architecture comparison diagrams, and deployment scenario illustrations

### Visual and Data Elements
- Use lightweight technical charts or diagrams to make product differences easier to understand
- Python-generated charts are allowed for technical explanations, such as:
  - target detection range comparison
  - frequency band comparison
  - scanning architecture comparison
  - coverage and field-of-view illustration
- Charts should be clean, minimal, and business-friendly
- Avoid overly decorative or consumer-style infographics
- All visuals should support technical understanding and purchasing decisions

### Chart Style Rules
- Prefer simple bar charts, comparison diagrams, and clean technical illustrations
- Use consistent labels, units, and terminology
- Keep colors restrained and professional
- Prioritize clarity over decoration
- Charts should look suitable for an engineering catalog or solution brochure
