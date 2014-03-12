#!/bin/bash

# $0 table num

gen_insert_sql(){
    local r=$RANDOM$RANDOM
    local int=$r
    local str=`echo $r | base64`
    echo "INSERT INTO $1 VALUES ($int, \"$str\");"
}

gen_insert_thousand(){
    for i in `seq 1000`
    do
        gen_insert_sql $1
        printf $i\\r\  1>&2
        #{ echo $i | grep '00$' >/dev/null; } && echo "" 1>&2
    done
}

gen_transaction_sql(){
    echo "BEGIN TRANSACTION;"

    for i in `seq $2`
    do
        gen_insert_thousand $1
    done

    echo "COMMIT TRANSACTION;"
}

gen_create_table_sql(){
    echo "CREATE TABLE \"$1\" (id int, str char);"
}

echo_help(){
    echo $1 create tablename
    echo or
    echo $1 tablename num
}

#test $# -eq 2 || exit 1
if test "$1" = create
then
    gen_create_table_sql "$2"
elif test -n "$1"
then
    gen_transaction_sql $1 $2
else
    echo_help $0
fi
