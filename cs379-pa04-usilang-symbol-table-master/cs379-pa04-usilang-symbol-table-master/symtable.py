"""
PA 4: The USILang Symbol Table -- starter.

Complete Environment and check_program below. See
PA_04_The_USILang_Symbol_Table.md, Part B, for the full requirements.
"""

from typing import Optional

from parser import Assignment, BinOp, Declaration, Number, Program, Variable


class SemanticError(Exception):
    pass



class Environment:
    def __init__(self, parent: Optional["Environment"] = None) -> None:
        self.parent = parent
        self._names: dict = {}  # name -> declaration line, THIS scope only

    def define(self, name: str, line: int) -> None:
        """
        Store name -> line in THIS scope. Raise SemanticError if `name`
        is already defined in THIS scope (not a parent scope --
        shadowing a parent name is allowed).
        """
        # TODO
        if name in self._names:
            oLine = self._names[name]
            raise SemanticError(f"duplicate declaration `{name}` at line {line}, first declard at line {oLine}")
        self._names[name] = line

        
        # raise NotImplementedError

    def resolve(self, name: str) -> int:
        """
        Look up `name` in this scope, then climb `parent` links.
        Return the declaration line, or raise SemanticError if not
        found anywhere in the chain.
        """
        # TODO
        if name in self._names:
            return self._names[name]
        if self.parent is not None:
            return self.parent.resolve(name)
        raise SemanticError('UNDEFINED')
        
        # raise NotImplementedError

def check_expr(expr, env):
    if isinstance(expr, Variable):
        env.resolve(expr.name)
    elif isinstance(expr, Number):
        return
    elif isinstance(expr, BinOp):
        check_expr(expr.left, env)
        check_expr(expr.right, env)




def check_program(ast: Program) -> Environment:
    """
    Walk `ast.statements` in order, using one top-level Environment.
    For a Declaration: resolve every Variable in its expr BEFORE
    defining the new name (so `let x = x;` fails as use-before-decl).
    For an Assignment: resolve the assigned-to name, then resolve
    every Variable in its expr. Errors must surface at the first
    offending statement, not be collected and reported together.
    """
    # TODO
    env = Environment()
    for statement in ast.statements:

        if isinstance(statement, Declaration):
            check_expr(statement.expr, env)
            env.define(statement.name, statement.line)
        elif isinstance(statement, Assignment):
            env.resolve(statement.name)
            check_expr(statement.expr, env)
    return env
    # raise NotImplementedError
