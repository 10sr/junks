#!/usr/bin/env python2

"""Measure time of getting sorted rows."""

from __future__ import print_function
import sqlite3
from time import clock

conn = sqlite3.connect("million.sqlite")
print("%f:connected to million.sqlite." % clock())

cur = conn.cursor()
print("%f:get cursor." % clock())

cur.execute("select id from t1 order by id;")
print("%f:execute started."% clock())

for d in cur.fetchmany(10):
    print(d, end="")
print("")

conn.close()
print("%f:closed connection." % clock())
