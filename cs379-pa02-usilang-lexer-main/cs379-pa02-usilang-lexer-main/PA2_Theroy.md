# Regex Design
```
NUMBER = r"[0-9]+(\.[0-9]+)?"
IDENT = r"[a-zA-Z_][a-zA-Z0-9_]*"
WHITESPACE = r"[ \t]+"
```
Maximal munch is when the lexer pick the longest sequence of char to form a token.
The order matters because when the lexer check letter it stop because it see the keyword lets first. A way to solve this is to match the wide Ident pattern for letter before let

# Hand Tokenization
```
let x = 12 + y3;
(LET,    "let", 1)
(IDENT,  "x",   1)  
(ASSIGN, "=",   1) 
(NUMBER, "12",  1)
(PLUS,   "+",   1)
(IDENT,  "y3",  1) 
(SEMI,   ";",   1)
(EOF,    "",    1)
```

# The Maximal Munch Edge Case
12x split into two token becasue theres no rule in regex saying that number can have char in it. This is dangerous becasue if a programmer make a typo like 12 x it would still be valid until detected during the parse.

# Throughput Reasoning
When ever the lexer recognize a whitespace or a comment it discard them inline during the scan without creating a token obj. This way is more memory effecent then makeing whitespace/comment token.
Rescanning the strings more then once would not be efficent becasue it makes the lexer do more unnecessary work.

