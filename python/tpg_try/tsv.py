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
class Field(Node):
    v: str


@dataclass
class Pair(Node):
    left: Node
    sep: Node
    right: Node


class Tsv(tpg.Parser):
    r"""
    token sep '	' str;
    token field '[a-zA-Z0-9]*' str;

    START/e -> Fields/e;
    Fields/e ->
        Field/e
        (Sep/s Fields/f  $ e = Pair(e, s, f)
        )*
        ;

    Sep/e -> sep/e $ e = Tab(e) $ ;

    Field/e -> field/e $ e = Field(e) $ ;
    """

p = Tsv()
print(p("aaa\tbbb"))
print(p("aaa\tbbb\tccc"))
try:
    print(p("aaa\tbbb\tあ"))
except Exception as e:
    print(e)
