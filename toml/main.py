#!/usr/bin/env python3

import pprint

import toml


with open("a.toml") as f:
    obj = toml.load(f)


pprint.pprint(obj, width=1)
