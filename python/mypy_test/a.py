from typing import Any


def f1(a: str) -> str:
    return a + 2

def f2(a: str) -> Any:
    return a + 3

f1("hoe")
f2("fue")
