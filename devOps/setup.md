# Setup

> OS setup/maintain should done by agent. Agent maintain have audible log trace, that also readable with highlight details.

## Rule of thumb

- Package manager preference: brew > apt > uv > pip3 > npm > .pkg installer
- `~/.profile` should stores all setup scripts or envs, then `~/.bashrc` or `~./zshrc` should invoke `source ~/.profile`

## SSH cloud

### Github

1) make sure `ssh-add -l` already added ssh public key
2) `pbcopy < ~/.ssh/id_rsa.pub` copy to clipboard
3) Login github & add id_rsa.pub to <https://github.com/settings/keys>
4) ssh -T <git@github.co>
  4.1) `ssh-keygen -R github.com` to renew github.com host key when `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`

### Jira
<https://id.atlassian.com/manage-profile/security/passkeys>

## Setup Linux

```bash
sudo apt update
sudo apt install -y curl ca-certificates git gnupg lsb-release nodejs python3 python3-pip wget unzip
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable --now docker
```

## Setup Mac

You are running in mac os terminal. Your goal is setup os.

Workflow:
OS setup through multiple Phases.
Inside each Phase can have multiple tasks, only run parallel tasks in different terminals when user ask.
Prefer to install everything in homebrew if possible, because easier to update in future.

Constraints:

- Don't destructive deletes, uninstall

### Phase 1: Install brew packages

- `brew update`
- `brew install ca-certificates docker docker-compose eslint git helm k9s kubectl nvm node openssh prettier poetry python sublime-text uv visual-studio-code wget`
- `brew install --cask codex-app gcloud-cli google-chrome github miniconda postman docker-desktop zoom`
- Check brew install packages's symlink; If missing, then manually link the CLI (brew is known for NOT auto-link it reliably)
  - especially on [`kubectl`, `python`, `pip3`, `node`, `npm`, `npx`]
- `brew cleanup`

### Phase 3: Setup different managers

> Run task within current phase in different terminals.

- Task 1: Setup Conda
  - Add `conda initialize script` to `~/.zshrc` or `~/.bashrc`
  - open another cmd terminal
  - `conda init` && `conda doctor`
    - If `conda doctor` reports `Missing Files: python.app`; Solution: The issue was a path mismatch: the package metadata lists pythonapp/... but the installed files are under python.app/.... I created a symlink pythonapp → python.app in the base environment;
  - `conda activate base`

