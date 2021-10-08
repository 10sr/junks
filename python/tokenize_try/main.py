#!/usr/bin/env python3

import tokenize

with tokenize.open('input.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)
