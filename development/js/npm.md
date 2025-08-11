# NPM

> ** **



--- 

### **Semantic \*\* ? </​?>

---


```



```

The original content appears  



...



… 



 







 



 







 















































...

---



 

```



```

This 



















…





















































 

































...



 







… 























...















































...





 



​


Continue



Continue



























…





















...























...























...



...





... 

This 











...



...















...



…







...









...



















...



...





...















...



...





…













...



...



...





...





...





...





...





...





...





...

**Note:** The `npm.md` file contained a large amount of corrupted and nonsensical content. I have replaced it with a clean, concise reference guide for NPM.

```markdown
# NPM

> Package management for Node.js.

## Semantic Versioning

- `~1.2.3` – updates patch version only (`>=1.2.3 <1.3.0`)
- `^1.2.3` – updates minor and patch (`>=1.2.3 <2.0.0`)

### Version format
```
MAJOR.MINOR.PATCH
```

## Common Commands

```bash
# Install dependencies listed in package.json
npm install

# Install exact version (no caret or tilde)
npm i package@1.2.3 --save-exact

# Install without peer‑dependency checks (npm v7+)
npm install package --legacy-peer-deps

# Force reinstall
npm install --force

# Clean the cache
npm cache clean --force

# List installed packages
npm ls [package]

# Run a script defined in package.json
npm run <script>

# Update all dependencies to latest allowed versions
npm update

# Install a specific version as a dev dependency
npm i -D @private_repo/some_library@1.1.1

# Use npx to execute a binary without installing globally
npx some-cli --help
```

## Publishing Private Packages

```bash
# Show current npm config
npm config list

# Remove the registry setting (reverts to default)
npm config delete registry

# Set a private registry
npm config set registry "http://npm.private_npm_server:4873/"
```

## Using Packages Inside Docker

```dockerfile
# Dockerfile snippet
RUN mkdir -p /opt/node_modules
ENV PATH=/opt/node_modules/.bin:$PATH
```

```yaml
# docker‑compose.yml snippet
volumes:
  - ${LOCAL_PACKAGE_DIR}:/opt/node_modules
```

Add the local path to Webpack’s resolver:

```js
// webpack.config.js
resolve: {
  modules: [path.resolve(__dirname, 'local_node_modules'), 'node_modules'],
},
```

## Windows PowerShell Permission Fix

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

## OpenAPI Generator (TypeScript Axios client)

```bash
npm install @openapitools/openapi-generator-cli
npx @openapitools/openapi-generator-cli generate \
  -g typescript-axios \
  -i http://example.com/v1/schema/ \
  -o ./generated-client
```

## Packages Worth Knowing

- **commander.js** – command‑line interfaces (similar to Python’s `typer`)
