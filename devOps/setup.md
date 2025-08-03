# Developer Setup
>
> Checklist for setup my env, my host os still windows or mac, even I works w linux a lot; There are too many linux, and when things goes wrong harder to google solution.

## Applications

- Sublime
- VS Code & Plugins
  - remote container
  - python
  - eslint
  - prettier
  - docker
  - C#
  - .net core essentials
  - Thunder Client
  - Base64
  - Code Spell Checker `Must Install`
  - Kubernetes `Official plugin let VS view k8 objects`
  - Kubernetes Support `the code snippets wasn't full k8 sets, i hate it`
  - Kubernetes Templates `code snippets`
  - Helm intellisense
  - Preference/Setting
    - Default Formatter: Prettier
    - Format On Save Mode: file
    - Autocomplete trigger
      - Commit characters
      - keyboard shortcut(trigger suggest)
- Chrome
  - react dev
  - redux dev
  - google analytics
  - [chrome://net-internals](chrome://net-internals/)
- Windows Terminal
- Docker
  > remove windows path if CMD run slow

  > WSL2 could have IO bottleneck
- WSL
  - debian
- OpenVPN
- MobaXTerms
- Putty
- DataGrid
- Homebrew
  - minikube `https://minikube.sigs.k8s.io/docs/start/`
  - kind

## VS code setting

```json
{
  "editor.emptySelectionClipboard": false
}
```

## Cool resources

- [Icons] <https://gist.github.com/rxaviers/7360908>
- [Cron Guru] <https://crontab.guru/>
- [Tech Stacks] <https://stackshare.io/>
- [Company Investor] <https://www.crunchbase.com/>

- [Create bots]<https://web.axiom.ai/recipes>
- [Math] <https://www.wolframalpha.com/>
- [PDF & other tools] <https://tinywow.com/>
- [Form Template] jotform.com
- [SASS product] <https://www.opensourcealternative.to/>

## Datatool

- HDFView #view tool for .h5
- R-Studio is hardware data recovery
- winhex
- mrtlab needs special hardware

# UI Tool

- [Figma: Design Pic](https://www.figma.com/)
- <https://videohive.net/>

## Linux GUI Tools

- Stacer
  > Similar PC manager
- Gnome Tweak Tool
  > Manage Windows Theme

# Security/DevOps

- Vulnerability Scoring <https://www.first.org/cvss/>
- netspy (Pen/Penetration testing)
- checkmarx `check code`
- Rapid7
- whitesource (check software dep security versions has security bugs)
  > GPL 2/3 are often deny, MIT is prefer

# Project Apps

- Selenium

> automation of web browsers, more features(EX: UI interaction) than scrapy

# Workflow

- Visio
- Draw.io

# Mock Data

- Generate test data <https://www.mockaroo.com/>
- <https://mockapi.io/>

**Windows Sub Linux**

1. `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
2. Go to Microsoft Store & get Debian

> ~/.bashrc is bash setting
> PS = Prompt String, just like python `Export PS ="\t"`
Try remove windows path from WSL if cmd in WSL is slow

- In `/etc/wsl.conf` add

```bash
[interop]
appendWindowsPath = false
```
