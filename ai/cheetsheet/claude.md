# Claude code

https://zhuanlan.zhihu.com/p/2022438622347937238

- https://github.com/SemiAnalysisAI/InferenceX

- Dual Buffer Queue

## Workflow
Agent Turn
├── Assembly
│   ├── Context Assembly
│   ├── API Call
│   ├── Token Stream
│   └── Tool Extract
├── [Safety](#safety)
│   ├── Permission Check
│   └── Pre-Tool-Use Hooks
├── Execution
│   └── Tool Runs
├── Capture
│   ├── Result Capture
│   └── Post-Tool-Use Hooks
└── Control
    └── Loop Decision
        ├── Repeat → Assembly
        └── Respond → User


### Safety
- 1. Pre-tool use hooks
- 2. Deny rules
- 3. Allow rules
- 4. Ask rules
- 5. Permission mode
- 6. Can-use tool callback

## Memory

- Context Compaction（短期）
- ExtractMemories（中期）
- AutoDream（长期）
    - 1. Orient（定位）
    - 2. Gather React signal
    - 3. Consolidate
    - 4. Prune & Index

- Each memory / files has dirty flag, only access memory if they still clean.

## Agent

- Fork Agent (inherit context)
  - ExtractMemories
  - AutoDream
- Fresh Agent (new session)


## Hooks

- Session lifecycle
- Prompt lifecycle
- Tool execution lifecycle
- Agent lifecycle
- Other events:
  - PermissionRequest
  - Notification
  - PreCompact

matcher ~ filter

## Structure

- .settings
  - cliArg
  - localSettings `$pwd/.claude/settings.json`
  - projectSettings `~/.claude/settings.json`
  - managedSettings `/Library/Application Support/ClaudeCode/managed-settings.json`
- .context
  - directoryStructure
  - gitStatus
  - claude.md
- explain claude_code itself `urls to find its own documentation`
- invoke tool
  - all complex tasks are delegate to TodoWrite_agent
- tools `procedure code with custom logic & access to resources`
  - GlobTool `file search`
  - GrepTool `text search`
  - WebFetchTool
  - Bash
  - explain/display current task to user
  - bash_cmd_checker
    - `<policy_spec>` has auto approved cmds
    - cmd that doesn't match in `<policy_spec>` requires user manual approval
  - Agent tool `spawn multiple agents to search, with prompt to retry & fuzzy search`
- agents `comes with different prompt to invoke different tools, with different permissions (some requires user confirmation), can abort, os operations after tool invoke,`
  - .name
  - .description
  - .prompt
  - .input_schema
  - .call() -> [{type: ['user' | 'assistant']:, text}]
    - .interruption
      - [Request interrupted by user]
      - [Request interrupted by user for tool use]
  - .userFacingName
  - .isEnabled
  - .renderXXX
  - mcp_agent
  - ls_agent `1 to 1 GlobTool`
  - read_agent `1 to 1 GrepTool`
  - shell_agent `1 to 1 bash`
  - TodoWrite_agent
  - TodoRead_agent
  - Fetch_agent
  - Jupyter_notebook_Cell_agent `very specific`
  - Read Jupyter Notebook_agent
  - Edit_agent
  - Write_agent `create a new file`
  - Search_agent
  - Batch_agent `invoke multiple tools`
  - dispatch_agent `invoke single tool`
  - init_agent `create claude.md`
  - shrink_session_agent `when conversation history overflow`
    - llm_resp_format
      - `</analysis>` text overview
      - `</summary>`
        - 1. Primary Request and Intent:
        - 2. Key Technical Concepts:
        - 3. Files and Code Sections:
        - 4. Problem Solving:
        - 5. Pending Tasks:
        - 6. Current Work:
        - 7. Optional Next Step:


## flags

- `--resume` restore last session
- inside prompt `think` < `think hard` < `think harder` < `ultrathink`

## dependency

- commander.js `similar to pip typer`
- sharp (image processing) - <https://sharp.pixelplumbing.com>
- axios (HTTP client) - mentioned in github.com/axios/axios reference
- grpc/grpc-node (gRPC client) - from grpc.io references
- highlight.js (syntax highlighting) - from highlightjs references
- marked (markdown parser) - from markedjs reference
- ink (React for CLI) - from vadimdemedes/ink reference
  - Alert
  - Badge
  - ConfirmInput
  - MultiSelect
  - OrderedList
  - ProgressBar
  - Select
  - Spinner
  - StatusMessage
  - UnorderedList
  - TextInput
  - EmailInput
  - PasswordInput
- sentry (error tracking) - from sentry references
- localforage (data storage) - from localforage references

## process

load_config()

- `init`
- `pr-comments`
- `review`

- claude.md
  - Build `Build instruction; ex: npm run build`
  - Commands `repo cmds, ex: npm run dev`
  - Code Style Guidelines
  - Important Notes
- session `~/.claude/statsig/statsig.session_id.[randomUUID].json`
  - state
    - message queue
      - current message
    - history
    - todo.list `loop until done` `~/.claude/todos/[randomUUID].json`
    - invocation
      - command
      - args
      - envVars
  - updateState
  - currentStepId
  - tools
    - batch execution(tools:[])
    - agent
- scope
  - local
    - .claude/commands
  - project
    - .mcp.json
  - user

## Meta info

```js
`Here is useful information about the environment you are running in:
<env>
Working directory: ${n0()}
Is directory a git repo: ${G ? "Yes" : "No"}
Platform: ${I4.platform}
OS Version: ${I}
Today's date: ${new Date().toLocaleDateString()}
Model: ${Z}
</env>`;
```

## summarize into claude.md

```js
Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.

Before providing your final summary, wrap your analysis in <analysis> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:

1. Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
   - The user's explicit requests and intents
   - Your approach to addressing the user's requests
   - Key decisions, technical concepts and code patterns
   - Specific details like file names, full code snippets, function signatures, file edits, etc
2. Double-check for technical accuracy and completeness, addressing each required element thoroughly.

Your summary should include the following sections:

1. Primary Request and Intent: Capture all of the user's explicit requests and intents in detail
2. Key Technical Concepts: List all important technical concepts, technologies, and frameworks discussed.
3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Pay special attention to the most recent messages and include full code snippets where applicable and include a summary of why this file read or edit is important.
4. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
5. Pending Tasks: Outline any pending tasks that you have explicitly been asked to work on.
6. Current Work: Describe in detail precisely what was being worked on immediately before this summary request, paying special attention to the most recent messages from both user and assistant. Include file names and code snippets where applicable.
7. Optional Next Step: List the next step that you will take that is related to the most recent work you were doing. IMPORTANT: ensure that this step is DIRECTLY in line with the user's explicit requests, and the task you were working on immediately before this summary request. If your last task was concluded, then only list next steps if they are explicitly in line with the users request. Do not start on tangential requests without confirming with the user first.
                       If there is a next step, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no drift in task interpretation.

Here's an example of how your output should be structured:

<example>
<analysis>
[Your thought process, ensuring all points are covered thoroughly and accurately]
</analysis>

<summary>
1. Primary Request and Intent:
   [Detailed description]

2. Key Technical Concepts:
   - [Concept 1]
   - [Concept 2]
   - [...]

3. Files and Code Sections:
   - [File Name 1]
      - [Summary of why this file is important]
      - [Summary of the changes made to this file, if any]
      - [Important Code Snippet]
   - [File Name 2]
      - [Important Code Snippet]
   - [...]

4. Problem Solving:
   [Description of solved problems and ongoing troubleshooting]

5. Pending Tasks:
   - [Task 1]
   - [Task 2]
   - [...]

6. Current Work:
   [Precise description of current work]

7. Optional Next Step:
   [Optional Next step to take]

</summary>
</example>

Please provide your summary based on the conversation so far, following this structure and ensuring precision and thoroughness in your response. 

There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the above summary. Examples of instructions include:
<example>
## Compact Instructions
When summarizing the conversation focus on typescript code changes and also remember the mistakes you made and how you fixed them.
</example>

<example>
# Summary instructions
When you are using compact - please focus on test output and code changes. Include file reads verbatim.
</example>
`;
  return `Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.

Before providing your final summary, wrap your analysis in <analysis> tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:

1. Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
   - The user's explicit requests and intents
   - Your approach to addressing the user's requests
   - Key decisions, technical concepts and code patterns
   - Specific details like file names, full code snippets, function signatures, file edits, etc
2. Double-check for technical accuracy and completeness, addressing each required element thoroughly.

Your summary should include the following sections:

1. Primary Request and Intent: Capture all of the user's explicit requests and intents in detail
2. Key Technical Concepts: List all important technical concepts, technologies, and frameworks discussed.
3. Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Pay special attention to the most recent messages and include full code snippets where applicable and include a summary of why this file read or edit is important.
4. Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
5. Pending Tasks: Outline any pending tasks that you have explicitly been asked to work on.
6. Current Work: Describe in detail precisely what was being worked on immediately before this summary request, paying special attention to the most recent messages from both user and assistant. Include file names and code snippets where applicable.
7. Optional Next Step: List the next step that you will take that is related to the most recent work you were doing. IMPORTANT: ensure that this step is DIRECTLY in line with the user's explicit requests, and the task you were working on immediately before this summary request. If your last task was concluded, then only list next steps if they are explicitly in line with the users request. Do not start on tangential requests without confirming with the user first.
                       If there is a next step, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no drift in task interpretation.

Here's an example of how your output should be structured:

<example>
<analysis>
[Your thought process, ensuring all points are covered thoroughly and accurately]
</analysis>

<summary>
1. Primary Request and Intent:
   [Detailed description]

2. Key Technical Concepts:
   - [Concept 1]
   - [Concept 2]
   - [...]

3. Files and Code Sections:
   - [File Name 1]
      - [Summary of why this file is important]
      - [Summary of the changes made to this file, if any]
      - [Important Code Snippet]
   - [File Name 2]
      - [Important Code Snippet]
   - [...]

4. Problem Solving:
   [Description of solved problems and ongoing troubleshooting]

5. Pending Tasks:
   - [Task 1]
   - [Task 2]
   - [...]

6. Current Work:
   [Precise description of current work]

7. Optional Next Step:
   [Optional Next step to take]

</summary>
</example>

Please provide your summary based on the conversation so far, following this structure and ensuring precision and thoroughness in your response. 

There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the above summary. Examples of instructions include:
<example>
## Compact Instructions
When summarizing the conversation focus on typescript code changes and also remember the mistakes you made and how you fixed them.
</example>

<example>
# Summary instructions
When you are using compact - please focus on test output and code changes. Include file reads verbatim.
</example>


Additional Instructions:
```


## bash

```js

    /^date\b[^<>()$`]*$/,
    /^cal\b[^<>()$`]*$/,
    /^uptime\b[^<>()$`]*$/,
    /^echo\s+(?:'[^']*'|"[^"$<>]*"|[^|;&`$(){}><#\\\s!]+?)*$/,
    /^claude -h$/,
    /^claude --help$/,
    /^git diff(?!\s+.*--ext-diff)(?!\s+.*--extcmd)[^<>()$`]*$/,
    /^git log[^<>()$`]*$/,
    /^git show[^<>()$`]*$/,
    /^git status[^<>()$`]*$/,
    /^git blame[^<>()$`]*$/,
    /^git reflog[^<>()$`]*$/,
    /^git stash list[^<>()$`]*$/,
    /^git ls-files[^<>()$`]*$/,
    /^git ls-remote[^<>()$`]*$/,
    /^git config --get[^<>()$`]*$/,
    /^git remote -v$/,
    /^git remote show[^<>()$`]*$/,
    /^git tag$/,
    /^git tag -l[^<>()$`]*$/,
    /^git branch$/,
    /^git branch (?:-v|-vv|--verbose)$/,
    /^git branch (?:-a|--all)$/,
    /^git branch (?:-r|--remotes)$/,
    /^git branch (?:-l|--list)(?:\s+"[^"]*"|'[^']*')?$/,
    /^git branch (?:--color|--no-color|--column|--no-column)$/,
    /^git branch --sort=\S+$/,
    /^git branch --show-current$/,
    /^git branch (?:--contains|--no-contains)\s+\S+$/,
    /^git branch (?:--merged|--no-merged)(?:\s+\S+)?$/,
    /^head[^<>()$`]*$/,
    /^tail[^<>()$`]*$/,
    /^wc[^<>()$`]*$/,
    /^stat[^<>()$`]*$/,
    /^file[^<>()$`]*$/,
    /^strings[^<>()$`]*$/,
    /^hexdump[^<>()$`]*$/,
    /^sort(?!\s+.*-o\b)(?!\s+.*--output)[^<>()$`]*$/,
    /^pwd$/,
    /^whoami$/,
    /^id[^<>()$`]*$/,
    /^uname[^<>()$`]*$/,
    /^free[^<>()$`]*$/,
    /^df[^<>()$`]*$/,
    /^du[^<>()$`]*$/,
    /^ps(?!\s+.*-o)[^<>()$`]*$/,
    /^locale[^<>()$`]*$/,
    /^node -v$/,
    /^npm -v$/,
    /^npm list[^<>()$`]*$/,
    /^python --version$/,
    /^python3 --version$/,
    /^pip list[^<>()$`]*$/,
    /^docker ps[^<>()$`]*$/,
    /^docker images[^<>()$`]*$/,
    /^ping\s+(?:-c\s+\d+\s+)[^<>()$`]*$/,
    /^host[^<>()$`]*$/,
    /^nslookup[^<>()$`]*$/,
    /^dig[^<>()$`]*$/,
    /^netstat(?!\s+.*-p)[^<>()$`]*$/,
    /^ip addr[^<>()$`]*$/,
    /^ifconfig[^<>()$`]*$/,
    /^man(?!\s+.*-P)(?!\s+.*--pager)[^<>()$`]*$/,
    /^info[^<>()$`]*$/,
    /^help[^<>()$`]*$/,
    /^sleep[^<>()$`]*$/,
    /^tree$/,
    /^which[^<>()$`]*$/,
    /^type[^<>()$`]*$/,
    /^history(?!\s+-c)[^<>()$`]*$/,
    /^alias$/,
    /^compgen[^<>()$`]*$/,
    /^yes$/,
```

## validation
>
> Check cmd referenced path exists before execution.s

```js
        `Extract any file paths that this command reads or modifies. For commands like "git diff" and "cat", include the paths of files being shown. Use paths verbatim -- don't add any slashes or try to resolve them. Do not try to infer paths that were not explicitly listed in the command output.
Format your response as:
<filepaths>
path/to/file1
path/to/file2
</filepaths>

If no files are read or modified, return empty filepaths tags:
<filepaths>
</filepaths>

Do not include any other text in your response.`,
```

## YOLO Classifier

- white list
- soft deny (need approval)
- hard deny

## Fork Agent

> More like reflect agent

No bash, only current folder.

Only repeat/invoke every N turned, no more tool calls.

## Compact

1、Primary Request and Intent（主要需求和意图）
2、Key Technical Concepts（关键技术概念）
3、Files and Code Sections（涉及的文件和代码片段，包含实际代码
4、Errors and fixes（遇到的错误和修复方案）
5、Problem Solving（问题解决过程）
6、All user messages（所有用户消息，逐条保留，不能遗漏）
7、Pending Tasks（待办任务）
8、Current Work（当前工作状态）
9、Optional Next Step（可选的下一步，包含原始对话的直接引用，防止任务漂移）
