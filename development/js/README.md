# js

## Frustrate

- in `node` shell, can't import, prevent dynamic development in shell.

## CommonJS
>
> Don't work in browser;
>
> Each file has its own scope; allow conditional loading

```js
module.exports = {
    's': 0
};
exports.x = 1;

if (true) {
    const s = require('./export_file_name')
    console.log(s.x)
}
```

# ES6
>
> most browser supports; must have file extension; must import in root level; tree shackable means only import files you used.

```js
const s = 0,
    x = 1;

export { s, x, } from "./xxx";
export default s;

import { s, x } from './export_file_name.js';
```
