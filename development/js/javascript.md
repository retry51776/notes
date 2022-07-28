# ES6 stuff
> I don't keep up w JS too much, but I am sure 20 years later JS still lives on.


**Frustration**
- Why not support name parameter? `test(name='a', age=3)`
- `const` only works with basic type. like string or number.
- `null` & `undefined`, I get it, but hate it. Python just have None, much easier
- To store large dataset in Json `JSON.parse("{XXX}")` is faster than `test = {XXX}`

## Emerscript Changes
- ES1 `1997`
- ES2 `1998`
- ES3 `1999 Try/Catch, Regx`
  - ES3.1 `microsoft drama`
- ES5 `2009 JSON, Array, Common StandardLib methods`
- ES6 `2015 for of; ()=>{}; Modules`
- ES7 `2016 @decorator(); observe; includes`
- ES8 `2017 Async Await`
- ES9 `2018 {...others};`
- TS


JS modules(import/export)
CommonJS (require/exports)

**callback vs Promise vs async/await**  
- callback
  > callback hell
- Promise
  > `new Promise((resolve, reject) => {}); XXX.then().catch()`   very bad read if multi nest, Promise(`blocking code`).then(`not blocking code`)

  > Promise.all(threePromises).spread((xx, yy, zz) => whatever(xx, yy, xx));`
- `async await, try, catch`
  > cleaner read, but still complex

  > `await` must have `async` decorator, but call `async` function can invoke without `await`

**Usefully Features**
- Destruct Object `const { rules, ...otherProps } = this.props;`
- Rename destruct array `const [a1, a2] = [1, 2];`
- Nullish coalescing operator `const test = 0 ?? '-';`
- Optional chaining `const test = {}?.a?.b?.c;`
- Merge unique items from arrays `[...new Set([...array1, ...array2])]`



## ES6
```js
// ES6 build in supports, most browser, webpack will auto figure file type
import getXYZ from 'xyz.js';
// dynamic import
async componentDidMount() {
  const { ABC } = await import('./ABC');
  this.setState({ ABC });
}

// Common JS module function, can be dynamics run
module.export = {};
require('./xyz.js')

// Format
xxx.toFixed()
xxx.toLocalString({
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
})

// Types
Number.isNan()
typeof xx === 'boolean'
```

# Buzzwords
- JWT is value base token, cookie is reference base token
- Import Relative Path : <https://www.youtube.com/shorts/WpgZKBtW_t8>
- JS Guide : <https://github.com/airbnb/javascript/tree/master/react>
- Javascript VM instance
- Tokenlized
- Abs Structure Tree
- Binary Code
- Optimizer