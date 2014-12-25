#!/usr/bin/env python2

import sys
import datetime
import json

date = str(datetime.datetime.now())

with open(sys.argv[1]) as f:
    args = f.read()

print(json.dumps({
    "time": date,
    "args": args
}))
