# git-linter edit-guide

## Table of Contents

- [Default Preferences](#default-preferences)
- [Patch Style](#patch-style)
- [Customization Template](#customization-template)

## Default Preferences

- Keep fixes as small as possible.
- Preserve existing architecture unless the bug requires more.
- Match local naming, formatting, and error-handling patterns.
- Avoid drive-by refactors during review fixes.
- Do not revert unrelated user changes.

## Patch Style

- Fix the highest-severity issue first.
- Prefer one focused patch per issue when practical.
- Add tests near the changed behavior when the repo already supports it.
- Add comments only when they reduce real ambiguity.
- Verify the nearest relevant command before claiming a fix.

## Customization Template

Fill this in later if you want the skill to enforce your personal
editing style:

- Refactor tolerance:
- Comment preference:
- Naming preference:
- Test preference:
- Formatting preference:
- Risk tolerance for broader cleanup:
