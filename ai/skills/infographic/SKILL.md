---
name: infographic
description: Use this skill when the user wants to turn a topic, notes, research, or data into a single-image visual that is immediately understandable and memorable.
---
# Infographic

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

Generate one of:

- `xxx.svg`
- `xxx.html`
- `xxx.png`
- `xxx.md`


## Workflow
  
1. Check user prompt against Inputs items to clarify any missing content.
  - If any input is missing, ask the user for that specific content before proceeding.
2. Determine the output format.
   - For svg: Read [references/svg.md](./references/svg.md)
   - For html: Read [references/html.md](./references/html.md)
   - For slidev: Read [references/slidev.md](./references/slidev.md)
3. Define the content hierarchy:
   - headline
   - deck or subhead
   - hero number, chart, or illustration
   - supporting sections
    - 3 or fewer words for each section as section headline
    - each section generate simple icon or symbol
   - source, footnote, conclusion area
4. Select a visual system that fits the subject.
5. Generate the final deliverable
6. Check readability, accuracy, and overflow with screen capture, REPEAT until no readability, accuracy, and overflow issues.

## Content Hierarchy

Start with content reduction, not styling.

Identify:

- the audience
- the single most important message
- break content into sections
  - Each section MUST have
    - headline
    - simple icon or symbol (default to SVG icon)
  - Optional addition
    - short explanation/desc
    - analogy/metaphor
    - KEYWORDs
- the most useful comparison, trend, or sequence
- what can be removed without hurting clarity

When extracting facts, preserve:

- information hierarchy
- units and timeframes
- rankings, deltas, percentages, and ratios
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

### Visualization Resources

Get Emojis from:
  https://emojidb.org/
  https://getemoji.com/

Get prebuilt svg from:
  https://www.svgrepo.com/

### Visualization Rules

Prefer visuals that reduce cognitive load.

Use:

- Eliminate clutter!!!
- 30% text 70% visuals
- Keep image & icon simple
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
