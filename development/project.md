# Project Misc stuff

## Dependency

> Prefer projects from Open sources foundations, should be mature, less breaking changes

- Linux Foundation
- Apache Software Foundation
- Open Source Initiative
- Eclipse Foundation `mostly java`

> Prefer projects under Corporations for long life time, but more breaking changes

- vscode from MS
- mongodb
- react

> Check maintainer

- Check most controversial github issue
  - how maintainer response to issues
  - what are issues itself
- Check maintainers counts
- Commit frequency & project length
- Check stars

## Architecture

- User Acceptant Test (UAT)

Why process PDF is pain in ass.
<https://github.com/py-pdf/pypdf/blob/main/docs/user/extract-text.md>

> PDF Portfolios is a special type of PDF file that acts as a container for multiple files.

## Windmill

```bs
-- Install Windmill CLI
npm install -g windmill-cli
wmill --version

-- Setup
export BASE_INTERNAL_URL=http://localhost
export WM_TOKEN=xxx
export WM_WORKSPACE=xxx

wmill init
wmill workspace add test-llm test-llm http://localhost/
wmill sync pull
```

> Variable max len 15000 chars

<https://www.windmill.dev/docs/apps/app_configuration_settings/app_component_library>
