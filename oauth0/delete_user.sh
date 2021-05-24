#!/bin/bash
set -euo pipefail

# Delete user John Doe<john.doe@gmail.com>


curl \
    -X DELETE \
    --header "authorization: Bearer `cat token.secret`" \
    https://dev-44517sj.jp.auth0.com/api/v2/users/auth0%7Cabc
