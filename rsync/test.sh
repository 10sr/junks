#!/bin/sh
set -e

# test.sh --- Test the usage of rsync

basedir="$PWD/rsynctest_base"

show_dirtree(){
    # http://www.math.kobe-u.ac.jp/~kodama/tips-dirtree.html
    echo ":: Dir tree of $1"
    (
        cd "$1" && \
        find . | sort | \
        sed -ne '1b;s/[^\/]*\//+--/g;s/+--+/|  +/g;s/+--+/|  +/g;s/+--|/|  |/g;p'
    )
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
    printf "Checking file $1..."
    if test -f "$1"
    then
        echo "passed."
    else
        echo "failed."
        return 1
    fi
}

isdir(){
    printf "Checking dir $1..."
    if test -d "$1"
    then
        echo "passed."
    else
        echo "failed."
        return 1
    fi
}

test1(){
    # rsync -av dir1 dir2 where dir2 does not exists
    rsync -av "$basedir/src" "$basedir/dst1"
}

test1_check(){
    isfile "$basedir/dst1/src/a.txt"
    isfile "$basedir/dst1/src/b.txt"
    isdir "$basedir/dst1/src/d"
    isfile "$basedir/dst1/src/d/b.txt"
}

main(){
    initialize
    test1 && test1_check
}

main
