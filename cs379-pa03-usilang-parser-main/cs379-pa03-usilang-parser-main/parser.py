"""
PA 3: The USILang Parser -- starter.

Complete the parsing functions below. AST node types are already
defined -- do not modify them. See the assignment,
Part B, for the full requirements.
"""

from dataclasses import dataclass, field
from typing import List

from lexer import Token, tokenize


@dataclass
class Program:
    statements: list


@dataclass
class Declaration:
    name: str
    expr: object
    line: int


@dataclass
class Assignment:
    name: str
    expr: object
    line: int


@dataclass
class BinOp:
    op: str
    left: object
    right: object
    line: int


@dataclass
class Number:
    value: int
    line: int


@dataclass
class Variable:
    name: str
    line: int


class ParseError(Exception):
    pass


class _ParserState:
    """Given: a small cursor wrapper over the token list. Not required to use, but handy."""

    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> Token:
        return self.tokens[self.pos]

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def expect(self, type_: str) -> Token:
        tok = self.peek()
        if tok.type != type_:
            raise ParseError(f"Line {tok.line}: expected {type_}, found {tok.type} ({tok.lexeme!r}).")
        return self.advance()


def parse_factor(state: _ParserState):
    # TODO
    if state.peek().type ==  "MINUS":
        token = state.expect("MINUS")
        factor = parse_factor(state)
        return BinOp("-", Number(0, token.line), factor, token.line)
    elif state.peek().type == "LPAREN":
        state.expect("LPAREN")
        expr = parse_expr(state)
        state.expect("RPAREN")
        return expr
    elif state.peek().type == "IDENT":
        token = state.expect("IDENT")
        return Variable(token.lexeme, token.line)
    elif state.peek().type == "NUMBER":
        token = state.expect("NUMBER")
        return Number(int(token.lexeme), token.line)
    else:
        raise ParseError(f"Line {state.peek().line}: expected factor, found {state.peek().type} ({state.peek().lexeme!r})")
    # raise NotImplementedError


def parse_term(state: _ParserState):
    # TODO
    factor = parse_factor(state)
    while state.peek().type in ("STAR", "SLASH"):
        op_token = state.advance()
        right = parse_factor(state)
        factor = BinOp(op_token.lexeme, factor, right, op_token.line)
    return factor
    # raise NotImplementedError


def parse_expr(state: _ParserState):
    # TODO
    term = parse_term(state)
    while state.peek().type in ("PLUS", "MINUS"):
        op_token = state.advance()
        right = parse_term(state)
        term = BinOp(op_token.lexeme, term, right, op_token.line)
    return term
    # raise NotImplementedError


def parse_declaration(state: _ParserState) -> Declaration:
    # TODO
    state.expect("LET")
    n_token = state.expect("IDENT")
    state.expect("ASSIGN")
    expr = parse_expr(state)
    state.expect("SEMI")

    return Declaration(n_token.lexeme, expr, n_token.line)
    # raise NotImplementedError


def parse_assignment(state: _ParserState) -> Assignment:
    # TODO
    n_token = state.expect("IDENT")
    state.expect("ASSIGN")
    expr = parse_expr(state)
    state.expect("SEMI")

    return Assignment(n_token.lexeme, expr, n_token.line)
    # raise NotImplementedError


def parse_statement(state: _ParserState):
    # TODO: peek at state.peek().type to choose declaration vs. assignment
    if state.peek().type == "LET":
        return parse_declaration(state)
    elif state.peek().type == "IDENT":
        return parse_assignment(state)
    else:
        raise ParseError(f"Line {state.peek().line}: expected LET or IDENT, found {state.peek().type} ({state.peek().lexeme!r})")
    # raise NotImplementedError


def parse_program(state: _ParserState) -> Program:
    # TODO: loop parse_statement() until EOF
    st = []

    while state.peek().type != "EOF":
        st.append(parse_statement(state))
    return Program(st)    
    # raise NotImplementedError


def parse(tokens: List[Token]) -> Program:
    state = _ParserState(tokens)
    return parse_program(state)
