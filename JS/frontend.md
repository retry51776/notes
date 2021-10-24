# Front End Library
| Imperative | Declarative |
| --- | --- |
| state & UI transitions | only state |

## Reudx
> Setting up Redux Store is a nightmare

>avoid redux connect() reduces unnecessary props defination

react -> dispatch(action) -> (middleware) -> reducer -> store -> react

```
1. Setup Actions: function return {type: 'xxx'}

2. Setup Reducer: (state, action => {do_your_thing})

3. Optional: create middleware, redux-devtools-extension(WTF they thinking, read latest doc)
import { compose, createStore, applyMiddleware } from 'redux';

4. const store = createStore(
  reducer, /* preloadedState, */
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);


5. uses Redux in component
import { useSelector, useDispatch } from 'react-redux';

// As long as redux will refresh same components, otherwise don't be lazy
const [printing, periodEnd] = useSelector(state => [
  state.ABC.getIn(['ABC', 'printing']) || '[]',
  state.XYZ.getIn(['EFG', 'xyz']),
]);

const dispatch = useDispatch();

dispatch('ACTION_XYZ');

```

1. React Component
type:
  > component string

  > component reference
key:
  > unqiue id from SILBING, react uses key to reuses element, which is WHY bad idea to use index as key

ref:
  > for focus, or 3rd party lib
  
`$$typeof:Symbol(react.element)`
  > react internal id

1. React Reconsiliation
  > determent which node of DOM tree needs replace

  > type changed? generate new DOM

  > props changed? update effected DOM

  > try to reused DOM by key. Only in silbing

3. Rendering by ReactDom or ReactNative
   > React Fiber, none blocking, support abort rending, dynamic import

props:
```
{
  type: "main"
}
```

## ImmutableJS

> Why? Fewer moving parts, performance(on cost of RAM), decouple logic

DX/UX mullet
> Immediate Mode in front, Retained Mode in back

persistent immutable data structure
> hash each data level for read, search (performance)

structural sharing
> changes will make a new object, with references of values havn't changed

> save memory(still uses more than single variables)


Maybe Immer? new dev could break things, but no new APIs

## React
Component Prefer Orders
1. Component States
2. Redux Store
3. Web actions
4. Events Handler
5. UI Components

```
/* React router pass in history & match*/
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


# Windows Events
> React.StrictMode 
```
useEventListener("online", callback);
```
- mousemove
- offline

useRef // Auto focus
componentDidCatch(error, errorInfo) {
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

# Webpack, module bunder
or rool up, parcel, snowpack

### Styles
- `node-sass` provides binding for Node.js to LibSass, a Sass compiler.
- `sass-loader` is a loader for Webpack for compiling SCSS/Sass files.
- `style-loader` injects our styles into our DOM.
- `css-loader` interprets @import and @url() and resolves them.
- `mini-css-extract-plugin` extracts our CSS out of the JavaScript bundle into a separate file, essential for production builds.

### JS
`babel` - es6
`polyfill` - browser compability

### webpack.config.js
```
const webpack = require('webpack');
const path = require('path');
// const merge = require('webpack-merge');
// process.env.npm_lifecycle_event

module.exports = {
  context: path.join(__dirname, 'xyz/'),
  entry: {
    /* multi entry will code splitting */
  },
  output: {},
  module: {
    rules: [
      {
        test: /* regx find target files */,
        use: [/* loaders */]
      }
    ]
  },
  // devtool: 'cheap-eval-source-map',
  plugins: [
    new CleanWebpackPlugin(),
    new webpack.HashedModuleIdsPlugin(),
    new webpack.optimize.SplitChunksPlugin(),
    new HtmlWebpackPlugin({
      filename: 'views/index.html',
      title: 'Terry',
      template: 'views/base.ejs',
    }),
    // Example inject variable into front end
    new webpack.DefinePlugin({
      AUTHOR: 'Terry',
      ANOTHER_ENV: '123',
    }),
  ],,
}
```