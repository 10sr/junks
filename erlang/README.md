Erlang Samples
==============


Basics
-------

To run `square` in `sample.erl`:

    $ erl
    1> c(sample).
    2> sample:square(5).

Press `C-c C-c` to exit the program.


escript example
----------------

Program `ecript` provides an easy way to run erlang programs. This program
compiles given scripts and call `main/1` (which means `main` function with 1
argument).

`escr.erl` is a example for this. Issue `./escr.erl` to try it.
