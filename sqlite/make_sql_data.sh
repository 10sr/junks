#!/bin/bash

gen_str(){
    echo $RANDOM$RANDOM$RANDOM | base64
}

gen_int(){
    echo $RANDOM$RANDOM
}

gen_insert_sql(){
    local r=$RANDOM$RANDOM
    local int=$r
    local str=`echo $r | base64`
    echo "INSERT INTO $1 VALUES ($int, \"$str\");"
}

gen_transaction_sql(){
    echo "BEGIN TRANSACTION;"

    for i in `seq 1000`
    do
        gen_insert_sql $1
        echo -n $i\  1>&2
        { echo $i | grep '00$' >/dev/null; } && echo "" 1>&2
    done

    echo "COMMIT TRANSACTION;"
}

test -z "$1" && exit 1
gen_transaction_sql $1
