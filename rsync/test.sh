#!/bin/sh
set -e

# test.sh --- Test the usage of rsync

# basedir="$PWD/rsynctest_base"
basedir="./rsynctest_base"

####################################
# utils

show_dirtree(){
    # http://www.math.kobe-u.ac.jp/~kodama/tips-dirtree.html
    if test -f "$1"
    then
        echo ":: show_dirtree: $1 is a file."
    else
        echo ":: show_dirtree: Dir tree of $1"
        (
            cd "$1" && \
                find . | sort | \
                sed -ne '1b;s/[^\/]*\//+--/g;s/+--+/|  +/g;s/+--+/|  +/g;s/+--|/|  |/g;p'
        )
    fi
}

debug(){
    echo :: "$@"
    "$@"
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

#####################################
# initialization

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

######################################
# tests

test1(){
    # rsync -a dir1 dir2 where dir2 does not exists
    debug rsync -a "$basedir/src" "$basedir/dst1"
}

test1_check(){
    isfile "$basedir/dst1/src/a.txt"
    isfile "$basedir/dst1/src/b.txt"
    isdir "$basedir/dst1/src/d"
    isfile "$basedir/dst1/src/d/b.txt"
    show_dirtree "$basedir/dst1"
}

test2(){
    # rsync -a dir1/ dir2 where dir2 does not exists
    debug rsync -a "$basedir/src/" "$basedir/dst2"
}

test2_check(){
    isfile "$basedir/dst2/a.txt"
    isfile "$basedir/dst2/b.txt"
    isdir "$basedir/dst2/d"
    isfile "$basedir/dst2/d/b.txt"
    show_dirtree "$basedir/dst2"
}

test3(){
    # rsync -a dir1 dir3 where dir3 exists
    debug mkdir -p "$basedir/dst3"
    debug rsync -a "$basedir/src" "$basedir/dst3"
}

test3_check(){
    isfile "$basedir/dst3/src/a.txt"
    isfile "$basedir/dst3/src/b.txt"
    isdir "$basedir/dst3/src/d"
    isfile "$basedir/dst3/src/d/b.txt"
    show_dirtree "$basedir/dst3"
}

test4(){
    # rsync -a dir1/ dir4 where dir4 exists
    debug mkdir -p "$basedir/dst4"
    debug rsync -a "$basedir/src/" "$basedir/dst4"
}

test4_check(){
    isfile "$basedir/dst4/a.txt"
    isfile "$basedir/dst4/b.txt"
    isdir "$basedir/dst4/d"
    isfile "$basedir/dst4/d/b.txt"
    show_dirtree "$basedir/dst4"
}

test5(){
    # rsync -a file path where path not exists
    debug rsync -a "$basedir/src/a.txt" "$basedir/dst5"
}

test5_check(){
    isfile "$basedir/dst5"
    show_dirtree "$basedir/dst5"
}

test6(){
    # rsync -a file path/ where path not exists
    debug rsync -a "$basedir/src/a.txt" "$basedir/dst6/"
}

test6_check(){
    isdir "$basedir/dst6"
    isfile "$basedir/dst6/a.txt"
    show_dirtree "$basedir/dst6"
}

test7(){
    # rsync -a file path/subdir/ where path not exists
    debug rsync -a "$basedir/src/a.txt" "$basedir/dst7/subdir/"
}

test7_check(){
    isdir "$basedir/dst7"
    isfile "$basedir/dst7/subdir/a.txt"
    show_dirtree "$basedir/dst7"
}

test_check(){
    # test_check <num>
    echo "-----test$1-------------------" && \
        test${1} && \
        echo "-----test$1 check-------------" && \
        test${1}_check && \
        echo
}

main(){
    initialize
    test_check 1
    test_check 2
    test_check 3
    test_check 4
    test_check 5
    test_check 6
    test_check 7
}

main
