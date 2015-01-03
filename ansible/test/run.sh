#!/bin/sh
set -e

pwd="`dirname "$0"`"
cd "$pwd/.."

git submodule update --init

# Fix for arch linux where python is symlink to python3
find ansible -type f -name '*.py' \
     -exec sed -ie 's|#!/usr/bin/env python|#!/usr/bin/env python2|' {} +
sed -ie 's/python setup.py egg_info/python2 setup.py egg_info/' \
    ansible/hacking/env-setup



# Start test
. ansible/hacking/env-setup

set -x
for f in library/*
do
    python2 ansible/hacking/test-module -m "$f" -a "arg1=true arg2=def"
done
