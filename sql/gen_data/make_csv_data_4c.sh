#!/bin/sh

gen_row(){
    local r=$RANDOM$RANDOM
    local s1=`echo $r | base64`
    local s2=`echo $s1 | base64`
    local s3=`echo $s2 | base64`
    echo $r, $s1, $s2, $s3
}

for j in `seq 1000`
do
    gen_row
done
