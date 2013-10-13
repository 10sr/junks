#!/bin/sh

echo $0

cat <<__EOC__ > $0
`cat $0`
echo abc
__EOC__
echo abc
echo abc
echo abc
echo abc
echo abc
