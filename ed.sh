#!/bin/sh

cat <<__EOC__ >edtest.txt
abcde
second line
.
fourth Line
__EOC__

ed edtest.txt <<__EOC__
,n
,s/l/1/g
2p
w
,n
q
__EOC__
