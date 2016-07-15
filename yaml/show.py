#!/usr/bin/env python2

import yaml

import sys
import pprint


def main(argv):
    with open(argv[1]) as f:
        d = yaml.load(f.read().decode("utf-8"))
    pprint.pprint(d)
    return 0

sys.exit(main(sys.argv))
