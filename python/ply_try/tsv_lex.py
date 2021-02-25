#!/usr/bin/env python3
# https://ply.readthedocs.io/en/latest/ply.html#lex-example

from ply import lex

tokens = (
    "FIELD",
    "TAB",
    "NEWLINE",
)

t_FIELD = r"[a-zA-Z0-9]+"
t_TAB = "[\t]"
t_NEWLINE = "[\n]"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input("a\tb\tc")
print(list(lexer))

lexer.input("aaaa\t100\tmomomo\n")
print(list(lexer))
