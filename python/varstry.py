#!/usr/bin/env python3


import os

def main():
    print("{}".format(type(vars(os))))
    for k, v in vars(os).items():
        print("{}: {}".format(k, v))
    return

main()
