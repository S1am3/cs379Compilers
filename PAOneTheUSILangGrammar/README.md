# PA 1: The USILang Grammar

Full assignment: `PA_01_The_USILang_Grammar.md`.

## Run
```bash
python validate_bnf.py usilang.bnf
```
Complete `usilang.bnf` (currently a blank skeleton with the 7 required
nonterminal headers). The harness parses your BNF file, checks
structure (every required nonterminal defined and reachable), then
builds a generic backtracking parser directly from your rules and
tests it against valid and invalid USILang snippets. Success Token
prints once every check passes.

Common failure mode: a left-recursive rule (`<expr> ::= <expr> "+" ...`)
will make the harness hang until it hits a recursion-depth guard and
reports "your grammar may be left-recursive" — see Part A, Questions
1-2, for the fix (a right-recursive "tail" helper nonterminal).

## Submit
1. `PA1_Theory.pdf` (or `.md`)
2. `usilang.bnf`
3. The Success Token
