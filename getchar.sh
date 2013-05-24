#!/bin/sh

stty -icanon

echo -n "input: "

key=`dd bs=1 count=1 2>/dev/null`
echo

stty icanon 2>/dev/null

echo key: $key
