#!/bin/bash
set -euxo pipefail

if [ "$(false | echo 1)" -eq 1 ]
then
    echo true
else
    echo false
fi
