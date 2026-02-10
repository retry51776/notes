# Setup

> OS setup/maintain should done by agent. Agent maintain have audible log trace, that also readable with highlight details.

## Rule of thumb

- Package manager preference: brew > apt > uv > pip3 > npm > .pkg installer
- `~/.profile` should stores all setup scripts or envs, then `~/.bashrc` or `~./zshrc` should invoke `source ~/.profile`

## Setup Linux

1. run below bash

```bash
sudo apt update
sudo apt install -y curl ca-certificates git gnupg lsb-release nodejs wget unzip

curl -fsSL https://get.docker.com | sudo sh
```

## Setup Mac

You are running in mac os terminal. Your goal is setup os.

OS setup through multiple Phase, early Phase acts barrier to next Phase, unless user specifically change it.
Inside each Phase can have multiple tasks, only run parallel tasks in different terminals when user ask.
Prefer to install everything in homebrew if possible, because easier to update in future.

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
  - `python -m pip install pip-audit`

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

You are running in window os powershell. Your goal is setup os. Prefer to install everything in winget if possible, because easier to update in future.

> FYI, chocolatey is very good alternative package manager, follow instruction @ <https://chocolatey.org/install>

### Winget package manager

- `winget upgrade --all --accept-source-agreements --accept-package-agreements`
- `winget install Git.Git Python.Python.3.12 Docker.DockerDesktop`
- `winget install -e --id CoreyButler.NVMforWindows`

### Windows features

- `Get-WindowsOptionalFeature -Online` to list all windows features
- `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`

### Setup SSH

1) Ask user.name & user.email & user.passphrase

2) Check if ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519.pub already exist.
   - If they exist, do NOT overwrite. Just use them.
   - If not, generate a new ed25519 SSH key with:
     ssh-keygen -t ed25519 -C "<YOUR_EMAIL@example.com>" -f ~/.ssh/id_ed25519 -N "user.passphrase"

### Setup WSL

- Share HOST `~/.ssh` to WSL by symlink; Run below script IN WSL

```bash
# Runs WSL terminal
mkdir -p ~/.ssh
rm -rf ~/.ssh
ln -s /mnt/c/Users/<WindowsUser>/.ssh ~/.ssh
chmod 700 ~/.ssh
chmod 600 ~/.ssh/*
```

- Append to WSL file `/etc/wsl.conf`:

```bash
# /etc/wsl.conf

# Fix WSL commands are slow, **Remove Windows PATH from WSL**
[interop]
appendWindowsPath = false
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
   - npm outdated -g --depth=0
3) Safe-update globals without major bumps:
   - npm update -g xxx
   - If `npm update -g` throws error `EINVALIDPACKAGENAME Invalid package name ".[packpage_path]" of package`
      - go ahead run `sudo rm -rf $(npm root -g)/.[packpage_path]` to remove Invalid package, Add `~/maintain.md` what package removed.
      - try `npm update -g` again
4) Capture the global package list again `npm ls -g --depth=0`. Log what you updated (from -> to)
5) Log SINGLE BASH CMD update all major-version to `~/maintain.md`;

Step C — Homebrew (mac/linux)

1) `brew update` & `brew list --versions`
2) `brew outdated --verbose`
3) Upgrade safely without major bumps:
   - `brew upgrade`
   - `brew doctor`. Follow `brew doctor` notes to update/fix packages.
   - `brew cleanup`
4) Capture the global package list again `brew list --versions`. Log what you updated (from -> to)
5) `softwareupdate --list` && `softwareupdate --install --all` && `softwareupdate --list`. Log what you updated (from -> to)

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
2) `brew upgrade poetry`
3) `conda doctor`

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

- `echo "## $(date '+%Y-%m-%d %H:%M')" >> maintain.md`

- List current repo's orchestration stacks. Ex: k8s, docker, poetry, nvm
  - Log single bash update CMD to `maintain.md`, (from -> to)

- For poetry
  - `poetry show -o`

- For pip
  - `python -m pip install -r requirements.txt --dry-run --ignore-installed --report report.json` (see any packages may raise red flag)
  - Find repo's `requirements.txt`, then `pip-audit -r requirements.txt >> maintain.md`

- If js package manager used? Ex: `npm`, `yarn`, `pnpm`
  - `[npm/yarn/pnpm] audit >> maintain.md`
  - According audit log, generate SINGLE LINE command install all packages to install latest packages, log SINGLE command to `maintain.md`

## OS Security Scan

- `launchctl list | grep -v "com.apple"` list all none apple service, report any suspicious service.

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
