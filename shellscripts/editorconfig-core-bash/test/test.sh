#!/bin/bash
set -eux

export EDITORCONFIG_CORE_BASH_ASLIB=t

. editorconfig.sh


test `fnmatch` == def
test `main` == def
