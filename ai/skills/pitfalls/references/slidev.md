# Slidev

## Table of Contents

- [Guideline](#guideline)
- [Common Failure Modes](#common-failure-modes)

## Guideline

### v-clicks

For `<v-clicks>` with Markdown content (lists, headings, paragraphs), always keep a blank line:
- after `<v-clicks ...>`
- before `</v-clicks>`

### Slide Size

Avoid slide overflow. If content is likely to overflow, constrain height and enable scrolling (for example `maxHeight: '2000px'` for long code blocks), or split content across slides.

### Slide Guideline

Keep slide density low: target at most 12 visible lines per slide, and keep each line at 70 characters or fewer when possible. Split content into multiple slides when limits are exceeded.

## Common Failure Modes

- When list items all collapsed into single line, MAKE SURE empty line BEFORE `</v-clicks>` & AFTER `<v-clicks>`
- If background image missing, MAKE SURE slide attributes `layout: image` && `image: xxx.png` are set.

