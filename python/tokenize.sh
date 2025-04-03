#!/bin/sh

cat <<__EOC__ | python3 -m tokenize
a = ("a"
     "b")
b = "c" "d"
__EOC__

echo ===

cat <<__EOC__ | python3 -m tokenize
n = 1
__EOC__

echo ===

cat <<__EOC__ | python3 -m tokenize
n = 1 + 2
__EOC__
