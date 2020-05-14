#!/bin/sh

cat <<__EOC__ | python3 -m tokenize
a = ("a"
     "b")
b = "c" "d"
__EOC__
