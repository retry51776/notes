# Backend
> What, nodejs has build-in fetch now! Only took years https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

## Key modules from runtime to framework
- node `runtime`
- http `node module`
- express `server framework`
- remix/nextjs `add SSR, file_route, websocket features on top express`


## Express
- In middleware, `next()` does NOT exit function
- Any operation could timeout, or involved multi datasources should use engine instead
- Keep route simple as possible, business logic should done on micro services

## NextJS & Remix
> MVC framework w react pattern


## download file
```js
//client
import { saveAs } from 'file-saver';
async function fetchBatch(id, filename) {
  const { data } = await axios.get(`/api/download/${id}/?`, {
    type: 'application/zip',
    responseType: 'arraybuffer',
  });
  const convertedFile = new Blob([data]);
  saveAs(convertedFile, filename);
}
//server
bucket = new GridFSBucket(xyz());
res.set({
  'Accept-Ranges': 'bytes',
  'Content-Disposition': `attachment; filename=${doc.filename}`,
  'Content-Type': 'application/zip',
});
bucket.openDownloadStream(doc.file_id).pipe(res);
return Promise.resolve();
```

## LDAP
```js
const LDAP = require('ldapjs'),
  config = require('@xxx/getconfig'),
  sltcCaFile = path.resolve('/certs/xxx_ca.crt');

const ldap = LDAP.createClient({
  url: config.ldap.uri,
  tlsOptions: {
    ca: [fs.readFileSync(caFile)],
  },
});

ldap.bind(config.ldap.bind_dn, config.ldap.bind_secret, err => {
  if (err) {
    const message = 'Error connecting to the LDAP server';
    app.get('logger').error({ req, err }, message);
    res.status(500).json({
      message,
      error: err,
    });
    return;
  }

  ldap.search(
    config.ldap.base_user_dn,
    ldap_query,
    callback,
  );
});
```

## Express & other libs
> more on expressjs.com/en/resources/middleware

- http `node server to handle network`
- express `web framework build on top http module`
- body-parser
- express-session `https://github.com/expressjs/session for docu`
- redis
- ejs # Template Engine
- helmet `Express header`
- jsonwebtoken
- Cookie-parser
- fs `fs.readdirSync()`
- request
- cros `app.get('/', cors(corsOpt), (req, res) => {})`
```js
const app = express(); # define request process

xxxRouter = express.Router(); # init express plugins

// attach express plugins
app.use('/xxx', xxxRouter);
app.use(express.static('public'))
app.use(bodyParser.json())

```

### http req & res
> both origin & referrer is attached by browser

> Block CROS will prevent embedded iframe, but won't protect from seliumn crawler

> define req, res object

> https://developer.mozilla.org/en-US/docs/WEb/http/headers

- Accept
- Keep-Alive
- Content-Encoding
- Content-Type
- Content-Disposition(Download File)
- Set-Cookie(server response) Cookie
- Cache-Control, Age(time been cache), Expires
- Request Context (From, Host)
```js
const server = http.createServer(app);
// server.address().address .port

server.listen(1234, err => {
})

req.headers.referer // where request redirect from (Ex: null, http://test:1234/sales/discount)
req.headers.origin // where request from (Ex: null, http://test:1234)
req.session // object
req.path
req.body
req.url
req.method

res.header('xxx', true)
res.status(401);
res.render('deny', {})
res.json({'message': 'no!'})
res.send('NO')
res.redirect('google.com')
```

### Redis Session
```js
const redisStore = req.sessionStore;
redisStore.get(req.xxxID, (err, sess) => {
  req.session // is available
})

// express redisSession
```
# Node Standard Lib
```js
import process from 'code:process';

process.cwd() // current directory
process.kill(process.pid) // process.ppid is parent_id

process.on('exit', () => {
});
```

## OPENAPI
> OpenAPI `is a specification`

> swagger `is tool with 3 components: UI, Editor, CodeGen`

> `tags` group endpoint into api;
> `operationId` should always `[tag]_methodName`

> openapi-cli won't generate request model w `multipart/form-data`, just api method params directly;
> while swagger generate request model;

### Keywords
- Style Values `standards of how serializeing complex value`
- parameter types `[path, query, header, cookie]`
- content type | media type `[application/json | xml | x-www-form-urlencoded, multipart/form-data, text/html, application/pdf, image/png]`
- data types `[string, number, integer, boolean, array, object]`
- required parameter `will generated as positional args`
- encoding `only apply for multipart request, control encoding per property`

- `requestBody.required`
- `requestBody.content.[application/json | multipart/mix]`
### Key Logic
- https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/python.md `generator doc`
- https://github.com/OpenAPITools/openapi-generator/blob/c59759f20a18dd2aaba9586943d99987cfd76f12/modules/openapi-generator/src/main/java/org/openapitools/codegen/DefaultCodegen.java#L4329 `openapi logic parse params`
- `mustache template`
### CodeGen & Editor
> 1. from spec(swagger.json) to template(flask routes)
>> https://editor.swagger.io `Check swagger file, generate server template`
>
>> openapi-generator `takes spec & generate server template, use their docker image`
> 2. from annotation to spec
>> apispec `takes docstring & marshmallow to generate spec https://gist.github.com/arundhaj/5f4c0f8c9a8efba9f92f81adea9fd4d7`

### Documentation UI
- Redoc `is nicer looking react api-documentation from swagger` `redoc-cli bundle -o /public/doc.html xx_swagger.yml`
- swagger static ui `static editor, change {{base_url}}`


# Buzzwords
JWT is value base token, cookie is reference base token

- Import Relative Path : <https://www.youtube.com/shorts/WpgZKBtW_t8>
- Scaffolding `MVC folder structure /bin /public /route /view`

