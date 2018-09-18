#!/bin/sh

echo 'abc,def,ghi
abc,aaa,bbb
hoe,fue,hie' | gawk '$1 ~ /abc/'
