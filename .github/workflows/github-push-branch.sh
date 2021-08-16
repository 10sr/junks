#!/bin/bash
set -euxo pipefail

git submodule deinit -f ansible/ansible_src || true
git rm -f ansible/ansible_src || true
rm -rf .git/modules/ansible/ansible

date >index.html
