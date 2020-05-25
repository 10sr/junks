#!/bin/sh
set -eux

for py in *.py
do
    <$py python -m tokenize
done
