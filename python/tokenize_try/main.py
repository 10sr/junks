#!/usr/bin/env python3

import sys
import tokenize

with tokenize.open(sys.argv[1]) as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)
