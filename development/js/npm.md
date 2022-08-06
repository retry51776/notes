# NPM 

libtrends.info/npm-compare

semantic versioning
`~` only update patch
`^` update minor & path

> remember reset lower level when increase major or minor

- major.minor.patch
> `npm update` to upgrade latest library
- package.lock.json
> force npm install library target version

To build library
`"build": "rimraf dist; npm run prettier; npm run compile; npm pack;"`

To install library
`npm install @private_repo/some_library@1.1.1 --save-dev --save-exact`

Only run `npm install` to init Project, then always `npm ci`

Node Package Execute `npx allow excute without install`

Other npm cmds
```js
// Ignore npm v7+ peer deps checks
npm install xxx --legacy-peer-deps
// Force npm to fetch remote resources
npm install xxx --force

npm cache clean --force  
npm install -i xyz
npm install --no-optional  
npm run [package.json/script]
npm ls xyz // to check repo has library

npm start --prefix folderA

// Update local packages
npm update
```

**Reset private registry **
```bash
npm config list  
npm config delete registry  
npm config set registry "http://npm.private_npm_server:4873/"  
registry = "http://npm.private_npm_server:4873/"  
/.npmrc
```

**Setup Dependence Library within Project **
```dockerfile
Step 1: Mount Library Source into Container  
Dockerfile  
RUN mkdir -p /opt/node_modules  
ENV PATH /opt/node_modules/.bin:$PATH  
  
docker-compose.yml  
- ${LOCAL_PACKAGE_DIR}:/opt/node_modules  
  
Step 2: Add to Webpack Resolve  
webpack.config.js  
resolve: {  
modules: [PATHS.localNode, 'node_modules'],  
unsafeCache: /assets/,  
},
```

Windows ESLint failed permission
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

```bash
npx @openapitools/openapi-generator-cli generate -g typescript-axios -i http://xxx:/v1/schema/ -o /ajax
```