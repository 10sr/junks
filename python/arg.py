#!/usr/bin/env python3

import argparse
import sys


def main(argv):
    parser = argparse.ArgumentParser(description='Try argparse functionality')

    parser.add_argument('--args',
                        nargs='+',
                        help='multiple args test')

    parser.add_argument("--choices",
                        choices=["a", "b", "c"],
                        help="Arg with choice test")

    args = parser.parse_args(argv[1:])
    print(args)
    return

main(sys.argv)
