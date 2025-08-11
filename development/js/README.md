# JavaScript

## Frustrations

- In the Node.js REPL you cannot import modules directly, which hinders rapid experimentation.

## CommonJS

> Does not work in browsers.

Each file has its own scope, allowing conditional loading.

```js
module.exports = {
  s: 0,
};

exports.x = 1;

if (true) {
  const s = require('./export_file_name');
  console.log(s.x);
}
```

## ES6 Modules

> Supported by most modern browsers.

- Requires the `.js` file extension.  
- Must be imported from a top‑level script.  
- Tree shaking removes unused code during bundling.

```js
// Exporting values
export const s = 0;
export const x = 1;

// Default export (optional)
export default s;

// Importing values
import { s, x } from './export_file_name.js';
```