- Task 2: Setup NVM
  - Add `nvm initialize script` to `~/.zshrc` or `~/.bashrc`

  ```bash
  # nvm initialize script
  export NVM_DIR="$HOME/.nvm" && (
    git clone https://github.com/nvm-sh/nvm.git "$NVM_DIR"
    cd "$NVM_DIR"
    git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" $(git rev-list --tags --max-count=1)`
  ) && \. "$NVM_DIR/nvm.sh"
  ```

  - `nvm install --lts`

- Task 3: Setup yabai tiling window manager
  - `brew install koekeishiya/formulae/yabai`
  - create `~/.yabairc` with standard config
  - `defaults write com.apple.dock mru-spaces -bool false` Disable: “Automatically rearrange Spaces based on most recent use
  - `defaults write -g AppleActionOnDoubleClick -string "Minimize"` Set double click window bar to Minimize window
  - `killall Dock` Apply (restarts Dock / Mission Control)
  - `which yabai` && `yabai` Start yabai, wait for user approve Mac OS Approval
  - create `~/Library/LaunchAgents/com.koekeishiya.yabai.plist` with proper context, then `launchctl load ~/Library/LaunchAgents/com.koekeishiya.yabai.plist`  will auto start `yabai` auto start when login
  - `yabai --start-service`

- Task 4: Install pip-audit
  - `python -m pip install pip-audit pip-tool`

- Task 5: Setup Codex
  - Append `~/.codex/config.toml` allow outbound network

```bash
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = true
```

### Phase 4: Setup ssh

1) Ask user.name & user.email & user.passphrase

2) Check if ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519.pub already exist.
   - If they exist, do NOT overwrite. Just use them.
   - If not, generate a new ed25519 SSH key with:
     ssh-keygen -t ed25519 -C "<YOUR_EMAIL@example.com>" -f ~/.ssh/id_ed25519 -N "user.passphrase"

3) Ensure correct permissions:
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/id_ed25519
   chmod 644 ~/.ssh/id_ed25519.pub

4) Start ssh-agent (if not running) and add the key:
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519

5) Print the public key and also copy it to clipboard:
   - If `clip.exe` exists (WSL), use: cat ~/.ssh/id_ed25519.pub | clip.exe
   - Else if `xclip` exists, use it
   - Else just print and tell me to copy

6) Open the GitHub page to add SSH keys:
   <https://github.com/settings/keys>
   Use `wslview` if available; otherwise print the URL.

7) Tell me exactly what to do on GitHub UI:
   Settings → SSH and GPG keys → New SSH key
   Title: "WSL Laptop (Feb 2026)"
   Paste the key
   Add SSH key

8) Finally test:
   ssh -T <git@github.com>
   If it fails, diagnose and propose fixes.

## Setup Windows
>
> FYI, chocolatey is very good alternative package manager, follow instruction @ <https://chocolatey.org/install>. Windows don't have single package manager covers common developer's packages.

You are running in window os powershell. Your goal is setup os.
Prefer to install everything in winget, then npm, then pip.

Constraints:

- Don't destructive deletes, uninstall.
- Before update, get current versions & status.
- Make update idempotent.
- Never assume install/update success. Always verify with explicit checks.
- After updated, log `maintain.md`. (from xxx to yyy)

### General

- `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` allow run `xxx.cmd` only with `xxx`

### winget package manager

- `winget upgrade --all --accept-source-agreements --accept-package-agreements`
- `winget install  --accept-source-agreements --accept-package-agreements Git.Git Python.Python.3.12 Docker.DockerDesktop CoreyButler.NVMforWindows OpenJS.NodeJS Derailed.k9s`

### npm package manager

`npm install -g @openai/codex eslint jest npx npm playwright pnpm prettier`

### pip package manager

`pip install poetry pip-audit pip-tool`

### Setup SSH

1) Ask user.name & user.email & user.passphrase

2) Check if ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519.pub already exist.
   - If they exist, do NOT overwrite. Just use them.
   - If not, generate a new ed25519 SSH key with:
     ssh-keygen -t ed25519 -C "<YOUR_EMAIL@example.com>" -f ~/.ssh/id_ed25519 -N "user.passphrase"

3) ssh-add ~/.ssh/id_ed25519

### Setup WSL

- Windows Host powershell
  - `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
  - `Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart`
  - `wsl --set-default-version Debian 2`
  - `wsl --update`
  - `wsl --install Debian`
  - Remember <WindowsUser> from `whoami`

WSL tips:

- Default WSL distro is fine. Default should be Debian.
- When PowerShell into WSL, prefer `wsl --%` to avoid quoting bugs.
- When PowerShell into WSL as root, use `wsl --% -u root`.
- Examples in this section are written as `Windows PowerShell -> WSL` commands so the execution context is explicit.

WSL tasks:

- Share HOST `~/.ssh` to WSL by symlink (run from Windows PowerShell; each command executes in WSL):

```bash
wsl --% -- bash -lc "mkdir -p ~/.ssh && ln -s /mnt/c/Users/<WindowsUser>/.ssh ~/.ssh"
wsl --% -- bash -lc "chmod 700 ~/.ssh && chmod 600 ~/.ssh/* "
wsl --% -- bash -lc "-add ~/.ssh/id_ed25519"

```

- Write `/etc/wsl.conf` (run from Windows PowerShell as root inside WSL):

```bash
wsl --% -u root -- bash -lc "printf '%s\n' '[interop]' 'appendWindowsPath = false' > /etc/wsl.conf"
```

## Mac/Linux OS Maintain

You are running in my terminal.
Goal: audit and safely update common developer tooling across npm (global), Homebrew, apt, and pip.
Follow CMD Rule when update each Step, log each Step's result to `~/maintain.md` follows Log Rules.

CMD Rules:

