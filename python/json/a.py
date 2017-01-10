#!/usr/bin/env python2

import json
import pprint
import sys

with open(sys.argv[1]) as f:
    obj = json.load(f)
    pprint.pprint(obj)
