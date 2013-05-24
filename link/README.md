Learning Link
=============

Files to learn dynamic link.


Usage
-----

First, try `make` and `./main`.

    $ make
    $ ./main
    Hello world!

Then, issue `make 2`.

    $ make 2
    $ ./main
    Hell world!

In this way, you can see that the function of `main` changes *without
re-compiling main.c*.

`make ldd` will show dynamic linked files from `main`.


What makefile does
------------------

### Create .so files

Shared library (with .so suffix) can be create with `gcc -shared` command.
`make` creates `limylib.so` from `mylib.c` and `make 2` creates `libmylib.so`
from `mylib2.c`.

### Use .so files

To use dynamic link in programs, use `-l*` option when compiling (use `-L*`
option to add a directory to search *.so files from).

### PIC (Position Independent Code)

???


Refs
----

1. [仕事で使える魔法のLAMP（7）：ダイナミックリンクとスタティックリンク - ＠IT](http://www.atmarkit.co.jp/ait/articles/1105/27/news111.html)
1. [Linuxで動的リンクライブラリ（.so）を作成する - 不定期日記](http://blog.livedoor.jp/ha_yshr/archives/51793675.html)
1. [Linux の共有ライブラリを作るとき PIC でコンパイルするのはなぜか - bkブログ](http://0xcc.net/blog/archives/000107.html)
