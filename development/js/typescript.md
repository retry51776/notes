# Typescript
> 2 way type def: (implicit, explicitly)
> 
> https://www.typescriptlang.org/docs/
> 
# Structure
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


## Scripts
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