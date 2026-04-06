# SVG

## Implementation Rules

- Every `rect` should calculate its max characters per line and max lines, for example:
  - make sure no text overflows its container
  - assume font sizes are pixel values, use `16px` as the default font size; font size * 1.5px is line height
  - Calculate max chars per line = rect width / font size, and max lines = rect height / font size / 1.5
```
<rect x="680" y="332" width="160" height="48" rx="20" fill="#FF8A5B"/>
<!-- max chars per line: 10, max lines: 2. -->
```

## Assumptions

- default font size is 16, font size is font width pixels, line heigh is 150% font width.


## Avoid

- `textLength` in `SVG`