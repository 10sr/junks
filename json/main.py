#!/usr/bin/env python3

import json
from pprint import pprint

with open("a.json") as f:
    o = json.load(f)
    pprint(o)
    print(o["hoehoe"])
