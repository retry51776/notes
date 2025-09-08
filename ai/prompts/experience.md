# Experience

**LLM Tips**

- """use parallel subagents to XXX"""
- For extraction task, tell LLM assigned default value when no info, and do not make any assumptions.
- AI sucks at Abbreviation, expand all abbreviation before understanding task.
- LLM is very TALKY, it will do instruction, but it also need a lot monolog between it's output.
  - `Format each xxx in a new line as ("xxx"{tuple_delimiter}<p1>{tuple_delimiter}<p2>{tuple_delimiter}<p3>{tuple_delimiter}<record_delimiter>)`
  - `Add {start_delimiter} & {end_delimiter}`
- Let LLM response in markdown section, Problem with json response is that it constrain verbosity of LLM response. Both input & output should be markdown, because LLM usually prefer markdown than json in my experience.

- "Recall a related problem, and then solve this one." `because Retrieval + reasoning > reasong only`

- special instructions embedded in prompts
  - adds `/no_think` before prompt to disable thinking mode (In qwen3)
  - `/fast` or `/quick`
  - `/no_history`

- Prompt Order
  - 0) Avoid & Deny List
  - 1) Context
    - LLM prefer Json, Array to let LLM understand relationship
    - Use text section splittGFer
    - json.dumps(xxx, indent=4) for better readability
  - 2) Instruction
    - Do NOT provider script, or steps to solve
    - Please respond **strictly** in the following JSON format, without additional keys or text:
    - expected value for each key
    - Always return a json dictionary, define key, value is type.
- Because by law even production code requires to keep its dependence license info.
  - `grep https xx.js` collects more false passivity, but should cover most dependencies
  - `grep github.com xx.js` most likely dependencies linkss

- LLM future improvement
  - habit simulation
    - Learned Gating Mechanisms
    -

## Useful Prompts

```
IMPORTANT: You should NOT answer with unnecessary preamble or postamble (such as explaining your code or summarizing your action)

If you can answer in 1-3 sentences or a short paragraph, please do

Explain above code & give a Quick Visualization
```
