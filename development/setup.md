# Setup Developer Applications
- Sublime
- VS Code
  - remote container
  - python
  - eslint
  - prettier
  - docker
  - C#
  - .net core essentials
  - Thunder Client
  - Base64
  - kubenetes
  - Preference/Setting
    - Default Formatter: Prettier
    - Format On Save Mode: file
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
  - 

## Cool resources
- [Icons] https://gist.github.com/rxaviers/7360908
- [Cron Guru] https://crontab.guru/
- [Tech Stacks] https://stackshare.io/
- [Company Investor] https://www.crunchbase.com/

## Datatool
- Generate test data https://www.mockaroo.com/
- HDFView #view tool for .h5
- R-Studio is hardware data recovery
- winhex
- mrtlab needs special hardware

# UI Tool
https://www.figma.com/
> Design Pic
https://videohive.net/


## Linux GUI Tools
- Stacer
  > Similar PC manager
- Gnome Tweak Tool
  > Manage Windows Theme

# Security/DevOps
- Vulnerability Scoring https://www.first.org/cvss/
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

**Windows Sub Linux**
1. `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
2. Go to Micr Store & get Debian

> ~/.bashrc is bash setting
> PS = Prompt String, just like python `Export PS ="\t"`
Try remove windows path from WSL if cmd in WSL is slow
- In `/etc/wsl.conf` add
```
[interop]
appendWindowsPath = false
```