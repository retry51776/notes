---
name: infographic-designer
description: Use this skill when the user wants an infographic, visual
  explainer, or single-image information design. Extract the strongest
  facts and narrative from provided material or a topic, choose an
  appropriate visual direction automatically, and produce a cohesive
  infographic concept with clear hierarchy, charts, icons, and a
  generation-ready prompt, layout brief, or direct SVG/HTML output.
---
# Infographic Designer

Use this skill when the user wants to turn a topic, notes, research, or
data into a single-image visual that is immediately understandable and
memorable.

The output should feel designed, not dumped. Prioritize one strong
message, clear hierarchy, visual storytelling, and factual accuracy.

## When To Use

Use this skill for:

- infographic concepts
- visual explainers
- single-image layout briefs
- generation-ready prompts for image or design tools
- direct `SVG` or `HTML` infographic implementation

## Workflow

1. Determine the source mode.
   - If the user provided material, extract the key facts, numbers,
     comparisons, relationships, caveats, and narrative arc.
   - If the user only provided a topic, research relevant and current
     sources first.
2. Reduce the content to one core takeaway sentence.
3. Choose the minimum number of sections needed to tell the story,
   usually three to six.
4. Pick the delivery mode:
   - prompt
   - layout brief
   - direct `SVG`
   - direct `HTML`
5. Select a visual direction that fits the subject instead of
   defaulting to one generic style.
6. Define the information hierarchy:
   - headline
   - deck or subhead
   - hero number, chart, or illustration
   - supporting sections
   - source or footnote area when needed
7. Map each fact to the clearest visual form.
8. Generate the final deliverable and check readability, accuracy, and
   overflow before finishing.

## Content Reduction

Start with content reduction, not styling.

Identify:

- the audience
- the single most important message
- the top three to five supporting facts
- the most useful comparison, trend, or sequence
- the best visual metaphor for abstract ideas
- what can be removed without hurting clarity

When extracting facts, preserve:

- units and timeframes
- rankings, deltas, percentages, and ratios
- cause and effect relationships
- steps, loops, and systems
- categories and groupings
- caveats that must remain visible

## Visual Direction

Choose the style that best supports the content.

Examples:

- modern editorial for technology and AI
- corporate clean for finance, policy, and enterprise
- illustrated casual for education or beginner explainers
- minimalist analytical for dense data stories
- poster-like only when it improves recall and tone

Define:

- a palette of four to six colors
- one dominant color, one accent color, and neutral support colors
- typography roles for headline, subhead, labels, and annotations
- icon or illustration style
- background treatment, negative space, and section dividers

Use scale, contrast, spacing, and alignment to control reading order.

## Visualization Rules

Prefer visuals that reduce cognitive load.

Use:

- bar, line, pie, scatter, or timeline charts only when the data fits
- process diagrams for steps, loops, and systems
- comparison panels for tradeoffs, before and after, or alternatives
- scale anchors to make large numbers meaningful
- custom icons tied to the subject matter
- contextual imagery only when it supports the story
- simple patterns, gradients, or textures to avoid a dead background

Avoid:

- decorative charts with no analytical value
- overloaded legends
- more than one main story
- clip-art visuals that fight the tone
- tiny copy blocks that fail when scaled down
- text overflow or elements running off the canvas
- `textLength` in `SVG` unless it is genuinely needed

## Direct Implementation Rules

When producing `SVG` or `HTML` directly:

- set explicit canvas dimensions
- assume font sizes are pixel values unless the format requires
  otherwise
- use `16px` as the default body size
- keep a clear dominant reading path
- leave enough padding for every text block
- make sure no text overflows its container
- ensure the final layout remains legible at smaller viewing sizes

## Output Contract

Default output should include:

- a headline and optional deck
- the core message in one sentence
- the section-by-section narrative flow
- the chosen visual style and rationale
- the palette and typography direction
- the chart, diagram, and icon plan
- the final deliverable in the requested format

If the user asks for direct generation, produce the asset after the
structure is clear.

Use this response structure unless the user asks for another format.

### Infographic Goal

- Audience:
- Core message:
- Format:

### Narrative Flow

- Headline:
- Section 1:
- Section 2:
- Section 3:
- Optional supporting sections:

### Visual Direction

- Style:
- Color palette:
- Typography:
- Icon or illustration approach:
- Layout flow:

### Visualization Plan

- Hero visual:
- Data visuals:
- Supporting comparisons:
- Scale anchors or metaphors:

### Final Deliverable

Provide one of:

- a generation-ready prompt
- a structured layout brief
- direct `SVG`
- direct `HTML`

## Guardrails

- do not invent facts, statistics, or citations
- if data is uncertain, label it clearly or leave it out
- prioritize clarity and intuitiveness over novelty
- keep to one dominant story and one dominant reading path
- avoid stock headline filler unless it is genuinely accurate
- preserve nuance for sensitive or high-stakes topics
