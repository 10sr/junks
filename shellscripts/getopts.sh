#!/bin/sh

main(){
    unset OPTIND
    echo "***"

    while getopts abcde opt
    do
        case "$opt" in
            a) echo a given; a=1;;
            b) echo b given;;
            c) echo c given;;
            d) echo d given;;
            e) echo e given;;
        esac
    done
    shift `expr $OPTIND - 1`

    echo additional arguments:
    for e in "$@"
    do
        echo $e
    done

    echo "***"
    echo
}

main -abc

main -ab eee

main - -ab

main -- ab
