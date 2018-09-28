#!/bin/sh
set -eu

for args in "$@"
do
    echo $args
    eval "$args"
done

echo $a
