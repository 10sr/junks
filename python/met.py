#!/usr/bin/env python3

def a(a: int) -> str:
    print(a)
    return f"a: {a}"

a(1)
print(repr(a.__name__))
