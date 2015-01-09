#!/bin/sh

var1=1

test_equal1(){
    echo equal test 1
    assertEquals 1 $var1
}

test_equal2(){
    echo equal test 2
    assertEquals 2 $var1
}
# Pass as environment variable from makefile?
. $SHUNIT2_MAIN_PATH
