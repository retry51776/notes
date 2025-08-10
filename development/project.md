# Project Misc Stuff

## Dependency

> Prefer projects from open‑source foundations; they should be mature and have fewer breaking changes.

- Linux Foundation
- Apache Software Foundation
- Open Source Initiative
- Eclipse Foundation `mostly Java`

> Prefer projects backed by corporations for long lifetimes, though they may introduce more breaking changes.

- VS Code (Microsoft)
- MongoDB
- React

> Check maintainer activity:

- Review the most controversial GitHub issues and how maintainers respond.
- Count the number of maintainers.
- Examine commit frequency and project age.
- Look at star count.

## Architecture

- User Acceptance Test (UAT)

Why processing PDFs is a pain:
<https://github.com/py-pdf/pypdf/blob/main/docs/user/extract-text.md>

> PDF portfolios are a special type of PDF file that act as containers for multiple files.

## Windmill

> The Windmill worker uses `nsjail`; `nsjail` supports the “loader_file” option in the job directory to set up the environment.

```bash
# Install Windmill CLI
npm install -g windmill-cli
wmill --version

# Setup
export BASE_INTERNAL_URL=http://localhost
export WM_TOKEN=xxx
export WM_WORKSPACE=xxx

wmill init
wmill workspace add test-llm test-llm http://localhost/
wmill sync pull
```

> Variable maximum length: 15 000 characters.

<https://www.windmill.dev/docs/apps/app_configuration_settings/app_component_library>
