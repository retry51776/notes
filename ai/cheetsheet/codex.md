# Codex

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
