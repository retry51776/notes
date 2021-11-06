
# Backend
## Express
- In middleware, `next()` does NOT exit function
- Any operation could timeout, or involed multi datasources should use engine instead
- Keep route simple as possiable, bussiness logic should done on micro services

## nextJS
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


# Tech Terms
JWT is value base token, cookie is reference base token

- Import Relative Path : <https://www.youtube.com/shorts/WpgZKBtW_t8>