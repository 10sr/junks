#!/bin/sh

_ask(){
    # _ask msg default
    # _ask use input with prompt MSG
    # DEFAULT must be y or n
    printf "$1 "
    read reply
    test -n "$reply" || reply="$2"
    case $reply in
        y|Y|yes|YES) return 0;;
        n|N|no|NO) return 1;;
        *) return 2;;
    esac
}

if _ask "aha? [y/N]" n
then
    echo yes
else
    echo no
fi
