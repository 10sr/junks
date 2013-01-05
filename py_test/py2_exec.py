#!/usr/bin/env python2

g = {"a" : "abc"}
l = {}

str = """
print(a)
b = 1
"""

# Both work.

# exec str in g, l
exec(str, g, l)

# print(g)
print(l)
