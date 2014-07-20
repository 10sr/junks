#!/bin/sh

main(){
    echo $#
}

main                            # -> 0
main a                          # -> 1
main a b                        # -> 2
