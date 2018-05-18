#!/usr/bin/env python3

import yaml

import sys
import pprint


def main(argv):
    with open(argv[1]) as f:
        d = yaml.load(f.read())
    pprint.pprint(d)
    return 0

sys.exit(main(sys.argv))
