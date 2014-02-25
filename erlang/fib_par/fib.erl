%%#!/usr/bin/env escript

-module(fib).
-export([main/1, fib_par/2, run/1]).

fib_par(Parent, 0) ->
    Parent ! 0;
fib_par(Parent, 1) ->
    Parent ! 1;
fib_par(Parent, N) ->
    spawn(fib, fib_par, [self(), N-1]),
    spawn(fib, fib_par, [self(), N-2]),

    receive
        M ->
            X = M
    end,
    receive
        M ->
            Y = M
    end,

    Parent ! X + Y.



run(N) ->
    spawn(fib, fib_par, [self(), N]),

    receive
        X ->
            io:format("~p", [X]),
            io:nl()
    end.

main(A) ->
    [A1|_] = A,
    N = list_to_integer(A1),
    run(N).
