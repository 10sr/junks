#!/bin/bash
set -e

f1(){
    set -e
    echo a
    hoehoe
    echo b
}

if f1
then
    echo Success
else
    echo Fail
fi
