---
name: infographic-designer
description: Use this skill when the user wants to turn a topic, notes, research, or
data into a single-image visual that is immediately understandable and
memorable.
---
# Infographic Designer

CONTENT (message)
  → STRUCTURE (content hierarchy)
    → LAYOUT (template)
      → COMPONENTS (cards/icons)
        → STYLE (colors/fonts)

## Inputs

- Content: the topic, notes, research, or data to visualize.
- Template: Flow, Explainer, Comparison, Timeline, or Marketing
- Audience: general(default), beginner, technical, or expert
- Orientation: (default infer from Template or Content) portrait, landscape, square, or vertical scroll
- Language: English(default) or [other language]
- Reference: image(optional)

## Output

Provide one of:

- direct `SVG`
- direct `HTML`
- direct `PNG`


## Workflow
  
1. Check user prompt against Inputs items to clarify any missing information.
  - If any input is missing, ask the user for that specific information before proceeding.
2. Reduce the content to one core takeaway sentence.
3. Choose the minimum number of sections needed to tell the story, usually three to six.
4. Select a visual system that fits the subject.
5. Define the information hierarchy:
   - headline
   - deck or subhead
   - hero number, chart, or illustration
   - supporting sections
    - 3 or fewer words for each section as section headline
   - source, footnote, conclusion area
6. Determine the output format.
   - For svg: Read [references/svg.md](./references/svg.md) 
   - For html: Read [references/html.md](./references/html.md)
7. Generate the final deliverable and check readability, accuracy, and overflow before finishing.

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

### Content Guardrails

- do not invent facts, statistics, or citations
- prioritize simple and intuitiveness


## Visual System

Choose the style that best supports the content.

Examples:

- modern editorial for technology and AI
- corporate clean for finance, policy, and enterprise
- illustrated casual for education or beginner explainers
- minimalist analytical for dense data stories
- poster-like only when it improves recall and tone

Define:

- a palette of four to six primary colors
  - dominant color
  - accent color
  - neutral support colors
- consistent typography
  - headline
  - subhead
  - labels
  - annotations
- icon or illustration style
- background treatment, negative space, and section dividers

Use scale, contrast, spacing, and alignment to control reading order.

### Visualization Rules

Prefer visuals that reduce cognitive load.

Use:

- 30% text 70% visuals.
- set explicit canvas dimensions
- bar, line, pie, scatter, or timeline charts only when the data fits
- process diagrams for steps, loops, and systems
- comparison panels for tradeoffs, before and after, or alternatives
- scale anchors to make large numbers meaningful
- custom icons tied to the subject matter
- contextual imagery only when it supports the story
- simple patterns, gradients, or textures backgrounds

Avoid:

- text overflow or elements running off the canvas
- decorative charts with no analytical value
- overloaded legends
- clip-art visuals that fight the tone
- tiny copy blocks that fail when scaled down
- Avoid blank backgrounds
