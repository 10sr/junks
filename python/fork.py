#!/usr/bin/env python3

import os
from time import sleep

def parent():
    while True:
        print("parent")
        sleep(2)
    return

def child():
    while True:
        print("child")
        sleep(2)
    return

def main():
    pid = os.fork()
    if pid == 0:
        child()
    else:
        parent()
    return

if __name__ == "__main__":
    main()
