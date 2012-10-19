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
        echo -n $i\  1>&2
        { echo $i | grep '00$' >/dev/null; } && echo "" 1>&2
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

test $# -eq 2 || exit 1
gen_transaction_sql $1 $2
