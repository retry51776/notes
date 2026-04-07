---
theme: default
title: Vehicle Analogy
transition: slide-left
layout: two-cols-header
mdc: true
---

<style>
:root {
  --road: #111827;
  --steel: #1f2937;
  --slate: #475569;
  --mist: #e2e8f0;
  --sky: #0ea5e9;
  --amber: #f59e0b;
  --sand: #fff7ed;
}
.slidev-layout {
  background:
    radial-gradient(circle at top left, rgba(14, 165, 233, 0.08), transparent 28%),
    radial-gradient(circle at top right, rgba(245, 158, 11, 0.12), transparent 34%),
    linear-gradient(180deg, #f8fafc 0%, #fff7ed 100%);
  color: var(--road);
}
.eyebrow {
  @apply inline-block rounded-full border px-3 py-1 text-xs font-semibold uppercase tracking-widest;
  border-color: rgba(71, 85, 105, 0.3);
  color: var(--slate);
  background: rgba(255, 255, 255, 0.65);
}
.hero-icon {
  font-size: 4.5rem;
  line-height: 1;
}
.grid-3 {
  @apply mt-8 grid grid-cols-3 gap-4;
}
.grid-2 {
  @apply grid grid-cols-2 gap-4;
}
.tile {
  @apply rounded-2xl border p-4 shadow-sm;
  border-color: rgba(148, 163, 184, 0.28);
  background: rgba(255, 255, 255, 0.78);
}
.tile-dark {
  @apply rounded-2xl border p-4 shadow-sm text-white;
  border-color: rgba(255, 255, 255, 0.08);
  background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
}
.tile-title {
  @apply mb-1 text-sm font-semibold uppercase tracking-wide;
  color: var(--slate);
}
.tile-dark .tile-title {
  color: #cbd5e1;
}
.mini {
  @apply text-sm leading-5;
  color: #475569;
}
.tile-dark .mini {
  color: #cbd5e1;
}
.big {
  @apply text-2xl font-semibold leading-tight;
}
.arrow {
  @apply flex items-center justify-center text-3xl font-bold;
  color: var(--amber);
}
.callout {
  @apply mt-6 rounded-2xl border-l-4 px-4 py-3 text-base leading-6;
  border-left-color: var(--amber);
  background: rgba(255, 255, 255, 0.72);
}
.footnote {
  @apply mt-4 text-xs leading-5;
  color: #64748b;
}
.metric {
  @apply rounded-xl px-3 py-2 text-sm font-medium;
  background: rgba(14, 165, 233, 0.08);
  color: #0f172a;
}
.roadline {
  @apply mt-6 rounded-full px-4 py-2 text-sm font-semibold text-white;
  background: linear-gradient(90deg, #0f172a 0%, #1e293b 60%, #334155 100%);
}
.compare {
  @apply flex items-center gap-3 rounded-xl border px-4 py-3;
  border-color: rgba(148, 163, 184, 0.28);
  background: rgba(255, 255, 255, 0.7);
}
.compare .lhs {
  @apply w-1/2 text-right font-semibold;
}
.compare .rhs {
  @apply w-1/2 font-semibold;
}
.compare .mid {
  color: var(--amber);
}
.caption {
  @apply mt-2 text-xs uppercase tracking-widest;
  color: #94a3b8;
}
.tight li {
  margin-bottom: 0.35rem;
}
.cover-image {
  @apply h-80 w-full overflow-hidden rounded-2xl border shadow-lg;
  border-color: rgba(255, 255, 255, 0.12);
}
.cover-image img {
  @apply w-full object-cover;
}
.engine-light {
  color: #f59e0b;
}
</style>


::left::

# AI System Components

- LLM
- Agentic System
- Mission

::right::

<img
  src="https://i0.wp.com/takebackroads.com/wp-content/uploads/2022/03/mountain-back-road-2.jpg"
  alt="Mountain back road"
/>

<div class="absolute bottom-4 left-0 w-full text-center text-sm text-gray-400">
  Agent ~ Context Engineering + DevOps's CICD
</div>

---
layout: default
---

## Analogy Overview
<div class="grid-3 items-center text-center">
  <div class="tile">
    <div class="big">LLM</div>
    <hr />
    <div class="big">Propulsion System</div>
    <svg class="engine-light mx-auto mb-2 h-16 w-16" xmlns="http://www.w3.org/2000/svg" id="mdi-engine" fill="none"
  stroke="currentColor"
  stroke-width="1" viewBox="0 0 24 24">
      <path d="M7,4V6H10V8H7L5,10V13H3V10H1V18H3V15H5V18H8L10,20H18V16H20V19H23V9H20V12H18V8H12V6H15V4H7Z" /></svg>
  </div>
  <div class="tile">
    <div class="big">Agentic System</div>
    <hr />
    <div class="big">Vehicle Operation</div>
    <svg
      class="mx-auto mb-2 h-16 w-16 text-sky-600"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      aria-label="Steering wheel icon"
    ><path d="M13,19.92C14.8,19.7 16.35,18.95 17.65,17.65C18.95,16.35 19.7,14.8 19.92,13H16.92C16.7,14 16.24,14.84 15.54,15.54C14.84,16.24 14,16.7 13,16.92V19.92M10,8H14L17,11H19.92C19.67,9.05 18.79,7.38 17.27,6C15.76,4.66 14,4 12,4C10,4 8.24,4.66 6.73,6C5.21,7.38 4.33,9.05 4.08,11H7L10,8M11,19.92V16.92C10,16.7 9.16,16.24 8.46,15.54C7.76,14.84 7.3,14 7.08,13H4.08C4.3,14.77 5.05,16.3 6.35,17.6C7.65,18.9 9.2,19.67 11,19.92M12,2C14.75,2 17.1,3 19.05,4.95C21,6.9 22,9.25 22,12C22,14.75 21,17.1 19.05,19.05C17.1,21 14.75,22 12,22C9.25,22 6.9,21 4.95,19.05C3,17.1 2,14.75 2,12C2,9.25 3,6.9 4.95,4.95C6.9,3 9.25,2 12,2Z" /></svg>

  </div>
  <div class="tile">
    <div class="big">Mission</div>
    <hr />
    <div class="big">Destination</div>
    <div class="hero-icon">🎯</div>
  </div>

</div>

---
layout: section
---

# LLM
<hr />

# Propulsion System
<svg class="engine-light mx-auto mb-2 h-35 w-35" xmlns="http://www.w3.org/2000/svg" id="mdi-engine" fill="none"
  stroke="currentColor"
  stroke-width="1" viewBox="0 0 24 24">
      <path d="M7,4V6H10V8H7L5,10V13H3V10H1V18H3V15H5V18H8L10,20H18V16H20V19H23V9H20V12H18V8H12V6H15V4H7Z" /></svg>

### Powerful, high-complexity

---
layout: default
mdi: true
---

## 1. Propulsion System Analogy
<div class="mb-2 flex items-center gap-3">
  <svg class="engine-light h-16 w-16" xmlns="http://www.w3.org/2000/svg" id="mdi-engine" fill="none"
    stroke="currentColor"
    stroke-width="1" viewBox="0 0 24 24">
        <path d="M7,4V6H10V8H7L5,10V13H3V10H1V18H3V15H5V18H8L10,20H18V16H20V19H23V9H20V12H18V8H12V6H15V4H7Z" /></svg>
  <svg class="engine-light h-12 w-16"  version="1.1" id="_x32_" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <style type="text/css"> .st0{fill:#000000;} </style> <g> <path class="st0" d="M485.395,158.609c-7.296-8.514-12.122-13.426-20.826-22.348c-27.93-28.573-53.191-53.843-53.218-53.869 l-12.591-12.6l-17.435,17.026l36.061,54.731l0.374,0.765c0.191,0.591,0.374,1.566,0.374,2.826c0.052,2.704-0.974,6.609-2.479,9.313 l-3.165,5.826c-3.661,6.756-5.713,21.113-5.705,28.574c-0.008,7.182,1.696,14.4,5.114,20.982l6.235,12.026 c7.295,14.07,21.347,23.148,36.991,24.348l3,0.939c0,39.574,0,88.904,0,126.835c-0.052,11.043-3.296,17.617-6.888,21.635 c-3.652,3.991-7.965,5.634-11.913,5.644c-3.826-0.07-7.217-1.348-10.417-4.948c-3.13-3.617-6.365-10.295-6.4-22.33 c0-35.618,0-44.522,0-66.783c-0.009-7.113-1.436-14.156-4.044-20.974c-3.93-10.191-10.601-20-20.348-27.582 c-9.678-7.583-22.678-12.592-37.226-12.539c-1.704,0-3.425,0.096-5.164,0.226V47.956C355.726,21.469,334.256,0,307.769,0H97.378 C70.891,0,49.422,21.469,49.422,47.956v406.166H18.256V512h368.634v-57.878h-31.165V282.174c1.843-0.27,3.6-0.452,5.164-0.452 c4.496,0.017,8.01,0.93,11.096,2.4c4.592,2.192,8.374,5.896,11.026,10.348c2.67,4.382,3.922,9.461,3.879,12.73 c0,22.261,0,31.165,0,66.783c-0.035,18.556,5.312,34.417,15.13,45.695c9.739,11.305,23.66,17.279,37.304,17.209 c14.183,0.008,28.174-6.165,38.296-17.339c10.174-11.165,16.174-27.148,16.122-45.565c0-57.878,0-150.261,0-185.878 C493.743,171.409,492.074,166.4,485.395,158.609z M284.491,227.061H120.656V71.235h163.834V227.061z M458.126,212.009 c0,2.808-1.609,4.122-3.896,4.078c-4.304-0.07-11.009-1-13.913-5.722c-5.191-8.435-12.183-24.87-4.609-37.756 c0.808-1.374,2.574-3.583,5.722-1.478l10.13,9.304c4.182,3.826,6.565,9.226,6.565,14.895 C458.126,195.33,458.126,209.2,458.126,212.009z"></path> </g> </g></svg>


</div>


- modality | LLM support data types ~ fuel type
- context window size ~ fuel tank size
  - generation token ~ engine cycle
      - inference cost ~ gasoline
    - weight/param ~ engine block
    - architecture ~ engine design
      - transformer ~ four-stroke cycle(most common engine design)
        - attention heads/experts ~ cylinders
        - hidden state(KV cache) ~ vehicle momentum / inertia
- roles `system | developer | user | assistant | tool` ~ control priority

---
layout: two-cols-header
---

## 1. LLM Considerations


::left::

<div class="space-y-3 mt-2">
  <div class="tile">
    <div class="tile-title">Data Type</div>
    <div class="mini">
      modality -> text, audio, image, video, multimodal support
    </div>
  </div>
  <div class="tile">
    <div class="tile-title">Context Window</div>
    <div class="mini">
      context window -> how much task state can be carried at once
    </div>
  </div>
  <div class="tile">
    <div class="tile-title">LLM size</div>
    <div class="mini">
      LLM size -> capability up, speed down, compute up
    </div>
  </div>
  <div class="tile">
    <div class="tile-title">AI Budget</div>
    <div class="mini">
      inference cost -> what it takes to keep the trip moving
    </div>
  </div>
</div>

::right::

<img class="ml-auto w-100" src="https://media.roughcountry.com/media/wysiwyg/C-9a-jeep_truck.jpg">

---
layout: section
---

# Agentic System / Harness
<hr />

# Vehicle Operation
<svg
      class="mx-auto mb-2 h-35 w-35 text-sky-600"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      aria-label="Steering wheel icon"
    ><path d="M13,19.92C14.8,19.7 16.35,18.95 17.65,17.65C18.95,16.35 19.7,14.8 19.92,13H16.92C16.7,14 16.24,14.84 15.54,15.54C14.84,16.24 14,16.7 13,16.92V19.92M10,8H14L17,11H19.92C19.67,9.05 18.79,7.38 17.27,6C15.76,4.66 14,4 12,4C10,4 8.24,4.66 6.73,6C5.21,7.38 4.33,9.05 4.08,11H7L10,8M11,19.92V16.92C10,16.7 9.16,16.24 8.46,15.54C7.76,14.84 7.3,14 7.08,13H4.08C4.3,14.77 5.05,16.3 6.35,17.6C7.65,18.9 9.2,19.67 11,19.92M12,2C14.75,2 17.1,3 19.05,4.95C21,6.9 22,9.25 22,12C22,14.75 21,17.1 19.05,19.05C17.1,21 14.75,22 12,22C9.25,22 6.9,21 4.95,19.05C3,17.1 2,14.75 2,12C2,9.25 3,6.9 4.95,4.95C6.9,3 9.25,2 12,2Z" /></svg>

### Agentic System is **Persistent**, unlike LLM is **Ephemeral**.

---
layout: two-cols-header
---

## 2. Agentic System components

<br />


::left::
- 1. workflow instruction ~ driver handling control

- 2. task context ~ driving route
incomplete route

- 3. agent tools ~ vehicle attachments

- 4. **memory system** ~ driving history | experience


- 5. evaluation system ~ test drive

- 6. agent profiles ~ different driver profiles

- 7. status management ~ turning signal
::right::

<img src="https://media1.tenor.com/m/unu0esewTrcAAAAC/horse-animal.gif"  class="ml-auto w-40"/>

<small>Agentic System also call **Harness**, <br/>similar horse harness give rider control over horse.</small>


<div class="absolute bottom-4 left-0 w-full text-center text-sm text-gray-400">
  Different Agentic System has different designs, we cover common components here.
</div>

---
layout: two-cols-header
---

::left::
## 2.1 Workflow instruction

<br/>

- Inputs Expectation
- Instructions
  - Rules
  - Avoid
- Resources | References
    - Dynamic: Tools
    - Static: References
- Outputs Expectation

::right::

## 2.2 Task context
<br/>

- Injection attack | conflict direction
- Dynamic per task
- Achievable task?
  - Prompt ambiguity ~ ambiguity route
  - Lazy delegation ~ incomplete route
  - Has tool permission?
  - Is LLM smart enough?


<div class="absolute bottom-4 left-0 w-full text-center text-sm text-gray-400">
Balance between workflow instruction vs task context

    - conflict directions
    - maintain momentum | progress
</div>

---
layout: default
---

## 2.3 Tools

### Tools like attachment, extend what the vehicle can do on the trip

<div class="grid grid-cols-3 gap-6 mt-6">
  <div class="tile">
    <div class="text-center">
      <div class="hero-icon">🧰</div>
      <div class="big">Skills</div>
      <div class="mini mt-1">lazy loading detail</div>
    </div>
    <div class="grid grid-cols-3 gap-3 mt-5 text-center">
      <div class="rounded-xl bg-slate-100 px-3 py-4">
        <div class="text-3xl">💻</div>
        <div class="mt-2 text-sm font-semibold">Terminal</div>
      </div>
      <div class="rounded-xl bg-slate-100 px-3 py-4">
        <div class="text-3xl">🧪</div>
        <div class="mt-2 text-sm font-semibold">Simulator</div>
      </div>
      <div class="rounded-xl bg-slate-100 px-3 py-4">
        <div class="text-3xl">🧱</div>
        <div class="mt-2 text-sm font-semibold">Sandbox</div>
      </div>
    </div>
  </div>
  <div class="tile text-center flex flex-col justify-center">
    <div class="hero-icon">⌨️</div>
    <div class="big">Commands</div>
    <div class="mini mt-1">user manual trigger</div>
  </div>
  <div class="tile text-center flex flex-col justify-center">
    <div class="hero-icon">🔌</div>
    <div class="big">MCP</div>
    <div class="mini mt-1">external tools and systems</div>
  </div>
</div>

<div class="callout">
  Recommend create custom skills for static knowledge, or custom workflow, internal tools.
</div>

---
layout: two-cols-header
---

## 2.4 Memory System
<br />

### Persistent storage and management

::left::

<div class="space-y-3 mt-2">
  <div class="tile">
    <div class="tile-title">Working Memory</div>
    <div class="mini">working memory -> driving state</div>
    <div class="mini">KV cache -> current momentum / engine state</div>
    <div class="mini">context rot -> driver fatigue</div>
  </div>
</div>

::right::

<div class="space-y-3 mt-2">
  <div class="tile">
    <div class="tile-title">Persistent Memory</div>
    <div class="mini">vehicle records, trip history, manuals, habits</div>

  </div>
</div>

- Skills (reusable process and semantic memory)
  - SKILL.md
    - name & description
    - main instructions
  - /reference
- session.md
- CLAUDE.md (project-level persistent profiles update by dream)


<div class="absolute bottom-4 left-0 w-full text-center text-sm text-gray-400">
  Restore state by loading episodic memory. Forked sessions and parallel
  workers are easier when the memory hierarchy is explicit.
</div>

---
layout: two-cols-header
---

## 2.7 Status Management
<br />

::left::

- Different Status
- Status Hooks
  - Auto Pipeline | Handler
  - Approval Confirmation
  - Logging
- Status Visibility & Update

::right::

<img class="w-50" src="https://www.roadtrafficsigns.com/img/lg/K/use-turn-signal-sign-k-0060.png" alt="Turn signal road sign" />

---
layout: section
---

# Mission
<hr />

# Destination

<div class="hero-icon">🎯</div>

### Planning vs Action

---
layout: two-cols-header
---

## 3. Mission Framing

::left::

<div class="tile mt-4">
  <div class="tile-title">Agentic Thinking</div>
  <ul class="tight mini mt-2">
    <li>Break long trips into sections.</li>
    <li>Avoid context rot before the route gets sloppy.</li>
    <li>Use parallel workers and forked sessions where useful.</li>
    <li>Clear session for clean evaluation and restore progress.</li>
  </ul>
</div>


<div class="tile mt-4">
  <div class="tile-title">Agentic Action</div>
  <ul class="tight mini mt-2">
    <li>Driving and exploration must stay consistent with the plan.</li>
    <li>Handiness means using the right tool effectively.</li>
    <li>Progress only counts if it still points at the destination.</li>
  </ul>
</div>

::right::
<div class="flex flex-col items-end tight mini mt-2">

<img class="w100" src="https://uffizio.com/wp-content/uploads/2023/12/Route-Planning.jpg">
Destination vs Exploration
<img class="w60" src="https://upload.wikimedia.org/wikipedia/commons/f/f5/BFS-Algorithm_Search_Way.gif">
</div>

---
layout: default
---

## Context Rot

### LLMs also fatigue on long prompt

<div class="grid-2 mt-6">
  <div class="tile">
    <div class="tile-title">What happens</div>
    <div class="mini">
      Large KV cache becomes slower, more expensive, and less precise.
    </div>
  </div>
  <div class="tile">
    <div class="tile-title">Why it matters</div>
    <div class="mini">
      Later positions can suffer from reduced relevance and weaker
      sensitivity to important details.
    </div>
  </div>
</div>

<div class="callout">
  Route resets, summaries, checkpoints, and fresh sessions are not
  optional hygiene. They are control systems.
</div>

<div class="absolute bottom-4 left-0 w-full text-center text-sm text-gray-400">Consider different Agent profiles(with different LLM engine) for different mission sections.</div>

---
layout: two-cols-header
---

## Misson

<br />
::left::

- Input & Output
  - High variances?
  - Modality | data type
  - Time Horizon
- Clear direction / Path?
- User has goal but not direction
   - Generate opinions, user choose
   - Abort

::right::

- Common Pitfall
  - Avoid
  - Update instruction
  - New tools
  - Switch LLM
  - Failure handler

- Monitor System
  - trace
  - feedback

---
layout: two-cols-header
---

# Exploration Considerations

<br />

- Break mission into sections
  - Information (Intent | lazy delegation) Drop
  - Different agents(LLM, Instructions, Tools) for different sections
  - Lost Coherence
- Searching Approach
  - Backtracking
  - Cost & Speed
  - Compare multiple answers
- Complexity vs Maintainability
  - Monitoring
  - Scheduler
  - Session / State Management

---
layout: statement
---

## Open Question

---
layout: fact
---

## Closing Point

Better destination design, route chunking, and evaluation often beat
small gains in engine size.

<div class="mt-8 grid grid-cols-2 gap-6">
  <div class="tile text-center">
    <div class="hero-icon">🏎️</div>
    <div class="mini mt-2">
      A good driver in a small go-kart can still finish the route.
    </div>
  </div>
  <div class="tile text-center">
    <div class="hero-icon">🚚</div>
    <div class="mini mt-2">
      A heavy-duty truck is not automatically better on every road.
    </div>
  </div>
</div>

---
layout: end
---

## End

<div class="mini mt-6">
  A usable mental model for debugging agent systems:
  engine limits, harness quality, task shaping, and feedback loops.
</div>
