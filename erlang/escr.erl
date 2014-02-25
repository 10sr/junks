#!/usr/bin/env escript

main(A) ->
    [io:format("~s~n", [E]) || E <- A].
