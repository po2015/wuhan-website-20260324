Build a reusable skill that evaluates B2B technical product detail pages based primarily on the final rendered HTML that real visitors see.

The skill must NOT evaluate raw markdown alone as the source of truth.
It must use a two-stage process:

--------------------------------------------------
GOAL
--------------------------------------------------

Create a product-page review skill for a professional B2B industrial website.

The pages being reviewed are product detail pages for technical products such as:
- radar systems
- RF detection systems
- electro-optical systems
- surveillance hardware
- low-altitude security products
- command-and-control platforms
- other industrial security / sensing products

The skill must determine whether a rendered product page should:
1. PASS
2. REQUIRE_REVISION
3. REQUIRE_REWRITE

The skill must be strict, structured, deterministic, and suitable for workflow automation.

--------------------------------------------------
IMPLEMENTATION REQUIREMENT
--------------------------------------------------

Implement the skill as a TWO-STAGE pipeline.

==========================
STAGE 1: HTML PREPROCESSING
==========================

Input:
- rendered_html
- optional page_url
- optional source_content (markdown/front matter)

Primary source of truth:
- rendered_html

The skill must first parse and extract structured page signals from the rendered HTML before doing any evaluation.

Extract as much of the following as possible:

1. Page metadata
- title
- meta description
- canonical URL if available

2. Heading structure
- H1
- H2 list
- H3 list

3. Hero / above-the-fold signals
- hero headline
- hero subheadline
- first CTA text
- first CTA link
- whether the hero clearly states what the product is

4. Product-description signals
- intro paragraphs
- summary copy
- key value proposition text

5. Feature block signals
- bullet lists
- feature cards
- key feature headings
- capability statements

6. Specification signals
- technical specification tables
- parameter lists
- performance values
- units like km, GHz, degrees, channels, weight, power, IP rating, etc.

7. Use-case / scenario signals
- sections mentioning deployment scenarios, applications, use cases, industries, environments

8. Conversion signals
- CTA buttons
- quote request language
- contact forms
- contact links
- datasheet download links

9. Internal linking signals
- related products
- related solutions
- related articles
- breadcrumbs
- product families

10. Trust signals
- datasheet references
- compliance references
- deployment claims
- installation guidance
- integration language
- technical diagrams
- real product terminology

11. Visual-structure signals inferred from HTML
- number of sections
- average paragraph length
- whether the page is one giant text block
- whether tables exist
- whether list structures exist
- whether images are present
- whether the page appears structurally balanced or thin

12. Placeholder / weak-content signals
Detect signs such as:
- lorem ipsum
- placeholder image alt text
- generic AI-like sections
- repeated claims
- empty headings
- sections with little actual information
- meaningless buzzword-heavy copy

After extracting the signals, produce an internal normalized representation of the page.

==========================
STAGE 2: PAGE EVALUATION
==========================

Use the extracted structure and the rendered HTML to evaluate the page as a real customer-facing B2B product page.

Do NOT evaluate it like a blog post.
Do NOT evaluate it like a raw markdown article.
Evaluate it like a product landing page that must support:
- product understanding
- technical trust
- commercial inquiry
- solution positioning

--------------------------------------------------
DECISION RULES
--------------------------------------------------

Apply these rules exactly:

1. If any critical dimension score is below 5:
   final_decision = "REQUIRE_REWRITE"

Critical dimensions:
- above_the_fold_clarity
- product_positioning_clarity
- technical_information_completeness
- conversion_readiness
- trust_procurement_readiness

2. Else if overall_score < 7:
   final_decision = "REQUIRE_REVISION"

3. Else if two or more of the following blocks are "weak" or "missing":
   - specifications
   - use_cases
   - cta
   then final_decision = "REQUIRE_REVISION"

4. Else:
   final_decision = "PASS"

Be strict.
Do not inflate scores.

--------------------------------------------------
10 EVALUATION DIMENSIONS
--------------------------------------------------

Score each dimension from 1 to 10.

1. Above-the-Fold Clarity
Evaluate:
- Is it immediately clear what the product is?
- Is the purpose understandable from the first visible section?
- Does the hero communicate category, use, and core value?

2. Page Structure & Information Hierarchy
Evaluate:
- Is the page logically organized?
- Are sections ordered in a useful way?
- Is the page easy to scan?

3. Product Positioning Clarity
Evaluate:
- Is the product category clear?
- Is the model or offering clearly positioned?
- Is the intended scenario, customer, or mission understandable?

4. Technical Information Completeness
Evaluate:
- Does the page provide enough concrete technical information?
- Are specs, capabilities, deployment details, and performance indicators present?
- Would a technical buyer find it useful?

5. Conversion Readiness
Evaluate:
- Is there a clear CTA?
- Is there a path to inquiry, quotation, datasheet, or contact?
- Is the next action obvious?

6. Readability & Professional Tone
Evaluate:
- Is the copy readable and professional?
- Does it avoid weak AI phrasing and excessive fluff?
- Does it sound like a serious industrial company?

