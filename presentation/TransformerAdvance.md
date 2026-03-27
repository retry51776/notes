---
theme: default
title: Transformer Advance
defaults:
  layout: image
  image: /codex-assets/slidev-light-background.svg
---
# Transformer Adv

<script setup>
import { onMounted } from 'vue'
import { useNav } from '@slidev/client'

const { next, go, currentPage, total } = useNav()

onMounted(() => {
  const switch_sec = 5, stop_slide_index = total.value;

  setInterval(() => {
    if (currentPage.value === stop_slide_index) {
      go(1)
    } else {
      next()
    }
  }, switch_sec * 1000)
})
</script>

<v-clicks>

- 🧠 Architecture
- ⚡ Performance
- Future Direction

</v-clicks>

---

# REQUIRES BASIC

Here we assumed you KNEW everything in Transformer Explain.

<v-clicks depth="3">

- Residual Stream
  - Attention Block
    - Query, Key, Value
    - Attention Score
    - Softmax Function
  - MLP BLOCK
  - Residual Connection
  - Circuit/Feature/Manifold
    - Steering Control

</v-clicks>

---

# TRAINING BASIC

<v-clicks depth="3">

- Pretrain
  - Pretrain ~ 4x RAM of BATCH inference
    - Compute is NOT bottleneck, RAM space is real bottleneck
    - Activation Checkpoint ~ recompute over storage
  - Back propagation
    - Learning Rate, Decay Rate
    - Direction & momentum
    - Weight decay

    - Optimizer
      - (NEW)muon optimizer: Matrix aware tracking vs individual weight tracking

- Reinforcement Learning Pipeline
  - RLHF
  - RL Verifiable Result (industry focus)
  - Optimizer
    - KL divergence

</v-clicks>

---

# TRAINING ADV

- How to Parallel? MP, PP, TP, DP?
  - Why Pipeline Parallel(PP) is BAD design except in pretrain.
    - PP means ONLY nodeX MUST wait for early node finish. Unless you guaranty none stop workflow, there ONLY a **single active node**.
    - TP Tensor Parallelism most likely better.
  - Why MOE makes this more complex?

---

# INFERENCE BASIC

<v-clicks depth="3">

- Why Prefill?
  - Calculate KV cache.
  - Why we need KV cache?
    - KV cache ~ Token's meaning. Aka number/force applied to next token
- Why decode need sequential?
  - There are many researches/approaches.
    - 1. Some COT can async
    - 1. Concise reduce token: uses pure vector replace human readable COT
    - 1. Multiple COTs

</v-clicks>

---

# IMO

- All inference weights does one of:
  - interactions
    - projection (expand or compress)
    - MLP
  - routing
    - MOE Gating
    - Attention Score
  - stabilization
    - Norm Layers

---

## Why ATTENTION matters?

- Why MLP CAN'T replace ATTENTION?
  - MLP has SAME operation on every Residual Stream.
  - Attention has DIFFERENT interactions on every token of RS.
- ATTENTION is O(n^2) operations on compute & RAM
  - Linear Attention ~ RNN
  - Spare Attention ~ Attend only top-k tokens
- What is MLP purpose?
  - Global feature extraction.
  - This is where interaction/compute happens. MLP cost 80% compute.

---

## RNN Problem

- RNN ~ Linear Attention
  - RNN has fixed size state, which always has limited capacity.
  - It can't parnell in pretrain, which Transformer can. Reference: Prefill

- Why Linear Attention can fix RNN now?
  - We INCREASE state size much bigger, it's capacity should enough for most use cases.
  - Pretrain no longer the main cost, inference & RL matters more now.
  - RAM pressure is main bottleneck, not compute.

---

## Context Window Constrains

- Position Encoding
  - YARN works at most ~ 1 million tokens
  - PE works by rotate RS different rate at different channels.
    - The problem is fast rotate freq channels is useless in long context. Ex: minutes is worthless in time scale of Earth.
- LONG Context Training Data is Lack/Expensive

---

# Training

<v-clicks>

## Back propagation problems

- When initialization random numbers, early layers BP signal are mostly NOISE.
- Early layers or farther away gets weak signal. That's why hard to scale layers beyond 100 layers. Also why residual connection useful.

</v-clicks>

---

## Security

- Remove or escape reserve token, such as `<|start|>`, `<|end|>`.
  - Most modern LLM already trained prevent injection attacks, but avoid strange LLM behavior.
- Use `role` in message define priority for instruction.

---

layout: center
---

## Thank You
