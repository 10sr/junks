#!/usr/bin/env bash
set -eu

file=$0
host=$1

locallines=12

tail -n +$locallines $file | ssh $host "bash -s 2>&1"
exit

# Run on remote host

set -eux
echo hell, world
hostname
