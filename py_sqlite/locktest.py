#!/usr/bin/env python2

import sqlite3

# When select query is being executed on another cursor, the atempt to drop
# that table fails because the table is locked.
# One way to avoid this is to call cur.fetchall()
# Another way is to 'free' cursor, that is, set None to the cursor variable.

conn = sqlite3.connect("million.sqlite")
cur = conn.cursor()

cur.execute("select * from tcopy2 limit 100;")

print(cur.fetchmany(5))

cur = None

cur2 = conn.cursor()

cur2.execute("drop table tcopy2;")

conn.close()
