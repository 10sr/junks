#!/bin/sh

echo "abc
def
jhi
until-this-line
hoe
fue
hie
" | gawk '!f{print} /until-this-line/{f=1}'
