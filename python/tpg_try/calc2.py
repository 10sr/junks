#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 括弧を理解する電卓パーザで演算の木を作る

import tpg

class Calc(tpg.Parser):
    r"""

	separator space	'\s+';

	token real	'\d+\.\d*|\.?\d+'	float

	token add	'[+-]';
	token mul	'[*/]';

        START/e -> EXPR/e ;

        EXPR/e ->
                TERM/e
		( add/a TERM/t  $ e = [ e, a, t]
		)*
                ;

        TERM/t ->
                FACT/t
		( mul/m FACT/f  $ t = [ t, m, f]
		)*
                ;

        FACT/f ->
                    real/f	$ f = [[], f, []]
                |   '\(' EXPR/f '\)'
                ;

    """

calc = Calc()

while 1:
    expr = input('calc: ')
    if not expr:
        break
    try:
        result = calc(expr)
        print(expr, "=>", result)
    except Exception as e:
        print(expr, ":", e)
