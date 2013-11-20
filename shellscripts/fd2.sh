#!/bin/bash

exec 3<< __EOC__
`cat "$@"`
__EOC__

<&3 perl -ne 'print $., ",", $_'

exec 3<&-

# # replace stdout
# exec 3<&1
# 0<&3 perl -ne 'print $., ",", $_'

# echo abc
# exec 3<&-
# exec 1<&-
