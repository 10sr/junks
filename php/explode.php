#!/usr/bin/env php
<?php

$a = explode(" ", "abc def");

var_dump($a);
// array(2) {
//   [0]=>
//   string(3) "abc"
//   [1]=>
//   string(3) "def"
// }

// Get only first element in $a
list($first, ) = $a;
var_dump($first);
// string(3) "abc"

?>
