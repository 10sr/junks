#!/bin/sh
set -eu

printf "a\nb\nc\n" | while read line
do
    echo data: $line
done

echo AAAAA

printf "a\nb\nc\n" | while read line
do
    echo data: $line
    cat
done

echo AAAAA

printf "a\nb\nc\n" | while read line
do
    echo data: $line
    ssh sakura "echo from sakura: $line"
done

echo AAAAA
for line in a b c
do
    echo data: $line
    ssh sakura "echo from sakura: $line"
done

echo AAAAA
printf "a\nb\nc\n" | while read line
do
    echo data: $line
    ssh sakura "echo from sakura: $line" </dev/null
done
