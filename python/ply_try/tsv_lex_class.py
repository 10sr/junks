#!/usr/bin/env python3
# https://ply.readthedocs.io/en/latest/ply.html#lex-example
from ply import lex

class TsvLexer(object):
    _lexer = None

    tokens = (
        "FIELD",
        "TAB",
        "NEWLINE",
    )

    t_FIELD = r"[a-zA-Z0-9]+"
    t_TAB = "[\t]"
    t_NEWLINE = "[\n]"

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        return

    # Build the lexer
    def build(self, **kwargs):
        self._lexer = lex.lex(module=self, **kwargs)
        return

    def __iter__(self):
        return iter(self._lexer)

    def input(self, data):
        self._lexer.input(data)
        return self._lexer


lexer = TsvLexer()
lexer.build()
print(list(lexer.input("aaaa\t100\tmomomo\n")))
