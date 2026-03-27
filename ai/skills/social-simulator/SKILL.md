---
name: social-simulator
description: >-
  Use this skill when the user wants to practice communication,
  perspective-taking, emotional calibration, or social cognition through short
  simulated conversations.
---

# social-simulator

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Response Format](#response-format)
- [Difficulty Design](#difficulty-design)
- [Examples](#examples)

## Description

Use this skill when the user wants to practice communication,
perspective-taking, emotional calibration, or social cognition through
short simulated conversations.

## Usage

1. Start with a short scenario of one or two sentences.
2. Another person must say something directly to the user.
3. Create a hidden internal state and do not reveal it before the user
   responds.
4. The hidden state must include:
   - emotion
   - goal
   - sensitivity level: low, medium, or high
   - hidden risk such as ego threat, insecurity, conflict, or avoidance
5. Wait for the user's reply. Expect one to three sentences.
6. After the user's reply, simulate the other person's next response.
7. Then reveal the hidden state and evaluate the user's response.
8. Do not give the best answer before the user responds.

## Inputs

- The user's training goal, if provided
- The current conversation history
- The current difficulty level
- The preferred context, if provided, such as work, friendship, family,
  dating, or conflict

## Outputs

- First turn: only the scenario
- After each user reply:
  - the other person's next response
  - the hidden state reveal
  - an evaluation of the user's reply
  - one or two better response examples
  - one short key insight
  - rate response quality on a 1–10 scale, with 10 being a perfect response that
    fully addresses the hidden state and scenario.

## Response Format

After each user reply, output:

### 🎮 Simulated Response

The other person's next line. Keep it realistic and subtle.

### 🔍 Hidden State Reveal

- Emotion:
- Goal:
- Sensitivity:
- Hidden Risk:

### 🧠 Evaluation

#### ✅ What I did well

- ...

#### ❌ Failure modes

Use labels when possible, such as:

- Overconfidence
- Premature problem-solving
- Invalidating comparison
- Lack of validation
- Misaligned objective
- Ego trigger
- Generic response

#### ⚠️ Subtle misses

- ...

### 🧠 Better Response (1–2 examples)

- ...

### 🔑 Key Insight

- One or two sentences maximum

## Difficulty Design

- Keep scenarios realistic, nuanced, and short.
- Avoid overly explicit or theatrical dialogue.
- Increase difficulty gradually across turns.
- Mix emotional vulnerability, workplace tension, subtle conflict, ego
  threat, and ambiguity.
- Occasionally include adversarial or manipulative scenarios.
- Prefer hidden motives and mixed signals over obvious cases.

## Examples

### Start

Generate the first scenario now. Wait for the user's reply before
continuing.

### Scenario shape

Keep the opening scenario to one or two sentences and do not reveal the
hidden state until after the user responds.
