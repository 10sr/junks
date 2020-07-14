#!/usr/bin/env python3

import json
import sys
from pprint import pprint

with open(sys.argv[1]) as f:
    o = json.load(f)
    pprint(o)
    # print(o["hoehoe"])
