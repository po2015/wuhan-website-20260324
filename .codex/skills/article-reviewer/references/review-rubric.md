# Review Rubric

Review one article and classify it as:

- `PASS`
- `REQUIRE_REVISION`
- `REQUIRE_REWRITE`

## Decision Logic

Apply in this order:

1. If any dimension score is below `5`, the decision is `REQUIRE_REWRITE`
2. Else if `word_count < 1000`, the decision is `REQUIRE_REVISION`
3. Else if `overall_score < 8.0`, the decision is `REQUIRE_REVISION`
4. Else the decision is `PASS`

`REQUIRE_REWRITE` is always more severe than `REQUIRE_REVISION`.
In iterative editorial workflows, `REQUIRE_REWRITE` means rewrite first, `REQUIRE_REVISION` means revise against the issues list, and the article should be reviewed again until it reaches `PASS`.

## Scoring

Score each dimension from `1` to `10`.

### 1. structure_logical_clarity
- Organization
- Heading quality
- Logical flow
- Topic control

### 2. target_classification_content_framing
- Clear article type
- Clear implied audience
- Proper scope and framing

### 3. marketing_noise_control
- Low hype
- Low sales language
- Informative tone

High score means low marketing noise.

### 4. content_depth
- Mechanisms
- Technical logic
- Trade-offs
- Engineering context

### 5. readability_human_quality
- Natural phrasing
- Varied sentence structure
- Low "generic AI" feel

### 6. information_density
- Useful content per paragraph
- Low filler
- Low repetition

### 7. seo_knowledge_base_fitness
- Clear topic
- Search / retrieval value
- Good knowledge-base fit

### 8. technical_credibility
- Domain awareness
- Precise claims
- Believable to technical readers

### 9. decision_value
- Helps comparison or selection
- Moves beyond description
- Gives practical judgment

### 10. original_insight
- Synthesis
- Fresh framing
- Non-obvious value

## Overall Score

`overall_score` must be the arithmetic mean of the 10 dimension scores, rounded to 1 decimal place.

## AI-like Writing Signals

Detect and report concrete signals such as:

- repetitive transitions
- generic opener or closer paragraphs
- empty claims
- shallow comparison
- templated structure without substance
- vague buzzwords
- fake authority tone
- padding for word count
- low-information paragraphs

## Output Expectations

- Be concrete
- Be unsentimental
- Keep `reason_for_decision` short
- Use arrays for findings, actions, strengths, and AI signals
- Keep `summary_assessment` compact but specific