- Find current package manager version(auto update), what packages current installed, what packages needs update.
- Be conservative: update to latest PATCH/MINOR only, avoid MAJOR version upgrades. Log `~/maintain.md` MAJOR version upgrades as SINGLE CMD for user manual execute.
- Don’t break my environment. Don't use things like: `--force`, `--break-system-packages`, `pip install -U pkg`.
- `timeout` parameter should relax 5min.
- Use sudo only when required, `sudo` required user's confirmation.
- If a command is unavailable on this system, skip it and continue with the rest.

Log Rules:

1) Add maintain_log section with header`/n/n ## yyyy-mm-dd hh:mm` to `~/maintain.md`:
2) What you found installed (key packages + versions)
3) What you updated (from -> to)
4) Log SINGLE BASH CMD update all major-version to `~/maintain.md`; User can manual run update cmd.
5) Security vulnerabilities found (package, severity, advisory id/link if available, fix available Y/N)
6) Log update time `hh:mm:ss` for each section.

Step A — System info

- Print OS, distro, and versions of node/npm, brew, apt, pip, pip3, uv, poetry.

Step B — npm global packages (Node)

1) List globally installed packages:
   - npm install -g npm@latest
   - npm ls -g --depth=0
2) Check for outdated:
   - npm outdated -g --depth=ssh0
3) Safe-update globals without major bumps:
   - npm update -g xxx
   - If `npm update -g` throws error `EINVALIDPACKAGENAME Invalid package name ".[packpage_path]" of package`
      - go ahead run `sudo rm -rf $(npm root -g)/.[packpage_path]` to remove Invalid package, Add `~/maintain.md` what package removed.
      - try `npm update -g` again
4) Capture the global package list again `npm ls -g --depth=0`. Log what you updated (from -> to)
5) Log SINGLE BASH CMD update all major-version to `~/maintain.md`;

Step C — Homebrew (mac/linux)

1) `brew update` & `brew list --versions`
2) `brew outdated --verbose` (poetry included here)
3) Upgrade safely without major bumps:
   - `brew upgrade`
   - `brew doctor`. Follow `brew doctor` notes to update/fix packages.
   - `brew cleanup`
4) Capture the global package list again `brew list --versions`. Log what you updated (from -> to)
5) `softwareupdate --list` && `softwareupdate --install --all` && `softwareupdate --list`. Log what you updated (from -> to)
6) `launchctl list | grep -v "com.apple"` list all none apple service, report any suspicious service.

Step D — apt (Linux)

1) sudo apt update
2) Show upgradable packages:
   - apt list --upgradable
3) Apply safe upgrades without major bumps::
   - sudo apt upgrade -y
   - Avoid dist-upgrade/full-upgrade unless I approve.
4) Follow Log Rules to log.

Step E — pip3

- `python3 -m pip3 install --upgrade pip`
- `python3 -m pip3 list --outdated` (to find all packages needs update)
  - Update all pip3 packages to latest PATCH/MINOR only, avoid MAJOR version upgrades.
  - Capture the global package list again `pip3 list`. Log what you updated (from -> to)
  - Write SINGLE COMMAND to `~maintain.md` allow user manually update all pip3 packages to their MAJOR version.
- `pip3 cache purge`

Step F — pip

- `pip install --upgrade pip`
- `python3 -m pip list --outdated` (to find all packages needs update)
  - Update all pip packages to latest PATCH/MINOR only, avoid MAJOR version upgrades.
  - Capture the global package list again `pip list`. Log what you updated (from -> to)
  - Write SINGLE COMMAND to `~maintain.md` allow user manually update all pip packages to their MAJOR version upgrades.
- `pip cache purge`

Step G — other package manager

1) `uv self update` & `uv self version`
2) `conda doctor`

Step H — Common developer packages checklist

- git, curl, wget, openssh, gnupg, jq, ripgrep, fd, fzf, tmux, htop/btop, openssl, sqlite, postgres client
- python3, node, npm, yarn/pnpm, uv
- docker, kubectl, helm, terraform, gcloud
- go, rust (rustup), java (temurin), cmake, make, gcc/clang, pkg-config
- List all background service & auto start service. Report any suspicious service to `~/maintain.md`.

Step I - Docker

- `docker system prune`
- Log `docker system df` into  `~/maintain.md`.

