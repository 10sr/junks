#!/bin/bash
set -euxo pipefail

git submodule deinit -f ansible/ansible_src
git rm -f ansible/ansible_src
rm -rf .git/modules/ansible/ansible

date >index.html
