#!/bin/bash
set -o pipefail
set -x

####
# 1)
# -e 無効・ declare と assign を分ける
set +e

readonly V1
V1=$(false)

echo $V1

####
# 2)
# -e 有効・ declare と assign を一緒にする
set -e

readonly V2=$(false)

echo $V2

####
# 3)
# -e 有効・ declare と assign を分ける
set -e

readonly V3
# ここで `./readonly.sh: line 27: V3: readonly variable` で落ちる
V3=$(false)

echo $V3
