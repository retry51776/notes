# Front End

| Imperative | Declarative |
| --- | --- |
| state & UI transitions | only state |

> Page‑level fetching  
> Component‑level fetching  
> Server‑side fetching

## UI Libraries

Three types:

- **UI enhancement** – only enhances UI, not logic (e.g., SASS, LESS, Tailwind)
- **Behavior libraries** – only provides logic, not UI (e.g., React, React Table, React Query, Headless UI)
- **Style systems** – includes both UI and logic (e.g., Bootstrap, Tailwind UI, DaisyUI)  
  - *styled‑components* – define CSS inside a React component

## Redux
> Avoid `connect()` to reduce unnecessary props.  
> Prefer using the React context hook instead of Redux when possible.  

> Flow: `react → dispatch(action) → (middleware) → reducer → store → react`

```js
// 1. Setup actions – functions that return { type: 'XXX' }

// 2. Setup reducer – (state, action) => { /* do your thing */ }

// 3. Optional: create middleware; note the Redux DevTools extension is optional.
import { compose, createStore, applyMiddleware } from 'redux';

// 4. Define store
const store = createStore(
  reducer,
  // preloadedState can be passed here
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

// 5. Use Redux in a component
import { useSelector, useDispatch } from 'react-redux';

const [printing, periodEnd] = useSelector(state => [
  state.ABC.getIn(['ABC', 'printing']) || '[]',
  state.XYZ.getIn(['EFG', 'xyz']),
]);

const dispatch = useDispatch();

dispatch('ACTION_XYZ');
```

## React Component
> **key** – a unique identifier among siblings; React uses it to reuse elements. Using an index as a key is discouraged.  
> **ref** – for focusing or integrating third‑party libraries; Next.js server‑side caching can use refs to scope cache.

### React Reconciliation
- Determines which DOM nodes need replacement.
- If the element type changes, a new DOM node is created.
- If props change, the existing DOM node is updated.
- Keys allow reuse of DOM nodes among siblings.

### Rendering (ReactDOM vs. React Native)
- Uses React Fiber for non‑blocking rendering, supports aborting renders and dynamic imports.

`$$typeof: Symbol(react.element) // internal React identifier`

## ImmutableJS
> Benefits: fewer moving parts, performance (at the cost of RAM), decoupled logic.  
> Persistent immutable data structures enable structural sharing; unchanged parts are reused, saving memory despite higher overall usage.  
> Consider Immer for convenience, but be aware it introduces new APIs.

## React
> Functional components are truly immutable; class component state is mutable. Hooks provide true separation of state and logic.

### Component Preference Order

1. Component state
2. Redux store
3. Web actions
4. Event handlers
5. UI components

- `wouter` is an alternative to React Router.

```js
/* React router passes in history & match */
const Abc = ({ history, match }) => {
  return 'xxx';
};

Abc.propTypes = {
  history: PropTypes.object.isRequired,
  match: PropTypes.object.isRequired,
};

import React, { useMemo, useCallback, useEffect } from 'react';

// useCallback(fn, deps) is equivalent to useMemo(() => fn, deps).
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);

// Example of a higher‑order component chain
useEffect(() => {
  console.log('Similar to componentDidMount');
  return () => {
    console.log('Clean up listener');
  };
}, []);

React.createElement(type, props, ...children);
React.cloneElement(element, config, ...children);

// React.StrictMode

const ref = useRef(); // auto‑focus or server‑side reference
const forwardRefComponent = forwardRef(...);
useImperativeHandle(ref, () => ({
  /* expose methods */
}));

const [isUpdating, startUpdate] = useTransition();

const id = useId(); // generates a stable ID

function componentDidCatch(error, errorInfo) {
  // handle errors
}

import { useContext, createContext } from 'react';
const TerryContext = createContext(null);
<TerryContext.Provider value={/* ... */} />
```

## Upload File

```js
import JSZip from 'jszip';
import Dropzone from 'react-dropzone';

JSZip.loadAsync(files[0])
  .then(zip => setZip(zip))
  .catch(err => zipError(error));
```

## moment
> `moment` is effectively dead (2020). Use `dayjs` instead.  
> <https://twitter.com/addyosmani/status/1304676118822174721>

```js
import moment from 'moment';

moment.utc(backfill.get('ts')).local().format('YYYY-MM-DD @ HH:mm:ss a');
moment()
  .add(1, 'day')
  .subtract(1, 'year')
  .startOf('day')
  .endOf('month')
  .isSame(xxx, 'year');
```

## react‑query & react‑table
> Avoid column accessor strings like `'xxx.xx'`; use `'xxx-xx'` instead.

```js
const {
  data,
  isLoading,
  isFetching,
  status,
  refetch,
} = useQuery('abc', axiosPromise, {
  refetchOnWindowFocus: false,
  throwOnError: true,
  initialData: undefined,
  placeholderData: new Map(),
  staleTime: 60 * 60 * 24, // one day
  cacheTime: 60 * 60, // one hour
});

useEffect(() => {
  if (data?.hasMore) {
    queryClient.prefetchQuery(['xxx', page + 1], () => doFetch(page + 1));
  }
}, [data, page]);

const edit = useMutation(postEdit, {
  onSuccess: () => {
    queryClient.invalidateQueries('abc');
  },
});
```

**mouseflow** – page‑tracking plugin.

## Formik
> Create each form input in its own file.  
> Use a `FormikController` similar to React Router.  
> Note that many older repos are no longer maintained.

```js
const formik = useFormik({
  initialValues: { field: 'xyz' },
  onSubmit: values => {},
  validate: values => {
    const errors = { field: 'Always Error' };
    return errors;
  },
});

<Formik initialValues={{}} validationSchema={Yup.object({})} onSubmit={() => {}}>
  <Form>
    <Field name="field" type="text" placeholder="xx" />
    <Field as="textarea" name="text1" placeholder="xx" />
    <ErrorMessage name="field" />
    <FieldArray name="">
      {props => {
        const { push, remove, form } = props;
        return form?.values?.map(x => x);
      }}
    </FieldArray>
  </Form>
</Formik>
```

# Yup

```js
// Yup schema example
const validationSchema = Yup.object({
  field: Yup.string().required('Must provide a value'),
  complex_field: {
    initialValue: { label: 'Texas', value: 'TX' },
    type: Yup.object()
      .nullable()
      .when('field', {
        is: 'Test',
        then: Yup.string().required('When field = Test, complex_field must be filled')
      }),
    description: 'cccc'
  }
});
```

## Chakra UI
> Documentation: <https://chakra-ui.com/docs/components>

```js
import { ThemeProvider, theme } from '@chakra-ui/core';
<ThemeProvider theme={theme}>
  <MyFormikForm />
</ThemeProvider>;

import { Field } from 'formik';
import { Input, FormControl, FormLabel, FormErrorMessage } from '@chakra-ui/core';

<Field name="my_field">
  {(field, form) => (
    <FormControl>
      <Input {...field} />
    </FormControl>
  )}
</Field>;
```

## react‑hook‑form (RHF)

```js
import { Controller, useForm } from 'react-hook-form';

// Register manually
const { register } = useForm();
<input {...register('fName')} />;

// Using Controller
<Controller
  render={props => (
    <TextField label={name} error={errors[name]} {...props} />
  )}
  control={control}
  name={name}
/>;
```
