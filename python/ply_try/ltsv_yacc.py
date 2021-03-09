#!/usr/bin/env python3

from dataclasses import dataclass

from ply import lex
from ply import yacc

class _LtsvLexer(object):
    lexer = None

    tokens = (
        "KEY",
        "VALUE",
        "COLON",
        "TAB",
        "NEWLINE",
    )

    t_KEY = r"[a-zA-Z0-9]+"
    t_VALUE = r"[a-zA-Z0-9]+"
    t_COLON = "[:]"
    t_TAB = "[\t]"
    t_NEWLINE = "[\n]"

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        return

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    def __iter__(self):
        return iter(self._lexer)

    def input(self, data):
        self.lexer.input(data)
        return self.lexer


lexer = _LtsvLexer()
lexer.build()
print(list(lexer.input("aaaa\t100:ee\tmomomo:bb\n")))


@dataclass
class Node():
    pass

@dataclass
class Tab(Node):
    v: str

@dataclass
class Field(Node):
    key: str
    sep: str
    value: str


@dataclass
class Pair(Node):
    left: Node
    sep: Node
    right: Node


class LtsvParser():
    def p_statement_line(self, p):
        """line : fields
                  | fields NEWLINE"""
        # discard NEWLINE?
        # output["root"] = p[1]
        p[0] = p[1]
        return

    def p_statement_fields(self, p):
        """fields : field
                    | field TAB fields"""
        if len(p) == 2:
            p[0] = Field(p[1])
        else:
            p[0] = Pair(p[1], p[2], p[3])
        return

    def p_statement_field(self, p):
        "field : KEY COLON VALUE"
        p[0] = Field(p[1], p[2], p[3])
        return

    def p_error(self, p):
        print(f"Syntax error in input! {p}")
        return

    def build(self, **kwargs):
        self.ltsv_lexer = _LtsvLexer()
        self.ltsv_lexer.build()
        self.tokens = self.ltsv_lexer.tokens
        self.parser = yacc.yacc(module=self, **kwargs)
        return

    def parse(self, s):
        return self.parser.parse(s, lexer=self.ltsv_lexer.lexer)


p = LtsvParser()
p.build()
print(p.parse("a:b"))
