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