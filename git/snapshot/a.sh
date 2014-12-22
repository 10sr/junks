#!/bin/sh
set -xe

gitdir=`git rev-parse --git-dir`
export GIT_INDEX_FILE=snapshot.index
cp $gitdir/index $GIT_INDEX_FILE
git add -A
tree=`git write-tree`
commit=`git commit-tree $tree -m Snapshot -p HEAD`
: >>$gitdir/logs/refs/snapshot
git update-ref refs/snapshot $commit
