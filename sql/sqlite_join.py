#!/usr/bin/env python3

import re
import sqlite3
import sys


# https://stackoverflow.com/questions/5365451/problem-with-regexp-python-and-sqlite
def _udf_regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None


def main(argv):
    conn = sqlite3.connect(":memory:")
    conn.create_function("REGEXP", 2, _udf_regexp)
    cur = conn.cursor()

    cur.execute("create table map1 (re varchar, value varchar)")
    cur.execute("INSERT INTO map1 VALUES ('.*\.txt\Z','text file')")
    cur.execute("INSERT INTO map1 VALUES ('.*\.py\Z','python script')")
    cur.execute("INSERT INTO map1 VALUES ('.*\.tar\.gz\Z','tgz archive')")
    cur.execute("INSERT INTO map1 VALUES ('.*\.gz\Z','gzip compressed')")
    for row in cur.execute("select * from map1"):
        print(row)

    cur.execute("create table data1 (name varchar unique, value varchar)")
    cur.execute("INSERT INTO data1 VALUES ('textfile1','a.txt')")
    cur.execute("INSERT INTO data1 VALUES ('pythonfile1','b.py')")
    cur.execute("INSERT INTO data1 VALUES ('gzcompressed1','b.gz')")
    cur.execute("INSERT INTO data1 VALUES ('tarball1','b.tar.gz')")
    for row in cur.execute("select * from data1"):
        print(row)

    for row in cur.execute("""
    select data1.name, map1.value from data1
    inner join map1
    on data1.value regexp map1.re
    """):
        print(row)

    for row in cur.execute("""
    select data1.name, map1.value from data1
    inner join map1
    on map1.value = (
    select top 1 map1.value
    from map1
    where data1.value regexp map1.re
    )
    """):
        print(row)

    return


main(sys.argv)
