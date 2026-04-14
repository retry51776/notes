# Codex

## Codex Cloud

Define codex sandbox: <https://chatgpt.com/codex/settings/environments>

Codex start contain(with their image) with mounted volume(from github repo); This github repo acts as s3 storage, codex container may open PR to this github repo for save changes.
  OpenAI codex provide runtime but not storage.

## Hooks

> internal hook system only.

## Security

- POV of control from user
  - Developer/User
    - OS boundary (Authentication, File, keychain)
      - Orchestrator/multi-agent Ex: claude cowork, gastown, overstory
        - Codex, Claude Agent (user shell, workspace boundary, clipboard access, whitelist/block path/commands/domains)
          - LLM engine
          - future impersonate user setting?
          - Session
            - log `~/.codex/sessions/xxx.jsonl`
              - traces `sqlite3 -header -column ~/.codex/logs_1.sqlite "select datetime(ts,'unixepoch','localtime') as time, level, target, substr(feedback_log_body,1,120) as msg from logs order by id desc limit │ 50;"`
              - tool-call records: `apply_patch` ~ diff_log
              - approval log
              - file access log
          - Skill (no access control)
          - Plugins
            - External api
          - MCP (access host's secret)
            - Authentication tokens stored @ `~/.codex/auth.json`
          - Execution Sandbox (leaky)
      - Admin Folder (read access, normal user can't edit)
        - Goal/Safety Instruction
  - Admin
    - 3rd Party Software
      - Grant Authentication
      - Control Authorization
      - Rate limits
    - LLM provider
      - Access
      - Global system message
      - budget control
- Emergency
  - emergency revoke

## Bash

```bash
codex login --device-auth

# Can read/edit file(need approval), but no external network access
codex --sandbox workspace-write --ask-for-approval untrusted

# Can read/edit file without approval
codex --sandbox workspace-write --ask-for-approval never

# Both network & read/edit
codex --yolo
```

## Config

```yaml
# ~/.codex/config.toml

full-auto = true
bypass-approvals = true
bypass-sandbox = true
trusted-workspace = true

sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = true
```
