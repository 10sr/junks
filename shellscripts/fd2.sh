#!/bin/bash

exec 3<< __EOC__
`cat "$@"`
__EOC__

<&3 perl -ne 'print $., ",", $_'

exec 3<&-


# not works
# # replace stdout
# exec 4<&1
# <&4 perl -ne 'print $., ",", $_'

# echo abc
# exec 1<&-
