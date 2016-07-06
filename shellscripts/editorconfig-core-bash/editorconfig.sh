#!/bin/bash
set -ue

fnmatch(){
    echo def
}

main(){
    echo abc
}

if test -z "${EDITORCONFIG_CORE_BASH_ASLIB}"
then
    main "$@"
fi
