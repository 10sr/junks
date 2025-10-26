#!/bin/bash

python -c 'import ast; print(ast.dump(ast.parse("n = 1")))'
python -c 'import ast; print(ast.dump(ast.parse("n = 1 + 2")))'
