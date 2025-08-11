# Example

Agent
- `create_prompt()`
- `_extract_tool_and_input()`

```py
AgentExecutor._call()
    intermediate_steps = []
    while self._should_continue():
        next_step_output = self._take_next_step()
            actions = self.agent.plan()
                # decide the next step based on intermediate_steps
                # output = self.llm_chain.run(
                #     intermediate_steps=intermediate_steps, stop=self.stop, **kwargs
                # )
                # return self.output_parser.parse(output)

            if isinstance(output, AgentFinish):
                return output

            result = []
            for agent_action in actions:
                observation = tool.run(
                    agent_action.tool_input,
                    verbose=self.verbose,
                    color=color,
                    **tool_run_kwargs,
                )
                result.append((agent_action, observation))

        if isinstance(next_step_output, AgentFinish):
            return
        intermediate_steps.append(next_step_output)
    return self.agent.return_stopped_response()
```

```python
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """The way you use the tools is by specifying a JSON blob.
Specifically, this JSON should have an `action` key (the name of the tool to use) and an `action_input` key (the input for that tool).

The only values allowed in the "action" field are: {tool_names}

The $JSON_BLOB must contain a SINGLE action; do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:

{{{{
  "action": $TOOL_NAME,
  "action_input": $INPUT
}}}}

ALWAYS use the following format:

Question: the input question you must answer  
Thought: you should always think about what to do  
Action:
$JSON_BLOB

Observation: the result of the action  
... (this Thought/Action/Observation can repeat N times)  
Thought: I now know the final answer  
Final Answer: the final answer to the original input question"""
SUFFIX = """Begin! Reminder to always use the exact characters `Final Answer` when responding."""
```

#1: python controller: should I continue?  
#2: LLM: ask plan for given question  

- 2a: AgentFinish – LLM returns an answer; end.  
- 2b: AgentAction – LLM decides: [{tool, tool_input}, {tool, tool_input}]  

    - `_extract_tool_and_input()` extracts the tool and its input from the LLM output.  

#3: Loop over AgentAction

Agent (chain)  

- `_call()`  
  - `_take_next_step()`  
    - `plan()` decides what to do given the input  
      1. `get_full_inputs()`  
      2. `_get_next_action()`  
         - `_extract_tool_and_input()` extracts tool and tool input from LLM output  
      3. If a Final Answer is obtained, exit early  

- `return_values`

**Questions:**  

- What is the agent’s responsibility? Deciding which tools to use?  
- Does the agent parse output from one tool to another?

Chain lifecycle  

- `prep_inputs()`  
- `run()` – performs tasks such as web search, database query, LLM call, script execution, etc.  
- `prep_outputs()`

- `input_keys` control input values for the prompt  
- `output_keys` control output of the prompt  
- `memory`  
- `verbose` – see how it thinks

**Tool lifecycle (required name, description, return_direct)**  

- `run()`  

  - `name: str`  
  - `description: str`  
  - `return_direct: bool = False`  
  - `verbose: bool = False`  
  - `callback_manager?` – how to use?

Given the tools below:

- toolA: do XYZ  
- toolB: do ABC  

**MRKL Systems (Modular Reasoning, Knowledge and Language)**  

Sometimes an AI agent will break when the LLM does NOT follow directions to generate the next‑step response.````

ai/README.md
