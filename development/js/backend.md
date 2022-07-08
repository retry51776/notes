# Backend

- node - runtime
- http - node module
- express - server framwork
- remix/nextjs - add SSR, file_route, websocket features on top express


## Express
- In middleware, `next()` does NOT exit function
- Any operation could timeout, or involed multi datasources should use engine instead
- Keep route simple as possiable, bussiness logic should done on micro services

## nextJS & Remix
> MVC framework w react pattern


## download file
```
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
```
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
- express-session
- redis
- ejs # Template Engine
- helmet `Express header`
- jsonwebtoken
- Cookie-parser
- fs `fs.readdirSync()`
- request
- cros `app.get('/', cors(corsOpt), (req, res) => {})`
```
const app = express(); # define request process

xxxRouter = express.Router(); # init express plugins

// attach express plugins
app.use('/xxx', xxxRouter);
app.use(express.static('public'))
app.use(bodyParser.json())

```

### http req & res
> both origin & referer is attched by brower

> Block CROS will prevent embeded iframe, but won't protect from seliumn crawler

> define req, res object

> https://developer.mozilla.org/en-US/docs/WEb/http/headers

- Accept
- Keep-Alive
- Content-Encoding
- Content-Type
- Set-Cookie
- Cookie
```
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
```
const redisStore = req.sessionStore;
redisStore.get(req.xxxID, (err, sess) => {
  req.session // is avaiable
})
```
# Node Standard Lib
```
import process from 'code:process';

process.cwd() // current directory
process.kill(process.pid) // process.ppid is parent_id

process.on('exit', () => {
});
```



# Buzzwords
JWT is value base token, cookie is reference base token

- Import Relative Path : <https://www.youtube.com/shorts/WpgZKBtW_t8>
- Scaffolding `MVC folder structure /bin /public /route /view`


## Mistery Errors
1. Memory Issue
```
error: Forever detected script was killed by signal: SIGKILL
```
2.