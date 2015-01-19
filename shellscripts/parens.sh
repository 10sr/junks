#!/bin/sh

# parens.sh --- Variable assignment and function call in parenthesis

a=abc

echo $a
# -> abc

(
    a=def
    echo $a
    # -> def
)

# a is restored to abc
echo $a
# -> abc

#####################################

b=123

f1(){
    echo $b
}

f1
# -> 123

(
    # Inside of function, f1 still can be called, yet variables are "local"
    b=456
    f1
    # -> 456
)

f1
# -> 123
