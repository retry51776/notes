# TypeScript

> Two ways to define types: implicit and explicit.

## Documentation

<https://www.typescriptlang.org/docs/>

## Project Structure

`tsconfig.json`

```json
{
  "compilerOptions": {
    "watch": true
  }
}
```

## Commands

```bash
tsc index.ts
```

## Example Types

```ts
type GreetFunction = (a: string | 'hhh') => void;
type CustomType2 = [number?, string?, boolean?, any?];
type CustomType1 = 'yes' | 'no';
let x: CustomType1 = 'yes';

interface Sale {
  id: number;
  amount: number;
  cust: string;
  [key: string]: any;
}

const funx = (a: number | null, b: number | string): void => {
  return;
};
```
```