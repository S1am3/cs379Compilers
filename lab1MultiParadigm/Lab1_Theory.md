# The Compilation vs. Interpretation Dilemma
**C** - Ahead of Time compiled: C code has to be compiled by GCC into an exe before its able to run. The exe turn into machine codes that the cpu can use.<br> **Python** - Interpreted: Python code can be ran by the python interpreter. You don't need to manually compiled it. Its done internally by the python interpreter.<br>**Go** - Ahead of Time compiled: Go is compiled straight to native machine code. The exe also has goroutine scheduler and garbage collector. Go is considered compiled because the human code is compiled into exe before you can run the program.
# Pipeline Tracing

## C
`total = 5 + 3 * 2`<br>
**Pipe**
SOURCE --lex--> TOKENS --parse--> AST --codegen--> BINARY --exec--> CPU

## Python
`total = 5 + 3 * 2`<br>
**Pipe**
SOURCE --lex--> TOKENS --parse--> AST --exec(Statemen #)--> CPU

## diverge 
Both pipelines splits after AST<br>
C: AST -> codegen -> Binary -> Cpu<br>
py:AST -> execute statement -> Cpu

C first compiles the program before executing. Python read and execute the statement during runtime.
# Paradigm Classification

## Imperative
`For every number in a list replace the number with number * number.`
## Object-Oriented
`list.squareEveryNumber()`
## Functional
`for every number in list1 square it and put it in new list2`
## Logic
`if there is a X in the list then y is x * x`

## Stats Cal Class
My **C** code is mainly Imperative becasue it make use of var loops and many step by step instructions to find the calculation.<br>
My **Python** code is also mostly Imperative but I did use the sum() and sorted() function, But the entirety of the program follows step by step instructions.<br>
My **Go** code is Imperative becasue of the use of var loops and step by step instruction to find the calculation.

The Classification does not change just because of a different coding language or the function being used. You can use function like `map` which is functional but use `for` loops to make use of it. Then the overall program is primarily imperative. 

# Startup Latency in the Real World
My start up startup times are Python: 80.72ms, C: 11.50ms, and Go: 14.29ms.<br>
Serverless platform like AWS Lambda historically had a "cold start tax" on interpreted lang like Python it due to how python has to load the interpreter and the program before it can run. While lang that can compile like c and Go already have their executable ready to run. JIT is like the middle approach. It first start interpreting and compile the most used loop into optimized machine code while the program is running. A CubeSat flight Computer would not want JIT due to the its limited computing resources. 

# TABLE
| Lang | Size(byte) | Cold-Start(ms)|
| ----------- | ----------- |-|
| Python | 1381 | 80.67 |
| C | 136106 | 10.62 |
| Go | 2535936 | 13.74 |