#!/usr/bin/env python2

# http://blog.livedoor.jp/kikwai/archives/51560304.html

class exDict(dict) :
    def __getattr__(self, key) :
        return self[key]

scr = """
from math import pi, e
v1 = "abc"
v2 = "def"

def myprint(str) :
    print("My " + str)
    print("E = {}".format(e))
    return
"""

d = exDict()

exec(scr, d)

print(d.v1, d.v2)
print("PI = {}".format(d.pi))
d.myprint("a")
