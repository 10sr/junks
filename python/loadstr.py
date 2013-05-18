#!/usr/bin/env python2

# http://blog.livedoor.jp/kikwai/archives/51560304.html

class exDict(dict):
    def __getattr__(self, key):
        return self[key]

scr = """
from math import pi, e
v1 = "abc"
v2 = "def"

def myintfunc(str):
    print("internal func : " + str)
    return

def myprint(str):
    print("My print : " + str)
    print("E = {}".format(e))
    myintfunc("aa" + str)
    return

fn = {"f1" : myintfunc,         # this line must be after func definition
      "f2" : myprint}

"""

d = exDict()
l = exDict()

exec(scr, d)                    # keyError when use locals arg

print(d.v1 + d.v2)
print("PI = {}".format(d.pi))
d.myprint("a")

d["fn"]["f1"]("astr")

print(d.keys())
