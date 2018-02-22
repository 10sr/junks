#!/usr/bin/env python3


def reverse(sec):
    return _reverse([], sec)

def _reverse(ret, rest):
    if not rest:
        return ret
    first = rest[0]
    rest = rest[1:]
    return _reverse([first] + ret, rest)


if __name__ == "__main__":
    print(reverse([1, 2, 3, 45, 6]))
