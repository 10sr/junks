j/c/recentf
===========

Record recently `open`ed files.

This library can be referenced as an example to hack the behaivor of system
calls.


Usage
-----

First issue `make`, then type:

    export LD_PRELOAD=$PWD/recentf.so

on your shell to record all files accessed via `open` system call.


Reference
----------

* <http://0xcc.net/unimag/3/index.html>
