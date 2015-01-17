#!/bin/sh

# fd3.sh --- fd test 3

# Output:
#     def
# $log_file:
#     abc
#     ghi
#     jkl


log_file=output.fd3.txt

exec 5>&1
exec 1>$log_file
exec 2>&1

stdout(){
    echo "$@"
}

stderr(){
    echo "$@" 1>&2
}

say(){
    echo "$@" 1>&5
}

main(){
    stdout abc
    say def
    stderr ghi
    stdout jkl
}

main
