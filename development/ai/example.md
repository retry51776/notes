# Example


Agent
- `create_prompt()`
- `_extract_tool_and_input()`
- 

```py
AgentExecutor._call()
    intermediate_steps = []
    while self._should_continue():
        next_step_output = self._take_next_step()
            actions = self.agent.plan()
                # decide next step base on intermediate_steps
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


```
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are: {tool_names}

The $JSON_BLOB should only contain a SINGLE action, do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:

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
  #2a: AgentFinish: LLM return answer; End
  #2b: AgentAction: LLM decided: [{tool, tool_input}, {tool, tool_input}]
    - _extract_tool_and_input() Extract tool and tool input from llm output.
  #3: Loop AgentAction

Agent(chain)
  - `_call()`
    - `_take_next_step()`
      - `plan()` Given input, decided what to do
        - 1. `get_full_inputs()` 
        - 2. `_get_next_action()`
          - `_extract_tool_and_input()` Extract tool and tool input from llm output
        - 3. if got Final Answer, early exit
        - 4. 

  - `return_values`

? Agent is a chain, what is agent responsibility? Decides on which tools?
does agent responsible for parse output from one tool to another?

chain lifecycle
  - `prep_inputs()`
  - `run()` do stuff here; Ex: google search, db search, call llm, run script,
  - `prep_outputs()`

  - `input_keys` control input_values to prompt
  - `output_keys` control output of prompt
  - `memory`
  - `verbose` see how it think

? is it chain's job to know what agent expect resp?

tool lifecycle(just required name, desc, return_direct)
  - `run()`

  - name: str
  - description: str
  - return_direct: bool = False
  - verbose: bool = False
  - callback_manager ? how to use?
Given below tools
-----
tools:

toolA: do XYZ
toolB: do ABC

MRKL Systems (Modular Reasoning, Knowledge and Language)
-----
Sometime AI Agent will break when LLM did NOT follow direction to generate next step response.