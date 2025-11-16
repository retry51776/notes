# OpenAI

## Agent RFT
>
> Finetune LLM to uses custom tools to generate structure output.

Different than RFT

- Multi Steps RL
- Context includes tool result
- Allow external reward signal
~ 100 Sample efficient

Prompt optimization -> Task & Tool division ->

Grader is our hosted http api;

Session start request prompt -> LLM tool(sess_id) -> tool_api -> LLM -> final_answer  -> grader_api -> json

<https://modal.com>
`Python create third-party serverless cloud SDK`
