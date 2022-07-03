# Rust
`cargo build`
Variables Types
https://doc.rust-lang.org/reference/types.html
by default immutable
```
let mut test = "ddd";
let test = Test::new();
run(&test)
```
borrower checker
    - tracking init & moves
    - lifetime inference(garbage collect)
    -  dancling pointers/race conditions

### Compilation Stages
1. Lexical Analysis
   > Convert code to token 
2. Parsing
   > translates to abstract syntax tree

   > convert Higher-level Intermediate Representation

        - Crate
        - Definition
        - Node
          - owner(which crate)

   > Mid-level Intermediate Representation

        - Control Flow Graph
          - Basic Block
          - Statements
          - Terminator


3. Semantic Analysis
4. Optimization
5. Code Generation
    > convert to binary

    > LLVM is collegection small compiler and toolchain technology
```
let y = x; // x's value is removed
let y = &x; // y has x's pointer
```