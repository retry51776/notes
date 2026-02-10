# Openclaw

- Gateway `Control plane, usually only expose as localhost`
  - Dashboard <http://127.0.0.1:18789/> `client side`
  - Client CLI
  - Openclaw Agent
  - Channel integration
  - Schedule triggers
- Node Service <http://127.0.0.1:51332/> `Execution engine runs skills`

- Settings ~/.openclaw
  - /workspace `agent, skills, cred bundles`
    - BOOTSTRAP.md `run once @ agent initialization`
    - BOOTSTRAP.md.done
    - AGENTS.md `main template`
    - IDENTITY.md
    - HEARTBEAT.md `short checklist or reminders, flexible time & need context`
    - /memory
      - /YYYY-MM-DD.md `always loaded latest by AGENTS.md`
    - /skills
      - xxx
        - SKILL.md
          - install
        - scripts/reddit.mjs
    - SOUL.md `always loaded by AGENTS.md`
      - behavior of agent
    - TOOLS.md
    - USER.md `always loaded by AGENTS.md`
      - name
      - timezone
      - behavior
      - Notes `session will invoke edit tool to store User's Notes here`

  - /agents/main/agent
    - /agent `store active LLM token`
    - /sessions `store active session`
      - sessions.json
      - agent:main:main
      - modelProvider/model
      - tools: []
      - skillsSnapshot
        - prompt: str
        - resolvedSkills: []
      - injectedWorkspaceFiles: []
  - /canvas
  - /browser
  - /media/browser `store browser screen shots`
  - /credentials `store channel cred`
  - /cron/jobs.json `Exact timing jobs & isolate session`
  - /devices/paired.json `Dashboard UI, CLI, agents controller authorized Node Service`
  - /memory/main.sqlite `sqlite stores dynamic templates/memories`
    - meta
      - key `agent:<name>:last_run or task:<id>:status`
      - value
    - files
    - chunks
    - embedding_cache

## Channel workflow

policy is agent-scoped, and channels choose which agent wakes up.

```
Discord message
  ↓
Gateway receives event
  ↓
Filter / policy checks(has approval pair code)  → decide IF an agent wakes up
  ↓
Agent invoked?  ──► yes → AGENT.md/Prompt policy  → decide WHAT the agent does after waking up
                 └─► no  → ignored
    
```

## Skill

Skill
 ├─ Manifest
 ├─ Tools (schemas)
 ├─ Tool implementations
 ├─ Environment adapters
 ├─ Dependencies
 ├─ Permissions
 ├─ State / artifacts
 └─ Validation

Parsed
 • Skill name
 • High-level capability description
 • Tool signatures (inputs / outputs)
 • Preconditions & constraints
 • Cost / latency hints (if available)

```bash
# CLI approve 
openclaw pairing approve --channel discord <code>

# Dashboard need token, token ttl ~1hr
openclaw dashboard --no-open

OPENCLAW_WORKSPACE=/Users/terry/.openclaw/workspace

# openclaw settings
ls ~/.openclaw

# auto start openclaw
openclaw node install

openclaw gateway restart

# 1. Download SKILL.md
npx clawhub install gog

# 2. Install deps, because clawhub won't auto install deps
brew tap steipete/tap
brew install gogcli

# 3. Setup OAuth Client Secret
https://console.cloud.google.com/apis/credentials -> /Users/terry/Library/Application Support/gogcli/credentials.json

https://console.cloud.google.com/auth/audience publishing status -> Testing & Add Test User
Or Finish verification https://console.cloud.google.com/auth/branding

# 4. Enable Google APIs
https://console.cloud.google.com/apis/api/gmail.googleapis.com

# 5. Grant gog access to Google Account
gog auth credentials credentials.json
gog auth login

# 6. Manually test gogcli
gog email search "is:unread"

openclaw skills enable gog
```

### gog

```bash
gog --client <name> auth credentials
```
