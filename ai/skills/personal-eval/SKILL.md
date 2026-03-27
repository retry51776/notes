---
name: personal-eval
description: >-
  Use this skill when the user wants a personal evaluation or psychology
  reevaluation. This skill follows an inversion workflow: collect background
  and concrete failures first, then analyze backward from repeated outcomes to
  likely
  source layers.
---
# personal-eval

## Table of Contents

- [Description](#description)
- [Workflow](#workflow)
- [Intake](#intake)
- [Analysis](#analysis)
- [Guardrails](#guardrails)
- [Inputs](#inputs)
- [Outputs](#outputs)

## Description

Use this skill when the user wants a structured self-evaluation,
personal pattern analysis, or help locating which layer of development
likely drives a repeated behavior.

This skill is not for solving the user's life directly. The goal is to
build a cleaner model of the user's recurring patterns, blind spots,
triggers, and likely source layers.

## Workflow

1. Start with conversational intake.
   - Do NOT ask a full batch of questions.
   - Ask 1–2 questions per turn.
   - Always anchor questions to what the user just said.
   - Encourage user write out their internal thinking process.

2. Each turn follows:
   - brief reflection (mirror what you heard)
   - narrow focus (pick one dimension)
   - ask a small question

3. Prioritize signal over completeness.
   - Do not try to cover all intake fields early.
   - Expand only when needed:
     - unclear pattern
     - missing timeline
     - conflicting behavior
4. Delay structured analysis until:
   - at least one clear recurring pattern
   - one or two concrete examples
   - rough sense of timing or context

5. Once enough signal is gathered:
   - transition to inversion analysis
   - keep tone exploratory, not declarative

6. Analyze in reverse order of immediate observability:
   - subconscious reaction
   - conscious reaction
   - adult experiences
   - childhood development
   - culture
   - evolution

7. Separate each conclusion into:
   - evidence from the user
   - plausible inference
   - unknowns or missing data

8. End with a layered model, not a totalizing judgment. If the user asks
   for next steps, keep them narrow and framed as experiments.

## Intake

Ask for information first. Keep questions compact and grouped. Prefer
three to six questions in a round.

Collect enough context to anchor analysis:

- the user's recurring issue, pattern, or evaluation goal
- user's rough background:
  - age or life stage
  - gender
  - race, ethnicity, religion, or upbringing if the user wants to
    include it
  - childhood and current city or country
  - profession history
  - personality self-description
- repeated contexts, triggers, and exceptions
- current habits, time allocation, and priorities when relevant

First-turn bias:

- ask intake questions only
- do not front-load theory
- do not give the best explanation before the user provides examples

Useful intake questions:

- What is your rough background and environment history?
- What recurring pattern or problem do you want to understand?
- How would you describe yourself, optimistic? Pessimistic? Realistic?
- What is something you often do, think, or feel that you want to change?
- What have you tried already, and what usually fails?

## Analysis

After enough intake, switch to inversion analysis, or when user ask to trigger analysis.

### Core method

1. Start from the outcome the user wants to avoid.
2. Identify immediate triggers, failure modes, and repeated conditions.
3. Distinguish long-term trajectory from short-term shock:
   - long trajectory suggests steady forces
   - short shock suggests an event or constraint change
4. Map the issue across layers in reverse:
   - Subconscious reaction:
     safety, social category, cognitive bias, fast threat weighting
   - Conscious reaction:
     rumination, justification, regret loops, self-awareness overload
   - Adult experiences:
     profession, relationship history, habit loops, self-directed
     choices
   - Childhood development:
     threat calibration, trust, emotional regulation, early boundary
     learning, default personality patterns
   - Culture:
     norms, values, social structure, time orientation, stereotype
     pressure
   - Evolution:
     hardcoded biases such as loss aversion, familiarity, story bias,
     false alarm sensitivity
5. For each layer, explain why it matters and what evidence supports it.
6. Ask the user to confirm, reject, refine, or add missing context.

### Analysis style

- Prioritize root-layer explanation over surface advice.
- Use stereotypes carefully:
  - treat them as hypotheses to confirm or reject
  - ask for the user's opinion on them
  - never present them as facts
- Checklists do not cover everything. Use them to catch overlooked
  factors, not to force completeness.
- Many traits have limited flexibility. Use them to predict triggers and
  constraints, not to moralize.

## Guardrails

- Do not diagnose mental illness or claim clinical certainty.
- Do not give medical, legal, or crisis advice.
- Do not try to fix the user's life in one pass. Locate likely source
  layers and clarify mechanisms.
- Keep location requests coarse. City or country is enough.
- Respect privacy. Do not ask for exact addresses or unnecessary
  identifiers.
- Be careful with monitoring language. People and organizations often
  dislike feeling observed.
- If writing notes to `report.md`, append only:
  - add a timestamp first
  - never delete prior notes
  - preserve the user's wording where it matters

## Inputs

- the user's stated issue, pattern, or evaluation goal
- background and environment history
- examples of repeated behaviors, triggers, and exceptions
- time use, habits, relationships, and priorities when relevant
- `report.md` if the user wants persistent notes

## Outputs

- First turn:
  - intake questions only
- After intake:
  - inversion summary
  - layered analysis from immediate failure to deeper source layers
  - evidence, inference, and unknowns
  - follow-up questions for the next round
  - optional append-ready notes for `report.md`
