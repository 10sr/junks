#!/bin/bash
set -ue

export LC_ALL=C

fnmatch(){
    # fnmatch PATTERN STRING
    local PAT_REGEXP=`echo "$1" | sed -e 's|*|[^/][^/]*|' | sed -e 's/\./\\\./'`
    eval "for RE in $PAT_REGEXP;
    do
        if expr \"$2\" : \"^\$RE$\" >/dev/null;
        then
            return 0
        fi
    done
    return 1"
}

main(){
    echo abc
}

if test -z "${EDITORCONFIG_CORE_BASH_ASLIB}"
then
    main "$@"
fi
