#!/bin/sh

# open input fd
if test -n "$1"
then
    exec 3<$1
else
    exec 3<&0
fi

while read -r line 0<&3
do
    echo line:$line
done

exec 3<&-

# open output fd
if test -n "$2"
then
    exec 4>$2
else
    exec 4>&1
fi

echo aaa 1>&4

exec 4>&-
