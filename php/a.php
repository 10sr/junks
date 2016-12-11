#!/usr/bin/env php
<?php

echo "abc\n";

function foo($arg1) {
    return $arg1 . "hoge";
}

$fooo = foo("fuga");
var_dump($fooo)

?>
