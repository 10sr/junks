#!/bin/sh

# Copyright (c) 2014, 10sr
# Licensed under GPL

# Alias version of git-snapshot. See comment in a.sh for details about the
# implementation.

git config --local alias.snapshot '! gitdir="`git rev-parse --git-dir`" && export GIT_INDEX_FILE="$gitdir"/snapshot.index && cp "$gitdir"/index "$GIT_INDEX_FILE" && git add -A && : >>"$gitdir"/logs/refs/snapshot && git update-ref refs/snapshot $(git commit-tree $(git write-tree) -m Snapshot -p HEAD)'

# snapshot which utilizes git stash create
# Problem: git stash create do not index untracked files

git config --local alias.stashsnap '! gitdir="`git rev-parse --git-dir`" && : >>"$gitdir"/logs/refs/snapshot && cmt=`git stash create` && test -n "$cmt" && git update-ref refs/snapshot $cmt && echo Snapshot created: $cmt'
