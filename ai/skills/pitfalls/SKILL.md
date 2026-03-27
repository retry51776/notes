---
name: pitfalls
description: >-
  Use this skill when an agent is starting a task, gets stuck mid-task, or
  needs a quick quality pass before replying.
---

# pitfalls

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Reference Loading](#reference-loading)
- [Inputs](#inputs)
- [Outputs](#outputs)

## Description

Use this skill when an agent is about to start a task, gets stuck mid-task,
or needs a quick quality pass before replying. It captures common agent
mistakes from practical experience and turns them into simple recovery
moves, tips, and execution rules.

## Usage

1. Restate the user's actual goal in one sentence.
2. Read local context before assuming structure, naming, or conventions.
3. Separate facts, assumptions, and open questions.
4. Prefer execution over commentary when the request is actionable.
5. Make small, reversible changes.
6. Verify the closest thing that can fail.
7. In the final reply, state what changed, what was verified, and what
   remains uncertain.

## Reference Loading

Keep this file lean by loading detailed guidance only when needed.

### ComfyUI
Read [references/comfyui.md](./references/comfyui.md) when you need:

### Slidev
Read [references/slidev.md](./references/slidev.md) when you need:

## Inputs

- User request
- Current blockers, failed attempts, or uncertain assumptions
- Repository instructions such as `AGENTS.md`
- Local conventions
- Relevant files, tests, and command output

## Outputs

- A short execution plan or recovery plan
- A list of task-specific pitfalls to avoid
- Concrete tips or tricks for the current task
- Clear final notes on changes, verification, and remaining risk
