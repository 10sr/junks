#!/usr/bin/env perl

use strict;
use warnings;

my $str = "eicie";
my $crypt = crypt($str, "xx");
print $crypt, "\n";
