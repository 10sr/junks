#!/bin/sh
set -eux

virtualenv=virtualenv
venv_dir=venv
python=python3.5

if ! test -d $venv_dir
then
    $virtualenv $venv_dir -p $python
fi

set +eu
. $venv_dir/bin/activate

exec "$@"
