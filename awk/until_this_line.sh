#!/bin/sh

# https://stackoverflow.com/questions/23934486/is-a-start-end-range-expression-ever-useful-in-awk

echo "abc
def
jhi
until-this-line
hoe
fue
hie
" | gawk '!f{print} /until-this-line/{f=1}'
