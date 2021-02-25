#!/usr/bin/env python3

from dataclasses import dataclass

import tpg


@dataclass
class Node():
    pass

@dataclass
class Tab(Node):
    v: str

@dataclass
class Key(Node):
    v: str

@dataclass
class Value(Node):
    v: str

@dataclass
class Colon(Node):
    v: str

@dataclass
class Field(Node):
    k: Key
    s: Colon
    v: Value

@dataclass
class Pair(Node):
    left: Node
    sep: Node
    right: Node


class LtsvField2(tpg.Parser):
    r"""

	separator space	'\s+';

	token real	'[a-zA-Z]+'	str

	token colon	':';

        START/e -> EXPR/e ;

        EXPR/e ->
                TERM/e
		( colon/a TERM/t  $ e = Field(e, a, t)
		)*
                ;

        TERM/t ->
                FACT/t
		( colon/m FACT/f  $ t = Field(t, m, f)
		)*
                ;

        FACT/f ->
                    real/f	$ f = Value(f)
                |   '\(' EXPR/f '\)'
                ;

    """

p = LtsvField2()
print(p("a:b:c"))


class LtsvField(tpg.Parser):
    r"""
    token colon ':' str;
    token key '[a-zA-Z]+' str;
    token value '[a-zA-Z]+' str;

    START/e -> FIELD/e;

    FIELD/e ->
        KEY/e
        (VAlUESEP/s VALUE/v  $ e = Field(e, s, v)
        )*
        ;
    KEY/e -> key/e  $ e = Key(e) $ ;
    VAlUESEP/s -> colon/s  $ s = Colon(s) $ ;
    VALUE/v -> value/v $ v = Value(v) $;
    """

p = LtsvField()
print(p("e:f:g"))


class Ltsv(tpg.Parser):
    r"""
    token tab '	' str;
    token colon ':' str;
    token key '[a-zA-Z]*' str;
    token value '[a-zA-Z]*' str;

    START/e -> Fields/e;
    Fields/e ->
        Field/e
        (Fieldsep/s Fields/f  $ e = Pair(e, s, f)
        )*
        ;

    Fieldsep/e -> tab/e $ e = Tab(e) $ ;

    Field/e -> Key/e Valuesep/s Value/v  $ e = Field(e, s, v) $ ;
    Key/e -> key/e  $ e = Key(e) $ ;
    Valuesep/e -> colon/e  $ e = Colon(e) $ ;
    Value/e -> value/e  $ e = Value(e) $ ;
    """


p = Ltsv()
print(p("g:h"))
print(p("aaa:hoe\tbbb:fue"))
print(p("aaa:1\tbbb:2\tccc:100"))
try:
    print(p("aaa\tbbb\tあ"))
except Exception as e:
    print(e)
