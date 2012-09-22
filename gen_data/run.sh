#!/bin/sh

for i in `seq 100`
do
    ./make_data.sh t1 2>/dev/null | sqlite3 db-large.sqlite
    ./make_data.sh t2 2>/dev/null | sqlite3 db-large.sqlite
    ./make_data.sh t3 2>/dev/null | sqlite3 db-large.sqlite
    echo loop $1 done
done
