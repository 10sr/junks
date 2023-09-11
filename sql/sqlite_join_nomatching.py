#!/usr/bin/env python3

import sqlite3
import sys



def main(argv):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("create table t1 (user varchar, name varchar)")
    cur.execute("INSERT INTO t1 VALUES ('user1', 'User 1')")
    cur.execute("INSERT INTO t1 VALUES ('user2', 'User 2')")
    cur.execute("INSERT INTO t1 VALUES ('user3', 'User 3')")
    for row in cur.execute("select * from t1"):
        print(row)

    cur.execute("create table rel1 (user varchar, org number)")
    cur.execute("INSERT INTO rel1 VALUES ('user1', 1)")
    cur.execute("INSERT INTO rel1 VALUES ('user1', 2)")
    cur.execute("INSERT INTO rel1 VALUES ('user2', 3)")
    for row in cur.execute("select * from rel1"):
        print(row)

    for row in cur.execute("""
    select *
    from t1
    left outer join rel1
    on t1.user = rel1.user
    """):
        print(row)

    for row in cur.execute("""
    select *
    from t1
    left outer join rel1
    on t1.user = rel1.user
    where rel1.org is null
    """):
        print(row)


    return


main(sys.argv)
