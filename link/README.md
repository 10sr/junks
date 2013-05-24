Learning Link
=============

Files to learn dynamic link.


Usage
-----

`make` will create `libmylib.so` from `mylib.c`.
`make 2` will create `libmylib.so` from `mylib2.c`.
In either cases `main` will be created.
`make ldd` will show dynamic linked files from `main`.


What makefile does
------------------

Shared library (with .so suffix) can be create with `gcc -shared` command.
To use dynamic link in programs, use `-l*` option when compiling (use `-L*`
option to add a directory to search *.so files from).


Refs
----

1. [仕事で使える魔法のLAMP（7）：ダイナミックリンクとスタティックリンク - ＠IT](http://www.atmarkit.co.jp/ait/articles/1105/27/news111.html)
1. [Linuxで動的リンクライブラリ（.so）を作成する - 不定期日記](http://blog.livedoor.jp/ha_yshr/archives/51793675.html)
