# Binding Times
(a) Language design time, because the language rules allow names like x to be bounded using keyword "let"\
(b) Run Time, because the storage cell for x is assigned when let get executed.\
(c) Run Time, because 5 get stored when that line get ran.

USILang has no static type declarations, this mean its not type bound. It is determined during the run time based on the thing assigned to it.

# Symbol Table State Tracing
```
let x = 5;              x -> 1
Symbol table
x -> 1


let y = x + 1;          y -> 2
Symbol table
x -> 1
y -> 2

x = y * 2;
Symbol table
x -> 1
y -> 2

let x = 9;              ERROR
ERROR

Symbol table
x -> 1
y -> 2

Semantic Error
x has already been declared
the declared error on line 4(redeclared). references line 1(original)

Sematic Error
duplicate declaration `x` at line 4
first declared at line 1
```

# Syntax Errors vs. Semantic Errors
The parser cannot catch this bug becasue the syntax and grammar is correct. The parser can make assignment without knowing of a var like x has been defined before being called. This is a semantic error(use-before-declaration error). It create symbol table too keep track of the variable that have already been declared. The order matter becasue x needs to be declared before it can be used or called. The parse check for structure will symbol table keep track of declaration order.

# Designing for the Future
Having a parent now mean you don't need to go back and change code that are already in use.