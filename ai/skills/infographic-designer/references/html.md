# HTML

## Implementation Rules

- define css class inside `<style>` tag, avoid css in another file.
  - define css classes for consistent typography
  - assume font sizes are pixel values, use `16px` as the default font size; font size * 1.5px is line height
  - Calculate max chars per line = rect width / font size, and max lines = rect height / font size / 1.5

- make sure no div overflows


## Assumptions

- default font size is 16, font size is font width pixels, line heigh is 150% font width.
- It's 16in mac screen, don't worry about resize problem.

## Avoid

- inline css, avoid css in another file.
- inline js, avoid js in another file, reference CDN, not local install.