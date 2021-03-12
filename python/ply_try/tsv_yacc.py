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


lexer = lex.lex()

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
class Fields(Node):
    v: list[Field]

    def append(self, n: Field):
        self.v.append(n)
        return

# output = dict()

def p_statement_line(p):
    """line : fields
            | fields NEWLINE"""
    # discard NEWLINE?
    # output["root"] = p[1]
    p[0] = p[1]
    return

def p_statement_fields_1(p):
    """fields : field"""
    p[0] = Fields(list(p[1]))
    return

def p_statement_fields_2(p):
    """fields : field TAB field"""
    p[0] = Fields([p[1], p[3]])
    return

def p_statement_fields_3(p):
    """fields : fields TAB field"""
    p[1].append(p[3])
    p[0] = p[1]
    return

def p_statement_field(p):
    "field : FIELD"
    p[0] = Field(p[1])
    return

def p_error(p):
    print(f"Syntax error in input! {p}")
    return

parser = yacc.yacc()
print(parser.parse("aaa\tbbb", lexer=lexer))
print(parser.parse("aaa\tbbb\tccc", lexer=lexer))
print(parser.parse("aaa\tbbb\tccc\tddd", lexer=lexer))
