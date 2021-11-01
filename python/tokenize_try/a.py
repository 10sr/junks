#!/usr/bin/env python3

def f1(a: int) -> int:
    v = a
    for i in range(3):
        v = v + i
    return v


if __name__ == "__main__":
    print(f1(4))
