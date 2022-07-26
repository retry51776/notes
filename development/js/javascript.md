# ES6 stuff


> To store large dataset in Json
`JSON.parse("{XXX}")` is faster than `test = {XXX}`


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

**Usefull Features**
- Destruct Object `const { rules, ...otherProps } = this.props;`
- Rename destruct array `const [a1, a2] = [1, 2];`
- Nullish coalescing operator `const test = 0 ?? '-';`
- Optional chaining `const test = {}?.a?.b?.c;`
- Merge unqiue items from arrays `[...new Set([...array1, ...array2])]`


**Frustration**
- Why not support name parameter? `test(name='a', age=3)`
- `const` only works with basic type. like string or number.
- `null` & `undefined`, I get it, but hate it. Python just have None, much easier

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