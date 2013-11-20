#!/bin/bash

exec 3<< __EOC__
`cat "$@"`
__EOC__

0<&3 perl -ne 'print $., ",", $_'

exec 3<&-
