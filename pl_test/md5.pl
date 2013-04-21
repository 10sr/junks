#!/usr/bin/env perl

use strict;
use warnings;

use Digest::MD5 qw/md5_hex/;

my $str = "aaa";
my $md5ed = md5_hex($str);
print $md5ed, "\n";
