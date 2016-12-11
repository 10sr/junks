#!/bin/bash
set -eux

export EDITORCONFIG_CORE_BASH_ASLIB=t

. editorconfig.sh


! fnmatch "*.js" "a.js"
! fnmatch "*.js" "aajs"
fnmatch "*.{js,sh}" "a.js"
fnmatch "*.{js,sh}" "a.sh"
fnmatch "*.{j\" \"s,sh}" "a.sh"
! fnmatch "*.{j\" \"s,sh}" "a.j s"
! fnmatch "*.{j\" \"s,sh}" "a.j f"
