# pitfalls

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Pitfalls](#pitfalls)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Examples](#examples)

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

## Pitfalls

- Acting before reading the repo or instructions:
  Produces code or notes that fight local conventions.
  Better move: read `AGENTS.md`, nearby files, and naming patterns first.
- Stopping at a plan when the user expects execution:
  Wastes a turn and forces the user to repeat themselves.
  Better move: if the task is concrete and safe, do the work.
- Editing too broadly:
  Increases regression risk and review cost.
  Better move: keep the diff narrow and aligned with the request.
- Reverting unrelated user changes:
  Destroys work and breaks trust.
  Better move: leave unrelated changes alone unless explicitly asked.
- Claiming verification without running anything:
  Gives false confidence.
  Better move: run the nearest relevant check or clearly say it was not run.
- Guessing facts that can be inspected locally:
  Leads to avoidable errors.
  Better move: search the repo, read the file, inspect the command output.
- Getting trapped in one failing approach:
  Burns time without progress.
  Better move: change tactics, simplify, isolate, or verify assumptions.
- Writing a long answer with little action:
  Looks helpful but does not move the task.
  Better move: prioritize edits, commands, and concrete outcomes.
- Ignoring edge cases after the happy path works:
  Leaves fragile results.
  Better move: check failure paths, missing input, and cleanup behavior.
- Hiding uncertainty:
  Makes follow-up harder.
  Better move: state the exact assumption or blocker directly.

## Inputs

- User request
- Repository instructions such as `AGENTS.md`
- Local conventions
- Relevant files, tests, and command output
- Current blockers, failed attempts, or uncertain assumptions

## Outputs

- A short execution plan or recovery plan
- A list of task-specific pitfalls to avoid
- Concrete tips or tricks for the current task
- Clear final notes on changes, verification, and remaining risk

## Examples

### ComfyUI

Task: "Before Download Model, check its hardware, make sure precision model are support by hardware."

Apply the skill by checking local Markdown conventions first, matching
the title to the filename, adding a table of contents, and editing only
the relevant note files.

### Example 2

Task: "Fix the failing script."

Apply the skill by reproducing the failure, reading the surrounding
code before editing, making the smallest plausible fix, and rerunning
the closest verification command.

### Example 3

Task: "Research the latest API behavior."

Apply the skill by treating freshness as unstable, verifying with the
current source, and separating confirmed facts from inference in the
reply.
