#!/bin/sh -x

for try in "$@"
do
    # main  $try >result.$try.pp.txt
    # main2 $try >result2.$try.pp.txt

    <result.$try.pp.txt  ./output2csv.sh >result.$try.csv
    <result2.$try.pp.txt ./output2csv.sh >result2.$try.csv
done
