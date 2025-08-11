# Aider

## architecture

- .message
  - .reasoning
  - .tool_call
    - .function

## Dependencies

- asyncclick `cli command framework`
- tree-sitter `code hierarchy scanner`
- watchfiles

> Until Visual LLM have architecture breakthrough, visual process always be slower than text(IMO forever). So for coding agent, unless there are information only exists in architecture diagram. Text LLM are always faster & better.

```bash
aider --model lm_studio/qwen3-30b-a3b
aider --model lm_studio/openai/gpt-oss-120b

/clear # will NOT clear /add files
/drop * # is required

# 128k context window = agent handle 3-5 files

# Undo fileX aider changed
git restore --source=abcb3187b27257798a6417523f7281ce4717b0f2^ -- /Users/terry/Documents/GitHub/notes/devOps/k8/traffic.md
git add /Users/terry/Documents/GitHub/notes/devOps/k8/traffic.md
git commit --amend --no-edit
```

execute_generator_loop
<https://github.com/Aider-AI/aider/blob/5e7ef6c50e58aab3c10c6b26cd38595da3e5a323/aider/coders/base_coder.py#L845>

- LLM
  - exception
    - network
    - ContextWindowExceededError
  - KeyboardInterrupt
