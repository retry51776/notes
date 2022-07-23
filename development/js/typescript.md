# Typescirpt
> 2 way type def: (implict, explicitly)
> 
> https://www.typescriptlang.org/docs/
> 
# Stucture
/tsconfig.config
```js
{
    "compilerOptions": {
        "watch": true
    }
}
```
## CMDs
```bash
tsc index.js
```


## Scipts
```js
type GreetFunction = (a: string |  'hhh') => void;
type CustomType2 = [number?, string?, boolean?, any?];
type CustomType1 = 'yes' | 'no';
let x: CustomType1 = 'yes';

interface Sale {
    id: int,
    amount: number,
    cust: string,
    [key: string]: any
}

const funx = (a: number | null, b: number | string):void => {
    return
}
```