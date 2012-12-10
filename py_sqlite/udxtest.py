#!/usr/bin/env python2

# import sqlite3

from random import randint

import sqlite3
import md5

def md5sum(t):
    return md5.md5(str(t)).hexdigest()

con = sqlite3.connect(":memory:")
con.create_function("md5", 1, md5sum)
cur = con.cursor()
cur.execute("select md5(?)", ("foo",))
print cur.fetchone()[0]

con = sqlite3.connect("million.sqlite")
con.create_function("md5", 1, md5sum)
cur = con.cursor()
cur.execute("select md5(t1.data) from t1 limit 10")
print(cur.fetchall())
