# ES6 stuff


> To store large dataset in Json
`JSON.parse("{XXX}")` is faster than `test = {XXX}`

**callback vs Promise vs async/await**  
- callback - the worst  
- Promise - `new Promise((resolve, reject) => {}); XXX.then().catch()`   very bad read if multi nest, Promise(`blocking code`).then(`not blocking code`)
- `async await, try, catch` - cleaner read, but still complex
- `Promise.all(threePromises).spread((xx, yy, zz) => whatever(xx, yy, xx));`

**Usefull Features**
- Destruct Object `const { rules, ...otherProps } = this.props;`
- Rename destruct array `const [a1, a2] = [1, 2];`
- Nullish coalescing operator `const test = 0 ?? '-';`
- Optional chaining `const test = {}?.a?.b?.c;`
- Merge unqiue items from arrays `[...new Set([...array1, ...array2])]`


**Frustration**
- Why not support name parameter? `test(name='a', age=3)`
- `const` only works with basic type. like string or number.

# Front End Library
## React/Redux
Component Prefer Orders
1. Component States
2. Redux Store
3. Web actions
4. Events Handler
5. UI Components

>avoid redux connect() reduces unnecessary props defination
```
import { useSelector, useDispath } from 'react-redux';

const [printing, periodEnd] = useSelector(state => [
  state.queryString.getIn(['queryParameters', 'printing']) || '[]',
  state.queryString.getIn(['queryParameters', 'period_end']),
]);

const Abc = ({ history, match }) => {
  return 'xxx'
};

Abc.propTypes = {
  history: PropTypes.object.isRequired,
  match: PropTypes.object.isRequired,
};


import React, { useMemo, useCallback } from 'react';

// useCallback(fn, deps) is equivalent to useMemo(() => fn, deps).
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
React.createElement(
  type,
  [props],
  [...children]
);
React.cloneElement(
  element,
  [config],
  [...children]
);
```

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

## Upload File
```
import JSZip from 'jszip';
import Dropzone from 'react-dropzone';
JSZip.loadAsync(files[0])
  .then(zip => setZip(zip))
  .catch(err => zipError(error));
```

## moment
> it's dead 2020 Aug, uses dayjs instead
https://twitter.com/addyosmani/status/1304676118822174721
```
import moment from 'moment';
moment
  .utc(backfill.get('ts'))
  .local()
  .format('YYYY-MM-DD @ HH:mm:ss a');
moment().add('day', 1).subtract('year', 1);
.startOf('day')
.endOf('month')
.isSame(xxx, 'year')
```
## react-query & react-table
>avoid column accessor 'xxx.xx' , instead 'xxx-xx'
```
const {
  data,
  isLoading,
  isFetching,
  refetch,
} = useQuery('abc', axios_promise, {
  refetchOnWindowFocus: false,
  throwOnError: true,
  initialData: null,
});
```

**mouseflow**
> Page tracking plugin

# Backend
**Express**
- In middleware, `next()` does NOT exit function
- Any operation could timeout, or involed multi datasources should use engine instead
- Keep route simple as possiable, bussiness logic should done on micro services

**LDAP**
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
- JS Guide : <https://github.com/airbnb/javascript/tree/master/react>
