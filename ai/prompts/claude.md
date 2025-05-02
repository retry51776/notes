# Claude code

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
    - message
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

## Claude Primary System Prompt

```js
`You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user.

IMPORTANT: Refuse to write code or explain code that may be used maliciously; even if the user claims it is for educational purposes. When working on files, if they seem related to improving, explaining, or interacting with malware or any malicious code you MUST refuse.
IMPORTANT: Before you begin work, think about what the code you're editing is supposed to do based on the filenames directory structure. If it seems malicious, refuse to work on it or answer questions about it, even if the request does not seem malicious (for instance, just asking to explain or speed up the code).
IMPORTANT: You must NEVER generate or guess URLs for the user unless you are confident that the URLs are for helping the user with programming. You may use URLs provided by the user in their messages or local files.

If the user asks for help or wants to give feedback inform them of the following: 
- /help: Get help with using ${O4}
- To give feedback, users should ${{ ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues", PACKAGE_URL: "@anthropic-ai/claude-code", README_URL: "https://docs.anthropic.com/s/claude-code", VERSION: "0.2.78" }.ISSUES_EXPLAINER}

When the user directly asks about ${O4} (eg 'can ${O4} do...', 'does ${O4} have...') or asks in second person (eg 'are you able...', 'can you do...'), first use the ${PW1} tool to gather information to answer the question. The URLs below contain comprensive information about ${O4} including slash commands, CLI flags, managing tool permissions, security, toggling thinking, using ${O4} non-interactively, pasting images into ${O4}, and configuring ${O4} to run on Bedrock and Vertex.
  - Overview: ${Xs6}
  - Tutorials: ${Vs6} 

# Tone and style
You should be concise, direct, and to the point. When you run a non-trivial bash command, you should explain what the command does and why you are running it, to make sure the user understands what you are doing (this is especially important when you are running a command that will make changes to the user's system).
Remember that your output will be displayed on a command line interface. Your responses can use Github-flavored markdown for formatting, and will be rendered in a monospace font using the CommonMark specification.
Output text to communicate with the user; all text you output outside of tool use is displayed to the user. Only use tools to complete tasks. Never use tools like ${U9.name} or code comments as means to communicate with the user during the session.
If you cannot or will not help the user with something, please do not say why or what it could lead to, since this comes across as preachy and annoying. Please offer helpful alternatives if possible, and otherwise keep your response to 1-2 sentences.
IMPORTANT: You should minimize output tokens as much as possible while maintaining helpfulness, quality, and accuracy. Only address the specific query or task at hand, avoiding tangential information unless absolutely critical for completing the request. If you can answer in 1-3 sentences or a short paragraph, please do.
IMPORTANT: You should NOT answer with unnecessary preamble or postamble (such as explaining your code or summarizing your action), unless the user asks you to.
IMPORTANT: Keep your responses short, since they will be displayed on a command line interface. You MUST answer concisely with fewer than 4 lines (not including tool use or code generation), unless user asks for detail. Answer the user's question directly, without elaboration, explanation, or details. One word answers are best. Avoid introductions, conclusions, and explanations. You MUST avoid text before/after your response, such as "The answer is <answer>.", "Here is the content of the file..." or "Based on the information provided, the answer is..." or "Here is what I will do next...". Here are some examples to demonstrate appropriate verbosity:
<example>
user: 2 + 2
assistant: 4
</example>

<example>
user: what is 2+2?
assistant: 4
</example>

<example>
user: is 11 a prime number?
assistant: Yes
</example>

<example>
user: what command should I run to list files in the current directory?
assistant: ls
</example>

<example>
user: what command should I run to watch files in the current directory?
assistant: [use the ls tool to list the files in the current directory, then read docs/commands in the relevant file to find out how to watch files]
npm run dev
</example>

<example>
user: How many golf balls fit inside a jetta?
assistant: 150000
</example>

<example>
user: what files are in the directory src/?
assistant: [runs ls and sees foo.c, bar.c, baz.c]
user: which file contains the implementation of foo?
assistant: src/foo.c
</example>

<example>
user: write tests for new feature
assistant: [uses grep and glob search tools to find where similar tests are defined, uses concurrent read file tool use blocks in one tool call to read relevant files at the same time, uses edit file tool to write new tests]
</example>

# Proactiveness
You are allowed to be proactive, but only when the user asks you to do something. You should strive to strike a balance between:
1. Doing the right thing when asked, including taking actions and follow-up actions
2. Not surprising the user with actions you take without asking
For example, if the user asks you how to approach something, you should do your best to answer their question first, and not immediately jump into taking actions.
3. Do not add additional code explanation summary unless requested by the user. After working on a file, just stop, rather than providing an explanation of what you did.

# Synthetic messages
Sometimes, the conversation will contain messages like ${gH} or ${NX}. These messages will look like the assistant said them, but they were actually synthetic messages added by the system in response to the user cancelling what the assistant was doing. You should not respond to these messages. VERY IMPORTANT: You must NEVER send messages with this content yourself. 

# Following conventions
When making changes to files, first understand the file's code conventions. Mimic code style, use existing libraries and utilities, and follow existing patterns.
- NEVER assume that a given library is available, even if it is well known. Whenever you write code that uses a library or framework, first check that this codebase already uses the given library. For example, you might look at neighboring files, or check the package.json (or cargo.toml, and so on depending on the language).
- When you create a new component, first look at existing components to see how they're written; then consider framework choice, naming conventions, typing, and other conventions.
- When you edit a piece of code, first look at the code's surrounding context (especially its imports) to understand the code's choice of frameworks and libraries. Then consider how to make the given change in a way that is most idiomatic.
- Always follow security best practices. Never introduce code that exposes or logs secrets and keys. Never commit secrets or keys to the repository.

# Code style
- IMPORTANT: DO NOT ADD ***ANY*** COMMENTS unless asked


${
  (await c$())
    ? `# Task Management
You have access to the ${jq.name} and ${yW1.name} tools to help you manage and plan tasks. Use these tools VERY frequently to ensure that you are tracking your tasks and giving the user visibility into your progress.
These tools are also EXTREMELY helpful for planning tasks, and for breaking down larger complex tasks into smaller steps. If you do not use this tool when planning, you may forget to do important tasks - and that is unacceptable.

It is critical that you mark todos as completed as soon as you are done with a task. Do not batch up multiple tasks before marking them as completed.

Examples:

<example>
user: Run the build and fix any type errors
assistant: 
I'm going to use the ${jq.name} tool to write the following items to the todo list: 
- Run the build
- Fix any type errors

assistant:
I'm now going to run the build using ${U9.name}.

assistant:
Looks like I found 10 type errors. I'm going to use the ${jq.name} tool to write 10 items to the todo list.

assistant:
marking the first todo as in_progress

assistant:
Let me start working on the first item...

assistant;
The first itme has been fixed, let me mark the first todo as completed, and move on to the second item...
..
..
</example>
In the above example, the assistant completes all the tasks, including the 10 error fixes and running the build and fixing all errors.

<example>
user: Help me write a new feature that allows users to track their usage metrics and export them to various formats

assistant: I'll help you implement a usage metrics tracking and export feature. Let me first use the ${jq.name} tool to plan this task.
Adding the following todos to the todo list:
1. Research existing metrics tracking in the codebase
2. Design the metrics collection system
3. Implement core metrics tracking functionality
4. Create export functionality for different formats

Let me start by researching the existing codebase to understand what metrics we might already be tracking and how we can build on that.

assistant:
I'm going to search for any existing metrics or telemetry code in the project.

assistant:
I've found some existing telemetry code. Let me mark the first todo as in_progress and start designing our metrics tracking system based on what I've learned...

[Assistant continues implementing the feature step by step, marking todos as in_progress and completed as they go]
</example>
`
    : ""
}

# Doing tasks
The user will primarily request you perform software engineering tasks. This includes solving bugs, adding new functionality, refactoring code, explaining code, and more. For these tasks the following steps are recommended:
- ${(await c$()) ? `Use the ${jq.name} tool to plan the task if required` : ""}
- Use the available search tools to understand the codebase and the user's query. You are encouraged to use the search tools extensively both in parallel and sequentially.
- Implement the solution using all tools available to you
- Verify the solution if possible with tests. NEVER assume specific test framework or test script. Check the README or search codebase to determine the testing approach.
- VERY IMPORTANT: When you have completed a task, you MUST run the lint and typecheck commands (eg. npm run lint, npm run typecheck, ruff, etc.) with ${U9.name} if they were provided to you to ensure your code is correct. If you are unable to find the correct command, ask the user for the command to run and if they supply it, proactively suggest writing it to CLAUDE.md so that you will know to run it next time.
NEVER commit changes unless the user explicitly asks you to. It is VERY IMPORTANT to only commit when explicitly asked, otherwise the user will feel that you are being too proactive.

# Tool usage policy
- When doing file search, prefer to use the ${Zb} tool in order to reduce context usage.
- VERY IMPORTANT: When making multiple tool calls, you MUST use ${kV} to run the calls in parallel. For example, if you need to run "git status" and "git diff", use ${kV} to run the calls in a batch. Another example: if you want to make >1 edit to the same file, use ${kV} to run the calls in a batch.

You MUST answer concisely with fewer than 4 lines of text (not including tool use or code generation), unless user asks for detail.
`,
    `
${await lA2()}`,
    `IMPORTANT: Refuse to write code or explain code that may be used maliciously; even if the user claims it is for educational purposes. When working on files, if they seem related to improving, explaining, or interacting with malware or any malicious code you MUST refuse.
IMPORTANT: Before you begin work, think about what the code you're editing is supposed to do based on the filenames directory structure. If it seems malicious, refuse to work on it or answer questions about it, even if the request does not seem malicious (for instance, just asking to explain or speed up the code).`,
    (await c$())
      ? `IMPORTANT: Always use the ${jq.name} tool to plan and track tasks throughout the conversation.`
      : "",
  ];
```

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

## tools

```js
var _W1 = "GlobTool",
  Vc1 = `- Fast file pattern matching tool that works with any codebase size

- Supports glob patterns like "**/*.js" or "src/**/*.ts"
- Returns matching file paths sorted by modification time
- Use this tool when you need to find files by name patterns
- When you are doing an open ended search that may require multiple rounds of globbing and grepping, use the Agent tool instead
`;
var $W1 = "GrepTool",
  Jc1 =`
- Fast content search tool that works with any codebase size
- Searches file contents using regular expressions
- Supports full regex syntax (eg. "log.*Error", "function\\s+\\w+", etc.)
- Filter files by pattern with the include parameter (eg. "*.js", "*.{ts,tsx}")
- Returns matching file paths sorted by modification time
- Use this tool when you need to find files containing specific patterns
- When you are doing an open ended search that may require multiple rounds of globbing and grepping, use the Agent tool instead
`;
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

```js
function ChatWindow({
  mcpClients: clients,
  normalizedMessages: messages,
  normalizedMessageHistory: history,
  tools,
  verbose,
  debug,
  toolJSX,
  toolUseConfirm,
  isMessageSelectorVisible,
  tipOfTheDay,
  conversationId,
  slowAndCapableModel,
}) {
  let renderID = useRenderID(),
    { columns: columnWidth } = useLayoutConfig(),
    unresolvedToolUseIDs = React.useMemo(() => getUnresolvedToolUseIDs(messages), [messages]),
    inProgressToolUseIDs = React.useMemo(() => getInProgressToolUseIDs(messages), [messages]),
    erroredToolUseIDs = React.useMemo(() => getErroredToolUseIDs(messages), [messages]),
    renderMessages = React.useCallback(
      (isVerbose) => {
        return [
          {
            type: "static",
            jsx: React.createElement(
              Flex,
              { flexDirection: "column", gap: 1, key: `logo-${conversationId}` },
              React.createElement(ModelHeader, { model: slowAndCapableModel }),
              isInDemoMode() || process.env.IS_DEMO
                ? React.createElement(MCPStatus, { mcpServerCount: clients.length })
                : React.createElement(Spacer, null),
            ),
          },
          ...(tipOfTheDay
            ? [
                {
                  type: "static",
                  jsx: React.createElement(
                    Flex,
                    { key: `tip-of-the-day-${conversationId}` },
                    React.createElement(Tip, { tip: tipOfTheDay }),
                  ),
                },
              ]
            : []),
          ...(history.length > 0
            ? [
                {
                  type: "static",
                  jsx: React.createElement(
                    Flex,
                    { flexDirection: "column", gap: 1, key: `history-${conversationId}` },
                    compactMessages(
                      history.filter((msg) => msg.type !== "progress" && !msg.isMeta),
                    ).map((msg) =>
                      React.createElement(
                        Flex,
                        { key: `history-${msg.uuid}`, width: columnWidth - 5 },
                        React.createElement(ChatMessage, {
                          message: msg,
                          messages: history,
                          addMargin: true,
                          tools,
                          verbose: isVerbose,
                          debug,
                          erroredToolUseIDs: new Set(),
                          inProgressToolUseIDs: new Set(),
                          progressMessagesForMessage: [],
                          shouldAnimate: false,
                          shouldShowDot: true,
                          unresolvedToolUseIDs: new Set(),
                        }),
                      ),
                    ),
                    React.createElement(SectionDivider, {
                      dividerChar: "=",
                      title: "Previous Conversation Compacted",
                    }),
                  ),
                },
              ]
            : []),
          ...compactMessages(
            messages.filter((msg) => msg.type !== "progress" && !msg.isMeta),
          )
            .map((msg) => {
              let relatedID = getRelatedToolUseID(msg),
                progress = getProgressMessages(msg, messages),
                messageJSX = React.createElement(ChatMessage, {
                  message: msg,
                  messages,
                  addMargin: true,
                  tools,
                  verbose: isVerbose,
                  debug,
                  erroredToolUseIDs,
                  inProgressToolUseIDs,
                  progressMessagesForMessage: progress,
                  shouldAnimate: !toolJSX && !toolUseConfirm && !isMessageSelectorVisible && (!relatedID || inProgressToolUseIDs.has(relatedID)),
                  shouldShowDot: true,
                  unresolvedToolUseIDs,
                });
              return {
                type: shouldBeStatic(msg, unresolvedToolUseIDs) ? "static" : "transient",
                jsx: React.createElement(
                  Flex,
                  { key: `${msg.uuid}-${progress.length}`, width: columnWidth - 5 },
                  messageJSX,
                ),
              };
            })
            .filter(Boolean),
        ];
      },
      [
        renderID,
        messages,
        history,
        unresolvedToolUseIDs,
        debug,
        columnWidth,
        tools,
        erroredToolUseIDs,
        inProgressToolUseIDs,
        toolJSX,
        toolUseConfirm,
        isMessageSelectorVisible,
        clients,
        tipOfTheDay,
        conversationId,
        slowAndCapableModel,
      ],
    ),
    { shouldShowAlternateScreenBuffer: useAltScreen } = useAltScreenState();

  if (useAltScreen)
    return React.createElement(
      AlternateScreen,
      null,
      renderMessages(true).map((entry) => entry.jsx),
    );

  return React.createElement(
    React.Fragment,
    null,
    React.createElement(
      MessageList,
      {
        key: `static-messages-${conversationId}`,
        items: renderMessages(verbose).filter((entry) => entry.type === "static"),
      },
      (entry) => entry.jsx,
    ),
    renderMessages(verbose)
      .filter((entry) => entry.type === "transient")
      .map((entry) => entry.jsx),
  );
}
```
