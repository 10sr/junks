#!/bin/sh

# https://stackoverflow.com/questions/23934486/is-a-start-end-range-expression-ever-useful-in-awk
# https://stackoverflow.com/questions/17908555/printing-with-sed-or-awk-a-line-following-a-matching-pattern#17914105

echo "abc
def
jhi
until-this-line
hoe
fue
hie
" | gawk '!f{print} /until-this-line/{f=1}'