Only update them via the system’s package manager (brew/apt). For language toolchains (rustup, gvm, nvm, pyenv), detect and log to `~/maintain.md`.

## Repo Maintain
>
> The problem is agent usually in HOST, if repo's runtime differ from HOST, agent can't rely on HOST has ecosystem as repo's runtime, especially on `npm`.

You are developer maintain ONLY current repo.
The goal is update repo's dependencies, run security scan.
Log relevant logs to `maintain.md`

### Find Orchestration Stack

- `echo "/n/n ## $(date '+%Y-%m-%d %H:%M')" >> maintain.md` Add maintain header.

- List current repo's orchestration stacks. Ex: k8s, docker, poetry, nvm
  - Find old stack version.
  - Update orchestration stack with appropriate update bash.
  - Find new stack version. Log update to `maintain.md`, (from -> to)

- For python repo
  - Scan vulnerabilities `pip-audit . >> maintain.md`
  - Does python repo missing poetry required files?
    - Create poetry required files: `pyproject.toml` & `poetry.lock`
  - `poetry show -o` List all outdated packages.
  - Create `latest_pyproject.toml` with latest dependencies reference `pyproject.toml`. (Because pip doesn't track package updates, always easier update through poetry)

- If js package manager used? Ex: `npm`, `yarn`, `pnpm`
  - `[npm/yarn/pnpm] audit >> maintain.md`
  - According audit log, generate SINGLE LINE command install all packages to install latest packages, log SINGLE command to `maintain.md`

### Agent work with Isolation

There are many virtualization tech stack for isolation env. Problem isolation env introduce barrier for Agent to works on these repos. Here are some tips / example commands for agent works on isolation env.

- For wsl
  - distros and versions: `wsl -l -v`
  - powershell command: `wsl -d Debian --% -- bash -lc "ls ~"`
- dev container
  - debug inside dev container: `python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m your_module`
- docker
  - For copying files out of a container: `docker cp <container>:/path ./` or `kubectl cp <pod>:/path ./`
  - For docker container: `docker exec -it <container> bash -lc "ls"`
  - For docker compose service: `docker compose exec <service> bash -lc "ls"`
- kubernetes
  - pod: `kubectl exec -it <pod> -- bash -lc "ls"`
  - debug port-forward: `kubectl port-forward <pod> 5678:5678`
- For ssh into a remote build host: `ssh -t user@host 'bash -lc "ls"'`

## Useful Resources

### Applications

- VS Code & Plugins  
  - Remote Containers  
  - Python  
  - ESLint  
  - Prettier  
  - Docker  
  - C#  
  - .NET Core Essentials  
  - Thunder Client  
  - Base64  
  - Code Spell Checker *(must install)*  
  - Kubernetes (official plugin to view K8s objects)  
  - Kubernetes Support (code snippets)  
  - Kubernetes Templates (snippets)  
  - Helm IntelliSense  

- Chrome  
  - React DevTools  
  - Redux DevTools  
  - Google Analytics  
  - `chrome://net-internals/`

- Docker  
  > Remove Windows PATH entries if CMD runs slowly.  

  > WSL 2 can have I/O bottlenecks.

- WSL  
  - Debian  

- OpenVPN  
- MobaXterm  
- PuTTY  
- DataGrid  

- Selenium – browser automation with richer UI interaction than Scrapy  

### Websites

- Icons: <https://gist.github.com/rxaviers/7360908>  
- Cron Guru: <https://crontab.guru/>  
- Tech Stacks: <https://stackshare.io/>  
- Company Investor Info: <https://www.crunchbase.com/>

- Create bots: <https://web.axiom.ai/recipes>  
- Math: <https://www.wolframalpha.com/>  
- PDF & other tools: <https://tinywow.com/>  
- Form templates: jotform.com  
- SASS products: <https://www.opensourcealternative.to/>

### Security / DevOps

- Vulnerability Scoring: <https://www.first.org/cvss/>  
- NetSpy – penetration testing  
- Checkmarx – code analysis  
- Rapid7  
- WhiteSource – checks for vulnerable dependencies (GPL 2/3 often denied; MIT preferred)

### Mock Data Generators

- Test data: <https://www.mockaroo.com/>  
- Mock APIs: <https://mockapi.io/>
