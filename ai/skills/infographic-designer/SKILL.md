---
name: infographic-designer
description: Use this skill when the user wants an infographic, visual
  explainer, or single-image information design. Extract the strongest
  facts and narrative from provided material or a topic, choose an
  appropriate visual direction automatically, and produce a cohesive
  infographic concept with clear hierarchy, charts, icons, and a
  generation-ready prompt or layout spec.
---
# infographic-designer

## Table of Contents

- [Description](#description)
- [Workflow](#workflow)
- [Analysis](#analysis)
- [Design System](#design-system)
- [Visualization Guidance](#visualization-guidance)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Response Format](#response-format)
- [Guardrails](#guardrails)

## Description

Use this skill when the user wants to turn a topic or source material
into an original infographic that is immediately understandable and
memorable.

This skill is for:

- infographic concepts
- infographic prompts for image or design tools
- layout specs for a single-image visual
- structured visual explainers built from notes, research, or datasets

The result should feel designed, not dumped. Prioritize a clear message,
strong hierarchy, visual storytelling, and factual accuracy.

## Workflow

1. Determine the source mode.
   - If the user provided detailed material, extract the key facts,
     numbers, comparisons, relationships, and narrative arc.
   - If the user only provided a topic, research the most relevant and
     current angles first.
2. Compress the content into one central takeaway sentence.
3. Identify the minimum set of sections needed to tell the story,
   usually three to six.
4. Select the visual style automatically based on the subject matter.
5. Choose a palette of four to six colors with defined roles.
6. Define the visual hierarchy.
   - headline
   - subheads
   - primary statistic or hero visual
   - supporting visuals
   - footnotes or source area when needed
7. Plan the layout as one cohesive image with clear reading flow.
8. Maintain an approximate 30 percent text to 70 percent visuals ratio.
9. Add custom icons, illustrations, charts, diagrams, and visual
   metaphors where they improve comprehension.
10. Check legibility, proportionality, and factual consistency before
    finalizing.

## Analysis

Start with content reduction, not styling.

For each request, identify:

- the audience
- the single most important message
- the top three to five supporting facts
- the most important comparison or change over time
- the best visual metaphor for the abstract parts
- what can be removed without hurting clarity

When working from source material, extract:

- statistics with units and timeframes
- rankings, deltas, percentages, and ratios
- cause and effect relationships
- sequences, processes, and loops
- categories and groupings
- caveats that must remain visible

When working from a topic only:

- research recent and credible sources
- prefer primary sources for technical, medical, legal, or financial
  topics
- separate confirmed facts from inference
- use concrete dates when timing matters

## Design System

Choose the style that best supports the content instead of defaulting to
one look.

Examples:

- modern editorial for technology, AI, and trend explainers
- corporate clean for finance, policy, and enterprise topics
- illustrated casual for education, lifestyle, or beginner material
- minimalist analytical for dense data stories
- vintage or poster-like only when it improves memory and tone

Define:

- a palette of four to six colors
- one dominant color, one accent color, and neutral support colors
- typography with distinct roles for headline, subhead, labels, and
  annotations
- icon and illustration style
- background treatment, negative space, and section dividers

Use scale, contrast, spacing, and alignment to guide the eye in the
intended order.

## Visualization Guidance

Prefer visuals that reduce cognitive load.

Use:

- bar, line, pie, scatter, or timeline charts only when the data fits
- process diagrams for steps, loops, and systems
- comparison panels for before and after or option tradeoffs
- scale anchors to make large numbers meaningful
- custom icons tied to the actual subject matter
- contextual imagery only when it supports the story

Avoid:

- decorative charts with no analytical value
- overloaded legends
- more than one main story per infographic
- clip-art style visuals that fight the tone
- tiny copy blocks that will fail when scaled down

## Inputs

- the user's source material, topic, or dataset
- intended audience, if known
- desired tone, if known
- delivery target, if known, such as prompt, layout brief, HTML, SVG, or
  design spec
- citations or source links when accuracy matters

## Outputs

Default output should include:

- a headline and optional deck
- the core message in one sentence
- the section-by-section narrative flow
- the chosen visual style and rationale
- the palette and typography direction
- the chart, diagram, and icon plan
- the final infographic prompt or implementation-ready spec

If the user asks for direct generation, produce the asset in the
requested format after establishing the above structure.

## Response Format

Use this structure unless the user asks for another format.

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

Provide either:

- a generation-ready prompt for an image or design model
- a structured layout brief
- direct implementation in the requested medium

## Guardrails

- Do not invent facts, statistics, or citations.
- If data is uncertain, label it clearly or leave it out.
- Do not sacrifice readability for visual flair.
- Keep the infographic to one main story and one dominant reading path.
- Avoid stock phrases such as "future of" or "everything you need to
  know" unless they are genuinely accurate.
- Make sure all text stays legible at multiple viewing sizes.
- Preserve nuance when the topic is sensitive or high stakes.
