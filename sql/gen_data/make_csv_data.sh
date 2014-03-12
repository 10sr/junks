#!/bin/sh

gen_row(){
    local r=$RANDOM$RANDOM
    echo $r\, `echo $r | base64`
}

for j in `seq 1000`
do
    gen_row
done
