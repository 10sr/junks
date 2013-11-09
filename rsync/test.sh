#!/bin/sh
set -e

# test.sh --- Test the usage of rsync

# basedir="$PWD/rsynctest_base"
basedir="./rsynctest_base"

show_dirtree(){
    # http://www.math.kobe-u.ac.jp/~kodama/tips-dirtree.html
    echo ":: Dir tree of $1"
    (
        cd "$1" && \
        find . | sort | \
        sed -ne '1b;s/[^\/]*\//+--/g;s/+--+/|  +/g;s/+--+/|  +/g;s/+--|/|  |/g;p'
    )
}

rsync(){
    echo :: rsync "$@"
    command rsync "$@"
}

initialize(){
    # this create the dir tree like:
    # +--src
    # |  +--a.txt
    # |  +--b.txt
    # |  +--d
    # |  |  +--b.txt

    test -d "$basedir" && rm -r "$basedir"
    mkdir -p "$basedir"
    mkdir "$basedir/src"
    echo a >"$basedir/src/a.txt"
    echo b >"$basedir/src/b.txt"
    mkdir "$basedir/src/d"
    echo c >"$basedir/src/d/b.txt"
    show_dirtree "$basedir/src"
    echo
}

isfile(){
    # printf "Checking file $1..."
    if test -f "$1"
    then
        true
        # echo "passed."
    else
        echo "Checking file $1 failed."
        return 1
    fi
}

isdir(){
    # printf "Checking dir $1..."
    if test -d "$1"
    then
        true
        # echo "passed."
    else
        echo "Checking dir $1 failed."
        return 1
    fi
}

test1(){
    echo "-----test1-------------------"
    # rsync -a dir1 dir2 where dir2 does not exists
    rsync -a "$basedir/src" "$basedir/dst1"
}

test1_check(){
    echo "-----test1 check-------------"
    isfile "$basedir/dst1/src/a.txt"
    isfile "$basedir/dst1/src/b.txt"
    isdir "$basedir/dst1/src/d"
    isfile "$basedir/dst1/src/d/b.txt"
    show_dirtree "$basedir/dst1"
    echo
}

test2(){
    echo "-----test2-------------------"
    # rsync -a dir1/ dir2 where dir2 does not exists
    rsync -a "$basedir/src/" "$basedir/dst2"
}

test2_check(){
    echo "-----test2 check-------------"
    isfile "$basedir/dst2/a.txt"
    isfile "$basedir/dst2/b.txt"
    isdir "$basedir/dst2/d"
    isfile "$basedir/dst2/d/b.txt"
    show_dirtree "$basedir/dst2"
    echo
}

main(){
    initialize
    test1 && test1_check
    test2 && test2_check
}

main