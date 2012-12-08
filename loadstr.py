#!/usr/bin/env python2

# http://blog.livedoor.jp/kikwai/archives/51560304.html

class exDict(dict) :
    def __getattr__(self, key) :
        return self[key]

scr = """
v1 = "abc"
v2 = "def"

def myprint(str) :
    print("My " + str)
    return
"""

d = exDict()

exec(scr, d)

print(d.v1, d.v2)
d.myprint("a")
