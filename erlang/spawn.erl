-module(spawn).
-export([par_func/0, child_f/1]).

child_f(A) ->
    receive
        {From, Str} ->
            io:format("~p ~s~n", [A, Str])
    end.

par_func() ->
    Pid = spawn(spawn, child_f, [1]),
    Pid ! {self(), "abc"}.
