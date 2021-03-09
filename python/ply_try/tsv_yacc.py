#!/usr/bin/env python3
# https://ply.readthedocs.io/en/latest/ply.html#lex-example

from dataclasses import dataclass

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


# Required for yacc to work
_ = lex.lex()

# lexer.input("a\tb\tc")
# print(list(lexer))


from ply import yacc

@dataclass
class Node():
    pass

@dataclass
class Tab(Node):
    v: str

@dataclass
class Field(Node):
    v: str


@dataclass
class Pair(Node):
    left: Node
    sep: Node
    right: Node

output = dict()

def p_statement_line(p):
    """line : fields
              | fields NEWLINE"""
    # discard NEWLINE?
    # output["root"] = p[1]
    p[0] = p[1]
    return

def p_statement_fields(p):
    """fields : field
                | field TAB fields"""
    if len(p) == 2:
        p[0] = Field(p[1])
    else:
        p[0] = Pair(p[1], p[2], p[3])
    return

def p_statement_field(p):
    "field : FIELD"
    p[0] = Field(p[1])
    return

def p_error(p):
    print(f"Syntax error in input! {p}")
    return

parser = yacc.yacc()
print(parser.parse("aaa\tbbb"))
print(parser.parse("aaa\tbbb\txccc"))
