#!/bin/bash

sudo=

if [ $# -ne 1 ]; then
    echo "$0 (performance|ondemand)"
    exit 1
fi

govonor=$1

number_of_core=`grep -c 'processor' /proc/cpuinfo`
last_core_id=`expr $number_of_core - 1`

for i in `seq 0 ${last_core_id}`; do
    $sudo cpufreq-set -c $i -g $govonor
done

if [ $govonor = "performance" ]; then
    echo "NEVER forget to set govenor 'ondemand'."
fi
