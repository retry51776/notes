# Experience

## LLM provider

- Token Cost
  - Self Host are most expensive, & slow
  - Deepseek is cheapest
  - <https://www.llmpricehub.com/compare/>
- Capability
  - Max context window size
  - (image, audio, video, or special capability)
  - Cache
    - Auto KV cache?
    - Some provider have adv KV cache support different prefix
  - RL fine tune
- SLA
  - P90/P95
  - fallback
  - Certification
- Security
  - self host
  - Data privacy agreement

## Automation

- We assume whatever atomic logic/behavior are ALREADY LEARNED within LLM training, if not no instruction will get LLM doing it.

- Control ~ Work. Many expects works magically done by LLM, which can be true in some cases. But also means in dynamic system, LLM is domaine force, and human give up control. We must list out fundamental forces in workflow or system, how they balance each other to create equilibrium. Human control always translate into work effort.

- Should automate application that less time sensitive, easy to evaluation.

- ALWAYS go for LONG prompt/input LOW decode/output ratio. (decode token ~ 10x prefill token, also prefill faster)
  - The key resolution/accuracy measure token efficiency. ~ `task_value / token_cost`


## Test

- Prompt
- Right now RL fine tune/Continue Learning still not mainstream. We still requires LLM with detail instruction on every job execution. Hopefully some cache strategy will can let LLM execute without detail instruction.

## LLM Tips

- """use parallel subagents to XXX"""
- Explain in mechanistic terms, not marketing terms.
- For extraction task, tell LLM assigned default value when no info, and do not make any assumptions.
- AI sucks at Abbreviation, expand all abbreviation before understanding task.
- LLM is very TALKY, it will do instruction, but it also need a lot monolog between it's output.
  - `Format each xxx in a new line as ("xxx"{tuple_delimiter}<p1>{tuple_delimiter}<p2>{tuple_delimiter}<p3>{tuple_delimiter}<record_delimiter>)`
  - `Add {start_delimiter} & {end_delimiter}`
- Let LLM response in markdown section, Problem with json response is that it constrain verbosity of LLM response. Both input & output should be markdown, because LLM usually prefer markdown than json in my experience.

- "Recall a related problem, and then solve this one." `because Retrieval + reasoning > reasoning only`

- special instructions embedded in prompts
  - adds `/no_think` before prompt to disable thinking mode (In qwen3)
  - `/fast` or `/quick`
  - `/no_history`

- Prompt Order
  - 1) Goal
  - 1) Constrain Rule (Avoid & Deny)
  - 1) Details
    - LLM prefer Json, Array to let LLM understand relationship
    - Use text section splittGFer
    - json.dumps(xxx, indent=4) for better readability
  - 1) Instruction
    - Do NOT provider script, or steps to solve
    - Please respond **strictly** in the following JSON format, without additional keys or text:
    - expected value for each key
    - Always return a json dictionary, define key, value is type.
  - prompting guide <a href="https://docs.anthropic.com/claude/docs/introduction-to-prompt-design">Anthropic</a>
   <a href="https://huggingface.co/docs/transformers/main/tasks/prompting#best-practices-of-llm-prompting">Hugging Face</a>
   or <a href="https://www.promptingguide.ai/introduction/elements">PromptingGuide</a>.
- Because by law even production code requires to keep its dependence license info.
  - `grep https xx.js` collects more false passivity, but should cover most dependencies
  - `grep github.com xx.js` most likely dependencies linkss

- LLM future improvement
  - habit simulation
    - Learned Gating Mechanisms
    -

## Useful Prompts

```md
IMPORTANT: You should NOT answer with unnecessary preamble or postamble (such as explaining your code or summarizing your action)

If you can answer in 1-3 sentences or a short paragraph, please do

Explain above code & give a Quick Visualization
```
