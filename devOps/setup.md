# Developer Setup
>
> Checklist for setting up my environment. My host OS may be Windows or macOS, though I work with Linux a lot. There are many Linux variations, and when things go wrong it’s harder to find solutions.

## Applications

- Sublime Text  
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

- Windows Terminal  
- Docker  
  > Remove Windows PATH entries if CMD runs slowly.  

  > WSL 2 can have I/O bottlenecks.

- WSL  
  - Debian  

- OpenVPN  
- MobaXterm  
- PuTTY  
- DataGrid  
- Homebrew  
  - minikube – <https://minikube.sigs.k8s.io/docs/start/>  
  - kind  

## VS Code Settings

`vscode://file/<absolute-path-to-file>:<line>:<column>` only works within VS code.

```json
{
  "editor.emptySelectionClipboard": false
}
```

## Useful Resources

- Icons: <https://gist.github.com/rxaviers/7360908>  
- Cron Guru: <https://crontab.guru/>  
- Tech Stacks: <https://stackshare.io/>  
- Company Investor Info: <https://www.crunchbase.com/>

- Create bots: <https://web.axiom.ai/recipes>  
- Math: <https://www.wolframalpha.com/>  
- PDF & other tools: <https://tinywow.com/>  
- Form templates: jotform.com  
- SASS products: <https://www.opensourcealternative.to/>

## Data Tools

- HDFView – view `.h5` files  
- R‑Studio – hardware data recovery  
- WinHex  
- MRTLab – requires special hardware  

## UI Tools

- Figma – design mockups (<https://www.figma.com/>)  
- Videohive – stock video assets (<https://videohive.net/>)

## Linux GUI Tools

- Stacer – system manager  
- GNOME Tweak Tool – manage window themes  

## Security / DevOps

- Vulnerability Scoring: <https://www.first.org/cvss/>  
- NetSpy – penetration testing  
- Checkmarx – code analysis  
- Rapid7  
- WhiteSource – checks for vulnerable dependencies (GPL 2/3 often denied; MIT preferred)

## Project Apps

- Selenium – browser automation with richer UI interaction than Scrapy  

## Workflow Tools

- Visio  
- Draw.io  

## Mock Data Generators

- Test data: <https://www.mockaroo.com/>  
- Mock APIs: <https://mockapi.io/>

### Windows Subsystem for Linux (WSL)

1. Enable the feature:  

   ```powershell
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   ```

2. Install Debian from the Microsoft Store.

> `~/.bashrc` contains Bash settings.  
> `PS` is the prompt string, similar to Python’s `export PS="\t"`.

**Remove Windows PATH from WSL** if commands are slow:

Add to `/etc/wsl.conf`:

```bash
[interop]
appendWindowsPath = false
```
