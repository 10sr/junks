#!/bin/bash
set -euo pipefail

# Create user John Doe<john.doe@gmail.com>

curl \
    -X POST  \
    -H "Content-Type: application/json" \
    -d '{"email":"john.doe@gmail.com","user_metadata":{},"blocked":false,"email_verified":false,"app_metadata":{},"given_name":"John","family_name":"Doe","name":"John Doe","nickname":"Johnny","picture":"https://secure.gravatar.com/avatar/15626c5e0c749cb912f9d1ad48dba440?s=480&r=pg&d=https%3A%2F%2Fssl.gstatic.com%2Fs2%2Fprofiles%2Fimages%2Fsilhouette80.png","user_id":"abc","connection":"Username-Password-Authentication","password":"'`cat password.secret`'","verify_email":false}' \
    --header "authorization: Bearer `cat token.secret`" \
    https://dev-44517sj.jp.auth0.com/api/v2/users
