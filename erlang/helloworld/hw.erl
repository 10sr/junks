% https://erlangcentral.org/wiki/index.php/Hello_World
-module(hw).
-export([start/0]).

start() ->
    io:fwrite("Hell, world!\n").
