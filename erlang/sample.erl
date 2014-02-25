%% Issue `escript <this> [<arg> ...]` to run as script
%% In this way, -module and -export are ignored.

%% module definition `sample'
-module(sample).

%% export functions
-export([square/1, sum/1, main/0, main/1, sum_odd/1, fib/1, if_f/1, case_f/1,
         use_for/0, use_map/0, use_map2/0, list_comp/0, trycatch/0]).

square(X) ->
    X * X.

%% sum(X) ->
%%     if
%%         X == 0 ->
%%             0;
%%         X /= 0 -> X + sum(X-1)
%%     end.

main() ->
    io:format("hell world~n").

main(A) ->
    io:format(A),
    io:nl().


%% use first function that arguments matched
sum([]) ->
    0;
sum([1,2,3]) ->
    io:format("1,2,3!"),
    io:nl(),
    6;
sum([H|T]) ->
    H + sum(T).


%% add only odd numbers
sum_odd([]) ->
    0;
sum_odd([H|T]) when H rem 2 =:= 1 ->
    H + sum_odd(T);
sum_odd([_|T]) ->
    sum_odd(T).

fib(0) ->
    0;
fib(1) ->
    1;
fib(N) ->
    fib(N-1) + fib(N-2).

if_f(X) ->
    io:put_chars(
      if X rem 6 == 0 -> "6\n";
         X rem 3 == 0 -> "3\n";
         X rem 2 == 0 -> "2\n";
	     true         -> "None of them\n"
	  end
     ).

case_f(X) ->
    case X of
        1 ->
            "1";
        2 ->
            "2";
        _ when X rem 2 == 0 ->
            "Many, but even!";
        _ ->
            "Many!"
    end.

for(M, M, F) ->
    %% same number
    [F(M)];
for(I, M, F) ->
    [F(I) | for(I+1, M, F)].

%% fun to use lambda function
use_for() ->
    for(1, 10, fun(I) ->
                       II = I*I, io:format("~p~n", [II]), II end).

use_map() ->
    lists:map(fun(X) ->
                      X * X end, [1,2,3,4,5]).

use_map2() ->
    lists:map(fun square/1, [1,3,5]).

%% list comprehension
list_comp() ->
    [X * X || X <- [1,2,3,4,5], X rem 2 =:= 1].

trycatch() ->
    try
        (1 + a)
    catch _:Reason ->
            io:format("1 + a failed. Reason: ~p~n", [Reason]) end.

