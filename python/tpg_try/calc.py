#!/usr/bin/env python

import tpg

class Calc(tpg.Parser):
    r"""

	separator space	'\s+';

	token real	'\d+\.\d*|\.\d+'	float
	token integer	'\d+'			long

	token pow	'\*\*';
	token mul	'\*';

        START/e -> EXPR/e ;

        EXPR/e ->
                TERM/e
                (   '\+' TERM/t       $ e += t
                |   '\-' TERM/t       $ e -= t
                )*
                ;

        TERM/t ->
                FACT/t
                (   '\*' FACT/f       $ t *= f
                |   '\/' FACT/f       $ t /= f
                )*
                ;

        FACT/f ->
                    '\-' FACT/f       $ f = -f
                |   POW/f
                ;

        POW/p ->
                ATOM/p
                (   ( '\*\*' | '\^' )
                    FACT/e            $ p **= e
                )?
                ;

        ATOM/a ->
                    integer/a
                |   real/a
                |   '\(' EXPR/a '\)'
                ;

    """

calc = Calc()
while 1:
    expr = input('calc: ')
    if not expr:
        break
    try:
        result = calc(expr)
        print(expr, "=", result)
    except Exception as e:
        print(expr, ":", e)
    print
