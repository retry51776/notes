# ES6 Stuff

> I don't keep up with JavaScript much, but I'm sure it will still be around 20 years from now.

## Frustrations

- Why isn’t there named parameters? `test(name='a', age=3)`
- `const` only works for primitive types like strings or numbers.
- The distinction between `null` and `undefined` is confusing; Python’s single `None` feels simpler.
- To store large datasets in JSON, `JSON.parse("{...}")` is faster than assigning an object literal.

## ECMAScript History

- **ES1** (1997)
- **ES2** (1998)
- **ES3** (1999) – try/catch, RegExp
  - ES3.1 – Microsoft‑specific extensions
- **ES5** (2009) – JSON, Array methods, common standard library
- **ES6** (2015) – `for…of`, arrow functions, modules
- **ES7** (2016) – decorators, `includes`
- **ES8** (2017) – async/await
- **ES9** (2018) – spread operator `{...others}`
- **TS** – TypeScript

## Modules

- **CommonJS** – `require` / `exports`
- **ES6 modules** – `import` / `export`

## Callback vs. Promise vs. async/await  

- **Callback** – leads to “callback hell”.
- **Promise** – `new Promise((resolve, reject) => { … })`; chaining with `.then().catch()` can become hard to read.
- **async/await** – cleaner syntax, but still requires proper error handling.

## Useful Features

- Destructuring objects: `const { rules, ...otherProps } = this.props;`
- Renaming array elements: `const [a1, a2] = [1, 2];`
- Nullish coalescing: `const test = 0 ?? '-';`
- Optional chaining: `const test = obj?.a?.b?.c;`
- Merging unique items from arrays: `[...new Set([...array1, ...array2])]`

## ES6 Examples

```js
// Import (ES6)
import getXYZ from 'xyz.js';

// Dynamic import
async function componentDidMount() {
  const { ABC } = await import('./ABC');
  this.setState({ ABC });
}

// CommonJS module export
module.exports = {};
require('./xyz.js');

// Number formatting
(1234.5).toFixed(2);
(1234.5).toLocaleString({
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

// Type checks
Number.isNaN(NaN);
typeof xx === 'boolean';
```

# Buzzwords

- JWT – value‑based token; cookies – reference‑based token
- Import relative paths: <https://youtu.be/shorts/WpgZKBtW_t8>
- JavaScript style guide: <https://github.com/airbnb/javascript/tree/master/react>
- VM … etc.
