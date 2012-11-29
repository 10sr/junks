#!/bin/bash

exec 3<< __EOC__
`cat "$@"`
__EOC__

0<&3 cat

exec 3<&-
