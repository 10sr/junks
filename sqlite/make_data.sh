#!/bin/bash

gen_str(){
    echo $RANDOM | base64
}

gen_int(){
    echo $RANDOM
}

gen_insert_sql(){
    echo "INSERT INTO $1 VALUES (`gen_int`, \"`gen_str`\");"
}

gen_transaction_sql(){
    echo "BEGIN TRANSACTION;"

    for i in `seq 10000`
    do
        gen_insert_sql $1
        echo -n $i\  1>&2
        { echo $i | grep '00$' >/dev/null; } && echo "" 1>&2
    done

    echo "COMMIT TRANSACTION;"
}

test -z "$1" && exit 1
gen_transaction_sql $1
