#!/bin/bash
set -euo pipefail

curl \
    --header "authorization: Bearer `cat token.secret`" \
    https://dev-44517sj.jp.auth0.com/api/v2/users
