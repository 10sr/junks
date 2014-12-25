#!/usr/bin/env python2

import sys
import json

with open(sys.argv[1]) as f:
    args = f.read()

print(json.dumps({
    "failed": True,
    "changed": False,
    "msg": args
}))
