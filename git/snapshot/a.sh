#!/bin/sh
set -xe
# Copyright (c) 2014, 10sr
# Licensed under GPL

# Find current `.git`
# CAUTION: For real cases this value should be quoted
gitdir=`git rev-parse --git-dir`

# Set environment variable that specify the index file
export GIT_INDEX_FILE=$gitdir/snapshot.index

# Copy existing index file
cp $gitdir/index $GIT_INDEX_FILE

# Add all files
git add -A

# Create tree object from the index where all files are registered
tree=`git write-tree`

# Create commit object with the tree object as tree and HEAD as parent
commit=`git commit-tree $tree -m Snapshot -p HEAD`

# Make sure the relog for snapshot is kept
# From git-stash
: >>$gitdir/logs/refs/snapshot

# Update ref to make the snapshot accessible by `refs/snapshot`
git update-ref refs/snapshot $commit
