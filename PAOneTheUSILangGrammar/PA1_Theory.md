# Part A: The Specification

## The Ambiguity Problem
Consider this naive, single-rule grammar for arithmetic expressions
```
<expr> ::= <expr> "+" <expr>
        | <expr> "*" <expr>
        | NUMBER
```
Draw two different, valid parse trees this grammar produces for the string 2 + 3 * 4
```
tree One
2 + (3 * 4)
        
        <expr>
       /  |  \
   <expr> + <expr>
     |      / | \
NUMBER  <expr>*<expr>
     |    |      |
     2  NUMBER NUMBER 
          |      |   
          3      4
Answer = 14

tree Two
(2 + 3) * 4
        
        <expr>
       /  |  \
   <expr> * <expr>
    / | \       |
<expr>+<expr> NUMBER
  |      |      | 
NUMBER NUMBER   4
  |      |
  2      3
Answer = 20    
```
This grammer is bad due to the `<expr>` rule having both "+" and "**" on the same level.<br> This allows `<expr>` to pick either "+" or "*". Due to this it can be grouped up in two different ways adding to different answers.

## The Precedence-Layered Fix
```
<expr>  ::= + -
<term>  ::= * /
<factor>::=Nums parentheses
THREE-LAYER BNF RULE

<expr> ::= <expr> + <term> | <expr> - <term> | <term>
<term> ::= <term> * <factor> | <term> / <factor> | <factor>
<factor> ::= ( <expr> ) | NUMBER
```
It enforce left-associativity for 2 - 3 - 4 because the `<expr>` is on the left side of -, so it has to group left to right of term.

## Leftmost Derivation Trace
```
<expr>
<term>
<term> * <factor>
<factor> * <factor>
(<expr>) * <factor>
(<expr> + <term>) * <factor>
(<term> + <term>) * <factor>
(<factor> + <term>) * <factor>
(5 + <term>) * <factor>
(5 + <factor>) * <factor>
(5 + 2) * <factor>
(5 + 2) * 3
```
`*` sit a the root of the tree. The `+` is on the left of the tree with 5 and 2 while 3 is on the right of `*`.

## Declarations vs. Assignments
```
<declaration> ::= "let" IDENT "=" <expr> ";"
<assignment> ::= IDENT "=" <expr> ";"
```
The first token "let" is enough to indicate declaration, while IDENT indicate assignment.
BNF is not able to reject `let x = 5;, let x = 6;` due to it just checking syntax. It can't keep track of declared var yet. For checking of the var been declared its handled in the symbol table in PA4, of week 5