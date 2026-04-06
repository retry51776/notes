---
name: git-linter
description: >-
  Use this skill when the user wants commit git repo. Focus on bugs,
  regressions, missing tests, and risky changes before code is commit.
---

# git-linter

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Checklist](#checklist)
- [Inputs](#inputs)
- [Outputs](#outputs)

## Description

Use this skill when the user wants commit git repo. Focus on checklist items.

## Usage

1. Review the actual diff before forming conclusions.
2. Prioritize findings that could break behavior, data, security, or
   deployment.
3. Prefer evidence-backed findings over subjective style opinions.
4. Present findings first, ordered by severity, with file references.
5. After findings, note open questions or testing gaps.
6. Only include a brief change summary if it helps the user act faster.
7. If the user asks for fixes, keep edits narrow and aligned with the
   current codebase.

## Checklist

Keep this file lean by loading detailed guidance only when needed.

- spelling, grammar, and clarity
- inconsistent variable name
- JS review checklist: [references/js.md](./references/js.md)
- Python review checklist: [references/python.md](./references/python.md)
- Markdown review checklist: [references/markdown.md](./references/markdown.md)

## Inputs

- The diff, changed files, or PR scope
- The base branch or expected behavior, if known
- Existing tests, logs, screenshots, or reproduction notes
- Repository conventions such as `AGENTS.md`

## Outputs

- Findings first, ordered by severity
- File-linked evidence for each finding
- Open questions or missing context
- Residual risks or testing gaps
- Optional patch guidance if the user wants edits
