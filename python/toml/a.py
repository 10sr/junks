#!/usr/bin/env python3

from pprint import pprint

import toml

with open("a.toml") as f:
    obj = toml.load(f)

pprint(obj)
