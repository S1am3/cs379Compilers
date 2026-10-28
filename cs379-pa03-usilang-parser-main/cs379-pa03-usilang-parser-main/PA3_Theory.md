# Top-Down vs. Bottom-Up
Top Down parsing - start at the top and expand downward. <br>
Bottom Up parsing - start at the input token and goes up toward the start symbol.

Top down builds the parse tree from the root `(<program>)` and works down to the terminals. While Bottom up start at the terminals and go up toward the root.
Recursive decent fit USILang becasue it simple to write read and debug. It also work with the USILang grammar after removing left recursion from PA1
One category of grammar that the recursive decent can not handle is left recursive grammars

# AST and Call-Stack Tracing
```
x = 2 + 3 * 4;
    =
  /   \
 x     +
     /   \
    2     *
        /   \
       3     4

parse_statement
parse_assignment
parse_expr
parse_term
parse_factor
NUMBER("2")
```

# Error Recovery Design
Looking for RPAREN ')' but found SEMI ';' at line # col #
The error should show line and col number and information of what it expect. For example got 'int' but expect 'Char'

# Syntactic vs. Semantic Responsibility
The parser has to make separate declaration and assignment AST nodes because the syntax can determind the difference between let x = 5 and x = 5. The keyword "let" indicate to the parser that it is a declaration, but if its just ident = then it is a assignment.<br>
If the parser collapsed both forms into a single statement pa4 symbol table wouldn't know of it should add the var to symbol table or find the already created var.