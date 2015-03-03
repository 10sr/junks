#!/usr/bin/env php
<?php

$s1 = "abc.php";
$s2 = "abcphp";
$rx = "/\.php$/";
$r1 = preg_replace($rx, "", $s1);
$r2 = preg_replace($rx, "", $s2);

var_dump($r1);
var_dump($r2);


#########################

# multiple lines
$s3 = "abcdef
ghi jil
mmmmmm";

$rx3 = "/.*ghi.*/";

$r3 = preg_replace($rx3, "", $s3);

var_dump($r3);

?>