# Front End

| Imperative | Declarative |
| --- | --- |
| state & UI transitions | only state |

> Page level fetching
> Component level fetching
> Server side fetching

## UI Libraries

3 types:

- UI enhancement `Only enhance UI, not logic; Ex: SASS, LESS, Tailwind`
- Behavior Libraries `Only logic, not UI; Ex: React, ReactTable, ReactQuery, headlessui`
- Style Systems `Both UI & logic; Ex: Bootstrap, TailwindUI, DaisyUI`
  - styled-components `Define css in react component`

## Redux
>
> Avoid redux connect() to reduces unnecessary props

> Avoid using redux at all, just uses react context hook

> react -> dispatch(action) -> (middleware) -> reducer -> store -> react

```js
// 1. Setup Actions: function return {type: 'xxx'}

// 2. Setup Reducer: (state, action => {do_your_thing})

// 3. Optional: create middleware, redux-devtools-extension(WTF they thinking, read latest doc)
import { compose, createStore, applyMiddleware } from 'redux';

// 4. Define Store
const store = createStore(
  reducer, /* preloadedState, */
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);


// 5. uses Redux in component
import { useSelector, useDispatch } from 'react-redux';

// As long as redux will refresh same components, otherwise don't be lazy
const [printing, periodEnd] = useSelector(state => [
  state.ABC.getIn(['ABC', 'printing']) || '[]',
  state.XYZ.getIn(['EFG', 'xyz']),
]);

const dispatch = useDispatch();

dispatch('ACTION_XYZ');

```

## React Component
>
> key:
>> unique id from SIBLING, react uses key to reuses element, which is WHY bad idea to use index as key

> ref:
>> for focus, or 3rd party lib; NextJS ServerSide caching using Ref to scope cache
  
> ### React Reconciliation
>>
>> determent which node of DOM tree needs replace
>
>> type changed? generate new DOM
>
>> props changed? update effected DOM
>
>> try to reused DOM by key. Only in silbing
>
> ### Rendering by ReactDom or ReactNative
>>
>> React Fiber, none blocking, support abort rending, dynamic import

`$$typeof:Symbol(react.element) // react internal id`

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
>
> Functional component is truely immutable, but class component's state is mutable; Because hooks allow true decouple of state

### Component Prefer Orders

1. Component States
2. Redux Store
3. Web actions
4. Events Handler
5. UI Components

- wouter is alterative to React Router

```js
/* React router pass in history & match*/
const Abc = ({ history, match }) => {
  return 'xxx'
};

Abc.propTypes = {
  history: PropTypes.object.isRequired,
  match: PropTypes.object.isRequired,
};

import React, { useMemo, useCallback, useEffect } from 'react';

// useCallback(fn, deps) is equivalent to useMemo(() => fn, deps).
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);

// Uses for HOC chain multiple different lifted states together
useEffect(() => {
  console.log('Similar to componentDidMount');
  return () => {
    console.log('Clean up listener');
  };
}, [])

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

// React.StrictMode 

useRef // Auto focus, or scoping sever side reference
forwardRef // reassign ref
useImperativeHandle // Specialize Event Handler when ref is changed

const [updating, startUpdate] = useTransition();

useId() generate hash
componentDidCatch(error, errorInfo) {
import { useContext, createContext } from 'react';

const TerryContext = createContext(null);
<GrouperContext.Provider value={}
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
>
> it's dead 2020 Aug, uses dayjs instead
<https://twitter.com/addyosmani/status/1304676118822174721>

```js
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
>
> avoid column accessor 'xxx.xx' , instead 'xxx-xx'

```js
const {
  data,
  isLoading,
  isFetching,
  status,
  refetch,
} = useQuery('abc', axios_promise, {
  refetchOnWindowFocus: false,
  throwOnError: true,
  initialData: undefined, // initialData will have staleTime too
  placeholderData: Map(), // use placeholderData, almost never use initialData
  staleTime: 60 * 60 * 24, // how long until data is dirty
  cacheTime: 60 * 60, // stay in cache even left page
});

useEffect(() => {
  if (data?.hasMore) {
    queryClient.prefetchQuery(['xxx', page + 1], doFetch(page + 1))
  }
}, [data, page])

const edit = useMutation(postEdit, {
  onSuccess: () => {
    queryClient.invalidateQueries('abc')
  }
})
```

**mouseflow**
> Page tracking plugin

## Formik
>
> Created Each Form Input in its own file
>
> Then Have a FormikController similar react_router
>
> Another dead popular repo

```js
const formik = useFormik({
  initialValues: {
    'field': 'xyz'
  },
  onSubmit: values => {},
  validate: values => {
    let errors = {
      field: 'Always Error'
    };
    return errors;
  },//or
  //validationSchema
})

//formik.values.field one of "", {}, []
//formik.handleSubmit uses ref.name
//formik.error.field ? 'Bad' : null

//formik.handleBlur & formik.touched.field
//{...formik.getFieldProps('field')}

//FastField decode state change, only rerender when sub state it uses changed
<Formik
  initialValues={}
  validationSchema={}
  onSubmit={}
>
  <Form>
    <Field name="field" type="text" placeholder="xx">
    <Field as="textarea" name="text1" placeholder="xx">
    <ErrorMessage name="field" />
    <FieldArray name="">
      {
        props => {
          const { push, remove, form } = props;
          return form?.values?.map(x => x)
        }
      }
    </FieldArray>
  </Form>
</Formik>
```

# Yup

```js
// Yup as schema
//string().oneOf([Yup.ref('password'), ''])
//.test('test-id', 'error-msg', val=>!val)
const validationSchema = Yup.object({
  field: Yup.string().required('Must field'),
  complex_field: {
    initialValue: {
      label: 'Texas',
      value: 'TX',
    },
    type: object()
      .nullable()
      .when('field', {
        'is': 'Test',//can also be () => {}
        then: string().required('field = Test, complex_field must fill')
      }),
    description: 'cccc'
  }
})
```

## Chakra UI
>
> <https://chakra-ui.com/docs/components>

```js

// Input
// 
import { theme, ThemeProvider } from '@chakra-ui/core';
<ThemeProvider them={them}>
  <MyFormikForm />
</ThemeProvider>

import { Field } from 'formik';
import { Input, FormControl, FormLabel, FormErrorMessage } from '@chakra-ui/core';
<Field name="my_field">
  {
    ((field, form)) => {
      return (
        <FormControl>
          <Input />
        </FormControl>
      );
    }
  }
</Field>
```

## react-hook-form (RHF)
>
> TODO: figure how it work
> <https://react-hook-form.com/api/useform/formstate/>

```js
import { Controller, useForm } from "react-hook-form";
// register manually
const { register } = useForm();
<input {...register("fName")} />

// Controller
<Controller
  render={props => (
    <TextField
      label={name}
      error={errors[name]}
      {...props}
    />
  )}
  control={control}
  name={name}
/>
```
