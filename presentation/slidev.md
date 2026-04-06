# Slidev

- Recommend 6 lines per slide, 8 words per line. Code block exam from this recommendation.
- Each slide should highlight its keywords with color.
- ALWAYS add new line After <v-clicks>, and another new line BEFORE </v-clicks>.
- Slide properties within `---` MUST avoid have empty newline
- Example to embed QR code with `<img
  src="https://api.qrserver.com/v1/create-qr-code/?size=260x260&data=Some String Here`
- Set slide background MUST set both `image: url_or_path` && `layout: image`
- ALWAYS add `<br />` between Title and list for clear spacing
- ALWAYS wrap footnote side div `<div class="absolute bottom-4 left-0 w-full text-center text-sm text-gray-400">foot note here</div>`

## Visual

Given above context, get keywords, then generate 3 visual resources in either formats:
- keyword.svg
- emoji

So user can preview & decide;

Assume Tailwind CSS are installed.

## Outline


============
Given above context, generate Markdown file `outline.md`, outline each slide summary;

Ex:

```md
---
layout: cover
---
<!-- Slide 1 -->
## Slide 1 Title

### Subtitle

<br />

summary here

visual:
- have background_a.png

---
layout: two-cols-header
---
<!-- Slide 2 -->
## XYZ

::left::
### Subtitle Left

<img />


::right::

### Subtitle Right

<br />

section A
section B
section C

footnote:
footnote here

visual:
- Subtile have icon_a
- section B have icon_b
---
```