7. Visual-Structural Balance
Evaluate:
- Does the page appear balanced in structure?
- Is it too text-heavy?
- Are sections, tables, bullets, and media reasonably distributed?

8. SEO & Topic Focus
Evaluate:
- Is the page clearly focused on one product/topic?
- Is the heading structure useful?
- Is the page likely to perform as a product landing page?

9. Internal Linking & System Context
Evaluate:
- Does the page connect to related products, solutions, or supporting content?
- Does it place the product inside a larger system or ecosystem?

10. Trust & Procurement Readiness
Evaluate:
- Would a serious B2B customer trust this page?
- Does it feel real, concrete, and procurement-friendly?
- Does it support early-stage vendor evaluation?

--------------------------------------------------
CONTENT BLOCK JUDGMENT
--------------------------------------------------

Explicitly judge the following content blocks as one of:
- "strong"
- "adequate"
- "weak"
- "missing"

Blocks:
- hero_summary
- key_features
- specifications
- use_cases
- cta
- related_links

--------------------------------------------------
PLACEHOLDER / AI / LOW-QUALITY SIGNALS
--------------------------------------------------

Actively detect:
- placeholder text
- generic AI wording
- repeated claims
- low-information sections
- over-marketing
- weak or missing specs
- vague feature bullets
- no use-case clarity
- no trust-building detail
- no actionable CTA

--------------------------------------------------
OUTPUT REQUIREMENTS
--------------------------------------------------

Return ONLY valid JSON.
No markdown.
No extra commentary.

Use this exact schema:

{
  "final_decision": "PASS | REQUIRE_REVISION | REQUIRE_REWRITE",
  "reason_for_decision": "string",
  "overall_score": 0.0,
  "dimension_scores": {
    "above_the_fold_clarity": 0,
    "page_structure_information_hierarchy": 0,
    "product_positioning_clarity": 0,
    "technical_information_completeness": 0,
    "conversion_readiness": 0,
    "readability_professional_tone": 0,
    "visual_structural_balance": 0,
    "seo_topic_focus": 0,
    "internal_linking_system_context": 0,
    "trust_procurement_readiness": 0
  },
  "critical_dimensions_below_5": [
    "string"
  ],
  "content_blocks": {
    "hero_summary": "strong | adequate | weak | missing",
    "key_features": "strong | adequate | weak | missing",
    "specifications": "strong | adequate | weak | missing",
    "use_cases": "strong | adequate | weak | missing",
    "cta": "strong | adequate | weak | missing",
    "related_links": "strong | adequate | weak | missing"
  },
  "extracted_page_signals": {
    "title": "string",
    "meta_description": "string",
    "canonical_url": "string",
    "h1": "string",
    "h2_headings": ["string"],
    "h3_headings": ["string"],
    "hero_headline": "string",
    "hero_subheadline": "string",
    "first_cta_text": "string",
    "first_cta_link": "string",
    "intro_summary": "string",
    "feature_signals": ["string"],
    "specification_signals": ["string"],
    "use_case_signals": ["string"],
    "conversion_signals": ["string"],
    "internal_link_signals": ["string"],
    "trust_signals": ["string"],
    "visual_structure_signals": {
      "section_count": 0,
      "has_tables": true,
      "has_bullet_lists": true,
      "has_images": true,
      "appears_text_heavy": true,
      "appears_structurally_balanced": true
    }
  },
  "placeholder_or_ai_signals": [
    "string"
  ],
  "major_issues": [
    "string"
  ],
  "revision_actions": [
    "string"
  ],
  "rewrite_actions": [
    "string"
  ],
  "strengths": [
    "string"
  ],
  "summary_assessment": "string"
}

--------------------------------------------------
SCORING GUIDANCE
--------------------------------------------------

9-10:
Excellent product page, strong technical and commercial quality, ready for serious B2B use.

7-8:
Good page, usable, but still has room for improvement.

5-6:
Weak or incomplete, needs meaningful revision before publication.

1-4:
Poor, placeholder-like, structurally weak, commercially ineffective, or technically thin. Rewrite required.

Important:
- Do not confuse polished wording with real product-page quality.
- Prioritize clarity, technical usefulness, trust, and conversion support.
- Penalize thin pages hard.
- Penalize weak or missing specs hard.
- Penalize vague hero copy hard.
- Penalize lack of CTA hard.

--------------------------------------------------
ENGINEERING REQUIREMENTS
--------------------------------------------------

Implement the skill so that:
- it can accept raw rendered HTML as input
- it can parse/extract structured page signals first
- it then evaluates using both extracted signals and original rendered HTML
- it outputs deterministic JSON
- it is suitable for use in an automated content-quality workflow

If optional source_content is provided, use it only as secondary context and never as the primary truth over rendered_html.

--------------------------------------------------
INPUTS
--------------------------------------------------

Rendered HTML:
{{rendered_html}}

Optional source content:
{{source_content}}

Optional page URL:
{{page_url}}