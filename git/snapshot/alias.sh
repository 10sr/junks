#!/bin/sh

git config --local alias.snapshot '! gitdir="`git rev-parse --git-dir`" && export GIT_INDEX_FILE="$gitdir"/snapshot.index && cp "$gitdir"/index "$GIT_INDEX_FILE" && git add -A && : >>"$gitdir"/logs/refs/snapshot && git update-ref refs/snapshot $(git commit-tree $(git write-tree) -m Snapshot -p HEAD)'
