# Backend

> Node.js now includes a built‑in `fetch` API. It took years to arrive.  
> <https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch>

## Key Modules from Runtime to Framework

- **node** – runtime
- **http** – core HTTP module
- **express** – server framework
- **remix / nextjs** – adds SSR, file‑based routing, and WebSocket features on top of Express

## Express

- In middleware, calling `next()` does **not** exit the function.
- Any operation that could time out—or that involves multiple data sources—should use an engine (e.g., a job queue).
- Keep routes as simple as possible; business logic belongs in micro‑services.

## Next.js & Remix
> MVC frameworks with a React pattern.

## Download File

```js
// client
import { saveAs } from 'file-saver';
async function fetchBatch(id, filename) {
  const { data } = await axios.get(`/api/download/${id}/?`, {
    type: 'application/zip',
    responseType: 'arraybuffer',
  });
  const blob = new Blob([data]);
  saveAs(blob, filename);
}

// server
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
const LDAP = require('ldapjs');
const config = require('@xxx/getconfig');
const caFile = path.resolve('/certs/xxx_ca.crt');

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

  ldap.search(config.ldap.base_user_dn, ldap_query, callback);
});
```

## Express & Other Libraries

- **http** – Node server to handle network traffic
- **express** – web framework built on top of the HTTP module
- **body‑parser**
- **express‑session** – <https://github.com/expressjs/session>
- **redis**
- **ejs** – template engine
- **helmet** – security headers
- **jsonwebtoken**
- **cookie‑parser**
- **fs** – e.g., `fs.readdirSync()`
- **request**
- **cors** – usage: `app.get('/', cors(corsOpt), (req, res) => {})`

```js
const app = express(); // define request processing

const xxxRouter = express.Router(); // init router

// Attach middleware and routes
app.use('/xxx', xxxRouter);
app.use(express.static('public'));
app.use(bodyParser.json());
```

### HTTP Request & Response

- Both `origin` and `referer` are sent by the browser.
- Blocking CORS prevents embedded iframes but does not stop Selenium crawlers.
- Important headers: Accept, Keep‑Alive, Content‑Encoding, Content‑Type, Content‑Disposition, Set‑Cookie, Cache‑Control, Age, Expires.

```js
const server = http.createServer(app);
server.listen(1234, err => { /* ... */ });

req.headers.referer; // where the request came from (may be null)
req.headers.origin;   // origin of the request (may be null)
req.session;         // session object
req.path;
req.body;
req.url;
req.method;

res.setHeader('xxx', true);
res.status(401);
res.render('deny', {});
res.json({ message: 'no!' });
res.send('NO');
res.redirect('https://google.com');
```

### Redis Session

```js
const redisStore = req.sessionStore;
redisStore.get(req.xxxID, (err, sess) => {
  // session is now available via req.session
});
```

## Node Standard Library

```js
import process from 'process';

process.cwd();          // current working directory
process.kill(process.pid); // kill the current process
process.on('exit', () => { /* ... */ });
```

## OpenAPI

- Specification for describing RESTful APIs.
- Swagger provides UI, editor, and code generation.

Key concepts:

- **tags** – group endpoints
- **operationId** – should follow `[tag]_[methodName]`
- `multipart/form-data` handling differs between openapi‑cli and swagger generators.

### Keywords

- Style values – how complex values are serialized
- Parameter locations – `path`, `query`, `header`, `cookie`
- Media types – e.g., `application/json`, `application/x-www-form-urlencoded`, `multipart/form-data`
- Data types – `string`, `number`, `integer`, `boolean`, `array`, `object`
- Required parameters become positional arguments
- Encoding – applies to multipart requests

### Code Generation & Editor

1. Generate server code from a spec (e.g., Swagger → Flask routes).  
   <https://editor.swagger.io>
2. Generate a spec from annotations (e.g., `apispec` with docstrings and Marshmallow).

## Documentation UI

- **Redoc** – modern React API docs (`redoc-cli bundle -o /public/doc.html swagger.yml`)
- Swagger static UI – customizable via `{{base_url}}`

# Buzzwords

- JWT is a value‑based token; cookies are reference‑based tokens.
- Relative imports: <https://www.youtube.com/shorts/WpgZKBtW_t8>
- Scaffolding – typical MVC folder structure (`bin`, `public`, `route`, `view`).
