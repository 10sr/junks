#!/usr/bin/env python2

import traceback

def func(b):
    if b:
        raise ValueError("failure!")
    return 1


def main():
    r = 0
    try:
        r = 1 + func(True)
    except ValueError as e:
        traceback.print_exc()
        print("TRACEBACK: {}".format(traceback.format_exc()))
        traceback.print_exception(ValueError, e, None)
    return r


if __name__ == "__main__":
    main()
