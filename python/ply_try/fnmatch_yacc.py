#!/usr/bin/env python3

from dataclasses import dataclass

from ply import lex
from ply import yacc

class _FnmatchLexer(object):
    lexer = None

    tokens = (
        "BACKSLASH",
        "ASTERISK",
        "LITERAL",
    )

    t_BACKSLASH = r"[\\]"
    t_ASTERISK = r"[*]"
    t_LITERAL = "[a-zA-Z0-9]+"

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


lexer = _FnmatchLexer()
lexer.build()
print(list(lexer.input(r"a*bc\*def")))


@dataclass
class Element():
    pass

@dataclass
class Backslash(Element):
    escaped: Element

@dataclass
class Asterisk(Element):
    pass

@dataclass
class Literal(Element):
    v: str

@dataclass
class Input():
    v: list[Element]

    def append(self, n: Element):
        self.v.append(n)
        return


class FnmatchParser():
    def p_statement_line(self, p):
        """line : elements"""
        p[0] = p[1]
        return

    def p_statement_elements_1(self, p):
        """elements : element"""
        p[0] =  Input([p[1]])
        return

    def p_statement_elements_2(self, p):
        """elements : elements element"""
        p[1].append(p[2])
        p[0] = p[1]
        return

    def p_statement_element_1(self, p):
        """element : LITERAL"""
        p[0] = Literal(p[1])
        return

    def p_statement_element_2(self, p):
        """element : ASTERISK"""
        p[0] = Asterisk()
        return

    # TODO: Support double backslash
    def p_statement_element_3(self, p):
        """element : BACKSLASH element"""
        p[0] = Backslash(p[2])
        return

    def p_error(self, p):
        print(f"Syntax error in input! {p}")
        return

    def build(self, **kwargs):
        self.fnmatch_lexer = _FnmatchLexer()
        self.fnmatch_lexer.build()
        self.tokens = self.fnmatch_lexer.tokens
        self.parser = yacc.yacc(module=self, **kwargs)
        return

    def parse(self, s):
        return self.parser.parse(s, lexer=self.fnmatch_lexer.lexer)


p = FnmatchParser()
p.build()
print(p.parse("a*bc\*def"))
